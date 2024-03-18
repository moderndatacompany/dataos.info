# Sales Performance Dashboard

## **Dashboard Overview**

Welcome to the Superstore Sales Performance Dashboard, a comprehensive tool designed to provide valuable insights into the superstore sales data. This dashboard is crafted to empower decision-makers by offering a clear and interactive view of sales performance utilizing multiple tabs grouped by category, city, region, and customers.

![Untitled](/interfaces/superset/1.jpeg)
<figcaption align = "center">Sales performance by Region</figcaption>


![Untitled](/interfaces/superset/2.jpeg)
<figcaption align = "center">Sales performance by Category</figcaption>


![Untitled](/interfaces/superset/3.jpeg)
<figcaption align = "center">Sales performance by City</figcaption>

![Untitled](/interfaces/superset/4.jpeg)
<figcaption align = "center">Sales performance by Customer</figcaption>


## **Data Source Information**

**Google BigQuery Connection:**

- The data for this dashboard is sourced from Google BigQuery, utilizing the dataset from Kaggle. The connection to Google BigQuery is established securely, ensuring a reliable and efficient data retrieval process.

**Dataset Details:**

- The primary dataset used for this dashboard is stored in Google BigQuery under the `superstore_sample` dataset. The dataset comprises a single table with the following columns:
    - **Row_ID (INTEGER):** Unique identifier for each row of data.
    - **Order_ID (VARCHAR):** Unique identifier for each order.
    - **Order_Date (DATE):** Date when the order was placed.
    - **Ship_Date (DATE):** Date when the order was shipped.
    - **Ship_Mode (VARCHAR):** Shipping mode chosen for the order.
    - **Customer_ID (VARCHAR):** Unique identifier for each customer.
    - **Customer_Name (VARCHAR):** Name of the customer.
    - **Segment (VARCHAR):** Market segment to which the customer belongs.
    - **Country (VARCHAR):** Country where the order was placed.
    - **City (VARCHAR):** City where the order was placed.
    - **State (VARCHAR):** State where the order was placed.
    - **Postal_Code (INTEGER):** Postal code associated with the order location.
    - **Region (VARCHAR):** Geographical region of the customer.
    - **Product_ID (VARCHAR):** Unique identifier for each product.
    - **Category (VARCHAR):** Product category.
    - **Sub_Category (VARCHAR):** Sub-category of the product.
    - **Product_Name (VARCHAR):** Name of the product.
    - **Sales (FLOAT):** Total sales amount for the order.
    - **Quantity (INTEGER):** Quantity of products ordered.
    - **Discount (FLOAT):** Discount applied to the order.
    - **Profit (FLOAT):** Profit generated from the order.

![Untitled](/interfaces/superset/5.png)

## Steps for Creating the Dashboard

### **Step 1: Creating Tabs**

1. Open Superset and navigate to the Create Dashboard section.
2. Create four tabs named:
    - "by region"
    - "by category"
    - "by city"
    - "by customer"

### **Step 2: "By Region" Tab**

Create the following charts for the “by region” tab.

1. **Discount Ratio by Region Pie Chart:**
    - Visualize the discount ratio using a pie chart.
2. **Quantity by Region Bar Chart:**
    - Create a bar chart to display quantity distribution across regions.
3. **By Region Performance Pivot Table:**
    - Utilize a pivot table to showcase performance metrics by region.
4. **Sales by Region Bar Chart:**
    - Generate a bar chart to represent sales data across different regions.
5. **Total Profit by Region Doughnut Chart:**
    - Create a doughnut chart to illustrate the total profit distribution by region.

### **Step 3: "By Category" Tab**

Create the following charts for the “by category” tab.

1. **Total Profit by Categories Pie Chart:**
    - Design a pie chart to visualize the total profit distribution across categories.
2. **Total Sub-Categories Count by Categories Bar Chart:**
    - Represent the count of sub-categories using a bar chart grouped by categories.
3. **Total Sales by Categories Bar Chart:**
    - Display total sales data using a bar chart categorized by different product categories.
4. **Sales by Category Pie Chart:**
    - Create a pie chart to showcase sales distribution by product categories.

### **Step 4: "By City" Tab**

Create the following charts for the “by city” tab.

1. **Total Sales and Quantity by City Bar Chart:**
    - Generate a bar chart to visualize both total sales and quantity distribution by city.
2. **Total Profit by City Bar Chart:**
    - Design a bar chart to represent the total profit distribution across different cities.

### **Step 5: "By Customer" Tab**

Create the following charts for the “by customer” tab.

1. **Top 10 Customers by Profit Bar Chart:**
    - Create a bar chart showcasing the top 10 customers based on profit.
2. **Total Customers by Region Bar Chart:**
    - Visualize the total number of customers across different regions using a bar chart.
3. **Top 10 Customers by Discount Bar Chart:**
    - Generate a bar chart to display the top 10 customers based on discounts.
4. **Top 10 Customers by Product Count Scatter Plot:**
    - Utilize a scatter plot to represent the product count for the top 10 customers.

### **Step 6: Assembling the Dashboard**

- Assemble the charts into their respective tabs to create a comprehensive dashboard.

### **Step 7: Customizing the Dashboard**

- Change the default color scheme to the "Airbnb color scheme" for a visually appealing theme.

![Untitled](/interfaces/superset/6.png)

- Use the CSS editor to customize the dashboard:
    - Change the background color of the entire dashboard.
    - Adjust the background color of each chart individually.
    - Modify the color and size of each chart's title.

![Untitled](/interfaces/superset/7.png)