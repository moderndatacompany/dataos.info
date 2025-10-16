# Monitor the Status and Runtime of the Cluster

The status indicates the Resource's lifecycle state, such as `active`, `error`, or `deleted`, and helps users quickly assess whether the Resource is available and functioning as expected. In contrast, the runtime reflects the Resource's execution state, such as `running`, `failed`, or `pending`, capturing what is actively happening behind the scenes, typically at the container or pod level. Together, these signals help users to detect configuration issues, operational failures, and disruptions that could impact downstream workflows.

<aside class="callout">
🗣 A Resource is considered healthy when its status is `active` and its runtime is either `running` or `succeeded`, depending on the type of workload it handles. For long-running services, a `running` runtime indicates health, whereas for batch jobs or workflows, `succeeded` confirms successful execution. Both signals together ensure the Resource is available and behaving as expected.
</aside>

## Monitor the status and runtime of a Cluster using DataOS CLI

The status and Runtime of a Cluster can be monitored using the DataOS CLI by executing the following command.

```bash
dataos-ctl get -t cluster -w public
```

**Example Usage:**

```bash
dataos-ctl get -t cluster -w public -a
INFO[0000] 🔍 get...
INFO[0001] 🔍 get...complete

NAME    | VERSION |  TYPE   | WORKSPACE |   STATUS    |  RUNTIME  |         OWNER
------------|---------|---------|-----------|-------------|-----------|-------------------------
lakehouse  | v1      | cluster | public    | active | running:1 | iamgroot 
```

## Monitor the status and runtime of a Cluster using Metis

To monitor the status and runtime of a Cluster on the Metis Catalog UI, follow the steps below:

1. Open the Metis Catalog.
    
    <div style="text-align: center;">
      <div style="text-align: center;">
        <img src="/products/data_product/observability/status/cluster/cluster_dataos_metis_activity_products_assets.png" style="width: 70%; height: auto;">
        <figcaption><i>BS DataOS® metis Activity Products Assets Resources Ally lakehouse ul (K] ® Govern Settings O © & Clusters | public 3...</i></figcaption>
      </div>
      <figcaption><i>Observability in DataOS</i></figcaption>
    </div>
    
2. Search for the Cluster by name.
    
    <div style="text-align: center;">
      <div style="text-align: center;">
        <img src="/products/data_product/observability/status/cluster/cluster_dataos_metis_activity_products_assets.png" style="width: 70%; height: auto;">
        <figcaption><i>BS DataOS® metis Activity Products Assets Resources Ally lakehouse ul (K] ® Govern Settings O © & Clusters | public 3...</i></figcaption>
      </div>
      <figcaption><i>Observability in DataOS</i></figcaption>
    </div>
    
3. Click on the Cluster that needs to be monitored and check the status and runtime.
    
    <div style="text-align: center;">
      <div style="text-align: center;">
        <img src="/products/data_product/observability/status/cluster/cluster_dataos_metis_activity_products_assets.png" style="width: 70%; height: auto;">
        <figcaption><i>BS DataOS® metis Activity Products Assets Resources Ally lakehouse ul (K] ® Govern Settings O © & Clusters | public 3...</i></figcaption>
      </div>
      <figcaption><i>Observability in DataOS</i></figcaption>
    </div>
    

## Monitor the status and runtime of a Cluster on Operations

To monitor the status and runtime of a Cluster on the Operations app, follow the steps below:

1. Open the Operations app.
    
    <div style="text-align: center;">
      <img src="/products/data_product/observability/observability.png" style="width: 70%; height: auto;">
      <figcaption><i>Observability in DataOS</i></figcaption>
    </div>
    
2. Under the User space → type → Cluster, search for the Cluster that needs to be monitored.
    
    <div style="text-align: center;">
      <div style="text-align: center;">
        <img src="/products/data_product/observability/cpu/cluster/cluster_dataos_operations_user_space_core.png" style="width: 70%; height: auto;">
        <figcaption><i>né DataOS? operations User Space Core Kernel Cloud Kernel Product @ 2 User Space Resources Minerva Queries Cluster An...</i></figcaption>
      </div>
      <figcaption><i>Observability in DataOS</i></figcaption>
    </div>
    
3. On clicking the Cluster, its detailed logs can also be monitored.
    
    <div style="text-align: center;">
      <div style="text-align: center;">
        <img src="/products/data_product/observability/cpu/cluster/cluster_dataos_operations_user_space_core.png" style="width: 70%; height: auto;">
        <figcaption><i>né DataOS? operations User Space Core Kernel Cloud Kernel Product @ 2 User Space Resources Minerva Queries Cluster An...</i></figcaption>
      </div>
      <figcaption><i>Observability in DataOS</i></figcaption>
    </div>
    

## Configure Alerts for Status Changes

To proactively track critical state transitions, users can configure a Monitor and Pager to send alerts when the status of a Cluster changes to values like `error` or `deleted`. This enables teams to respond immediately to resource failures, misconfigurations, or unexpected deletions that may impact dependent components. [Click here to view the steps to set up alerts for status changes]().

## Configure Alerts for Runtime Changes

To proactively detect execution issues, users can configure a Monitor and Pager to send alerts when the runtime of a Cluster enters a failure state, such as `failed` or remains stuck in `pending`. This ensures timely awareness of broken or stalled executions that may affect downstream processes. [Click here to view the steps to set up alerts for runtime failures.]()
