# Monitor the Status of Instance Secret

In DataOS, the status of a Resource indicates its current life-cycle state, such as `active`, `error`, or `deleted`. Monitoring status allows teams to detect state transitions (e.g., from `active` to `deleted` or `error`) that may impact downstream dependencies, trigger configuration issues, or reflect access problems. 

## Monitor the Status of the Instance Secret using DataOS CLI

The status of an Instance Secret can be monitored using the DataOS CLI by executing the following command.

```bash
dataos-ctl get -t instance-secret
```

**Example Usage:**

```bash
dataos-ctl get -t instance-secret
INFO[0000] 🔍 get...                                     
INFO[0001] 🔍 get...complete                             

        NAME       | VERSION |      TYPE       | WORKSPACE | STATUS | RUNTIME |    OWNER     
-------------------|---------|-----------------|-----------|--------|---------|--------------
  bqdepot-r        | v1      | instance-secret |           | active |         | iamgroot  
  bqdepot-rw       | v1      | instance-secret |           | active |         | iamgroot  
```

In the example above, the `STATUS` column indicates the current state of the Instance Secret `active` in this case, which confirms that the Instance Secret is available and usable. 

## Monitor the Status of the Instance Secret on the Metis Catalog

To monitor the status of an Instance Secret on the Metis Catalog UI, follow the steps below:

1. Open the Metis Catalog.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/status/instance_secret/instance_secret_metis_catalog_endtoend_metadata_management.png" style="border:1px solid black; width: 70%; height: auto;">
    <figcaption><i>Metis UI</i></figcaption>
    </div>
    
2. Search for the Instance Secret by name.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/status/instance_secret/instance_secret_bqdepot_tables.png" style="border:1px solid black; width: 70%; height: auto;">
    <figcaption><i>Metis UI</i></figcaption>
    </div>
    
3. Click on the Instance Secret that needs to be monitored and check the Status, which is represented as `State`.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/status/instance_secret/instance_secret_instance_secrets_badepotr_owner_tier.png" style="border:1px solid black; width: 70%; height: auto;">
    <figcaption><i></i>Metis UI</figcaption>
    </div>
    
    The `active` state indicates that the secret is currently accessible and usable by other DataOS Resources.  This is the expected state for any secret that is in use by other DataOS Resources.
    

## Monitor the Status of the Instance Secret on Operations

To monitor the status of an Instance Secret on the Operations app, follow the steps below:

1. Open the Operations app.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/status/instance_secret/instance_secret_operations_administer_data0s_grafana.png" style="border:1px solid black; width: 70%; height: auto;">
    <figcaption><i>Operations UI</i></figcaption>
    </div>
    
2. Under the User space → type → Instance Secret, search for the Instance Secret.
    
    <div style="text-align: center;">
      <img src="/products/data_product/observability/status/instance_secret/instance_secret_adataos_operations_userspace_core_kernel.png" style="width: 70%; height: auto;">
    <figcaption><i>Operations Ui</i></figcaption>
    </div>
    
    The `active` state indicates that the secret is currently accessible and usable by other DataOS Resources.  This is the expected state for any secret that is in use by other DataOS Resources.
    
3. On clicking the Instance Secret, its builder state can also be monitored. 
    
    <aside class="callout">
    🗣 The Builder Stage reflects the internal progress of a DataOS Resource as it is being reconciled and provisioned by the platform. This stage is managed by the Poros controller, which is responsible for ensuring the system’s actual state matches the desired state defined in the Resource manifest (YAML).
    
    When a user applies a Resource YAML (`dataos-ctl resource apply -f resource.yaml`), the builder workflow begins. Poros orchestrates this by comparing the input state (what the user requested) with the current cluster state (what already exists), and attempts to reconcile the two.
    
    If a Resource enters an `error` state during this stage, it means something failed while setting it up. A Resource in an error state at the Builder Stage is considered not fully created and should not be treated as active, even if it appears in the UI list.
    </aside>
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/status/instance_secret/instance_secret_bqdepotr_resource_details_info_name.png" style="border:1px solid black; width: 70%; height: auto;">
    <figcaption><i>Operations UI</i></figcaption>
    </div>
    
    Monitoring the Builder Stage is crucial, especially when `status` = `error`. If `builder stage` = `building`, the issue likely occurred after build, possibly runtime or external issues. But if `builder stage` = `error`, then the YAML itself needs fixing.
    

## Configure Alerts for Status Changes

To automatically track critical state transitions, users can configure a Monitor and Pager to send alerts when the status of an Instance Secret changes to values like `error` or `deleted`. This enables teams to respond immediately to resource failures, misconfigurations, or unexpected deletions that may impact dependent components. [Click here to view the steps to set up alerts for status changes](/products/data_product/observability/alerts/alerts_resource_status_change/).
