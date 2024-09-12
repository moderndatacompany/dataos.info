To optimize data retrieval and enhance performance, you can use the datasets cached by Flash to construct Lens logical tables. This strategic caching minimizes the amount of data queried, making operations more efficient. By storing logical tables of frequently accessed or queried Lenses in Flash, you avoid repeatedly accessing the source and scanning large datasets. This enables faster performance with responses delivered in seconds.

## When to Flash Logical Tables?

Consider the following criteria to determine if the logical tables of a Lens need to be cached in Flash:

- **Complexity of the SQL View:** Look for SQL that involves complex operations such as aggregate functions, multiple joins, and subqueries. These indicate potentially resource-intensive queries.
- **Data Volume:** Lens models operating on large volumes of data from the source are prime candidates. Caching such logical tables in Flash can expedite query processing.
- **Source Optimization:** If the source system struggles to handle complex queries efficiently, evidenced by prolonged query execution times or frequent timeouts, storing the table in Flash could significantly enhance performance.

## Steps to consume Flash dataset in Lens

1. Define the Flash layer (Service) as the data source for your Lens deployment manifest file:
    
    ```yaml
    source:
      type: flash #minerva/themis/depot
      name: flash-test  # name of the Flash service
      catalog: icebase
    ```
    
2. Specify two additional environment variables in the Worker, API, and router sections of the Lens deployment YAML:
    
    ```yaml
    envs:
      LENS2_SOURCE_WORKSPACE_NAME: public
      LENS2_SOURCE_FLASH_PORT: 5433
    ```
    
    Below is the sample Lens deployment manifest file of Flash as a source for better understanding.
    
    ```yaml
    version: v1alpha
    name: "lens-test01"
    layer: user
    type: lens
    tags:
      - lens
    description: A sample lens that contains three entities, a view, and a few measures for users to test
    lens:
      compute: runnable-default
      secrets: # Referred Instance-secret configuration (**mandatory for private code repository, not required for public repository)
        - name: gitsecret-r # Referred Instance Secret name (mandatory)
          allKeys: true # All keys within the secret are required or not (optional)
      source:
        type: flash # minerva, themis and depot
        name: flash-test01 # flash service name
      repo:
        url: https://github.com/iamgroot/lens-flash
        lensBaseDir: lens-flash/flash/model     # location where lens models are kept in the repo
        syncFlags:
          - --ref=main
      api:
        replicas: 1
        logLevel: debug
        envs:
          LENS2_SCHEDULED_REFRESH_TIMEZONES: "UTC,America/Vancouver,America/Toronto"
          LENS2_SOURCE_WORKSPACE_NAME: public
          LENS2_SOURCE_FLASH_PORT: 5433
        resources: # optional
          requests:
            cpu: 100m
            memory: 256Mi
          limits:
            cpu: 2000m
            memory: 2048Mi
    
      worker:
        replicas: 1
        logLevel: debug
        envs:
          LENS2_SCHEDULED_REFRESH_TIMEZONES: "UTC,America/Vancouver,America/Toronto"
          LENS2_SOURCE_WORKSPACE_NAME: public
          LENS2_SOURCE_FLASH_PORT: 5433
        resources: # optional
          requests:
            cpu: 100m
            memory: 256Mi
          limits:
            cpu: 6000m
            memory: 6048Mi
    
      router:
        logLevel: info
        envs:
          LENS2_SCHEDULED_REFRESH_TIMEZONES: "UTC,America/Vancouver,America/Toronto"
          LENS2_SOURCE_WORKSPACE_NAME: public
          LENS2_SOURCE_FLASH_PORT: 5433
        resources: # optional
          requests:
            cpu: 100m
            memory: 256Mi
          limits:
            cpu: 6000m
            memory: 6048Mi
    
      iris:
        logLevel: info  
        envs:
          LENS2_SCHEDULED_REFRESH_TIMEZONES: "UTC,America/Vancouver,America/Toronto"
          LENS2_SOURCE_WORKSPACE_NAME: public
          LENS2_SOURCE_FLASH_PORT: 5433
        resources: # optional
          requests:
            cpu: 100m
            memory: 256Mi
          limits:
            cpu: 6000m
            memory: 6048Mi
    ```
    
3. Now create the [Lens model](https://www.notion.so/Lens-Set-up-5e0c742506304ec286d42bae32428509?pvs=21) and deploy it as mentioned [here](https://www.notion.so/Deploying-Lens-98553d2e1a7d425080cee8247b49f457?pvs=21).