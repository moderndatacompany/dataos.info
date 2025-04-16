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
      description: ${{'Ingest data'}}
      purpose: ${{'ingestion'}}

    inputs: # mandatory
      - refType: ${{dataos}}
        ref: ${{dataset:icebase:customer_relationship_management:customer}}
        description: ${{'Ingest data'}}
        purpose: ${{'ingestion'}}

      - refType: ${{dataos}}
        ref: ${{dataset:icebase:customer_relationship_management:purchase}}
        description: ${{'Ingest data'}}
        purpose: ${{'ingestion'}}

      - refType: ${{dataos}}
        ref: ${{dataset:icebase:customer_relationship_management:product}}
        description: ${{'Ingest data'}}
        purpose: ${{'ingestion'}}

    outputs: # optional
      - refType: ${{dataos}}
        ref: ${{dataset:icebase:customer_relationship_management:product_affinity_matrix}}
        description: ${{'Ingest data'}}
        purpose: ${{'ingestion'}}

      - refType: ${{dataos}}
        ref: ${{dataset:icebase:customer_relationship_management:cross_sell_recommendations}}
        description: ${{'Ingest data'}}
        purpose: ${{'ingestion'}}

    ports: # optional
      lens:
        ref: ${{lens:v1alpha:cross-sell-affinity:public}}
        refType: ${{dataos}}

      talos:
        - ref: ${{service:v1:cross-sell-talos:public}}
          refType: ${{dataos}}
            
```



## Product meta section

This section serves as the header of the manifest file, defining the overall characteristics of the Data Product you wish to create. It includes attributes common to all types of Products in DataOS. 

### **`name`**


**Description:** Unique identifier for the Product.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | • alpha numeric values with the RegEx `[a-z0-9]([-a-z0-9]*[a-z0-9])`; a hyphen/dash is allowed as a special character<br>• total length of the string should be less than or equal to 48 characters |

**Example usage:**

```yaml
name: product-affinity-cross-sell
```

<center>
  <img src="/products/data_product/configurations/metis_title.png" alt="DPH" style="width:40rem; border: 1px solid black;" />
  <figcaption><i>Data Product card showing the title on Metis</i></figcaption>
</center>

### **`version`**

**Description:** The version of the Product.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | v1alpha |

**Example usage:**

```yaml
version: v1beta
```

**`entity`**

**Description:** Indicates the DataOS entity to which the attributes apply, specified as "product".

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | product, resource, workspace, domain |

**Example usage:**

```yaml
entity: product
```

### **`type`**

**Description:** Indicates the type of product.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | data |

**Example usage:**

```yaml
type: data
```

### **`tags`**

**Description:** Tags associated with the product.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list of strings | optional | none | list of strings |

**Example usage:**

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

<center>
  <img src="/products/data_product/configurations/dp_tags.png" alt="DPH" style="width:40rem; border: 1px solid black;" />
  <figcaption><i>Data Product card showing the tags on Data Product Hub</i></figcaption>
</center>

<center>
  <img src="/products/data_product/configurations/metis_tags.png" alt="DPH" style="width:40rem; border: 1px solid black;" />
  <figcaption><i>Data Product card showing the tags on Metis</i></figcaption>
</center>


### **`description`**

**Description:** A brief description of the Product.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | any string |

**Example usage:**

```yaml
description: Leverages product affinity analysis to identify cross-sell opportunities, enabling businesses to enhance customer recommendations and drive additional sales by understanding the relationships between products purchased together # optional
```
<center>
  <img src="/products/data_product/configurations/dp_description.png" alt="DPH" style="width:40rem; border: 1px solid black;" />
  <figcaption><i>Data Product card showing the description on Data Product Hub</i></figcaption>
</center>

<center>
  <img src="/products/data_product/configurations/metis_description.png" alt="DPH" style="width:40rem; border: 1px solid black;" />
  <figcaption><i>Data Product card showing the description on Metis</i></figcaption>
</center>

**`owner`**

 **Description:** The owner of the Product.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | valid user-id |

**Example usage:**

```yaml
owner: iamgroot
```

**`refs`**

 **Description:** References associated with the Product that can provide the additional information about it.
 
| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list of mappings | optional | none | mappings containing title and href address |

**Example usage:**

```yaml
refs:
  - title: Lens Info 
    href: https://dataos.info/interfaces/lens/
```

<center>
  <img src="/products/data_product/configurations/metis_refer.png" alt="DPH" style="width:40rem; border: 1px solid black;" />
  <figcaption><i>Data Product card showing the reference links on Metis</i></figcaption>
</center>


## Data Product-specific section

Data Product-specific section is different for different versions. This section comprises attributes specific to the Data Product for each version. The attributes within the section are listed below:


### **`v1beta`**

**Description:** Specifies the version of the Data Product.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | v1beta |

**Example usage:**

```yaml
v1beta:
  data: # Data Product version details
```

### **`data`**

**Description:** Contains additional sections related to the Data Product.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| object | mandatory | none | Contains `meta`, `collaborators`, `relatedDataProducts`, `resource`, `inputs`, `outputs`, `ports`, and `metrics` |

**Example usage:**

```yaml
data:
  meta:
```

### **`meta`**

**Description:** An optional section for additional metadata.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| object | optional | none | Contains key-value pairs for metadata |

**Example usage:**

```yaml
meta: # mandatory
  title: ${{Product Affinity & Cross-Sell Opportunity}} # optional
  sourceCodeUrl: ${{https://bitbucket.org/tmdc/product-affinity-cross-sell/src/main/}}
  trackerUrl: ${{https://rubikai.atlassian.net/browse/DPRB-65}}
```
<center>
  <img src="/products/data_product/configurations/dp_title.png" alt="DPH" style="width:40rem; border: 1px solid black;" />
  <figcaption><i>Data Product card showing the title on Data Product Hub</i></figcaption>
</center>

<center>
  <img src="/products/data_product/configurations/dp_meta.png" alt="DPH" style="width:40rem; border: 1px solid black;" />
  <figcaption><i>Data Product card showing the Git and Jira links on Data Product Hub</i></figcaption>
</center>


Below table describes each attribute of the product meta section.

| Key | Value | Description |
| --- | --- | --- |
| `title` | `${{Product Affinity & Cross-Sell Opportunity}}` | The name of the data product for product affinity and cross-sell opportunities. |
| `sourceCodeUrl` | `${{https://bitbucket.org/tmdc/product-affinity-cross-sell/src/main/}}` | URL to the source code repository. |
| `trackerUrl` | `${{https://rubikai.atlassian.net/browse/DPRB-65}}` | URL to the issue tracker for tracking development and tasks. |

<aside class="callout">

🗣️ If no title is provided, the default title will be set to the name of the product. For example, if a developer enters a name like 'product-affinity-cross-sell' without specifying a title, the system will automatically assign 'product-affinity-cross-sell' as the title.
 
</aside>

### **`collaborators`**

**Description:** Specifies the list of collaborators involved with the Data Product.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list of objects | mandatory | none | Each object contains `name` and `description` |

**Example usage:**

```yaml
collaborators:
  - name: ${{iamgroot}}
    description: ${{owner}}
  - name: ${{itsthor}}
    description: ${{developer}}
  - name: ${{itsloki}}
    description: ${{consumer}}
```

<center>
  <img src="/products/data_product/configurations/dp_collaborators.png" alt="DPH" style="width:40rem; border: 1px solid black;" />
  <figcaption><i>Data Product card showing the collaborators on Data Product Hub</i></figcaption>
</center>

<center>
  <img src="/products/data_product/configurations/metis_collaborators.png" alt="DPH" style="width:40rem; border: 1px solid black;" />
  <figcaption><i>Data Product card showing the collaborators on Metis</i></figcaption>
</center>

### **`name`**

**Description:** The name of the collaborator.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | Any valid string representing the collaborator's identity. |

**Example usage:**

```yaml
name: ${{iamgroot}}
```

### **`description`**

**Description:** A brief description of the collaborator's role.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | Example roles include owner, developer, consumer. |

**Example usage:**

```yaml
description: ${{owner}}
```

### **`relatedDataProducts`**

**Description:** Lists related Data Products connected or associated with the current Data Product.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list of strings | optional | none | Each string references another Data Product by specifying the version and name. |

**Example usage:**

```yaml
relatedDataProducts:
  - ${{data:v1beta:customer-360-demov3}}
```

### **`resource`**

**Description:** Defines the resources utilized by the Data Product.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| object | mandatory | none | Contains fields like `description`, `purpose`, `refType`, and `ref` |

**Example usage:**

```yaml
resource:
  description: ${{'Ingest data'}}
  purpose: ${{'ingestion'}}
  refType: ${{dataos}}
  ref: ${{bundle:v1beta:sales-data-pipeline}}
```
<center>
  <img src="/products/data_product/configurations/metis_bundle.png" alt="DPH" style="width:40rem; border: 1px solid black;" />
  <figcaption><i>Data Product card showing the Bundle Resource info on Metis</i></figcaption>
</center>

### **`description (resource)`**

**Description:** A brief description of the resource.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | Any string describing the resource. |

**Example usage:**

```yaml
description: ${{'Ingest data'}}
```

### **`purpose (resource)`**

**Description:** The purpose of the Resource.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | Possible values include specific purposes like `ingestion` |

**Example usage:**

```yaml
purpose: ${{'ingestion'}}
```

### **`refType`**

**Description:** The reference type of the Resource.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | Example: `dataos` |

**Example usage:**

```yaml
refType: ${{dataos}}
```

### **`ref`**

**Description:** The reference of the Resource.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | Example: `bundle:v1beta:sales-data-pipeline` |

**Example usage:**

```yaml
ref: ${{bundle:v1beta:sales-data-pipeline}}
```

### **`inputs`**

**Description:** Lists the input data sources required for the Data Product.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list of objects | mandatory | none | Each object describes an input with fields like `description`, `purpose`, `refType`, and `ref` |

**Example usage:**

```yaml
inputs: # mandatory
  - refType: dataos
    ref: dataset:icebase:customer_relationship_management:customer

  - refType: dataos
    ref: dataset:icebase:customer_relationship_management:purchase

  - refType: dataos
    ref: dataset:icebase:customer_relationship_management:product
```

<center>
  <img src="/products/data_product/configurations/dp_input.png" alt="DPH" style="width:40rem; border: 1px solid black;" />
  <figcaption><i>Data Product card showing an input on Data Product Hub</i></figcaption>
</center>

<center>
  <img src="/products/data_product/configurations/metis_input.png" alt="DPH" style="width:40rem; border: 1px solid black;" />
  <figcaption><i>Data Product card showing the input datasets on Metis</i></figcaption>
</center>


### **`outputs`**

**Description:** Specifies the output data generated by the Data Product.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list of objects | optional | none | Each object details an output with fields like `description`, `purpose`, `refType`, `ref`, and optional `checks` |

**Example usage:**

```yaml
outputs: # optional
  - refType: dataos
    ref: dataset:icebase:customer_relationship_management:product_affinity_matrix

  - refType: dataos
    ref: dataset:icebase:customer_relationship_management:cross_sell_recommendations
```

<center>
  <img src="/products/data_product/configurations/dp_output.png" alt="DPH" style="width:40rem; border: 1px solid black;" />
  <figcaption><i>Data Product card showing an output on Data Product Hub</i></figcaption>
</center>

<center>
  <img src="/products/data_product/configurations/metis_output.png" alt="DPH" style="width:40rem; border: 1px solid black;" />
  <figcaption><i>Data Product card showing the output datasets on Metis</i></figcaption>
</center>

### **`ports`**

**Description:** Defines the ports for accessing the Data Product through various tools.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| object | mandatory | none | Contains `lens`, `talos`, `rest`, and `postgres` sections for different types of ports |

**Example usage:**

```yaml
ports:
  lens:
    - ref: ${{lens:v1alpha:sales360:public}}
      refType: ${{dataos}}

  talos:
    - ref: ${{service:v1:sales360-talos:public}}
      refType: ${{dataos}}

```

