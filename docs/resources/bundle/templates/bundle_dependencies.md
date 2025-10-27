# Bundle Template with Dependencies

This YAML template demonstrates a Bundle Resource with sequential Resource dependencies. It showcases how to orchestrate Resource deployment in a specific order using the `dependencies` and `dependencyConditions` attributes to ensure Resources are created only when their dependent Resources reach the required state.

## Use Case

This template is ideal for scenarios where:

- Resources must be created in a specific sequence (e.g., Depot → Cluster → Workflow)
- Each Resource depends on the successful creation and activation of previous Resources
- You need to ensure infrastructure is ready before deploying workloads
- Complex multi-step deployments require orchestrated execution order

## Template

```yaml
version: v1beta
name: sfbundle01
type: bundle
tags:
  - dataproduct
  - transaction
description: This bundle Resource is for customer data product.
layer: user
bundle:
  workspaces:
    - name: public
      description: "This workspace runs dataos bundle Resource for test"
      layer: user

  Resources:

    - id: mydepot
      file: /home/office/bundle-test/depot.yaml

    - id: mycluster
      file: /home/office/bundle-test/cluster.yaml
      workspace: public
      dependencies:
        - mydepot
      dependencyConditions:
        - ResourceId: mydepot
          status:
            is:
              - active

    - id: flarejob
      file: /home/office/bundle-test/flare.yaml
      workspace: public
      dependencies:
        - mycluster
      dependencyConditions:
        - ResourceId: mycluster
          status:
            is:
              - active   
          runtime:
            is: 
              - running:1    
```

## Resource Flow

1. **Depot Creation** (`mydepot`): Creates a data connection/depot as the foundation
2. **Cluster Setup** (`mycluster`): Creates a compute cluster only after the depot is `active`
3. **Flare Job Execution** (`flarejob`): Runs a data processing job only when the cluster is `active` and has at least one pod `running`


## Customizations

**To adapt this template for your use case:**

1. **Update Resource IDs**: Replace `mydepot`, `mycluster`, and `flarejob` with meaningful identifiers for your Resources
2. **Modify File Paths**: Update the `file` attribute paths to point to your actual Resource manifest files
3. **Adjust Workspace**: Change the `workspace` name from `public` to your target workspace
4. **Configure Dependencies**: Modify the dependency chain based on your Resource orchestration requirements
5. **Set Dependency Conditions**: Customize `status` and `runtime` conditions to match your specific deployment needs
6. **Update Metadata**: Change `name`, `tags`, and `description` to reflect your data product or application

## Understanding Dependency Conditions

Dependency conditions control when a Resource should be created based on the state of its dependencies. They use two key attributes: `status` and `runtime`.
The following tables show the possible values you can use for status and runtime conditions:

**Status Values**

| Status Value | Description | Use Case |
|--------------|-------------|----------|
| `active` | Resource is operational and ready | Most common condition - ensures Resource is fully initialized |
| `pending` | Resource is being created or initialized | Wait for Resources that are in progress |
| `failed` | Resource creation or execution failed | Check for failure states before proceeding |
| `error` | Resource encountered an error | Similar to failed, indicates error conditions |

**Runtime Values**

| Runtime Value | Description | Use Case |
|--------------|-------------|----------|
| `running` | Resource is currently executing | Ensure workloads are active |
| `running:N` | At least N pods/instances are running | Verify minimum replicas (e.g., `running:1`, `running:3`) |
| `succeeded` | Resource completed successfully | Wait for completion of jobs/workflows |
| `failed` | Resource execution failed | Check for failure conditions |

<aside class="callout">
🗣 <b>Understanding <code>is</code> vs <code>contains</code></b><br><br>
When defining dependency conditions, you can use two operators for matching:<br><br>

<code>is</code> - Exact Match: The Resource status or runtime must exactly match one of the specified values. This is a strict equality check.<br>
<pre><code>status:
  is:
    - active    # Resource status must be exactly "active"</code></pre>

<code>contains</code> - Partial Match: The Resource status or runtime must contain one of the specified values as a substring. This allows for flexible matching.<br>
<pre><code>status:
  contains:
    - pending   # Matches "pending", "pending:0/2", etc.</code></pre>

When to use each:
<ul>
<li>Use <code>is</code> for precise state matching (recommended for most cases)</li>
<li>Use <code>contains</code> when you need flexible matching across multiple state variations</li>
<li>You can combine both in the same condition - if either matches, the condition is satisfied</li>
</ul>
</aside>

### **Example 1: Wait for Active Status**

```yaml
dependencyConditions:
  - ResourceId: mydepot
    status:
      is:
        - active
```
The dependent Resource will only be created when `mydepot` status is exactly `active`.

### **Example 2: Wait for Running Cluster with Minimum Replicas**

```yaml
dependencyConditions:
  - ResourceId: mycluster
    status:
      is:
        - active
    runtime:
      is:
        - running:1
```
The dependent Resource waits for `mycluster` to be `active` AND have at least 1 pod running.


### **Example 4: Combining Multiple Conditions**

```yaml
dependencyConditions:
  - ResourceId: scanner
    status:
      is:
        - active
    runtime:
      is:
        - succeeded
```
The condition is met if status is exactly `active` AND runtime is `succeeded`.
