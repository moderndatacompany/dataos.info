# Microsoft Excel Integration

## Prerequisites

**PowerBI:** Ensure the PowerBI remains on your screen while you try to connect with the Excel.

**Install the Analyze in Excel plugin in PowerBI:** 

Visit the [Analyze in Excel for Power BI Desktop](https://www.sqlbi.com/tools/analyze-in-excel-for-power-bi-desktop/) link and follow the instructions to download and install the necessary extension.

Locate the "Analyze in Excel" extension in the top left corner of Excel. and Click on it This action will open Excel and establish a connection to the Power BI dataset or report.

<center>
  <img src="/interfaces/data_product_hub/activation/bi_sync/Untitled%20(17).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
</center>



<aside class="callout">
💡 Ensure that Power BI Desktop remains open while working in Excel, as Power BI acts as the server for the data connection.
</aside>

This setup allows you to leverage Excel's analytical tools while working with data from Power BI.

<center>
  <img src="/interfaces/data_product_hub/activation/bi_sync/Untitled%20(18).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
</center>



## Governance of model on Excel

When the Lens Model is activated via BI Sync on Excel, all user-level access controls and data policies from Lens are automatically applied to Tableau.

The process is managed through authentication and authorization using your DataOS user ID and API key when accessing synced data models. This ensures that columns redacted by Lens data policies are restricted based on the user's group permissions. 

For instance, if a user named **iamgroot** in the "**Analyst**" group is restricted from viewing the "Annual Salary" column, they will not see it either in the Data Product exploration page or in Excel after syncing. First PowerBI requires the DataOS user ID and API key for authentication, ensuring the user can access the full model except for any columns restricted by their data policies. This maintains security and ensures users only see the data they are authorized to view.