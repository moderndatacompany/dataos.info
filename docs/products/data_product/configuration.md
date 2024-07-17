# Data Product Configurations

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
- title: {{Bundle Info}} # Reference title (Mandatory if adding reference)
    href: {{https://dataos.info/resources/bundle/}} # Reference link (Mandatory if adding reference)
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
    
    inputs: # Input specific section (Mandatory)
      - description: Sales 360
        purpose: source
        refType: dataos
        ref: dataos://bigquery:PUBLIC/MYTABLE
    
    outputs: # Output specific section (Mandatory)
      - description: Customer
        purpose: consumption
        refType: dataos_address
        ref: dataos://icebase:sandbox/sales?acl=rw  
```        


## **Product meta section**

This section serves as the header of the manifest file, defining the overall characteristics of the Data Product you wish to create. It includes attributes common to all types of Products in DataOS. 

### **`name`**


**Description:** Unique identifier for the Product.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | • alpha numeric values with the RegEx `[a-z0-9]([-a-z0-9]*[a-z0-9])`; a hyphen/dash is allowed as a special character<br>• total length of the string should be less than or equal to 48 characters |

**Example Usage:**

```yaml
name: test-data-product
```

### **`version`**

**Description:** The version of the Product manifest file

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | v1alpha |

**Example Usage:**

```yaml
version: v1alpha
```

**`entity`**

**Description:** Indicates the DataOS Entity to which the attributes apply, specified as "product".

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | product, resource, workspace, domain |

**Example Usage:**

```yaml
entity: product
```

### **`type`**

**Description:** Indicates the type of product.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | data |

**Example Usage:**

```yaml
type: data
```

### **`tags`**

**Description:** Tags associated with the product.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list of strings | optional | none | list of strings |

**Example Usage:**

```yaml
tags: 
  - data-product
  - dataos:type:product
  - dataos:product:data
```

There are also some pre-defined tags that can help users to manage their Data Products effectively.

**`Readiness.Ready to use`:** This tag defines the readiness of the Data Product, if the Data Product is ready to use then `Readiness.Ready to use` tag is required if you want users to use your Data Product as template `Readiness.Template` tag is required, this is completely optional but it is recommended to define the readiness of your Data Product so that business users can easily identify the Data Product.

**`Type.3rd Party Data Product`:** This tag defines the type of the Data Product based on its data source, if the Data Product is incorporating data source outside of the organization then `Type.3rd Party Data Product` tag is required and if the Data Product incorporates data source inside of the organization then `Type.Internal Data Product` is required. This is completely optional but it is recommended to define the type of your Data Product so that business users can easily identify the Data Product.

**`Domain.Customer Service`** tag is needed, The following are the pre-existing domains of the Data Product:

- Customer Service
- Executive Reporting
- Finance
- Marketing
- Quality
- Sales
- Supply Chain

<aside class="callout">
🗣 Note that on Data Product Hub, the user can filter out the Data Products based on their readiness, type, and usecases.

</aside>

### **`description`**

**Description:** A brief description of the product.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | any string |

**Example Usage:**

```yaml
description: the customer 360 view of the world
```

### **`purpose`**

**Description:** Further elaboration on the purpose of the data product.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | any string |

**Example Usage:**

```yaml
purpose: The purpose of the data product is to provide comprehensive insights into the creditworthiness of companies. By leveraging various data points such as company contact information, credit score, company details, financial data, and industrial data, this product aims to assist users in making informed decisions related to credit risk assessment, investment opportunities, and business partnerships.
```

### **`collaborators`**

**Description:** Optional field listing collaborators involved in developing or maintaining the product.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list of strings | optional | none | list of strings, string must be an valid user-id |

**Example Usage:**

```yaml
collaborators:
  - thor
  - blackwidow
  - loki 
```

**`owner`**

 **Description:** The owner of the Product.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | valid user-id |

**Example Usage:**

```yaml
owner: iamgroot
```

**`refs`**

 **Description:** References associated with the product that can provide the additional information about it.
 
| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list of mappings | optional | none | mappings containing title and href address |

**Example Usage:**

```yaml
refs:
  - title: Lens Info 
    href: https://dataos.info/interfaces/lens/
```




## **Data Product-specific section**

This section comprises attributes specific to the Data Product. The attributes within the section are listed below:

#### **`v1alpha`**

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

#### **`data`**

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

#### **`resources`**

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

#### **`description`**

**Description:** Describes the resource.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | any valid string |

**Example Usage:**

```yaml
description: Ingest lens Data 
```

#### **`purpose`**

**Description:** Indicates the purpose of the resource.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | any valid string |

**Example Usage:**

```yaml
purpose: ingestion of data 
```

#### **`type`**

**Description:** Indicates the type of resource.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | worker, workflow, service, depot, cluster, bundle, policy, stack, database, compute, secret, instance secret, monitor, lakehouse, operator, and pager |

**Example Usage:**

```yaml
type: workflow
```

#### **`version`**

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

#### **`refType`**

**Description:** Represents the resource address or location.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | dataos, dataos_address |

**Example Usage:**

```yaml
refType: dataos
```

#### **`name`**

**Description:** Represents the unique identifier of the resource.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | any valid string |

**Example Usage:**

```yaml
name: sales360test
```

#### **`workspace`**

**Description:** Represents the workspace where the resource is located or managed.

<aside class="callout">
🗣 Workspace is required and mandatory only for <a href="/resources/index">workspace-level resources</a>.
</aside>

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | workspace specific to the referred resource  |

**Example Usage:**

```yaml
workspace: public 
```

### Input section configurations

#### **`inputs`**

**Description:** Represents the input mappings.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list of mappings | mandatory | none | none |


**Example Usage:**

```yaml
inputs: 
  - refType: dataos
    ref: dataos://icebase:retail/customer  
    description: Customer 
    purpose: source 
```

#### **`description`**

**Description:** Describes the input data.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | any valid string |

**Example Usage:**

```yaml
description: Customer 
```

#### **`purpose`**

**Description:** Indicates the purpose of the input.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | aone | any valid string |

**Example Usage:**

```yaml
 purpose: source 
```

#### **`refType`**

**Description:** Represents the reference type of the input.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | None | dataos, dataos_address |

**Example Usage:**

```yaml
refType: dataos
```

#### **`ref`**

**Description:** Represents the reference address of the input.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | input data reference address |

**Example Usage:**

```yaml
ref: dataos://icebase:retail/customer  
```

### Output section configurations

#### **`outputs`**

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

#### **`description`**

**Description:** Describes the input data.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | None | Any valid string |

**Example Usage:**

```yaml
description: Customer 360 
```

#### **`purpose`**

**Description:** Indicates the purpose of the input.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | None | Any valid string |

**Example Usage:**

```yaml
purpose: consumption
```

#### **`refType`**

**Description:** Represents the reference type of the input.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | None | dataos, dataos_address |

**Example Usage:**

```yaml
refType: dataos_address
```

#### **`ref`**

**Description:** Represents the reference address of the input.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | None | Reference address |

**Example Usage:**

```yaml
ref: dataos://icebase:retail/customer
```

**Usecases section**

#### **`useCases`**

**Description:** Lists the use cases associated with the data product.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list of strings | optional | none | • alpha numeric values with the RegEx[a-z0-9]([-a-z0-9]*[a-z0-9]); a hyphen/dash is allowed as a special character
• total length of the string should be less than or equal to 48 characters |

**Example Usage:**

```yaml
usecases:    
  - c360-dataset
  - check-usecase-01
  - check-usecase-02 
```