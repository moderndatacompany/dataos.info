# Data Product Configurations

The following attributes are declared for every Data Product deployed in a DataOS context. Some of these attributes/fields need to be mandatorily declared, while others are optional.

## Structure of Data Product manifest file

```yaml
# product meta section

name: ${{product-affinity-cross-sell}} # mandatory
version: ${{v1beta}} # mandatory
entity: ${{product}} # mandatory
type: ${{data}} # mandatory
tags:   # optional
  - ${{DPDomain.Sales}}
  - ${{DPDomain.Marketing}}
  - ${{DPUsecase.Customer Segmentation}}
  - ${{DPUsecase.Product Recommendation}}
  - ${{DPTier.DataCOE Approved}}
description: ${{Leverages product affinity analysis to identify cross-sell opportunities, enabling businesses to enhance customer recommendations and drive additional sales by understanding the relationships between products purchased together}} # optional
refs:  # optional
  - title: ${{Workspace Info}} # optional
    href: ${{https://dataos.info/interfaces/cli/command_reference/#workspace}} # mandatory

# data product specific section

v1beta: # mandatory
  data: # mandatory
    meta: # mandatory
      title: ${{Product Affinity & Cross-Sell Opportunity}}
      sourceCodeUrl: ${{https://bitbucket.org/tmdc/product-affinity-cross-sell/src/main/}}
      trackerUrl: ${{https://rubikai.atlassian.net/browse/DPRB-65}}
 
    collaborators: # optional
      - name: ${{iamgroot}}
        description: ${{developer}}
      - name: ${{iamthor}}
        description: ${{consumer}}

    resource: # mandatory
      refType: ${{dataos}}
      ref: ${{bundle:v1beta:product-affinity-bundle}}

    inputs: # mandatory
      - refType: ${{dataos}}
        ref: ${{dataset:icebase:customer_relationship_management:customer}}

      - refType: ${{dataos}}
        ref: ${{dataset:icebase:customer_relationship_management:purchase}}

      - refType: ${{dataos}}
        ref: ${{dataset:icebase:customer_relationship_management:product}}

    outputs: # optional
      - refType: ${{dataos}}
        ref: ${{dataset:icebase:customer_relationship_management:product_affinity_matrix}}

      - refType: ${{dataos}}
        ref: ${{dataset:icebase:customer_relationship_management:cross_sell_recommendations}}

    ports: # optional
      lens:
        ref: ${{lens:v1alpha:cross-sell-affinity:public}}
        refType: ${{dataos}}

      talos:
        - ref: ${{service:v1:cross-sell-talos:public}}
          refType: ${{dataos}}
            
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
name: product-affinity-cross-sell
```

### **`version`**

**Description:** The version of the Product manifest file

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | v1alpha |

**Example Usage:**

```yaml
version: v1beta
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
  - DPDomain.Sales
  - DPDomain.Marketing
  - DPUsecase.Customer Segmentation
  - DPUsecase.Product Recommendation
  - DPTier.DataCOE Approved
```
Following are the predefined tags which you can customize as per the specific Data Product.

| Tags | Description |
| --- | --- |
| `DPDomain.Sales` | Refers to Data Products related to the sales domain, focusing on sales data and analytics. similarly you can assign any related doamin to the Data Product. |
| `DPDomain.Marketing` | Pertains to Data Products in the marketing domain, emphasizing customer outreach and campaigns. |
| `DPUsecase.Customer Segmentation` | Assigns the customer segmentation use case. |
| `DPUsecase.Product Recommendation` |  Assigns the product recommendation use case.  |
| `DPTier.DataCOE Approved` | Assigns the tier to the Data Product. Indicates that the Data Product meets standards set by the Data Center of Excellence. |


### **`description`**

**Description:** A brief description of the product.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | any string |

**Example Usage:**

```yaml
description: Leverages product affinity analysis to identify cross-sell opportunities, enabling businesses to enhance customer recommendations and drive additional sales by understanding the relationships between products purchased together # optional
```

### **`collaborators`**

**Description:** Optional field listing collaborators involved in developing or maintaining the product.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list of strings | optional | none | list of objects, includes the name and the description of the collaborator |

**Example Usage:**

```yaml
collaborators: # optional
  - name: iamgroot
    description: developer
  - name: iamthor
    description: consumer
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

Data Product-specific section is different for different versions. This section comprises attributes specific to the Data Product for each version. The attributes within the section are listed below:

### **`v1beta`**

**Description:** The `v1alpha` mapping comprises attributes for configuring a Data Product in DataOS.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | mandatory | none | none |

**Example Usage:**

```yaml
v1beta: # mandatory
  data: # mandatory
    meta: # mandatory
      title: Product Affinity & Cross-Sell Opportunity
      sourceCodeUrl: https://bitbucket.org/tmdc/product-affinity-cross-sell/src/main/
      trackerUrl: https://rubikai.atlassian.net/browse/DPRB-65
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

#### **`meta`**

**Description:** Represents the essential metadata associated with the Data Product, providing details like the title, source code location, and issue tracking.

| Attribute | Description | Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- | --- | --- |
| **title** | The name of the Data Product, indicating its purpose and focus. | String | Mandatory | None | Any descriptive title of the Data Product |
| **sourceCodeUrl** | URL to the source code repository for the Data Product, enabling code access. | URL | Mandatory | None | URL pointing to the source code location |
| **trackerUrl** | URL to the issue tracker, allowing team members to view and report issues related to the Data Product. | URL | Mandatory | None | URL pointing to the tracking system (e.g., Jira) |

#### **`resources`**

**Description:** Represents the resource mappings associated with the Data Product.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list of mappings | mandatory | none | none |

**Example Usage:**

```yaml
resource: # mandatory
  refType: dataos
  ref: bundle:v1beta:product-affinity-bundle
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

#### **`ref`**

**Description:** The bundle reference, specifying the version and name of the bundle associated with the Data Product.

| Attribute | Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- | --- | --- |
| **ref** | String | Mandatory | None | `bundle:v1beta:product-affinity-bundle` or similar format |


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
| list of strings | optional | none | • alpha numeric values with the RegEx[a-z0-9][-a-z0-9]*[a-z0-9]; a hyphen/dash is allowed as a special character
• total length of the string should be less than or equal to 48 characters |

**Example Usage:**

```yaml
usecases:    
  - c360-dataset
  - check-usecase-01
  - check-usecase-02 
```

### **`v1beta`**

**Description:** Specifies the version of the Data Product.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | v1beta |

**Example Usage:**

```yaml
v1beta:
  data: # Data Product version details
    meta:
      foo: bar
```

#### **`data`**

**Description:** Contains additional sections related to the Data Product.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| object | mandatory | none | Contains `meta`, `collaborators`, `relatedDataProducts`, `resource`, `inputs`, `outputs`, `ports`, and `metrics`. |

**Example Usage:**

```yaml
data:
  meta:
    foo: bar
```

#### **`meta`**

**Description:** An optional section for additional metadata.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| object | optional | none | Contains key-value pairs for metadata. |

**Example Usage:**

```yaml
meta:
  foo: bar
```

#### **`collaborators`**

**Description:** Specifies the list of collaborators involved with the Data Product.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list of objects | mandatory | none | Each object contains `name` and `description`. |

**Example Usage:**

```yaml
collaborators:
  - name: ${{iamgroot}}
    description: ${{owner}}
  - name: ${{itsthor}}
    description: ${{developer}}
  - name: ${{itsloki}}
    description: ${{consumer}}
```

#### **`name`**

**Description:** The name of the collaborator.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | Any valid string representing the collaborator's identity. |

**Example Usage:**

```yaml
name: ${{iamgroot}}
```

#### **`description`**

**Description:** A brief description of the collaborator's role.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | Example roles include owner, developer, consumer. |

**Example Usage:**

```yaml
description: ${{owner}}
```

#### **`relatedDataProducts`**

**Description:** Lists related Data Products connected or associated with the current Data Product.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list of strings | optional | none | Each string references another Data Product by specifying the version and name. |

**Example Usage:**

```yaml
relatedDataProducts:
  - ${{data:v1beta:customer-360-demov3}}
```

#### **`resource`**

**Description:** Defines the resources utilized by the Data Product.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| object | mandatory | none | Contains fields like `description`, `purpose`, `refType`, and `ref`. |

**Example Usage:**

```yaml
resource:
  description: ${{'Ingest data'}}
  purpose: ${{'ingestion'}}
  refType: ${{dataos}}
  ref: ${{bundle:v1beta:sales-data-pipeline}}
```

#### **`description (resource)`**

**Description:** A brief description of the resource.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | Any string describing the resource. |

**Example Usage:**

```yaml
description: ${{'Ingest data'}}
```

#### **`purpose (resource)`**

**Description:** The purpose of the resource.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | Possible values include specific purposes like `ingestion`. |

**Example Usage:**

```yaml
purpose: ${{'ingestion'}}
```

#### **`refType`**

**Description:** The reference type of the resource.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | Example: `dataos`. |

**Example Usage:**

```yaml
refType: ${{dataos}}
```

#### **`ref`**

**Description:** The reference of the resource.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | Example: `bundle:v1beta:sales-data-pipeline`. |

**Example Usage:**

```yaml
ref: ${{bundle:v1beta:sales-data-pipeline}}
```

#### **`inputs`**

**Description:** Lists the input data sources required by the Data Product.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list of objects | mandatory | none | Each object describes an input with fields like `description`, `purpose`, `refType`, and `ref`. |

**Example Usage:**

```yaml
inputs: # mandatory
  - refType: dataos
    ref: dataset:icebase:customer_relationship_management:customer

  - refType: dataos
    ref: dataset:icebase:customer_relationship_management:purchase

  - refType: dataos
    ref: dataset:icebase:customer_relationship_management:product
```

#### **`outputs`**

**Description:** Specifies the output data generated by the Data Product.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list of objects | mandatory | none | Each object details an output with fields like `description`, `purpose`, `refType`, `ref`, and optional `checks`. |

**Example Usage:**

```yaml
outputs: # optional
  - refType: dataos
    ref: dataset:icebase:customer_relationship_management:product_affinity_matrix

  - refType: dataos
    ref: dataset:icebase:customer_relationship_management:cross_sell_recommendations
```

#### **`ports`**

**Description:** Defines the ports for accessing the Data Product through various services.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| object | mandatory | none | Contains `lens`, `talos`, `rest`, and `postgres` sections for different types of ports. |

**Example Usage:**

```yaml
ports:
  lens:
    ref: ${{lens:v1alpha:sales360:public}}
    refType: ${{dataos}}

  talos:
    - ref: ${{service:v1:sales360-talos:public}}
      refType: ${{dataos}}

```

