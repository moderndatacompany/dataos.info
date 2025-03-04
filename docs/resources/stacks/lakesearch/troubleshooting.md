# Lakesearch Troubleshooting

After deploying the LakeSearch Service, if its runtime state remains unchanged for an extended period, it may have encountered an issue. Users can check the Service logs to identify potential errors and resolve them. Below are some common errors and their respective solutions.

## `id` is not present in the index_table

If you forget to add the additional column `id` while configuring the LakeSearch Service, the runtime status will remain pending, and the logs will display the following message:

```bash
dataos-ctl log -t service -n testingls -w public -r

INFO[0000] 📃 log(public)...                             
INFO[0001] 📃 log(public)...complete                     

              NODE NAME             │     CONTAINER NAME     │ ERROR  
────────────────────────────────────┼────────────────────────┼────────
  testingls-eacp-d-7f4ccb75d8-rtflh │ testingls-eacp-indexer │        

-------------------LOGS-------------------
10:42AM INF pkg/config/config.go:126 > Loading config... file:///etc/dataos/config/lakesearch.yaml [success]
10:42AM FTL pkg/config/lakesearch.go:227 > column `id` is not present in the index_table: newcity columns schema, mandatory column.

```

**Steps to resolve:**

1. In the Lakesearch Service manifest file, add an additional column in the `index_tables.columns` section as shown below.
    
    ```yaml
          index_tables:
            - name: newcity
              description: "index for cities"
              tags:
                - cities
              properties:
                morphology: stem_en
              columns:
                - name: city_id
                  type: keyword
                - name: zip_code
                  type: bigint  
                - name: id                         #added
                  description: "mapped to row_num"
                  tags:
                    - identifier
                  type: bigint
                - name: city_name
                  type: keyword
                - name: county_name
                  type: keyword
                - name: state_code
                  type: keyword
                - name: state_name
                  type: text
                - name: version
                  type: text
                - name: ts_city
                  type: timestamp
    ```
    
2. Corresponding to this, add an additional column in which the primary key is identified as id in the indexer.base_sql section.
    
    ```yaml
          indexers:
            - index_table: newcity
              base_sql: |
                SELECT 
                  city_id,
                  zip_code,
                  zip_code as id,  # added
                  city_name,
                  county_name,
                  state_code,
                  state_name,
                  version,
                  cast(ts_city as timestamp) as ts_city
                FROM 
                  city
    ```
    
3. Reapply the LakeSearch Service by running the command below. It will update automatically, eliminating the need to delete the existing Service.
    
    ```bash
    dataos-ctl resource apply -f ${{path-to-the-manifest-file}}
    ```
    
    **Expected output:**
    
    ```bash
    INFO[0000] 🛠 apply...                                   
    INFO[0000] 🔧 applying(public) testingls:v1:service...   
    INFO[0002] 🔧 applying(public) testingls:v1:service...updated 
    INFO[0002] 🛠 apply...complete  
    ```
    
4. If no further issues are found, the Service runtime state will change to "running.”
    
    ```bash
    dataos-ctl get -t service -n testingls -w public -r                 
    INFO[0000] 🔍 get...                                     
    INFO[0000] 🔍 get...complete                             
    
        NAME    | VERSION |  TYPE   | WORKSPACE | STATUS |  RUNTIME  |    OWNER     
    ------------|---------|---------|-----------|--------|-----------|--------------
      testingls | v1      | service | public    | active | running:1 | iamgroot  
    
    ```