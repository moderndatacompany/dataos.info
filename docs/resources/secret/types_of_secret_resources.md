# Types of Secret Resources

DataOS comes equipped with 5 intrinsic types of secrets to accommodate standard usage cases. They are `cloud-kernel`, `cloud-kernel-image-pull`, `certificates`, `key-value`, and `key-value-properties`.

The sections below describe each one of them in detail.

## `cloud-kernel`

The cloud-kernel secret type means that a Kubernetes secret will be created with the same name as the secret resource in the same workspace

**Syntax**

```yaml
name: testing
version: v1
type: secret
description: a very special test secret
secret:
  type: cloud-kernel
  acl: r
  data:
    {{a: b}}
    {{c: d}}
    {{e: f}}
```

## `cloud-kernel-image-pull`

Accessing a Docker registry for images requires valid Docker credentials. You can use this secret type to create a Secret to store the credentials for accessing a private container image registry. To do so, add a Secret resource into the Workspace using the syntax provided below.

**Syntax**

```yaml
name: {{docker-image-pull}}
version: v1
type: secret
secret:
  type: cloud-kernel-image-pull
  acl: r
  data:
    .dockerconfigjson: |
      {
        "auths": {
          "https://index.docker.io/v1/": {
            "auth": "",
            "username": "",
            "password": ""
          }
        }
      }
```


## `key-value`

This secret type is for storing simple pairs of keys and values. They are stored in Heimdall vault.

**Syntax**

```yaml
name: {{testing}}
version: v1
type: secret
secret:
  type: key-value
  acl: r
  data:
    {{key1:value1}}
    {{key2:value2}}
```

When you store a secret as a key-value type, the system passes the secret in the format they are stated, without any alterations.


## `key-value-properties`

This type is similar to key-value, but the difference lies in the way the system passes the data. In the key-value-properties type, the system passes all the secrets as one single field, while in the case of the key-value type, they are passed as separate fields.

**Syntax**

```yaml
name: {{testing}}
version: v1
type: secret
secret:
  type: key-value-properties
  acl: r
  data:
    {{key1:value1}}
    {{key2:value2}}
```

Another way of creating a secret is to make the value of that secret available as a file, and referring the path of that file in the YAML

**Syntax**

```yaml
name: {{testing}}
version: v1
type: secret
secret:
  type: key-value-properties
  acl: r
  data:
    {{key1:value1}}
    {{key2:value2}}
    key_json: {{json-file-name}} # secrets in a file
```

## `certificate`

This type is used to store TLS certificates and keys. The most common usage scenario is Ingress resource termination, but this type is also sometimes used with other resources.

**Syntax**

```yaml
name: {{secret-name}}
version: v1
type: secret
secret:
  type: certificate
  acl: rw
  files:
    truststoreLocation: {{file-path}}
    keystoreLocation: {{file-path}}
```