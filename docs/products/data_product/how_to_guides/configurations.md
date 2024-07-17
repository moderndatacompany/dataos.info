# Data Product manifest file configuration

The following attributes are declared for every Data Product deployed in a DataOS context. Some of these attributes/fields need to be mandatorily declared, while others are optional.

## Structure of Data Product manifest file

```yaml
# Product meta section
name: {{dp-test}} # Product name (mandatory)
version: {{v1alpha}} # Manifest version (mandatory)
type: {{data}} # Product-type (mandatory)
tags: # Tags (Optional)
  - {{data-product}}
  - {{dataos:type:product}}
  - {{dataos:product:data}}
description: {{the customer 360 view of the world}} # Descripton of the product (Optional)
Purpose: {{This data product is intended to provide insights into the customer for strategic decisions on cross-selling additional products.}} # purpose (Optional)
collaborators: # collaborators User ID (Optional)
  - {{thor}}
  - {{blackwidow}}
  - {{loki}}
owner: {{iamgroot}} # Owner (Optional)
refs: # Reference (Optional)
  - title: {{Data Product Hub}} # Reference title (Mandatory if adding reference)
    href: {{https://liberal-donkey.dataos.app/dph/data-products/all}} # Reference link (Mandatory if adding reference)
entity: {{product}} # Entity (Mandatory)
# Data Product-specific section (Mandatory)
v1alpha: # Data Product version
  data:
    resources: # Resource specific section(Mandatory)
      - name: {{bundle-dp}} # Resource name (Mandatory)
        type: {{bundle}} # Resource type (Mandatory)
        version: {{v1beta}} # Resource version (Mandatory)
        refType: {{dataos}} # Resource reference type (Mandatory)
        workspace: {{public}} # Workspace (Requirement depends on the resource type)
        description: {{this bundle resource is for a data product}} # Resource description (Optional)
        purpose: {{deployment of data product resources}} # Purpose of the required resource (Optional)   
    
    inputs:
      - description: S3 Depot
        purpose: source
        refType: dataos
        ref: dataos://s3depot:none/ga_data/
    
    outputs:
      - description: Icebase Depot
        purpose: consumption
        refType: dataos_address
        ref: dataos://icebase:google_analytics/ga_sessions_daily_data_raw    
```
To know more about the Product meta section, [refer to this](/products/data_product/configurations/).

Following are the details of each attributes  of Product specific section:

**`v1alpha`**

**Description:** The `v1alpha` mapping comprises attributes for configuring a Data Product in DataOS.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | mandatory | none | none |

**Example Usage:**

```yaml
v1alpha:
  data:
    resources:
      - name: sales360test
        type: lens 
        ...
```

**`data`**

**Description:** The `data` attribute is a mapping that comprises attributes for configuring a Data Product in DataOS, including resources, input, output, etc.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | mandatory | none | none |

**Example Usage:**

```yaml
data:
  resources:
    - name: sales360test
      type: lens 
      ...
```

### **Resource section configurations**

**`resources`**

**Description:** Represents the resource mappings associated with the data product.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list of mappings | mandatory | none | none |

**Example Usage:**

```yaml
resources: 
  - name: sales360test 
    type: lens 
    version: v1alpha 
    refType: dataos
    workspace: public 
    description: Ingest lens Data 
    purpose: ingestion of data 
```

**`description`**

**Description:** Describes the resource.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | any valid string |

**Example Usage:**

```yaml
description: Ingest lens Data 
```

**`purpose`**

**Description:** Indicates the purpose of the resource.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | any valid string |

**Example Usage:**

```yaml
purpose: ingestion of data 
```

**`type`**

**Description:** Indicates the type of resource.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | worker, workflow, service, depot, cluster, bundle, policy, stack, database, compute, secret, instance secret, monitor, lakehouse, operator, and pager |

**Example Usage:**

```yaml
type: workflow
```

**`version`**

**Description:** Represents the version of the resource.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | v1, v1alpha, v2alpha, v1beta |

**Additional information:** The below table shows the information on the version and workspace of each resource.

| Resource Type | Versions | Workspace |
| --- | --- | --- |
| bundle | v1beta |  |
| cluster | v1 | ✅ |
| compute | v1beta |  |
| database | v1 | ✅ |
| depot | v1,v2alpha |  |
| instance-secret | v1 |  |
| lakehouse | v1alpha | ✅ |
| monitor | v1alpha | ✅ |
| operator | v1alpha |  |
| pager | v1alpha | ✅ |
| policy | v1 |  |
| resource | v1beta | ✅ |
| secret | v1 | ✅ |
| service | v1 | ✅ |
| stack | v1alpha |  |
| worker | v1beta | ✅ |
| workflow | v1 | ✅ |

**Example Usage:**

```yaml
version: v1alpha
```

**`refType`**

**Description:** Represents the resource address or location.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | dataos, dataos_address |

**Example Usage:**

```yaml
refType: dataos
```

**`name`**

**Description:** Represents the unique identifier of the resource.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | any valid string |

**Example Usage:**

```yaml
name: sales360test
```

**`workspace`**

**Description:** Represents the workspace where the resource is located or managed.

<aside class="callout">
  🗣 Workspace is required and mandatory only for <a href="https://www.notion.so/Attributes-of-Data-Product-Specific-Section-30ea9e9fd5c844e49ec874483eb89570?pvs=21">workspace-level resources</a>.
</aside>


| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | workspace specific to the referred resource  |

**Example Usage:**

```yaml
workspace: public 
```

### **Input section configurations**

**`inputs`**

**Description:** Represents the input mappings.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list of mappings | mandatory | none | none |

<aside class="callout">
🗣 As you can add multiple inputs and outputs, make sure to add all the input and output data sources as different resources may incorporate different input and output sources.

</aside>

**Example Usage:**

```yaml
inputs: 
  - refType: dataos
    ref: dataos://icebase:retail/customer  
    description: Customer 
    purpose: source 
```

**`description`**

**Description:** Describes the input data.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | any valid string |

**Example Usage:**

```yaml
description: Customer 
```

**`purpose`**

**Description:** Indicates the purpose of the input.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | aone | any valid string |

**Example Usage:**

```yaml
 purpose: source 
```

**`refType`**

**Description:** Represents the reference type of the input.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | None | dataos, dataos_address |

**Example Usage:**

```yaml
refType: dataos
```

**`ref`**

**Description:** Represents the reference address of the input.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | input data reference address |

**Example Usage:**

```yaml
ref: dataos://icebase:retail/customer  
```

### **Output section configurations**

**`outputs`**

**Description:** Represents the input object.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list of mappings | mandatory | none | none |

**Example Usage:**

```yaml
    outputs: 
      - refType: dataos_address
        ref: dataos://icebase:retail/customer
        description: Customer 360 
        purpose: consumption
```

**`description`**

**Description:** Describes the input data.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | None | Any valid string |

**Example Usage:**

```yaml
description: Customer 360 
```

**`purpose`**

**Description:** Indicates the purpose of the input.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | None | Any valid string |

**Example Usage:**

```yaml
purpose: consumption
```

**`refType`**

**Description:** Represents the reference type of the input.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | None | dataos, dataos_address |

**Example Usage:**

```yaml
refType: dataos_address
```

**`ref`**

**Description:** Represents the reference address of the input.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | None | Reference address |

**Example Usage:**

```yaml
ref: dataos://icebase:retail/customer
```

**Usecases section**

**`useCases`**

**Description:** Lists the use cases associated with the data product.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list of strings | optional | none | • alpha numeric values with the RegEx[a-z0-9]([-a-z0-9]*[a-z0-9]); a hyphen/dash is allowed as a special character<br>• total length of the string should be less than or equal to 48 characters |

**Example Usage:**

```yaml
usecases:    
  - c360-dataset
  - check-usecase-01
  - check-usecase-02 
```