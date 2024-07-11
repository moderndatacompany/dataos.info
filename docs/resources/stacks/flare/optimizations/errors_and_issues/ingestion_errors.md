# Ingestion Errors


## Error: Job finished with error=Could not alter output datasets for workspace

**Message**

```bash
22/10/17 12:29:14 INFO Flare$: Gracefully stopping Spark Application
22/10/17 12:29:14 ERROR ProcessingContext: =>Flare: Job finished with error=Could not alter output datasets for workspace: p....
There is an existing job with same workspace: public and name: account-new-n writing into below datasets
		1. dataos://icebase:gcdcore_bronze/gcdcore_account
You should use a different job name for your job as you cannot change output datasets for any job
Exception in thread "shutdownHook1" io.dataos.flare.exceptions.FlareException: Could not alter output datasets for workspace
There is an existing job with same workspace; public and name: account-new-n writing into below datasets
		1. dataos://icebase:gcdcore_bronze/gcdcore_account
You should use a different job name for your job as you cannot change output datasets for any job.
		at io.dataos.flare.contexts.ProcessingContext.error(ProcesingContext.scala:87)
```

**What went wrong?**

The reason is same workflow name already exists because the same workflow is already used by another person and maybe you can also use the same workflow in the past yaml.

**Solution**

Change the job/workflow name

## Error: Too old resource version

**Message**

```bash
				at java.lang.Thread.run(Thread.java:748)
Caused by: io.fabric8.kubernetes.client.KubernetesClientException: **too old resource version**: 71146153
				... 11 common frames omitted
2022-03-14 06:11:35,830 INFO [dispatcher-BlockManagerMaster] o.a.s.s.BlockManagerInfo: Added taskresu...
, free: 10.9 GiB)
```

**What went wrong?**

It's the standard behaviour of Kubernetes to give 410 after some time during watch. It's usually the client's responsibility to handle it. In the context of a watch, it will return `HTTP_GONE` when you ask to see changes for a `resourceVersion` that is too old - i.e. when it can no longer tell you what has changed since that version since too many things have changed. In that case, you'll need to start again and upgrade to the `latest version`

## Error: Too Many Data Columns

**What went wrong?**

This happens because the column has been `incremented` at the time of ingestion.

## Error: Apply Error

![Untitled](/resources/stacks/flare/ingestion_errors/untitled.png)

```bash
tmdc@tmdc:~/data$ dataos-ctl apply -f data-ingestion/flare/super-dag/config-super-dag1.yaml -l  
INFO[0000] 🛠 apply...                                    
INFO[0000] 🔧 applying(public) bronze-s-dag1:v1beta1:workflow...  
ERRO[0000] 🔧 applying(public) bronze-s-dag1:v1beta1:workflow...error  
WARN[0000] ⚠️ failure matching dag step:  cannot proceed  
ERRO[0000] 🛠 **apply...error**                               
ERRO[0000] failure applying a resource
```

## Error: Same workflow name already exists

```verilog
There is an existing job with same workspace: public and name: camp-connect-city writing into below datasets
  1. dataos://icebase:campaign/city
 You should use a different job name for your job as you cannot change output datasets for any job.
```

Solution

You can change the workflow name. 

**What went wrong?**

## Error: Path Not Found Error

**Message**

```verilog
22/06/27 05:51:33 ERROR ProcessingContext: =>Flare: Job finished with error=Path does not exist: s3a://tmdc-dataos/demo-mockdata/data-analyst/campaigns02.csv
Exception in thread "shutdownHook1" io.dataos.flare.exceptions.FlareException: Path does not exist: s3a://tmdc-dataos/demo-mockdata/data-analyst/campaigns02.csv
```

**What went wrong?**

If your input path does not match from cloud source then the path is not found when your will failed. To rectify the error:

1. Check input path
2. Validate the path from resources.

## Error: label-names and the value length <= 47

```verilog
spark.kubernetes.executor.podNamePrefix is invalid. must conform https://kubernetes.io/docs/concepts/overview/working-with-objects/names/
#dns-label-names and the value length <= 47
```

**What went wrong?**

The reason behind the error is workflow and dag name are less than equal to 47. if the length is more than 47 then the job will be failed. To resolve this you can reduce the length of workflow & dag name.

## Error: Hera bases not provided

**Message**

```verilog
Exception in thread "main" java.lang.Exception: Fatal! env HERA_BASE_URL not provided.
```

**What went wrong?**

Hera bases missing. 

**Solution**

Hera Bases need to be provided in the following format - 

```yaml
envs:
  HERA_SSL: "false"
  HERA_BASE_URL: "https://eager-skylark.dataos.app/hera"
```
