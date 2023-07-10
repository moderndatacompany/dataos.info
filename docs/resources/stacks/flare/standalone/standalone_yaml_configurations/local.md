# Local

## Read Config

```yaml
version: v1 # Manifest Version
name: local-read-write # Workflow Name
type: workflow # Resource/primitive (here its workflow)
tags: # Tags   
  - standalone
  - read
  - write
description: Sample job # Description
workflow: # Workflow Section
  dag: # Directed Acyclic Graph of Jobs (it has only one job at present can be more than one also)    
  - name: customer # Job Name       
    title: Sample Transaction Data Ingester # Title       
    description: The job ingests customer data from pulsar topic to file source # Job Description 
    spec: # Specs for the job        
      tags: # Tags          
        - standalone
        - read
        - pulsar
      stack: flare:3.0 # Stack Version         
      compute: runnable-default # Compute Type         
      flare:
        job:
          explain: true
          logLevel: INFO #logLevel for the Job
          inputs:
            - name: oms_transactions_data
              inputType: file
              file:
                path: /data/examples/transactions/
                format: json
          outputs: # Output Data Source Section
            - name: finalDf # Name of the output data source
              outputType: file # Datasource output type (here's its file)                
              file: # Datasource outputs specific section                  
                path: /data/examples/dataout/
                format: parquet
          steps: # Transformation Steps Section              
            - sequence: # Sequence                  
              - name: finalDf # Step Name                    
                sql: SELECT * FROM oms_transactions_data # SQL
```
## Write Config

```yaml
version: v1 # Manifest Version
name: local-read-write # Workflow Name
type: workflow # Resource/primitive (here its workflow)
tags: # Tags   
  - standalone
  - read
  - write
description: Sample job # Description
workflow: # Workflow Section
  dag: # Directed Acyclic Graph of Jobs (it has only one job at present can be more than one also)    
  - name: customer # Job Name       
    title: Sample Transaction Data Ingester # Title       
    description: The job ingests customer data from pulsar topic to file source # Job Description 
    spec: # Specs for the job        
      tags: # Tags          
        - standalone
        - read
        - pulsar
      stack: flare:3.0 # Stack Version         
      compute: runnable-default # Compute Type         
      flare:
        job:
          explain: true
          logLevel: INFO #logLevel for the Job
          inputs:
            - name: oms_transactions_data
              inputType: file
              file:
                path: /data/examples/transactions/
                format: json
          outputs: # Output Data Source Section
            - name: finalDf # Name of the output data source
              outputType: file # Datasource output type (here's its file)                
              file: # Datasource outputs specific section                  
                path: /data/examples/dataout/
                format: parquet
          steps: # Transformation Steps Section              
            - sequence: # Sequence                  
              - name: finalDf # Step Name                    
                sql: SELECT * FROM oms_transactions_data # SQL
```


