# Container Stack within a Workflow

You can also execute or call Container stack within a Workflow as given below:

```yaml
name: container-workflow
version: v1
type: workflow
workflow:
  dag:
    - name: drop-column
      spec:
        stack: container
        envs:
          LOG_LEVEL: debug
        stackSpec:
          image: <container-image-path>
          arguments:
            - dataset
            - drop-column
            - --address=dataos://icebase:retail/city?acl=rw
            - --name=country
    - name: add-column
      spec:
        stack: container
        envs:
          LOG_LEVEL: debug
        container:
          image: <container-image-path>
          arguments:
            - dataset
            - add-column
            - --address=dataos://icebase:retail/city?acl=rw
            - --name=time
            - --type=timestamp_without_zone
      dependencies:
        - drop-columnn
```