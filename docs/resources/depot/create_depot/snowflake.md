# Steps to create Snowflake Depot

To create a Snowflake Depot you must have the following details:

## Pre-requisites specific to Depot creation

- **Tags:** A developer must possess the following tags, which can be obtained from a DataOS operator.

    ```bash
            NAME     │     ID      │  TYPE  │        EMAIL         │              TAGS               
        ─────────────┼─────────────┼────────┼──────────────────────┼─────────────────────────────────
        Iamgroot     │   iamgroot  │ person │   iamgroot@tmdc.io   │ roles:id:data-dev,                            
                     │             │        │                      │ roles:id:user,                  
                     │             │        │                      │ users:id:iamgroot  
    ```

- **Use cases:** Alternatively, instead of assigning tags, a developer can create a Depot if an operator grants them the "Manage All Instance-level Resources of DataOS in the user layer" use case through Bifrost Governance.

    <center>
    <img src="/resources/depot/usecase2.png" alt="Bifrost Governance" style="width:60rem; border: 1px solid black; padding: 5px;" />
    <figcaption><i>Bifrost Governance</i></figcaption>
    </center>

## Pre-requisites specific to the source system

- **Snowflake Account URL**: The unique URL used to access your Snowflake account, typically in the format `https://<account_name>.snowflakecomputing.com`. You can retrieve this from your Snowflake admin or find it in your Snowflake login credentials email.

- **Snowflake Username**: The username used to log in to your Snowflake account. This is usually provided by the Snowflake admin when your account is created.

- **Snowflake User Password**: The password associated with your Snowflake username for authentication. This password is set during account creation or upon first login. If forgotten, you may need to reset it via the Snowflake login page or contact your Snowflake admin.

- **Snowflake Database Name**: The name of the database in Snowflake that you need to connect to. You can find this in the Snowflake console under the Databases section or by consulting the team managing the Snowflake environment.

- **Database Schema**: The specific schema within the Snowflake database where your required table resides. This can also be found in the Snowflake console under the relevant database or provided by the team managing the database structure.

## Create a Snowflake Depot

DataOS provides integration with Snowflake, allowing you to seamlessly read data from Snowflake tables using Depots. Snowflake is a cloud-based data storage and analytics data warehouse offered as a Software-as-a-Service (SaaS) solution. It utilizes a new SQL database engine designed specifically for cloud infrastructure, enabling efficient access to Snowflake databases. To create a Depot of type 'SNOWFLAKE', follow the below steps:

### **Step 1: Create an Instance Secret for securing Snowflake credentials**


Begin by creating an Instance Secret Resource by following the [Instance Secret document](/resources/instance_secret/data_sources/snowflake/).

### **Step 2: Create a Snowflake Depot manifest file**

Create a manifest file to hold the configuration details for your Snowflake Depot. A Depot is created by referencing the Instance Secret by name in the Depot manifest file as shown in below template.


```yaml 
name: ${{snowflake-depot}}
version: v2alpha
type: depot
tags:
    - ${{tag1}}
    - ${{tag2}}
layer: user
depot:
    type: snowflake
    description: ${{snowflake-depot-description}}
    snowflake:
    warehouse: ${{warehouse-name}}
    url: ${{snowflake-url}}
    database: ${{database-name}}
    external: true
    secrets:
    - name: ${{redshift-instance-secret-name}}-r
        allkeys: true

    - name: ${{redshift-instance-secret-name}}-rw
        allkeys: true
```

To get the details of each attribute, please refer [to this link](/resources/depot/configurations).
   

### **Step 3: Apply the Depot manifest file**

Once you have the manifest file ready in your code editor, simply copy the path of the manifest file and apply it through the DataOS CLI by pasting the path in the placeholder, using the command given below:

=== "Command"

    ```bash 
    dataos-ctl resource apply -f ${{yamlfilepath}}
    ```
=== "Alternative Command"

    ```bash 
    dataos-ctl apply -f ${{yamlfilepath}}
    ```



## Verify the Depot creation

To ensure that your Depot has been successfully created, you can verify it in two ways:

- Check the name of the newly created Depot in the list of Depots where you are named as the owner:

    ```bash
    dataos-ctl get -t depot
    ```

- Additionally, retrieve the list of all Depots created in your organization:

    ```bash
    dataos-ctl get -t depot -a
    ```

You can also access the details of any created Depot through the DataOS GUI in the [Operations App](https://dataos.info/interfaces/operations/) and [Metis UI](https://dataos.info/interfaces/metis/).

## Delete a Depot

<aside class="callout">
🗣️ As part of best practices, it is recommended to regularly delete Resources that are no longer in use. This practice offers several benefits, including saving time and reducing costs.
</aside>

If you need to delete a Depot, use the following command in the DataOS CLI:

=== "Command"

    ```bash 
    dataos-ctl delete -t depot -n ${{name of Depot}}
    ```
=== "Alternative Command"

    ```bash 
    dataos-ctl delete -f ${{path of your manifest file}}
    ```


By executing the above command, the specified Depot will be deleted from your DataOS environment.