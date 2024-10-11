# Tableau Desktop Integration

## Steps

The following steps outline the process for integrating Tableau Desktop with DataOS:

### **Step 1: Navigate to the Data Product Hub**

Access the **Home Page** of DataOS. From the home page, navigate to the **Data Product Hub** to explore the various data products available within the platform.

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/image%20(20).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>

### **Step 2: Browse and Select a Data Product**

In the Data Product Hub, users should browse through the list of data products. Clicking on a specific data product to integrate with Tableau is essential. For example, selecting **Sales360** from the list allows exploration of the **Sales360** data product in Tableau.

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/image%20(21).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>

### **Step 3: Access Integration Options**

After selecting a data product, navigate to the **Access Options** tab. Within this tab, various methods to access and interact with the data product can be found, including the **BI Sync** tab, where **Tableau Desktop** is located.

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/Screenshot%20from%202024-09-21%2000-14-20.png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>

### **Step 4: Download and Extract the `.tds` File**

Download the .tds file and extract the zip file into Tableau's default repository, typically located at `My Tableau Repository\Datasources\`.

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/image%20(22).png" alt="DPH" style="width:25rem; border: 1px solid black;" />
</center>

### **Step 5: Proceed with Data Product**

Click on the Data Product (DP) to continue.

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/image%20(23).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>

### **Step 6: Enter Credentials**

Users will be prompted to enter their username and API key.

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/image%20(24).png" alt="DPH" style="width:25rem; border: 1px solid black;" />
</center>

### **Step 7: Visualize Data in Tableau Desktop**

Once the connection is established, users can begin visualizing the Data Product in Tableau Desktop.

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/image%20(25).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>

---

## Governance of Model on Tableau Desktop

When the Lens Model is activated via BI Sync on Tableau, all user-level access controls and data policies from Lens are automatically applied to Tableau.

The management process utilizes authentication and authorization through the DataOS user ID and API key when accessing synced data models. This ensures that columns redacted by Lens data policies are restricted based on the user's group permissions.

For instance, if a user named **iamgroot** in the "**Analyst**" group is restricted from viewing the "Annual Salary" column, this column will not be visible in either the Data Product exploration page or in Tableau after syncing. Tableau Desktop requires the DataOS user ID and API key for authentication, ensuring users can access the full model, except for any columns restricted by their data policies. This approach maintains security and guarantees that users only see the data they are authorized to view.
