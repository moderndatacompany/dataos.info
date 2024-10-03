# How to apply data masking while exposing data through an API?

With Talos, you can mask the data for the API endpoint by defining user groups on their segments and dimensions. 

1. To create the user groups, define the user groups in `config.yaml`, as shown below:
    
    ```yaml
    name: employee
    description: A talos app
    version: 0.0.1
    logLevel: DEBUG
    auth:
        heimdallUrl: https://liberal-donkey.dataos.app/heimdall
        userGroups: 
        - name : intern
          description: intern group
          includes: # Users to include in this group
            - users:id:iamgroot
          excludes: # Users to exclude from this group
            - users:id:blackwidow
        - name : datadev
          description: data dev group
          includes: # Users to include in this group
            - roles:id:data-dev
           
    metrics:
      type: summary
      percentiles: [ 0.5, 0.75, 0.95, 0.98, 0.99, 0.999 ]
    rateLimit:
      enabled: true
      options:
        interval:
          min: 1
        max: 100
        delayAfter: 4
    cors:
      enabled: true
      options:
        origin: 'https://google.com'
        allowMethods: 'GET'  
    cachePath: tmp       
    sources:
      - name: pg 
        type: pg
        connection:
          host: pg-db
          port: 5432
          user: postgres
          password: '12345'
          database: employee
    ```
    
2. Customize your SQL query in the `department.sql` example according to the user group as shown below:
    
    ```sql
    SELECT
        -- dynamic data masking
        id,
        department,
        last_name,
        company_role,
        -- column level security
        {% if context.user.userGroup == 'datadev' %}
            annual_salary
        {% else %}
            NULL AS annual_salary
        {% endif %}
    FROM departments
    ```
    
3. Update `department.yaml` to activate the user groups as shown below:
    
    ```yaml
    urlPath: /departments
    description: Get a list of departments
    source: pg
    allow:
      - intern
      - datadev
    filters:
      - description: Allow only certain department
        userGroups:
          - reader
          - default
      - description: Indian Content Only
        userGroups:
          - asian
          - indian
    depends:
      - table: departments
        columns:
          - IT
          - Finance
    ```

- Descriptions for filters explain how various user groups will access content. This improves the API documentation by offering clear guidance for users interacting with the API.

- External dependencies, such as tables and columns, have been included to clarify what the API relies on. This adds context to the API documentation, helping users better understand the data sources involved.

Now you are ready to expose your data via APIs securly.