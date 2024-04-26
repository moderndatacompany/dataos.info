# Streaming Errors


## Error: Job finished with error = CheckPoint Location must be specified either through option ("checkpointlocation")

**Message**

```bash
Spark Application
Job finished with Error= checkpointLocation must be specified either through option /
("checkpointLocation",_checkpointLocation", ...)
```


**What went wrong?**

Checkpoint location won't work if `isstream` is `false`

**Solution**

Check `isstream` mode (true or false).

## Error: Job finished with error =  Non-time based windows  are not  supported  on streaming  Dataframes/Datasets

**Message**

```bash
stopping Spark Application
Flare: Job finished with error=Non-time-based windows are not supported on streaming DataFrames/Datasets; line 9

cal_period_id#50, gcd_modified_utc#56 DESC NULLS LAST, specifiedwindowframe(RowFrame, unboundedpreceding$(), cur.......
], [gcd modified utc#56 DESC NULLS LAST]
```

**What went wrong?**

Windows functions do not work with streaming