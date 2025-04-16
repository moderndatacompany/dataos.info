# **Generating Comprehensive API Documentation**

Talos automatically generates and serves API documentation. To enable automated API documentation generation, configure the `table.yaml` file corresponding to the `table.sql` file by adding the following attributes:

```yaml
urlPath: /artist/:productname  # Defines the API endpoint with a dynamic path parameter
request:  # Specifies the request parameters
  - fieldName: productname  # Defines the name of the field in the request
    fieldIn: path  # Specifies where the field appears in the request (e.g., path, query)
    description: Constituent product name  # Provides a brief description of the field
    validators:
      - required  # Specifies validation rules (e.g., mandatory field)
sample:  # Defines a sample response (optional)
  parameters:  # Specifies example values for API request parameters
    productname: 'Samsung Convoy 3'
    sales: 1
    quantity: 1
    profit: 1
  profile: snowflake  # Indicates the data source profile
sources:
  - snowflake  # Specifies the data source used for querying records

```

## Request Parameter

The `request` parameter specifies input fields required for API requests. In the example above, `productname` acts as a placeholder for identifying a product record. This parameter should be customized based on API requirements.

### **Attributes of `request` Parameter**

| Attribute | Data Type | Default Value | Possible Values | Requirement |
| --- | --- | --- | --- | --- |
| `fieldName` | string | none | e.g., `productname` | Mandatory if the request parameter is applied |
| `fieldIn` | string | none | `path` | Mandatory if the request parameter is applied |
| `description` | string | none | Any description | Optional |
| `validators` | object | none | `required` | Optional |

## **Sample Parameter**

The `sample` parameter provides an example representation of the data available through the API.

<aside>🗣 If caching is enabled on the API endpoint, the sampling functionality is disabled.

</aside>

### **Attributes of `sample` Parameter**

| Attribute | Data Type | Default Value | Possible Values | Requirement |
| --- | --- | --- | --- | --- |
| `fieldName` | string | none | e.g., `productname` | Mandatory if the request parameter is applied |
| `fieldIn` | string | none | `path` | Mandatory if the request parameter is applied |
| `description` | string | none | Any description | Optional |
| `validators` | object | none | `required` | Optional |

## **Additional Parameters in `api.yaml`**

### **Filters**

Filters define access restrictions based on user groups. They ensure that different users receive appropriate content.

```yaml
filters:
  - description: Allow only 'US' content  # Describes the filtering rule
    userGroups:
      - reader  # User group with access
      - default  # Default user group with access

  - description: Indian Content Only  # Describes a filter for Indian content
    userGroups:
      - asian  # User group with access
      - indian  # User group with access

```

### **Attributes of `filters` Parameter**

| Attribute | Data Type | Default Value | Possible Values | Requirement |
| --- | --- | --- | --- | --- |
| `description` | string | none | Any description | Optional |
| `userGroups` | array | none | Defined user groups | Mandatory (at least one value must be specified) |

### **Dependencies**

Dependencies specify external tables and columns required for API functionality. This ensures that users understand the data sources involved.

```yaml
depends:
  - table: dataos://icebase:default/country  # Defines the external table dependency
    columns:
      - Country  # Specifies required column
      - Country_code  # Specifies required column
      - WHO_region  # Specifies required column

```

### **Attributes of `depends` Parameter**

| Attribute | Data Type | Default Value | Possible Values | Requirement |
| --- | --- | --- | --- | --- |
| `table` | string | none | Table name | Mandatory |
| `columns` | array | none | Column names | Mandatory (at least one column must be specified) |

### **Headers**

Headers define key-value pairs required for API requests and responses.

```yaml
headers:
  - key: my-personal-key  # Defines a custom API key
    value: super-hot-value  # Corresponding value for the key

  - key: Cache-Control  # Standard HTTP header to manage caching
    value: max-age=604800  # Defines the maximum cache age in seconds (7 days)

```

### **Attributes of `headers` Parameter**

| Attribute | Data Type | Default Value | Possible Values | Requirement |
| --- | --- | --- | --- | --- |
| `key` | string | none | Any key | Mandatory |
| `value` | string | none | Corresponding value | Mandatory |

## Accessing API Documentation

API documentation can be accessed via a web browser using the following URL:

```
http://localhost:3000/doc?apikey=xxx

```

Replace `xxx` with the DataOS API token configured for Talos. Additionally, the OpenAPI specification can be downloaded in JSON format by clicking the **Download** button.

<center> <img src="/resources/stacks/talos/img1.png" alt="Talos API Documentation" style="width:50rem; border: 1px solid black;" /> <figcaption><i>Talos API Documentation</i></figcaption> </center>

## Sample Section for Dataset Metadata

A sample section can be included to illustrate dataset metadata. This helps developers understand the data exposed by the API.

<center> <img src="/resources/stacks/talos/img2.png" alt="Talos Sample Metadata" style="width:50rem; border: 1px solid black;" /> <figcaption><i>Talos API Documentation</i></figcaption> </center>