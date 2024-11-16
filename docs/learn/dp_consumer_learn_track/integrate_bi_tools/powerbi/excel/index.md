# Excel via Power BI

This topic introduces the methods to connect with Excel via PowerBI to create visuals and perform analysis.

## Scenario

Use Excel's robust data visualization and analytics capabilities to connect with 'Product 360'. Build real-time, interactive dashboards that provide insights into customer buying patterns and help forecast demand, enabling proactive marketing decisions.

There are two methods to interact  with the Excel via PowerBI

- [Using third party tool -  Analyze in Excel](/learn/dp_consumer_learn_track/integrate_bi_tools/powerbi/excel/#using-analyze-in-excel)

- [Using PowerBI Service Account](/learn/dp_consumer_learn_track/integrate_bi_tools/powerbi/excel/#using-powerbi-service-account)

## Prerequisites

- **Power BI Desktop**: Ensure you have Power BI Desktop installed on your system.
- **Follow the Power BI Integration Steps**: Complete the necessary steps for Power BI integration as outlined in the Power BI guide.

## Using Analyze in Excel

### **Step 1: Install Analyze in Excel plugin in PowerBI**

Visit the [Analyze in Excel for Power BI Desktop](https://www.sqlbi.com/tools/analyze-in-excel-for-power-bi-desktop/) link and follow the instructions to download and install the necessary extension.

### **Step 2: Use the Analyze in Excel Feature**

Once the extension is installed, a new tab labeled "Analyze in Excel" will appear in Power BI Desktop.

![Untitled](/learn/dp_consumer_learn_track/integrate_bi_tools/powerbi/excel/Untitled.png)

### **Step 3: Export to Excel**

Click on the "Analyze in Excel" tab. This action will open Excel and establish a connection to the Power BI dataset or report.

![powerbi.png](/learn/dp_consumer_learn_track/integrate_bi_tools/powerbi/excel/powerbi.png)

### **Step 2: Work in Excel**

In Excel, you can now use PivotTables, charts, and other Excel features to analyze the data coming from Power BI.

![powerbi_excel.png](/learn/dp_consumer_learn_track/integrate_bi_tools/powerbi/excel/powerbi_excel.png)

<aside class="callout">
💡 Ensure that Power BI Desktop remains open while working in Excel, as Power BI acts as the server for the data connection with Excel.

</aside>

## Using PowerBI Service Account

### **Step 1: Publish the Report to Power BI Service**

In the PowerBI, click **Publish**. This action will push the report to your online Power BI service account, making it available for access in the Power BI workspace. Choose the required workspace.

<aside class="callout">
💡 This step requires a valid Power BI service account, as the report will be published to the online service.

</aside>

![powerbi_publish.png](/learn/dp_consumer_learn_track/integrate_bi_tools/powerbi/excel/powerbi_publish.png)

### **Step 2: Confirm Publishing in the Chosen Workspace**

The image below shows the power BI is publishing the semantic model in the chosen workspace.

![powerbi_publishing.png](/learn/dp_consumer_learn_track/integrate_bi_tools/powerbi/excel/powerbi_publishing.png)

### **Step 3: Navigate to Your Workspace**

Once published, go to your **workspace** where the report has been saved. Here it is Demo Testing.

![powerrbi_workspace.png](/learn/dp_consumer_learn_track/integrate_bi_tools/powerbi/excel/powerrbi_workspace.png)

Click on the connected semantic model below the workspace with the name `cross-sell-affinity`.

![powerbi_settings.png](/learn/dp_consumer_learn_track/integrate_bi_tools/powerbi/excel/powerbi_settings.png)

### **Step 4: Locate and Access Report Settings**

Scroll down to the **Gateway and Cloud Connections** section. Toggle the switch to **enable the gateway connection**. Click on the **Add to Gateway** button to initiate the connection process.

![powerbi_gateway.png](/learn/dp_consumer_learn_track/integrate_bi_tools/powerbi/excel/powerbi_gateway.png)

### **Step 5: Enable Gateway Connection**

After clicking the “Add to Gateway” button, you'll be prompted to enter the necessary **connection details** for the data source. Once you’ve entered the required connection information, finalize the connection setup.

![powerbi_gateway_connection.png](/learn/dp_consumer_learn_track/integrate_bi_tools/powerbi/excel/powerbi_gateway_connection.png)

### **Step 7: Confirm Successful Connection**

After successfully connecting,you will be mapped to the semantic model as shown in the image below:

![powerbi_gateway_conn1.png](/learn/dp_consumer_learn_track/integrate_bi_tools/powerbi/excel/powerbi_gateway_conn1.png)

### **Step 8: Access the semantic model**

After successfully connecting, you will be able to access the dashboard. 

![powerbi_chart.png](/learn/dp_consumer_learn_track/integrate_bi_tools/powerbi/excel/powerbi_chart.png)

### **Step 9: Open 'Analyze in Excel'**

The **Analyze in Excel** page should now appear, allowing you to interact with the data as needed.

![powerbi_analyze_excel.png](/learn/dp_consumer_learn_track/integrate_bi_tools/powerbi/excel/powerbi_analyze_excel.png)

### **Step 10: Interact with Data in Excel**

Analyze in Excel page appears.

![analyze_in_excel.png](/learn/dp_consumer_learn_track/integrate_bi_tools/powerbi/excel/analyze_in_excel.png)