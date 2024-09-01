# Consumption usin SQL APIs

In this guide, we'll walk you through the steps to connect to a deployed Lens using a SQL client (like `psql` and `dataos-ctl usql` interfaces. 

## Retrieve or Create Your API Key Token

### **Existing API Key Token Retrieval**

If you already possess an API key token, execute the following command to retrieve it:

```bash
dataos-ctl user apikey get   
```

Upon successful execution, the output will resemble the following, listing available API keys:

```bash
dataos-ctl user apikey get 
# Expected Output
INFO[0000] 🔑 user apikey get...                         
INFO[0000] 🔑 user apikey get...complete                 

                        TOKEN                          │  TYPE  │        EXPIRATION         │                   NAME                    
───────────────────────────────────────────────────────┼────────┼───────────────────────────┼───────────────────────────────────────────
  abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz │ apikey │ 2024-03-02T05:30:00+05:30 │ token_officially_recently_alphabet
  alphabetaomegasigmapizeroonetwothreefourfivesixseven │ apikey │ 2024-02-28T05:30:00+05:30 │ token_newly_mathematics_equations       
```

If there are no apikey’s available, as shown in the code block below:

```bash
dataos-ctl user apikey get 
# Expected Output
INFO[0000] 🔑 user apikey get...                         
INFO[0000] 🔑 user apikey get...complete                 

                        TOKEN                          │  TYPE  │        EXPIRATION         │                   NAME                    
───────────────────────────────────────────────────────┼────────┼───────────────────────────┼───────────────────────────────────────────
```

If you get a similar output, create a new apikey.

### **Creating a New API Key**

To generate a new API key, use the `apikey create` command with the following syntax:

```bash
dataos-ctl user apikey create -d ${{duration}} -i ${{user-id}} -n ${{apikey-name}}
```
**Command Parameters**

- `-d`, `--duration` flag (optional): Specifies the lifetime of the API key. Acceptable units are `m` for minutes and `h` for hours. The default duration is "`24h`".
- `-i`, `--id` flag (optional): Identifies the user ID.
- `-n`, `--name` flag (optional): Assigns a name to the API key.

```bash
# Example
dataos-ctl user apikey create -d 21h -i iamgroot -n marvel
# Expected Output
# This command will generate a new API key, with output similar to the following:
INFO[0000] 🔑 user apikey...
INFO[0001] 🔑 user apikey...complete

                             TOKEN                             │  TYPE  │        EXPIRATION         │  NAME
───────────────────────────────────────────────────────────────┼────────┼───────────────────────────┼─────────
     bWFydmVsLmY4NTA1MzMwLThhZWItNDIwMS04MTNjLTUwOWYyMTY3ZDM=  │ apikey │ 2024-02-22T15:30:00+05:30 │ marvel
```

Copy the value of the Token column for the procedure ahead.

### **Retrieving Lens Name**

To identify the Lens name for generating a Cluster Token, you'll need to list all Lenses within a specific Workspace. Use the following command to retrieve a comprehensive list of Lenses:

```bash
dataos-ctl resource get -t lens -w ${workspace} -a
```

This command requires specifying the workspace name to filter the Lens accordingly.

```bash
# Example
# For a workspace named "curriculum", the command and its expected output are as follows:
dataos-ctl resource get -t lens -w curriculum -a
# Expected Output
INFO[0000] 🔍 get...                                     
INFO[0000] 🔍 get...complete                             

              NAME             | VERSION |  TYPE   | WORKSPACE  | STATUS |   RUNTIME   |     OWNER        
-------------------------------|---------|---------|------------|--------|-------------|-------------------
         monitor360            | v1      | cluster | curriculum | active | running:1   |     thor       
         sales360              | v1      | cluster | curriculum | active | running:1   |     ironman  
         finance360            | v1      | cluster | curriculum | active | running:2   |     thanos  
```

For the rest of the documentation, we will use be using the `sales360` and the apikey token to create a wrapped token.

## Creating a Wrap Token for Lens

To create a wrap token for a Lens, you can use the following commands for Unix-like systems (such as Linux or macOS) and Windows, respectively:

**Unix-like Systems (e.g., Linux, macOS)**

```bash
echo '{"apikey":"<API_KEY>","lens2":"<WORKSPACE>:<LENS_NAME>"}' | base64
```

Replace `<your_api_key_here>`, `<workspace>`, and `<lens_name>` with your actual API key, deploying Workspace name, and Lens Resource name. This command will encode the JSON object into base64 format, producing a wrap token.

**Windows**

```powershell
[System.Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes('{"apikey":"<your_api_key_here>","lens2": "<workspace>:<lens_name>"}'))
```

Replace `<your_api_key_here>`, `<workspace>`, and `<lens_name>` with your actual API key, deploying Workspace name and Lens Resource name. This PowerShell command will encode the JSON object into base64 format, creating the wrap token.

## Connecting to Lens using `psql`

1. Open your terminal.
2. Use the following command to connect to the Lens using `psql`:
    
    ```bash
    psql -h tcp.<dataos-fqdn> -p 6432
    ```
    
    Replace the `<dataos-fqdn>` with your DataOS Fully qualified domain name. For instance, `liberal-donkey.dataos.app`.s 
    
3. Enter your ‘**Wrap Token**’ in place of password when prompted.
4. You should now be connected to the Lens. You can verify the connection by listing the available relations using the `\dt` command:
    
    ```sql
    iamgroot=> \dt
    ```
    
    Expected output
    
    ```bash
    Password for user iamgroot: 
    psql (16.3 (Ubuntu 16.3-1.pgdg22.04+1), server 14.2 (Lens2/public:sales400 v0.35.41-01))
    Type "help" for help.
    
    iamgroot=> \dt
                    List of relations
     Schema |       Name        | Type  |    Owner    
    --------+-------------------+-------+-------------
     public | account           | table | iamgroot
     public | product           | table | iamgroot
     public | sales             | table | iamgroot
     public | wallet_sales_view | table | iamgroot
    (4 rows)
    ```
    
5. To exit `psql`, type:
    
    ```sql
    iamgroot=> \q
    ```
    