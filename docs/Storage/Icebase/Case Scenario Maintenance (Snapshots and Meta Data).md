# Case Scenario: Maintenance (Snapshots and Meta Data Listing)

## List Snapshots

The list snapshot command is used to list all the snapshots of the dataset. This will help determine how many dataset snapshots you have. Execute the following command -

```bash
dataos-ctl dataset -a dataos://icebase:retail/city snapshots 
```

Output

```bash
INFO[0000] 📂 get snapshots...                           
INFO[0000] 📂 get snapshots...completed                  

      SNAPSHOTID      |   TIMESTAMP    
----------------------|----------------
  5724215526433994041 | 1660579675496  
  7521925172258223419 | 1660745070207
```

The first column represents the Snapshot IDs and the second one represents the respective timestamp

## Set Snapshot

The Set Snapshot command helps to set a snapshot so that you can travel back. The command is as follows -

```bash
dataos-ctl dataset -a dataos://icebase:retail/city set-snapshot \
-i <snapshot-id>
```

Let’s say you wanna revert back to a specific snapshot ID from the once listed by the list snapshots command. Execute the command as -

```bash
dataos-ctl dataset -a dataos://icebase:retail/city set-snapshot \
-i 5724215526433994041
```

Output (successful execution)

```bash
INFO[0000] 📂 set snapshot...                            
INFO[0001] 📂 set snapshot...completed
```

(Make sure that all the operations have been committed, else there will be errors)

# Metadata Listing

## List Metadata

The metadata command lists all the metadata files

```bash
dataos-ctl dataset -a dataos://icebase:retail/city metadata
```

Output (successful execution)

```bash
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

## Set Metadata

In order to set the metadata to the latest or some specific version, the following command can be used

```bash
dataos-ctl dataset -a dataos://icebase:retail/city set-metadata \
-v <latest|version.gz.metadata.json>
```

In order to set the metadata to the `latest` format use the command as -

```bash
dataos-ctl dataset -a dataos://icebase:retail/city set-metadata \
-v latest
```

In order to set the metadata to some specfic version among the ones in the list say `v4.gz.metadata.json`, use the command as -

```bash
dataos-ctl dataset -a dataos://icebase:retail/city set-metadata \
-v v4.gz.metadata.json
```

Output

```bash
INFO[0000] 📂 set metadata...                            
INFO[0001] 📂 set metadata...completed
```

## Mark Column Nullable

To set nullability in a specific column, use the code as follows :

```bash
dataos-ctl dataset -a dataos://icebase:retail/city set-nullable \
-n <column-name> \
-b <true/false>
```

Let’s say we wanna set a column random as nullable. The code will be as follows:

```bash
dataos-ctl dataset -a dataos://icebase:retail/city set-nullable \
-n random \
-b true
```

Output (on successful execution)

```bash
INFO[0000] 📂 set nullability                            
INFO[0000] 📂 set nullability...completed
```

The column is now set as nullable.