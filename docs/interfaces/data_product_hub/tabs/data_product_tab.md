# Data Products Tab

**The Data Products** tab is the homepage of the Data Product Hub that showcases the list of Data Products that are deployed in the Data Product Hub. To add the Data Product on Data Product Hub you need to run the scanner workflow of Data Products. To search the Data Product of your choice you can filter out the Data Products by readiness, by type, and by use case just by clicking on the checkbox on the right panel of the Hub. You can also filter out the Data Products by domain just by clicking on a particular domain tab such as Customer Service. 

<img src="/interfaces/data_product_hub/Untitled%20(14).png" alt="Outlined Image" style="border:2px solid black;">

## Filter Options for Data Products

You can apply various filters to filter out the Data Product of your requirement. Below are the filters that can be applied to Data Products.

**By Readiness:**  Readiness is categorized as Ready-to-use Data Products and Template of Data Products. If you want to consume the pre-built Data Products then select the Ready to use checkbox or if you need to create the Data Product of your own then use the Data Product templates by selecting the Template checkbox.

**By Type:** There are two types of Data Products based on the source of data, Internal Data Products powered by data internal to the organization, and 3rd Party Data Products, powered by data obtained from 3rd party sources.

**By Use Case:** Each Data Product is designed to address a specific use case. However, a single Data Product may cater to multiple use cases, and conversely, multiple Data Products may target the same use case. Therefore, you can filter out the relevant Data Products based on your specific use case.

**By Domain:** Each Data Product belongs to a particular domain so selecting the domain of your interest will filter out the Data Products of that domain.

**By Keywords:** You can search Data Products by keywords mentioned in the Data Product name. For example, if you search the ‘new’ keyword in the search bar on the right corner and click enter, it will list all the Data Products with the ‘new’ keyword in their name, as you can see below.

<img src="/interfaces/data_product_hub/Untitled%20(15).png" alt="Outlined Image" style="border:2px solid black;">

**By Favourites:** You can filter out all the bookmarked Data Products by clicking on the ‘star’ symbol.

<img src="/interfaces/data_product_hub/Untitled%20(16).png" alt="Outlined Image" style="border:2px solid black;">

In this tab, you can explore individual Data Products. Just click on a Data Product of your choice, and an interface will open that resembles the below image.

<img src="/interfaces/data_product_hub/Untitled%20(17).png" alt="Outlined Image" style="border:2px solid black;">

## Tabs
The Data Product Hub interface consists of various tabs, each serving a distinct purpose.

### **Overview Tab**

In the **Overview Tab,** you can see a brief overview of the Data Product such as purpose, use cases, owner, collaborators, users, number of queries, SLO adherence, and data flow.

**Purpose:** Describes the purpose of the Data Product. The purpose is defined while configuring the Data Product manifest file.

**Use cases:** Use cases are defined while configuring the Data Product manifest file. A Data Product can have multiple use cases.

**Owner:** Owners are defined while configuring the Data Product manifest file and can be changed later on Metis. If you do not mention the owner in your manifest file, it will default to consider the person who created the Data Product as the owner.

**Collaborators:** Collaborators are defined only while configuring the Data Product manifest file.

**Users:** It shows the number of users who clicked on the Data Product on Metis. Services running in the back end count the number of users who clicked on the particular Data Product.

**Queries:** It shows the number of queries run on the Data Product in Minerva cluster. Services running in the back end count the number of queries run on the particular Data Product.

**SLO Adherence:** Service Level Objectives (SLOs) are our Data Product's defined data quality standards, ensuring it meets user expectations and business needs. We continuously monitor our data product against these SLOs using data quality checks to identify and address any deviations promptly. SLO Adherence indicates the success rate of data quality checks and can be calculated as `SLO Adherence (%) = (Total Checks Passed / Total Checks Applied) * 100` based on the last 10 checks applied.

<img src="/interfaces/data_product_hub/Untitled%20(18).png" alt="Outlined Image" style="border:2px solid black;">

<aside class="callout">
🗣 Remember that quality checks can be applied to both input and output data.

</aside>

**SLO Adherence Indicators:** SLO Adherence indicators represent different colors for different SLO Adherence ranges.  A green indicator represents SLO Adherence of 100%, a yellow indicator represents SLO Adherence between 50% and 99%, and a red indicator represents SLO Adherence between 0% and 49%. Green is considered good, yellow is considered average,  and red is considered bad SLO Adherence.

<img src="/interfaces/data_product_hub/Untitled%20(19).png" alt="Outlined Image" style="border:2px solid black;">


### **Performance Tab**

**Performance Tab** shows the performance of the output tables, here you can check how many data fields are in each output Table and their SLO adherence based on the last ten runs.

<img src="/interfaces/data_product_hub/Untitled%20(20).png" alt="Outlined Image" style="border:2px solid black;">

You can also view the SLO checks in detail by clicking the **Details of the last 10 runs** in the **Highlights** section.

<img src="/interfaces/data_product_hub/Untitled%20(21).png" alt="Outlined Image" style="border:2px solid black;">

### **Governance Tab**

In the **Governance Tab**, If the Data Product incorporates access or data policy then the user has to send the request to the Data Product owner or the contributors to access the data.

<img src="/interfaces/data_product_hub/Untitled%20(22).png" alt="Outlined Image" style="border:2px solid black;">

To send the request, click on the three-dot menu on the right side of the table name, then click on **Request Access.**

<img src="/interfaces/data_product_hub/Untitled%20(23).png" alt="Outlined Image" style="border:2px solid black;">

On the right, a panel will open where you need to give the title for your request, and the assignee name, the assignee can be the owner or collaborators, you can select multiple assignees, and then provide the description of why you need to access the data then click on the **Send Request.** On sending the request, the Data Product owner or collaborators are notified on Metis and Email.

<img src="/interfaces/data_product_hub/Untitled%20(24).png" alt="Outlined Image" style="border:2px solid black;">

<aside class="callout">
🗣 For Data Product owner and collaborators, to approve the request you need to reconfigure your policy.

</aside>

### **About Tab**

**About Tab** describes the Data Product, which is defined while configuring the Data Product manifest file and can be changed later on Metis.

<img src="/interfaces/data_product_hub/Untitled%20(25).png" alt="Outlined Image" style="border:2px solid black;">

### **Recent Updates Tab**

In the **Recent Updates Tab**, you can see all the recent updates made to the Data Product.

<img src="/interfaces/data_product_hub/Untitled%20(26).png" alt="Outlined Image" style="border:2px solid black;">

You can also explore and query the output data by clicking on the output dataset in the **Explore Data** drop-down menu in the right corner. It will redirect you to the workbench where you can query.

<img src="/interfaces/data_product_hub/Untitled%20(27).png" alt="Outlined Image" style="border:2px solid black;">