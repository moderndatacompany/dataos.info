# Steps to create MongoDB Depot

There are two ways to set up the MongoDB connection: Through `username` and `password`, and certificate authentication. Follow the sections below to create the Depot using both methods.

## Pre-requisites specific to Depot creation

The following are the prerequisites for creating a MongoDB Depot.

- **Tags:** A developer must possess the following tags, which can be obtained from a DataOS operator.

    ```bash
            NAME     │     ID      │  TYPE  │        EMAIL         │              TAGS               
      ───────────────┼─────────────┼────────┼──────────────────────┼─────────────────────────────────
        Iamgroot     │   iamgroot  │ person │   iamgroot@tmdc.io   │ roles:id:data-dev,                            
                     │             │        │                      │ roles:id:user,                  
                     │             │        │                      │ users:id:iamgroot  
    ```

- **Use cases:** Alternatively, instead of assigning tags, a developer can create a Depot if an operator grants them the "Manage All Instance-level Resources of DataOS in the user layer" use case through Bifrost Governance.

    <center>
    <img src="/resources/depot/usecase2.png" alt="Bifrost Governance" style="width:60rem; border: 1px solid black; padding: 5px;" />
    <figcaption><i>Bifrost Governance</i></figcaption>
    </center>

## Pre-requisites specific to the source system

**For username and password authentication:**

1. Obtain the username and password for MongoDB from your organization's database administrator
2. Also, obtain the MongoDB node's details from the database administrator.

**For certificate authentication:**

1. Obtain the username and password for MongoDB from your organization's database administrator.

2. Obtain the MongoDB node's details from the database administrator.

3. Obtain the `.crt` certificate file for the MongoDB connection from the database administrator for creating the Depot through certificate authentication.

4. Java 17 must be installed in your system.

5. Create a Keystore and Truststore file from a `.crt` file. Follow the below steps to create the keystore and trust store files from the `.crt` file.

      - Initialize the Keystore, remember the password you create while initializing the Keystore.

      - Run the following command, to import a certificate (`demo-ssl-public-cert.cert`) into the Java KeyStore with the alias (`moderncert03`). It will create a keystore and trust store files in the JAVA folder.

      ```bash
      sudo  keytool -importcert -alias moderncert03 -keystore $JAVA_HOME/lib/security/cacerts -storepass 123456 -file /Users/iamgroot/office/poc-squad/mongodb-poc/demo-ssl-public-cert.cert
      ```

      - `keystore`: Points to the KeyStore file to update.

      - `importcert`: Specifies the operation of importing a certificate.

      - `alias moderncert03`: Assigns the alias `moderncert03` to the imported certificate.

      - `storepass 123456`: Provide the password for the keystone you created while initializing the keystore.

      - `file`: Specifies the path to the certificate file to import.

### **Steps to create MongoDB Depot through username and password authentication**

This section involves the alternative steps to create a MongoDB  Depot without an Instance Secret.

1. Create a manifest file for Depot containing the following code and update the details.

    ```yaml
    version: ${{v1}} # depot version
    name: ${{"mongodb03"}}
    type: ${{depot}}
    tags:
      - ${{MongoDb}}
      - ${{Sanity}}
    layer: ${{user}}
    depot:
      type: ${{mongodb}}
      description: ${{"MongoDb depot for sanity"}}
      compute: ${{query-default}}
      spec:
        subprotocol: ${{"mongodb"}}
        nodes: ${{["mongodb-tmdc.dataos.info:27017"]}}
        params: 
          tls: ${{false}}
      external: ${{true}}
      connectionSecret:
        - acl: ${{rw}}
          type: ${{key-value-properties}}
          data:
            username: ${{root}}
            password: ${{f5ce9b0d972fd9555560}}
    ```
    To get the details of each attribute, please refer [to this link](/resources/depot/configurations).

2. Apply the Depot manifest file by executing the below command.

    ```bash
    dataos-ctl apply -f /home/office/depots/mongo_depot.yaml
    ```

3. Verify the Depot creation by executing the below command.

    ```bash
    dataos-ctl get -t depot -n mongodb03 -w public
    ```

4. Scan the metadata. By creating and applying the Scanner Workflow by referring to the MongoDB Depot name, you can extract the metadata that can be accessed on the Metis App.

    ```yaml
    version: v1
    name: depotscanner
    type: workflow
    tags:
      - postgres
      - scanner
    description: The job scans schema tables and register metadata
    workflow:
      dag:
        - name: depotjob
          description: The job scans schema from postgres depot tables and register metadata to metis
          spec:
            stack: scanner:2.0
            compute: runnable-default
            stackSpec:
              depot: dataos://mongodb03         # MongoDB depot name
    ```
    To get the details of each attribute, please refer [to this link](/resources/depot/configurations).
   
5. Apply the Scanner Workflow by executing the below command.

    ```yaml
    dataos-ctl apply -f /home/office/workflow/depot_scanner.yaml
    ```

### **Steps to create MongoDB Depot through certificate authentication**

This section involves the alternative steps to create a MongoDB  Depot without an Instance Secret.

1. Create a manifest file for Depot containing the following code and update the details.

    ```yaml
    version: ${{v1}} # depot version
    name: ${{"mongodb"}}
    type: ${{depot}}
    tags:
      - ${{MongoDb}}
      - ${{Sanity}}
    layer: ${{user}}
    depot:
      type: ${{mongodb}}
      description: ${{"MongoDb depot for sanity"}}
      compute: ${{query-default}}
      spec:
        subprotocol: ${{"mongodb"}}
        nodes: ${{["SG-demo-66793.servers.mongodirector.com:27071"]}}
        params: 
          tls: ${{true}}
      external: ${{true}}
      connectionSecret:
        - acl: ${{rw}}
          type: ${{key-value-properties}}
          data:
            username: ${{admin}}
            password: ${{Kl6swyCRLPteqljkdyrf}}
            keyStorePassword: ${{123456}}
            trustStorePassword: ${{123456}}
          files:
            ca_file: ${{mongodb-poc/demo-ssl-public-cert.cert}}
            key_store_file: ${{/Library/Java/JavaVirtualMachines/jdk-22.jdk/Contents/Home/lib/security/cacerts}}
            trust_store_file: ${{/Library/Java/JavaVirtualMachines/jdk-22.jdk/Contents/Home/lib/security/cacerts}}
    ```
    To get the details of each attribute, please refer [to this link](/resources/depot/configurations).
   
2. Apply the Depot manifest file by executing the below command.

    ```bash
    dataos-ctl apply -f /home/office/depots/mongo_depot.yaml
    ```

3. Verify the Depot creation by executing the below command.

    ```bash
    dataos-ctl get -t depot -n mongodb03 -w public
    ```

4. Scan the metadata. By creating and applying the Scanner Workflow by referring to the MongoDB Depot name, you can extract the metadata that can be accessed on the Metis App.

    ```yaml
    version: v1
    name: depotscanner
    type: workflow
    tags:
      - postgres
      - scanner
    description: The job scans schema tables and register metadata
    workflow:
      dag:
        - name: depotjob
          description: The job scans schema from postgres depot tables and register metadata to metis
          spec:
            stack: scanner:2.0
            compute: runnable-default
            stackSpec:
              depot: dataos://mongodb         # MongoDB depot name
    ```
    To get the details of each attribute, please refer [to this link](/resources/depot/configurations).
   
5. Apply the Scanner Workflow by executing the below command.

    ```bash
    dataos-ctl apply -f /home/office/workflow/udscoremongodb.yaml
    ```

### **Steps to create MongoDB Depot through VPCE**

This section involves the alternative steps to create a MongoDB  Depot without an Instance Secret. VPCE-based Depot is similar to certificate authentication Depot just additional parameters have been added that allow connection with VPCs.

1. Create a manifest file for Depot containing the following code and update the details.

    ```yaml
    version: ${{v1}}
    name: ${{"ldmmongodb"}}
    type: ${{depot}}
    tags:
      - ${{Mongodb}}
    layer: ${{user}}
    depot:
      type: ${{mongodb}}
      description: ${{"MongoDb depot for sanity"}}
      compute: ${{query-default}}
      spec:
        subprotocol: ${{"mongodb"}}
        nodes: ${{["SG-demo-664533.servers.mongodirector.com:27071"]}}
        params: 
          tls: ${{true}}
          tlsAllowInvalidHostnames: ${{true}}
          directConnection: ${{true}}
      external: ${{true}}
      secrets:
      connectionSecret:
        - acl: ${{rw}}
          type: ${{key-value-properties}}
          data:
            username: ${{admin}}
            password: ${{Kl6lyCRLPteqljkdyrf}}
            keyStorePassword: ${{changeit}}
            trustStorePassword: ${{changeit}}
          files:
            ca_file: ${{/Users/iamgroot/Downloads/ca-chain-cn-qa.crt}}
            key_store_file: ${{$JAVA_HOME/lib/security/cacerts}}
            trust_store_file: ${{$JAVA_HOME/lib/security/cacerts}}
    ```
    To get the details of each attribute, please refer [to this link](/resources/depot/configurations).
   
1. Apply the Depot manifest file by executing the below command.

    ```bash
    dataos-ctl apply -f /home/office/depots/mongo_depot.yaml
    ```

1. Verify the Depot creation by executing the below command.

    ```bash
    dataos-ctl get -t depot -n mongodb03 -w public
    ```

1. Scan the metadata. By creating and applying the Scanner Workflow by referring to the MongoDB Depot name, you can extract the metadata that can be accessed on the Metis App.

    ```yaml
    version: v1
    name: depotscanner
    type: workflow
    tags:
      - postgres
      - scanner
    description: The job scans schema tables and register metadata
    workflow:
      dag:
        - name: depotjob
          description: The job scans schema from postgres depot tables and register metadata to metis
          spec:
            stack: scanner:2.0
            compute: runnable-default
            stackSpec:
              depot: dataos://mongodb         # MongoDB depot name
    ```
    To get the details of each attribute, please refer [to this link](/resources/depot/configurations).
   
1. Apply the Scanner Workflow by executing the below command.

    ```bash
    dataos-ctl apply -f /home/office/workflow/udscoremongodb.yaml
    ```