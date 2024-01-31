# Structure of Bundle YAML Manifest

```yaml
# Bundle-specific section
bundle:

	# Bundle schedule section
  schedule: 
    initialState: {{initial state}}
    timezone: {{timezone}}
    create:
      - cron: {{create cron expression}}
    delete:
      - cron: {{delete cron expression}}

	# Bundle Workspaces section
	workspaces: 
		- name: {{workspace to be created name}}
			description: {{workspace description}}
			tags: 
				- {{tag1}}
				- {{tag2}}
			labels: 
				{{key: value}}
			layer: {{layer}}

	# Bundle Resources section
	resources:
	  - id: {{resource id}}
	    workspace: {{workspace name}}
	    dependencies:
	      - {{dependent resource id 1}}
	      - {{dependent resource id 2}}
	    spec:
	      {{specific-Resource spec}}
	    file: {{Resource file reference}}

	# Additional properties section
	properties:
	  {{key: value}}
```


# Attribute configuration

### **`bundle`**

**Description:** Bundle-specific section or the mapping containing attributes of Bundle Resource.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | mandatory | none | none |

**Example Usage:**

```yaml
# Bundle-specific section
bundle:
	# Bundle Workspaces section
  workspaces:
    - name: testingspace
      description: This workspace runs dataos bundle resource
      tags:
        - dataproduct
        - product
        - bundleResource
      labels:
        name: dataproductBundleResources
      layer: user
	# Bundle Resources section
  resources:
    - id: depot
      file: yaml/1_depot.yaml

    - id: scanner
      file: yaml/2_scanner.yaml
      workspace: testingspace
      dependencies:
        - depot
      dependencyConditions:
        - resourceId: depot
          status:
            is:
              - active

    - id: profiling
      file: yaml/3_profiling.yaml
      workspace: testingspace
      dependencies:
        - scanner
      dependencyConditions:
        - resourceId: scanner
          status:
            is:
              - active
          runtime:
            is:
              - succeeded
```

---

### **`schedule`**

**Description:** Bundle schedule section or the mapping comprising attributes for scheduling Bundle Resource.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | optional | none | none |

**Example Usage:**

```yaml
schedule: 
  initialState: create
  timezone: Asia/Kolkata
  create:
   - cron: '31 0 * * *'
```

---

### **`initialState`**

**Description:** The `initialState` attribute defines the starting condition of the Bundle Resource. Setting this attribute to `create` initiates the creation of a new Bundle Resource according to the schedule outlined in the `create` attribute. Conversely, assigning the value `delete` triggers the deletion of an existing Bundle, following the cron schedule specified in the `delete` attribute.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | create/delete |

**Example Usage:**

```yaml
initialState: create
```

---

### **`timezone`**

**Description:** The timezone attribute specifies the timezone to be used in interpreting the schedule.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | valid time zone identifier from the https://en.wikipedia.org/wiki/List_of_tz_database_time_zones |

**Additional Details:** Some time zones include a provision for daylight savings time. The rules for daylight saving time are determined by the chosen time zone.

**Example Usage:**

```yaml
# Example 1
timezone: "America/New_York"
# Example 2
timezone: "Eurpoe/Berlin"
```

---

### **`create`**

**Description:** The `create` attribute specifies the schedule for creating the Bundle Resource.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| list of mappings | optional | none | none |

**Additional Details:** Defined as a list, the `create` attribute comprises cron expressions that determine when the Bundle Resource should be created. Multiple cron expressions can be included, each representing a distinct schedule. For instance, if a Workflow requires execution at two different times, such as at 00:31 and then at 01:00, the respective cron schedules can be delineated as follows:

```yaml
create:
  - cron: "31 0 * * *"
  - cron: "0 1 * * *"
```

**Example Usage:**

```yaml
create:
  - cron: "0 0 * * *"
```

---

### **`cron`**

**Description:** The `cron` attribute is used to specify a cron expression, a string consisting of five characters, separated by white spaces describing the individual details of the Bundle creation or deletion schedule.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | valid cron expression as per the https://en.wikipedia.org/wiki/Cron |

**Example Usage:**

```yaml
cron: "24 0 * * *" # Cron expression for the time 00:24
```

---

### **`delete`**

**Description:** The `delete` attribute is used to define the deletion schedule for the Bundle Resource.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list of mappings | optional | none | none |

**Additional Details:** The `delete` attribute is defined as a list of cron expressions specifying when the Bundle Resource should be deleted. You can provide one or more cron expressions within the list, each indicating a different deletion schedule.

**Example Usage:**

```yaml
delete:
  - cron: "0 8 * * *"
```

---

### **`workspaces`**

**Description:** The `workspaces` attribute, or the Bundle Workspaces section, is defined as a list comprising multiple mappings. Each mapping within this list corresponds to a distinct Workspace configuration. This attribute enables the inclusion of various Workspace configurations, each equipped with its unique set of attributes. These attributes can include `name`, `description`, `tags`, `labels`, and `layer`, allowing customization according to the specific requirements of your use case.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list of mappings | optional | none | none |

**Example Usage:**

```yaml
workspaces: 
  - name: bundletesting
    description: this is a workspace for bundle testing
		tags:
		  - testing
		labels: 
			key1: value1
    layer: user
```

---

### **`name`**

**Description:** The `name` attribute is used to specify the name of a Workspace.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | valid Workspace name, not exceeding 32 characters, adhering to the regex pattern: [a-z]([-a-z0-9]*[a-z0-9])? |

**Example Usage:**

```yaml
name: myworkspace
```

---

### **`description`**

**Description:** The `description` attribute is used to provide a description for a Workspace.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | valid string |

**Example Usage:**

```yaml
description: "This is a description of my workspace."
```

---

### **`tags`**

**Description:** The `tags` attribute is used to specify tags associated with a specific-Workspace.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list of strings | optional | none | valid string |

**Additional Details:** Certain tags like `dataos:type:workspace:**`, `dataos:layer:**`, `dataos:workspace:**` are assigned by the DataOS itself for internal discoverability purposes. You can get the list of tags on the DataOS CLI using the following command:

```yaml
dataos-ctl workspace get

# Expected Sample Output

  NAME       │ LAYER │        OWNER   │          DESCRIPTION   │                TAGS                │ STATUS  
─────────────┼───────┼────────────────┼────────────────────────┼────────────────────────────────────┼─────────
public       │ user  │ dataos-manager │ the default user layer │ workspace, user, public,           │ active  
             │       │                │ workspace              │ dataos:type:workspace:default,     │         
             │       │                │                        │ dataos:type:workspace,             │         
             │       │                │                        │ dataos:layer:user,                 │         
             │       │                │                        │ dataos:workspace:public            │         
sandbox      │ user  │ dataos-manager │ the default user layer │ workspace, user,                   │ active  
             │       │                │ development and testing│ sandbox, dev, test,                │         
             │       │                │ workspa                │ dataos:type:workspace:default,     │         
             │       │                │                        │ dataos:type:workspace,             │         
             │       │                │                        │ dataos:layer:user,                 │         
             │       │                │                        │ dataos:workspace:sandbox           │         
bundletesting│ user  │ iamgroot       │ This workspace is for  │ bundletesting, dataproducts,       │ active  
             │       │                │ dataos bundle resource │ dataos:type:workspace:not-default, │         
             │       │                │ testing                │ dataos:type:workspace,             │         
             │       │                │                        │ dataos:layer:user,                 │         
             │       │                │                        │ dataos:workspace:bundletesting     │
```

**Example Usage:**

```yaml
tags:
  - bundletesting
  - dataproducts
```

---

### **`labels`**

**Description:** The `labels` attribute is used to specify key-value labels associated with a Workspace.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | optional | none | none |

**Example Usage:**

```yaml
labels:
  key1: "value1"
  key2: "value2"
```

---

### **`layer`**

**Description:** The `layer` attribute is used to specify the layer within the User Space where the Bundle Resource belongs.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | user/system |

**Example Usage:**

```yaml
layer: user
```

---

### **`resources`**

**Description:** The Bundle Resources section or the `resources` attribute specifies a list of Resource configurations within the Bundle definition.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list of mappings | mandatory | none | none |

**Example Usage:**

```yaml
resources:
  - name: create-icebase-depot
    file: depot.yaml
  - name: write-into-icebase
    dependencies:
      - create-icebase-depot
    workspace: testbundle14
    file: read_icebase_write_snowflake.yaml
```

---

### **`id`**

**Description:** The `id` attribute is used to specify the unique identifier of a Resource within the Bundle definition. This identifier is used to create dependencies between different resources within the Bundle.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | mandatory | none | valid string |

**Example Usage:**

```yaml
id: myresource
```

---

### **`workspace`**

**Description:** The `workspace` attribute is used to specify the name of the workspace associated with a Workspace-level Resource within the Bundle definition.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | optional (mandatory for Workspace-level Resources) | none | valid Workspace name, not exceeding 32 characters, adhering to the regex pattern: [a-z]([-a-z0-9]*[a-z0-9])? |

**Additional Information:** A Bundle can reference Resources located in other Workspaces, which may not be created using the Bundle itself, for the creation of a Workspace-level Resource. For instance, a Workspace named `myworkspace` might be created using the Bundle, but when specifying a Workflow within the Bundle Workspace, Resources can also be created in a different Workspace, like a `testingspace`, provided there is access to that Workspace. Absence of access rights could prevent such operations.

**Example Usage:**

```yaml
workspace: myworkspace
```

---

### **`dependencies`**

**Description:** The `dependencies` attribute is used to specify a list of Resources referred by their resource `id` on which the current resource depends within the Directed Acyclic Graph (DAG) of resources.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| list of strings | optional | none | Resource ids within the DAG except the current one |

**Example Usage:**

```yaml
dependencies:
  - scanner
```

---

### **`dependencyConditions`**

**Description:** The `dependencyConditions` attribute is a mapping that configures dependency conditions based on status and runtime. By default, if `dependencyConditions` are not specified but a `dependency` is indicated on some Resource, the default condition assumes the status is active.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| list of mappings | optional | dependencyConditions:
  - resourceId: {{dependent resource}}
    status:
      is:
        - active | none |

**Example Usage:**

```yaml
dependencyConditions:
  - resourceId: scanner
    status:
      is:
        - active
    runtime:
      is:
        - succeeded
```

---

### **`resourceId`**

**Description:** The `resourceId` attribute designates the unique identifier of a Resource that a given Resource is dependent on. This identifier plays a critical role in establishing dependencies among various resources within the Bundle.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | mandatory | none | Valid ID of a Resource specified within the Bundle on which this Resource is dependent |

**Example Usage:**

```yaml
resourceId: myresource
```

---

### **`status`**

**Description:** The `status` attribute is used to specify the expected status of a Resource within the Bundle. The status can be evaluated using two different operators: `is` and `contains`.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| mapping | optional | none | none |

**Example Usage:**

```yaml
status:
	is:
		- active
```

### **`status`**

**Description:** The `status` attribute is employed to define the anticipated status of a Resource within the Bundle. This attribute facilitates the assessment of a Resource's operational condition based on predefined criteria. It utilizes two distinct operators for evaluation: `is` and `contains`. The `is` operator is used to specify an exact match of the Resource's status, while the `contains` operator allows for a more flexible match, indicating that the Resource's status includes one or more specified conditions.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| mapping | optional | none | none |

**Additional Details:**

- The `is` operator is precise and checks for an exact status. If the status of the Resource exactly matches one of the values listed, the condition is considered met.
- The `contains` operator is used when the status may include multiple conditions or a broader state. It checks if the Resource's status includes any of the specified conditions.
- This attribute is critical in scenarios where the execution or activation of a Resource depends on the state of another Resource. It ensures that dependencies are correctly managed and that Resources are activated or processed in the correct order and state.

**Example Usage:**

```yaml
status:
  is:
    - active
  contains:
    - error
    - warning
```

In this example, the `status` attribute is configured to meet conditions where the Resource is exactly `active` or contains either `error` or `warning` in its status. 

---

### **`is`**

**Description:** The `is` attribute is used to specify an exact match condition within a parent attribute structure. It is typically employed to define a precise state or value that a resource or property must match exactly for a condition to be considered true.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| list of strings | mandatory | none | A set of exact values relevant to the context in which the is attribute is used |

**Example Usage:**

```yaml
is:
  - active
```

In this usage, the `is` attribute lists specific states ('active', 'completed'), and the condition is met only if the resource or property matches one of these exact states.

---

### **`contains`**

**Description:** The `contains` attribute is used to specify a condition where the presence of one or more values within a larger set satisfies the requirement. Unlike `is`, which demands an exact match, `contains` is used for more flexible matching, allowing for partial or subset matches within a broader context.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| list of strings | mandatory | none | A range of values or substrings that are permissible within the context where the contains attribute is applied |

**Example Usage:**

```yaml
contains:
  - error
  - pending
```

In this example, the `contains` attribute lists conditions ('error', 'warning') that, if present in any part of the larger set or string, would satisfy the condition. This allows for a broader and more inclusive matching criterion.

---

### **`runtime`**

**Description:** The `runtime` attribute specifies the execution state or duration of a Resource within the Bundle. It typically indicates the operational phase of the Resource, such as whether it is currently running, completed, or has encountered an error during execution.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string or time duration format | optional | none | Predefined runtime states like running, succeeded, failed, or specific time durations. |

**Example Usage:**

```yaml
runtime: succeeded
```

---

### **`spec`**

**Description:** The `spec` attribute enables in-line definition of specification or configuration for a Resource within the Bundle. It is particularly useful for defining configurations that are concise or specific to a single Bundle, avoiding the need for external files.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| mapping | optional (either spec or file should be provided) | none | valid Resource spec |

**Example Usage:**

```yaml
# Spec of a Snowflake Depot
spec:
  name: abcd
  version: v1
  type: depot
  tags: 
    - snowflake
    - depot
  description: this is a snowflake depot
  layer: user
  depot: 
    type: snowflake
    description: this is not a snowflake depot
    connectionSecret: 
      - acl: rw
        type: key-value-properties
        data: 
          username: iamgroot
          password: ironman
    external: true
    spec: 
      warehouse: random_warehouse
      url: https://abcdefgh.west-usa.azure.snowflakecomputing.com
      database: mydatabase
```

<aside>
🗣 A data developer has the option to either define the complete Resource manifest directly within the `spec` attribute or alternatively, construct a separate file and reference its path using the `file` attribute. This provides flexibility in how Resource configurations are managed and maintained within the Bundle.

</aside>

---

### **`file`**

**Description:** The `file` attribute specifies the path to the Resource specification file associated with the Resource. When a Resource is applied or linted, the contents of the file indicated in the `file` attribute are interpolated within the `spec` attribute. This allows for external configuration of Resource specifications, enabling more dynamic and modular resource management.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | optional (either spec or file should be provided) | none | valid Resource config file path |

**Example Usage:**

```yaml
file: "/path/to/resource/manifest.yaml"
```

---

### **`properties`**

**Description:** The `properties` attribute is used to specify additional properties associated with a resource within the Bundle definition.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | optional | none | properties in the form of key-value pairs |

**Example Usage:**

```yaml
properties:
	alpha: beta
```