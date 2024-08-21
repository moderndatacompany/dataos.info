# Bar Chart

The Bar Chart in Superset is a visualization that presents data using rectangular bars. Each bar's length corresponds to the value of a metric, and bars are typically grouped by categories (dimensions) on the horizontal axis. It's effective for comparing values across different categories or displaying trends over time.


<div style="text-align: center;">
  <img src="/interfaces/superset/charts_components/bar_interface.png" alt="Your Image Description" style="border:1px solid black; width: 80%; height: auto;">
</div>

On selecting the Bar chart, you can then proceed with its components. Common components such as METRIC, FILTERS, ROW LIMIT, SORT BY, ROLLING FUNCTION, PERIOD, and MIN PERIOD are already covered in the '[Common Charts Components](/interfaces/superset/charts_components/)' section for reference.


<div style="text-align: center;">
  <img src="/interfaces/superset/charts_components/bar.png" alt="Your Image Description" style="border:1px solid black; width: 80%; height: auto;">
</div>

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

These components offer a detailed breakdown of the various settings and options for configuring a bar chart in Superset.