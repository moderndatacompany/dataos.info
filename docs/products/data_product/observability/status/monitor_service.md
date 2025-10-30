# Monitor the status and runtime of a Service

The status indicates the Resource's lifecycle state, such as `active`, `error`, or `deleted`, and helps users quickly assess whether the Resource is available and functioning as expected. In contrast, the runtime reflects the Resource's execution state, such as `running`, `failed`, or `pending`, capturing what is actively happening behind the scenes, typically at the container or pod level. Together, these signals help users to detect configuration issues, operational failures, and disruptions that could impact downstream workflows.

<aside class="callout">
🗣 A Resource is considered healthy when its status is `active` and its runtime is either `running` or `succeeded`, depending on the type of workload it handles. For long-running services, a `running` runtime indicates health, whereas for batch jobs or workflows, `succeeded` confirms successful execution. Both signals together ensure the Resource is available and behaving as expected.
</aside>

## DataOS CLI

The status and Runtime of a Service can be monitored using the DataOS CLI by executing the following command.

```bash
dataos-ctl get -t service -w public
```

**Example Usage:**

```bash
dataos-ctl get -t service -w public
INFO[0000] 🔍 get...                                     
INFO[0001] 🔍 get...complete                             

           NAME          | VERSION |  TYPE   | WORKSPACE | STATUS |  RUNTIME  |    OWNER     
-------------------------|---------|---------|-----------|--------|-----------|--------------
  flash-service-training | v1      | service | public    | active | running:1 | iamgroot  
  pals01                 | v1      | service | public    | active | running:1 | iamgroot  
```

## Metis UI

To monitor the status and runtime of a Service on the Metis Catalog UI, follow the steps below:

1. Open the Metis Catalog.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/status/instance_secret/instance_secret_metis_catalog_endtoend_metadata_management.png" style="border:1px solid black; width: 70%; height: auto">
    <figcaption><i>Open the Metis Catalog</i></figcaption>
    </div>
    
2. Search for the Service by name.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/status/service/service_flashservicetraining_tables_lakehouse_modemtesting_lakehouse.png" style="border:1px solid black; width: 70%; height: auto">
    <figcaption><i>Search the Service in Metis</i></figcaption>
    </div>
    
3. Click on the Service that needs to be monitored and check the status and runtime.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/status/service/service_flashservicetraining_owner_iamgroot_tier_domain.png" style="border:1px solid black; width: 70%; height: auto">
    <figcaption><i>Service details in Metis</i></figcaption>
    </div>
    

## Operations App

To monitor the status and runtime of a Service on the Operations app, follow the steps below:

1. Open the Operations app.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/status/instance_secret/instance_secret_operations_administer_data0s_grafana.png" style="border:1px solid black; width: 70%; height: auto">
    <figcaption><i>Open the Operations app</i></figcaption>
    </div>
    
2. Under the User space → type → Service, search for the Service that needs to be monitored.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/status/service/service_adataos_operations_userspace_core_kernel.png" style="border:1px solid black; width: 70%; height: auto">
    <figcaption><i>Operations > User Space > Service</i></figcaption>
    </div>
    
3. On clicking the Service, its detailed logs can also be monitored.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/status/service/service_flashservicetraining_resource_details_resource_yaml.png" style="border:1px solid black; width: 70%; height: auto">
    <figcaption><i>Service resource details in Operations</i></figcaption>
    </div>
    

## Status alerts

To proactively track critical state transitions, users can configure a Monitor and Pager to send alerts when the status of a Service changes to values like `error` or `deleted`. This enables teams to respond immediately to resource failures, misconfigurations, or unexpected deletions that may impact dependent components. [Click here to view the steps to set up alerts for status changes](/products/data_product/observability/alerts/alerts_resource_status_change).

## Runtime alerts

To proactively detect execution issues, users can configure a Monitor and Pager to send alerts when the runtime of a Service enters a failure state, such as `failed` or remains stuck in `pending`. This ensures timely awareness of broken or stalled executions that may affect downstream processes. [Click here to view the steps to set up alerts for runtime failures.](/products/data_product/observability/alerts/alerts_runtime_failure).
