# Talos for Bigquery
This section provides the configuration guide to set up Talos service for Bigquery.  

## **Prerequisites**

To access the data using API from BigQuery, User need the following:

1. Ensure that the BigQuery project is created.
2. **Access Permissions in GCP**: To successfully execute Talos Service in GCP, the user or service account needs specific permissions to access and retrieve the required data. Here’s a summary of the minimum required permissions:
    - Ingestion Permissions
    - Stored Procedure Permissions
    - Fetch Policy Tags Permissions
    - BigQuery Usage & Lineage Workflow Permissions
    
    If the user has External Tables, please attach relevant permissions needed for external tables, along with the above list of permissions.

3. **Access Permissions in DataOS**: To execute a Scanner Workflow in DataOS, verify that at least one of the following role tags is assigned:
    - **`roles:id:data-dev`**
    - **`roles:id:system-dev`**
    - **`roles:id:user`**

    Use the following command to check assigned roles:

    ```bash
    dataos-ctl user get
    ```

    If any required tags are missing, contact a **DataOS Operator** or submit a **Grant Request** for role assignment.

    Alternatively, if access is managed through **use cases**, ensure the following use cases are assigned:

    - **Manage Talos**
    - **Read Talos**

To validate assigned use cases, refer to the **Bifrost Application Use Cases** section.

4. **Pre-created Bigquery Depot**: Ensure that a Bigquery Depot is already created with valid read access and the necessary permissions to extract metadata. To check the Depot go to the Metis UI of the DataOS or use the following command:

    ```bash
    dataos-ctl get -t depot -a

    #expected outputINFO[0000] 🔍 get...
    INFO[0000] 🔍 get...complete

    | NAME             | VERSION | TYPE  | WORKSPACE | STATUS | RUNTIME | OWNER      |
    | ---------------- | ------- | ----- | --------- | ------ | ------- | ---------- |
    | bigquerydepot    | v2alpha | depot |           | active |         | usertest   |
    ```

    Template for creating BIGQUERY Depot is shown below:

    ```yaml
    name: ${{depot-name}}
    version: v2alpha
    type: depot
    tags:
    - ${{dropzone}}
    - ${{bigquery}}
    owner: ${{owner-name}}
    layer: user
    depot:
    type: BIGQUERY                 
    description: ${{description}} # optional
    external: ${{true}}
    secrets:
        - name: ${{bq-instance-secret-name}}-r
        allkeys: true

        - name: ${{bq-instance-secret-name}}-rw
        allkeys: true
    bigquery:  # optional                         
        project: ${{project-name}} # optional
        params: # optional
        ${{"key1": "value1"}}
        ${{"key2": "value2"}}
    ```

## **Steps**

### **Connect to the data source**

Open the repository in the preferred code editor. Navigate to the `setup` folder and open the `config.yaml` manifest file. This file contains details such as the Talos app name, description, version, authentication information, and source connection settings.

```yaml
name: ${{superstore}}
description: ${{A talos-depot-bigquery app}} # description
version: "0.1.26-test" # The version of the Talos(string)
auth:
  userGroups:
  - name: datadev
    description: data dev group
    includes:
      - users:id:iamgroot
      - users:id:thisisthor
  - name: default
    description: Default group to accept everyone
    includes: "*"
logLevel: ${{'DEBUG'}}
sources: # source details
  - name: ${{bigquerydepot}} # source name
    type: ${{depot}} # source type
```

Update the following attributes within the file to align with the required configurations:

- **name**: Set the Talos app name.
- **description**: Provide a description of the Talos application.
- **version**: Specify the application version.
- **source name**: Update the source system name.
- **source type**: Define the type of source system being used.

<aside class="callout">
🗣 Verify that the source type, if specified as 'Depot,' is active.
</aside>

To know more information about each attribute, please refer to the [Configuration Page](/resources/stacks/talos/configurations/config/).

### **Writing SQL templates**

Open the `apis` folder within the `setup` directory and access the `table.sql` and `table.yaml` files. Update the SQL queries in `table.sql` and modify the `urlPath`, `description`, and `source` fields in `table.yaml` to accurately reflect the API's data access paths and configuration details. 

```yaml
urlPath: /table # output path
description: product list # description
source: ${{bigquerydepot}} # source name
```

Ensure that both the queries and the **YAML** configuration are properly aligned with the API requirements.

Additionally, multiple **SQL** files and their corresponding manifest files can be added within the **apis** folder as needed. This ensures modularity and maintainability of query definitions.

```sql
SELECT * FROM myschema.mytable LIMIT 10;
```
To know more information about each attribute, please refer to the [Configuration Page](/resources/stacks/talos/configurations/apis/).
<aside class="callout">
🗣 A refresh time and refresh expression can be added to the query to improve the caching mechanism. The refresh time specifies the interval at which the data should be refreshed, while the refresh expression defines the conditions under which the refresh should occur.
</aside>

### **Push the changes**

Push the changes to the working source control service (here ‘bitbucket’) repository as shown below:

<center>
  <img src="/resources/stacks/talos/image1.png" alt="Talos" style="width:20rem; border: 1px solid black; padding: 5px;" />
</center>

### **Create a Talos Service manifest file**

- Now create a manifest file for the Service as shown below.
    
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
    
    To know more information about each attribute, please refer to the Configuration Page.
    
- Apply the Service manifest by executing the below command:
    
    ```bash
    dataos-ctl resource apply -f ${{path to the service YAML file }}
    ```
    
- To check if the service is running successfully, execute the following command.
    
    ```bash
    dataos-ctl log -t service -n ${{service-name}} -w ${{workspace}}
    ```
    
    Successful execution will look like the following:
    
    ```bash
    DEBUG [CORE]   config: TimeZone = Etc/UTC
    2025-01-31 08:51:12.566  
    DEBUG [SERVE] Data source   initialized
    2025-01-31 08:51:12.567  DEBUG
    [SERVE] Initializing data source: pg
    2025-01-31 08:51:12.567  DEBUG
    [SERVE] Data source pg initialized
    2025-01-31 08:51:12.567  DEBUG
    [SERVE] Initializing data source: redshift
    2025-01-31 08:51:12.567  DEBUG
    [SERVE] Data source redshift initialized
    2025-01-31 08:51:12.568  
    DEBUG [SERVE] Initializing data source: bigquery
    2025-01-31 08:51:12.568  DEBUG
    [CORE] Initializing profile: bigquery using bigquery driver
    2025-01-31 08:51:12.681  DEBUG
    [CORE] Profile bigquery initialized
    2025-01-31 08:51:12.681  DEBUG [SERVE] Data source bigquery initialized
    2025-01-31 08:51:12.682  
    INFO  [SERVE] Start to load and schedule prefetched data results from data sources to cache layer...
    2025-01-31 08:51:12.689  DEBUG
    [SERVE] profile: bigquery, allow: *
    2025-01-31 08:51:12.690  
    DEBUG [SERVE] profile: talos.cache, allow: *
    2025-01-31 08:51:12.696  DEBUG
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
    2025-01-31 08:51:12.702  
    INFO  [CLI] 🚀 Server is listening at port 3000.
    ```
    
- The data can now be accessed through the API endpoint on platforms such as Postman, Swagger (OpenAPI Specification), and Google APIs Platform, as shown below (in Postman):
    
    <center>
      <img src="/resources/stacks/talos/image2.png" alt="Talos" style="width:40rem; border: 1px solid black; padding: 0px;" />
    </center>

  The endpoint can also be hit as “**/doc/postman?apikey='xxxxxxxxx”** in order to download the postman collection and import the .json collection into postman.

  - Authenticate the API endpoints by passing the API Key on DataOS CLI, as query param as shown below.

  ```bash
  curl -X GET 'https://liberal-donkey.dataos.app/talos/pubic:talos-test/api/table?apikey=xxxx'
  ```    