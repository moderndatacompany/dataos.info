# Deploying Private Images Available on DockerHub

Container Stack allows you to pass your secret keys and credentials as environment variables. But these are visible to everybody. To counter this, Container Stack provides a secure method to pass this sensitive information through DataOS [Secret](/resources/secret/) Resource. The following steps outline the procedure:

## Create a manifest file for the Secret Resource

```yaml
# Images
name: docker-image
version: v1beta1
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

The `type` field should be set to "cloud-kernel-image-pull", which will generate a Docker container registry Secret within the same Workspace. Learn more about Cloud Kernel Image Pull secret on the link: [Referencing Secrets to Pull Images from a Private Conatiner Registry](/resources/secret/#referencing-secrets-to-pull-images-from-private-container-registry)

## Apply the Secret Resource

Apply the Secret to the desired workspace where the Container Service or Workflow will be executed.

```bash
dataos-ctl apply -f ${path-to-secret-yaml} -w ${name of the workspace}
```

## Reference the secret within the Container YAML

Specify the name of the secret and add it to the "secrets" attribute of the service section in the Container Service/ Workflow YAML file. This will mount the Dataos secret directory on each replica of your Service and/or Workflow in the directory specified by the environment variable

```yaml
name: example-container
version: v1
type: workflow
workflow:
  dag:
  - name: example
    spec:
      resources:
          requests:
            cpu: 250m
            memory: 500m
          limits:
            cpu: 1
            memory: 1Gi
      dataosSecrets:
          - name: workflow-user-secret
            workspace: public
            keys:
              - DATAOS_USER_NAME
              - CLUSTER_NAME
              - DATAOS_API_KEY
              - DATAOS_ENV_NAME
      stack: container
      compute: runnable-default
      stackSpec:
        image: docker.io/helloworldimage/helloworldimage:tag
        imagePullSecret: dockers-secrets
        command:
          - python
```