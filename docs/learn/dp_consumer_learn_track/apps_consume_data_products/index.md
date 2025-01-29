# Custom applications to consume Data Products

This topic discusses several ways DataOS enables users to consume data products—through applications built using Streamlit, Appsmith, etc., leveraging REST APIs, GraphQL, and LLM capabilities. You can develop and deploy custom applications to consume data products. Whether you're building dashboards, analytical tools, or specialized business applications, DataOS makes it easy to integrate and access these applications.

## Streamlit applications

One popular way to consume your data product is by building a Streamlit application powered by the DataOS REST API.

Here is the sample Streamlit application built which is powered by the example data product.

### **Deploying Streamlit application on DataOS**

Once your Streamlit application is built, you can deploy it on DataOS and can access it through DataOS home.

![pa_app_dataos_home.png](/learn/dp_consumer_learn_track/apps_consume_data_products/pa_app_dataos_home.png)

Refer to the following quick guide for the step by step process.

[Deploying Data Applications on DataOS](/quick_guides/deploy_data_app_using_container_stack/)

### **API-fetched data**

This example Streamlit application securely fetches data through APIs, ensuring a smooth integration within the DataOS ecosystem. With built-in governance features, data access policies, and security controls, you can trust that your data remains protected and compliant.

<div style="text-align: left; padding-left: 1em;">
<img src="/learn/dp_consumer_learn_track/apps_consume_data_products/api_fetched_data.png" alt="image" style="max-width: 50%; height: auto; border: 1px solid #000;">
</div>

<!-- ![api_fetched_data.png](/learn/dp_consumer_learn_track/apps_consume_data_products/api_fetched_data.png) -->

<aside class="callout">
🗣 Any data masked in DataOS will remain masked when accessed through the Streamlit application or any other application. Governance policies, including data access controls and masking rules, are automatically enforced to ensure compliance and data security.

</aside>

### **Interactive dashboard**

You can create interactive dashboards with the data as shown for the example Streamlit application. It provides insightful visualizations and analytics to help users explore data effectively. 

Users can analyze individual customer data using the available options in the application’s UI. The application allows for filtering, searching, and drilling down into specific customer records to gain deeper insights.

<div style="text-align: left; padding-left: 1em;">
<img src="/learn/dp_consumer_learn_track/apps_consume_data_products/dashboard.png" alt="image" style="max-width: 50%; height: auto; border: 1px solid #000;">
</div>

<!-- ![dashboard.png](/learn/dp_consumer_learn_track/apps_consume_data_products/dashboard.png) -->

## Appsmith applications

Similarly, you can build custom applications using Appsmith. DataOS supports integration with REST APIs, PostgreSQL, and GraphQL for effortless data connectivity and application development. A sample Appsmith application powered by the example data product has been built.

![image.png](/learn/dp_consumer_learn_track/apps_consume_data_products/image.png)

### **Building application with Appsmith** 

Appsmith provides a low-code development platform to create feature-rich applications quickly. Using its drag-and-drop interface, you can build interactive dashboards, forms, and workflows with seamless connectivity to your data products within DataOS.

[Building an application with Appsmith](/learn/dp_consumer_learn_track/apps_consume_data_products/build_app_appsmith/)

## Sophos- LLM application

Sophos is an advanced application that seamlessly integrates LLM (Large Language Model) capabilities, offering a powerful natural language interface to query your data product's semantic model. With Sophos, users can interact with their Data Product using simple, conversational queries without needing to write complex SQL or GraphQL statements. The LLM-powered interface understands user intent, context, and data relationships and provides accurate and meaningful responses.

By leveraging Sophos, both technical and non-technical users can unlock the full potential of their data products, enhancing productivity and decision-making.

### **Accessing Sophos**

Log in to your DataOS instance and navigate to the **Sophos** application from the home page.

![dataos_sophos.png](/learn/dp_consumer_learn_track/apps_consume_data_products/dataos_sophos.png)

The following examples demonstrate the LLM system for natural language interactions with the data. 

![sophos_home.png](/learn/dp_consumer_learn_track/apps_consume_data_products/sophos_home.png)

### **Exploring Data Product**

Click on ‘Explore DP’. The follwoing screen will appear.

You will get the option to enter your query. Enter the query in natural language and click on ‘Submit’. 

**Examples**

The following examples demonstrate the LLM system for natural language interactions with the data.

1. suppose you want to know how purchase frequesncy of customers for each product correlate with customer segments. Sophos will first validate the query, and if valid, it will execute the query and display the result.
    
    ![purchase.png](/learn/dp_consumer_learn_track/apps_consume_data_products/purchase.png)
    
2. You can get insights into the most frequently bought products, helping businesses identify popular items and customer preferences.
    
    ![most_freq_bought_prods.png](/learn/dp_consumer_learn_track/apps_consume_data_products/most_freq_bought_prods.png)
    

### **Handling invalid queries**

If an invalid query is entered, Sophos will not only provide a reason why the query is invalid but also suggest probable questions based on the text entered. This feature helps users refine their queries and obtain accurate results.

By leveraging the capabilities of Sophos, businesses can explore their data product effectively and make informed decisions.

![invalid_query.png](/learn/dp_consumer_learn_track/apps_consume_data_products/invalid_query.png)

