# Setting up Talos within DataOS

This section involves a step-by-step guide to set up Talos within DataOS enviroment using [Service](/resources/service/) resource. By following this guide, you will be able to effectively implement Talos in your DataOS environment.

## Pre-requisite

Extract the [zip](/resources/stacks/talos/talos.zip) and initialize it with Bitbucket.

## Steps

Steps to set up Talos for Depot source type. Types of Depot supported by Talos are BigQuery, Snowflake, Postgres, and Redshift.  To set up Talos within DataOS as a Service follow the below steps.

1. Open the repository using code editor. Navigate to the `setup` folder and open the `config.yaml` manifest file. Within this file, update the fields for name, description, version, dataos context, source name, and source type to ensure they accurately reflect your specific configurations and align with requirements.
    
    ```yaml
    name: ${{superstore}}
    description: ${{A talos-depot-postgres app}} # description
    version: 0.1.6 # talos image version
    auth: # authentication details
      heimdallUrl: https://${{dataos-context}}/heimdall 
    logLevel: ${{'DEBUG'}}
    sources: # source details
      - name: ${{snowflakedepot}} # depot name
        type: ${{depot}} # source type
    ```
    
    <aside class="callout">
    🗣 Verify that the source type, if specified as 'Depot', is active.
    
    </aside>
    
    To know more about each attribute, [please refer to this](/resources/stacks/talos/configurations/config/).
    
2. Open the `docker-compose.yaml` manifest file and update it by adding your DataOS username and API key. Enter your DataOS username in the `DATAOS_RUN_AS_USER` field and your DataOS API key in the `DATAOS_RUN_AS_APIKEY` field. 
    
    ```yaml
    version: "2.2"
    services:
      talos:
        image: rubiklabs/talos:0.1.6
        ports:
          - "3000:3000"
        volumes:
          - .:/etc/dataos/work
        environment:
          DATAOS_RUN_AS_USER: ${{iamgroot}}
          DATAOS_RUN_AS_APIKEY: ${{dG9rZW5fYWRtaXR0ZGHHJ987uYXR1cmFsbHlfZW5hYmxpbmdfb3J5eC5lODg2MjIyZC05NDMwLTQ4MWEtYjU3MC01YTJiZWY5MjI5OGE=}}
          DATAOS_FQDN: ${{liberal-donkey.dataos.app}}
        tty: true
    ```
    
    To know more about each attribute, [please refer to this](/resources/stacks/talos/configurations/docker_compose/).
    
3. Open the `apis` folder within the `setup` directory and access the `table.sql` and `table.yaml` files. Update the SQL queries in `table.sql` and modify the `urlPath`, `description`, and `source` fields in `table.yaml` to accurately reflect your API's data access paths and configuration details. Ensure that both the queries and the YAML configuration are properly aligned with your API requirements. Additionally, you may add multiple SQL files and their corresponding manifest files within the `apis` folder as needed.
    
    ```sql
    # table.sql
    SELECT * FROM myschema.mytable LIMIT 10;
    ```
    
    ```yaml
    # table.yaml
    urlPath: /table # output path
    description: product list # description
    source: ${{snowflakedepot}} # source name
    ```
    
    To know more about each attribute, [please refer to this](/resources/stacks/talos/configurations/apis/).

5. Push the changes to your Bitbucket repository as shown below:

<div style="text-align: center;">
  <img src="/resources/stacks/talos/image1.png" style="border:1px solid black; width: 40%; height: auto;">
</div>


1. To run it as a Service, create an Instance Secret to store your Bitbucket credentials. This step ensures that the necessary authentication details are securely stored and accessible for the Service.
    
    ```yaml
    name: ${{bitrepo}}-r
    version: v1
    type: instance-secret
    description: ${{"Bitbucket credentials"}}
    layer: ${{user}}
    instance-secret:
      type: ${{key-value}}
      acl: ${{r}}
      data:
        GITSYNC_USERNAME: ${{"iamgroot7340"}}# Bitbucket username
        GITSYNC_PASSWORD: ${{"ATBBe2we5UPdGVthtEHnjkLDHL7443AC"}}# Bitbukcet app password
    ```
    
    To create an app password in Bitbucket follow the below steps:
    
    - Go to settings, then click on Personal Bitbucket settings.
    - Go to App passwords create one and paste the password into your Instance Secret manifest file.
        
        ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/f2a9e006-6401-4684-9bc4-ba59acc0c695/Untitled.png)
        
    
    Apply the Instance Secret manifest file by executing the below command:
    
    ```bash
    dataos-ctl resource apply -f /home/office/talos/secret.yaml 
    ```
    
    To know more about Instance Secret, [please refer to this](https://dataos.info/resources/instance_secret/).
    
2. Now create a manifest file for the Service as shown below.
    
    ```yaml
    name: ${{talos-test}} # service name
    version: ${{v1}} # version
    type: service # resource type
    tags: # tags
      - ${{service}}
      - ${{dataos:type:resource}}
      - ${{dataos:resource:service}}
      - ${{dataos:layer:user}}
    description: ${{Talos Service}}
    workspace: ${{public}}
    service: # service specific section
      servicePort: 3000
      ingress:
        enabled: true
        stripPath: true
        path: /talos/${{workspace}}:${{talos-test}} # service name
        noAuthentication: true
      replicas: ${{1}}
      logLevel: ${{DEBUG}}
      compute: runnable-default
      envs:
        TALOS_SCHEMA_PATH: ${{talos/setup}}
        TALOS_BASE_PATH: /talos/public:${{talos-test}}
      resources:
        requests:
          cpu: ${{100m}}
          memory: ${{128Mi}}
        limits:
          cpu: ${{500m}}
          memory: ${{512Mi}}
      stack: talos:2.0
      dataosSecrets:
        - name: ${{bitrepo-r}}
          allKeys: true
      stackSpec:
        repo:
          url: ${{https://bitbucket.org/mywork15/talos/}}
          projectDirectory: ${{talos/setup}}
          syncFlags:
            - '--ref=main'
    ```
    
    To know more about each attribute, [please refer to this](docs/resources/stacks/talos/configurations/service/).
    
3. Apply the Service manifest by executing the below command:
    
    ```bash
    dataos-ctl resource apply -f /home/office/talos/service.yaml 
    ```
    
    To check if the service is running successfully, execute the following command.
    
    ```bash
    dataos-ctl log -t service -n ${{service-name}} -w ${{workspace}}
    ```
    
    Successful execution will look like the following:
    
    ```bash
    EBUG [CORE] Duckdb config: TimeZone = Etc/UTC
    2024-07-31 08:51:12.566  
    DEBUG [SERVE] Data source duckdb initialized
    2024-07-31 08:51:12.567  DEBUG
    [SERVE] Initializing data source: pg
    2024-07-31 08:51:12.567  DEBUG
    [SERVE] Data source pg initialized
    2024-07-31 08:51:12.567  DEBUG
    [SERVE] Initializing data source: redshift
    2024-07-31 08:51:12.567  DEBUG
    [SERVE] Data source redshift initialized
    2024-07-31 08:51:12.568  
    DEBUG [SERVE] Initializing data source: snowflake
    2024-07-31 08:51:12.568  DEBUG
    [CORE] Initializing profile: snowflake using snowflake driver
    2024-07-31 08:51:12.681  DEBUG
    [CORE] Profile snowflake initialized
    2024-07-31 08:51:12.681  DEBUG [SERVE] Data source snowflake initialized
    2024-07-31 08:51:12.682  
    INFO  [SERVE] Start to load and schedule prefetched data results from data sources to cache layer...
    2024-07-31 08:51:12.689  DEBUG
    [SERVE] profile: snowflake, allow: *
    2024-07-31 08:51:12.690  
    DEBUG [SERVE] profile: talos.cache, allow: *
    2024-07-31 08:51:12.696  DEBUG
    [CORE] Authenticator: {
      "heimdallUrl": "https://liberal-donkey.dataos.app/heimdall",
      "userGroups": [
        {
          "name": "default",
          "description": "auto-generated default group to include everyone",
          "includes": "*"
        }
      ]
    }
    2024-07-31 08:51:12.702  
    INFO  [CLI] 🚀 Server is listening at port 3000.
    ```
    
4. Now you can access the data on the API endpoint using Postman, as shown below:

    <div style="text-align: center;">
    <img src="/resources/stacks/talos/image2.png" style="border:1px solid black; width: 40%; height: auto;">
    </div>

    
    You can even hit the endpoint `/doc/postman?apikey='xxxxxxxxx'` to download the postman collection and import the `.json` collection into postman.
    
5. Authenticate the API endpoints by passing the API Key as query param as shown below.
    
    ```bash
    curl --location 'https://liberal-donkey.dataos.app/talos/pubic:talos-test/api/table?apikey=xxxx' 
    ```