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

In the example provided, `productname` represents a placeholder for accessing a specific record. Here, `productname` refers to the column name used to identify the record. Similarly, as per your requirements, you can customize the request section.

To access this API documentation, on your browser, open this link `http://localhost:3000/doc?apikey=xxx` by providing your DataOS API token which you have used to configure Talos.

<center>
  <img src="/resources/stacks/talos/img1.png" alt="Talos" style="width:60rem; border: 1px solid black;" />
  <figcaption><i>Talos API Documentation</i></figcaption>
</center>

You can also include a sample section to illustrate the metadata of the dataset. For example, by providing sample parameters, data developers can gain a clearer understanding of the data exposed by the API, as shown below.

<center>
  <img src="/resources/stacks/talos/img2.png" alt="Talos" style="width:60rem; border: 1px solid black;" />
  <figcaption><i>Talos API Documentation</i></figcaption>
</center>

<aside class=callout>
🗣 Note that, if caching is enabled in the API endpoint, the sampling functionality is disabled.
</aside>
