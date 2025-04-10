# Create an Instance Secret for securing AWS CodeCommit credentials

AWS CodeCommit is a central storage location where code, documentation, and related files are managed and versioned. It allows developers to track changes over time, collaborate on code by merging contributions from multiple developers, and maintain a history of modifications.

## Pre-requisites

To create an Instance Secret for securing AWS CodeCommit credentials, you must have the following information:

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
    <img src="/resources/instance_secret/usecase2.png" alt="Metis UI" style="width:60rem; border: 1px solid black; padding: 5px;" />
    <figcaption><i>Bifrost Governance</i></figcaption>
    </center>

### **Source System Requirements**

- **GITSYNC\_USERNAME**: This represents the AWS CodeCommit username required for authentication.

- **GITSYNC\_PASSWORD**: This is the corresponding password or an app password used for authentication.
    These credentials can be obtained from the  AWS CodeCommit settings or provided by an administrator.

Ensure you have these credentials ready before proceeding with the Instance Secret creation process. Follow the steps below to complete the creation process efficiently and securely.

To create a AWS CodeCommit Instance Secret in DataOS, ensure you have access to the DataOS Command Line Interface (CLI) and the required permissions. Follow the steps below to complete the creation process efficiently and securely.

### **Step 1: Create a manifest file**

Begin by creating a manifest file to hold the configuration details for your AWS CodeCommit Instance Secret. Depending on your access needs (read-only or read-write), start with the corresponding YAML template provided below.

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
    name: ${{codecommit-r}}
    version: ${{v1}}
    type: instance-secret
    description: ${{"bitbucket credentials"}}
    layer: ${{user}}
    instance-secret:
    type: ${{key-value}}
    acl: ${{r}}
    data:
        GITSYNC_USERNAME: ${{"iamgroot"}}
        GITSYNC_PASSWORD: ${{"56F4japOhkkQDS3trUnZetFB2J3lnclDPgHThHLto="}}
    ```

=== "Read-only Instance Secret"

    ```yaml
    name: ${{codecommit-rw}}
    version: ${{v1}}
    type: instance-secret
    description: ${{"bitbucket credentials"}}
    layer: ${{user}}
    instance-secret:
    type: ${{key-value}}
    acl: ${{rw}}
    data:
        GITSYNC_USERNAME: ${{"iamgroot"}}
        GITSYNC_PASSWORD: ${{"56F4japOhkkQDS3trUnZsetB2J3lnclDPgHThHLto="}}
    ```


**Resource meta section**

The manifest includes a Resource meta section with essential metadata attributes common to all resource types. Some attributes in this section are optional, while others are mandatory. For more details, refer to the [configurations section](/resources/instance_secret/configurations/).

**Instance-secret specific section**

This section focuses on attributes specific to AWS CodeCommit Instance Secrets. It includes details like:

- `type`: Specifies the Instance Secret type (key-value-properties).

- `acl`: Access control level (read-only or read-write).

- `data`: Contains sensitive information such as Azure endpoint suffix, storage account key, and storage account name.

For more information, refer to the [configurations section](/resources/instance_secret/configurations/).


### **Step 2: Apply the manifest**

To create the AWS CodeCommit Instance Secret within DataOS, use the `apply` command. Since Instance Secrets are Instance-level resources, do not specify a workspace while applying the manifest.


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
    dataos-ctl resource apply -f secret.yaml
    Example usage:
    $ dataos-ctl apply -f secret.yaml
    INFO[0000] 🛠 apply...                                   
    INFO[0000] 🔧 applying codecommit-r:v1:instance-secret... 
    INFO[0004] 🔧 applying codecommit-r:v1:instance-secret...created 
    INFO[0004] 🛠 apply...complete
    ```