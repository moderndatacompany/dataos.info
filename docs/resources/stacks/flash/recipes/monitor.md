# Monitoring cached dataset

To monitor the cached dataset, it is mandatory to provide the `ingress` attribute in Flash Service manifest file, as shown below.

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
The `ingress` attribute will enable you to add inspect web app path, through which you can monitor the cached datasets.

To open the web app, simply copy the ingress path from [Metis](/interfaces/metis/) as shown below.

<center>
  <img src="/resources/stacks/flash/annotely_image%20(30).png" alt="Metis" style="width:40rem; border: 1px solid black; padding: 5px;" />
  <figcaption><i>Metis Interface</i></figcaption>
</center>

and browse the URL with syntax similar to `<DataOS env URL>/flash/workspace:service_name` by providing DataOS environment URL and ingress path, which will open an interface similar to this:

<center>
  <img src="/resources/stacks/flash/webapp.png" alt="Metis" style="width:40rem; border: 1px solid black; padding: 5px;" />
  <figcaption><i>Flash web app</i></figcaption>
</center>

Let's explore each elements of the web app to better undertand and monitor the cached dataset.

### **Meta**

The Meta section provides information such as the creation time of the cached data, the uptime of the cached data in seconds, and the image of the flash container. **Uptime** refers to the amount of time the Flash Service has been continuously running without interruption or downtime.

<center>
  <img src="/resources/stacks/flash/meta.png" alt="Metis" style="width:40rem; border: 1px solid black; padding: 5px;" />
  <figcaption><i>Flash web app</i></figcaption>
</center>

### **Data Cached**
This section provides the number of cached tables and views, along with the data size in bytes.

<center>
  <img src="/resources/stacks/flash/datacached.png" alt="Metis" style="width:40rem; border: 1px solid black; padding: 5px;" />
  <figcaption><i>Flash web app</i></figcaption>
</center>

### **Inspection**

Inspection section provides the observations on CPU uage, memory usage in GB, total users queried on the cached data, and total number of queries.

### **Queries**

Queries section provides the information on Query, User, Submitted at, Status, and	Execution Time(ms).


