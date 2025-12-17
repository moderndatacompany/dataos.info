# Kafka

An Instance Secret for Kafka in DataOS is used to create a Depot Resource that requires secure access to Kafka. The following sections outline the necessary permissions, configurations, and steps required to set up an Instance Secret efficiently.

## Pre-requisites

To create an Instance Secret for securing Kafka credentials, you must have the following information:

<aside class="callout">
🗣️ Note that tags and use cases may have varying access permissions depending on the organization.
</aside>

To create an Instance Secret in DataOS, at least one of the following role tags must be assigned:

- `roles:id:data-dev`

- `roles:id:system-dev`

- `roles:id:user`

    ```bash
        NAME     │     ID      │  TYPE  │        EMAIL         │              TAGS               
    ───────────────┼─────────────┼────────┼──────────────────────┼─────────────────────────────────
    Iamgroot     │   iamgroot  │ person │   iamgroot@tmdc.io   │ roles:id:data-dev,              
                    │             │        │                      │  roles:id:user,                  
                    │             │        │                      │ users:id:iamgroot  
    ```

**Checking Assigned Roles**

Use the following command to verify assigned roles:

```bash
dataos-ctl user get
```

If any required roles are missing, contact a DataOS Operator or submit a Grant Request for role assignment.

Alternatively, if access is managed through use cases, ensure the following use case is assigned:

- **Manage All Instance-level Resources of DataOS in User Layer**

    To validate assigned use cases, refer to the Bifrost Application Use Cases section.

    <center>
    <img src="/resources/instance_secret/usecase2.png" alt="Bifrost Governance" style="width:80rem; border: 1px solid black; padding: 5px;" />
    <figcaption><i>Bifrost Governance</i></figcaption>
    </center>


## Create an Instance Secret for securing Kafka credentials

Kafka is a distributed event streaming platform capable of handling trillions of events a day. To create a Kafka Instance Secret in DataOS, ensure you have access to the DataOS Command Line Interface (CLI) and the required permissions. Follow the steps below to complete the creation process efficiently and securely.

### **Step 1: Create a manifest file**

Begin by creating a manifest file to hold the configuration details for your Kafka Instance Secret. Depending on your access needs (read-only or read-write), start with the corresponding YAML template provided below.

<aside class="callout">
🗣️ Note that for read-write access of an  Instance Secret the user has to create two Instance Secrets one with `acl:r` and other with `acl:rw` with similar names such as `kafka-depot-r` and `kafka-depot-rw`. If a user creates an Instance Secret with only read-write access and does not create a separate read-only Instance Secret, an error will be triggered while applying the Depot manifest file, as shown below.

    ```bash
    dataos-ctl apply -f /home/office/Depots/abc_depot.yaml
    INFO[0000] 🛠 apply...                                   
    INFO[0000] 🔧 applying testdepot:v2alpha:depot...        
    WARN[0000] 🔧 applying testdepot:v2alpha:depot...error   
    ⚠️ Invalid Parameter - failure validating instance resource : invalid depot, missing a secret reference with acl: r
    WARN[0000] 🛠 apply...error                              
    ERRO[0000] failure applying resources
    ```
</aside>

=== "Read-only instance-secret"

    ```yaml 
    # Kafka Read Instance Secret Manifest

    name: ${kafka-depot-name}-r # Name of the instance-secret, indicating it's for read-only access.
    version: v1 # Manifest Version           
    type: instance-secret # Resource-type
    description: ${description} # Optional: Brief description of the instance-secret's purpose.
    layer: user # DataOS Layer
    instance-secret:
      - acl: r
        type: key-value-properties
        data:
          security_protocol: ${{SASL_SSL}} #optional
          sasl_mechanism: ${{sasl_mechanism}} #optional
          trust_store_type: ${{trust_store_type}} #optional
          trust_store_password: ${{trust_store_password}} #optional
          username: ${{username}}
          password: ${{password}}
        files: #optional
          ca_file: "{{Local File path where .pem file is located}}"
          trust_store_file: "{{Local File path where cacerts file is located}}"
 
    ```

=== "Read-write instance-secret"

    ```yaml 
    # Kafka Read-write Instance Secret Manifest
    name: ${kafka-depot-name}-rw # Name of the instance-secret, indicating it's for read-only access.
    version: v1 # Manifest Version           
    type: instance-secret # Resource-type
    description: ${description} # Optional: Brief description of the instance-secret's purpose.
    layer: user # DataOS Layer
    instance-secret:
      - acl: rw
        type: key-value-properties
        data:
          security_protocol: ${{SASL_SSL}} #optional
          sasl_mechanism: ${{sasl_mechanism}} #optional
          trust_store_type: ${{trust_store_type}} #optional
          trust_store_password: ${{trust_store_password}} #optional
          username: ${{username}}
          password: ${{password}}
        files: #optional
          ca_file: "{{Local File path where .pem file is located}}"
          trust_store_file: "{{Local File path where cacerts file is located}}"
    ```




**Resource meta section**

The Kafka manifest includes a Resource meta section with essential metadata attributes common to all Resource types. Some attributes in this section are optional, while others are mandatory. For more details, refer to the [configurations section](/resources/instance_secret/configurations/).

**Instance-secret specific section**

This section focuses on attributes specific to Kafka Instance Secrets. It includes details like:

- `acl: rw`: Specifies the access control level for the Instance Secret. `rw` means the secret is read-write, allowing both retrieval and updates.

- `type: key-value-properties`: Declares the format of the secret, indicating it is composed of key-value pairs.

- `data`: A container that holds sensitive configuration parameters needed for secure authentication.

- `security_protocol: ${{SASL_SSL}}`: Defines the communication protocol to use.

- `SASL_SSL`: Enables SASL authentication over SSL encryption. (Optional)

- `sasl_mechanism: ${{sasl_mechanism}}`: Specifies the SASL mechanism for authentication (e.g., PLAIN, SCRAM-SHA-256). (Optional)

- `trust_store_type: ${{trust_store_type}}`: Indicates the format of the trust store used to validate SSL certificates (e.g., JKS, PKCS12). (Optional)

- `trust_store_password: ${{trust_store_password}}`: Password to unlock the trust store file, allowing access to trusted certificates. (Optional)

- `username: ${{username}}`: The authentication username required to connect to the target system.

- `password: ${{password}}`: The password associated with the Kafka username for authentication.

- `files`: A container specifying paths to local files required for secure connections (e.g., certificates or trust stores).

- `ca_file`: "{{Local File path where .pem file is located}}"
    Path to the Certificate Authority (.pem) file used to verify the server’s SSL certificate. (Optional)

- `trust_store_file`: "{{Local File path where `cacerts` file is located}}"
    Path to the trust store file (e.g., .jks, `cacerts`) that holds trusted certificates for SSL validation. (Optional)

<aside class="callout">
🗣️ Use the above optional TLS-related attributes when your Kafka connection requires encrypted communication and certificate-based authentication.
</aside>

For more information, refer to the [configurations section](/resources/instance_secret/configurations/).

### **Step 2: Apply the manifest**

!!! warning
    If the connection credentials contain special characters such as `@ : / ? # & = + ; % \ ' { } ( ) * $ !`, the `--disable-interpolation` flag must be used when applying `instance-secrets` or `secrets`. This ensures that special characters are retained as-is in the string.

    **Example:**

    ```bash
    dataos-ctl resource apply -f ${{path/to/instance-secret.yml}} --disable-interpolation
    ```


To create the ABFSS Instance Secret within DataOS, use the `apply` command. Since ABFSS Instance Secrets are Instance-level resources, do not specify a workspace while applying the manifest.

=== "Command"

    ```bash
    dataos-ctl resource apply -f ${manifest-file-path}
    ```
=== "Alternative Command"

    ```bash
    dataos-ctl apply -f ${manifest-file-path}
    ```

=== "Example Usage"

    ```bash
    dataos-ctl resource apply -f depot_secret.yaml
    Example usage:
    $ dataos-ctl apply -f depot_secret.yaml
    INFO[0000] 🛠 apply...                                   
    INFO[0000] 🔧 applying depotsecret-r:v1:instance-secret... 
    INFO[0004] 🔧 applying depotsecret-r:v1:instance-secret...created 
    INFO[0004] 🛠 apply...complete
    ```


### **Step 3: Validate the Instance Secret**

To validate the proper creation of the ABFSS Instance Secret in DataOS, use the `get` command.

=== "Command"

    ```bash
    dataos-ctl resource get -t instance-secret
    ```
=== "Expected Output"

    ```bash
    INFO[0000] 🔍 get...                                     
    INFO[0000] 🔍 get...complete                             

            NAME     | VERSION |      TYPE       | WORKSPACE | STATUS |  RUNTIME  |  OWNER             
    -----------------|---------|-----------------|-----------|--------|-----------|------------------------------
         depotsecret | v1      | instance-secret |           | active |           | iamgroot
    ```


To get the list of all the Instance Secret within the DataOS environment execute the following command.

=== "Command"

    ```bash
    dataos-ctl resource get -t instance-secret -a
    ```
=== "Expected Output"

    ```bash
    dataos-ctl resource get -t instance-secret -a
    INFO[0000] 🔍 get...                                     
    INFO[0000] 🔍 get...complete                             

                NAME            | VERSION |      TYPE       | WORKSPACE | STATUS | RUNTIME |         OWNER          
    ----------------------------|---------|-----------------|-----------|--------|---------|------------------------
     abfssv2alpha-r             | v1      | instance-secret |           | active |         | iamgroot       
     abfssv2alpha-rw            | v1      | instance-secret |           | active |         | iamgroot       
     abfsswithoutmetastore-r    | v1      | instance-secret |           | active |         | thisisthor              
     abfsswithoutmetastore-rw   | v1      | instance-secret |           | active |         | thisisthor              

    ```


Alternatively, you can also check on Metis UI by searching the Instance Secret by name.

<center>
<img src="/resources/instance_secret/metis_is.png" alt="Metis UI" style="width:60rem; border: 1px solid black; padding: 5px;" />
<figcaption><i>Metis UI</i></figcaption>
</center>

## Delete the Instance Secret

<aside class="callout">
🗣️ Before you can delete an Instance Secret, you need to make sure there are no other Resources dependent on it. For example, if a Depot has a dependency on an Instance Secret, trying to delete that Instance Secret will cause an error. So, you'll need to remove the Depot first, and then you can delete the Instance Secret. This rule applies to not just Depot, but all dependent Resources, such as Workflow, Service, Worker, etc. The following error will be thrown if any Resource has a dependency on Instance Secret as shown below. Example usage:

    ```bash
    dataos-ctl delete -t instance-secret -n sampleinstsecret
    INFO[0000] 🗑 delete...                                  
    INFO[0000] 🗑 deleting sampleinstsecret:v1:instance-secret... 
    INFO[0001] 🗑 deleting sampleinstsecret:v1:instance-secret...error 
    WARN[0001] 🗑 delete...error                             
    ERRO[0001] Invalid Parameter - failure deleting instance resource : cannot delete resource, it is a dependency of 'depot:v2alpha:sampleinstdepot'
    ```
</aside>


To delete the ABFSS Instance Secret, use one of the following methods:

### **Method 1**

Specify the Resource type and Instance Secret name in the [`delete`](https://dataos.info/interfaces/cli/command_reference/#delete) command.

=== "Command"

    ```bash
    dataos-ctl resource delete -t ${resource-type} -n ${resource-name}
    ```
=== "Alternative Command"

    ```bash
    dataos-ctl delete -t ${resource-type} -n ${resource-name}
    ```
=== "Example Usage" 

    ```bash 
    dataos-ctl resource delete -t instance-secret -n sampleinstsecret
    Expected output:
    dataos-ctl delete -t instance-secret -n sampleinstsecret
    INFO[0000] 🗑 delete...                                  
    INFO[0000] 🗑 deleting sampleinstsecret:instance-secret...deleted
    INFO[0000] 🗑 delete...complete
    ```


### **Method 2**

Copy the Instance Secret name, version, and Resource-type from the output of the [`get`](https://dataos.info/interfaces/cli/command_reference/#get) command separated by '|' enclosed within quotes and use it as a string in the delete command.

=== "Command"

    ```bash
    dataos-ctl resource delete -i "${resource-name|version|resource-type}"
    ```
=== "Alternative Command"

    ```bash
    dataos-ctl delete -i "${resource-name|version|resource-type}"
    ```
=== "Example Usage"

    ```bash
    dataos-ctl delete -i "sfdepot01-r | v1      | instance-secret | public   "
    INFO[0000] 🗑 delete...                                  
    INFO[0000] 🗑 deleting sfdepot01-r:v1:instance-secret... 
    INFO[0000] 🗑 deleting sfdepot01-r:v1:instance-secret...deleted 
    INFO[0000] 🗑 delete...complete            
    ```


### **Method 3**

Specify the path of the manifest file and use the [`delete`](/interfaces/cli/command_reference/#delete) command.

=== "Command"

    ```bash
    dataos-ctl resource delete -f ${manifest-file-path}
    ```
=== "Alternative Command"

    ```bash
    dataos-ctl delete -f ${manifest-file-path}
    ```
=== "Example Usage"

    ```bash
    dataos-ctl delete -f /home/desktop/connect-city/instance_secret.yaml
    Expected output:
    INFO[0000] 🗑 delete...                                  
    INFO[0000] 🗑 deleting sampleinstsecret:instance-secret...deleted
    INFO[0000] 🗑 delete...complete
    ```


