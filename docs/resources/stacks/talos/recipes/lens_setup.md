# Setting up Talos for Lens

## Pre-requisites

- [Lens](/resources/lens/) set up
- Docker initialization

## Steps

1. Create and open a folder with a code editor (VS Code), and create a `config.yaml` manifest file and copy the below code. Update the name, description, version, dataos context, Lens as type, and Lens name.
    
    ```yaml
    name: lens
    description: A talos-lens app
    version: 0.1.19-dev
    auth:
      heimdallUrl: https://${{liberal-donkey.dataos.app}}/heimdall
    logLevel: 'DEBUG'
    sources:
      - name: lens 
        type: lens
        lensName: 'public:sales360'
    ```
    
    
2. Create a folder named `apis` inside the same parent folder, inside `apis` create the files `sales.sql` which will contain the SQL query, and `sales.yaml` to define the path to access sales data in your API as shown below. You can add as many `.sql` files as needed, but each one must have a corresponding `.yaml` manifest file with the same name.
    
    ```sql
    # sales.sql
    SELECT customer_no FROM sales LIMIT 20
    ```
    
    ```yaml
    # sales.yaml
    urlPath: /customers
    description: list customer numbers from sales table
    source: lens
    ```
    
3. To deploy Talos as a Service within DataOS, initialize the repository and push the changes to the Bitbucket.

4. Create an Instance Secret to store your Bitbucket credentials. This step ensures that the necessary authentication details are securely stored and accessible for the Talos Service.

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
        
        <center>
          <img src="/resources/stacks/talos/app.png" alt="Talos" style="width:30rem; border: 1px solid black; padding: 5px;" />
        </center>

    Apply the Instance Secret manifest file by executing the below command:

    ```bash
    dataos-ctl resource apply -f /home/office/talos/secret.yaml 
    ```

    To know more about Instance Secret, [please refer to this](/resources/instance_secret/).

5. Now create a manifest file for the Talos Service as shown below.

    <aside class="callout">
    🗣 Ensure to map the repository path correctly.
    </aside>
    
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
      stack: talos:1.0
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
    
    To know more about each attribute, [please refer to this](/resources/stacks/talos/configurations/service/).
    
6. Apply the Service manifest by executing the below command:
    
    ```bash
    dataos-ctl resource apply -f /home/office/talos/service.yaml 
    ```
    
7. To check if the Service is running successfully, execute the following command.
    
    ```bash
    dataos-ctl log -t service -n ${{service-name}} -w ${{workspace}}
    ```
    
    Successful execution will look like the following:
    
    ```bash
    EBUG [CORE]   config: TimeZone = Etc/UTC
    2024-07-31 08:51:12.566  
    DEBUG [SERVE] Data source initialized
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
    

**Good to go!**

- Now you can test the API endpoint using Postman, as shown below:
    
    <center>
      <img src="/resources/stacks/talos/image2.png" alt="Talos" style="width:40rem; border: 1px solid black; padding: 5px;" />
    </center>

    You can even hit the endpoint `/doc/postman?apikey='xxxxxxxxx'` to download the postman collection and import the `.json` collection into postman.
    
- Authenticate the API endpoints by passing the API Key on [DataOS CLI](/resources/stacks/cli_stack/), as query param as shown below.
    
    ```bash
    curl --location 'https://liberal-donkey.dataos.app/talos/pubic:talos-test/api/table?apikey=xxxx' 
    ```    

