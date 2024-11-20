# Creating Data APIs

In this section of the module, you'll be building data APIs to create data applications. This guide provides the step-by-step instructions you need to build data APIs within DataOS.

## Scenario

As a Data Product developer, your goal is to create an API that delivers product recommendations based on sales data. You will use DataOS to build this API, applying product affinity analysis to identify items frequently bought together. The resulting API will serve as the backbone of a recommendation system, helping the marketing team craft targeted promotions and boosting sales by enhancing customer experience.

## What do you need to get started?

To make the most out of this part, you’ll need:

- Permission or use case assigned to be able to create the API.
- Version control:- Git and Bitbucket.

## Steps to to build data API

Here, you’ll find step-by-step instructions to build data API. 

1. You create a bit-bucket repository and clone it on your local system.
2. Using VS code, you open the repository and create an ‘apis’ folder and a `config.yaml` manifest file.
    - config.yaml
        
        ```yaml
        # config.yaml
        name: affinity_cross_sell_api
        description: An api for sending affinity scores, enabling real-time cross-sell recommendations. 
        version: 0.1.19-dev
        auth:
          heimdallUrl: https://splendid-shrew.dataos.app/heimdall
          userGroups:
          - name : datadev
            description: data dev group
            includes:
              - users:id:iamgroot
              - users:id:thor
          - name: default
            description: Default group to accept everyone
            includes: "*"
        logLevel: 'DEBUG' 
        cachePath: tmp
        sources:
          - name: lens # profile name
            type: lens
            lensName: 'public:cross-sell-affinity'
        metrics:
          type: summary
          percentiles: [ 0.5, 0.75, 0.95, 0.98, 0.99, 0.999 ]
        ```
        
    
    ![image.png](/learn/dp_developer_learn_track/data_api/image.png)
    
3. Inside the apis folder create two SQL files named `cp_insights.sql` and `product_affinity.sql` and two manifest files corresponding to the SQL files named `cp_insights.yaml` and `product_affinity.yaml`. And push the changes.
    - cp_insights.sql
        
        ```sql
        {% cache %}
        SELECT 
          customer_id,
          CASE 
            WHEN random() < 0.33 THEN 'High Risk'
            WHEN random() < 0.66 THEN 'Moderate Risk'
            ELSE 'Low Risk'
          END AS customer_segments,
          CASE 
            WHEN random() < 0.33 THEN CASE WHEN random() < 0.5 THEN 'Pair Wine with Meat' ELSE 'Pair Fish with Sweet Products' END
            WHEN random() < 0.66 THEN CASE WHEN random() < 0.5 THEN 'Pair Meat with Fruits' ELSE 'Pair Wine with Fish' END
          ELSE 
              CASE WHEN random() < 0.5 THEN 'Pair Fruits with Sweet Products' ELSE 'Pair Wine with Fruits' END 
          END AS cross_sell_recommendations
        FROM cross_sell_cache
        
        {% endcache %}
        ```
        
    - cp_insights.yaml
        
        ```yaml
        urlPath: /cross_sell
        description: This endpoint exposes individual customer purchase data and recommended cross-sell products for integration into CRM or sales platforms. 
        source: lens
        response:
          - name: customer_id
          - name: customer_segments
          - name: cross_sell_recommendations
        cache:
          - cacheTableName: 'cross_sell_cache'
            sql: SELECT product_customer_id as customer_id FROM product
            source: lens
        ```
        
    - product_affinity.sql
        
        ```sql
        {% cache %}
        
         with random_cat as(select customer_id,   CASE
              WHEN random() < 0.2 THEN 'Wines'
              WHEN random() < 0.4 THEN 'Meats'
              WHEN random() < 0.6 THEN 'Fish'
              WHEN random() < 0.8 THEN 'Sweet Products'
              ELSE 'Fruits'
            END AS product_category from affinity_cache) 
          SELECT 
            cp1.product_category AS category_1,
            cp2.product_category AS category_2,
            COUNT(DISTINCT cp1.customer_id)*4/10.0 AS product_affinity_score
          FROM random_cat cp1
            INNER JOIN random_cat cp2 
          ON cp1.customer_id = cp2.customer_id AND cp1.product_category <> cp2.product_category 
          group by 1,2
        {% endcache %}
        ```
        
    - product_affinity.yaml
        
        ```yaml
        urlPath: /affinity
        description: This endpoint provides affinity scores between product categories, enabling real-time cross-sell recommendations. 
        source: lens
        response:
          - name: category_1
          - name: category_2
          - name: customer_id
          - name: product_affinity_score
        cache:
          - cacheTableName: 'affinity_cache'
            sql: SELECT product_customer_id as customer_id,product_category FROM product
            source: lens
        ```
        
    
    ![image.png](/learn/dp_developer_learn_track/data_api/image1.png)
    
4. Create an Instance Secret that will have the Bitbucket username and password (Butbucket App password) for security, and refer the Instance Secret in Talos Service.
  ```yaml
  name: icebasedev-rw
  version: v1
  type: instance-secret
  description: "abfss v2 alpha depot password; acl=rw"
  layer: user
  instance-secret:
    type: key-value-properties
    acl: rw
    data:
      username: imagroot57
      password: AyuhksPltysjnjsuog86734ggTUIBRO
  ```

5. Apply the Instance Secret manifest file.

    ```shell
    dataos-ctl apply -f /home/office/secrets/instance_secret.yaml
    ```


6. Create a Talos Service manifest file and refer to the Bitbucket repository as the path.
    - service.yaml
        
        ```yaml
        name: affinity-cross-sell-api
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
            path: /talos/public:affinity-cross-sell-api
            noAuthentication: false
          replicas: 1
          logLevel: DEBUG
          compute: runnable-default
          envs:
            TALOS_SCHEMA_PATH: talos/setup/consumption_ports/dataApi
            TALOS_BASE_PATH: /talos/public:affinity-cross-sell-api
          resources:
            requests:
              cpu: 100m
              memory: 128Mi
            limits:
              cpu: 500m
              memory: 512Mi
          stack: talos:1.0
          dataosSecrets:
            - name: bitbucket-cred
              allKeys: true
          stackSpec:
            repo:
              url: https://bitbucket.org/mywork15/talos
              projectDirectory: talos/setup/consumption_ports/dataApi
              syncFlags:
                - --ref=main
        ```
        
7. Apply the Service manifest file using CLI, or you can refer the Talos Service manifest path in the Bundle Resource to apply the Talos Service along with the other Resources.
    
```shell
dataos-ctl apply -f /home/iamgroot/talos/setup/service.yaml
```

### **Good to go!**
    
Authenticate the API endpoints by passing the API Key on [DataOS CLI](/resources/stacks/cli_stack/) terminal, as query param as shown below.
    
```bash
curl --location 'https://liberal-donkey.dataos.app/talos/pubic:talos-test/api/table?apikey=xxxx' 
``` 
