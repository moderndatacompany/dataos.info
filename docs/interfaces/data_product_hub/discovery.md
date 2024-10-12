# Data Product Discovery

Discovering data among thousands of datasets is difficult without rich metadata and faceted search. The Data Product Hub is used as a single Data Product catalog that aggregates metadata about all Data Products and presents the appropriate information to users based on their needs. The Data Product Hub is intended to help data consumers make timely decisions with the right data.

A user-friendly interface is provided for Data Product discovery. Data Products can be discovered through a variety of strategies, including keyword searches and filters.

<center>
  <img src="/interfaces/data_product_hub/discovery/image%20(29).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
  <figcaption><i>Data Product Hub Interface</i></figcaption>
</center>


## How to discover Data Products of Interest

The Data Product discovery process is simplified with the following strategies.

### **Keyword search**

Search is available in the top right menu bar across the Data Products page within the Data Product Hub home page.

A simple yet powerful way to find Data Products is provided by typing the name, description, or owner in the search interface. By default, matching Data Products are displayed, grouped by use cases. The Data Product’s name may be human-readable or a unique identifier.

<center>
  <img src="/interfaces/data_product_hub/discovery/annotely_image%20(1)%20(1).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
  <figcaption><i>Keyword Search</i></figcaption>
</center>


### **Filters**

Multiple filter options further help narrow the search using parameters such as **Tier**, **Domain**, and **Owner**.

- **Tier:** Describes how the data product is organized, whether it follows a medallion architecture, is source-aligned, or is structured around specific entities or consumer needs.

- **Domain:** Specifies the business domain to which the data product belongs. Multiple domains can be selected at once to filter for the desired Data Product.

- **Owner:** Filters can be applied by owner, allowing users to direct questions to the appropriate person or team. The owner's DataOS User ID is used to list the various owners in the Owner dropdown, and only a single owner can be selected at a time.


    <center>
    <img src="/interfaces/data_product_hub/discovery/annotely_image%20(2)%20(1).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    <figcaption><i>Filters</i></figcaption>
    </center>
    

### **Categorize by domain**

By default, the search results are categorized by use cases, and they can also be categorized by domains.

<center>
  <img src="/interfaces/data_product_hub/discovery/annotely_image%20(3)%20(1).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
  <figcaption><i>Categorize by Domain</i></figcaption>
</center>


### **Recently searched Data Products**

Recently searched Data Products can be found in the 'Recent' tab, as illustrated below. Note that clearing the cache will remove all recently searched Data Products from the 'Recent' tab.

<center>
  <img src="/interfaces/data_product_hub/discovery/annotely_image%20(31)%20(1).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
  <figcaption><i>Recently searched Data Products</i></figcaption>
</center>


### **Favorites**

All starred Data Products can be found in the 'Favorites' tab.

<center>
  <img src="/interfaces/data_product_hub/discovery/annotely_image%20(32)%20(1).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
  <figcaption><i>Favorites</i></figcaption>
</center>


## Get a Quick Glance of the Data Products

For each Data Product displayed on the Data Products page, some basic information is shown on the Data Product card. The name of the Data Product, description, tier, and domain information can be viewed for each Data Product, while each one is categorized by use-case.

<center>
  <img src="/interfaces/data_product_hub/discovery/image%20(30).png" alt="DPH" style="width:20rem; border: 1px solid black;" />
  <figcaption><i>Data Products Page</i></figcaption>
</center>


A preview of the Data Products is provided by the Data Product Hub on the right-side panel. Clicking on the space next to the relevant Data Products allows for a quick preview.

## Detailed View of the Data Products

On clicking a Data Product, an interface is opened that provides an overview of the Data Product. In the following section, each part of the Data Product Hub interface is explained in detail.

### **Top panel**

The top panel of the Data Product details page displays the domain, name of the Data Product, description, Git repository link, JIRA link, tier, use-case, and owner.

Additionally, a button showcasing conformance with defined Accuracy, Completeness, Freshness, Schema, Uniqueness, and Validity constraints is displayed.

<center>
  <img src="/interfaces/data_product_hub/discovery/annotely_image%20(4)%20(1).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
  <figcaption><i>Data Product Details Page</i></figcaption>
</center>


### **Other details in the top panel**

Details on the top right of the data product details page include:

- **Add to Favorite:** By clicking the star icon (⭐), the respective Data Product can be added to Favorites.
- **BI Sync:** Opens the BI sync functionality, enabling the Data Product to be synced to PowerBI, Tableau Cloud, Tableau Desktop, and Apache Superset.
- **AI and ML:** Allows the data product to be consumed in Jupyter Notebooks to power AI and ML use cases.
- **App Development:** Enables syncing of the data product using REST and GraphQL APIs to power data applications.
- **Data API:** Allows the creation of Data APIs on top of the data product.
- **Explore:** Opens the Data Product for further exploration.


    <center>
    <img src="/interfaces/data_product_hub/discovery/image%20(54).png" alt="DPH" style="width:20rem; border: 1px solid black;" />
    <figcaption><i>Other details in the top panel of Data Product details</i></figcaption>
    </center>


### **Data Product tabs**

There are separate tabs each for Overview, Inputs, Outputs, Model, Metrics, Data APIs, Quality, and Access Options based on the respective data asset selected. Let's take a look at each of the tabs.

| **Tabs** | **Description** |
| --- | --- |
| **Overview** | Displays a visual snapshot of the Data Product, from inputs to outputs, including the semantic model. |
| **Inputs** | Lists all tables and schemas feeding into the data product with metadata and search functionality. |
| **Outputs** | Shows the tables generated by the data product, with metadata and search options for further analysis. |
| **Model** | Displays the semantic model, transforming inputs into insights for easier analysis. |
| **Metrics** | Allows exploration of key business metrics derived from the data product's lens models. |
| **Data APIs** | Lists available API endpoints for building data applications, with detailed descriptions and access info. |
| **Quality** | Provides insights into data quality checks, including completeness, freshness, and accuracy trends. |
| **Access Options** | Offers connection options to BI, AI, ML, and app development tools like Power BI, Excel, and Jupyter Notebook. |

**Overview tab**

The Overview Tab will display the visual snapshot of your Data Product's work: from input to output, including the semantic model, metrics, and access options.

<center>
  <img src="/interfaces/data_product_hub/discovery/annotely_image%20(5)%20(1).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
  <figcaption><i>Overview Tab</i></figcaption>
</center>

The ‘Inputs’ section displays all the datasets fed into the Data Product, while the ‘Output’ section lists the materialized tables generated from it. A Data Product doesn't need to have output, there can be a Data Product that exposes models. A Data Product presents only one model at a time, along with its associated metrics. Metrics are unavailable if the model is not built on top of the Data Product. The ‘Access Options’, list all the available consumption options to share the Data Product.

#### **Inputs tab**

Within the Inputs Tab, you will find all the tables and their schemas that feed into the data product, including those sourced from other data products. For each table you will see the Name of the Table, Tier, Domain, Owner, Access Permission, Uniform Data Link (UDL) Address, and the various data products the particular table is part of.

Below that you will find a search bar that enables you to search various columns with the table, you can also see other details of a specific column such as Data Type, Description, Tags, and Glossary Terms.

In addition to that you can open up a specific table within Metis, the DataOS Catalog to get comprehensive metadata of that table, as well as in the Workbench App for exploratory analysis using SQL.

<center>
  <img src="/interfaces/data_product_hub/annotely_image%20(6)%20(1).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
  <figcaption><i>Inputs Tab</i></figcaption>
</center>


To know more about the access permissions, click on ‘Restricted Access’, which will open a right panel as shown below.

<center>
  <img src="/interfaces/data_product_hub/discovery/image%20(31).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
  <figcaption><i>Restricted Access</i></figcaption>
</center>


The restricted access panel will give information about the filters and the policies applied to the input dataset as shown in the above image, if data masking is applied then it will show which column is masked along with the masking type. 

#### **Outputs tab**

The Output Tab displays the materialized tables generated by the Data Product, ready to be used on their own or combined with others to create new insights and Data Products. For each table you will see the Name of the Table, Tier, Domain, Owner, Access Permission, Uniform Data Link (UDL) Address, and the various Data Products the particular table is part of.

Below that you will find a search bar that enables you to search various columns with the table, you can also see other details of a specific column such as Data Type, Description, Tags, and Glossary Terms.

In addition to that you can open up a specific table within Metis, the DataOS Catalog to get comprehensive metadata of that table, as well as in the Workbench App for exploratory analysis using SQL.

<center>
  <img src="/interfaces/data_product_hub/discovery/annotely_image%20(7)%20(2).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
  <figcaption><i>Outputs Tab</i></figcaption>
</center>

#### **Model tab**

The Model tab displays a logical model, a representation of the Lens model built on top of the Data Product, shaping the data into meaningful insights for easier analysis and understanding.

<center>
  <img src="/interfaces/data_product_hub/discovery/annotely_image%20(8)%20(1).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
  <figcaption><i>Model Tab</i></figcaption>
</center>


#### **Metrics tab**

In the Metrics tab, you can explore the key business metrics derived from the lens models to observe the performance and make data-driven decisions with ease. 

<aside class="callout">

🗣 If a Data Product does not have any metrics built on top of it, the Metric tab will not be available.

</aside>

- In the image below, you can see a metric ‘Cloud Service Cost’ with its description and the number of measures, dimensions, and segments used to derive the metric. By clicking on the **Quick Insights** or **Explore** link you can further explore the metrics.

    <center>
    <img src="/interfaces/data_product_hub/discovery/annotely_image%20(10)%20(1).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    <figcaption><i>Quick Insights and Explore</i></figcaption>
    </center>

    

- Below you can see the **References** section that shows the lineage with the flow, from which dataset, the metric is derived.

    <center>
    <img src="/interfaces/data_product_hub/discovery/annotely_image%20(11)%20(1).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    <figcaption><i>References</i></figcaption>
    </center>

    
- The **Measures** and **Dimensions** section gives details of each dimension and measure used to derive the metric such as name, data type, description, and alias.

    <center>
    <img src="/interfaces/data_product_hub/discovery/annotely_image%20(12)%20(1).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    <figcaption><i>Measures and Dimensions</i></figcaption>
    </center>


    

#### **Data APIs tab**

In the Data APIs tab, you can explore the API endpoints to develop the data applications. 

<aside class="callout">

🗣 If a Data Product does not have any APIs built on top of it, the Data API tab will not be available.

</aside>

- On clicking the Data APIs tab, it will list all the API endpoint collections. by clicking on a particular endpoint, you can see a short description of the API collection as shown below.
    
    <center>
    <img src="/interfaces/data_product_hub/discovery/annotely_image%20(13)%20(1).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    <figcaption><i>API Endpoint Collections</i></figcaption>
    </center>

    
- You can download the OpenAPI specifications and Postman collection for each endpoint by clicking on the **Download OpenAPI Spec** and **Download Postman Collection** respectively.

    <center>
    <img src="/interfaces/data_product_hub/discovery/annotely_image%20(15)%20(1).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    <figcaption><i>Download OpenAPI spec and Postman collection</i></figcaption>
    </center>

    
- After downloading the OpenAPI Spec and Postman Collection, open the Postman application.

    <center>
    <img src="/interfaces/data_product_hub/discovery/image%20(32).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    <figcaption><i>Postman Application</i></figcaption>
    </center>

 
    
- Go to Collections, click on import, and select the files option, in which you have to select the downloaded JSON file.

    <center>
    <img src="/interfaces/data_product_hub/discovery/annotely_image%20(17)%20(1).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    <figcaption><i>Import collection</i></figcaption>
    </center>

    
- On clicking the ‘View complete documentation’ link, it will open an OpenAPI documentation as shown below.
    
    <center>
    <img src="/interfaces/data_product_hub/discovery/annotely_image%20(18)%20(1).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    <figcaption><i>View Complete Documentation</i></figcaption>
    </center>


    
- To hit the API endpoint on Postman, click on the ‘Open request’ link as shown in the above image, which will open the below interface.
    
    <center>
    <img src="/interfaces/data_product_hub/discovery/image%20(33).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    <figcaption><i>Open Request</i></figcaption>
    </center>

    
- Hover over the `{{baseUrl}}`, and copy the base URL.

    <center>
    <img src="/interfaces/data_product_hub/discovery/image%20(34).png" alt="DPH" style="width:55rem; border: 1px solid black;" />
    <figcaption><i>Copy the Base URL</i></figcaption>
    </center>
    
    
- Paste the copied URL in place of `{{baseUrl}}`, give your DataOS API key as a bearer token, and click on the send after which you can access the data as shown below. You can use this API endpoint along with the bearer token to build your data application.
    
    <center>
    <img src="/interfaces/data_product_hub/discovery/annotely_image%20(19)%20(1).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    <figcaption><i>Paste the copied URL</i></figcaption>
    </center>

    
- Now on the Data APIs tab, by clicking on the particular API endpoint you can see who has access to the endpoint, the description of the endpoint, authorization details, response details, and the response samples.
    
    <center>
    <img src="/interfaces/data_product_hub/discovery/annotely_image%20(20)%20(1).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    <figcaption><i>API Endpoint Access</i></figcaption>
    </center>

    
- **Authorizations - bearerToken** indicates that the API requires an authorization token, specifically a **Bearer Token** for authentication. **Bearer Token** is a type of token that must be included in the HTTP header when making requests to the API. The format of the token is **JWT** (JSON Web Token), which is a compact, URL-safe means of representing claims to be transferred between two parties.

    <center>
    <img src="/interfaces/data_product_hub/discovery/image%20(35).png" alt="DPH" style="width:20rem; border: 1px solid black;" />
    <figcaption><i>Authorization</i></figcaption>
    </center>
    
    
- In the **Responses section,** a **200 response** indicates that the request was successful, and the API is returning data as expected. The response schema is in **application/json** format, which means the data will be returned in JSON format. The response schema defines the structure of the data returned when the API responds with a **200 (OK)** status.
    
    <center>
    <img src="/interfaces/data_product_hub/discovery/image%20(36).png" alt="DPH" style="width:20rem; border: 1px solid black;" />
    <figcaption><i>Response section</i></figcaption>
    </center>

    
    In this case, the API returns the following fields:
    
    - **total_revenue (string)**: This field provides the total revenue generated by the brand. The value is expected to be a string, even though it represents financial information (likely formatted with currency symbols or as a string for other reasons). The description indicates that this data provides insight into the financial performance of the brand.
    - **brand (string)**: This field contains the name of the brand being analyzed. It represents the company related to the revenue data.
    
    The **5XX** status code refers to a server-side error. If the API is unable to process the request due to an internal issue or failure, it will return a 5XX response. This indicates a problem on the server, not with the client's request.
    
- The **Response Samples** section provides a sample of what the successful **200** response would look like when calling this API. The sample JSON response provided in the below image has two fields **total_revenue** and **brand.** In this sample, both `total_revenue` and `brand` are shown as placeholder strings. In a real response, `total_revenue` will be a string representing the revenue (like `"10000 USD"`), and the `brand` will be the actual brand name (like `"Nike"` ).
    
    <center>
    <img src="/interfaces/data_product_hub/discovery/image%20(37).png" alt="DPH" style="width:20rem; border: 1px solid black;" />
    <figcaption><i>Response Samples</i></figcaption>
    </center>
    
    **GET /top_brand_list** is the **API endpoint** that you will call using the HTTP `GET` method. It retrieves data related to a list of top brands. Typically, `GET` methods are used to retrieve data from a server without modifying it.
    

#### **Quality tab**

The **Quality tab** provides insights into the health and quality of your input and output data, allowing you to monitor and ensure that the data meets expected standards across several quality checks. 

Quality is categorized into six types, that is Schema, Freshness, Validity, Completeness, Uniqueness, and Accuracy.

<div style="text-align: center;">
  <table border="1" cellpadding="10" cellspacing="0">
    <tr>
      <th>Category</th>
      <th>Description</th>
    </tr>
    <tr>
      <td>Freshness</td>
      <td>Reflects how up-to-date and timely the data is.</td>
    </tr>
    <tr>
      <td>Schema</td>
      <td>Keep an eye on your data structure, ensuring everything is aligned and consistent.</td>
    </tr>
    <tr>
      <td>Validity</td>
      <td>Check that your data follows the expected rules and formats, keeping things on track.</td>
    </tr>
    <tr>
      <td>Completeness</td>
      <td>Ensure you have all the data you need, without gaps or missing pieces.</td>
    </tr>
    <tr>
      <td>Uniqueness</td>
      <td>Verify that your data stays clean and non-duplicated, providing clear, trustworthy results.</td>
    </tr>
    <tr>
      <td>Accuracy</td>
      <td>Confirms that the data correctly represents the real-world values and facts it models.</td>
    </tr>
  </table>
</div>



- In the image below, it tracks aspects like completeness, schema validation, uniqueness, and accuracy.
    

    <center>
    <img src="/interfaces/data_product_hub/discovery/annotely_image%20(21)%20(1).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    <figcaption><i>Quality Tab</i></figcaption>
    </center>


    
- In the above image, data have 100% completeness which ensures that essential fields do not contain missing or null values.
- Trend Chart displays the completeness over time. The y-axis represents completeness as a percentage (0-100%), while the x-axis represents the timeline. In this case, the chart indicates a consistent **100% completeness** for the period shown (up to September 13th), meaning no data was missing.
    
    <center>
    <img src="/interfaces/data_product_hub/discovery/image%20(38).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    <figcaption><i>Trend chart</i></figcaption>
    </center>

    
- Below you can see the applied checks and their status. In this case the `f_sales` dataset, the completeness check focuses on ensuring that critical columns are fully populated. `f_sales_invoice_no_completeness_of_the_invoice_number_column` check ensures that the `invoice_number` column in the `f_sales` dataset does not have missing or null values. A green checkmark (✔) indicates that the check has passed successfully. In this case, there are no missing invoice numbers, and the dataset is 100% complete in this aspect.

    <center>
    <img src="/interfaces/data_product_hub/discovery/image%20(39).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    <figcaption><i>Applied Checks and their status</i></figcaption>
    </center>

    

#### **Access options tab**

The **Access options** tab allows users to connect their Data Products to various [BI (Business Intelligence)](/interfaces/data_product_hub/#bi-sync), [AI and ML](/interfaces/data_product_hub/#aiml), [app development](/interfaces/data_product_hub/#app-development), and [Data API](/interfaces/data_product_hub/#data-apis) tools like Power BI, Excel, Tableau, Apache Superset, Jupyter Notebook, etc. 

<center>
<img src="/interfaces/data_product_hub/discovery/annotely_image%20(22)%20(1).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
<figcaption><i>Access Options Tab</i></figcaption>
</center>


To know more about access options, please [refer to this section](/interfaces/data_product_hub/discovery/#access-options-tab). 

## **Perspectives**

In the Perspectives tab, you can access the saved explorations of the Data Products as Perspectives.

<center>
<img src="/interfaces/data_product_hub/discovery/image%20(40).png" alt="DPH" style="width:20rem; border: 1px solid black;" />
<figcaption><i>Perspectives Tab</i></figcaption>
</center>



**How to create a Perspective?**

Follow the below steps to save your Data Product exploration as a Perspective to access it later on the Perspective tab.

1. Choose the Data Product of your choice and navigate to the ‘Explore’ button. 
    
    <center>
    <img src="/interfaces/data_product_hub/discovery/annotely_image%20(23)%20(1).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    <figcaption><i>Choose and Navigate</i></figcaption>
    </center>


    
2. Click the ‘Explore’ tab, where you can start exploring the Data Product.
    
    <center>
    <img src="/interfaces/data_product_hub/discovery/image%20(41).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    <figcaption><i>Navigate to Explore Tab</i></figcaption>
    </center>

    
3. After exploration, navigate to the **Save Perspective** button.
    
    <center>
    <img src="/interfaces/data_product_hub/discovery/image%20(42).png" alt="DPH" style="width:20rem; border: 1px solid black;" />
    <figcaption><i>Save Perspective</i></figcaption>
    </center>

4.  On clicking the ‘Saved Perspective’ button, it will open a dialogue box prompting for the name and description of your perspective.
    
    <center>
    <img src="/interfaces/data_product_hub/discovery/image%20(43).png" alt="DPH" style="width:20rem; border: 1px solid black;" />
    <figcaption><i>Dialogue Box</i></figcaption>
    </center>


5. Give your exploration a name and description (optional) and click on ‘Save’.
    
    <center>
    <img src="/interfaces/data_product_hub/discovery/image%20(44).png" alt="DPH" style="width:20rem; border: 1px solid black;" />
    <figcaption><i>Save</i></figcaption>
    </center>



**How to access the perspectives?**

After saving your exploration as a perspective to access it later on the Perspective tab follow the below steps.

1. Navigate to the ‘Perspectives’ tab, where you can access all the perspectives given by name, tags, data product, and owner. 
    
    <center>
    <img src="/interfaces/data_product_hub/discovery/image%20(45).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    <figcaption><i>Navigate to Perspectives Tab</i></figcaption>
    </center>


2. In the search bar, you can directly search for the perspectives by name or keywords used in a name.
    
    <center>
    <img src="/interfaces/data_product_hub/discovery/image%20(46).png" alt="DPH" style="width:20rem; border: 1px solid black;" />
    <figcaption><i>Search</i></figcaption>
    </center>


3. You can filter out the perspectives by the owners, navigate to the ‘Filters’ drop-down, click on the ‘Owner’ option, and select the owner of your choice.
    
    <center>
    <img src="/interfaces/data_product_hub/discovery/image%20(47).png" alt="DPH" style="width:20rem; border: 1px solid black;" />
    <figcaption><i>Filter</i></figcaption>
    </center>



4. Similarly, as the ‘Owner’, you can filter out the perspectives by the ‘Data Products’ and ‘Tags’. 

    <center>
    <img src="/interfaces/data_product_hub/discovery/annotely_image%20(25)%20(1).png" alt="DPH" style="width:20rem; border: 1px solid black;" />
    <figcaption><i>Filter using 'Data Products'</i></figcaption>
    </center>
    


    <center>
    <img src="/interfaces/data_product_hub/discovery/annotely_image%20(24)%20(1).png" alt="DPH" style="width:20rem; border: 1px solid black;" />
    <figcaption><i>Filter using 'Tags'</i></figcaption>
    </center>

    
    
5. For example, on selecting the ‘corp-market-performance’ Data Product on the Filters options, it will list out all the perspectives created on that Data Product as shown   below. 
    
    <center>
    <img src="/interfaces/data_product_hub/discovery/annotely_image%20(26)%20(1).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    <figcaption><i>List Perspectives</i></figcaption>
    </center>


    
6. On clicking any perspective it will redirect you to the Explore page of the Data Product on which the particular perspective is created as shown below, where you can continue with your exploration.

    <center>
    <img src="/interfaces/data_product_hub/discovery/image%20(48).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    <figcaption><i>Explore</i></figcaption>
    </center>
    


## **Metrics**

In the Metrics tab, you can access the actionable and reliable key insights of the Data Products to get information, assess operations, and make quick and right decisions for your business. To explore the ‘Metric’ tab, navigate to the Metric tab, and you’ll see a short description on the tab, by default, you’ll be able to see all the metrics grouped by use cases.

> A metric is an entity that, by default, provides a logical view of the logical table, containing only one measure and a time dimension.


<center>
<img src="/interfaces/data_product_hub/discovery/image%20(49).png" alt="DPH" style="width:20rem; border: 1px solid black;" />
<figcaption><i>Metrics Tab</i></figcaption>
</center>


<center>
<img src="/interfaces/data_product_hub/discovery/image%20(50).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
<figcaption><i>Metrics Listing Page</i></figcaption>
</center>


**Search the metrics by keyword**

In the search bar, you can directly search for the potential metrics by keywords, just enter the name or keyword used in the metric name as shown below.

<center>
<img src="/interfaces/data_product_hub/discovery/image%20(51).png" alt="DPH" style="width:20rem; border: 1px solid black;" />
<figcaption><i>Search the metrics by keyword</i></figcaption>
</center>


**Filter the metrics**

You can filter out the metrics by the particular owner, by navigating to the ‘Filter’ drop-down, clicking on the owners, and selecting the owner of your choice   

<center>
<img src="/interfaces/data_product_hub/discovery/image%20(52).png" alt="DPH" style="width:20rem; border: 1px solid black;" />
<figcaption><i>Filter the metrics</i></figcaption>
</center>


**Metrics recommendations based on domains**

On navigating to the Metrics tab, by default, it recommends the metrics grouped by use cases, if you want the metrics recommendation based on the domain, simply navigate to the ‘Use-case’ drop-down and select the ‘Domain’ option, now you’ll get the metrics recommendation grouped by domains. 

<center>
<img src="/interfaces/data_product_hub/discovery/image%20(53).png" alt="DPH" style="width:20rem; border: 1px solid black;" />
<figcaption><i>Metrics recommendations based on domains</i></figcaption>
</center>

