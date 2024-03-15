![Instance Secret Icon](/resources/instance_secret/instance_secret_icon.svg){ align=left }

# Instance Secret

An Instance Secret is a [DataOS resource](../resources.md) designed for securely storing sensitive information at the instance level. This encompasses items like usernames, passwords, certificates, tokens, and keys.

Instance Secret's significance lies in its ability to provide an instance level security for such confidential information, ensuring that it is safeguarded across the entire DataOS Instance. Consolidating sensitive data at this level, offers convenience and efficiency in managing access and permissions, thereby enhancing overall security measures within the platform.

<div class="grid cards" markdown>

-   :material-format-list-bulleted-type:{ .lg .middle } **How to create and manage an Instance Secret?**

    ---

    Instance Secrets provide secure storage for sensitive information, reducing exposure risks inherent in embedding such data directly in resource configurations.

    [:octicons-arrow-right-24: Create Instance Secret](/resources/instance_secret/#how-to-create-an-instance-secret)


-   :material-script-text-outline:{ .lg .middle } **How to refer an Instance Secret into other Resources?**

    ---

    An Intsnace Secret manifest file includes resource meta and Secret specific sections with attributes that must be configured for creating a Secret.

    [:octicons-arrow-right-24: Refering Instance Secrets](/resources/instance_secret/#how-to-refer-instance-secret-into-other-resources)



-   :material-clock-fast:{ .lg .middle } **Types of Instance Secrets**

    ---

    DataOS Instance Secret types securely store diverse sensitive data, addressing specific needs like cloud credentials, image pulling, key-value pairs, metadata, and SSL/TLS certificates.

    [:octicons-arrow-right-24: Types](../resources/instance_secret/instance_secret_attributes.md)


-   :material-console:{ .lg .middle } **Instance Secret Template**

    ---

    Instance Secret Resource can be refered into various types of Depots.


    [:octicons-arrow-right-24: Example](/resources/instance_secret/#instance-secret-templates)
</div>



## How to create an Instance Secret?

To create an Instance Secret Resource in DataOS, ensure you have access to the [DataOS Command Line Interface (CLI)](../interfaces/cli.md) and the required permissions. Then, follow the provided steps to complete the creation process efficiently and securely.

### **Structure of Instance Secret YAML file**

The YAML structure for the Instance Secret is outlined as follows:

![Instance Secret YAML Structure](/resources/instance_secret/Slide1.jpg)


### **Create an Instance Secret YAML configuration**

Begin by creating a manifest file that will hold the configuration details for your Instance Secret.
### **Resource meta section**

The Insatnce Secret manifest snippet provided below serves as a reference for the Resource meta section, outlining essential declarations for Instance Secrets. Note that while some attributes are optional, others are mandatory for consistency across all resource types.

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
For more information about the various attributes in Resource meta section, refer to the Attributes of [Resource meta section](../resources/resource_attributes.md).

### **Instance-Secret specific section**

This section focuses on Instance Secret attributes, outlining essential details such as Instance Secret type, access control list (ACL), and required key-value pairs. Additionally, it allows for the optional inclusion of file paths for manifest files.

```yaml
# Instance-secret specific section
instance-secret:
  type: key-value-properties # Type of Instance-secret (mandatory)
  acl: ${{r|rw}} # Access control list (mandatory)
  data: # Data section mapping (mandatory)
    ${{username: iamgroot}}
    ${{password: abcd1234}}
	files: # Manifest file path (optional)
		${{xyz: /home/instance-secret.yaml}}
```

#### **Instance Secret YAML Configuration Fields**

| Field | Data Type | Default Value | Possible Value | Requirement |
| --- | --- | --- | --- | --- |
| [`instance-secret`](./instance_secret/instance_secret_attributes.md#instance-secret) | object | none | none | mandatory |
| [`type`](./instance_secret/instance_secret_attributes.md#instance-secret) | string | none | cloud-kernel, cloud-kernel-image-pull, key-value, key-value-properties, certificates | mandatory |
| [`acl`](./instance_secret/instance_secret_attributes.md#instance-secret) | string | none | r, rw | mandatory |
| [`data`](./instance_secret/instance_secret_attributes.md#instance-secret) | object | none | none | mandatory |
| [`files`](./instance_secret/instance_secret_attributes.md#instance-secret) | string | none | file-path | optional |


For more information about the various attributes in Instance Secret specific section, refer to the Attributes of [Instance Secret specific section](./instance_secret/instance_secret_attributes.md).



### **Apply the Instance Secret YAML**

To implement the Instance Secret YAML, you can utilize the [DataOS Command Line Interface (CLI)](../interfaces/cli.md) by explicitly indicating the path to the YAML file. When applying the YAML file, note that Instance Secrets do not require workspace specification. The apply command is as follows:

=== "Command"
    ```shell
    dataos-ctl apply -f ${path/instance_secret.yaml} -w ${name of the workspace}
    ```
=== "Example Usage"
    ```shell
    dataos-ctl apply -f myinstance_secrets.yaml -w sandbox
    ```

Alternative to the above apply command.

=== "Command"
    ```shell
    dataos-ctl resource apply -f ${path/instance_secret.yaml} -w ${name of the workspace}
    ```
=== "Example Usage"
    ```shell
    dataos-ctl resource apply -f myinstance_secrets.yaml -w sandbox
    ```

## How to manage an Instance-Secret?

### **Validate the Instance Secret**

To validate the proper creation of the Instance Secret Resource within the DataOS environment, employ the `get` command. Execute the following command to ascertain the existence and correctness of the Instance Secret Resource:

=== "Command"

    ```shell
    dataos-ctl get -t instance-secret -w {{workspace}}
    ```

=== "Example Usage"

    ```shell
    dataos-ctl get -t instance-secret -w sandbox
    ```


### **Delete the Instance Secret**

To remove the Instance Secret Resource from the DataOS environment, utilize the `delete` command within the Command Line Interface (CLI). Execute the following command to initiate the deletion process:

**delete command structure for -t (type) and -n (name)**

=== "Command"

    ```shell
    dataos-ctl delete -t {{resource-type}} -n {{resource-name}}
    ```

=== "Example Usage"

    ```shell
    dataos-ctl delete -t instance-secret -n myinstance_secret
    ```


**delete command structure for -i (identifier)**

=== "Command"

    ```shell
    dataos-ctl delete -i {{resource-name:version:resource-type}}
    ```

=== "Example Usage"

    ```shell
    dataos-ctl delete -i myinstance_secret:v1:instance-secret
    ```


Before you can delete an Instance Secret, you need to make sure there are no other resources still utilizing it. For example, if a Depot has a dependency on an Instance Secret, trying to delete that Instance Secret will cause an error. So, you'll need to remove the Depot first, and then you can delete the Instance Secret. This rule applies to both Instance Secrets and Secrets.

An error will be thrown if any resource has a dependency on Instance Secret as shown below.

Example usage:

```shell
dataos-ctl delete -t instance-secret -n sampleinstsecret
INFO[0000] 🗑 delete...                                  
INFO[0000] 🗑 deleting sampleinstsecret:v1:instance-secret... 
INFO[0001] 🗑 deleting sampleinstsecret:v1:instance-secret...error 
WARN[0001] 🗑 delete...error                             
ERRO[0001] Invalid Parameter - failure deleting instance resource : cannot delete resource, it is a dependency of 'depot:v2alpha:sampleinstdepot'
```

```shell
dataos-ctl delete -t depot -n sampleinstdepot
INFO[0000] 🗑 delete...                                  
INFO[0000] 🗑 deleting sampleinstdepot:depot...nothing   
INFO[0000] 🗑 delete...complete
```

```shell
dataos-ctl delete -t instance-secret -n sampleinstsecret
INFO[0000] 🗑 delete...                                  
INFO[0000] 🗑 deleting sampleinstsecret:instance-secret...nothing 
INFO[0000] 🗑 delete...complete
```

## How to refer Instance Secret into Other Resources

Refering Instance Secrets into various resources involves obtaining dynamically generated credentials and updating configurations for secure access. This process enhances security by mitigating risks associated with static credentials and enables fine-grained control over resource access.

**Syntax**
```yaml


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

??? tip "Instance Secret referencing in Depot manifest"

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

??? tip "Instance Secret referencing in Workflow manifest"

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


### **Referencing Instance Secrets in a Service**

Create a YAML file for your Service Workflow. In the application spec of your Service Workflow, ensure to incorporate a reference to the Instance Secret to uphold confidentiality and security measures.

**Service** **Workflow** **YAML using Instance Secret**

Example usage:

??? tip "Instance Secret referencing in Service manifest"

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

    Object stores, such as Azure Blob Storage (WASBS) and Azure Blob File System (ABFSS), are distributed storage systems designed to store and manage large amounts of unstructured data. Instance-Secrets are configured to securely access and interact with the respective object store.

    === "ABFSS"

        To create an instance-secret for securely accessing ABFSS, the following details are required:

          - `name`: Define the name of your ABFSS depot using the format `${lakehouse-name}0${workspace-name}0storage`. For instance, if your `${lakehouse-name}` is alpha and `${workspace-name}` is testing and the `acl`(access control list) is `rw`, then the instance secret name will be `alpha0testing0storage`.
          - `description`: Provide a brief description of the instance-secret's purpose. This field is optional but recommended for easier management and identification of instance-secrets.
          - `azureendpointsuffix`: The endpoint suffix for your Azure storage account, which varies by cloud environment. 
          - `azurestorageaccountkey`: The access key for your Azure storage account. This key is essential for authentication and must be kept secure.
          - `azurestorageaccountname`: The name of your Azure storage account. This name is used in conjunction with the endpoint suffix to form the base URL for your ABFSS resources.
    
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

          - `name`: Define the name of your WASBS depot using the format `${lakehouse-name}0${workspace-name}0storage`. For instance, if your `${lakehouse-name}` is alpha and `${workspace-name}` is testing, then the `${gcs-depot-name}` will be alpha0testing0storage.
          - `description`: Provide a brief description of the instance-secret's purpose. This field is optional but recommended for easier management and identification of instance-secrets.
          - `azureendpointsuffix`: The endpoint suffix for your Azure storage account, which varies by cloud environment. 
          - `azurestorageaccountkey`: The access key for your Azure storage account. This key is essential for authentication and must be kept secure.
          - `azurestorageaccountname`: The name of your Azure storage account. This name is used in conjunction with the endpoint suffix to form the base URL for your WASBS resources.
    
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

          - `name`:  Define the name of your GCS depot using the format `${lakehouse-name}0${workspace-name}0storage`. For instance, if your `${lakehouse-name}` is alpha and `${workspace-name}` is testing, then the `${gcs-depot-name}` will be alpha0testing0storage.
          - `description`: Provide a brief description of the instance-secret's purpose. This field is optional but recommended for easier management and identification of instance-secrets.
          - `projectid`: The unique identifier of the Google Cloud project that your GCS bucket resides in. You can find this information in the Google Cloud Console under the 'Project Info' section.
          - `email`:  The email address associated with the Google Cloud service account that will be used for accessing GCS. This service account should have the necessary permissions to perform operations on the GCS bucket.
          - `gcskey_json`: The JSON key file of the Google Cloud service account. This file contains the private key and other credentials that are required for authenticating the service account. It can be obtained by creating a service account key in the Google Cloud Console.

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

          - `name`: Define the name of your S3 depot using the format `${lakehouse-name}0${workspace-name}0storage`. For instance, if your `${lakehouse-name}` is alpha and `${workspace-name}` is testing, then the `${gcs-depot-name}` will be alpha0testing0storage.
          - `description`: Provide a brief description of the instance-secret's purpose. This field is optional but recommended for easier management and identification of instance-secrets.
          - `access-key-id`: Your access key ID. This key serves as an identifier for your IAM user or role.
          - `awsaccesskeyid`: AWS-specific access key ID, required for authenticating requests made to AWS services.
          - `awssecretaccesskey`: The secret access key for AWS. It's used in conjunction with the AWS access key ID to sign programmatic requests to AWS.
          - `secretkey`: The secret key associated with your access key ID. Together, they authenticate requests to AWS services.
    
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

    A data warehouse serves as a centralized repository for structured data, enabling efficient query and analysis. Instance-Secrets are configured to securely access and interact with the respective data warehouses, with specific details like project IDs and access keys.

    === "Bigquery"
        
        To create an instance-secret for securely accessing Google BigQuery, the following details are required:

          - `name`: Define the name of your BigQuery depot using the format `${lakehouse-name}0${workspace-name}0storage`. For instance, if your `${lakehouse-name}` is `alpha` and `${workspace-name}` is `testing`, then the `${bigquery-depot-name}` will be `alpha0testing0storage`.
  
          - `description`: Provide a brief description of the instance-secret's purpose. This field is optional but recommended for easier management and identification of instance-secrets.

          - `projectid`: Your BigQuery project ID. This identifier is associated with your Google Cloud project and is required for authenticating requests made to BigQuery services.

          - `email`: The email ID associated with your BigQuery account. This information is essential for specifying the user account that will be used to access BigQuery resources.

        Ensure that you replace each placeholder (e.g., `${depot-name}`, `${projectid}`, `${email}`) with the actual values pertaining to your Google Cloud account and BigQuery configuration.

        
        === "Read-only instance-secret"
            ```yaml title="instance_secret_bigquery_read.yaml" 
            --8<-- "examples/resources/instance_secret/bigquery/bigquery.yaml"
            ```
        === "Read-write instance-secret"
            ```yaml title="instance_secret_bigquery_read_write.yaml"
            --8<-- "examples/resources/instance_secret/bigquery/bigquery_rw.yaml"
            ```
    === "Redshift"

        To create an instance-secret for securely accessing Amazon Redshift, the following details are required:

          - `name`: Define the name of your Redshift depot using the format ${depot-name}. For instance, if your ${depot-name} is "analytics" and ${workspace-name} is "production", then the ${redshift-depot-name} will be analytics-production-r.

          - `description`: Provide a brief description of the instance-secret's purpose. This field is optional but recommended for easier management and identification of instance-secrets.

          - `username`: Your Redshift username. This is the identifier for your Redshift user account.

          - `password`: The password associated with your Redshift username. It is used for authenticating requests to your Redshift cluster.

          - `awsaccesskey`: AWS-specific access key ID, required for authenticating requests made to AWS services, including Redshift.

          - `awssecretaccesskey`: The secret access key for AWS. It's used in conjunction with the AWS access key ID to sign programmatic requests to AWS, including Redshift.

        Ensure that you replace each placeholder (e.g., ${redshift-depot-name}, ${username}, ${access key}) with the actual values pertaining to your Redshift and AWS account configuration.


        === "Read-only instance-secret"
            ```yaml title="instance_secret_redshift_read.yaml" 
            --8<-- "examples/resources/instance_secret/redshift/redshift.yaml"
            ```
        === "Read-write instance-secret"
            ```yaml title="instance_secret_redshift_read_write.yaml"
            --8<-- "examples/resources/instance_secret/redshift/redshift_rw.yaml"
            ```

    === "Snowflake"

        To create an instance-secret for securely accessing Snowflake, the following details are required:

          - `name`: Define the name of your Snowflake depot using the format `${depot-name}`. For instance, if your `${depot-name}` is "analytics" and `${workspace-name}` is "production", then the `${snowflake-depot-name}` will be `analytics-production-r`.

          - `description`: Provide a brief description of the instance-secret's purpose. This field is optional but recommended for easier management and identification of instance-secrets.

          - `${{username}}`: Your Snowflake username. This is the identifier for your Snowflake user account.

          - `${{password}}`: The password associated with your Snowflake username. It is used for authenticating requests to your Snowflake account.

        Ensure that you replace each placeholder (e.g., `${snowflake-depot-name}`, `${username}`) with the actual values pertaining to your Snowflake account configuration.


        === "Read-only instance-secret"
            ```yaml title="instance_secret_snowflake_read.yaml" 
            --8<-- "examples/resources/instance_secret/snowflake/snowflakes.yaml"
            ```
        === "Read-write instance-secret"
            ```yaml title="instance_secret_snowflake_read_write.yaml"
            --8<-- "examples/resources/instance_secret/snowflake/snowflake_rw.yaml"
            ```

=== "SQL Database"

    SQL databases are typically centralized systems designed for structured data, organized into tables with a predefined schema. Instance-Secrets are configured to securely access and interact with the respective SQL databases.

    === "MYSQL"

        To create an instance-secret for securely accessing MySQL, the following details are required:

          - `name`: Define the name of your MySQL depot using the format `${depot-name}`. For instance, if your `${depot-name}` is "database" and `${workspace-name}` is "production", then the `${mysql-depot-name}` will be `database-production-r`.

          - `description`: Provide a brief description of the instance-secret's purpose. This field is optional but recommended for easier management and identification of instance-secrets.

          - `username`: Your MySQL username. This is the identifier for your MySQL user account.

          - `password`: The password associated with your MySQL username. It is used for authenticating requests to your MySQL database.

        Ensure that you replace each placeholder (e.g., `${mysql-depot-name}`, `${username}`) with the actual values pertaining to your MySQL account configuration.


        === "Read-only instance-secret"
            ```yaml title="instance_secret_mysql_read.yaml" 
            --8<-- "examples/resources/instance_secret/mysql/mysql.yaml"
            ```
        === "Read-write instance-secret"
            ```yaml title="instance_secret_mysql_read_write.yaml"
            --8<-- "examples/resources/instance_secret/mysql/mysql_rw.yaml"
            ```

    === "MSSQL"

        To create an instance-secret for securely accessing Microsoft SQL Server (MSSQL), the following details are required:

          - `name`: Define the name of your MSSQL depot using the format `${depot-name}`. For instance, if your `${depot-name}` is "database" and `${workspace-name}` is "production", then the `${mssql-depot-name}` will be `database-production-r`.

          - `description`: Provide a brief description of the instance-secret's purpose. This field is optional but recommended for easier management and identification of instance-secrets.

          - `username`: Your MSSQL username. This is the identifier for your MSSQL user account.

          - `password`: The password associated with your MSSQL username. It is used for authenticating requests to your MSSQL database.

        Ensure that you replace each placeholder (e.g., `${mssql-depot-name}`, `${username}`) with the actual values pertaining to your MSSQL account configuration.


        === "Read-only instance-secret"
            ```yaml title="instance_secret_mssql_read.yaml" 
            --8<-- "examples/resources/instance_secret/mssql/mssql.yaml"
            ```
        === "Read-write instance-secret"
            ```yaml title="instance_secret_mssql_read_write.yaml"
            --8<-- "examples/resources/instance_secret/mssql/mssql_rw.yaml"
            ```

    === "JDBC"

        To create an instance-secret for securely accessing a database via JDBC, the following details are required:

          - `name`: Define the name of your JDBC depot using the format `${depot-name}`. For instance, if your `${depot-name}` is "data" and `${workspace-name}` is "production", then the `${jdbc-depot-name}` will be `data-production-r`.

          - `description`: Provide a brief description of the instance-secret's purpose. This field is optional but recommended for easier management and identification of instance-secrets.

          - `username`: Your JDBC username. This is the identifier for your database user account when connecting via JDBC.

          - `password`: The password associated with your JDBC username. It is used for authenticating requests when connecting to the database via JDBC.

        Ensure that you replace each placeholder (e.g., `${jdbc-depot-name}`, `${username}`) with the actual values pertaining to your JDBC configuration.


        === "Read-only instance-secret"
            ```yaml title="instance_secret_jdbc_read.yaml" 
            --8<-- "examples/resources/instance_secret/jdbc/jdbc.yaml"
            ```
        === "Read-write instance-secret"
            ```yaml title="instance_secret_jdbc_read_write.yaml"
            --8<-- "examples/resources/instance_secret/jdbc/jdbc_rw.yaml"
            ```

    === "Oracle"

        To create an instance-secret for securely accessing Oracle, the following details are required:

          - `name`: Define the name of your Oracle depot using the format `${depot-name}`. For instance, if your `${depot-name}` is "database" and `${workspace-name}` is "production", then the `${oracle-depot-name}` will be `database-production-r`.

          - `description`: Provide a brief description of the instance-secret's purpose. This field is optional but recommended for easier management and identification of instance-secrets.

          - `username`: Your Oracle username. This is the identifier for your Oracle user account.

          - `password`: The password associated with your Oracle username. It is used for authenticating requests to your Oracle database.

        Ensure that you replace each placeholder (e.g., `${oracle-depot-name}`, `${username}`) with the actual values pertaining to your Oracle account configuration.


        === "Read-only instance-secret"
            ```yaml title="instance_secret_oracle_read.yaml" 
            --8<-- "examples/resources/instance_secret/oracle/oracle.yaml"
            ```
        === "Read-write instance-secret"
            ```yaml title="instance_secret_oracle_read_write.yaml"
            --8<-- "examples/resources/instance_secret/oracle/oracle_rw.yaml"
            ```

    === "Postgres"

        To create an instance-secret for securely accessing PostgreSQL, the following details are required:

          - `name`: Define the name of your PostgreSQL depot using the format `${depot-name}`. For instance, if your `${depot-name}` is "database" and `${workspace-name}` is "production", then the `${postgres-depot-name}` will be `database-production-r`.

          - `description`: Provide a brief description of the instance-secret's purpose. This field is optional but recommended for easier management and identification of instance-secrets.

          - `username`: Your PostgreSQL username. This is the identifier for your PostgreSQL user account.

          - `password`: The password associated with your PostgreSQL username. It is used for authenticating requests to your PostgreSQL database.

        Ensure that you replace each placeholder (e.g., `${postgres-depot-name}`, `${username}`) with the actual values pertaining to your PostgreSQL account configuration.


        === "Read-only instance-secret"
            ```yaml title="instance_secret_postgres_read.yaml" 
            --8<-- "examples/resources/instance_secret/postgres/postgres.yaml"
            ```
        === "Read-write instance-secret"
            ```yaml title="instance_secret_postgres_read_write.yaml"
            --8<-- "examples/resources/instance_secret/postgres/postgres_rw.yaml"
            ```
        
=== "NoSQL Database"

    NoSQL databases are designed for flexible, distributed data storage, accommodating unstructured or semi-structured data. Instance-Secrets are configured to securely access and interact with the respective NoSQL databases.

    === "MongoDB"

        To create an instance-secret for securely accessing MongoDB, the following details are required:

          - `name`: Define the name of your MongoDB depot using the format `${depot-name}`. For instance, if your `${depot-name}` is "data" and `${workspace-name}` is "production", then the `${mongodb-depot-name}` will be `data-production-r`.

          - `description`: Provide a brief description of the instance-secret's purpose. This field is optional but recommended for easier management and identification of instance-secrets.

          - `username`: Your MongoDB username. This is the identifier for your MongoDB user account.

          - `password`: The password associated with your MongoDB username. It is used for authenticating requests to your MongoDB database.

        Ensure that you replace each placeholder (e.g., `${mongodb-depot-name}`, `${username}`) with the actual values pertaining to your MongoDB account configuration.


        === "Read-only instance-secret"
            ```yaml title="instance_secret_mongo_read.yaml" 
            --8<-- "examples/resources/instance_secret/mongodb/mongodb.yaml"
            ```
        === "Read-write instance-secret"
            ```yaml title="instance_secret_mongo_read_write.yaml"
            --8<-- "examples/resources/instance_secret/mongodb/mongodb_rw.yaml"
            ```

        
=== "Streaming"

    Streaming refers to the continuous and real-time transmission of data from a source to a destination. Instance-Secrets are configured to securely access and interact with the respective streaming platforms.

    === "Eventhub" 

        To create an instance-secret for securely accessing Azure Event Hubs, the following details are required:

          - `name`: Define the name of your Event Hub depot using the format `${depot-name}`. For instance, if your `${depot-name}` is "events" and `${workspace-name}` is "production", then the `${eventhub-depot-name}` will be `events-production-r`.

          - `description`: Provide a brief description of the instance-secret's purpose. This field is optional but recommended for easier management and identification of instance-secrets.

          - `eh_shared_access_key_name`: Your Azure Event Hub shared access key name. This is the identifier for your Event Hub.

          - `eh_shared_access_key`: The shared access key associated with your Azure Event Hub. It is used for authenticating requests to your Event Hub.

        Ensure that you replace each placeholder (e.g., `${eventhub-depot-name}`, `${EH_SHARED_ACCESS_KEY_NAME}`) with the actual values pertaining to your Azure Event Hub configuration.


        === "Read-only instance-secret"
            ```yaml title="instance_secret_eh_read.yaml" 
            --8<-- "examples/resources/instance_secret/eventhub/eventhub.yaml"
            ```
        === "Read-write instance-secret"
            ```yaml title="instance_secret_eh_read_write.yaml"
            --8<-- "examples/resources/instance_secret/eventhub/eventhub_rw.yaml"
            ```

</div>