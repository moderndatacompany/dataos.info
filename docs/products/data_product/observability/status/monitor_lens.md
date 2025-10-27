# Monitor the Status and Runtime of the Lens

The status indicates the Resource's lifecycle state, such as `active`, `error`, or `deleted`, and helps users quickly assess whether the Resource is available and functioning as expected. In contrast, the runtime reflects the Resource's execution state, such as `running`, `failed`, or `pending`, capturing what is actively happening behind the scenes, typically at the container or pod level. Together, these signals help users to detect configuration issues, operational failures, and disruptions that could impact downstream workflows.

A Lens is a non-runnable Resource in DataOS; however, during the creation of a Lens model, a corresponding Service is automatically generated in the backend with the suffix ‘-api’. This Service handles the Lens’s API interface, and users can view its status and runtime.

<aside class="callout">
🗣 A Resource is considered healthy when its status is `active` and its runtime is either `running` or `succeeded`, depending on the type of workload it handles. For long-running services, a `running` runtime indicates health, whereas for batch jobs or workflows, `succeeded` confirms successful execution. Both signals together ensure the Resource is available and behaving as expected.
</aside>

## Monitor the status of Lens using DataOS CLI

The status of a Lens can be monitored using the DataOS CLI by executing the following command, replacing the placeholder with the workspace in which the user is working. This command will list all the Lenses created by the user.

```bash
dataos-ctl get -t lens-w ${{workspace-name}}
```

**Example Usage:**

```bash
dataos-ctl get -t lens -w public 
INFO[0000] 🔍 get...                                     
INFO[0001] 🔍 get...complete                             

                   NAME                  | VERSION | TYPE | WORKSPACE |   STATUS    | RUNTIME |           OWNER            
-----------------------------------------|---------|------|-----------|-------------|---------|----------------------------
   data-product-insights                 | v1alpha | lens | public    | active      |         | iamgroot                    
```

In the example above, the `STATUS` column indicates the current state of the Lens is `active` in this case, which confirms that the Lens is available and usable. 

## Monitor the status of Lens on Metis

To monitor the status of Lens on the Metis Catalog UI, follow the steps below:

1. Open the Metis Catalog.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/observability.png" style="width: 70%; height: auto;">
    </div>
    
2. Search for a Lens by name.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/observability.png" style="width: 70%; height: auto;">
    </div>
    
3. Click on the Lens that needs to be monitored and check the Status, which is represented as `State`.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/observability.png" style="width: 70%; height: auto;">
    </div>
    

The `active` state indicates that the Lens is currently accessible and usable by other DataOS Resources.  This is the expected state for any active Lens within DataOS.

## Monitor the status of a Lens on Operations

To monitor the status of Lens on the Operations app, follow the steps below:

1. Open the Operations app.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/observability.png" style="width: 70%; height: auto;">
    </div>
    
2. Under the User space → type → Lens search for the Lens.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/observability.png" style="width: 70%; height: auto;">
    </div>
    
    The `active` status indicates that the Resource is valid and available for use within DataOS. This is the expected state for a healthy and usable Resource.
    
3. On clicking the Lens, its builder state can also be monitored.
    
    <aside class="callout">
    🗣 The Builder Stage reflects the internal progress of a DataOS Resource as it is being reconciled and provisioned by the platform. This stage is managed by the Poros controller, which is responsible for ensuring the system’s actual state matches the desired state defined in the Resource manifest (YAML).
    
    When a user applies a Resource YAML (`dataos-ctl resource apply -f resource.yaml`), the builder workflow begins. Poros orchestrates this by comparing the input state (what the user requested) with the current cluster state (what already exists), and attempts to reconcile the two.
    
    If a Resource enters an `error` state during this stage, it means something failed while setting it up. A Resource in an error state at the Builder Stage is considered not fully created and should not be treated as active, even if it appears in the UI list.
    
    </aside>
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/observability.png" style="width: 70%; height: auto;">
    </div>
    
    Monitoring the Builder Stage is crucial, especially when `status` = `error`. If the `builder stage` = `building`, the issue likely occurred after build, possibly runtime or external issues.
    But if the `builder stage` = `error`, then the YAML file itself needs fixing.
    

## Configure alerts for status changes

To automatically track critical state transitions, users can configure a Monitor and Pager to send alerts when the status of a Lens changes to values like `error` or `deleted`. This enables teams to respond immediately to resource failures, misconfigurations, or unexpected deletions that may impact dependent components. [Click here to view the steps to set up alerts for status changes](https://www.notion.so/Alerts-for-Resource-Status-Change-20fc5c1d487680519a0bf069917dec31?pvs=21).