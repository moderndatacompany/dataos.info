# Tableau Desktop

In this module, you will learn how to activate a data product using Tableau Desktop to build interactive dashboards and uncover valuable insights from your data. 

<aside class="callout">
🗣 Tableau Desktop is available for Windows and macOS. If you’re using Linux, you’ll need to set up a virtual machine or use an alternative method since Tableau Desktop isn’t natively supported on this platform.
</aside>

## Scenario

Imagine you’re a sales analyst for a retail company, and you’re tasked with providing insights into the company’s Product360 data—an extensive dataset stored in DataOS. Your goal is to visualize and analyze this data within Tableau to help the sales team track trends, understand which products are frequently purchased together (product affinity), and monitor sales across different regions.

## Step-by-Step: Syncing Tableau with DataOS

1. **Navigate to Access Options**
    
    Go to the **Access Options** tab for your Data product in Data Product Hub. Under the **BI Sync**
    
    section, locate the **Tableau Desktop** option. Click to download the .tds file, which contains all the necessary connection settings for Tableau.
    
    ![tab-desk_conn.png](/learn/dp_consumer_learn_track/integrate_bi_tools/tab_desktop/tab-desk_conn.png)
    
2. **Extract the File to Tableau’s Repository**
    
    After downloading, you’ll notice a zip file. Extract this file and place it into Tableau’s default repository folder at *My Tableau Repository\Datasources*. This setup ensures that Tableau can smoothly access the connection details.
    

    ![tableau_desk_file.png](/learn/dp_consumer_learn_track/integrate_bi_tools/tab_desktop/tableau_desk_file.png)

3. **Open the Connection in Tableau**
    
    Next, open Tableau and locate the `public.sales360.tables` data source. When prompted, enter your **DataOS Username** and use your **API Key** as the password. You can retrieve your API Key by clicking on your profile icon at the bottom left of the screen.
    
    ![tab_desk_apikey.png](/learn/dp_consumer_learn_track/integrate_bi_tools/tab_desktop/tab_desk_apikey.png)
    
4. **Start Visualizing**
    
    Once connected, you’re all set! You can now start visualizing your data and building dashboards in Tableau. 
    
    ![tableau_dashboard.png](/learn/dp_consumer_learn_track/integrate_bi_tools/tab_desktop/tableau_dashboard.png)