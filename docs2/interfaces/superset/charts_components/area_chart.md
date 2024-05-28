The area chart in Superset is a powerful data visualization tool designed to showcase and compare quantitative data trends over time or across categories. This chart type particularly illustrates cumulative values and highlights patterns between different series. 

![Untitled](/interfaces/superset/charts_components/area_interface.png)

On selecting the Area chart, you can then proceed with its components. Common components such as METRIC, FILTERS, ROW LIMIT, SORT BY, ROLLING FUNCTION, PERIOD, and MIN PERIOD are already covered in the '[Common Charts Components](../charts_components.md)' section for reference.


![Untitled](/interfaces/superset/charts_components/area.png)

1. **X-Axis: (Mandatory)**
    - Represents the horizontal axis, typically displaying time or categorical data.
2. **Time Grain: (Mandatory)**
    - Set the granularity or interval for time-based data displayed on the X-axis (e.g., daily, weekly).
3. **Contribution Mode: (Optional)**
    - View the contribution of each metric to the total.
4. **Series Limit: (Optional)**
    - Restrict the number of series (areas) displayed on the chart.
5. **Truncate Metric: (Optional)**
    - Truncate long metric names for better visualization.
6. **Show Empty Columns: (Optional)**
    - Toggle to display or hide columns with no data.
7. **Time Comparison: (Optional)**
    - Enable time comparison to compare data over different periods.
8. **Time Shift: (Optional)**
    - Shift the time axis to compare data at different time points.
9. **Calculation Type: (Optional)**
    - Specify the calculation type for the area chart (e.g., resample).
10. **Rule: (Optional)**
    - Define the resampling rule or method.
11. **Fill Method: (Optional)**
    - Choose the method for filling in missing data points during resampling.
12. **Annotations and Layers: (Optional)**
    - Add annotation layers to highlight specific points on the area chart.
13. **Enable Forecast: (Optional)**
    - **Forecast Periods:** Specify the number of periods for the forecast.
    - **Confidence Interval:** This shows the range where the actual values are likely to fall, indicating the level of uncertainty. A higher percentage means a wider range.
    - **Yearly, Weekly, and Daily Seasonality:** Enable or disable seasonality patterns at different intervals.

These components offer a detailed breakdown of the various settings and options for configuring an area chart in Superset.