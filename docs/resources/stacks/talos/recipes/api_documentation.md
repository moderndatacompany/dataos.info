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

