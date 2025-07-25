# Setting Up CLI Client

## Connecting to Minerva

To set up the Minerva Client or minerva-cli and run queries on Minerva via the terminal, there are two approaches:

### **Setup**

#### **Approach 1 - Docker**

- Open the terminal and pull the minerva-cli image by executing the following command. Ensure that Docker is installed and running on your system.

    ```bash
    docker pull tmdc/minerva-cli:latest
    ```

- To verify that the installation is successful, run the following command. It should display a list of supported commands.

    ```bash
    docker run --rm -it --name minerva tmdc/minerva-cli:latest java -jar minerva-cli.jar --help
    ```

- To set up an alias for future ease, execute the following command.

    ```bash
    echo 'alias minerva="docker run --rm -it --name minerva tmdc/minerva-cli:latest java -jar minerva-cli.jar"' >> ~/.bashrc && source ~/.bashrc
    ```

- Confirm that the alias has been created by running the following command.

    ```bash
    minerva --help
    ```

#### **Approach 2 - Executable Jar**

<aside>

💡 If you encounter issues executing the steps mentioned in the previous section, you can use the equivalent `java` command with the `-jar` option to run the CLI. Please note that the Minerva client runs on JVM 11 or higher.

</aside>

- Open the terminal and ensure that you have Java 11 or a higher version installed by running the following command:

    ```bash
    java --version
    ```

- Download the `minerva-cli` JAR file from [here](https://github.com/anismiles/anismiles.github.com/blob/master/minerva-cli-388.jar).

- To verify that `minerva-cli` runs properly, execute the following command. It should display a list of supported commands.

    ```bash
    java -jar minerva-cli-388.jar --help
    ```

- Set up an alias for future ease using the following command.

    ```bash
    echo alias 'minerva="java -jar minerva-cli-388.jar"' >> ~/.bashrc && source ~/.bashrc
    ```

- Confirm that the created alias works correctly.

    ```bash
    minerva --help
    ```

### **Connecting to Minerva**

To connect with a running Minerva Cluster, use the following command:

```bash
minerva --server https://tcp.{{dataos instance fqdn}}:7432 \
     --user {{user id}} \
     --apikey {{dataos api key}} \
     --cluster-name={{CLUSTER_NAME}}
```


## Connecting to Themis

<aside class="callout">

🗣 If you encounter issues executing the steps mentioned in the previous section, you can use the equivalent <code>java</code> command with the <code>-jar</code> option to run the CLI. Please note that the Trino client runs on JVM 11 or higher.

</aside>

- Open the terminal and ensure that you have Java 11 or a higher version installed by running the following command:
    
    ```bash
    java --version
    ```
    
- Download the `trino-cli` JAR file from [here](https://repo1.maven.org/maven2/io/trino/trino-cli/435/trino-cli-435-executable.jar).
- To verify that `trino-cli` runs properly, execute the following command. It should display a list of supported commands.
    
    ```bash
    java -jar trino-cli-435-executable.jar --help
    ```
    
- Set up an alias for future ease using the following command.
    
    ```bash
    # For bash terminals
    echo alias 'minerva="java -jar minerva-cli-388.jar"' >> ~/.bashrc && source ~/.bashrc
    # For zsh terminals
    echo alias 'trino="java -jar trino-cli-435-executable.jar"' >> ~/.zshrc && source ~/.zshrc
    ```
    
- Confirm that the created alias works correctly.
    
    ```bash
    trino --help
    ```
    
- To connect with a running Themis Cluster, use the following command:
    
    ```bash
    trino --server = https://tcp.{{dataos instance fqdn}}:7432 \
         --user = {{dataos userID}} \
         --apikey {{dataos user apikey}}
    		 --extra-credential accessToken={{dataos user apikey}} \
         --extra-credential cluster={{themis cluster name}}
    
    # Sample
    trino --server = https://tcp.cheerful-delta.dataos.app:7432 \
    			--user=iamgroot \
    			--extra-credential accessToken=abcdefghijklmnopqrstuvwxyz 
    			--extra-credential cluster=themiscluster
    ```


## Query

The following commands can be used to perform various operations:

- List Catalogs:

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

- List Schemas within a Catalog:

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

- Set Default Catalog:

    ```bash
    ➜ Minerva# USE icebase.surveys;
    	USE
    ```

- Show Tables:

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

- Describe Table:

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

- Show Table Data:

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

- Quit CLI:

    ```bash
    ➜ Minerva:icebase.surveys# quit
    ```

## Export results as CSV

To export query results as a CSV file, you can use the `output-format` option. The example below demonstrates how to execute a query and save the results to a CSV file named `result.csv`:

```bash
minerva \
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

> The `execute` option enables batch mode, allowing the query to automatically exit after execution.