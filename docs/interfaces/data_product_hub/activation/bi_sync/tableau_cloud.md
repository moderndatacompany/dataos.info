# Tableau Cloud Integration

1. **Navigate to the Data Product Hub:** Start by accessing the **Home Page** of DataOS. From there, navigate to the **Data Product Hub**, where you can explore various Data Products available within the platform.

    <center>
    <img src="/interfaces/data_product_hub/activation/bi_sync/image%20(6).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    </center>


2. In the Data Product Hub, browse through the list of data products. Click on the specific data product you wish to integrate with Tableau. For example, select Corp Market Performance from the list to explore Tableau's **Corp Market Performance** data product.

    <center>
    <img src="/interfaces/data_product_hub/activation/bi_sync/image%20(7).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    </center>


3. **Access Integration Options:** Navigate to the Access Options tab once you’ve selected a Data Product. Here, you’ll find various methods to access and interact with the Data Product.

    <center>
    <img src="/interfaces/data_product_hub/activation/bi_sync/image%20(8).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    </center>

4. **Locate Tableau Cloud Connection:** Scroll through the Access Options until you find the **Tableau Cloud Connection** option. 

    <center>
    <img src="/interfaces/data_product_hub/activation/bi_sync/image%20(9).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    </center>


5. **Enter Connection Details:** Click on the **Add Connection** button. A connection window will open, prompting you to enter the necessary connection details.


    <center>
    <img src="/interfaces/data_product_hub/activation/bi_sync/image%20(19).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    </center>



    **Connection Details**

    - **Project**: Enter the Tableau project name.  If the Project Name is left blank, it will automatically default to the Data Product Name, and all data sources will be registered under this project. Providing a custom project name ensures better organization of Models, Views, and Metrics in Tableau
    - **Server Address:** The address of the Tableau server (e.g., `https://prod-apnortheast-a.online.tableau.com`
    - **Site id:** The site ID, in this case, `tableausuer@123`.
    - **Username**: The Tableau username.
    - **Password**: The password associated with the Tableau account.

    You can obtain these when you **log in** to Tableau. You’ll see the **URL** like below:

    [https://prod-apnortheast-a.online.tableau.com/#/site/site_id](https://prod-apnortheast-a.online.tableau.com/#/site/piyushjoshi704a51af6e)

    **Sample:**

    [https://prod-apnortheast-a.online.tableau.com/#/site/tableauuser@123/home](https://prod-apnortheast-a.online.tableau.com/#/site/foxofe1086a891fef336/home)

    here: tableauuser@123  is your **site_id.**

6. **Activate the Connection:** After entering the required credentials, click the **Activate Key** button to establish the connection. Upon successful connection, a confirmation message will appear. The confirmation should look like the following image:

    <center>
    <img src="/interfaces/data_product_hub/activation/bi_sync/image%20(11).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    </center>

## Consuming the Data Product on Tableau Cloud

1. Log in to Tableau Cloud using the same credentials (username and password from the Data Products activation), and the user will be redirected to the Tableau Cloud home page, as shown in the following section.

    <center>
    <img src="/interfaces/data_product_hub/activation/bi_sync/image%20(12).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    </center>


2. Click on the **Manage Projects** option on the home page as shown below.

    <center>
    <img src="/interfaces/data_product_hub/activation/bi_sync/image%20(13).png" alt="DPH" style="width:25rem; border: 1px solid black;" />
    </center>


3. **The Manage Projects** option will open an interface where all the projects reside, including the newly created project **‘Corporate finance**,’ as shown below.

    <center>
    <img src="/interfaces/data_product_hub/activation/bi_sync/image%20(14).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    </center>


4. Click on the ‘Corporate finance’ project to view the available data sources that can be used to create the dashboard.

    <center>
    <img src="/interfaces/data_product_hub/activation/bi_sync/image%20(15).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    </center>

5. Click on the menu option at the right corner of the data source and select the New Workbook option, as shown below.

    <center>
    <img src="/interfaces/data_product_hub/activation/bi_sync/image%20(16).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    </center>


6. To create a new workbook, the user will be prompted to provide their DataOS username and API key as the password to sign in to the data source and open the view, which he can get by  navigating to the profile page on the bottom left corner of the DPH

    <center>
    <img src="/interfaces/data_product_hub/activation/bi_sync/image%20(17).png" alt="DPH" style="width:30rem; border: 1px solid black;" />
    </center>


7. After signing in, the user will be redirected to the workbook, where dashboard creation can begin.

    <center>
    <img src="/interfaces/data_product_hub/activation/bi_sync/image%20(18).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    <figcaption><i>Happy dashboarding!</i></figcaption>
    </center>


### **Important Considerations for Tableau Integration**

1. **Handling Entities Without Relationships**: An error will occur during synchronization if any entity in the data model lacks a defined relationship. To resolve this, you can hide the entity to avoid errors.
2. **Live Connection**: The connection between the Lens semantic layer and Tableau Cloud is live, meaning any changes to the underlying data or measure logic will automatically reflect in Tableau.
3. **Schema Changes**: If schema updates exist, such as adding new dimensions or measures, you will need to repeat the integration steps to incorporate these changes into Tableau.
4. **Avoiding Cyclic Dependencies**: Tableau does not support cyclic dependencies within data models. To avoid integration issues, ensure your data model is free of cyclic dependencies before syncing with Tableau.


### **Handling Specific Data Types in Tableau**

1. **Time Data Type as Measure in Tableau**  

    When syncing the Lens semantic layer with Tableau, note that Tableau **does not support the time data type as a measure**. While Lens supports time-based measures, Tableau treats **date and time fields as dimensions** by default. As a result, Tableau will not correctly interpret any measure with a **time data type**.

    **Recommended Actions**:

    To avoid synchronization issues:

    - Use time or date fields in Tableau only for **dimension-based** filtering or grouping.
    - For time-based calculations, limit aggregations to **MIN()** or **MAX()** functions when dealing with date/time fields in Tableau.

    <aside class="callout">
    📌 This limitation is specific to Tableau's handling of time data types as measures and does not affect other aspects of the Lens semantic layer's functionality.
    </aside>


2. **String Data Type to Geographical**

    When connecting a dataset to Tableau, it automatically detects fields such as **City** and **Country** and converts them from string data types to **Geography** types. This enables Tableau to treat these fields as geographical locations, allowing features like map visualizations and geospatial analysis without requiring manual adjustments.

## Governance of model on Tableau Cloud

When the Lens Model is activated via BI Sync on Tableau, all user-level access controls and data policies from Lens are automatically applied to Tableau.

The process is managed through authentication and authorization using your DataOS user ID and API key when accessing synced data models. This ensures that columns redacted by Lens data policies are restricted based on the user's group permissions. 

For instance, if a user named **iamgroot** in the "**Analyst**" group is restricted from viewing the "Annual Salary" column, they will not see it either in the Data Product exploration page or in Tableau after syncing. Tableau Cloud requires the DataOS user ID and API key for authentication, ensuring the user can access the full model except for any columns restricted by their data policies. This maintains security and ensures users only see the data they are authorized to view.