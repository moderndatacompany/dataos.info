## Steps for Integrating Data Products with Tableau

This document outlines the steps required to integrate data products from DataOS with Tableau.

### **Step 1: Navigate to the Data Product Hub**

Access the **Home Page** of DataOS. From the home page, navigate to the **Data Product Hub** to explore the various data products available within the platform.

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/image%20(6).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>

### **Step 2: Browse and Select a Data Product**

In the Data Product Hub, users should browse through the list of available data products. Selecting a specific data product to integrate with Tableau is essential. For instance, **Corp Market Performance** can be chosen to explore Tableau's data offerings.

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/image%20(7).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>

### **Step 3: Access Integration Options**

After selecting a data product, users should navigate to the **Access Options** tab. Within this tab, the **BI Sync** option, which is the default, can be accessed.

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/image%20(8).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>

### **Step 4: Locate Tableau Cloud Connection**

Scroll through the Access Options to find the **Tableau Cloud Connection** option.

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/image%20(9).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>

### **Step 5: Enter Connection Details**

Click on the **Add Connection** button. A connection window will open, prompting the entry of the necessary connection details.

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/image%20(19).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>

**Connection Details**

- **Project**: Enter the Tableau project name. If left blank, the project name will default to the Data Product Name, registering all data sources under this project. Providing a custom project name enhances organization within Tableau.
- **Server Address**: The address of the Tableau server (e.g., `https://prod-apnortheast-a.online.tableau.com`).
- **Site ID**: The site ID (e.g., `tableausuer@123`).
- **Username**: The Tableau username.
- **Password**: The password associated with the Tableau account.

These details can be obtained upon logging into Tableau. The URL format will appear as follows:

[https://prod-apnortheast-a.online.tableau.com/#/site/site_id](https://prod-apnortheast-a.online.tableau.com/#/site/piyushjoshi704a51af6e)

**Sample URL**: 

[https://prod-apnortheast-a.online.tableau.com/#/site/tableauuser@123/home](https://prod-apnortheast-a.online.tableau.com/#/site/foxofe1086a891fef336/home)

In this example, `tableauuser@123` represents the **site_id**.

### **Step 6: Activate the Connection**

After entering the required credentials, click the **Activate Key** button to establish the connection. A confirmation message will appear upon successful connection, as illustrated in the image below.

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/image%20(11).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>

## Exploring the Data Product on Tableau Cloud

### **Step 1: Log in to Tableau Cloud**

Users should log in to Tableau Cloud using the same credentials (username and password from the Data Products activation). This will redirect them to the Tableau Cloud home page.

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/image%20(12).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>

### **Step 2: Manage Projects**

Click on the **Manage Projects** option on the home page.

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/image%20(13).png" alt="DPH" style="width:25rem; border: 1px solid black;" />
</center>

### **Step 3: Access the Project Interface**

The **Manage Projects** option opens an interface displaying all projects, including the newly created project titled **‘Corporate Finance**.’

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/image%20(14).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>

### **Step 4: Select the Project**

Click on the **‘Corporate Finance’** project to view the available data sources for dashboard creation.

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/image%20(15).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>

### **Step 5: Create a New Workbook**

Click on the menu option in the upper right corner of the data source and select the **New Workbook** option.

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/image%20(16).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>

### **Step 6: Provide Credentials**

To create a new workbook, users will be prompted to provide their DataOS username and API key as the password to access the data source. This information can be retrieved by navigating to the profile page in the bottom left corner of the Data Product Hub.

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/image%20(17).png" alt="DPH" style="width:30rem; border: 1px solid black;" />
</center>

### **Step 7: Start Creating the Dashboard**

After signing in, users will be redirected to the workbook, where dashboard creation can commence.

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/image%20(18).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
<figcaption><i>Happy dashboarding!</i></figcaption>
</center>


## Important Considerations for Tableau Integration

**1. Handling Entities Without Relationships**

An error will occur during synchronization if any entity in the data model lacks a defined relationship. To resolve this issue, the entity can be hidden to avoid synchronization errors.

**2. Live Connection**

The connection between the Lens semantic layer and Tableau Cloud is live. This means that any changes to the underlying data or measure logic will automatically be reflected in Tableau.

**3. Schema Changes**

If there are schema updates, such as adding new dimensions or measures, the integration steps will need to be repeated to incorporate these changes into Tableau.

**4. Avoiding Cyclic Dependencies**

Tableau does not support cyclic dependencies within data models. To prevent integration issues, it is essential to ensure that the data model is free of cyclic dependencies prior to syncing with Tableau.

---

## Handling Specific Data Types in Tableau

**1. Time Data Type as Measure in Tableau**

When syncing the Lens semantic layer with Tableau, it is important to note that Tableau **does not support the time data type as a measure**. While Lens supports time-based measures, Tableau treats **date and time fields as dimensions** by default. Consequently, Tableau will not correctly interpret any measure with a **time data type**.

To avoid synchronization issues:

- Use time or date fields in Tableau solely for **dimension-based** filtering or grouping.
- For time-based calculations, limit aggregations to **MIN()** or **MAX()** functions when handling date/time fields in Tableau.

<aside class="callout">
📌 This limitation is specific to Tableau's handling of time data types as measures and does not affect other functionalities of the Lens semantic layer.
</aside>

**2. String Data Type to Geographical**

When connecting a dataset to Tableau, the platform automatically detects fields such as **City** and **Country**, converting them from string data types to **Geography** types. This functionality enables Tableau to treat these fields as geographical locations, facilitating map visualizations and geospatial analysis without requiring manual adjustments.

---

## Governance of Model on Tableau Cloud

When the Lens Model is activated via BI Sync on Tableau, all user-level access controls and data policies from Lens are automatically applied to Tableau.

The management process involves authentication and authorization using the DataOS user ID and API key when accessing synced data models. This ensures that columns redacted by Lens data policies are restricted based on the user's group permissions.

For example, if a user named **iamgroot** in the "**Analyst**" group is restricted from viewing the "Annual Salary" column, this column will not be visible in either the Data Product exploration page or Tableau after syncing. Tableau Cloud requires the DataOS user ID and API key for authentication, ensuring that users can access the full model, except for any columns restricted by their data policies. This approach maintains security and guarantees that users only see the data they are authorized to view.
