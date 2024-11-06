# Setting Up Data APIs on Lens with Talos

This document provides step-by-step instructions for setting up Data APIs on Lens using Talos within DataOS. This document will enable users to:

- Create a config file for Talos API definition for Lens.
- Add SQL query and manifest files for API paths.
- Push the code to a hosted code repository.
- Configure an Instance Secret to securely manage code repository access.
- Define and deploy a Talos Service to set up a Data API on deployed Lens.

## Prerequisites

- Ensure Lens is deployed in DataOS. Refer to the [Lens documentation](/resources/lens/) for setup instructions.

## Steps

### **Step 1: Initialize a Git repository**
- Create a new project directory.
- Initialize a Git repository within the directory.

### **Step 2: Prepare the configuration file**
- In the project directory, open a code editor (e.g., Visual Studio Code).
- Create a file named `config.yaml` and add the following configuration:
```yaml
name: cross_sell_api # Replace the name with your API name
description: A Data API on top of Lens using Talos. # API description
version: 0.1.1 # API Version
auth:
  heimdallUrl: https://liberal-donkey.dataos.app/heimdall # Replace the Heimdall URL with your environments
  userGroups: # User Groups
    - name: datadev
      description: Data dev group
      includes:
        - users:id:thor
        - users:id:iamgroot
    - name: default
      description: Default group to include everyone
      includes: "*"
logLevel: 'DEBUG' # Log Level
sources:
  - name: lens # Source name
    type: lens # Source Type
    lensName: 'public:cross-sell-affinity' # Lens Name format '<workspace>:<lens-name>'
```
- Adjust the values for `name`, `description`, `version`, `heimdallUrl`, `userGroups` and `lensName` to suit your environment. Refer to the [Talos config.yaml attribute documentation](/resources/stacks/talos/configurations/config/) for detailed descriptions.

### **Step 3: Add SQL query and manifest files**

- Inside the project directory, create a folder named `apis`.
- Within the `apis` folder:
    - Create the `product_affinity.sql` containing the SQL query:

        ```sql
        --- product_affinity.sql
        SELECT affinity_score FROM product LIMIT 20
        ```

    - Create a corresponding `sales.yaml` manifest file defining the API path:

          ```yaml
          # product_affinity.yaml
          urlPath: /affinity
          description: This endpoint provides affinity scores. 
          source: lens
          ```

- Each `.sql` file should have a matching `.yaml` manifest file to ensure correct API path mappings.

### **Step 4: Push the code to the repository**

After following the above steps, push the code to the code repository. The repository structure will resemble the following:

```
project-directory/
├── config.yaml
├── apis/
│   ├── product_affinity.sql
│   └── product_affinity.yaml
```

### **Step 5: Configure Instance Secret**

!!!info
    For setups using a public code repository, this step can be skipped entirely. 

    In cases where the code is stored in a private code repository, Instance Secrets become necessary to securely store and access repository credentials. This enables Talos Service to sync with the repository without exposing sensitive information in the configuration files.

- If you are using Bitbucket, to securely store Bitbucket credentials so that the Talos Service could securely access them, create an Instance Secret manifest file named `secret.yml` with the following content:

```yaml
name: bitbucket-r
version: v1
type: instance-secret
description: "Bitbucket credentials"
layer: user
instance-secret:
  type: key-value
  acl: r
  data:
    GITSYNC_USERNAME: "iamgroot7340"  # Replace with actual Bitbucket username
    GITSYNC_PASSWORD: "abcdefghijklmnopqrstuv"  # Replace with Bitbucket app password
```

- To generate an app password in Bitbucket:
    - Navigate to **Settings > Personal Bitbucket settings > App passwords**.
          <center>
            <img src="/resources/stacks/talos/app.png" alt="Talos" style="width:30rem; border: 1px solid black; padding: 5px;" />
          </center>
    - Create a new app password and include it in `secret.yaml`.

- Apply the `secret.yaml` file to DataOS:

    ```bash
    dataos-ctl resource apply -f /path/to/secret.yaml
    ```

The process remains the same for other hosted code repository such as GitHub, and AWS Codecommit with slight variations in the `data` section of Instance Secret manifest file. For more details, refer to the following [link](/resources/instance_secret/#templates).

### **Step 6: Define the Talos Service manifest**

- In the project directory, create `service.yaml` to configure the Talos Service, specifying details like `servicePort`, `path`, and `resources`:

    ```yaml
    name: cross-sell-api 
    version: v1
    type: service
    tags:
      - service
      - dataos:type:resource
      - dataos:resource:service
      - dataos:layer:user
    description: Talos Service
    workspace: public
    service:
      servicePort: 3000
      ingress:
        enabled: true
        stripPath: true
        path: /talos/public:cross-sell-api
        noAuthentication: false
      replicas: 1
      logLevel: DEBUG
      compute: runnable-default
      envs:
        TALOS_SCHEMA_PATH: talos/setup/consumption_ports/project-directory # Path to the project directory
        TALOS_BASE_PATH: /talos/public:cross-sell-api # Base Path (Format /talos/<workspace>:<api-name>)
      resources:
        requests:
          cpu: 100m
          memory: 128Mi
        limits:
          cpu: 500m
          memory: 512Mi
      stack: talos:1.0
      dataosSecrets: # For public code repository you can commented out the entire `dataosSecrets` attribute
        - name: bitbucket-cred # Replace with Instance Secret name
          allKeys: true
      stackSpec:
        repo:
          url: https://bitbucket.org/mywork/talos # Repository URL
          projectDirectory: talos/setup/consumption_ports/project-directory # Project directory path
          syncFlags: # Branch
            - --ref=main
    ```

- Refer to the [Talos Service configuration documentation](/resources/stacks/talos/configurations/service/) for attribute descriptions.


### **Step 7: Deploy the Talos Service**

- Run the following command to apply the `service.yaml` file:

    ```bash
    dataos-ctl resource apply -f /path/to/service.yaml
    ```

- Verify the deployment by checking service logs:

    ```bash
    dataos-ctl log -t service -n ${{service-name}} -w ${{workspace}}
    ```

   Logs will display successful initialization messages, confirming the service is running.

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

## Testing the API

- Use Postman to test the API endpoint.
- Download the Postman collection by hitting the endpoint `/doc/postman?apikey='xxxxxxxxx'` and importing the `.json` file into Postman. Provide the `DATAOS_USER_APIKEY` for Authorization in Bearer Token Auth Type.
    <center>
      <img src="/resources/stacks/talos/image2.png" alt="Talos" />
    </center>
- To test the endpoint via CLI, use `curl` with the API key as a query parameter:

    ```shell
    curl --location 'https://liberal-donkey.dataos.app/talos/public:cross-sell-api/api/affinity?apikey=xxxx'
    ```