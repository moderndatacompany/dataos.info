# Case Scenario: Maintenance (Snapshots and Meta Data Listing)

## Snapshots

### **List Snapshots**

The list snapshot command is used to list all the snapshots of the dataset. This will help determine how many dataset snapshots you have. The command is as follows:

**Command**

```shell
dataos-ctl dataset -a ${{udl}} snapshots 
```

**Example**

```shell
dataos-ctl dataset -a dataos://icebase:retail/city snapshots 
```

Output

```shell
INFO[0000] 📂 get snapshots...                           
INFO[0000] 📂 get snapshots...completed                  

      SNAPSHOTID      |   TIMESTAMP    
----------------------|----------------
  5724215526433994041 | 1660579675496  
  7521925172258223419 | 1660745070207
```

The first column represents the Snapshot IDs and the second one represents the respective timestamp

### **Set Snapshot**

The Set Snapshot command helps to set a snapshot so that you can travel back. The command is given below.

**Command**

```shell
dataos-ctl dataset -a ${{udl}} set-snapshot \
-i ${{snapshot-id}}
```

**Example**

Let’s say you wanna revert back to a specific snapshot ID from the once listed by the list snapshots command. The command will be:

```shell
dataos-ctl dataset -a dataos://icebase:retail/city set-snapshot \
-i 5724215526433994041
```

Output (successful execution)

```shell
INFO[0000] 📂 set snapshot...                            
INFO[0001] 📂 set snapshot...completed
```

(Make sure that all the operations have been committed, else there will be errors)

## Metadata Listing

### **List Metadata**

The metadata command lists all the metadata files. The command is given below.

**Command**

```shell
dataos-ctl dataset -a ${{udl}} metadata
```

**Example**

```shell
dataos-ctl dataset -a dataos://icebase:retail/city metadata
```

Output (successful execution)

```shell
INFO[0000] 📂 get metadata...                            
INFO[0000] 📂 get metadata...completed                   

        VERSION        |   TIMESTAMP    
-----------------------|----------------
  v34.gz.metadata.json | 1661252152036
  v30.gz.metadata.json | 1661249266230  
  v4.gz.metadata.json  | 1661163612098  
  v17.gz.metadata.json | 1661242729511  
  v37.metadata.json    | 1661253371394  
  v43.gz.metadata.json | 1661254272987
```

### **Set Metadata**

<aside class=callout>
🗣 In instances where data is being written in Iceberg format and the catalog is designated as <b>Hadoop catalog</b>, it is necessary for users to utilize this command to set the metadata version. However, it is important to note that this command is not requisite for <b>Hive catalogs</b>.

</aside>

In order to set the metadata to the latest or some specific version, use the below command.

**Command**

```shell
dataos-ctl dataset -a ${{udl}} set-metadata \
-v ${{latest|version.gz.metadata.json}}
```
**Example**

In order to set the metadata of the dataset `dataos://icebase:retail/city` to the `latest` format.

```shell
dataos-ctl dataset -a dataos://icebase:retail/city set-metadata \
-v latest
```

In order to set the metadata to some specfic version among the ones in the list say `v4.gz.metadata.json`.

```shell
dataos-ctl dataset -a dataos://icebase:retail/city set-metadata \
-v v4.gz.metadata.json
```

Output

```shell
INFO[0000] 📂 set metadata...                            
INFO[0001] 📂 set metadata...completed
```

## Mark Column Nullable

To set nullability in a specific column. The command is as follows:

```shell
dataos-ctl dataset -a ${{udl}} set-nullable \
-n ${{column-name}} \
-b ${{true/false}}
```

Let’s say we wanna set a column random as nullable. The command is given below:

```shell
dataos-ctl dataset -a dataos://icebase:retail/city set-nullable \
-n random \
-b true
```

Output (on successful execution)

```shell
INFO[0000] 📂 set nullability                            
INFO[0000] 📂 set nullability...completed
```

The column is now set as nullable.