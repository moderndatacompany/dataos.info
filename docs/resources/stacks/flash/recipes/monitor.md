# How to Monitor Cached Datasets in Flash?

Monitoring cached datasets in Flash is essential for tracking performance and resource usage. To enable monitoring, the `ingress` attribute must be included in the Flash Service manifest file, as shown below:

```yaml
service:
  servicePort: ${{8080}}
  servicePorts:
  - name: ${{backup}}
    servicePort: ${{5433}}
  ingress:
    enabled: ${{true}}
    stripPath: ${{false}}
    path: ${{/flash/public:flash-test-6}}
    noAuthentication: ${{true}}
  replicas: ${{1}}
  logLevel: ${{info}}
  compute: ${{runnable-default}}
  envs:
    APP_BASE_PATH: ${{'dataos-basepath'}}
    FLASH_BASE_PATH: ${{/flash/public:flash-test-6}}
  resources:
    requests:
      cpu: ${{500m}}
      memory: ${{512Mi}}
    limits:
      cpu: ${{1000m}}
      memory: ${{1024Mi}}
```

The `ingress` attribute allows access to the Flash web app, which enables monitoring of the cached datasets.

## Accessing the Flash Service metrics

1. **Get the ingress path**: Retrieve the ingress path from [Metis](/interfaces/metis/), as shown below:

    <center>
      <img src="/resources/stacks/flash/annotely_image%20(30).png" alt="Metis" style="width:45rem; border: 1px solid black; padding: 5px;" />
      <figcaption><i>Metis Interface</i></figcaption>
    </center>

2. **Access the metrics**: Use the following URL syntax in postman to fetch the metrics endpoint by providing the DataOS API key as the bearer token:

    ```bash
    <DataOS env URL>/flash/workspace:service_name/metrics
    ```

    Replace `<DataOS env URL>` and the ingress path as needed. 

    <center>
      <img src="/resources/stacks/flash/recipes/postman.png" alt="Flash Service endpoint" style="width:45rem; border: 1px solid black; padding: 5px;" />
      <figcaption><i>Flash Service endpoint</i></figcaption>
    </center>


