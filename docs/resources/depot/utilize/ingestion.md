# Data ingestion and transformation

A Depot can be used further for data ingestion and transformation through [Flare Stack](/resources/stacks/flare/). To learn more about the Flare Stack, please refer to this link.

**For example:**

The below manifest file defines a Flare job, `wf-vendor-insights`, for ingesting and transforming vendor insights data from poss3 Depot into the Lakehouse Depot. It includes a DAG node, `dg-vendor-insights`, which processes `promotional_data` from a CSV dataset in poss3 and outputs `transformed_data` as an Iceberg table in Lakehouse. The Workflow specifies compute resources for execution, with a driver and executor configuration limiting cores and memory. The transformation logic applies an SQL query that extracts key vendor attributes, including organization details, contact information, certifications, and category identifiers, while also generating a row number using `row_number() OVER (ORDER BY id)`. The resulting dataset is saved in Iceberg format with Parquet storage and gzip compression, ensuring optimized analytics and efficient querying.


```yaml
version: v1
name: wf-vendor-insights
type: workflow
tags:
    - vendor.insights
    - Tier.Gold
description: The job is to ingest vendor-insights from poss3 into Lakehouse.
workflow:
    title: promotional
    dag:
    - name: dg-vendor-insights
        description: The job is to ingest vendor-insights from poss3 into Lakehouse.
        title: organization  data 
        spec:
        tags:
            - vendor.insights
        stack: flare:6.0
        compute: runnable-default
        stackSpec:
            driver:
            coreLimit: 1200m
            cores: 1
            memory: 1024m
            executor:
            coreLimit: 1200m    
            cores: 1
            instances: 1
            memory: 1024m
            job:
            explain: true
            inputs:
                - name: promotional_data
                dataset: dataos://poss3:promo_effectiveness/target_count02.csv?acl=rw
                format: csv
                options: 
                    inferSchema: true

            logLevel: INFO
            outputs:
                - name: transformed_data
                dataset: dataos://lakehouse:promo_effectiveness/vendor_subscription_insight?acl=rw
                format: Iceberg
                description: The job is to ingest vendor data from S3 into lakehouse.
                tags:
                    - vendor.insights
                options:
                    saveMode: overwrite
                    iceberg:
                    properties:
                        write.format.default: parquet
                        write.metadata.compression-codec: gzip
                title: vendor data

            steps:
                - sequence:
                    - name: transformed_data
                    sql: >
                        select 
                            messagekey,
                            id,
                            organization_id,
                            unique_entity_id,
                            state_of_incorporation,
                            business_type,
                            no_dbe_designations,
                            emergency_disaster,
                            emergency_health,
                            emergency_other,
                            created_at,
                            updated_at,
                            doing_business_as,
                            doing_business_as_keyword,
                            ein,
                            duns,
                            name,
                            organization_name_keyword,
                            website,
                            address1,
                            address2,
                            city,
                            country_code,
                            state,
                            zip_code,
                            billing_address1,
                            billing_address2,
                            billing_city,
                            billing_country_code,
                            billing_state,
                            billing_zip_code,
                            description,
                            phone_country,
                            phone,
                            phone_ext,
                            fax_phone_country,
                            fax_phone,
                            fax_phone_ext,
                            categories_ids,
                            categories_codes,
                            nigp_categories,
                            naics_categories,
                            unspsc_categories,
                            users_emails,
                            users_ids,
                            subscribed_governments_ids,
                            certification_ids,
                            self_reported_certifications,
                            verified_certifications,
                            vendor_list_ids,
                            private_vendor_lists,
                            public_vendor_lists,
                            ethnicities,
                            row_number() over (order by id) as row_num 
                        from  promotional_data
```

