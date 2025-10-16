# Monitor the Status of the Compute

In DataOS, the status of a Resource indicates its current life-cycle state, such as `active`, `error`, or `deleted`. Monitoring status allows teams to detect state transitions (e.g., from `active` to `deleted` or `error`) that may impact downstream dependencies, trigger configuration issues, or reflect access problems. 

## Monitor the Status of Compute using DataOS CLI

The status of a Compute can be monitored using the DataOS CLI by executing the following command. This command will list all the computes created by the user.

```bash
dataos-ctl get -t compute 
```

**Example Usage:**

```bash
dataos-ctl get -t compute
INFO[0000] 🔍 get...                                     
INFO[0001] 🔍 get...complete                             

        NAME       | VERSION |      TYPE       | WORKSPACE | STATUS | RUNTIME |    OWNER     
-------------------|---------|-----------------|-----------|--------|---------|--------------
  new-usecases     | v1beta  |    compute      |           | active |         | iamgroot   
```

In the example above, the `STATUS` column indicates the current state of the Compute`active` in this case, which confirms that the Compute is available and usable. 

## Monitor the Status of Compute on Metis

To monitor the status of Compute on the Metis Catalog UI, follow the steps below:

1. Open the Metis Catalog.
    
    <div style="text-align: center;">
      <img src="/products/data_product/observability/observability.png" style="width: 70%; height: auto;">
      <figcaption><i>Observability in DataOS</i></figcaption>
    </div>
    
2. Search for a Compute by name.
    
    <div style="text-align: center;">
      <img src="/products/data_product/observability/observability.png" style="width: 70%; height: auto;">
      <figcaption><i>Observability in DataOS</i></figcaption>
    </div>
    
3. Click on the Compute that needs to be monitored and check the Status, which is represented as `State`.
    
    <div style="text-align: center;">
      <img src="/products/data_product/observability/observability.png" style="width: 70%; height: auto;">
      <figcaption><i>Observability in DataOS</i></figcaption>
    </div>
    

The `active` state indicates that the Compute is currently accessible and usable by other DataOS Resources.  This is the expected state for any Compute that is in use by other DataOS Resources.

## Monitor the Status of a Compute on Operations

To monitor the status of Compute on the Operations app, follow the steps below:

1. Open the Operations app.
    
    <div style="text-align: center;">
      <div style="text-align: center;">
        <img src="/products/data_product/observability/status/worker/worker_dataos_operations_userspace_core_kernel.png" style="width: 70%; height: auto;">
        <figcaption><i>DataOS® operations —_UserSpace _—Core Kernel User Space Resources Minerva Queries Name « — data-product-insights-wor ...</i></figcaption>
      </div>
      <figcaption><i>Observability in DataOS</i></figcaption>
    </div>
    
2. Under the User space → type → Compute, search for Compute.
    
    <div style="text-align: center;">
      <div style="text-align: center;">
        <img src="/products/data_product/observability/status/worker/worker_dataos_operations_userspace_core_kernel.png" style="width: 70%; height: auto;">
        <figcaption><i>DataOS® operations —_UserSpace _—Core Kernel User Space Resources Minerva Queries Name « — data-product-insights-wor ...</i></figcaption>
      </div>
      <figcaption><i>Observability in DataOS</i></figcaption>
    </div>
    
    The `active` status indicates that the Resource is valid and available for use within DataOS. This is the expected state for a healthy and usable Resource.
    
3. On clicking the Compute, its builder state can also be monitored.
    
    <aside class="callout">
    🗣 The Builder Stage reflects the internal progress of a DataOS Resource as it is being reconciled and provisioned by the platform. This stage is managed by the Poros controller, which is responsible for ensuring the system’s actual state matches the desired state defined in the Resource manifest (YAML).
    
    When a user applies a Resource YAML (`dataos-ctl resource apply -f resource.yaml`), the builder workflow begins. Poros orchestrates this by comparing the input state (what the user requested) with the current cluster state (what already exists), and attempts to reconcile the two.
    
    If a Resource enters an `error` state during this stage, it means something failed while setting it up. A Resource in an error state at the Builder Stage is considered not fully created and should not be treated as active, even if it appears in the UI list.
    
    </aside>
    
    <div style="text-align: center;">
      <img src="/products/data_product/observability/observability.png" style="width: 70%; height: auto;">
      <figcaption><i>Observability in DataOS</i></figcaption>
    </div>
    
    Monitoring the Builder Stage is recommended when the Resource status shows an `error`.
    
    - If the status is `error` and the Builder Stage is still `building`, it indicates that the issue occurred after the building stage.
    - If the status is `error` and the Builder Stage also shows `error`, it means the issue happened during the building stage itself.
    
    This helps in identifying whether the problem lies within the building phase or after the Resource was built.
    

## Configure Alerts for Status Changes

To automatically track critical state transitions, users can configure a Monitor and Pager to send alerts when the status of a Compute changes to values like `error` or `deleted`. This enables teams to respond immediately to resource failures, misconfigurations, or unexpected deletions that may impact dependent components. [Click here to view the steps to set up alerts for status changes](https://www.notion.so/Alerts-for-Resource-Status-Change-20fc5c1d487680519a0bf069917dec31?pvs=21).
