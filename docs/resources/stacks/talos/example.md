# Covid-19 Example

In this example, we utilized the WHO COVID-19 dataset to expose data on countries, maximum cases, minimum cases, reports, and WHO regions through an API using Talos.

## Pre-requisites

- Extract the zip and initialize it with Bitbucket. [Talos Zip](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/e5d3ccb1-9156-4caa-b024-3a6c0c6fab5a/Untitled.zip)
    

## Steps

The following steps are followed to set up the Talos for this example:

1. The repository includes the following components: `config.yaml`, an `apis` folder containing SQL and YAML files, a `database` folder with database configuration files, and `docker-compose.yaml`. Below is the `config.yaml` file, which contains the configuration details for Talos.
    
    ```yaml
    name: covid19
    description: A talos app
    version: 0.1.6
    logLevel: ERROR
    auth:
        heimdallUrl: https://liberal-donkey.dataos.app/heimdall
        userGroups:
        - name: reader
          description: This is a reader's group
          includes:
            - roles:id:data-dev
            - roles:id:data-guru
          excludes:
            - users:id:iamgroot
        - name: default
          description: Default group to accept everyone
          includes: "*"
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
          password: '12345678'
          database: covid19
    ```
    
2. The `docker-compose.yaml` manifest file contains the docker image of DataOS as shown below.
    
    ```yaml
    version: "2.2"
    services:
      pg-db:
        build: ./database
        container_name: covid19-db
        environment:
          POSTGRES_USER: postgres
          POSTGRES_PASSWORD: 123456
        ports:
          - "54321:5432"
        networks:
          - app-network
        healthcheck:
          test: [ "CMD-SHELL", "pg_isready -U postgres" ]
          interval: 10s
          timeout: 5s
          retries: 5
          
      talos:
        image: rubiklabs/talos:0.1.6
        ports:
          - "3000:3000"
        volumes:
          - .:/etc/dataos/work
        environment:
          DATAOS_RUN_AS_USER: 
          DATAOS_RUN_AS_APIKEY: 
          DATAOS_FQDN: https://liberal-donkey.dataos.app
        tty: true
        depends_on:
          pg-db:
            condition: service_healthy
        networks:
          - app-network
    
    networks:
      app-network:
        driver: bridge
    ```
    
3. The `apis` folder contains SQL files along with their manifest file.
4. The database folder contains the `docker-compose.yaml`, `Dockerfile`, `install.sh`, `install.sql`, and `WHO-COVID-19-global-data.csv.` As shown below:
    
    ```yaml
    #docker-compose.yaml
    version: '2'
    services:
      db:
        build: ./
        container_name: covid19-db
        environment:
          POSTGRES_USER: postgres
          POSTGRES_PASSWORD: 12345
        ports:
          - 54321:5432
    ```
    
    ```docker
    #Docker file
    FROM library/postgres
    
    RUN apt-get update
    RUN apt-get -y install dos2unix
    
    RUN mkdir /data
    COPY WHO-COVID-19-global-data.csv /data/
    COPY install.sql /data/
    
    COPY install.sh /docker-entrypoint-initdb.d/
    WORKDIR /data/
    RUN dos2unix /docker-entrypoint-initdb.d/*.sh
    ```
    
    ```bash
    # install.sh
    export PGUSER=postgres
    psql <<- SHELL
      ALTER USER postgres WITH SUPERUSER;
      CREATE DATABASE "covid19";
      GRANT ALL PRIVILEGES ON DATABASE "covid19" TO postgres;
    SHELL
    psql -d covid19 -U postgres < /data/install.sql
    ```
    
    ```sql
    
    # install.sql 
    -- Create the cases table
    CREATE TABLE cases (
        Date_reported DATE,
        Country_code VARCHAR(10),
        Country VARCHAR(100),
        WHO_region VARCHAR(50),
        New_cases INTEGER,
        Cumulative_cases INTEGER,
        New_deaths INTEGER,
        Cumulative_deaths INTEGER
    );
    
    -- Copy data from the CSV file into the cases table
    COPY cases(Date_reported, Country_code, Country, WHO_region, New_cases, Cumulative_cases, New_deaths, Cumulative_deaths)
    FROM '/data/WHO-COVID-19-global-data.csv'
    DELIMITER ','
    CSV HEADER;
    ```
    

5. Now use the `docker-compose up` command on the terminal. Now the Talos set-up is ready. you can access the data on your browser using the DataOS API Key as shown below.

<div style="text-align: center;">
  <img src="/resources/stacks/talos/result.png" style="border:1px solid black; width: 60%; height: auto;">
</div>