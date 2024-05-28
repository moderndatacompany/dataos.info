# Deploying images on a Private DockerHub

Alpha Stack allows you to pass your secret keys and credentials as environment variables. But these are visible to everybody. To counter this, Alpha Stack provides a secure method to pass this sensitive information through a Secret (a DataOS Primitive/resource). The following steps outline the procedure:

## Create a YAML file for the Secret resource

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

The `type` field should be set to "cloud-kernel", which will generate a k8s secret with the same name as the secret resource in the same workspace.

## Apply the Secret Resource

Apply the Secret to the desired workspace where the Alpha Service or Workflow will be executed.

```bash
dataos-ctl apply -f <path/secret.yaml> -w <name of the workspace>
```

## Reference the secret within the Alpha YAML

Specify the name of the secret and add it to the "secrets" attribute of the service section in the Alpha Service/ Workflow YAML file. This will mount the Dataos secret directory on each replica of your Service and/or Workflow in the directory specified by the environment variable

`DATAOS_SECRET_DIR =/opt/dataos/secret`. 

```yaml
version: v1
name: hello
type: service
service:
	compute: runnable-default
	title: Hello UI
	replicas: 1
	servicePort: 8080
	secrets: # Refer Secrets like this
		- testing
	stack: alpha
	envs:
		LOG_LEVEL: info
	alpha:
		image: yeasy/simple-web:latest
```