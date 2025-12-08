# Build Workflows for Transformed Output Datasets

!!! info "Overview"
    You’ve already transformed raw, unstructured data from Azure Blob into structured tables in Postgres during the first part of the foundations learning path. Now, your next challenge is to derive actionable insights from this structured data— insights that sales and marketing teams can consume. In this step, we’ll build Flare workflows to ingest and transform data into two strategic outputs. These workflows demonstrate complex SQL logic and joins, and also show how you can support analytics to drive business decisions by providing enriched datasets as output.

---

## 📘 Scenario

Your business stakeholders—especially in sales and marketing—need ready-to-use insights to improve cross-selling strategies, campaign targeting, and product bundling decisions. 

To meet this need, you’ll create two output datasets from the curated source data:

- **Product Affinity Matrix**: Reveals how product categories are related based on customer purchasing patterns. (e.g., “Customers who buy wine often buy cheese.”)

- **Cross-Sell Recommendations**: Segments customers by engagement risk and pairs them with tailored product combinations to drive next-best actions.

---

<aside class="callout">
🗣 
Some steps in this module require permissions typically granted to DataOS Operators. Hence, before diving into building data pipelines, you need to ensure you have the `Operator` tag. Contact the training team for assistance.
</aside>

## Step 1: Create Flare Workflows

You’ll build two Flare workflows in this step— one for each output dataset. These workflows will read from your structured Postgres tables and write the results into Lakehouse for scalable downstream access.

<aside class="callout">

🗣 It’s important to note that these workflows are powered by a <b>Source-aligned Data Product</b>, which acts as a curated, trusted foundation for all downstream consumer Data Products. This separation of responsibilities ensures that raw data is consistently processed, quality-checked, and made analytics-ready—so your consumer-aligned products focus purely on delivering business value.

</aside>

### **Creating product affinity matrix output**
Analyzes co-purchase patterns between product categories to identify cross-category buying behavior.

??? "Show YAML Template"
    ```yaml
    # Important: Replace 'abc' with your initials to personalize and distinguish the resource you’ve created.
    version: v1
    name: wf-affinity-matrix-data-abc
    type: workflow
    tags:
      - crm
    description: Ingesting a matrix showing the affinity score between all product categories.
    workflow:
      dag:
        - name: dg-affinity-data
          description: A matrix showing the affinity score between all product categories (e.g., customers who buy wine are X% likely to also buy meat). 
          spec:
            tags:
              - crm
            stack: flare:7.0
            compute: runnable-default
            stackSpec:
              driver:
                coreLimit: 2000m
                cores: 1
                memory: 1000m
              executor:
                coreLimit: 2000m
                cores: 1
                instances: 1
                memory: 2000m
              job:
                explain: true
                logLevel: INFO
                inputs:                # Change the depotname
                  - name: product_data
                    dataset: dataos://postgresabc:public/product_data?acl=rw
                    driver: org.postgresql.Driver
                    format: jdbc

                steps:
                  - sequence:
                      - name: affinity_view
                        sql: >
                            SELECT 
                              customer_id,
                              CASE
                                WHEN rand() < 0.2 THEN 'Wines'
                                WHEN rand() < 0.4 THEN 'Meats'
                                WHEN rand() < 0.6 THEN 'Fish'
                                WHEN rand() < 0.8 THEN 'Sweet Products'
                                ELSE 'Fruits'
                              END AS product_category
                            FROM product_data
                        
                      - name: final
                        sql: >
                            SELECT 
                              cp1.product_category AS category_1,
                              cp2.product_category AS category_2,
                              CAST((COUNT(DISTINCT cp1.customer_id) * 4/ 10.0) AS DECIMAL(10,2)) AS product_affinity_score
                            FROM affinity_view as cp1
                            JOIN affinity_view as cp2 ON cp1.customer_id != cp2.customer_id AND cp1.product_category != cp2.product_category
                            GROUP BY cp1.product_category, cp2.product_category

                outputs:
                  - name: final
                    dataset: dataos://lakehouse:crm_data/product_affinity_matrix?acl=rw
                    format: Iceberg
                    options:
                      saveMode: overwrite
                      iceberg:
                        properties:
                          write.format.default: parquet
                          write.metadata.compression-codec: gzip
                        # partitionSpec:
                        #   - type: day
                        #     column: date_time
                        #     name: day

    ```

    
### **Creating cross-sell recommendations output**

Segments customers by risk and maps them to personalized product pairings.

??? "Show YAML Template"
    ```yaml
    # Important: Replace 'abc' with your initials to personalize and distinguish the resource you’ve created.
    version: v1  # v1
    name: wf-cross-sell-data
    type: workflow
    tags:
      - crm
    description: Ingesting customer segments.
    workflow:
      dag:
        - name: dg-cross-data
          description: Segment the customers into groups based on churn risk with the different campaign recommendations for retention. 
          spec:
            tags:
              - crm
            stack: flare:7.0
            compute: runnable-default
            stackSpec:
              driver:
                coreLimit: 2000m
                cores: 1
                memory: 1000m
              executor:
                coreLimit: 2000m
                cores: 1
                instances: 1
                memory: 2000m
              job:
                explain: true
                logLevel: INFO
                inputs:
                  - name: product_data
                    dataset: dataos://postgresabc:public/product_data?acl=rw
                    driver: org.postgresql.Driver
                    format: jdbc

                steps:
                  - sequence:
                      - name: final
                        sql: >
                          SELECT 
                            customer_id,
                            CASE 
                              WHEN rand() < 0.33 THEN 'High Risk'
                              WHEN rand() < 0.66 THEN 'Moderate Risk'
                              ELSE 'Low Risk'
                            END AS customer_segments,
                            CASE 
                              WHEN rand() < 0.33 THEN CASE WHEN rand() < 0.5 THEN 'Pair Wine with Meat' ELSE 'Pair Fish with Sweet Products' END
                              WHEN rand() < 0.66 THEN CASE WHEN rand() < 0.5 THEN 'Pair Meat with Fruits' ELSE 'Pair Wine with Fish' END
                            ELSE 
                                CASE WHEN rand() < 0.5 THEN 'Pair Fruits with Sweet Products' ELSE 'Pair Wine with Fruits' END 
                            END AS cross_sell_recommendations
                          FROM product_data
              
                outputs:
                  - name: final
                    dataset: dataos://lakehouse:crm_data/cross_sell_recommendations?acl=rw
                    format: Iceberg
                    options:
                      saveMode: overwrite
                      iceberg:
                        properties:
                          write.format.default: parquet
                          write.metadata.compression-codec: gzip
                        # partitionSpec:
                        #   - type: day
                        #     column: date_time
                        #     name: day
    ```


<aside class="callout">
🗣 
For this example, the `lakehouse` depot has already been created in the training instance. Please open the Operations app to confirm its existence.
</aside>

## 🎯 Your actions

1. Review Workflow Templates

    Use the provided YAML templates for both **affinity** and **recommendation** outputs. Review the UDL properties, inputs, and outputs before deployment.

2. Customize the SQL Logic

    Adapt the transformation SQL to align with your business logic (e.g., segmentation thresholds, product mappings).

3. Create a Workspace (if needed) 

    Create a workspace using the following command:

    ```bash
    dataos-ctl workspace create -n <workspace-name>
    ```

4. Deploy Your Workflow

    ```bash

    dataos-ctl apply -f <workflow-file.yaml> -w <workspace-name>
    ```

5. Monitor Execution in Operations App
    
    Use the Operations app to monitor logs and ensure successful execution.

6. Verify output in Workbench
   
   Open Workbench, and explore the generated datasets under:

    lakehouse → crm_data → product_affinity_matrix  
    lakehouse → crm_data → cross_sell_recommendations

## Checklist before moving on

- ✅ Flare workflows created and deployed using `dataos-ctl`  
- ✅ Jobs executed successfully (verified in Operations app)  
- ✅ Datasets verified in Workbench  
- ✅ Outputs match expected schema and business logic  

---

## Next step

Now that you’ve created these refined output datasets, the next step is to create a business-ready **semantic model** so consumers can easily explore them on Data Product Hub or using **APIs**.

👉 [Go to: Define the Semantic Model](/learn/dp_foundations2_learn_track/create_semantic_model/)


