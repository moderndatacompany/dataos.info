# Monitor the Logs of a Workflow

This section involves the steps to observe the logs of the Workflow on different endpoints such as DataOS CLI, Metis UI, and Operations App.

<aside class="callout">
🗣 The logs of a Workflow consist of two types:
<ul>
  <li><b><code>init</code> Logs</b>: These are the logs from the init container, which runs before the main container starts. In workflows, it often handles preparation tasks, such as loading artifacts or mounting volumes. If something fails here, the main logic won’t even start.</li>
  <li><b><code>main</code> Logs</b>: These are from the primary container, where the actual workload or execution logic runs. This is where the core of the workflow pipeline executes, and most application-level logs will appear.</li>
</ul>
</aside>

## Monitor the logs of a Workflow using DataOS CLI

To monitor the logs of a Workflow using DataOS CLI, follow the steps below:

<aside class="callout">
🗣 Logs can only be viewed via the DataOS CLI for Workflows that are in a `running` state or are scheduled. If a Workflow has already `succeeded` or `failed`, its logs will no longer be accessible from the CLI. Use Metis to view historical logs in such cases.
Users will not see `init` container logs in the CLI output. If a workflow fails before entering its main logic (e.g., due to a failed init container setup), the CLI logs might appear empty.
</aside>

1. On DataOS CLI, execute the following command by replacing the placeholders with the actual values. 
    
    ```bash
    dataos-ctl log -t worklow -w ${{workspace-name}} -n ${{workflow-name}}
    ```
    
    **Example Usage:**
    
    ```bash
    dataos-ctl log -t worklow -w public -n t-sub
    
      NODE NAME │ CONTAINER NAME │ ERROR  
    ────────────┼────────────────┼────────
      t-sub-rd  │ main           │        
    
    -------------------LOGS-------------------
    time="2025-06-12T07:24:28.680Z" level=info msg="Starting Workflow Executor" version=v3.5.11
    time="2025-06-12T07:24:28.683Z" level=info msg="Using executor retry strategy" Duration=1s Factor=1.6 Jitter=0.5 Steps=5
    time="2025-06-12T07:24:28.683Z" level=info msg="Executor initialized" deadline="0001-01-01 00:00:00 +0000 UTC" includeScriptOutput=false namespace=public podName=t-sub-jvsg-kym-1635177909 templateName= version="&Version{Version:v3.5.11,BuildDate:2024-09-20T14:09:00Z,GitCommit:25bbb71cced32b671f9ad35f0ffd1f0ddb8226ee,GitTag:v3.5.11,GitTreeState:clean,GoVersion:go1.21.13,Compiler:gc,Platform:linux/amd64,}"
    time="2025-06-12T07:24:28.706Z" level=info msg="Loading manifest to /tmp/manifest.yaml"
    time="2025-06-12T07:24:28.706Z" level=info msg="kubectl delete --ignore-not-found -f /tmp/manifest.yaml -o name"
    time="2025-06-12T07:24:29.653Z" level=info msg="sub-process exited" argo=true error="<nil>"
    ```
    
    <aside class="callout">
    ⚠️ If the workflow is in a `running` state but no logs are visible, it may be due to insufficient Cluster resources (e.g., CPU, node availability) preventing the pod from starting. This scenario can be confirmed by checking the Runtime Node Details of the Workflow in the Operations App, where scheduling issues and event messages are displayed for further diagnosis.
    <div style="text-align: center;">
    <img src="/products/data_product/observability/logs/workflow/image%20(21).png" style="border:1px solid black; width: 80%; height: auto">
    </div>
    </aside>
    

## Monitor the logs of a Workflow using Metis UI

To monitor the logs of a Workflow on the Metis Catalog UI, follow the steps below:

1. Open the Metis Catalog.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/logs/workflow/image%20(22).png" style="border:1px solid black; width: 70%; height: auto">
    </div>
    
2. Search for the Workflow by name.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/logs/workflow/image%20(23).png" style="border:1px solid black; width: 70%; height: auto">
    </div>
    
3. Click on the Workflow that needs to be monitored and navigate to the ‘Run History’ section.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/logs/workflow/image%20(24).png" style="border:1px solid black; width: 70%; height: auto">
    </div>
    
4. Click on any run name for which you want to monitor the logs, and navigate to the ‘Physical Plan’ section.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/logs/workflow/image%20(25).png" style="border:1px solid black; width: 70%; height: auto">
    </div>
    
5. Under the ‘Physical Plan’ section, click on the pod name.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/logs/workflow/image%20(26).png" style="border:1px solid black; width: 70%; height: auto">
    </div>
    
6. Navigate to the pod logs section, where you can access the init and main logs.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/logs/workflow/image%20(27).png" style="border:1px solid black; width: 70%; height: auto">
    </div>
    

## Monitor the logs of a Workflow using the Operations app

<aside class="callout">
🗣 Logs for a Workflow are available on the Operations App only while the Workflow is still in progress (e.g., in a `scheduled` or `running` state). Once the Workflow succeeds or fails to execute, its logs are no longer visible in Operations. To access logs after completion, refer to the Metis UI or DataOS CLI, which retains historical logs.
</aside>

To monitor the logs of a Workflow on the Operations App, follow the steps below:

1. Open the Operations app.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/logs/workflow/image%20(28).png" style="border:1px solid black; width: 70%; height: auto">
    </div>
    
2. Navigate to User Space → Resources → Workflow and search for the Workflow by name.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/logs/workflow/image%20(29).png" style="border:1px solid black; width: 70%; height: auto">
    </div>
    
3. Click on the Workflow that needs to be monitored and navigate to the ‘Resource Runtime’ section.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/logs/workflow/image%20(30).png" style="border:1px solid black; width: 70%; height: auto">
    </div>
    
4. Click on any runtime node for which you want to monitor the logs, and navigate to the ‘Runtime Node Logs’ section. Here, users can monitor the init container and main container logs.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/logs/workflow/image%20(31).png" style="border:1px solid black; width: 70%; height: auto">
    </div>