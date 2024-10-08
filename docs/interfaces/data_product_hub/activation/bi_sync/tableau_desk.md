# Tableau Desktop Integration

1. **Navigate to the Data Product Hub:** Start by accessing the **Home Page** of DataOS. From there, navigate to the **Data Product Hub**, where you can explore various data products available within the platform.

    <center>
    <img src="/interfaces/data_product_hub/activation/bi_sync/image%20(20).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    </center>

2. In the Data Product Hub, browse through the list of data products. Click on the specific data product you wish to integrate with Tableau. For example, select **Sales360** from the list to explore the **Sales360** data product in Tableau.

    <center>
    <img src="/interfaces/data_product_hub/activation/bi_sync/image%20(21).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    </center>

3. **Access Integration Options:** Navigate to the Access Options tab once you’ve selected a data product. Here, you’ll find various methods to access and interact with the data product in the BI Sync tab and locate **Tableau Desktop.**

    <center>
    <img src="/interfaces/data_product_hub/activation/bi_sync/Screenshot%20from%202024-09-21%2000-14-20.png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    </center>

4. Download the .tds file and Extract the zip file into Tableau's default repository, usually located at `My Tableau Repository\Datasources\`.

    <center>
    <img src="/interfaces/data_product_hub/activation/bi_sync/image%20(22).png" alt="DPH" style="width:25rem; border: 1px solid black;" />
    </center>

5. Click on the DP (Data Product) to proceed.

    <center>
    <img src="/interfaces/data_product_hub/activation/bi_sync/image%20(23).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    </center>

6. You will be prompted to enter your username and API key.

    <center>
    <img src="/interfaces/data_product_hub/activation/bi_sync/image%20(24).png" alt="DPH" style="width:25rem; border: 1px solid black;" />
    </center>

7. Once the connection is established, you can start visualising the Data Product in the Tableau Desktop.

    <center>
    <img src="/interfaces/data_product_hub/activation/bi_sync/image%20(25).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    </center>

## Governance of model on Tableau Desktop

When the Lens Model is activated via BI Sync on Tableau, all user-level access controls and data policies from Lens are automatically applied to Tableau.

The process is managed through authentication and authorization using your DataOS user ID and API key when accessing synced data models. This ensures that columns redacted by Lens data policies are restricted based on the user's group permissions. 

For instance, if a user named **iamgroot** in the "**Analyst**" group is restricted from viewing the "Annual Salary" column, they will not see it either in the Data Product exploration page or in Tableau after syncing. Tableau Desktop requires the DataOS user ID and API key for authentication, ensuring the user can access the full model except for any columns restricted by their data policies. This maintains security and ensures users only see the data they are authorized to view.