# PowerBI Integration

1. **Navigate to the Data Product Hub: A**ccess the **Home Page** of DataOS. From there, navigate to the **Data Product Hub**, where you can explore various data products available within the platform.

    <center>
    <img src="/interfaces/data_product_hub/activation/bi_sync/image%20(1).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    </center>


2. In the Data Product Hub, browse through the list of data products. Click on the specific data product you wish to integrate with PowerBI. For example, select **Sales360** from the list to explore **Sales360** data product.

    <center>
    <img src="/interfaces/data_product_hub/activation/bi_sync/image%20(2).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    </center>


3. **Access Integration Options:** Navigate to the Access Options tab once you’ve selected a data product. Here, you’ll find various methods to access and interact with the data product in the BI Sync tab and locate **Excel and PowerBI** options**.**

    <center>
    <img src="/interfaces/data_product_hub/activation/bi_sync/image%20(3).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    </center>


4. Locate the downloaded ZIP file on the local system and unzip the folder. Three files will be present in the folder. Open the 'public_sales360' file in Power BI. Ensure that all three files are kept together, as the other two files are essential for the semantic sync of the data product. 


    <center>
    <img src="/interfaces/data_product_hub/activation/bi_sync/Untitled%20(15).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    </center>


5. Once the file is opened, a popup will appear. Enter the DataOS username and API key.

    <center>
    <img src="/interfaces/data_product_hub/activation/bi_sync/Untitled%20(16).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    </center>


    <center>
    <img src="/interfaces/data_product_hub/activation/bi_sync/Untitled17.png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    </center>



6. Click the connect button. A popup will appear. Click OK.


    <center>
    <img src="/interfaces/data_product_hub/activation/bi_sync/untitled18.png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    </center>


7. After connecting, you can see tables and views with dimensions and measures.


    <center>
    <img src="/interfaces/data_product_hub/activation/bi_sync/Untitled%20(19).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    </center>



## Governance of model on Power BI

When the Lens Model is activated via BI Sync on Power Bi

The process is managed through authentication and authorization using your DataOS user ID and API key when accessing synced data models. This ensures that columns redacted by Lens data policies are restricted based on the user's group permissions. 

For instance, if a user named **iamgroot** in the "**Analyst**" group is restricted from viewing the "Annual Salary" column, they will not see it either in the Data Product exploration page or in PowerBI after syncing. Power BI requires the DataOS user ID and API key for authentication, ensuring the user can access the full model except for any columns restricted by their data policies. This maintains security and ensures users only see the data they are authorized to view.