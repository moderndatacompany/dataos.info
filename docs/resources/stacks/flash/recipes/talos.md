To expose cached datasets via [Talos APIs](https://dataos.info/resources/stacks/talos/), follow the below to use Flash as the source for Talos API.

## Pre-requisites

Before moving on to the steps, please ensure you meet the following requirements.

- [Flash set up](https://www.notion.so/Talos-Documentation-WIP-ea816ed14fd74b769383c815e7908825?pvs=21)
- Docker initialization

## Steps

1. Create a repository, open the repository with a code editor (VS Code), and create a `config.yaml` manifest file and copy the below code. Update the name, description, version, DataOS context, Flash as source type, and source Flash name.
    
    ```yaml
    name: flash
    description: A talos-flash app
    version: 0.1.6
    auth:
      heimdallUrl: https://liberal-donkey.dataos.app/heimdall
    logLevel: 'DEBUG'
    sources:
      - name: flash # source name
        type: flash
        flashName: 'public:flash-service'
    ```
    
2. In the same repository, create `docker-compose.yaml` manifest file, copy the below-provided code, and update the `volumes` path `/home/iamgroot/Desktop/talos-examples/lens` with the actual path of your repository, add your DataOS username and DataOS API key in `DATAOS_RUN_AS_USER` and `DATAOS_RUN_AS_APIKEY` respectively.
    
    ```yaml
    version: "2.2"
    services:
      talos:
        image: rubiklabs/talos:0.1.6
        ports:
          - "3000:3000"
        volumes:
          - .:/etc/dataos/work
        environment:
          DATAOS_RUN_AS_USER: ${{iamgroot}}
          DATAOS_RUN_AS_APIKEY: ${{Dyiuyuidy98837686bbdhkjhugIPOPHGgGHTIOnsd68FH=}}
          DATAOS_FQDN: liberal-donkey.dataos.app
        tty: true
    ```
    
3. Create a folder named `apis` inside the same repository, inside `apis` create the files `customer.sql` which will contain the SQL query, and `customer.yaml` to define the path to access cached data in your API as shown below. 
    
    ```sql
    SELECT * FROM mycustomer LIMIT 20
    ```
    
    ```yaml
    urlPath: /flash/customers
    description: list customers from customer table
    source: flash
    ```
    
4. Now apply the Talos service as mentioned [here](https://dataos.info/resources/stacks/talos/set_up/#steps).