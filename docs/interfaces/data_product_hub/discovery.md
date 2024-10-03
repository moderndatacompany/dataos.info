# Data Product Discovery

Discovering data among thousands of datasets is hard without rich metadata and faceted search. The Data Product Hub serves as a single data product catalog that aggregates metadata about all data products and presents the right information to users depending on their needs. Data Product Hub aims to help **data consumers** make timely decisions with the right data.

Data Product Hub provides a user-friendly interface for D**ata Product discovery**. Data Product Hub enables you to discover your data using a variety of strategies, including keyword searches, filters, etc.

![                                                                  *Data Product Hub Interface*](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/62163047-cf17-42a9-900f-d05c20af54b3/image.png)

                                                                  *Data Product Hub Interface*

# How to discover Data Products of Interest

Data Product Hub simplifies the Data Product discovery with the following strategies.

## **Keyword Search**

Search is at the front and center of Data Product Hub and is available in the top right menu bar across the Data Products page. 

A simple yet powerful way to find data products is by typing the name, description, or owner from the search interface. By default, The search will display matching data products grouped by use cases. The Data Product’s name can be human-readable or a unique identifier.

![annotely_image (1).png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/85c5c107-53bc-4f8b-b7e9-f397bfa47693/b487a7e1-15d6-4570-a493-0a991629edec.png)

## **Filters**

Multiple filter options further help narrow the search by using parameters **Tier**, **Domain**, and **Owner**. 

- **Tier:** Illustrates how the data product is organized, whether it follows a medallion architecture, is source-aligned, or is structured around specific entities or consumer needs.
- **Domain:** The specific business domain to which the data product belongs. You can select multiple domains at once to filter out the Data Product of your choice.
- **Owner:** A user can own a Data Product in the Data Product Hub. Users can filter Data Products by the owner. With information on the Data Product owners, you can direct your questions to the right person or team. The owner's DataOS User ID is used to list the various owners in the Owner dropdown. You can select only a single owner at a time.
    
    ![annotely_image (2).png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/31281ac0-2979-4153-a71e-f8507952d764/3d88cabe-189a-47dc-bcec-5fe90512c361.png)
    

## Categorize by Domain

The search results by default are categorized by use cases. Users can also categorize them by domains.

![annotely_image (3).png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/382c977e-373d-49f6-9dce-0d039657cfed/2cc7b5ce-2afe-4ae5-9e70-4d63e3679db7.png)

## Recently searched Data Products

You can find recently searched Data Products in the 'Recent' tab, as illustrated below. Note that clearing the cache will remove all recently searched Data Products from the 'Recent' tab.

![annotely_image (31).png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/1176d9b1-6bf3-4f2b-affc-1297dd8e425e/annotely_image_(31).png)

## Favorites

In the ‘Favorites’ tab, you can find all the starred Data Products.

![annotely_image (32).png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/f8ef41ef-ba37-4048-aada-e0dfb35aad6e/annotely_image_(32).png)

# Get a Quick Glance of the Data Products

For each of the Data Products displayed on the Data Products page, some basic information is displayed on the Data Product card. Users can view the **Name of the Data Product, Description,  Tier, and Domain** information for each data product, while each data product is categorized by **Use case.**

![*Basic information about a Data Product*](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/2e5e0a22-a3b4-4ddd-8bcb-4edebd156338/image.png)

*Basic information about a Data Product*

Data Product Hub provides a detailed preview of the data asset on the right side panel. Just click on the space next to the relevant data asset to get a quick preview.

# Detailed View of the Data Products

## Top Panel

The data product details page displays the **Domain**, **Name of the Data Product**, **Description, Git Repository link, JIRA link, Tier, Use-case, and Owner** on the top panel.

Along with that, it showcases a button displaying conformation with defined **Accuracy, Completeness, Freshness, Schema, Uniqueness,** and **Validity** constraints.

![annotely_image (4).png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/8012cd15-71cd-4996-9545-2e34709fc006/07df92c2-73ac-4039-be3b-805aa0432443.png)

## **Other Details in the top panel**

On the top right of the data product details page, we can view details on:

- **Add to Favorite:** On clicking the star icon (⭐), users can add the respective data product to Favorites.
- **BI Sync:** Opens the BI Sync functionality which enables you to sync the data product to PowerBI, Tableau Cloud, Tableau Desktop, and Apache Superset.
- **AI and ML:** Enables you to consume the data product in Jupyter Notebooks to power your AI and ML use cases.
- **App Development:** Enables you to sync the data product using REST and GraphQL APIs to power your data applications
- **Data API:** Enables you to create Data APIs on top of your data product.
- **Explore:** Explore opens the Data Product for further exploration.

![*Other details in the top panel of Data Product details*](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/6c0f9188-3526-4adb-8aa1-5a7648c6b6fc/image.png)

*Other details in the top panel of Data Product details*

## **Data Product tabs**

There are separate tabs each for Overview, Inputs, Outputs, Model, Metrics, Data APIs, Quality, and Access Options based on the respective data asset selected. Let's take a look at each of the tabs.

| **Tabs** | **Description** |
| --- | --- |
| **Overview** | Displays a visual snapshot of the data product, from inputs to outputs, including the semantic model. |
| **Inputs** | Lists all tables and schemas feeding into the data product with metadata and search functionality. |
| **Outputs** | Shows the tables generated by the data product, with metadata and search options for further analysis. |
| **Model** | Displays the semantic model, transforming inputs into insights for easier analysis. |
| **Metrics** | Allows exploration of key business metrics derived from the data product's lens models. |
| **Data APIs** | Lists available API endpoints for building data applications, with detailed descriptions and access info. |
| **Quality** | Provides insights into data quality checks, including completeness, freshness, and accuracy trends. |
| **Access Options** | Offers connection options to BI, AI, ML, and app development tools like Power BI, Excel, and Jupyter Notebook. |

### Overview tab

The Overview Tab will display the visual snapshot of your Data Product's work: from input to output, including the semantic model, metrics, and access options.

![annotely_image (5).png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/ca3a21e5-b629-49ba-bcc5-eb976063d3cf/5e09eef7-d665-470c-bd63-ff35e74a0305.png)

The ‘Inputs’ section displays all the datasets fed into the Data Product, while the ‘Output’ section lists the materialized tables generated from it. A Data Product doesn't need to have output, there can be a Data Product that exposes models. A Data Product presents only one model at a time, along with its associated metrics. Metrics are unavailable if the model is not built on top of the Data Product. The ‘Access Options’, list all the available consumption options to share the Data Product.

### Inputs tab

Within the Inputs Tab, you will find all the tables and their schemas that feed into the data product, including those sourced from other data products. For each table you will see the Name of the Table, Tier, Domain, Owner, Access Permission, Uniform Data Link (UDL) Address, and the various data products the particular table is part of.

Below that you will find a search bar that enables you to search various columns with the table, you can also see other details of a specific column such as Data Type, Description, Tags, and Glossary Terms.

In addition to that you can open up a specific table within Metis, the DataOS Catalog to get comprehensive metadata of that table, as well as in the Workbench App for exploratory analysis using SQL.

![annotely_image (6).png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/2574c991-1163-4eb8-bd9f-32e730eb3a64/annotely_image_(6).png)

To know more about the access permissions, click on ‘Restricted Access’, which will open a right panel as shown below.

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/9cea7532-3a08-456f-a5e0-d5684f6d0270/image.png)

The restricted access panel will give information about the filters and the policies applied to the input dataset as shown in the above image, if data masking is applied then it will show which column is masked along with the masking type. 

### Outputs tab

The Output Tab displays the materialized tables generated by the Data Product, ready to be used on their own or combined with others to create new insights and Data Products. For each table you will see the Name of the Table, Tier, Domain, Owner, Access Permission, Uniform Data Link (UDL) Address, and the various Data Products the particular table is part of.

Below that you will find a search bar that enables you to search various columns with the table, you can also see other details of a specific column such as Data Type, Description, Tags, and Glossary Terms.

In addition to that you can open up a specific table within Metis, the DataOS Catalog to get comprehensive metadata of that table, as well as in the Workbench App for exploratory analysis using SQL.

![annotely_image (7).png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/e44304b9-a9f9-492b-909b-036aaafc4175/3b723e80-1c11-4818-bb2d-d976c4449746.png)

### **Model tab**

The Model tab displays a logical model, a representation of the Lens model built on top of the Data Product, shaping the data into meaningful insights for easier analysis and understanding.

![annotely_image (8).png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/94f1aef3-b042-4916-8f54-ae1d3eca80ce/af34e71a-2bc5-412c-a7da-b26c6cde6fc4.png)

### Metrics tab

In the Metrics tab, you can explore the key business metrics derived from the lens models to observe the performance and make data-driven decisions with ease. 

<aside>
🗣

If a Data Product does not have any metrics built on top of it, the Metric tab will not be available.

</aside>

- In the image below, you can see a metric ‘Cloud Service Cost’ with its description and the number of measures, dimensions, and segments used to derive the metric. By clicking on the **Quick Insights** **Explore** link you can further explore the metrics.
    
    ![annotely_image (10).png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/f301d39c-8af1-4344-b10e-7f7d0626b19b/cb07ef4d-1d7a-4cd4-a0fa-fe7e666e97ff.png)
    

- Below you can see the **References** section that shows the lineage with the flow, from which dataset, the metric is derived.
    
    ![annotely_image (11).png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/b2acd3a9-0ec7-44ef-9851-5487b323e198/09eed56e-df81-418a-acc9-a49dca5b946b.png)
    
- The **Measures** and **Dimensions** section gives details of each dimension and measure used to derive the metric such as name, data type, description, and alias.
    
    ![annotely_image (12).png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/4cdd9ee7-21f1-4494-86f0-ac50272d5d2b/annotely_image_(12).png)
    

### Data APIs tab

In the **Data APIs tab,** you can explore the API endpoints to develop the data applications. 

<aside>
🗣

If a Data Product does not have any APIs built on top of it, the Data API tab will not be available.

</aside>

- On clicking the Data APIs tab, it will list all the API endpoint collections. by clicking on a particular endpoint, you can see a short description of the API collection as shown below.
    
    ![annotely_image (13).png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/e0a8afc9-c4e4-4ddd-806a-00fc72d1a3a1/ad0870ae-5969-4f2c-9c25-22bb2e013950.png)
    
- You can download the OpenAPI specifications and Postman collection for each endpoint by clicking on the **Download OpenAPI Spec** and **Download Postman Collection** respectively.
    
    ![annotely_image (15).png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/71a534d5-c29f-4093-b9b5-0d1d0b517043/annotely_image_(15).png)
    
- After downloading the OpenAPI Spec and Postman Collection, open the Postman application.
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/1a9e9491-471a-42d2-a869-2a974ab75d8d/image.png)
    
- Go to Collections, click on import, and select the files option, in which you have to select the downloaded JSON file.
    
    ![annotely_image (17).png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/3335daa8-1f8a-4bd3-9248-f9e8e1263f4a/annotely_image_(17).png)
    
- On clicking the ‘View complete documentation’ link, it will open an OpenAPI documentation as shown below.
    
    ![annotely_image (18).png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/9caaf3d7-146f-48bd-8a8d-2b32153342b7/annotely_image_(18).png)
    
- To hit the API endpoint on Postman, click on the ‘Open request’ link as shown in the above image, which will open the below interface.
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/ed0ed818-1ae8-45cf-bf55-06b9daf0fb31/image.png)
    
- Hover over the `{{baseUrl}}`, and copy the base URL.
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/5882d0c5-eb00-4746-8dca-e35745d4a623/image.png)
    
- Past the copied URL in place of `{{baseUrl}}`, give your DataOS API key as a bearer token, and click on the send after which you can access the data as shown below. You can use this API endpoint along with the bearer token to build your data application.
    
    ![annotely_image (19).png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/e6588b5e-e004-43c1-9343-744bdb125c2d/annotely_image_(19).png)
    
- Now on the **Data APIs tab**, by clicking on the particular API endpoint you can see who has access to the endpoint, the description of the endpoint, authorization details, response details, and the response samples.
    
    ![annotely_image (20).png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/c4cbb2f7-132c-41bf-838e-c3a8bbf4481f/annotely_image_(20).png)
    
- **Authorizations - bearerToken** indicates that the API requires an authorization token, specifically a **Bearer Token** for authentication. **Bearer Token** is a type of token that must be included in the HTTP header when making requests to the API. The format of the token is **JWT** (JSON Web Token), which is a compact, URL-safe means of representing claims to be transferred between two parties.
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/0587db63-be5e-48b1-a577-5fef974313c5/image.png)
    
- In the **Responses section,** a **200 response** indicates that the request was successful, and the API is returning data as expected. The response schema is in **application/json** format, which means the data will be returned in JSON format. The response schema defines the structure of the data returned when the API responds with a **200 (OK)** status.
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/88e99090-b913-496a-ade7-101aa8f7d402/image.png)
    
    In this case, the API returns the following fields:
    
    - **total_revenue (string)**: This field provides the total revenue generated by the brand. The value is expected to be a string, even though it represents financial information (likely formatted with currency symbols or as a string for other reasons). The description indicates that this data provides insight into the financial performance of the brand.
    - **brand (string)**: This field contains the name of the brand being analyzed. It represents the company related to the revenue data.
    
    The **5XX** status code refers to a server-side error. If the API is unable to process the request due to an internal issue or failure, it will return a 5XX response. This indicates a problem on the server, not with the client's request.
    
- The **Response Samples** section provides a sample of what the successful **200** response would look like when calling this API. The sample JSON response provided in the below image has two fields **total_revenue** and **brand.** In this sample, both `total_revenue` and `brand` are shown as placeholder strings. In a real response, `total_revenue` will be a string representing the revenue (like `"10000 USD"`), and the `brand` will be the actual brand name (like `"Nike"` ).
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/f61dfb27-4e39-4706-b982-a86da273be5e/image.png)
    
    **GET /top_brand_list** is the **API endpoint** that you will call using the HTTP `GET` method. It retrieves data related to a list of top brands. Typically, `GET` methods are used to retrieve data from a server without modifying it.
    

### Quality tab

The **Quality tab** provides insights into the health and quality of your input and output data, allowing you to monitor and ensure that the data meets expected standards across several quality checks. 

Quality is categorized into six types, that is Schema, Freshness, Validity, Completeness, Uniqueness, and Accuracy.

| **Category** | **Description** |
| --- | --- |
| **Freshness** | Reflects how up-to-date and timely the data is. |
| **Schema** | Keep an eye on your data structure, ensuring everything is aligned and consistent. |
| **Validity** | Check that your data follows the expected rules and formats, keeping things on track. |
| **Completeness** | Ensure you have all the data you need, without gaps or missing pieces. |
| **Uniqueness** | Verify that your data stays clean and non-duplicated, providing clear, trustworthy results. |
| **Accuracy** | Confirms that the data correctly represents the real-world values and facts it models. |
- In the image below, it tracks aspects like completeness, schema validation, uniqueness, and accuracy.
    
    ![annotely_image (21).png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/d20589e3-0d72-4831-be18-0ff53bd979ec/annotely_image_(21).png)
    
- In the above image, data have 100% completeness which ensures that essential fields do not contain missing or null values.
- Trend Chart displays the completeness over time. The y-axis represents completeness as a percentage (0-100%), while the x-axis represents the timeline. In this case, the chart indicates a consistent **100% completeness** for the period shown (up to September 13th), meaning no data was missing.
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/fb0083f0-cc84-426b-a605-c74944fe1f8d/image.png)
    
- Below you can see the applied checks and their status. In this case the `f_sales` dataset, the completeness check focuses on ensuring that critical columns are fully populated. `f_sales_invoice_no_completeness_of_the_invoice_number_column` check ensures that the `invoice_number` column in the `f_sales` dataset does not have missing or null values. A green checkmark (✔ ) indicates that the check has passed successfully. In this case, there are no missing invoice numbers, and the dataset is 100% complete in this aspect.
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/dcc6d7a0-5111-4dba-82a4-5255b013e3e6/image.png)
    

### Access Options tab

The **Access Options** tab allows users to connect their Data Products to various [BI (Business Intelligence)](https://www.notion.so/Data-Product-Hub-Documentation-WIP-101c5c1d487680779460eaed43c13518?pvs=21), [AI and ML](https://www.notion.so/Data-Product-Hub-Documentation-WIP-101c5c1d487680779460eaed43c13518?pvs=21), [app development](https://www.notion.so/Data-Product-Hub-Documentation-WIP-101c5c1d487680779460eaed43c13518?pvs=21), and [Data API](https://www.notion.so/Data-Product-Hub-Documentation-WIP-101c5c1d487680779460eaed43c13518?pvs=21) tools like Power BI, Excel, Tableau, Apache Superset, Jupyter Notebook, etc. 

![annotely_image (22).png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/f68e534c-2ddf-429c-ba13-fd8627e22470/annotely_image_(22).png)

To know more about access options, please [refer to this section](https://www.notion.so/Data-Product-Hub-Documentation-WIP-101c5c1d487680779460eaed43c13518?pvs=21). 

## Perspectives tab

In the Perspectives tab, you can access the saved explorations of the Data Products as perspectives.

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/84a209de-de53-4a78-bead-1b2888462baf/image.png)

### How to create a perspective?

Follow the below steps to save your Data Product exploration as a perspective to access it later on the Perspective tab.

1. Choose the Data Product of your choice and navigate to the ‘Explore’ button. 
    
    ![annotely_image (23).png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/21de52f9-2947-4c14-83f3-71249ed83fc6/annotely_image_(23).png)
    
2. Click the ‘Explore’ tab, where you can start exploring the Data Product.
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/b05622f9-8d10-4883-9696-f7a5e5cf217e/image.png)
    
3. After exploration, navigate to the **Save Perspective** button.
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/43a6b436-57c2-47f8-a611-5333539afe52/image.png)
    
4.  On clicking the ‘Saved Perspective’ button, it will open a dialogue box prompting for the name and description of your perspective.
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/d16c5cea-9ff9-4f62-abd2-f4d0629da861/image.png)
    
5. Give your exploration a name and description (optional) and click on ‘Save’.
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/e715c0cc-a759-4cca-92d3-f567508a052b/image.png)
    

### How to access the perspectives?

After saving your exploration as a perspective to access it later on the Perspective tab follow the below steps.

1. Navigate to the ‘Perspectives’ tab, where you can access all the perspectives given by name, tags, data product, and owner. 
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/fc0a92ae-c896-4d82-9eea-2741a9e03981/image.png)
    
2. In the search bar, you can directly search for the perspectives by name or keywords used in a name.
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/a9ddab10-022f-4619-8851-791ee230a09c/image.png)
    
3. You can filter out the perspectives by the owners, navigate to the ‘Filters’ drop-down, click on the ‘Owner’ option, and select the owner of your choice.
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/5d303001-aaf1-4e42-8d7c-7735840cf321/image.png)
    

1. Similarly, as the ‘Owner’, you can filter out the perspectives by the ‘Data Products’ and ‘Tags’. 
    
    ![annotely_image (25).png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/d9b594a0-8b5e-4152-bc28-b4354964b383/annotely_image_(25).png)
    
    ![annotely_image (24).png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/cfb8a98f-6d4e-412a-962a-0604717eb81c/annotely_image_(24).png)
    
2. For example, on selecting the ‘corp-market-performance’ Data Product on the Filters options, it will list out all the perspectives created on that Data Product as shown below. 
    
    ![annotely_image (26).png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/b662847b-85d0-4af2-8411-a4511321c350/annotely_image_(26).png)
    
3. On clicking any perspective it will redirect you to the Explore page of the Data Product on which the particular perspective is created as shown below, where you can continue with your exploration.
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/7cb86795-f168-4b01-bbae-068889c5a7ec/image.png)
    

## Metrics tab

In the Metrics tab, you can access the actionable and reliable key insights of the Data Products to get information, assess operations, and make quick and right decisions for your business. To explore the ‘Metric’ tab, navigate to the Metric tab, and you’ll see a short description on the tab, by default, you’ll be able to see all the metrics grouped by use cases.

<aside>
🗣

A metric is an entity that, by default, provides a logical view of the logical table, containing only one measure and a time dimension.

</aside>

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/3968290c-7285-4a86-8ecc-447031c9d597/image.png)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/c94770ce-52f4-4f37-9703-2a3f122a79b0/image.png)

### Search the metrics by keyword

In the search bar, you can directly search for the potential metrics by keywords, just enter the name or keyword used in the metric name as shown below.

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/14215ff5-a857-4450-8770-3dec70806aec/4eba62d6-0c62-4065-ba07-36843e1a6fc2.png)

### Filter the metrics

You can filter out the metrics by the particular owner, by navigating to the ‘Filter’ drop-down, clicking on the owners, and selecting the owner of your choice   

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/2caf3e04-a7d9-4017-81ef-be02e9a45850/image.png)

### Metrics recommendations based on domains

On navigating to the Metrics tab, by default, it recommends the metrics grouped by use cases, if you want the metrics recommendation based on the domain, simply navigate to the ‘Use-case’ drop-down and select the ‘Domain’ option, now you’ll get the metrics recommendation grouped by domains. 

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/a829ff83-508d-4c34-8044-9e48dfb6fe4e/image.png)