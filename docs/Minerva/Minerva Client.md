# Minerva Client

There are multiple ways to interact with Minerva.

1. Minerva CLI: This is a command line-based interactive interface for running your queries. 
2. Workbench: [Workbench](../../Getting%20Started%20-%20DataOS%20Documentation/Data%20Management%20Capabilities/GUI/GUI%20Applications/Workbench.md) is a UI-based query interface for your data.
3. Connect via Tableau and Power BI: One can use these popular BI analytics platforms to access data from DataOS, which is exposed through Minerva URL. To know more about integration with these tools, click on [Tableau](../../Integration%20&%20Ingestion/Tableau.md) and [PowerBI](../../Integration%20&%20Ingestion/Power%20BI.md).

This article helps in setting up the minerva-cli for running queries on Minerva via the terminal. There are two ways to install the same -

# Setup

### Approach 1 - With Docker

1. Open the terminal and enter the following command the minerva-cli image. Ensure that Docker is installed and running on your system.
    
    ```bash
    docker pull tmdc/minerva-cli:latest
    ```
    
2. Ensure that it runs properly. It should display a list of supported commands. 
    
    ```bash
    docker run --rm -it --name minerva tmdc/minerva-cli:latest java -jar minerva-cli.jar --help 
    ```
    
3. Set up an alias for future ease.
    
    ```bash
    echo 'alias minerva="docker run --rm -it --name minerva tmdc/minerva-cli:latest java -jar minerva-cli.jar"' >> ~/.bashrc && source ~/.bashrc
    ```
    
4. Check that the alias-created works -
    
    ```bash
    minerva --help
    ```
    

### Approach 2 - With Executable Jar

<br>

> 💡 If you are unable to execute the steps given in the previous section, you can use the equivalent `java` command with the `-jar` option to run the CLI. Please note that Minerva client runs on JVM 11 or higher.

1. Open the terminal and enter the following command to ensure that you have Java 11 or higher.

    <pre><code><b>java --version</b></code></pre>

1. Download `minerva-cli` from here -
    
    ```bash
    https://github.com/anismiles/anismiles.github.com/blob/master/minerva-cli-388.jar 
    ```
    
2. Ensure that `minerva-cli` runs properly. It should display a list of supported commands -
    
    ```bash
    java -jar minerva-cli-388.jar --help
    ```
    
3. Set up an alias for future ease -
    
    ```bash
    echo alias 'minerva="java -jar minerva-cli-388.jar"' >> ~/.bashrc && source ~/.bashrc
    ```
    
4. Check the alias-created runs -
    
    ```bash
    minerva --help
    ```
    

# Tutorial

### Connect

You can connect with any running Minerva cluster using the below command -

<pre><code>minerva --server https://tcp.<<b>DATAOS_INSTANCE_FQDN</b>>:7432 \
     --user <<b>USER_NAME</b>> \
     --apikey <<b>DATAOS_API_KEY</b>> \
     --cluster-name=<<b>CLUSTER_NAME</b>>
</pre></code>

### Query

The commands below help you get started -

- List Catalogs
    
    ```bash
    ➜ Minerva# show catalogs;
     Catalog 
    ---------
     icebase 
     system  
    (2 rows)
    
    Query 20220714_030402_00049_izefc, FINISHED, 2 nodes
    Splits: 20 total, 20 done (100.00%)
    0.66 [0 rows, 0B] [0 rows/s, 0B/s]
    
    ```
    
- List Schemas within a catalog
    
    ```bash
    ➜ Minerva# show schemas in icebase;
           Schema       
    --------------------
     default            
     gcd_raw            
     gcd_report         
     gcd_sandbox        
     gcd_views          
     gcdcore_bronze     
     information_schema 
     locationdb         
     minerva_events     
     quality_summary    
     sandbox            
     surveys            
     sys01              
    (13 rows)
    
    Query 20220714_030408_00050_izefc, FINISHED, 2 nodes
    Splits: 20 total, 20 done (100.00%)
    0.66 [13 rows, 199B] [19 rows/s, 302B/s]
    
    ```
    
- Set Default Catalog
    
    ```bash
    ➜ Minerva# USE icebase.surveys;
    	USE
    ```
    
- Show Tables
    
    ```bash
    ➜ Minerva:icebase.surveys# SHOW tables;
    	           Table           
    	---------------------------
    	 combined_survey_list      
    	 legacy_surveys            
    	 legacy_surveys_fixes      
    	 qualtrics_questions_table 
    	 qualtrics_responses_table 
    	 qualtrics_survey_list     
    	 sharepoint_metadata       
    	(7 rows)
    	
    	Query 20220714_030421_00054_izefc, FINISHED, 2 nodes
    	Splits: 20 total, 20 done (100.00%)
    	0.64 [7 rows, 263B] [10 rows/s, 410B/s]
    ```
    

- Describe Table
    
    ```bash
    ➜ Minerva:icebase.surveys# describe qualtrics_questions_table;
              Column           |         Type          | Extra | Comment 
    ---------------------------+-----------------------+-------+---------
     __metadata                | map(varchar, varchar) |       |         
     survey_id                 | varchar               |       |         
     block_id                  | varchar               |       |         
     block_description         | varchar               |       |         
     items                     | varchar               |       |         
     groups                    | varchar               |       |         
     regions                   | varchar               |       |         
     sbs_question_selector     | varchar               |       |         
     choice_recode_value       | integer               |       |         
    
    (9 rows)
    
    Query 20220714_030447_00055_izefc, FINISHED, 2 nodes
    Splits: 20 total, 20 done (100.00%)
    0.65 [25 rows, 2.24KB] [38 rows/s, 3.47KB/s]
    ```
    

- Show Table Data
    
    ```bash
    ➜ Minerva:icebase.surveys# SELECT question_number, question_name, groups FROM qualtrics_questions_table LIMIT 10;
     question_number | question_name | groups 
    -----------------+---------------+--------
                   1 | Q118          | NULL   
                   1 | Q118          | NULL   
                   1 | Q118          | NULL   
                   1 | Q118          | NULL   
                   1 | Q118          | NULL   
    (5 rows)
    
    Query 20220714_030531_00056_izefc, FINISHED, 2 nodes
    Splits: 19 total, 13 done (68.42%)
    0.66 [60 rows, 1.2MB] [91 rows/s, 1.82MB/s]
    ```
    
- Quit CLI
    
    ```bash
    ➜ Minerva:icebase.surveys# quit
    ```
    

### Export results as CSV

You can use `output-format` to specify the result format and export or save the result of your query to a CSV file e.g. -

```bash
➜  minerva \
		 --server https://tcp.<DATAOS_INSTANCE>:7432 \
	   --user <USER_NAME> \
		 --apikey <API_KEY> \
		 --cluster-name=<CLUSTER_NAME> \
		 --execute "
SELECT * FROM icebase.surveys.qualtrics_responses_table R 
INNER JOIN icebase.surveys.sharepoint_metadata M 
ON R.survey_id=M.surveyid 
WHERE M.templatetypeltemplatecategory like '%Workplace' LIMIT 10
" \
--output-format CSV > result.csv
```

> With the `execute` option, minerva-cli uses the batch (non-interactive) mode, so the query automatically exits after running.