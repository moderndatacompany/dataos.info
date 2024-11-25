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

## Accessing the Flash web app

1. **Get the ingress path**: Retrieve the ingress path from [Metis](/interfaces/metis/), as shown below:

    <center>
      <img src="/resources/stacks/flash/annotely_image%20(30).png" alt="Metis" style="width:45rem; border: 1px solid black; padding: 5px;" />
      <figcaption><i>Metis Interface</i></figcaption>
    </center>

2. **Access the web app**: Use the following URL syntax in your browser to open the Flash web app:

    ```shell
    <DataOS env URL>/flash/workspace:service_name
    ```

    Replace `<DataOS env URL>` and the ingress path as needed. This will open an interface similar to the following:

    <center>
      <img src="/resources/stacks/flash/recipes/web_app.png" alt="Flash Web App" style="width:45rem; border: 1px solid black; padding: 5px;" />
      <figcaption><i>Flash Web App</i></figcaption>
    </center>

## Exploring the Flash web app


### **Meta**

The **Meta** section provides detailed information about the Flash Service, including:

- **Creation Time**: When the cached data was created.

- **Uptime**: How long the Flash Service has been running without interruptions.

- **Container Image**: The image used by the Flash container.

<center>
  <img src="/resources/stacks/flash/meta.png" alt="Meta Section" style="width:45rem; border: 1px solid black; padding: 5px;" />
  <figcaption><i>Meta section</i></figcaption>
</center>

### **Data cached**

This section displays the number of tables and views cached in Flash, along with the total data size (in bytes).

<center>
  <img src="/resources/stacks/flash/datacached.png" alt="Data Cached Section" style="width:45rem; border: 1px solid black; padding: 5px;" />
  <figcaption><i>Data cached section</i></figcaption>
</center>

### **Inspection**

The **Inspection** section provides insights into:

<center>
  <img src="/resources/stacks/flash/recipes/inspection.png" alt="Inspection section" style="width:45rem; border: 1px solid black; padding: 5px;" />
  <figcaption><i>Inspection section</i></figcaption>
</center>

- **CPU Usage**: The amount of CPU resources used.

- **Memory Usage**: The memory consumption (in GB).

- **Users**: The number of users querying the cached data.

- **Total Queries**: The total number of queries executed.

### **Queries**

The **Queries** section lists detailed information about each query, including:

<center>
  <img src="/resources/stacks/flash/recipes/queries.png" alt="Queries section" style="width:45rem; border: 1px solid black; padding: 5px;" />
  <figcaption><i>Queries section</i></figcaption>
</center>

- **Query**: The SQL query executed.

- **User**: The user who submitted the query.

- **Submitted At**: The timestamp when the query was submitted.

- **Status**: Whether the query was completed, in progress, or encountered an error.

- **Execution Time (ms)**: The time it took to execute the query in milliseconds.

### **Settings**

Settings section of the Flash web app provides the information on the default settings of Flash as shown below.

<center>
  <img src="/resources/stacks/flash/recipes/settings.png" alt="Settings section" style="width:45rem; border: 1px solid black; padding: 5px;" />
  <figcaption><i>Settings section</i></figcaption>
</center>
