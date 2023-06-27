# Transformation Errors


## Error: Caused By **Already closed files for partition: month**

**Message**

```bash
    ...62 more
Caused by: java.lang.IllogicalStateException: Already closed files for partition: month=2019-04
		at org.apache.iceberg.io.PartitionedWriter.write(PartitionedWriter.java:69)
		at org.apache.spark.sql.execution.datasources.v2.DataWritingSparkTask$.$anonfun$run$run$1(WriteT.....
```

**What went wrong?**

This basically happens when the partition is not done on the correct column or if the data is large we need to sort it by that column to avoid this error. 

**Solution**

To rectify the issue, the partition on the `date/time` column should be done like this

```yaml
saveMode: overwrite 
sort: 
  mode: partition 
  columns: 
    - name: gcd_modified_utc 
      order: asc 
iceberg: 
  properties: 
    overwrite-mode: dynamic 
    write.format.default: parquet 
    write.metadata.compression-codec: gzip 
  partitionSpec: 
    - type: day 
      column: gcd_modified_utc 
      name: day
```

## Error: **Caused by Cannot write incompatible data to table**

**Message**

```bash
				at org.apache.spark.deploy.SparkSubmit$.main(SparkSubmit.scala:1052)
				at org.apache.spark.deploy.SparkSubmit.main(SparkSubmit.scala)
Caused by: org.apache.spark.sql.AnalysisException: Cannot write incompatible data to table
/gcdcore_bronze/gcdcore_fiscal_period':
- Cannot safely cast 'start_date': string to timestamp
- Cannot safely cast 'end_date': string to timestamp
- Cannot safely cast 'gcd_modified_utc': string to timestamp
				at org.apache.spark.sql.errors.QueryCompilationErrors$.cannotWriteIncompatibleDataToTable...
```

**What went wrong?**

Due to incompatible data in table

**Solution**

Cast the `date/time` column as `timestamp`

Convert `date/time` column to `timestamp`

## Error: **Job finished with error = java.lang.string Cannot be cast to java.lang.boolean**

**Message**

```bash
Stopping Spark Application
Flare: Job finished with error=java.lang.String cannot be cast to java.lang.Boolean
...os.flare.exceptions.FlareException: java.lang.String cannot be cast to java.lang.Boolean
..ingContext.error(ProcessingContext.scala:87)
..addShutdownHook$1(Flare.scala:79)
..on$1.run(ShutdownHookThread.scala:37)
<-0] o.a.s.u.ShutDownHookManager: Shutdown hook called
```

```bash
				at org.apache.spark.deploy.SparkSubmit$.main(SparkSubmit.scala)
Caused by: java.lang.ClassCastException: **java.lang.String cannot be cast to java.lang.Boolean**
				at scala.runtime.BoxesRunTime.unboxToBoolean(BoxesRunTime.java:87)
				at io.dataos.flare.configurations.job.input.File.getReader(File.scala:42)
				at io.dataos.flare.configurations.job.input.DatasetInput.getReader(Input.scala:167)
				at io.dataos.flare.configurations.job.input.Input.getReader(Input.scala:61)
				at io.dataos.flare.configurations.job.JobConfiguration.$anonfun$readers$1(JobConfiguration...
```

**What went wrong?**

The spelling of `false` was wrong in the batch mode

Table of Contents