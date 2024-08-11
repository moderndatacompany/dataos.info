# Cross Filtering

Cross-filtering enables you to apply a data element from a chart (e.g., a table row, a slice from a pie chart) and then apply it as a filter across all eligible charts in the dashboard.

## Eligible Charts
In order to use cross-filtering, you need to use an eligible chart:

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

## Applying Cross-Filters
Cross-filters can be used in any dashboard with eligible charts. 

To illustrate the usage of cross-filtering, we will do a walkthrough showing three charts: 1 table chart and 2 pie charts. In this walkthrough, we will apply corss-filtering on superstore sample dataset.

<div style="text-align: center;">
  <img src="/interfaces/superset/cf1.png" alt="Untitled image" style="border:1px solid black; width: 80%; height: auto;">
</div>

In the "Profit by cities" pie chart, after clicking on a city in the pie chart.

<div style="text-align: center;">
  <img src="/interfaces/superset/cf2.png" alt="Untitled image" style="border:1px solid black; width: 80%; height: auto;">
</div>

You'll notice in the graphic below that the "Profit by sub category" pie chart and the table have both been updated to reflect the applied filter:

<div style="text-align: center;">
  <img src="/interfaces/superset/cf3.png" alt="Untitled image" style="border:1px solid black; width: 80%; height: auto;">
</div>

Now, let's add an additional cross filter by selecting Furnishings in the "Profit by sub-categories" pie chart:

<div style="text-align: center;">
  <img src="/interfaces/superset/cf5.png" alt="Untitled image" style="border:1px solid black; width: 80%; height: auto;">
</div>

You can see that both filters—one from each pie chart—are being applied to the table. The table now shows the profit by dublin city only.

This is demonstrated by the small number "2" icon, which conveys the number of filters currently being applied to the chart:

<div style="text-align: center;">
  <img src="/interfaces/superset/cf6.png" alt="Untitled image" style="border:1px solid black; width: 80%; height: auto;">
</div>

You can check which cross-filters are active in the dashboard filter bar. 

<div style="text-align: center;">
  <img src="/interfaces/superset/cf7.png" alt="Untitled image" style="border:1px solid black; width: 80%; height: auto;">
</div>
 
<aside class="callout">
🗣Each chart can only emit one cross-filter. 
If you wish to apply a filter for multiple values, use the dashboard filter bar.

</aside>

## Disabling Cross-Filters

In some situations, you may want to prevent dashboard consumers from using cross-filtering. 

To disable cross-filtering, click on the **Gear icon** in the dashboard filter bar, and uncheck the "Enable cross-filtering" box.

<div style="text-align: center;">
  <img src="/interfaces/superset/cf8.png" alt="Untitled image" style="border:1px solid black; width: 80%; height: auto;">
</div>

