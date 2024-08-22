# Data Product Configurations

The following attributes are declared for every Data Product deployed in a DataOS context. Some of these attributes/fields need to be mandatorily declared, while others are optional.

## Structure of Data Product manifest file

=== "version:v1alpha"

    ```yaml
    # Product meta section
    name: ${{dp-test}} # Product name (mandatory)
    version: v1alpha # Manifest version (mandatory)
    type: ${{data}} # Product-type (mandatory)
    tags: # Tags (Optional)
      - ${{data-product}}
      - ${{dataos:type:product}}
      - ${{dataos:product:data}}
    description: ${{the customer 360 view of the world}} # Descripton of the product (Optional)
    Purpose: ${{This data product is intended to provide insights into the customer for strategic decisions on cross-selling additional products.}} # purpose (Optional)
    collaborators: # collaborators User ID (Optional)
      - ${{thor}}
      - ${{blackwidow}}
      - ${{loki}}
    owner: ${{iamgroot}} # Owner (Optional)
    refs: # Reference (Optional)
      - title: ${{Data Product Hub}} # Reference title (Mandatory if adding reference)
        href: ${{https://liberal-donkey.dataos.app/dph/data-products/all}} # Reference link (Mandatory if adding reference)
    entity: ${{product}} # Entity (Mandatory)
    # Data Product-specific section (Mandatory)
    v1alpha: # Data Product version
      data:
        resources: # Resource specific section(Mandatory)
          - name: ${{bundle-dp}} # Resource name (Mandatory)
            type: ${{bundle}} # Resource type (Mandatory)
            version: ${{v1beta}} # Resource version (Mandatory)
            refType: ${{dataos}} # Resource reference type (Mandatory)
            workspace: ${{public}} # Workspace (Requirement depends on the resource type)
            description: ${{this bundle resource is for a data product}} # Resource description (Optional)
            purpose: ${deployment of data product resources}} # Purpose of the required resource (Optional)   
        
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
=== "version:v1beta"

    ```yaml
    # Product meta section
    name: ${{sales-360}} # Product name (mandatory)
    version: v1beta # Manifest version (mandatory)
    entity: ${{product}} # Entity type (mandatory)
    type: ${{data}} # Product type (mandatory)
    purpose: ${{Sales360 enables data analysts to efficiently explore and analyze sales data, with robust capabilities across product and customer dimensions.}} # Purpose (optional)
    tags: # Tags (Optional)
      - ${{DPDomain.sales}}
      - ${[DPTier.Consumer-aligned}}
      - ${{DPUsecase.purchase behaviour}}
    description: ${{Sales360 enables data analysts to efficiently explore and analyze sales data, with robust capabilities across product and customer dimensions.}} # Descripton of the product (Optional)
    refs: # Reference (Optional)
    - title: ${{'Workspace Info'}} # Reference title (Mandatory if adding reference)
      href: ${{https://dataos.info/interfaces/cli/command_reference/#workspace}} # Reference link (Mandatory if adding reference)

    # Data Product-specific section (Mandatory)
    v1beta: # Data Product version
      data:
        meta:
          foo: bar
        collaborators: # Collaborators (mandatory)
          - name: ${{iamgroot}} # Collaborator's name 
            description: ${{owner}} #Collaborator's description
          - name: ${{itsthor}} # Collaborator's name 
            description: ${{developer}} #Collaborator's description
          - name: ${{itsloki}} # Collaborator's name 
            description: ${{consumer}} #Collaborator's description
        relatedDataProducts: # (optional)
          - ${{data:v1beta:customer-360-demov3}}

        resource: # Resource specific section (mandatory)
          description: ${{'Ingest data'}} # Resource description (optional)
          purpose: ${{'ingestion'}} # Resource purpose (optional)
          refType: ${{dataos}} # Resource reference type (Mandatory) 
          ref: ${{bundle:v1beta:sales-data-pipeline}} # Resource reference

        inputs: # Input specific section (mandatory)
        - description: ${{icebase.sales360mockdb.f_sales}} # Input decsription
          purpose: ${{source}} # Input purpose
          refType: ${{depot}} # Input reference type
          ref: ${{dataos://icebase:sales360mockdb/f_sales}} # Input reference

        - description: ${{customer data pulling from s3 bucket}} 
          purpose: ${{source}}
          refType: ${{dataos}}
          ref: ${{dataset:icebase:sales360mockdb:customer_data_master}}

        - description: ${{product data pulling from s3 bucket}}
          purpose: ${{source}}
          refType: ${{dataos}}
          ref: ${{dataset:icebase:sales360mockdb:product_data_master}}

        outputs:
        - description: ${{sales data}} # Output description
          purpose: ${{source}} # Output purpose
          refType: ${{dataos}} # Output reference type
          ref: ${{dataset:icebase:flash:f_sales}} # Output reference
          checks: 
            availability: ${{bar}} 
        ports: 
          lens: 
            ref: ${{lens:v1alpha:sales360:public}} # Lens reference
            refType: ${{dataos}} # Reference type
            meta: 
              foo: bar 
          talos: 
          - ref: ${{service:v1:sales360-talos:public}} #  Talos reference
            refType: ${{dataos}} # Reference type
            meta: 
              foo: bar 
          rest: 
          - url: https://liberal-donkey.dataos.app/lens2/api/public:sales360/v2/rest # API endpoint url
            meta: 
              foo: bar 
          postgres: 
          - host: ${{tcp.liberal-donkey.dataos.app}} 
            port: ${{5432}} 
            params: 
              ssl: ${{true}} 
            meta: 
              foo: bar 
        metrics: 
          - description: ${{understand proof revenue across product dimensions}} # Metrics description
            purpose: ${{metric analysis}} # Metrics purpose
            refType: ${{depot}} # Metrics reference type
            ref: ${{lens:public:sales360:wallet_sales_view}} # Metrics reference

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

Data Product-specific section is different for different versions. This section comprises attributes specific to the Data Product for each version. The attributes within the section are listed below:

### **`v1alpha`**

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

#### **`resources`**

**Description:** Represents the resource mappings associated with the Data Product.

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
🗣 Workspace is required and mandatory only for <a href="/resources/index/">workspace-level resources</a>.
</aside>

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | workspace specific to the referred resource  |

**Example Usage:**

```yaml
workspace: public 
```

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
inputs:
  - description: ${{icebase.sales360mockdb.f_sales}}
    purpose: ${{source}}
    refType: ${{depot}}
    ref: ${{dataos://icebase:sales360mockdb/f_sales}}
  - description: ${{customer data pulling from s3 bucket}}
    purpose: ${{source}}
    refType: ${{dataos}}
    ref: ${{dataset:icebase:sales360mockdb:customer_data_master}}
```

#### **`outputs`**

**Description:** Specifies the output data generated by the Data Product.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list of objects | mandatory | none | Each object details an output with fields like `description`, `purpose`, `refType`, `ref`, and optional `checks`. |

**Example Usage:**

```yaml
yamlCopy code
outputs:
  - description: ${{sales data}}
    purpose: ${{source}}
    refType: ${{dataos}}
    ref: ${{dataset:icebase:flash:f_sales}}
    checks:
      availability: ${{bar}}

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
    meta:
      foo: bar
  talos:
    - ref: ${{service:v1:sales360-talos:public}}
      refType: ${{dataos}}
      meta:
        foo: bar
```

#### **`metrics`**

**Description:** Lists the metrics related to the Data Product, used for analysis and monitoring.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list of objects | optional | none | Each object contains fields like `description`, `purpose`, `refType`, and `ref`. |

**Example Usage:**

```yaml
metrics:
  - description: ${{understand proof revenue across product dimensions}}
    purpose: ${{metric analysis}}
    refType: ${{depot}}
    ref: ${{lens:public:sales360:wallet_sales_view}}
```

