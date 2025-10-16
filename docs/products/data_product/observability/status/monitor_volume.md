# Monitor the Status of Volume

In DataOS, the status of a Resource indicates its current life-cycle state, such as `active`, `error`, or `deleted`. Monitoring status allows teams to detect state transitions (e.g., from `active` to `deleted` or `error`) that may impact downstream dependencies, trigger configuration issues, or reflect access problems. 

## Monitor the Status of Volume using DataOS CLI

The status of Volume can be monitored using the DataOS CLI by executing the following command, replacing the placeholder with the workspace in which the user is working. This command will list all the Volumes created by the user.

```bash
dataos-ctl get -t volume -w ${{workspace-name}}
```

**Example Usage:**

```bash
dataos-ctl get -t volume -w public
INFO[0000] 🔍 get...                                     
INFO[0001] 🔍 get...complete                             

        NAME       | VERSION |      TYPE       | WORKSPACE | STATUS | RUNTIME |    OWNER     
-------------------|---------|-----------------|-----------|--------|---------|--------------
   pap-volume      | v1beta  |     volume      |  public   | active |         | iamgroot   
```

In the example above, the `STATUS` column indicates the current state of the Volume `active` in this case, which confirms that the Volume is available and usable. 

## Monitor the Status of Volume on Operations

To monitor the status of Volume on the Operations app, follow the steps below:

1. Open the Operations app.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/observability.png" style="width: 70%; height: auto;">
    </div>
    
2. Under the User space → type → Volume, search for the Volume by name.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/observability.png" style="width: 70%; height: auto;">
    </div>
    
    The `active` status indicates that the Resource is valid and available for use within DataOS. This is the expected state for a healthy and usable Resource.
    
3. On clicking the Volume name, its builder state can also be monitored.
    
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
    

## Configure Alerts for Status Changes

To automatically track critical state transitions, users can configure a Monitor and Pager to send alerts when the status of a Volume changes to values like `error` or `deleted`. This enables teams to respond immediately to resource failures, misconfigurations, or unexpected deletions that may impact dependent components. [Click here to view the steps to set up alerts for status changes](https://www.notion.so/Alerts-for-Resource-Status-Change-20fc5c1d487680519a0bf069917dec31?pvs=21).