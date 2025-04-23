# Creating a Dashboard with LQL (Lens 1.0)

!!! info "Information"
    This guide will teach you how to create charts and dashboards in the Navigator using datasets generated through Lens Query Language. It provides a step-by-step process to help you turn your lens findings into impactful visual insights.


Let's visualize our data. We're all set to kickstart this endeavor using the Navigator application within DataOS. It is our primary tool for exploring insights and is built on Apache Superset. 

Navigator operates on "Datasets". This means we'll need to create a Dataset powered by the LQL (Lens Query Language) that we will copy from the Lens View (created while exploring our data and finding answers to the analytical questions). This dataset will serve as the foundation for our visualization. We will create the required visualization/chart from this dataset and add it to a dashboard, named- Sales Performance Dashboard. This dashboard is crafted to empower decision-makers by offering a clear and interactive view of sales performance for a sports retail store utilizing multiple tabs.

## Launching Navigator App

To get started, head over to the Navigator application directly from the DataOS home page.

![dashboard_home.png](/quick_guides/create_dashboard_lql/navigator_home.png)

## Creating Dashboards

Before we can dive into our visualization, there are a couple of steps we need to follow.

Let's create a blank Dashboard before we start.

1. Navigate to the "**Dashboards**" tab. Click the "**+Dashboard**" button.
    
    ![dashboard_home](/quick_guides/create_dashboard_lql/dashboard_home.png)
    
2. You'll now have a new dashboard with the title [untitled dashboard].  Let's rename it to "Sales Performance Analysis”. Don't forget to click on the "**Save**" button to ensure your changes are preserved.
    
    ![dashboard created.png](/quick_guides/create_dashboard_lql/dashboard_created.png)
    

## Navigating to SQL Lab

Selecting the SQL tab at the navigation bar and choosing the SQL Lab in Superset will redirect you to the query interface. Here, you can write your queries and explore your data with efficiency. 

Let's go back to the Lens View that we saved and copy the LQL as shown below.

1. Click the query statement above your table.
2. Click on the **Copy** button at the top right of the LQL.
    
    ![image](/quick_guides/create_dashboard_lql/copy_lql.png)
    
3. To Create our Dataset, let's paste our LQL into SQL Lab.
4. Click **Run.** This action will execute the query, and you should see the query results returned promptly. ****
    
    ![image](/quick_guides/create_dashboard_lql/run_query_nav.png)
    
5. Now click on **Save** **dataset**.
    
    ![image](/quick_guides/create_dashboard_lql/save_dataset_nav.png)
    
6. We will save it as new and give it a name. Let’s call this "Country wise Revenue Data”
7. Then click on "Save & Explore".
    
    ![image](/quick_guides/create_dashboard_lql/save_explore_box.png)
    


**Select and aggregate metrics**

1. Drag the variables that we want to aggregate into the "Metrics" Pane
2. Select your aggregation function.
3. Click on the pencil to rename metrics names to make them clearer to the end user. 

**Save and Add**

Let's save this chart and add it to our dashboard.

1. Edit the name.
2. Click **Save.**
3. Select the dashboard you wish to add it to from the drop-down.
4. Select "Save" in the "Save Chart" Pop-up. 

 Repeat the process for the rest of the LQL for the analysis. 

## Customizing the Dashboard

1. Change the default color scheme to the "Airbnb color scheme" for a visually appealing theme.

    ![image](/quick_guides/create_dashboard_lql/dashboard_properties.png)

1. Use the CSS editor to customize the dashboard:
    - Change the background color of the entire dashboard.
    - Adjust the background color of each chart individually.
    - Modify the color and size of each chart's title.

    ![image](/quick_guides/create_dashboard_lql/css_editor.png)

Add tabs and create few more charts and add them to dashboards.