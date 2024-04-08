# Lakehouse Management Commands

Here is a reference to the various commands related to managing Lakehouses in DataOS:

## Linting a Lakehouse manifest

## Applying a Lakehouse

Applying the Lakehouse Resource manifest creates a Lakehouse Resource-instance in the DataOS environment. The manifest can be applied using one of the two commands provided below. Both commands achieve the same outcome.

**Command**

```sql
dataos-ctl resource apply -f ${manifest-file-path} -w ${workspace}
```

**Alternate Command**

```sql
dataos-ctl apply -f ${manifest-file-path} -w ${workspace}
```

**Flags and Placeholders**

- **`-f`** or **`--manifestFile`**: This flag specifies the location of the manifest file containing the configuration for the Lakehouse Resource.
    - **Placeholder**: **`${manifest-file-path}`**
    - **Example**: **`./lakehouse/manifest.yaml`**
- **`-w`** or **`--workspace`**: This flag indicates the target Workspace within DataOS where the Lakehouse Resource will be created. If not specified, the default Workspace used is “public”.
    - **Placeholder**: **`${workspace}`**
    - **Example**: **`sandbox`**, **`testing`**

**Example**

To apply a Lakehouse Resource manifest to a specific workspace, replace the placeholders with the actual file path and workspace name. For instance:

```bash
dataos-ctl resource apply -f ./lakehouse/manifest.yaml -w testing
```

This command instructs DataOS to apply the Lakehouse Resource configuration defined in `./lakehouse/manifest.yaml` to the `testing` workspace.

## Get Lakehouse Status

Retrieving the status of a specific Lakehouse provides insight into its current operational state within the DataOS environment. This operation can be performed using any of the two commands detailed below.

**Command**

```bash
dataos-ctl resource get -t lakehouse -w ${workspace-name}
```

**Alternate Command**

```bash
dataos-ctl resource get -t lakehouse -w ${workspace-name}
```

**Flags and Placeholders**

- `-t`: This flag specifies the type of resource for which the status is being requested, in this case, `lakehouse`.
- `w`: This flag indicates the Workspace from which to retrieve the Lakehouse status.
    - **Placeholder**: `${workspace-name}`
    - **Example**: `curriculum`

**Example Usage**

To check the status of a Lakehouse in the 'curriculum' workspace:

```bash
dataos-ctl resource get -t lakehouse -w curriculum
```

This command queries the status of Lakehouse resources within the 'curriculum' workspace.

---

## Get the Status of all Lakehouses within a Workspace

To overview the status of all Workers related to Lakehouse instances within a specified workspace, the following command is used:

**Command**

```bash
dataos-ctl resource get -t lakehouse -w ${workspace-name} -a
```

**Alternate Command**

```bash
dataos-ctl get -t lakehouse -w ${workspace-name} -a
```

**Flags and Placeholders**

- `a`: This flag is used to retrieve the status of all Workers within the given Workspace.
- Other flags and placeholders are the same as previously described.

**Example Usage**

To obtain the status of all Workers in the 'curriculum' workspace:

```bash
dataos-ctl resource get -t lakehouse -w curriculum -a
```

This instructs DataOS to display the status of all Workers related to Lakehouse within the 'curriculum' workspace.

---

## Generate Lakehouse JSON Schema

Generating the JSON schema for a Lakehouse, especially for a specified version, is crucial for developers to understand its configuration structure:

**Command**

```bash
dataos-ctl develop schema generate -t lakehouse -v ${version}

```

**Sample Command**

```bash
dataos-ctl develop schema generate -t lakehouse -v v1alpha

```

**Flags and Placeholders**

- `-t` or `--type`: This flag denotes the type of schema to generate, here, `lakehouse`.
- `v`: Specifies the version of the Lakehouse for which the schema is to be generated.
    - **Placeholder**: `${version}`
    - **Example**: `v1alpha`

**Example Usage**

To generate a JSON schema for a Lakehouse of version 'v1alpha':

```bash
dataos-ctl develop schema generate -t lakehouse -v v1alpha

```

This generates the JSON schema for Lakehouse resources conforming to the 'v1alpha' version.

---

## Get Lakehouse JSON Resource Schema

To obtain the JSON resource schema for a Lakehouse, especially for a specific version, use the command below:

**Command**

```bash
dataos-ctl develop get resource -t lakehouse -v ${version}

```

**Sample Command**

```
dataos-ctl develop get resource -t lakehouse -v v1alpha

```

**Flags and Placeholders**

Similar to generating the JSON schema, the flags `-t` and `-v` are used to specify the resource type and version, respectively.

**Example Usage**

For acquiring the JSON resource schema for a Lakehouse version 'v1alpha':

```bash
dataos-ctl develop get resource -t lakehouse -v v1alpha

```

This command retrieves the detailed JSON schema for Lakehouse resources of the specified version.

---

## Deleting Lakehouse

To delete a specific lakehouse, you can use the below command:

**Command**

```bash
dataos-ctl resource delete -t lakehouse -w ${workspace_name} -n ${lakehouse_name}
```

**Flags and Placeholders**

- **`-t`** or `-type`: Specifies the type of resource to delete, which in this case is a lakehouse.
- **`w`** or `-workspace`: Specifies the name of the workspace where the lakehouse is located.
    - **Placeholder**: ${workspace_name}
    - **Example:** ${bent}
- **`-n`** or `--name`: Specifies the name of the lakehouse to delete.
    - **Placeholder**: ${lakehouse_name}
    - **Example:** ${benthos3-lakehouse}

**Example**

```bash
dataos-ctl resource delete -t lakehouse -w curriculum -n benthos3-lakehouse
```

This command will delete the lakehouse named `benthos3-lakehouse` located in the `curriculum` workspace.

# Dataset Management Commands

## Create Dataset

## Get the list of all Datasets

This command enables users to list datasets within a specific depot and collection in the DataOS environment. It provides a concise overview of all datasets available under the specified location.

**Command**

```bash
dataos-ctl dataset list -a dataos://icebase:retail
```

**Flags and Placeholders**

- flags and placeholders are the same as previously described.
- **`${depot}`** and **`${collection}`**: Placeholder for the depot and collection names within the DataOS environment as described in previous command.

**Output**

Upon executing the command, the output provides a list of datasets available under the specified depot and collection:

```bash
     DATASETS
──────────────────
  city_test
  product
  city
  store
```

#Create dataset

## Retrieving Dataset Information

This command allows users to retrieve detailed information about a specific dataset within the DataOS environment. It provides insights into the dataset's schema and its properties, such as the schema type, Avro schema definition, and Iceberg metadata.

**Command**

```bash
dataos-ctl dataset  get -a dataos://${depot}:${collection}/${dataset}  #UDL
```

**Flags and Placeholders**

- **`-a`** or **`-address`**: This flag specifies the target address or location of a dataset in a UDL format.
    - **Placeholder**: **`${depot}`**, **`${collection}`**, and **`${dataset}`**
    - **Example**: `dataos://icebase:retail/city`

**Example**

To retrieve information about the dataset located at `dataos://icebase:retail/city`, you can use the following command:

```bash
dataos-ctl dataset  get -a dataos://icebase:retail/city
```

## Drop Dataset

This command is used to drop a dataset specified by its unique dataset location (UDL) in the DataOS platform.

**Command**

```bash
dataos-ctl dataset properties -a dataos://{collection}/{dataset}
```

**Flags and Placeholders**

- **`-a`** or  `--address`: Specifies the target address or location of the dataset in a UDL format.
    - **Placeholder**: **`${collection}`** and **`${dataset}`**
    - **Example**: `dataos://retail/city`

**Example**

```bash
dataos-ctl dataset -a dataos://icebase:retail/city drop
```

Dropping a dataset will permanently delete it and its associated data. This action cannot be undone.

or you can also equivalently use 

**drop with `--purge`** 

If this `-p`/`--purge` (Purge Value) is set to `true` (by default, this is `false`), the dataset entry gets deleted from the store as well as all its files.

**Command**

```bash
dataos-ctl dataset -a ${{udl}} drop -p false
# OR
dataos-ctl dataset -a ${{udl}} drop --purge false

# '-a' flag denotes the Dataset Address
# ${{udl}} is a placeholder for dataset UDL - dataos://icebase:retail/city is one such sample UDL
# '-p' or '--purge' flags denote the purge value
```

- **`-a`** or `--address`: Specifies the target address or location of the dataset in a UDL format.
    - **Placeholder**: **`${collection}`** and **`${dataset}`**
    - **Example**: `dataos://retail/city`

# **How to configure table properties?**

## List Properties

This command allows users to retrieve properties of a specific dataset within a collection in the DataOS environment.

**Command**

```bash
dataos-ctl dataset properties -a dataos://{collection}/{dataset}
```

**Flags and Placeholders**

- `-**a**` or `--address`: Specifies the target address or location of the dataset in a UDL format.
    - **Placeholder**: **`${collection}`** and **`${dataset}`**
    - **Example**: `dataos://retail/city`

**Example**

To retrieve properties of the city dataset in the retail collection:

```bash
dataos-ctl dataset properties -a dataos://retail/city
```

This command will display the properties of the city dataset within the retail collection

## Adding Properties

This command allows users to add custom properties to a specific dataset within a collection in the DataOS environment.

**Command**

```bash
dataos-ctl dataset add-properties -a dataos://{depot}:{collection}/{dataset} \
-p {property_key}:{property_value}
```

**Flags and Placeholders**

- `-**a**` or `--address`: Specifies the target address or location of the dataset in a UDL format.
    - **Placeholder**: **`${depot}`**, **`${collection}`**, and **`${dataset}`**
    - **Example**: `dataos://icebase:retail/city`
- `-**p**` or `--properties`: Specifies the properties to be added to the dataset.
    - **Placeholder**: {property_key}:{property_value}
    - **Example**: `write.sample.property:testaddproperty`

**Example**

To add the custom property `write.sample.property` with the value `testaddproperty` to the city dataset in the retail collection of Icebase depot:

```bash
dataos-ctl dataset add-properties -a dataos://icebase:retail/city \
-p write.sample.property:testaddproperty

```

This command will add the specified property to the city dataset.

## Removing Properties

This command allows users to remove custom properties from a specific dataset within a collection in the DataOS environment.

**Command**

```bash
dataos-ctl dataset remove-properties -a dataos://{depot}:{collection}/{dataset} \
-p {property_key}
```

**Flags and Placeholders**

- `-**a**` or `--address`: Specifies the target address or location of the dataset in a UDL format.
    
    **Placeholder**: **`${depot}`**, **`${collection}`**, and **`${dataset}`**
    
    - **Example**: `dataos://icebase:retail/city`
- `-**p**` or `--properties`: Specifies the property key to be removed from the dataset.
    - **Placeholder**: {property_key}
    - **Example**: `write.sample.property`

**Example**

To remove the custom property `write.sample.property` from the city dataset in the retail collection of Icebase depot:

```bash
dataos-ctl dataset remove-properties -a dataos://icebase:retail/city \
-p write.sample.property
```

This command will remove the specified property from the city dataset.

# **How to manage field/column? (Schema Evolution)**

## Adding Field/Column

This command allows users to add a new field to a specific dataset within a collection in the DataOS environment.

**Command**

```bash
dataos-ctl dataset add-field -a dataos://{depot}:{collection}/{dataset} \
-n {field_name} \
-t {field_type}
```

**Flags and Placeholders**

- `-**a**` or `--address`: Specifies the target address or location of the dataset in a UDL format.
    - **Placeholder**: **`${depot}`**, **`${collection}`**, and **`${dataset}`**
    - **Example**: `dataos://icebase:retail/city`
- `-**n**` or `--name`: Specifies the name of the field to be added.
    - **Placeholder**: {field_name}
    - **Example**: `sample_field`
- `-**t**` or `--type`: Specifies the type of the field to be added.
    - **Placeholder**: {field_type}
    - **Example**: `string`

**Example**

To add a new field named `sample_field` of type `string` to the city dataset in the retail collection of Icebase depot:

```bash
dataos-ctl dataset add-field -a dataos://icebase:retail/city \
-n sample_field \
-t string
```

This command will add the specified field to the city dataset.

## Dropping Field/Column

This command allows users to drop (delete) a field from a specific dataset within a collection in the DataOS environment.

**Command**

```bash
dataos-ctl dataset drop-field -a dataos://{depot}:{collection}/{dataset} \
-n {field_name}
```

**Flags and Placeholders**

- `-**a**` or `--address`: Specifies the target address or location of the dataset in a UDL format.
    - **Placeholder**: **`${depot}`**, **`${collection}`**, and **`${dataset}`**
    - **Example**: `dataos://icebase:retail/city`
- `-**n**` or `--name`: Specifies the name of the field to be dropped.
    - **Placeholder**: {field_name}
    - **Example**: `sample_field`

## Renaming Field/Column

This command allows users to rename a field in a specific dataset within a collection in the DataOS environment.

**Command**

```bash
dataos-ctl dataset rename-field -a dataos://{depot}:{collection}/{dataset} \
-n {old_field_name} \
-m {new_field_name}
```

**Flags and Placeholders**

- `-**a**` or `--address`: Specifies the target address or location of the dataset in a UDL format.
    - **Placeholder**: **`${depot}`**, **`${collection}`**, and **`${dataset}`**
    - **Example**: `dataos://icebase:retail/city`
- `-**n**` or `--name`: Specifies the current name of the field to be renamed.
    - **Placeholder**: {old_field_name}
    - **Example**: `county_name`
- `-**m**` for `--new-name`: Specifies the new name for the field.
    - **Placeholder**: {new_field_name}
    - **Example**: `country_name`

**Example**

To rename the field from `county_name` to `country_name` in the city dataset of the retail collection in Icebase depot:

```bash
dataos-ctl dataset rename-field -a dataos://icebase:retail/city -n county_name -m country_name
```

This command will rename the specified field from `county_name` to `country_name` in the city dataset.

## Updating Dataset Field

This command allows users to update the type of a field in a specific dataset within a collection in the DataOS environment.

**Command**

```bash
dataos-ctl dataset update-field -a dataos://{depot}:{collection}/{dataset} \
-n {field_name} \
-t {new_field_type}
```

**Flags and Placeholders**

- `-**a**` or `--address`: Specifies the target address or location of the dataset in a UDL format.
    - **Placeholder**: **`${depot}`**, **`${collection}`**, and **`${dataset}`**
    - **Example**: `dataos://icebase:retail/city`
- `-**n**` or `--name`: Specifies the name of the field to be updated.
    - **Placeholder**: {field_name}
    - **Example**: `zip_code`
- `-**t**` or `--type`: Specifies the new type for the field.
    - **Placeholder**: {new_field_type}
    - **Example**: `long`

**Example**

To update the type of the field `zip_code` to `long` in the city dataset of the retail collection in Icebase depot:

```bash
dataos-ctl dataset update-field -a dataos://icebase:retail/city -n zip_code -t long
```

This command will update the specified field `zip_code` to have the type `long` in the city dataset.

# How to perform partitioning?

<aside>
🗣 This procedure uses partitioning on the upcoming/future data, not the existing one. To make changes to the current data, please look at the partitioning in Flare Case Scenarios.

</aside>

### **Single Partitioning**

The partitioning in any iceberg table is column based. Currently, 
Flare supports only these Partition Transforms: identity, year, month, 
day, and hour.

**Command**

```bash
dataos-ctl dataset -a <dataset_udl> -p "<partition_key>"
```

**Example**

```bash
dataos-ctl dataset -a dataos://icebase:retail/city -p "identity:state_name"

```

**All available single partitioning**

- **identity**

```bash
dataos-ctl dataset -a dataos://icebase:retail/city -p "identity:state_name"
```

- **year**

```bash
dataos-ctl dataset -a dataos://icebase:retail/city -p "year:ts_city:year_partition"
```

- **month**

```bash
dataos-ctl dataset -a dataos://icebase:retail/city \
-p "month:ts_city:month_partition"
```

- **day**

```bash
dataos-ctl dataset -a dataos://icebase:retail/city \
-p "day:ts_city:day_partition"
```

- **hour**

```
dataos-ctl dataset -a dataos://icebase:retail/city \
-p "hour:ts_city:hour_partition"
```

## **Multiple Partitioning**

Partitioning can be done on multiple levels. For example, a user wants 
to partition the city data into two partitions, the first based on `state_code` and the second based on the `month`. This can be done using the below command:

```bash
dataos-ctl dataset -a dataos://icebase:retail/city \
-p "identity:state_code" \
-p "month:ts_city:month_partition"
```

<aside>
🗣  The order of partition given should be the hierarchy in which the user needs the data to be partitioned.

</aside>

## To Update partition

Command

```bash
dataos-ctl dataset -a dataos://icebase:retail/city update-partition \
-p "${{partition_type}}:${{column_name}}:${{partition_name}}"
```

**Flags and Placeholders**

- `-a <dataset_udl>`: Denotes the Dataset Address. It specifies the UDL (Unique Dataset Location) of the dataset to be updated.
    - `dataos://icebase:retail/city`: Sample UDL provided.
- `-p "${{partition_type}}:${{column_name}}:${{partition_name}}"`: Specifies the new partition configuration.
    - `${{partition_type}}`: Placeholder for the type of partitioning to be used (e.g., identity, range).
    - `${{column_name}}`: Placeholder for the column name used for partitioning.
    - `${{partition_name}}`: Placeholder for the name of the partition.
    - **Example** `month:ts_city:month_partition`

**Example**

```bash
dataos-ctl dataset -a dataos://icebase:retail/city update-partition \
-p "month:ts_city:month_partition"

--Output
INFO[0000] 📂 update partition...                        
INFO[0000] 📂 update partition...completed
```

# How to create and manage branch?

## Listing Branches

This command allows users to list branches for a specific dataset within a depot and collection in the DataOS environment. To list the branches of a particular dataset in a collection, replace the placeholders with the targeted depot, collection, and dataset. 

**Command**

```bash
dataos-ctl dataset list-branch -a dataos://{depot}:{collection}/{dataset}
```

**Flags and Placeholders**

- ****`-**a**` or `--address`: This flag specifies the target address or location of a dataset in a UDL format.
    - **Placeholder**: **`${depot}`**, **`${collection}`**, and **`${dataset}`**
    - **Example**: `dataos://icebase:retail/city`

**Example**

To list the branches of the city dataset in the retail collection of Icebase depot

```bash
dataos-ctl dataset list-branch -a dataos://icebase:retail/city
```

Output:

```bash
INFO[0000] 📂 list branches...                           
INFO[0001] 📂 list branches...completed                  

  BRANCH │     SNAPSHOTID      
─────────┼─────────────────────
  test   │ 905423312211489819  
  main   │ 905423312211489819  

```

## Creating Branch

This command allows users to create a new branch for a specific dataset within a depot and collection in the DataOS environment.

**Command**

```bash
dataos-ctl dataset create-branch -a dataos://{depot}:{collection}/{dataset} -b {branch_name}
```

**Flags and Placeholders**

- `-**a**` or `--address`: Specifies the target address or location of the dataset in a UDL format.
    - **Placeholder**: **`${depot}`**, **`${collection}`**, and **`${dataset}`**
    - **Example**: `dataos://icebase:retail/city`
- `-**b**` or `--branch`: Specifies the name of the new branch to be created.
    - **Placeholder**: {branch_name}
    - **Example**: `test_branch2`

**Example**

To create a new branch named 'test_branch2' for the city dataset in the retail collection of the Icebase depot:

```bash
dataos-ctl dataset create-branch -a dataos://icebase:retail/city -b test_branch2
```

This command will create a new branch named 'test_branch2' for the specified [dataset.](http://dataset.You) You can use the list branch command to look for newly created branch

## Renaming Branch

This command allows users to rename a branch for a specific dataset within a depot and collection in the DataOS environment.

**Command**

```bash
dataos-ctl dataset rename-branch -a dataos://{depot}:{collection}/{dataset} -b {branch_name} -n {new_branch_name}
```

**Flags and Placeholders**

- `-**a**` or `--address`: Specifies the target address or location of the dataset in a UDL format.
    - **Placeholder**: **`${depot}`**, **`${collection}`**, and **`${dataset}`**
    - **Example**: `dataos://icebase:retail/city`
- `-**b**` or `--branch`: Specifies the current name of the branch to be renamed.
    - **Placeholder**: {branch_name}
    - **Example**: `test`
- **`-n`** or `--name`: Specifies the new name for the branch.
    - **Placeholder**:  {new_branch_name}
    - **Example**: `test_branch`

**Example**

To rename the branch named 'test' to 'test_branch' for the city dataset in the retail collection of Icebase depot:

```bash
dataos-ctl dataset rename-branch -a dataos://icebase:retail/city -b test -n test_branch
```

This command will rename the specified branch, and upon listing the branches again, you would observe the updated branch name.

```bash
BRANCH    │     SNAPSHOTID
──────────────┼─────────────────────
test_branch │ 905423312211489819
main        │ 905423312211489819
```

## Deleting Branch for a Dataset

This command allows users to delete a specific branch for a dataset within a depot and collection in the DataOS environment.

**Command**

```bash
dataos-ctl dataset delete-branch -a dataos://icebase:retail/city -b {branch_name}
```

**Flags and Placeholders**

- `-**a**` or `--address`: Specifies the target address or location of the dataset in a UDL format.
    - **Placeholder**: **`${depot}`**, **`${collection}`**, and **`${dataset}`**
    - **Example**: `dataos://icebase:retail/city`
- `-**b**` or `--branch`: Specifies the name of the branch to be deleted.
    - **Placeholder**: {branch_name}
    - **Example**: `test_branch2`

**Example**

To delete the branch named 'test_branch2' for the city dataset in the retail collection of Icebase depot:

```bash
dataos-ctl dataset delete-branch -a dataos://{depot}:{collection}/{dataset} -b test_branch2
```

This command will delete the specified branch ('test_branch2') for the dataset.

## Replacing Branch

This command allows users to replace the snapshot of a branch with another snapshot for a specific dataset within a depot and collection in the DataOS environment.

**Command**

```bash
dataos-ctl dataset replace-branch -a dataos://{depot}:{collection}/{dataset} --source {branch_name} --target {branch_to_replace_with}
```

**Flags and Placeholders**

- `-**a**` or `--address`: Specifies the target address or location of the dataset in a UDL format.
    - **Placeholder**: **`${depot}`**, **`${collection}`**, and **`${dataset}`**
    - **Example**: `dataos://icebase:retail/city`
- **`--source`**: Specifies the source branch whose snapshot needs to be replaced.
    - **Placeholder**: {branch_name}
    - **Example**: `test_branch`
- **`--target`**: Specifies the target branch where the snapshot will be replaced.
    - **Placeholder**: {branch_to_replace_with}
    - **Example**: `test_branch2`

**Example**

To replace the snapshot of the 'test_branch' with another snapshot for the 'test_branch2' for the city dataset in the retail collection of Icebase depot:

```bash
dataos-ctl dataset replace-branch -a dataos://icebase:retail/city --source test_branch --target test_branch2
```

This command will replace the snapshot of the 'test_branch' with another snapshot for the 'test_branch2' branch.

## Fast Forwarding Branch

This command allows users to fast-forward a branch to another branch's state for a specific dataset within a collection in the DataOS environment.

**Command**

```bash
dataos-ctl dataset fastforward-branch -a dataos://{depot}:{collection}/{dataset} --source {source_branch} --target {target_branch}
```

**Flags and Placeholders**

- `-**a**` or `--address`: Specifies the target address or location of the dataset in a UDL format.
    - **Placeholder**: **`${depot}`**, **`${collection}`**, and **`${dataset}`**
    - **Example**: `dataos://icebase:retail/city`
- `--**source**`: Specifies the source branch from which the changes will be fast-forwarded.
    - **Placeholder**: {source_branch}
    - **Example**: `main`
- `--**target**`: Specifies the target branch to which the changes will be fast-forwarded.
    - **Placeholder**: {target_branch}
    - **Example**: `test_branch`

**Example**

To fast forward the `test_branch` to the state of the `main` branch for the city dataset in the retail collection of Icebase depot:

```bash
dataos-ctl dataset fastforward-branch -a dataos://icebase:retail/city --source main --target test_branch
```

This command will fast forward the `test_branch` to the state of the `main` branch for the city dataset.

# **How to model snapshots and managed metadata versions?**

## Retrieving Snapshots

This command allows users to retrieve information about the snapshots associated with a specific dataset within a collection in the DataOS environment.

**Command**

```bash
dataos-ctl dataset snapshots -a dataos://{depot}:{collection}/{dataset}
```

**Flags and Placeholders**

- `-a` or `--address`: Specifies the target address or location of the dataset in a UDL format.
    - **Placeholder**: **`${depot}`**, **`${collection}`**, and **`${dataset}`**
    - **Example**: `dataos://icebase:retail/city`

**Output Columns**

- **`SNAPSHOTID`**: The unique identifier of the snapshot.
- **`TIMESTAMP`**: The timestamp associated with the snapshot.
- **`DATE AND TIME (GMT)`**: The date and time of the snapshot in GMT timezone.

**Example**

To retrieve information about the snapshots associated with the city dataset in the retail collection of Icebase depot:

```bash
dataos-ctl dataset snapshots -a dataos://icebase:retail/city
```

This command will display the snapshot ID, timestamp, and date/time (GMT) of the snapshots associated with the city dataset.

## Retrieving Metadata Versions

This command allows users to retrieve information about the versions of metadata associated with a specific dataset within a collection in the DataOS environment.

**Command**

```bash
dataos-ctl dataset metadata -a dataos://{depot}:{collection}/{dataset}
```

**Flags and Placeholders**

- **`a`** or `address`: Specifies the target address or location of the dataset in a UDL format.
    - **Placeholder**: **`${depot}`**, **`${collection}`**, and **`${dataset}`**
    - **Example**: `dataos://icebase:retail/city`

**Output Columns**

- **`VERSION`**: The version of the metadata file.
- **`TIMESTAMP`**: The timestamp associated with the metadata version.

**Example**

To retrieve information about the metadata versions associated with the city dataset in the retail collection of Icebase depot:

```bash
dataos-ctl dataset metadata -a dataos://icebase:retail/city
```

This command will display the versions and timestamps of the metadata files associated with the city dataset.

## Setting Dataset Metadata

This command allows users to set the metadata version for a specific dataset within a collection in the DataOS environment.

**Command**

```bash
dataos-ctl dataset set-metadata -a dataos://{depot}:{collection}/{dataset} -v {metadata_version}
```

**Flags and Placeholders**

- `-**a**` or `--address`: Specifies the target address or location of the dataset in a UDL format.
    - **Placeholder**: **`${depot}`**, **`${collection}`**, and **`${dataset}`**
    - **Example**: `dataos://icebase:retail/city`
- `-**v**` or `--version`: Specifies the metadata version to be set.
    - **Placeholder**: {metadata_version}
    - **Example**: `latest`

**Example**

To set the metadata version to "latest" for the city dataset in the retail collection of Icebase depot:

```bash
dataos-ctl dataset set-metadata -a dataos://icebase:retail/city -v latest
```

This command will set the metadata version of the city dataset to "latest".

## Setting Snapshot

This command allows users to set a specific snapshot as the current state of a dataset within a collection in the DataOS environment.

**Command**

```bash
dataos-ctl dataset set-snapshot -a dataos://{depot}:{collection}/{dataset} -i {snapshot_id}
```

**Flags and Placeholders**

- `-**a**` or `--address`: Specifies the target address or location of the dataset in a UDL format.
    - **Placeholder**: **`${depot}`**, **`${collection}`**, and **`${dataset}`**
- `-**i**` or `--id`: Specifies the ID of the snapshot to set as the current state of the dataset.
    - **Placeholder**: {snapshot_id}

**Example**

To set the snapshot with ID `905423312211489819` as the current state of the `city` dataset in the `retail` collection of the `icebase` depot:

```bash
dataos-ctl dataset set-snapshot -a dataos://icebase:retail/city -i 905423312211489819
```

This command will set the specified snapshot as the current state of the `city` dataset.

Before

```bash
    BRANCH    │     SNAPSHOTID       
──────────────┼──────────────────────
  stage       │ 8843932524527268980  
  test-branch │ 8843932524527268980  
  main        │ 8843932524527268980  
```

After

```bash

     BRANCH    │     SNAPSHOTID       
───────────────┼──────────────────────
  test_branch  │ 8546760663040429688  
  main         │ 905423312211489819   
  test_branch2 │ 8546760663040429688 
```

## Cherry-picking Snapshot

This command allows users to cherry-pick changes from one snapshot to another for a specific dataset within a collection in the DataOS environment.

**Command**

```bash
dataos-ctl dataset cherrypick-snapshot -a dataos://{depot}:{collection}/{dataset} --sid {snapshot_id}
```

**Flags and Placeholders**

- `-**a**` or `--address`: Specifies the target address or location of the dataset in a UDL format.
    - **Placeholder**: **`${depot}`**, **`${collection}`**, and **`${dataset}`**
- **`--sid`**: Specifies the ID of the snapshot to cherry-pick changes from.
    - **Placeholder**: {snapshot_id}

**Example**

To cherry-pick changes from the snapshot with ID `8546760663040429688` for the `city` dataset in the `retail` collection of the `icebase` depot:

```bash
dataos-ctl dataset cherrypick-snapshot -a dataos://icebase:retail/city --sid 8546760663040429688
```

This command will cherry-pick changes from the specified snapshot for the `city` dataset.

This will result in 

```bash
    BRANCH    │     SNAPSHOTID       
───────────────┼──────────────────────
  test_branch  │ 8546760663040429688  
  main         │ 8546760663040429688  
  test_branch2 │ 8546760663040429688  
```

## Rollback

This command allows users to roll back a dataset to a specific snapshot within a collection in the DataOS environment.

**Command**

```bash
dataos-ctl dataset rollback -a dataos://{depot}:{collection}/{dataset} -i {snapshot_id}
```

**Flags and Placeholders**

- **`a`** or `address`: Specifies the target address or location of the dataset in a UDL format.
    - **Placeholder**: **`${depot}`**, **`${collection}`**, and **`${dataset}`**
- **`i`** or `id`: Specifies the ID of the snapshot to roll back the dataset to.
    - **Placeholder**: {snapshot_id}

**Example**

To roll back the `city` dataset in the `retail` collection of the `icebase` depot to the snapshot with ID `905423312211489819`:

```bash
dataos-ctl dataset rollback -a dataos://icebase:retail/city -i 905423312211489819
```

This command will roll back the dataset to the specified ancestral snapshot.

1. **Setting Snapshot (`dataos-ctl dataset set-snapshot`)**:
    - This command sets a specific snapshot as the current state of the dataset.
    - It effectively replaces the current state with the state of the specified snapshot.
    - Useful when you want to explicitly switch to a specific known state if this state fails
    - Typically used when you want to make sure that end user can only view a certain previous snapshot your dataset is at a particular point in time.
2. **Rollback (`dataos-ctl dataset rollback`)**:
    - This command rolls back the dataset to a specific snapshot.
    - It changes the current state to a previous state in the history of the dataset.
    - It's important to note that you can only roll back to snapshots that are ancestors of the current state.
    - If the snapshot you want to roll back to is not an ancestor, the operation will fail.
    - Useful when you want to undo changes or revert to a previous known state of the main branch.
3. **Cherrypicking Snapshot (`dataos-ctl dataset cherrypick-snapshot`)**:
    
    In an audit workflow, new data is written to an orphan {@link Snapshot snapshot} that is not committed as the table's current state until it is audited. After auditing a change, it may need to be applied or cherry-picked on top of the latest snapshot instead of the one that was current when the audited changes were created. This supports cherry-picking the changes from an orphan snapshot by applying them to the current snapshot. The output of the operation is a new snapshot with the changes from cherry-picked snapshot.