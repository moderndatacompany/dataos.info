# Building an application with Appsmith

This guide walks you through creating a simple Appsmith application to consume a DataOS data product. Let's get started and transform your data into interactive and insightful visualizations!

## **What do you need to get started?**

1. Ensure your data product is created and the semantic model is configured before starting application development. For this demonstration, we are using the Product Affinity data product. Once completed, the following access options will be available.
    
    ![access_options.png](/learn/dp_consumer_learn_track/apps_consume_data_products/build_app_appsmith/access_options.png)
    
2. To access your data over HTTP using `curl`, refer to [this](/learn/dp_consumer_learn_track/explore_sm/#using-curl) link.

## Using cURL for requests

Using cURL to connect with Appsmith allows you to quickly import API requests directly from the command line. This method is useful for users who have pre-existing cURL commands and want to seamlessly integrate them into their Appsmith applications.

### **Step 1: Log in and set up your workspace**

1. Log in to Appsmith to access your home screen. You’ll find an existing workspace or create one if it’s your first time.
2. In your workspace, click the "Create New" button at the top right.
    
    ![image](/learn/dp_consumer_learn_track/apps_consume_data_products/build_app_appsmith/deepakapp.png)
    

### **Step 2: Start creating your application**

1. Select "Application" to create a new application. You can either choose a template or start from scratch.
2. Once selected, you’ll land on the editor page where you’ll design and develop your application.
    
    ![image](/learn/dp_consumer_learn_track/apps_consume_data_products/build_app_appsmith/image.png)
    

### **Step 3: Import and configure your API**

1. Navigate to the Queries section, then choose "Import via cURL" from Quick Actions.
    
    ![image](/learn/dp_consumer_learn_track/apps_consume_data_products/build_app_appsmith/curl_import.png)
    
2. Paste the cURL command obtained. Ensure the API key is added in the command.
    
    ![import_from_curl_option.png](/learn/dp_consumer_learn_track/apps_consume_data_products/build_app_appsmith/import_from_curl_option.png)
    
3. Validate the query by running it and renaming it for easy identification during UI binding.
    
    ![curl_validate.png](/learn/dp_consumer_learn_track/apps_consume_data_products/build_app_appsmith/curl_validate.png)
    

### **Step 4: Build your user interface**

1. Switch to the **UI tab** and start designing your app by dragging and dropping UI elements (like charts, tables, etc.) onto the canvas.
    
    ![/learn/dp_consumer_learn_track/apps_consume_data_products/build_app_appsmith/image%201.png](/learn/dp_consumer_learn_track/apps_consume_data_products/build_app_appsmith/image_1.png)
    
2. Select widgets and configure them based on your visualization needs.
    
    ![drag_widget.png](/learn/dp_consumer_learn_track/apps_consume_data_products/build_app_appsmith/drag_widget.png)
    

### **Step 5: Bind your data to the UI**

1. Connect your UI elements to the query you created earlier by selecting its name.
2. Your data will populate the visualization in real time.
3. A right-side panel will open where you can edit the JavaScript settings as needed
4. Add more visualizations as needed for your use case. Experiment with different types and use Appsmith’s features to enhance and refine your app.
    
    ![image](/learn/dp_consumer_learn_track/apps_consume_data_products/build_app_appsmith/pie.png)
    

### **Step 6: Deploy your application**

1. Once your application is complete, click the 'Deploy' button in the top-right corner.
    
    ![image](/learn/dp_consumer_learn_track/apps_consume_data_products/build_app_appsmith/dashboard.png)
    
2. Your deployed application will look something like this: 
    
    ![dashboard_published.jpeg](/learn/dp_consumer_learn_track/apps_consume_data_products/build_app_appsmith/dashboard_published.jpeg)
    

## Querying via Postgres

### **Step 1: Log in and set up your workspace**

**Log in to Appsmith** to access your home screen. You’ll find an existing workspace or create one if it’s your first time. In your workspace, click the 'Create New' button at the top right.
    
![image](/learn/dp_consumer_learn_track/apps_consume_data_products/build_app_appsmith/deepakapp.png)
    

### Step 2: Start creating your application

1. Select 'Application' to create a new application. You can either choose a template or start from scratch. 
    
    ![create_ne_app_options.png](/learn/dp_consumer_learn_track/apps_consume_data_products/build_app_appsmith/create_ne_app_options.png)
    
2. Once selected, you’ll land on the **editor page** where you’ll design and develop your application.
    
    ![/learn/dp_consumer_learn_track/apps_consume_data_products/build_app_appsmith/image.png](/learn/dp_consumer_learn_track/apps_consume_data_products/build_app_appsmith/image.png)
    

### **Step 3: Configure your source**

1. Navigate to the **Query** tab. Click on the **+** button to add a new data source.
    
    ![query_tab.png](/learn/dp_consumer_learn_track/apps_consume_data_products/build_app_appsmith/query_tab.png)
    

2. Select **PostgreSQL** as your data source.

    ![connect_datasource.png](/learn/dp_consumer_learn_track/apps_consume_data_products/build_app_appsmith/connect_datasource.png)

3. You will see the follwoing screen. Click on ‘Edit Configurations’ to provide the datasource connection details.
    
    ![untitled_ds.png](/learn/dp_consumer_learn_track/apps_consume_data_products/build_app_appsmith/untitled_ds.png)
    
4. Enter your credentials and click **Save**. 
    
    ![authentication.png](/learn/dp_consumer_learn_track/apps_consume_data_products/build_app_appsmith/authentication.png)
    
    > You can customize the data source name to better reflect its purpose or enhance clarity.
    > 

### **Step 4: Write your query to fetch data**

1. After the source is created, you'll see the screen below. Click on **New Query** to start building your query.
    
    ![create_new_query.png](/learn/dp_consumer_learn_track/apps_consume_data_products/build_app_appsmith/create_new_query.png)

2. Add your query and run it. Make sure to rename it for future reference.
    
    ![query_result.png](/learn/dp_consumer_learn_track/apps_consume_data_products/build_app_appsmith/query_result.png)
    

### **Step 5: Start designing your application**

Once you are able to fetch your data, you can create visualizations and dashboards as per requirements.

Follow the steps 4-6 given in the [Via Curl](/learn/dp_consumer_learn_track/apps_consume_data_products/build_app_appsmith/#via-curl) section.

## Using GraphQL for queries

### **Step 1: Log in and set up your workspace**

1. **Log in to Appsmith** to access your home screen. You’ll find an existing workspace or create one if it’s your first time.
2. In your workspace, click the 'Create New' button at the top right.
    
    ![image](/learn/dp_consumer_learn_track/apps_consume_data_products/build_app_appsmith/deepakapp.png)
    

### **Step 2: Start creating your application**

1. Select 'Application' to create a new application. You can either choose a template or start from scratch.
    
    ![create_ne_app_options.png](/learn/dp_consumer_learn_track/apps_consume_data_products/build_app_appsmith/create_ne_app_options%201.png)
    
2. Once selected, you’ll land on the **editor page** where you’ll design and develop your application.
    
    ![image.png](/learn/dp_consumer_learn_track/apps_consume_data_products/build_app_appsmith/image.png)
    

### **Step 3: Navigate to the Queries tab**

For adding GraphQL connection and building with GraphQL queries, go to the **Queries** tab in your application.

![add_new_datasource.png](/learn/dp_consumer_learn_track/apps_consume_data_products/build_app_appsmith/add_new_datasource.png)

### **Step 4: Configure the GraphQL connection**

1. From the **Quick Actions** menu, select **GraphQL API**.
2. The next screen will appear. Click **Authentication** to proceed.
    
    ![auth_option.png](/learn/dp_consumer_learn_track/apps_consume_data_products/build_app_appsmith/auth_option.png)
    
3. Add the GraphQL URL and click **Save URL** to access authentication settings. you will see the screen below. Select **Bearer Token** as the authentication type, and provide your API Key in the Bearer Token field. Click **Save** to confirm.

![edit_configuration.png](/learn/dp_consumer_learn_track/apps_consume_data_products/build_app_appsmith/edit_configuration.png)

### **Step 5: Add your GraphQL query**

You will see the screen below. 

1. Navigate to the **Body** section and enter your GraphQL query.
2. Click **Run** to validate the response.
3. Once validated, give the query a memorable name for future reference.
    
    ![graphql_query.png](/learn/dp_consumer_learn_track/apps_consume_data_products/build_app_appsmith/graphql_query.png)
    

### **Step 6: Start designing your application**

Once you are able to fetch your data, you can create visualizations and dashboards as per requirements.

Follow the steps 4-6 given in the [Via Curl](/learn/dp_consumer_learn_track/apps_consume_data_products/build_app_appsmith/#via-curl) section.