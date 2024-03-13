![Instance Secret Icon](/resources/instance_secret/instance_secret_icon.svg){ align=left }

# Instance Secret

An Instance Secret is a [DataOS resource](../resources.md) designed for securely storing sensitive information at the instance level. This encompasses items like usernames, passwords, certificates, tokens, and keys.

Instance Secret's significance lies in its ability to provide an instance level security for such confidential information, ensuring that it is safeguarded across the entire DataOS Instance. Consolidating sensitive data at this level, offers convenience and efficiency in managing access and permissions, thereby enhancing overall security measures within the platform.

<aside class="callout">

🗣️ An Instance Secret operates as a DataOS Resource at the <a href="/resources/types_of_dataos_resources/#instance-level-resources">Instance-level</a>, in contrast to a <a href="/resources/secret">Secret Resource </a>, which functions at the <a href="/resources/types_of_dataos_resources/#workspace-level-resources">Workspace-level</a>.

</aside>

<div class="grid cards" markdown>

-   :material-format-list-bulleted-type:{ .lg .middle } **Get Started**

    ---

  

    [:octicons-arrow-right-24: How to create an Instance Secret?](#how-to-create-an-instance-secret)

    [:octicons-arrow-right-24: Validate the Instance Secret.](#validate-the-instance-secret)

    [:octicons-arrow-right-24: Delete the Instance Secret.](#delete-the-instance-secret)

    [:octicons-arrow-right-24: How to integrate Instance Secret into Other Resources?](#how-to-integrate-instance-secret-into-other-resources)



</div>


## How to create an Instance Secret?

To create an Instance Secret Resource in DataOS, ensure you have access to the [DataOS Command Line Interface (CLI)](../interfaces/cli.md) and the required permissions. Then, follow the provided steps to complete the creation process efficiently and securely.

### **Structure of Instance Secret YAML file**

```yaml
name: {{depotsecret-r}} # Resource name (mandatory)
version: {{v1}} # Manifest version (mandatory)
type: {{instance-secret}} # Resource-type (mandatory)
tags: # Tags (optional)
  - just for practice
description: {{instance secret configuration}} # Description of Resource (optional)
layer: user
instance-secret: # Instance Secret mapping (mandatory)
  type: {{key-value-properties}} # Type of Instance-secret (mandatory)
  acl: {{r|rw}} # Access control list (mandatory)
  data: # Data section mapping (mandatory)
    username: {{iamgroot}}
    password: {{yourpassword}}
```

### **Create an Instance Secret YAML configuration**

Begin by creating a YAML file that will hold the configuration details for your Instance Secret.

### **Resource meta section**

The YAML snippet provided below serves as a reference for the Resource meta section, outlining essential declarations for Instance Secrets. Note that while some attributes are optional, others are mandatory for consistency across all resource types.

```yaml
# Resource meta section
name: {{depotsecret-r}} # Resource name (mandatory)
version: {{v1}} # Manifest version (mandatory)
type: {{resource-type}} # Resource-type (mandatory)
tags: 
  - just for practice # Tags (optional)
description: {{resource description}}
owner: iamgroot
layer: user # Layer (user)
```

### **Instance-Secret specific section**

This section focuses on Instance Secret attributes, outlining essential details such as Instance Secret type, access control list (ACL), and required key-value pairs. Additionally, it allows for the optional inclusion of file paths for manifest files.

```yaml
instance-secret:
  type: {{secret-type}} # Type of Instance-secret (mandatory)
  acl: r|rw # Access control list (mandatory)
  data: # Data section mapping (mandatory)
    key: {{value}}
    key: {{value}}
```

*Demystifying Attribute Configurations: [Details](./instance_secret/instance_secret_attributes.md)*

### **Apply the Instance Secret YAML**

To implement the Instance Secret YAML, you can utilize the [DataOS Command Line Interface (CLI)](../interfaces/cli.md) by explicitly indicating the path to the YAML file. When applying the YAML file, note that Instance Secrets do not require workspace specification. The apply command is as follows:

```bash
dataos-ctl apply -f {{Instance Secret YAML path}} 
```

Example usage:

```bash
dataos-ctl apply -f /home/iamgroot/instanceSecret.yaml 
```

## Validate the Instance Secret

To validate the proper creation of the Instance Secret Resource within the DataOS environment, employ the `get` command. Execute the following command to ascertain the existence and correctness of the Instance Secret Resource:

```bash
dataos-ctl get
```

Example usage:

```bash
dataos-ctl get
```

## Delete the Instance Secret

To remove the Instance Secret Resource from the DataOS environment, utilize the `delete` command within the Command Line Interface (CLI). Execute the following command to initiate the deletion process:

**delete command structure for -t (type) and -n (name)**

```bash
dataos-ctl delete -t {{resource-type}} -n {{resource-name}}
```

Example usage:

```bash
dataos-ctl delete -t instance-secret -n depotSecret-r
```

**delete command structure for -i (identifier)**

```bash
dataos-ctl delete -i {{resource-name:version:resource-type}}
```

Example usage:

```bash
dataos-ctl delete -i depotSecret-r:v1:instance-secret
```

Before you can delete an Instance Secret, you need to make sure there are no other resources still utilizing it. For example, if a Depot has a dependency on an Instance Secret, trying to delete that Instance Secret will cause an error. So, you'll need to remove the Depot first, and then you can delete the Instance Secret. This rule applies to both Instance Secrets and Secrets.

An error will be thrown if any resource has a dependency on Instance Secret as shown below.

Example usage:

```bash
dataos-ctl delete -t instance-secret -n sampleinstsecret
INFO[0000] 🗑 delete...                                  
INFO[0000] 🗑 deleting sampleinstsecret:v1:instance-secret... 
INFO[0001] 🗑 deleting sampleinstsecret:v1:instance-secret...error 
WARN[0001] 🗑 delete...error                             
ERRO[0001] Invalid Parameter - failure deleting instance resource : cannot delete resource, it is a dependency of 'depot:v2alpha:sampleinstdepot'
```

```bash
dataos-ctl delete -t depot -n sampleinstdepot
INFO[0000] 🗑 delete...                                  
INFO[0000] 🗑 deleting sampleinstdepot:depot...nothing   
INFO[0000] 🗑 delete...complete
```

```bash
dataos-ctl delete -t instance-secret -n sampleinstsecret
INFO[0000] 🗑 delete...                                  
INFO[0000] 🗑 deleting sampleinstsecret:instance-secret...nothing 
INFO[0000] 🗑 delete...complete
```

## How to integrate Instance Secret into Other Resources

Integrating Instance Secrets into various resources involves obtaining dynamically generated credentials and updating configurations for secure access. This process enhances security by mitigating risks associated with static credentials and enables fine-grained control over resource access.

### **Referencing Instance Secrets in a Depot**

Create a YAML file for your Depot. In the application spec of your Depot, ensure to incorporate a reference to the Instance Secret to uphold confidentiality and security measures.

**Instance Secret YAML for Depot**

Example usage:

```yaml
name: depotsecret-r # Resource name (mandatory)
version: v1 # Manifest version (mandatory)
type: instance-secret # Resource-type (mandatory)
tags: # Tags (optional)
  - just for practice
description: instance secret configuration # Description of Resource (optional)
layer: user
instance-secret: # Instance Secret mapping (mandatory)
  type: key-value-properties # Type of Instance-secret (mandatory)
  acl: r # Access control list (mandatory)
  data: # Data section mapping (mandatory)
    username: iamgroot
    password: yourpassword
```
<aside class="callout">

🗣️ To ensure controlled access for read-write, it is essential to create two Instance Secrets: one with acl:r for read-only access and another with acl:rw for both read and write access and refer to both Instance-Secrets in a Depot. This enables precise management of permissions for different levels of access.

</aside>


**Depot YAML using Instance Secret**

Example usage:

??? tip "Instance Secret referencing in Depot YAML"

    ```yaml

    name: depotsecret
    version: v2alpha
    type: depot
    tags:
      - snowflake
      - depot
    layer: user
    depot:
      type: SNOWFLAKE
      description: testing instance secrets using snowflake depot
    snowflake:
      warehouse: compute_WH
      url: nhjjsf.central-india.azure.snowflakecomputing.com
      database: mydatabase
    external: true
    secrets:
      - name: depotsecret-r
         keys:
           - depotsecret-r

    ```

Expected output:

```bash
$ dataos-ctl apply -f /home/shraddhaade/YAMLS/istest.yaml
INFO[0000] 🛠 apply...                                   
INFO[0000] 🔧 applying depotsecret-r:v1:instance-secret... 
INFO[0004] 🔧 applying depotsecret-r:v1:instance-secret...created 
INFO[0004] 🛠 apply...complete
```

*Know more about Depot: [Depot](./depot00.md)*

### **Referencing Instance Secrets in a Workflow**

Create a YAML file for your Workflow. In the application spec of your Workflow, ensure to incorporate a reference to the Instance Secret to uphold confidentiality and security measures.

**Instance Secret YAML for Workflow**

Example usage:

```yaml
# Resource meta section
name: inst-secret-cli
version: v1
type: instance-secret
layer: user

# Instance-secret specific section
instance-secret:
  type: key-value
  acl: rw
  data:
    USER_ID: iamgroot
    APIKEY: dG9rZW5fdG90YWxseZhZDctYWE4MC00Mzk0LWI0MTct
```

**Workflow** **YAML using Instance Secret**

Example usage:

```yaml
# Resource meta section
name: cli-workflow
version: v1
type: workflow

# Workflow-specific section
workflow:
  dag:

# First Job
  - name: create-volume
    spec:
      stack: dataos-ctl # dataos-ctl stack name
      compute: runnable-default

        # Referred Instance secrets 
      dataosSecrets:
      - name: inst-secret-cli # Instance secret name same as declared above
        allKeys: true
        consumptionType: envVars

      secrets:
      - name: inst-secret-cli # Instance secret name same as declared above
        keys: 
         - inst-secret-cli-rw

        # Stack-specific section
      stackSpec:
        arguments:
        - resource
        - apply
        - -f
        - /etc/dataos/config/manifest.yaml
        - -w
        - ${CURRENT_WORKSPACE}

        # Manifest for the Resource against which the above command is executed
        manifest:
          version: v1beta
          name: "temp001"
          type: volume
          volume:
            size: 1Gi
            accessMode: ReadWriteMany
            type: temp

# Second Job
  - name: get-volume
    spec:
      stack: dataos-ctl
      compute: runnable-default

        # Referred Instance secrets 
      dataosSecrets:
      - name: inst-secret-cli
        allKeys: true
        consumptionType: envVars

        # Stack-specific section
      stackSpec:
        arguments:
        - resource
        - get
        - -t
        - volume
        - -n
        - temp001
        - -w
        - ${CURRENT_WORKSPACE}
    dependencies:
    - create-volume # Second Job dependent on successful execution of First Job
```

*Know more about Workflow: [Workflow](./workflow.md)*

### **Referencing Instance Secrets in a Service**

Create a YAML file for your Service Workflow. In the application spec of your Service Workflow, ensure to incorporate a reference to the Instance Secret to uphold confidentiality and security measures.

**Service** **Workflow** **YAML using Instance Secret**

Example usage:

```yaml
version: v1
name: dataos-ctl-service-workflow
type: workflow
workflow:
  dag:
  - name: create-service
    spec:
      stack: dataos-ctl
      compute: runnable-default
      dataosSecrets:
      - name: dataos-ctl-user-apikey
        allKeys: true
        consumptionType: envVars
      stackSpec:
        arguments:
        - resource
        - apply
        - -f
        - /etc/dataos/config/manifest.yaml
        - -w
        - ${CURRENT_WORKSPACE}
        manifest:
          version: v1
          name: random-user
          type: service
          tags:
            - service
          description: Random User
          service:
            title: Test  API
            replicas: 1
            servicePort: 9876
            compute: runnable-default
            resources:
              requests:
                cpu: 100m
                memory: 128Mi
              limits:
                cpu: 1000m
                memory: 1024Mi
            ingress:
              enabled: true
              path: /random-user
              noAuthentication: true
              annotations:
                konghq.com/strip-path: "false"
                kubernetes.io/ingress.class: kong
            stack: benthos:3.0
            logLevel: DEBUG
            tags:
              - service
              - random-user
            stackSpec:
              input:
                  http_client:
                    url: https://randomuser.me/api/
                    verb: GET
                    headers:
                      Content-Type: application/octet-stream

              pipeline:
                processors:

                  - bloblang: meta status_code = 200

                  - log:
                      level: DEBUG
                      message: "received message: ${!meta()}"

                  - bloblang: |
                      root.id = uuid_v4()
                      root.title = this.results.0.name.title.or("")
                      root.first_name = this.results.0.name.first.or("")
                      root.last_name = this.results.0.name.last.("")
                      root.gender = this.results.0.gender.or("")
                      root.email = this.results.0.email.or("")
                      root.city = this.results.0.location.city.or("")
                      root.state = this.results.0.location.state.or("")
                      root.country = this.results.0.location.country.or("")
                      root.postcode = this.results.0.location.postcode.or("").string()
                      root.age = this.results.0.age.or("").string()
                      root.phone = this.results.0.phone.or("").string()
                  - log:
                      level: INFO
                      message: 'payload: ${! json() }'

              output:
                broker:
                  outputs:
                    - broker:
                        pattern: fan_out
                        outputs:
                          - stdout: {}
                          - type: dataos_depot
                            plugin:
                              address: dataos://fastbase:default/random_users_test_01
                              metadata:
                                auth:
                                  token:
                                    enabled: true
                                description: Audit receiver Service
                                format: AVRO
                                schema: "{\"type\":\"record\",\"name\":\"default\",\"namespace\":\"defaultNamespace\",\"fields\":[{\"name\":\"id\",\"type\":\"string\"},{\"name\":\"title\",\"type\":\"string\"},{\"name\":\"first_name\",\"type\":\"string\"},{\"name\":\"last_name\",\"type\":\"string\"}, {\"name\":\"gender\",\"type\":\"string\"},{\"name\":\"email\",\"type\":\"string\"},{\"name\":\"city\",\"type\":\"string\"},{\"name\":\"state\",\"type\":\"string\"},{\"name\":\"country\",\"type\":\"string\"},{\"name\":\"postcode\",\"type\":\"string\"},{\"name\":\"age\",\"type\":\"string\"},{\"name\":\"phone\",\"type\":\"string\"}]}"
                                schemaLocation: http://registry.url/schemas/ids/11
                                title: Random Uses Info
                                tls:
                                  enabled: true
                                  tls_allow_insecure_connection: true
                                  tls_validate_hostname: false
                                type: STREAM
  - name: get-service-runtime
    spec:
      stack: dataos-ctl
      compute: runnable-default
      dataosSecrets:
      - name: dataos-ctl-user-apikey
        allKeys: true
        consumptionType: envVars
      stackSpec:
        arguments:
        - resource
        - get
        - -t
        - service
        - -n
        - random-user
        - runtime
        - -w
        - ${CURRENT_WORKSPACE}
    dependencies:
    - create-service
```

*Know more about Service: [Service](./service.md)*

## Instance Secret Templates

<div class="grid" markdown>

=== "Object Store"

    === "ABFSS"

        To create an instance-secret for securely accessing ABFSS, the following details are required:

          - `${abfss-depot-name}`: Define the name of your ABFSS depot using the format `${lakehouse-name}0${workspace-name}0storage`. For instance, if your `${lakehouse-name}` is alpha and `${workspace-name}` is testing and the `acl`(access control list) is `rw`, then the instance secret name will be `alpha0testing0storage`.
          - `${description}`: Provide a brief description of the instance-secret's purpose. This field is optional but recommended for easier management and identification of instance-secrets.
          - `${azure-endpoint-suffix}`: The endpoint suffix for your Azure storage account, which varies by cloud environment. 
          - `${azure-storage-account-key}`: The access key for your Azure storage account. This key is essential for authentication and must be kept secure.
          - `${azure-storage-account-name}`: The name of your Azure storage account. This name is used in conjunction with the endpoint suffix to form the base URL for your ABFSS resources.
    
        Ensure that you replace each placeholder (e.g., `${abfss-depot-name}`, `${azure-endpoint-suffix}`) with the actual values pertaining to your Azure account and ABFSS configuration. 

        === "Read-only instance-secret"
            ```yaml title="instance_secret_abfss_read.yaml"
            --8<-- "examples/resources/lakehouse/abfss/resource_instance_secret_abfss_read.yaml"
            ```
        === "Read-write instance-secret"
            ```yaml title="instance_secret_abfss_read_write.yaml"
            --8<-- "examples/resources/lakehouse/abfss/resource_instance_secret_abfss_read_write.yaml"
            ```

    === "WASBS"

        To create an instance-secret for securely accessing WASBS, the following details are required:

          - `${wasbs-depot-name}`: Define the name of your WASBS depot using the format `${lakehouse-name}0${workspace-name}0storage`. For instance, if your `${lakehouse-name}` is alpha and `${workspace-name}` is testing, then the `${gcs-depot-name}` will be alpha0testing0storage.
          - `${description}`: Provide a brief description of the instance-secret's purpose. This field is optional but recommended for easier management and identification of instance-secrets.
          - `${azure-endpoint-suffix}`: The endpoint suffix for your Azure storage account, which varies by cloud environment. 
          - `${azure-storage-account-key}`: The access key for your Azure storage account. This key is essential for authentication and must be kept secure.
          - `${azure-storage-account-name}`: The name of your Azure storage account. This name is used in conjunction with the endpoint suffix to form the base URL for your WASBS resources.
    
        Ensure that you replace each placeholder (e.g., `${wasbs-depot-name}`, `${azure-endpoint-suffix}`) with the actual values pertaining to your Azure account and WASBS configuration. 

        === "Read-only instance-secret"
            ```yaml title="instance_secret_wasbs_read.yaml"
            --8<-- "examples/resources/lakehouse/wasbs/resource_instance_secret_wasbs_read.yaml"
            ```
        === "Read-write instance-secret"
            ```yaml title="instance_secret_wasbs_read_write.yaml"
            --8<-- "examples/resources/lakehouse/wasbs/resource_instance_secret_wasbs_read_write.yaml"
            ```

    === "GCS"

        To configure your instance-secret maniest for GCS access, you'll need to gather the following details:

          - `${gcs-depot-name}`:  Define the name of your GCS depot using the format `${lakehouse-name}0${workspace-name}0storage`. For instance, if your `${lakehouse-name}` is alpha and `${workspace-name}` is testing, then the `${gcs-depot-name}` will be alpha0testing0storage.
          - `${description}`: Provide a brief description of the instance-secret's purpose. This field is optional but recommended for easier management and identification of instance-secrets.
          - `${project-id}`: The unique identifier of the Google Cloud project that your GCS bucket resides in. You can find this information in the Google Cloud Console under the 'Project Info' section.
          - `${email}`:  The email address associated with the Google Cloud service account that will be used for accessing GCS. This service account should have the necessary permissions to perform operations on the GCS bucket.
          - `${gcskey_json}`: The JSON key file of the Google Cloud service account. This file contains the private key and other credentials that are required for authenticating the service account. It can be obtained by creating a service account key in the Google Cloud Console.

        After collecting the above details, depending on your access needs (read-only or read-write), start with the corresponding YAML template provided below. In the chosen template, replace the placeholders (`${gcs-depot-name}`, `${project-id}`, `${email}`, `${gcskey_json}`, and optionally `${description}`) with the actual values you gathered and save it locally on your system.

        === "Read-only instance-secret"
            ```yaml title="instance_secret_gcs_read.yaml"
            --8<-- "examples/resources/lakehouse/gcs/resource_instance_secret_gcs_read.yaml"
            ```
        === "Read-write instance-secret"
            ```yaml title="instance_secret_gcs_read_write.yaml"
            --8<-- "examples/resources/lakehouse/gcs/resource_instance_secret_gcs_read_write.yaml"
            ```
    === "S3"

        To create an instance-secret for securely accessing Amazon S3, the following details are required:

          - `${s3-depot-name}`: Define the name of your S3 depot using the format `${lakehouse-name}0${workspace-name}0storage`. For instance, if your `${lakehouse-name}` is alpha and `${workspace-name}` is testing, then the `${gcs-depot-name}` will be alpha0testing0storage.
          - `${description}`: Provide a brief description of the instance-secret's purpose. This field is optional but recommended for easier management and identification of instance-secrets.
          - `${access-key-id}`: Your access key ID. This key serves as an identifier for your IAM user or role.
          - `${aws-access-key-id`}: AWS-specific access key ID, required for authenticating requests made to AWS services.
          - `${aws-secret-access-key}`: The secret access key for AWS. It's used in conjunction with the AWS access key ID to sign programmatic requests to AWS.
          - `${secret-key}`: The secret key associated with your access key ID. Together, they authenticate requests to AWS services.
    
        Ensure that you replace each placeholder (e.g., `${depot-name}`, `${accesskeyid}`) with the actual values pertaining to your AWS account and S3 configuration. 

        === "Read-only instance-secret"
            ```yaml title="instance_secret_s3_read.yaml" 
            --8<-- "examples/resources/lakehouse/s3/resource_instance_secret_s3_read.yaml"
            ```
        === "Read-write instance-secret"
            ```yaml title="instance_secret_s3_read_write.yaml"
            --8<-- "examples/resources/lakehouse/s3/resource_instance_secret_s3_read_write.yaml"
            ```

=== "Data Warehouse"

    === "Bigquery"

        
        === "Read-only instance-secret"
            ```yaml title="instance_secret_s3_read.yaml" 
            --8<-- "examples/resources/instance_secret/bigquery/bigquery.yaml"
            ```
        === "Read-write instance-secret"
            ```yaml title="instance_secret_s3_read_write.yaml"
            --8<-- "examples/resources/lakehouse/s3/resource_instance_secret_s3_read_write.yaml"
            ```
    === "Redshift"
    === "Snowflake"
    === "Synapse"

=== "SQL Database"

    === "MYSQL"
    === "MsSQL"
    === "JDBC"
    === "Oracle"
    === "Postgres"
        
=== "NoSQL Database"

    === "MongoDB"
    === "Elasticsearch"
    === "Opensearch"
        
=== "Streaming"

    === "Pulsar"
    === "Kafka"
    === "Eventhub" 


</div>