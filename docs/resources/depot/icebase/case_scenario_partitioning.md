# Case Scenario: Partitioning

## Single Partitioning

The partitioning in any iceberg table is column based. Currently, Flare currently supports only these Partition Transforms identity, year, month, day, and hour.

- ### **identity**
    
    ```bash
    dataos-ctl dataset -a dataos://icebase:retail/city \
    -p "identity:state_name"
    ```
    
- ### **year**
    
    ```bash
    dataos-ctl dataset -a dataos://icebase:retail/city \
    -p "year:ts_city:year_partition"
    ```
    
- ### **month**
    
    ```bash
    dataos-ctl dataset -a dataos://icebase:retail/city \
    -p "month:ts_city:month_partition"
    ```
    
- ### **day**
    
    ```bash
    dataos-ctl dataset -a dataos://icebase:retail/city \
    -p "day:ts_city:day_partition"
    ```
    
- ### **hour**
    
    ```bash
    dataos-ctl dataset -a dataos://icebase:retail/city \
    -p "hour:ts_city:hour_partition"
    ```
    

## Multiple Partitioning
Partitioning can be done on multiple levels. For e.g, a user wants to partition the city data into two partitions, first based on `state_code` and second based on `month`. The command will be as follows:

```bash
dataos-ctl dataset -a dataos://icebase:retail/city \
-p "identity:state_code" \
-p "month:ts_city:month_partition"
```

<aside style="background-color:#FAF3DD; padding:15px; border-radius:5px;">

🗣 **Note:** The order of partition given should be the hierarchy in which the user needs the data to be partitioned.
</aside>

## Partition Updation

For updating partition, use the below command.
```bash
dataos-ctl dataset -a dataos://icebase:retail/city update-partition \
-p "<partition_type>:<column_name>:<partition_name>"
```

Let’s say we wanna update the partition of city data along the `month` using the timestamp in the `ts_city` column, the code will be as follows -

```bash
dataos-ctl dataset -a dataos://icebase:retail/city update-partition \
-p "month:ts_city:month_partition"
```

Output

```bash
INFO[0000] 📂 update partition...                        
INFO[0000] 📂 update partition...completed
```