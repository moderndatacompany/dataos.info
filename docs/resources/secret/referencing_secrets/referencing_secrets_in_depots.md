# Referencing Secrets in Depots

Following the creation of a Secret resource, it can be conveniently referred to within the Depot YAML. This eliminates the need to incorporate confidential data during your Depot configuration definition.

Depots store essential connection details like Postgres database type, access URL, domain name, and port number and can refer to the secrets that you need for establishing the connection.

## Create a Secret YAML

Define a secret by creating a YAML file. Below is an example YAML file containing two secret definitions corresponding to two access control permissions (i.e., for ‘RW’ and ‘R’ access).

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

## Apply the Secret YAML

To create a secret resource, we use the `apply` command. Since a Secret is a workspace resource we apply it to a particular workspace where you want to create the additional resource.

```bash
dataos-ctl apply -f <path-to-secret-yaml> -w <workspace>
```

## Referencing the Secret in Depot YAML

Create a YAML file for your Depot. In the application spec of your Depot, make a reference to the secret.

```yaml
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
  dataosSecrets:
    - name: gcsrw                    # refer secret for read & write access
      workspace: public
      keys:
        - public_gcsrw
    - name: gcsr                     # refer secret for read-only access
      workspace: public
      keys:
        - public_gcsr
```

## Apply the Depot YAML

Utilize the `apply` command to create a Depot resource.

```bash
dataos-ctl apply -f <path-to-depot-yaml>
```

> Please note that we've generated distinct secrets for various access control levels (ACLs), and we've made references to them based on the requirements.
>