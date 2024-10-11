# Apache Superset Integration

## Steps

Below are the steps to proceed:

### **Step1 : Navigate to the Data Product Hub** 

Start by accessing the **Home Page** of DataOS. From there, navigate to the **Data Product Hub**, where you can explore various data products available within the platform.

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/image%20(6).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>

###  **Step2: Browse and Select a Data Product:** 

In the Data Product Hub, browse through the list of data products. Click on the specific data product you wish to integrate with Tableau. For example, select Corp Market Performance from the list to explore Tableau's **Corp Market Performance** data product.

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/image%20(7).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>

### **Step 3: Access Integration Options:** 

Navigate to the Access Options tab once you’ve selected a data product. Here, you’ll find various methods to access and interact with the data product.

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/image%20(8).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>


### **Step 4: Locate Superset Connection:** 

Scroll through the Access Options until you find the **Superset** option. Click on the **Add Connection** button. A connection window will open, prompting you to enter the necessary connection details.

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/annotely_image(10).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>


### **Step 5: Enter Connection Details:** 

Click on the **Add Connection** button. A connection window will open, prompting you to enter the necessary connection details.

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/image%20(4).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>


Enter details of **Host Address** as given in the following syntax:

```yaml
superset-<DATAOS_FQDN>
```
    
Replace `<DATAOS_FQDN**>` with the **DataOS Fully Qualified Domain Name (FQDN)**. For example, if your context is "happy-raccoon" and the FQDN is `happy-raccoon.dataos.app`, then the correct entry would be:
    
```yaml
superset-happy-raccoon.dataos.app
```
    

Enter **Username and Password:** The username and password for the Superset admin specific to the organization need to be provided. For example, in this case, you should add the credentials as `adder_1` for both the username and password. This ensures proper access and management of Superset within the organizational context.

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/image%20(4).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>


Click on **Activate** button. After clicking "Activate," a pop-up message will appear indicating that the  sync has been completed.

## Consuming the data model on Superset

Navigate to Superset, and the datasets will be created as shown below.

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/image%20(5).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>

## Governance of model on Superset

When the Lens Model is activated via BI Sync on Superset, all user-level access controls and data policies from Lens are automatically applied to Superset.

The process is managed through authentication and authorization using your DataOS user ID and API key when accessing synced data models. This ensures that columns redacted by Lens data policies are restricted based on the user's group permissions. 

For instance, if a user named **iamgroot** in the "**Analyst**" group is restricted from viewing the "Annual Salary" column, they will not see it either in the Data Product exploration page or Superset after syncing.