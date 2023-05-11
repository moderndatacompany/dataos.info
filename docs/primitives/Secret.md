# Secret

A Secret is a primitive in DataOS that contains the information of sensitive data such as a password, a token, or a key needed to access your data sources and other services. This helps in keeping the secrets independent of any stack or storage. You can store almost any secret in DataOS, and they can be referred to in different stacks.

## Creating Secrets

You can define the `Secret` resource in a  YAML file and then create that object using the `apply` command in CLI.

1. Create the YAML file. 
    - Specify the version, resource name (secret will be referred to by this name), and resource type (secret). 
    - Specify the secret type under the `secret` section.
        - cloud-kernel - workspace since secrets are namespaced
        - certificate - workspace since secrets are namespaced
        - image-pull - workspace since secrets are namespaced
        - key-value|key-value-properties - could be cluster/global since they are stored in a secret provider (Heimdall)
    - Specify the access control level. (’r,’ or ‘rw’).
    - Provide the credentials under the `data` section in the YAML file.
    
    <br>
    
    > 🗣 You need to create separate secrets for different access control levels (ACLs) and refer to them as per your requirement.

    There are two ways to create a secret resource.
    
    ### Key Value Properties
    
    Define the required properties directly under the `data` section in your YAML. 
    
    ```bash
    ---
    version: v1beta1
    name: <secret-name>
    type: secret
    secret:
      type: <secret-type>
      acl: rw    # can be r|rw
      data:
        key1:value1
        key2:value2
        ...
        ...            
    ```
    
    ### File in Key-Value-Properties
    
    Another way of creating a secret is to make the value of that secret be available as a file inside the filesystem of the DataOS ecosystem.
    
    ```yaml
    ---
    version: v1beta1
    name: <secret-name>
    type: secret
    secret:
      type: key-value-properties
      acl: r
      data:
        key1:value1
        key2:value2
        key_json: <json-file-name> # secrets in a file
    ```
    
2. Create the secret using `dataos-ctl apply` :
    
    ```bash
    dataos-ctl apply -f <path/secret.yaml> -w <name of the workspace>
    ```

<br>

> 🗣 When you create a ‘Secret’ artifact YAML and apply it in CLI, Poros, the resource manager, sends it to Heimdall, the Governance engine. Heimdall provides vault support for secrets and enables you to control access to secrets using fine-grained permissions whenever the users or applications want to retrieve credentials.

## Referring Secrets

DataOS allows you to create a secret as a primitive. Once a secret primitive is created, you can refer to it in different stacks or you can link secrets to depots.

## Passing Secrets Using Alpha Stack

1. Create a YAML file for defining a secret.
    
    <u>secret.yaml</u>
    
    ```yaml
    version: v1
    name: testing
    type: secret
    description: a very special test secret
    secret:
      type: cloud-kernel
      acl: r
      data:
        a: b
        c: d
        e: f
    ```
    <br>
> 🗣 Note that the secret type is “cloud-kernel”, which means that a k8s secret will be created with the same name as the secret resource in the same workspace.

2. Apply the secret to the workspace where you want to run your service or workflow.
3. Create a YAML file for your service. Reference the secret in the application spec of your service and/or workflow. 
    
    <u>alpha.yaml</u>
    
    ```yaml
    version: v1
    name: hello
    type: service
    service:
      compute: runnable-default
      title: Hello UI
      replicas: 1
      servicePort: 80
      secrets:
        - testing             # secret name
      stack: alpha
      envs:
        LOG_LEVEL: info
      alpha:
        image: yeasy/simple-web:latest
    ```
    
4. Use the `apply` command to create a service resource.
    
    The secret will be mounted into the DataOS secret dir on each replica of your service and/or job in the directory defined by the environment variable: DATAOS_SECRET_DIR=/opt/dataos/secret
    

> While your service is running, the Administrator, who has access to the whole cluster like K8s, can check the secrets on the running pod using the following commands:

```bash
cat /etc/dataos/secret/a
b
cat /etc/dataos/secret/c
d
cat /etc/dataos/secret/e
f
```

## Using Secrets with Depots

Once a secret primitive is created, you can simply refer to it in the Depot YAML. That means you don't need to include confidential data while defining your Depot configuration. 

Depots keep physical connection information, such as a database of type Postgres, its URL to hit, and the domain name along with the port number, and can refer to the secrets that you need to connect to it.

1. Create a YAML file for defining a secret. The following YAML file includes two secret definitions for two access control permissions ( for ‘RW’ and ‘R’ access).
    
    secret.yaml
    
    ```yaml
    name: gcsr
    version: v1
    type: secret
    description: "the user and password for the depot to read"
    secret:
      type: key-value-properties
      acl: r
      data:
        projectid: <project id>
        email: <email id>
        gcskey.json: "{\n  \"type\": \"service_account\",\n  \"project_id\": \"projectid\",\n  \"private_key_id\": \"privatekey\",\n  \"private_key\": \"-----BEGIN PRIVATE KEY-----\\n<privatekey>\\n-----END PRIVATE KEY-----\\n\",\n  \"client_email\": \"email\",\n  \"client_id\": \"107040717795711219453\",\n  \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",\n  \"token_uri\": \"https://oauth2.googleapis.com/token\",\n  \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\",\n  \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/ds-sa-r-bird--dev%40dataos-ck-res-yak-dev.iam.gserviceaccount.com\"\n}\n"
        gcskey_json: gcskey.json
    ---
    name: gcsrw
    version: v1
    type: secret
    description: "the user and password for the depot to read and write"
    secret:
      type: key-value-properties
      acl: rw
      data:
        projectid: <project id>
        email: <email id>
        gcskey.json: "{\n  \"type\": \"service_account\",\n  \"project_id\": \"projectid\",\n  \"private_key_id\"privatekey\",\n  \"private_key\": \"-----BEGIN PRIVATE KEY-----\\n<privatekey>\\n-----END PRIVATE KEY-----\\n\",\n  \"client_email\": \"ds-sa-bird--dev@dataos-ck-res-yak-dev.iam.gserviceaccount.com\",\n  \"client_id\": \"101436172406509362992\",\n  \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",\n  \"token_uri\": \"https://oauth2.googleapis.com/token\",\n  \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\",\n  \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/ds-sa-bird--dev%40dataos-ck-res-yak-dev.iam.gserviceaccount.com\"\n}\n"
        gcskey_json: gcskey.json
    ```
    
2. Use the `apply` command to create secret resources. Apply the secret to the workspace where you want to run your service or workflow.
3. Create a YAML file for your Depot. Reference the secret in the application spec of your Depot. 
    
    GCSDepot.yaml
    
    ```yaml
    ---
    name: gcs
    type: depot
    version: v1
    description: "GCS Data Depot"
    layer: user
    depot:
      type: "GCS"
      spec:
        bucket: "airbyte-minio-testing"
        relativePath: "sanity"
        format: "ICEBERG"
      external: true
      secrets:
        - name: gcsrw                    # refer secret for read & write access
          workspace: public
          keys:
            - public_gcsrw
        - name: gcsr                     # refer secret for read only access
          workspace: public
          keys:
            - public_gcsr
    ```
    
4. Use the `apply` command to create a Depot resource.

> 🗣 You need to create separate secrets for different access control levels (ACLs) and refer to them as per your requirement.