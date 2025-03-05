# **Applying Data Masking When Exposing Data Through an API**

In Talos, data masking for an API endpoint is implemented by defining user groups based on their segments and dimensions.

1. **Define User Groups**
    
    User groups must be specified in the `config.yaml` file. The following example illustrates the configuration:
    
    ```yaml
    name: employee  # Name of the Talos service  
    description: A talos app  # Description of the Talos application  
    version: "0.1.26-dev"  # Version of the Talos application(String type)  
    logLevel: DEBUG  # Logging level (DEBUG, INFO, WARN, ERROR)  
    
    auth:  
        userGroups:  # Definition of user groups for authentication  
        - name: intern  # Name of the user group  
          description: intern group  # Description of the user group  
          includes:  # Users included in this group   
            - roles:id:data-intern  # Specific role included in the 'intern' group  
          excludes:  # Users explicitly excluded from this group  
            - users:id:blackwidow  # Specific user excluded from the 'intern' group  
    
        - name: datadev  # Name of another user group  
          description: data dev group  # Description of the user group  
          includes:  # Users included in this group  
            - roles:id:data-dev  # Role-based inclusion for the 'data-dev' group  
    
    metrics:  
      type: summary  # Type of metrics collection (summary or histogram)  
      percentiles: [ 0.5, 0.75, 0.95, 0.98, 0.99, 0.999 ]  # Percentile levels for metric reporting  
    
    rateLimit:  
      enabled: true  # Enables rate limiting  
      options:  
        interval:  
          min: 1  # Minimum interval in minutes between requests  
        max: 100  # Maximum allowed requests in the defined interval  
        delayAfter: 4  # Introduces a delay after the specified number of requests in minutes 
    
    cors:  
      enabled: true  # Enables Cross-Origin Resource Sharing (CORS)  
      options:  
        origin: 'https://google.com'  # Specifies allowed origins  
        allowMethods: 'GET'  # Specifies allowed HTTP methods  
    
    cachePath: tmp  # Defines the path for caching  
    sources:  
      - name: pg  # Name of the data source  
        type: depot  # Type of the data source (e.g., depots, lens, etc)  
    
    ```
    
2. **Customize SQL Queries Based on User Groups**
    
    Modify the SQL query in `department.sql` to apply data masking according to the user group. The following example demonstrates how access restrictions can be enforced:
    
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
    
3. **Update Configuration to Activate User Groups**
    
    Modify `department.yaml` to enable user groups and apply the corresponding masking policies:
    
    ```yaml
    urlPath: /departments  # API endpoint for retrieving department data  
    description: Get a list of departments  # Brief description of the API  
    source: pg  # Specifies the data source (as defined in the 'sources' section)  
    
    allow:  # Defines user groups allowed to access this API  
      - intern  
      - datadev 
    
    filters:  # Defines access control filters based on user groups  
      - description: Allow only certain department  # Restricts access to specific departments  
        userGroups:  
          - reader  # Access restricted to 'reader' user group  
          - default  # Access restricted to 'default' user group  
    
      - description: Indian Content Only  # Restricts content to Indian-specific data  
        userGroups:  
          - asian  
          - indian  
    
    depends:  # Specifies external dependencies required for this API  
      - table: departments  # Defines the table used in the API  
        columns:  
          - IT  # Includes the 'IT' column from the departments table  
          - Finance  # Includes the 'Finance' column from the departments table  
    
    ```
    
4. **Enhance API Documentation with Filter Descriptions**

Provide detailed descriptions for filters to clarify how different user groups interact with the API. This documentation ensures that users understand access rules and masked content behavior.
5. **Include External Dependencies for Context**

Document external dependencies, such as tables and columns, to enhance the clarity of the API. This improves usability by providing insights into the underlying data sources.

Once these configurations are applied, the data can be securely exposed via the API while enforcing appropriate data masking.