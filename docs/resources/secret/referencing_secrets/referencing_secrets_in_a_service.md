# Referencing Secrets in a Service

Given that a Secret is a fundamental Resource within the data operating system, it can be referred to in other DataOS Resources once created. To demonstrate this capability, we will use the example of a Service.

## Create a Secret YAML

Create a YAML file to define a Secret.

```yaml
version: v1
name: testing
type: secret
description: a very special test secret
secret:
  type: key-value #do not use the cloud-kernel type here
  acl: r
  data:
    a: b
    c: d
    e: f
```

## Apply the Secret YAML

Apply the Secret to the Workspace where you want to run your service.

```bash
dataos-ctl apply -f {{path-to-secret-yaml}} -w {{workspace}}
```

<aside class="callout">
🗣 **Note:** The type is <code>cloud-kernel</code> that means a secret will be created with the same name as the secret resource in the same workspace.

</aside>

## Referencing the Secret in Service YAML

Create a YAML file for your service. In the application spec of your service, make a reference to the secret.

```yaml
version: v1
name: hello
type: service
service:
  compute: runnable-default
  title: Hello UI
  replicas: 1
  servicePort: 80
  dataosSecrets:
    - testing             # secret name
  stack: alpha
  envs:
    LOG_LEVEL: info
  alpha:
    image: yeasy/simple-web:latest
```

## Apply the Service YAML

To create a Service Resource, use the `apply` command.

Your secret will be mounted in the DataOS secret directory on each replica of your service and/or job. This directory is defined by the environment variable: `DATAOS_SECRET_DIR=/opt/dataos/secret`

> Kubernetes Administrators with cluster-wide access can inspect the secrets on the running pod using the commands below while your service is running:
> 

```
cat /etc/dataos/secret/a
b
cat /etc/dataos/secret/c
d
cat /etc/dataos/secret/e
f
```