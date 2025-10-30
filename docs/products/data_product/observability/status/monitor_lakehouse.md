# Monitor the Status of Lakehouse

In DataOS, the status of a Resource indicates its current life-cycle state, such as `active`, `error`, or `deleted`. Monitoring status allows teams to detect state transitions (e.g., from `active` to `deleted` or `error`) that may impact downstream dependencies, trigger configuration issues, or reflect access problems. 

## DataOS CLI

The status of a Lakehouse can be monitored using the DataOS CLI by executing the following command, replacing the placeholder with the workspace in which the user is working. This command will list all the Lakehouse Resources created by the user.

```bash
dataos-ctl get -t lakehouse -w ${{workspace-name}}
```

**Example Usage:**

```bash0
dataos-ctl get -t lakehouse -w public
INFO[0000] 🔍 get...                                     
INFO[0001] 🔍 get...complete                             

        NAME       | VERSION |      TYPE       | WORKSPACE | STATUS | RUNTIME |    OWNER     
-------------------|---------|-----------------|-----------|--------|---------|--------------
  lakehouse      | v1alpha |   lakehouse     |  public   | active |         | iamgroot   
```

In the example above, the `STATUS` column indicates the current state of the Lakehouse `active` in this case, which confirms that the Lakehouse is available and usable. 

## Metis UI

To monitor the status of Lakehouse on the Metis Catalog UI, follow the steps below:

1. Open the Metis Catalog.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/status/instance_secret/instance_secret_metis_catalog_endtoend_metadata_management.png" style="border:1px solid black; width: 70%; height: auto">
    <figcaption><i>Open the Metis Catalog</i></figcaption>
    </div>
    
2. Search for a Lakehouse by name.
    
    <div style="text-align: center;">
      <img src="/products/data_product/observability/status/lakehouse/lakehouse_lakehouse_policies_customersegmentspolicy_lakehouses_lakehouse.png" style="border:1px solid black; width: 70%; height: auto">
      <figcaption><i>Search the Lakehouse in Metis</i></figcaption>
      </div>
    
3. Click on the Lakehouse that needs to be monitored and check the Status, which is represented as `State`.
    
    <div style="text-align: center;">
      <img src="/products/data_product/observability/status/lakehouse/lakehouse_lakehouses_public_lakehouse_owner_dataosazure.png" style="border:1px solid black; width: 70%; height: auto">
      <figcaption><i>Lakehouse details in Metis</i></figcaption>
      </div>
    

The `active` state indicates that the Lakehouse is currently accessible and usable. This is the expected state for any Lakehouse Resource.

## Operations App

To monitor the status of Lakehouse on the Operations app, follow the steps below:

1. Open the Operations app.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/status/instance_secret/instance_secret_operations_administer_data0s_grafana.png" style="border:1px solid black; width: 70%; height: auto">
    <figcaption><i>Open the Operations app</i></figcaption>
    </div>
    
2. Under the User space → type → Lakehouse, search for the Lakehouse by name.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/status/lakehouse/lakehouse_adataos_operations_userspace_core_kernel.png" style="border:1px solid black; width: 70%; height: auto">
    <figcaption><i>Operations > User Space > Lakehouse</i></figcaption>
    </div>
    
    The `active` status indicates that the Resource is valid and available for use within DataOS. This is the expected state for a healthy and usable Resource.
    
3. On clicking the Lakehouse, its builder state can also be monitored.
    
    <aside class="callout">
    🗣 The Builder Stage reflects the internal progress of a DataOS Resource as it is being reconciled and provisioned by the platform. This stage is managed by the Poros controller, which is responsible for ensuring the system’s actual state matches the desired state defined in the Resource manifest (YAML).
    
    When a user applies a Resource YAML (`dataos-ctl resource apply -f resource.yaml`), the builder workflow begins. Poros orchestrates this by comparing the input state (what the user requested) with the current cluster state (what already exists), and attempts to reconcile the two.
    
    If a Resource enters an `error` state during this stage, it means something failed while setting it up. A Resource in an error state at the Builder Stage is considered not fully created and should not be treated as active, even if it appears in the UI list.
    
    </aside>
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/status/lakehouse/lakeouse_ops.png" style="border:1px solid black; width: 70%; height: auto">
    <figcaption><i>Lakehouse details in Operations</i></figcaption>
    </div>
    
    Monitoring the Builder Stage is recommended when the Resource status shows an `error`.
    
    - If the status is `error` and the Builder Stage is still `building`, it indicates that the issue occurred after the building stage.
    - If the status is `error` and the Builder Stage also shows `error`, it means the issue happened during the building stage itself.
    
    This helps in identifying whether the problem lies within the building phase or after the Resource was built.
    

## Status alerts

To automatically track critical state transitions, users can configure a Monitor and Pager to send alerts when the status of a Lakehouse changes to values like `error` or `deleted`. This enables teams to respond immediately to resource failures, misconfigurations, or unexpected deletions that may impact dependent components. [Click here to view the steps to set up alerts for status changes](/products/data_product/observability/alerts/alerts_resource_status_change).
