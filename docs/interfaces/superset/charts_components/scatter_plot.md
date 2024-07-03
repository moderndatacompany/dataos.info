The Scatter Plot in Superset is a visualization that displays data points on a two-dimensional plane, where each point represents the value of two metrics. It's particularly for identifying relationships or correlations between two variables.

![Untitled](/interfaces/superset/charts_components/scatter_interface.png)

On selecting the Scatter plot chart, you can then proceed with its components. Common components such as METRIC, FILTERS, ROW LIMIT, ROLLING FUNCTION, PERIOD, and MIN PERIOD are already covered in the '[Common Charts Components](../charts_components.md)' section for reference.


![Untitled](/interfaces/superset/charts_components/scatter.png)

1. **X-Axis (Mandatory):**
    - Represents the horizontal axis, typically displaying time or categorical data.
2. **Time Grain (Mandatory):**
    - Set the granularity or interval for time-based data displayed on the X-axis (e.g., daily, weekly).
3. **Contribution Mode (Optional):**
    - View the contribution of each metric to the total.
4. **Series Limit (Optional):**
    - Restrict the number of series (areas) displayed on the chart.
5. **Sort By (Optional):**
    - Define the sorting order for the series display.
6. **Truncate Metric (Optional):**
    - Truncate long metric names for better visualization.
7. **Show Empty Columns (Optional):**
    - Toggle to display or hide columns with no data.
8. **Time Comparison (Optional):**
    - Enable time comparison to compare data over different periods.
9. **Time Shift (Optional):**
    - Shift the time axis to compare data at different time points.
10. **Calculation Type (Optional):**
    - Specify the calculation type for the area chart (e.g., resample).
11. **Rule (Optional):**
    - Define the resampling rule or method.
12. **Fill Method (Optional):**
    - Choose the method for filling in missing data points during resampling.
13. **Annotations and Layers (Optional):**
    - Add annotation layers to highlight specific points on the area chart.
14. **Enable Forecast (Optional):**
    - **Forecast Periods (Optional):** Specify the number of periods for the forecast.
    - **Confidence Interval (Optional):** Indicates the range where actual values are likely to fall, with a higher percentage indicating a wider range.
    - **Yearly, Weekly, and Daily Seasonality (Optional):** Enable or disable seasonality patterns at different intervals.