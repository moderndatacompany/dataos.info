# Cross-filtering

We will now introduce cross-filtering. Cross-filtering allows you to select a data element from a chart (such as a table row or a slice from a pie chart) and apply it as a filter across all eligible charts within the dashboard.

## **Eligible Charts**

To use cross-filtering, you need to use an eligible chart:

- All charts built with ECharts
- Area Chart
- Bar Chart
- Graph Chart
- Line Chart
- Mixed Chart
- Pivot Table Chart
- Scatter Plot
- Smooth Line Chart
- Stepped Line Chart
- Table Chart
- World Maps

## **Applying Cross-Filters**

Cross-filters can be used in any dashboard with eligible charts.

To illustrate the usage of cross-filtering, we will do a walkthrough showing three charts: 1 table chart, 1 bar chart, and 2 pie charts. The data is comprised of superstore sales, with the pie charts showing profit by cities and profit by sub-categories and the table showing profit y cities.

<div style="text-align: center;">
  <img src="/interfaces/superset/dashboard_filtering/cross_filtering/Untitled%20(10).png" alt="Your Image Description" style="border:1px solid black; width: 80%; height: auto;">
</div>


In the profit by cities pie chart, let's hover the cursor over a city pie slice, and select it.

<div style="text-align: center;">
  <img src="/interfaces/superset/dashboard_filtering/cross_filtering/Untitled%20(11).png" alt="Your Image Description" style="border:1px solid black; width: 80%; height: auto;">
</div>


After doing this, the selected filter Dublin will be applied to the other two charts.

You'll notice in the image below that the other charts have been updated to reflect the applied filter:

<div style="text-align: center;">
  <img src="/interfaces/superset/dashboard_filtering/cross_filtering/Untitled%20(12).png" alt="Your Image Description" style="border:1px solid black; width: 80%; height: auto;">
</div>


Now, let's add another cross filter by selecting **Furnishings** in the "Profit by sub-categories" pie chart:

<div style="text-align: center;">
  <img src="/interfaces/superset/dashboard_filtering/cross_filtering/Untitled%20(13).png" alt="Your Image Description" style="border:1px solid black; width: 80%; height: auto;">
</div>

and you can see that both filters one from each pie chart are being applied to the table. 

This is demonstrated by the small number "2" icon, which conveys the number of filters currently being applied to the chart:

<div style="text-align: center;">
  <img src="/interfaces/superset/dashboard_filtering/cross_filtering/Untitled%20(14).png" alt="Your Image Description" style="border:1px solid black; width: 60%; height: auto;">
</div>


You can check which cross-filters are active in the dashboard filter bar.


<div style="text-align: center;">
  <img src="/interfaces/superset/dashboard_filtering/cross_filtering/untitled.png" alt="Your Image Description" style="border:1px solid black; width: 80%; height: auto;">
</div>


**Each chart can only emit one cross-filter.**

If you wish to apply a filter for multiple values, use the dashboard filter bar.

## **Disabling Cross-Filters**

In some situations, you may want to prevent dashboard consumers from using cross-filtering.

To disable cross-filtering, click on the **Gear icon** in the dashboard filter bar, and uncheck the "Enable cross-filtering" box.


<div style="text-align: center;">
  <img src="/interfaces/superset/dashboard_filtering/cross_filtering/Untitled%20(15).png" alt="Your Image Description" style="border:1px solid black; width: 50%; height: auto;">
</div>
