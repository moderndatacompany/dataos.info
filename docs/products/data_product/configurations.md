The following attributes are declared for every Product deployed in a DataOS context. Some of these attributes/fields need to be mandatorily declared, while others are optional.

## Structure of Product meta section

```yaml
# Product meta section
name: {{lens-dp-test2}} # Resource name (mandatory)
version: v1alpha # Manifest version (mandatory)
entity: product # Entity (Mandatory)
type: data # Product-type (mandatory)
tags: # Tags (Optional)
  - data-product
  - dataos:type:product
  - dataos:product:data
  - dataos:product:data:lens-dp-test
description: the customer 360 view of the world # Descripton of the product (Optional)
purpose: The purpose of the data product is to provide comprehensive insights into the creditworthiness of companies. By leveraging various data points such as company contact information, credit score, company details, financial data, and industrial data, this product aims to assist users in making informed decisions related to credit risk assessment, investment opportunities, and business partnerships.
collaborators: # collaborators User ID (Optional)
  - thor
  - blackwidow
  - loki 
owner: iamgroot # Owner (Optional)
refs: # Reference (Optional)
  - title: Lens Info # Reference title (Mandatory if adding reference)
    href: https://dataos.info/interfaces/lens/ # Reference link (Mandatory if adding reference)
```

## Configuration attributes

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

