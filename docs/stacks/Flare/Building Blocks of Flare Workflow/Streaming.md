# **Streaming**

# **Structure of Streaming Section**

```yaml
streaming:
  triggerMode: ProcessingTime #(Optional)
  triggerDuration: 10 seconds #(Optional)
  outputMode: append #(Optional)
  checkpointLocation: /tmp/checkpoint #(Optional)
  forEachBatchMode: true #(Optional)
  extraOptions:
    opt: val #(Optional)
```

To know more about a case scenario on Streaming Job, refer to
[Stream Job](/mkdocs/Mk%20Docs/Transformation/Flare/Case%20Scenario/Stream%20Job.md).

| Property | Description | Example | Default Value | Possible Values | Note/Rule | Field (Mandatory / Optional) |
| --- | --- | --- | --- | --- | --- | --- |
| `streaming` | Set options for each batch streaming writing or setting default streaming configuration. | `streaming:` <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `{}` | NA | NA | NA | Optional |
| `triggerMode` | Set the trigger mode  | `triggerMode:ProcessingTime` | NA | `ProcessingTime`, <br> `Once`, <br> `Continuous`, <br> `AvailableNow` | NA | Optional |
| `triggerDuration` | Set the trigger duration | `triggerDuration: 10 seconds` | NA | NA | If the trigger is `ProcessingTime`/`Continuous`  | Optional |
| `outputMode` | Output mode | `outputMode: append` | NA | `append`,`replace`,`complete` | NA | Optional |
| `checkpointLocation` | Where to save Spark's checkpoint | `checkpointLocation: /tmp/checkpoint` | NA | NA | NA | Optional |
| `forEachBatchMode` | Optionally set streaming to use forEachBatchMode when writing streams. This enables writing to all available writers and to write to multiple outputs. | `forEachBatchMode: true` | `false` | `true`/`false` | NA | Optional |
| `extraOptions` | Add any other options supported by the DataStreamWriter | `extraOptions:`  <br> &nbsp;&nbsp;&nbsp;&nbsp;`opt: val`  | NA | NA | NA | Optional |