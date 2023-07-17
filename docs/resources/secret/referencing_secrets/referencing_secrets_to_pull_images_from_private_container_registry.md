# Referencing Secrets to Pull Images from Private Container Registry

## Create a Secret YAML

Add a Secret Resource into the Workspace where you will run the Alpha Service or Job; the `cloud-kernel-image-pull` secret type will create a Kubernetes Secret in the Workspace.

```yaml
version: v1beta1
name: docker-image-pull
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

## Apply the Secret YAML

Use the `apply` command to create a Secret Resource in the workspace.

```shell
dataos-ctl apply -f {{path-to-secret-yaml}} -w {{workspace}}
```

## Referencing the Secret in Alpha YAML

Reference the Secret in Alpha Stack

```yaml
version: v1beta1
name: example-alpha-workflow
type: workflow
workflow:
  dag:
  - name: example
    spec:
      stack: alpha
      alpha:
        image: docker.io/REPOSITORY/IMAGE:TAG
        imagePullSecret: docker-image-pull
```