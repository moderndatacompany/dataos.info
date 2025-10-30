# Monitor the Status and Runtime of the Depot

The status indicates the Resource's lifecycle state, such as `active`, `error`, or `deleted`, and helps users quickly assess whether the Resource is available and functioning as expected. In contrast, the runtime reflects the Resource's execution state, such as `running`, `failed`, or `pending`, capturing what is actively happening behind the scenes, typically at the container or pod level. Together, these signals help users to detect configuration issues, operational failures, and disruptions that could impact downstream workflows.

<aside class="callout">
🗣 A Resource is considered healthy when its status is `active` and its runtime is either `running` or `succeeded`, depending on the type of workload it handles. For long-running services, a `running` runtime indicates health, whereas for batch jobs or workflows, `succeeded` confirms successful execution. Both signals together ensure the Resource is available and behaving as expected.
</aside>

## DataOS CLI

Users can check whether a Depot is active or deleted by running the command `dataos-ctl resource get -t depot -n ${{depotname}}` in the DataOS CLI. The output will appear as follows:

```bash
dataos-ctl get -t depot -n systemstreams              
INFO[0000] 🔍 get...                                     
INFO[0000] 🔍 get...complete                             
      NAME      | VERSION | TYPE  | WORKSPACE | STATUS | RUNTIME |     OWNER       
----------------|---------|-------|-----------|--------|---------|-----------------
  systemstreams | v1      | depot |           | active |         | dataos-manager
```

<aside class="callout">
🗣 Only Depots created on Object Storage (S3, Azure, AWS, or GCS) will have a runtime available.
</aside>

## Metis UI

Users can track the status of a Depot, whether active or deleted, along with the total count of active and deleted Depots through the Metis UI.

- Simply navigate to `Resources → Depots` to check the status of any Depot within the environment. Additionally, users can quickly find a specific Depot by searching for its name in the Metis UI search bar.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/status/instance_secret/instance_secret_metis_catalog_endtoend_metadata_management.png" style="border:1px solid black; width: 70%; height: auto">
    <figcaption><i>Open the Metis Catalog</i></figcaption>
    </div>
    
- When a user clicks on a specific Depot, they can also track the aggregated status along with the runtime, which applies only to the object storage Depots.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/status/depot/depot_dataosmetis_activity_products_assets_resources_dup.png" style="border:1px solid black; width: 70%; height: auto">
    <figcaption><i>Depot details in Metis</i></figcaption>
    </div>
    
- To check the runtime of a Depot (If applicable), simply navigate to the ‘Runtime’ tab as shown below.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/status/depot/depot_depots_poss3_explore_assets_meta.png" style="border:1px solid black; width: 70%; height: auto">
    <figcaption><i>Depot runtime in Metis</i></figcaption>
    </div>
    
    The Runtime section shows the live execution environment of a Resource, in this case, a Depot. It reflects details like when the runtime was created, which workspace and data plane it’s using, its current status (e.g., `Running`), and how long it has been active. This helps users verify whether the Resource is functioning as expected in real time.
    

## Operations App

Using the Operations App, users can monitor the operational logs of a Depot. In addition to tracking its status, they can also view details such as the builder stage, Cloud Kernel Resource Count, WebService Resource Count, and, if applicable, the Operator Runtime Resource Count.

Follow the steps below to monitor a Depot on the Operations app:

1. Open the Operations app.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/status/instance_secret/instance_secret_operations_administer_data0s_grafana.png" style="border:1px solid black; width: 70%; height: auto">
    <figcaption><i>Open the Operations app</i></figcaption>
    </div>
    
2. Navigate to the User Space tab and go to the Resources section.
3. Select Depot as the Resource type to filter all Depots in the environment.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/status/depot/depot_dataos_operations_user_space_core.png" style="border:1px solid black; width: 70%; height: auto">
    <figcaption><i>Operations > User Space > Depot</i></figcaption>
    </div>
    
4. Search for or select the target Depot.
5. Monitor its status, including Cloud Kernel Resource Count, WebService Resource Count, Operator Runtime Resource Count, Builder Stage, and Runtime Status.
    
    <div style="text-align: center;">
      <img src="/products/data_product/observability/status/depot/depot_dataos_operations_user_space_corel.png" style="border:1px solid black; width: 70%; height: auto">
      <figcaption><i>Depot status and runtime in Operations</i></figcaption>
    </div>

    
    Monitoring the Builder Stage is recommended when the Resource status shows an `error`.
    
    - If the status is `error` and the Builder Stage is still `building`, it indicates that the issue occurred after the building stage.
    - If the status is `error` and the Builder Stage also shows `error`, it means the issue happened during the building stage itself.
    
    This helps in identifying whether the problem lies within the building phase or after the Resource was built.
    

## Status alerts

To proactively track critical state transitions, users can configure a Monitor and Pager to send alerts when the status of a Depot changes to values like `error` or `deleted`. This enables teams to respond immediately to resource failures, misconfigurations, or unexpected deletions that may impact dependent components. [Click here to view the steps to set up alerts for status changes](/products/data_product/observability/alerts/alerts_resource_status_change).

## Runtime alerts

To proactively detect execution issues, users can configure a Monitor and Pager to send alerts when the runtime of a Resource enters a failure state, such as `failed` or remains stuck in `pending`. This ensures timely awareness of broken or stalled executions that may affect downstream processes. [Click here to view the steps to set up alerts for runtime failures.](/products/data_product/observability/alerts/alerts_runtime_failure).
