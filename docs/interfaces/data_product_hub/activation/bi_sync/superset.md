# Apache Superset Integration

## Step 1

Enter details of:

- **Host Address**
    
    Enter the host address as given in the following syntax:
    
    ```yaml
    superset-<DATAOS_FQDN>
    ```
    
    Replace `<TAOS_FQDN**>` with the **DataOS Fully Qualified Domain Name (FQDN)**. For example, if your context is "happy-raccoon" and the FQDN is `happy-raccoon.dataos.app`, then the correct entry would be:
    
    ```yaml
    superset-happy-raccoon.dataos.app
    ```
    

- **Username and Password:**

    Since in our organization we have integrated **Superset** as one of the key components within our DataOS interfaces, we do not require external authentication credentials for it, as it is managed at the organizational level. Therefore, the username and password for the Superset admin specific to the organization need to be provided. For example, in this case, you should add the credentials as `adder_1` for both the username and password. This ensures proper access and management of Superset within the organizational context.

    <center>
    <img src="/interfaces/data_product_hub/activation/bi_sync/image%20(4).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    </center>


    After clicking "Activate," a pop-up message will appear indicating that the  sync has been completed.

## Step 2

Navigate to Superset, and the datasets will be created as shown below.

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/image%20(5).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
</center>

## Governance of model on Superset

When the Lens Model is activated via BI Sync on Superset, all user-level access controls and data policies from Lens are automatically applied to Superset.

The process is managed through authentication and authorization using your DataOS user ID and API key when accessing synced data models. This ensures that columns redacted by Lens data policies are restricted based on the user's group permissions. 

For instance, if a user named **iamgroot** in the "**Analyst**" group is restricted from viewing the "Annual Salary" column, they will not see it either in the Data Product exploration page or Superset after syncing.