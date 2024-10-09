# How to generate the comprehensive API documentation?

Talos automatically generates and serves the API documentation for you. To automate API documentation generation, add the following attributes to your `table.yaml` corresponding to your `table.sql` file.

```yaml
urlPath: /artist/:productname
request:
  - fieldName: productname
    fieldIn: path
    description: constituent product name
    validators:
      - required 
sample: # Optional 
  parameters:
    productname: 'Samsung Convoy 3'
    sales: 1
    quantity: 1
    profit: 1
  profile: snowflake
sources:
  - snowflake       
```

## **`request` parameter**
In the example provided, `productname` represents a placeholder for accessing a specific product record. Here, `productname` refers to the column name used to identify the record. Similarly, as per your requirements, you can customize the request section.
For detailed information about each attribute, please refer to the below table.

| Attribute      | Data Type | Default Value | Possible Value      | Requirement |
|----------------|-----------|---------------|---------------------|-------------|
| `fieldName`    | string    | none          | 'productname'       | mandatory if request parameter applied     |
| `fieldIn    `  | string    | none          | 'path'              | mandatory if request parameter applied     |
| `description`  | string    | none          |  any description    | optional     |
| `validators`   | object    | none          | `required'          | optional     |



## **`sample` parameter**
Sample parameter is useful when you want to provide the sample of your data in the API doc.

<aside class=callout>
🗣 Note that, if caching is enabled in the API endpoint, the sampling functionality is disabled.
</aside>

For detailed information about each attribute, please refer to the below table.

| Attribute      | Data Type | Default Value | Possible Value      | Requirement |
|----------------|-----------|---------------|---------------------|-------------|
| `fieldName`    | string    | none          | 'productname'       | mandatory if request parameter applied     |
| `fieldIn    `  | string    | none          | 'path'              | mandatory if request parameter applied     |
| `description`  | string    | none          |  any description    | optional     |
| `validators`   | object    | none          | `required'          | optional     |

## Additional Parameters

Below are some additional parameters you can add in the `api.yaml` manifest file to enhance the API documentation.

### **Filters**

Added detailed descriptions for filters to explain how different user groups will access content. This enhances the documentation, providing clear guidance for users interacting with the API.

```yaml
filters:
  - description: Allow only 'US' content
    userGroups:
      - reader
      - default
  - description: Indian Content Only
    userGroups:
      - asian
      - indian
```

For detailed information about each attribute, please refer to the below table.

| Attribute    | Data Type | Default Value | Possible Value  | Requirement                           |
|--------------|-----------|---------------|-----------------|---------------------------------------|
| `description`| string    | none          | any description | optional                              |
| `userGroups` | array     | none          | defined user groups | mandatory (at least one value must be specified) |



### **Dependencies**

Included descriptions of external dependencies, such as tables and columns, that the API relies on. This adds context to the API documentation, ensuring users understand the data sources involved.

```yaml

depends:
  - table: dataos://icebase:default/country
    columns:
      - Country
      - Country_code
      - WHO_region

```
For detailed information about each attribute, please refer to the below table.

| Attribute  | Data Type | Default Value | Possible Value                                | Requirement                           |
|------------|-----------|---------------|-----------------------------------------------|---------------------------------------|
| `table`    | string    | none          | table name           | mandatory                             |
| `columns`  | array     | none          | column name      | mandatory (at least one column must be specified) |



### **Headers**

Added detailed context about the headers used in the API, including their purpose and value. This helps developers understand how headers should be managed in requests and responses.

```yaml
headers:
  - key: my-personal-key
    value: super-hot-value
  - key: Cache-Control
    value: max-age=604800
```

For detailed information about each attribute, please refer to the below table.

| Attribute | Data Type | Default Value | Possible Value                | Requirement                           |
|-----------|-----------|---------------|-------------------------------|---------------------------------------|
| `key`     | string    | none          | any key | mandatory                             |
| `value`   | string    | none          | value corresponding to the key | mandatory                             |


## Access the API documentation

To access this API documentation, on your browser, open this link `http://localhost:3000/doc?apikey=xxx` by providing your DataOS API token which you have used to configure Talos. You can also download OpenAPI specification in the JSON format by clicking on the Download button as shown below.

<center>
  <img src="/resources/stacks/talos/img1.png" alt="Talos" style="width:50rem; border: 1px solid black;" />
  <figcaption><i>Talos API Documentation</i></figcaption>
</center>

You can also include a sample section to illustrate the metadata of the dataset. For example, by providing sample parameters, data developers can gain a clearer understanding of the data exposed by the API, as shown below.

<center>
  <img src="/resources/stacks/talos/img2.png" alt="Talos" style="width:50rem; border: 1px solid black;" />
  <figcaption><i>Talos API Documentation</i></figcaption>
</center>

