# Data Product discovery

Discovering data among thousands of datasets is difficult without rich metadata and faceted search. The Data Product Hub is used as a single Data Product catalog that aggregates metadata about all Data Products and presents the appropriate information to users based on their needs. The Data Product Hub is intended to help data consumers make timely decisions with the right data.

A user-friendly interface is provided for Data Product discovery. Data Products can be discovered through a variety of strategies, including keyword searches and filters.

<center>
  <img src="/interfaces/data_product_hub/discovery/image%20(29).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
  <figcaption><i>Data Product Hub Interface</i></figcaption>
</center>


## How to discover the Data Products of interest ?

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


## Get a quick glance of the Data Products

For each Data Product displayed on the Data Products page, some basic information is shown on the Data Product card. The name of the Data Product, description, tier, and domain information can be viewed for each Data Product, while each one is categorized by use-case.

<center>
  <img src="/interfaces/data_product_hub/discovery/image%20(30).png" alt="DPH" style="width:20rem; border: 1px solid black;" />
  <figcaption><i>Data Products Page</i></figcaption>
</center>


A preview of the Data Products is provided by the Data Product Hub on the right-side panel. Clicking on the space next to the relevant Data Products allows for a quick preview.

## Detailed view of the Data Products

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

The 'Inputs' section displays all the datasets that are fed into the Data Product, while the 'Output' section lists the materialized tables that are generated from it. An output does not need to be present for a Data Product, as there can be Data Products that expose models. Only one model is presented by a Data Product at a time, along with its associated metrics. Metrics are not available if the model is not built on top of the Data Product. The 'Access Options' lists all the available consumption options for sharing the Data Product.

#### **Inputs tab**

Within the Inputs Tab, all tables and their schemas that feed into the Data Product, including those sourced from other Data Products, are displayed. For each table, the name of the table, tier, domain, owner, access permission, Uniform Data Link (UDL) address, and the various Data Products the particular table is part of are shown.

Below that, a search bar is provided to enable searching for various columns within the table. Other details of a specific column, such as data type, description, tags, and glossary terms, can also be viewed.

Additionally, a specific table can be opened within Metis, the DataOS catalog, to get comprehensive metadata of that table, or in the Workbench App for exploratory analysis using SQL.

<center>
  <img src="/interfaces/data_product_hub/annotely_image%20(6)%20(1).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
  <figcaption><i>Inputs Tab</i></figcaption>
</center>



To learn more about access permissions, click 'Restricted Access', which will open a right panel as shown below.

<center>
  <img src="/interfaces/data_product_hub/discovery/image%20(31).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
  <figcaption><i>Restricted Access</i></figcaption>
</center>


Information about the filters and policies applied to the input dataset is provided in the restricted access panel, as shown in the above image. If data masking is applied, the panel will indicate which column is masked along with the masking policy type.

#### **Outputs tab**

The materialized tables generated by the Data Product are displayed in the Output Tab, ready for use on their own or for combining with others to create new insights and Data Products. For each table, the name of the table, Tier, Domain, Owner, Access Permission, Uniform Data Link (UDL) Address, and the various Data Products the particular table is part of are shown.

Below that, a search bar is provided to enable searching for various columns within the table. Other details of a specific column, such as Data Type, Description, Tags, and Glossary Terms, can also be viewed.

Additionally, a specific table can be opened within Metis, the DataOS Catalog, to get comprehensive metadata of that table, or in the Workbench App for exploratory analysis using SQL.

<center>
  <img src="/interfaces/data_product_hub/discovery/annotely_image%20(7)%20(2).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
  <figcaption><i>Outputs Tab</i></figcaption>
</center>

#### **Model tab**

A data model, representing the Lens model built on top of the Data Product, is displayed in the Model tab, shaping the data into meaningful insights for easier analysis and understanding.

<center>
  <img src="/interfaces/data_product_hub/discovery/annotely_image%20(8)%20(1).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
  <figcaption><i>Model Tab</i></figcaption>
</center>


#### **Metrics tab**

Key business metrics derived from the Lens models can be explored in the Metrics tab to observe performance and make data-driven decisions with ease.


<aside class="callout">

🗣 If no model is exposed by the Data Product, the Metric tab will not be available.

</aside>

- In the image below, a metric 'Cloud Service Cost' is shown along with its description and the number of measures, dimensions, and segments used to derive the metric. By clicking on the quick insights or explore link, the metrics can be further explored.

    <center>
    <img src="/interfaces/data_product_hub/discovery/annotely_image%20(10)%20(1).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    <figcaption><i>Quick Insights and Explore</i></figcaption>
    </center>

    

- Below, the references section is shown, which displays the lineage, including the flow and the dataset from which the metric is derived.

    <center>
    <img src="/interfaces/data_product_hub/discovery/annotely_image%20(11)%20(1).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    <figcaption><i>References</i></figcaption>
    </center>

    
- The measures and dimensions sections provide details of each dimension and measure used to derive the metric, including the name, data type, description, and alias.

    <center>
    <img src="/interfaces/data_product_hub/discovery/annotely_image%20(12)%20(1).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    <figcaption><i>Measures and Dimensions</i></figcaption>
    </center>


    

#### **Data APIs tab**

API endpoints for developing data applications can be explored in the Data APIs tab.

<aside class="callout">

🗣 If no APIs are built on top of a Data Product, the Data API tab will not be available.

</aside>

- On the Data APIs tab, all API endpoint collections are listed. By clicking on a particular endpoint, a short description of the API collection is displayed, as shown below.
    
    <center>
    <img src="/interfaces/data_product_hub/discovery/annotely_image%20(13)%20(1).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    <figcaption><i>API Endpoint Collections</i></figcaption>
    </center>

    
- The OpenAPI specifications and Postman collection for each endpoint can be downloaded by clicking on **Download OpenAPI Spec** and **Download Postman Collection**, respectively.

    <center>
    <img src="/interfaces/data_product_hub/discovery/annotely_image%20(15)%20(1).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    <figcaption><i>Download OpenAPI spec and Postman collection</i></figcaption>
    </center>

    
- After downloading the OpenAPI spec and Postman collection, open the Postman application to proceed further.

    <center>
    <img src="/interfaces/data_product_hub/discovery/image%20(32).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    <figcaption><i>Postman Application</i></figcaption>
    </center>

 
    
- Navigate to collections in Postman, click on import, and select the files option to choose the downloaded JSON file.

    <center>
    <img src="/interfaces/data_product_hub/discovery/annotely_image%20(17)%20(1).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    <figcaption><i>Import collection</i></figcaption>
    </center>

    
- The **View complete documentation** link will open the OpenAPI documentation, as shown below.
    
    <center>
    <img src="/interfaces/data_product_hub/discovery/annotely_image%20(18)%20(1).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    <figcaption><i>View Complete Documentation</i></figcaption>
    </center>


    
- To hit the API endpoint in Postman, click on the 'Open request' link, as shown in the above image, which will open the interface below.
    
    <center>
    <img src="/interfaces/data_product_hub/discovery/image%20(33).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    <figcaption><i>Open Request</i></figcaption>
    </center>

    
- Hover over the `{{baseUrl}}`, and copy the base URL.

    <center>
    <img src="/interfaces/data_product_hub/discovery/image%20(34).png" alt="DPH" style="width:55rem; border: 1px solid black;" />
    <figcaption><i>Copy the Base URL</i></figcaption>
    </center>
    
    
- Paste the copied URL in place of {{baseUrl}}, provide the DataOS API key as a bearer token, and click on send to access the data, as shown below. This API endpoint, along with the bearer token, can be used to build your data application.
    
    <center>
    <img src="/interfaces/data_product_hub/discovery/annotely_image%20(19)%20(1).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    <figcaption><i>Paste the copied URL</i></figcaption>
    </center>

    
- On the Data APIs tab, clicking on a particular API endpoint will display information about who has access to the endpoint, the endpoint's description, authorization details, response details, and response samples.
    
    <center>
    <img src="/interfaces/data_product_hub/discovery/annotely_image%20(20)%20(1).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    <figcaption><i>API Endpoint Access</i></figcaption>
    </center>

    
- **Authorizations - bearerToken** indicates that the API requires an authorization token, specifically a **Bearer Token** for authentication. A **Bearer Token** is a type of token that must be included in the HTTP header when making requests to the API. The format of the token is **JWT** (JSON Web Token), which is a compact, URL-safe means of representing claims to be transferred between two parties.


    <center>
    <img src="/interfaces/data_product_hub/discovery/image%20(35).png" alt="DPH" style="width:20rem; border: 1px solid black;" />
    <figcaption><i>Authorization</i></figcaption>
    </center>
    
    
- In the **Responses section**, a **200 response** indicates that the request was successful, and the API is returning data as expected. The response schema is in **application/json** format, meaning the data will be returned in JSON format. The response schema defines the structure of the data returned when the API responds with a **200 (OK)** status.

    
    <center>
    <img src="/interfaces/data_product_hub/discovery/image%20(36).png" alt="DPH" style="width:20rem; border: 1px solid black;" />
    <figcaption><i>Response section</i></figcaption>
    </center>

    
    In this case, the API returns the following fields:

    - **total_revenue (string)**: This field provides the total revenue generated by the brand. The value is expected to be a string, even though it represents financial information. The description indicates that this data provides insight into the financial performance of the brand.

    - **brand (string)**: This field contains the name of the brand being analyzed. It represents the company related to the revenue data.

    The **5XX** status code refers to a server-side error. If the API is unable to process the request due to an internal issue or failure, it will return a **5XX** response. This indicates a problem on the server, not with the client's request. Server-side errors generally imply that something unexpected happened on the server while trying to handle the request, and the client cannot resolve these issues without intervention from the server team.

    
- The **Response Samples** section provides an example of what the successful **200** response would look like when calling this API. The sample JSON response shown in the image below contains two fields: **total_revenue** and **brand**. In this sample, both `total_revenue` and `brand` are represented as placeholder strings. In a real response, `total_revenue` will be a string representing the revenue (e.g., `"10000 USD"`), and `brand` will be the actual brand name (e.g., `"Nike"`).

    
    <center>
    <img src="/interfaces/data_product_hub/discovery/image%20(37).png" alt="DPH" style="width:20rem; border: 1px solid black;" />
    <figcaption><i>Response Samples</i></figcaption>
    </center>
    
    **GET /top_brand_list** is the **API endpoint** that is called using the HTTP `GET` method. It retrieves data related to a list of top brands. Typically, `GET` methods are used to retrieve data from a server without modifying it.

    

#### **Quality tab**

The **Quality tab** provides insights into the health and quality of input and output data, allowing for monitoring and ensuring that the data meets expected standards across several quality checks.

Quality is categorized into six types: Schema, Freshness, Validity, Completeness, Uniqueness, and Accuracy.


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



- In the image below, aspects such as completeness, schema validation, uniqueness, and accuracy are tracked.
    

    <center>
    <img src="/interfaces/data_product_hub/discovery/annotely_image%20(21)%20(1).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    <figcaption><i>Quality Tab</i></figcaption>
    </center>


    
- In the above image, the data shows 100% completeness, ensuring that essential fields do not contain missing or null values.


- The trend chart displays completeness over time. The y-axis represents completeness as a percentage (0-100%), while the x-axis represents the timeline. In this case, the chart indicates consistent **100% completeness** for the period shown (up to September 13th), meaning no data was missing.

    
    <center>
    <img src="/interfaces/data_product_hub/discovery/image%20(38).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    <figcaption><i>Trend chart</i></figcaption>
    </center>

    
- Below, you can see the applied checks and their status. In this case, for the `f_sales` dataset, the completeness check focuses on ensuring that critical columns are fully populated. The `f_sales_invoice_no_completeness_of_the_invoice_number_column` check ensures that the `invoice_number` column in the `f_sales` dataset does not have missing or null values. A green checkmark (✔) indicates that the check has passed successfully. In this case, there are no missing invoice numbers, and the dataset is 100% complete in this aspect.


    <center>
    <img src="/interfaces/data_product_hub/discovery/image%20(39).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    <figcaption><i>Applied Checks and their status</i></figcaption>
    </center>

    

#### **Access options tab**

The **Access options** tab allows users to connect their Data Products to various [BI (Business Intelligence)](/interfaces/data_product_hub/#bi-sync), [AI and ML](/interfaces/data_product_hub/#aiml), [app development](/interfaces/data_product_hub/#app-development), and [Data API](/interfaces/data_product_hub/#data-apis) tools such as Power BI, Excel, Tableau, Apache Superset, and Jupyter Notebook.


<center>
<img src="/interfaces/data_product_hub/discovery/annotely_image%20(22)%20(1).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
<figcaption><i>Access Options Tab</i></figcaption>
</center>


To know more about access options, please [refer to this section](/interfaces/data_product_hub/discovery/#access-options-tab). 

## **Perspectives**

In the **Perspectives** tab, saved explorations of the Data Products can be accessed as Perspectives.


<center>
<img src="/interfaces/data_product_hub/discovery/image%20(40).png" alt="DPH" style="width:20rem; border: 1px solid black;" />
<figcaption><i>Perspectives Tab</i></figcaption>
</center>



**How to create a Perspective?**

Follow the steps below to save your Data Product exploration as a Perspective, allowing you to access it later in the **Perspective** tab.


1. Choose the Data Product of choice and navigate to the **Explore** button.
 
    
    <center>
    <img src="/interfaces/data_product_hub/discovery/annotely_image%20(23)%20(1).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    <figcaption><i>Choose and Navigate</i></figcaption>
    </center>


    
2. Click the **Explore** tab to begin exploring the Data Product.

    <center>
    <img src="/interfaces/data_product_hub/discovery/image%20(41).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    <figcaption><i>Navigate to Explore Tab</i></figcaption>
    </center>

    
3. After exploration, navigate to the **Save Perspective** button.

    
    <center>
    <img src="/interfaces/data_product_hub/discovery/image%20(42).png" alt="DPH" style="width:20rem; border: 1px solid black;" />
    <figcaption><i>Save Perspective</i></figcaption>
    </center>

4.  Clicking the **Save Perspective** button will open a dialog box prompting users for the name and description of your perspective.

    
    <center>
    <img src="/interfaces/data_product_hub/discovery/image%20(43).png" alt="DPH" style="width:20rem; border: 1px solid black;" />
    <figcaption><i>Dialogue Box</i></figcaption>
    </center>


5. Provide a name and, optionally, a description for the exploration, then click on **Save**.

    
    <center>
    <img src="/interfaces/data_product_hub/discovery/image%20(44).png" alt="DPH" style="width:20rem; border: 1px solid black;" />
    <figcaption><i>Save</i></figcaption>
    </center>



**How to access the Perspectives?**

After saving the exploration as a perspective, follow the steps below to access it later in the **Perspective** tab.

1. Navigate to the **Perspectives** tab, where all perspectives are accessible by name, tags, data product, and owner.

    
    <center>
    <img src="/interfaces/data_product_hub/discovery/image%20(45).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    <figcaption><i>Navigate to Perspectives Tab</i></figcaption>
    </center>


2. In the search bar, perspectives can be directly searched by name or keywords used in the name.

    
    <center>
    <img src="/interfaces/data_product_hub/discovery/image%20(46).png" alt="DPH" style="width:20rem; border: 1px solid black;" />
    <figcaption><i>Search</i></figcaption>
    </center>


3. Perspectives can be filtered by owners. Navigate to the **Filters** dropdown, click on the **Owner** option, and select the owner of choice.

    
    <center>
    <img src="/interfaces/data_product_hub/discovery/image%20(47).png" alt="DPH" style="width:20rem; border: 1px solid black;" />
    <figcaption><i>Filter</i></figcaption>
    </center>



4. Similarly, perspectives can be filtered by **Data Products** and **Tags**, just as with **Owner**.


    <center>
    <img src="/interfaces/data_product_hub/discovery/annotely_image%20(25)%20(1).png" alt="DPH" style="width:20rem; border: 1px solid black;" />
    <figcaption><i>Filter using 'Data Products'</i></figcaption>
    </center>
    


    <center>
    <img src="/interfaces/data_product_hub/discovery/annotely_image%20(24)%20(1).png" alt="DPH" style="width:20rem; border: 1px solid black;" />
    <figcaption><i>Filter using 'Tags'</i></figcaption>
    </center>

    
    
5. For example, selecting the **corp-market-performance** Data Product in the filters options will list all the Perspectives created for that Data Product, as shown below.

    
    <center>
    <img src="/interfaces/data_product_hub/discovery/annotely_image%20(26)%20(1).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    <figcaption><i>List Perspectives</i></figcaption>
    </center>


    
6. Clicking on any Perspective will redirect you to the explore page of the Data Product for which the particular Perspective is created, as shown below, allowing you to continue your exploration.


    <center>
    <img src="/interfaces/data_product_hub/discovery/image%20(48).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    <figcaption><i>Explore</i></figcaption>
    </center>
    


## **Metrics**

In the **Metrics** tab, key insights of the Data Products can be accessed to gather information, assess operations, and make quick, informed business decisions. To explore the **Metrics** tab, navigate to it, and a short description will be displayed. By default, all metrics are displayed grouped by use cases.


<aside class="callout">

🗣 A metric is an entity that, by default, provides a logical view of the logical table, containing only one measure and a time dimension.

</aside>

<center>
<img src="/interfaces/data_product_hub/discovery/image%20(49).png" alt="DPH" style="width:20rem; border: 1px solid black;" />
<figcaption><i>Metrics Tab</i></figcaption>
</center>


<center>
<img src="/interfaces/data_product_hub/discovery/image%20(50).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
<figcaption><i>Metrics Listing Page</i></figcaption>
</center>


**Search the Metrics by keyword**

Metrics of interest can be directly searched in the search bar by entering the name or keyword used in the metric name, as shown below.


<center>
<img src="/interfaces/data_product_hub/discovery/image%20(51).png" alt="DPH" style="width:20rem; border: 1px solid black;" />
<figcaption><i>Search the metrics by keyword</i></figcaption>
</center>


**Filter the Metrics**

Metrics can be filtered by a particular owner by navigating to the **Filter** dropdown, clicking on **Owners**, and selecting the desired owner.
 

<center>
<img src="/interfaces/data_product_hub/discovery/image%20(52).png" alt="DPH" style="width:20rem; border: 1px solid black;" />
<figcaption><i>Filter the metrics</i></figcaption>
</center>


**Metrics recommendations based on domains**

By default, the **Metrics** tab recommends metrics grouped by use cases. To get metric recommendations based on the domain, navigate to the **Use-case** dropdown, select the **Domain** option, and the metrics will be grouped by domains.

<center>
<img src="/interfaces/data_product_hub/discovery/image%20(53).png" alt="DPH" style="width:20rem; border: 1px solid black;" />
<figcaption><i>Metrics recommendations based on domains</i></figcaption>
</center>

