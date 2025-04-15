# Opensearch

## Pre-requisites

To create an Instance Secret for securing OpenSearch credentials, you must have the following information:

### **Access Permissions in DataOS**

<aside class="callout">
🗣️ Note that tags and use cases may have varying access permissions depending on the organization.
</aside>

To create an Instance Secret in DataOS, at least one of the following role tags must be assigned:

- `roles:id:data-dev`

- `roles:id:system-dev`

- `roles:id:user`

    ```bash
        NAME     │     ID      │  TYPE  │        EMAIL         │              TAGS               
    ─────────────┼─────────────┼────────┼──────────────────────┼─────────────────────────────────
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
    <img src="/resources/instance_secret/usecase2.png" alt="Metis UI" style="width:60rem; border: 1px solid black; padding: 5px;" />
    <figcaption><i>Bifrost Governance</i></figcaption>
    </center>

### **Source System Requirements**

- **Username:**- The OpenSearch username used to authenticate access to the OpenSearch instance. This is typically a user-specific or role-based identifier.

- **Password:**- The OpenSearch password corresponding to the username for authentication. You can retrieve it from your OpenSearch configuration or admin settings, depending on how the instance credentials are managed in your organization.

Ensure you have these credentials ready before proceeding with the Instance Secret creation process.

## Create an instance secret for securing OpenSearch credentials

OpenSearch is a distributed search and analytics engine designed to handle large volumes of structured and unstructured data. It is commonly used for log analytics, full-text search, and real-time monitoring applications.

To create an OpenSearch Instance Secret in DataOS, ensure you have access to the DataOS Command Line Interface (CLI) and the necessary permissions. Follow the steps below to complete the creation process efficiently and securely.

### **Step 1: Create a manifest file**

Begin by creating a manifest file to hold the configuration details for your OpenSearch Instance Secret. Below are the templates for the read-only and read-write manifests:

<aside class="callout">
🗣️ Note that for read-write access of an  Instance Secret the user has to create two Instance Secrets one with `acl:r` and other with `acl:rw` with similar names such as `testdepot-r `and` testdepot-rw`. If a user creates an Instance Secret with only read-write access and does not create a separate read-only Instance Secret, an error will be triggered while applying the Depot manifest file, as shown below.

    ```bash
    dataos-ctl apply -f /home/office/Depots/sf_depot.yaml
    INFO[0000] 🛠 apply...                                   
    INFO[0000] 🔧 applying testdepot:v2alpha:depot...        
    WARN[0000] 🔧 applying testdepot:v2alpha:depot...error   
    ⚠️ Invalid Parameter - failure validating instance resource : invalid depot, missing a secret reference with acl: r
    WARN[0000] 🛠 apply...error                              
    ERRO[0000] failure applying resources
    ```
</aside>

=== "Read-only Instance Secret"

    ```yaml
    name: ${opensearch-depot-name}-r # Name of the instance-secret, indicating it's for read-only access.
    version: v1 # Manifest Version           
    type: instance-secret # Resource-type
    description: ${description}   # Optional: Brief description of the instance-secret's purpose.
    layer: user # DataOS Layer                 
    instance-secret:
    type: key-value-properties  # Type of Instance-secret
    acl: r                     # Access control level, set to 'r' for read-only access.
    data:
        username: ${{Opensearch username}}
        password: ${{Opensearch password}}
    ```
=== "Read-write Instance Secret"

    ```yaml
    name: ${opensearch-depot-name}-rw # Name of the instance-secret, indicating it's for read-write access.
    version: v1 # Manifest Version           
    type: instance-secret # Resource-type
    description: ${description}   # Optional: Brief description of the instance-secret's purpose.
    layer: user # DataOS Layer                 
    instance-secret:
    type: key-value-properties  # Type of Instance-secret
    acl: rw                     # Access control level, set to 'rw' for read-write access.
    data:
        username: ${{username}}
        password: ${{password}}
    ```


**Resource meta section**

The Opensearch manifest includes a Resource meta section with essential metadata attributes common to all resource types. Some attributes in this section are optional, while others are mandatory. For more details, refer to the [configurations section](/resources/instance_secret/configurations/).

**Instance-secret specific section**

This section focuses on attributes specific to OpenSearch Instance Secrets. It includes details like:

- `type`: Specifies the Instance Secret type (key-value-properties).

- `acl`: Access control level (read-only or read-write).

- `data`: Contains sensitive information such as Azure endpoint suffix, storage account key, and storage account name.

For more information, refer to the [configurations section](/resources/instance_secret/configurations/).

### **Step 2: Apply the manifest**

To create the OpenSearch Instance Secret within DataOS, use the `apply` command. Since the Instance Secrets are Instance-level resources, do not specify any workspace while applying the manifest.


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

To validate the proper creation of the Instance Secret in DataOS, use the `get` command.


=== "Command"

    ```bash
    dataos-ctl resource get -t instance-secret
    ```
=== "Example Usage"

    ```bash
    INFO[0000] 🔍 get...                                     
    INFO[0000] 🔍 get...complete                             

            NAME     | VERSION |      TYPE       | WORKSPACE | STATUS |  RUNTIME  |  OWNER             
    -----------------|---------|-----------------|-----------|--------|-----------|------------------------------
        depotsecret | v1      | instance-secret |           | active |           | iamgroot
    ```


To get the list of all the Instance Secret within the Dataos environment execute the following command.


=== "Command"

    ```bash
    dataos-ctl resource get -t instance-secret -a
    ```
=== "Example Usage"

    ```bash
    dataos-ctl resource get -t instance-secret -a
    INFO[0000] 🔍 get...                                     
    INFO[0000] 🔍 get...complete                             

                NAME            | VERSION |      TYPE       | WORKSPACE | STATUS | RUNTIME |         OWNER          
    -----------------------------|---------|-----------------|-----------|--------|---------|------------------------
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


To delete an Instance Secret, use one of the following methods:

### **Method 1** 

Specify the Resource type and Instance Secret name in the [`delete`](/interfaces/cli/command_reference/#delete) command.


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

Copy the Instance Secret name, version, and Resource-type from the output of the [`get`](/interfaces/cli/command_reference/#get) command separated by '|' enclosed within quotes and use it as a string in the delete command.


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



