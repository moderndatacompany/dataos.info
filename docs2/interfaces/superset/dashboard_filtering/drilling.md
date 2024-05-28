# Drilling to Chart Details

Within Superset, you can delve deeper into chart data and obtain further insights regarding specific metrics or a group of metrics by utilizing the Drill to Detail feature in a dashboard view.

The Drill to Detail functionality is supported across all charts in Superset, provided that the chart organizes data based on dimension values.

## **Drill to Detail from Drop Down**

To showcase all the data comprising a chart, you can utilize the Drill to Detail feature from the chart's drop-down menu.

1. Right-click on the vertical ellipsis (⋮) menu of a chart within the dashboard.
2. Select **Drill to detail** to access the complete table view.

<p align="center">
  <img src="/interfaces/superset/dashboard_filtering/drilling/Untitled%20(10).png" alt="Your Image Description" />
</p>


## **Drill to Detail on a Chart**

You can also directly interact with the chart to display all relevant data.

1. Right-click on any part of a chart.
2. Choose **Drill to detail** to access the full table view.

<p align="center">
  <img src="/interfaces/superset/dashboard_filtering/drilling/Untitled%20(11).png" alt="Your Image Description" />
</p>

## **Drill to Detail By on a Chart**

To delve into the underlying data corresponding to specific values or a set of values on the chart — essentially, all columns in the dataset for rows filtered to the selected values — you can employ the Drill to Detail By feature.

Drill to Detail By offers an interactive approach to transition from a high-level dimension, such as countries, to a more detailed one, such as the United States.

1. Right-click on the dimension values displayed on the chart.
2. Choose **Drill to detail by.**

<p align="center">
  <img src="/interfaces/superset/dashboard_filtering/drilling/Untitled%20(12).png" alt="Your Image Description" />
</p>

## **Tips**

- As you filter the dashboard, Drill to Detail will reflect the applied filters while displaying the underlying data in a tabular format.
- You can scroll down to 50 rows per page on a Drill to Detail table.
- When applicable, the Drill to Detail table shows the formatted data by default. You can change the column formatting to the original value by clicking the gear icon.

<p align="center">
  <img src="/interfaces/superset/dashboard_filtering/drilling/Untitled%20(13).png" alt="Your Image Description" />
</p>