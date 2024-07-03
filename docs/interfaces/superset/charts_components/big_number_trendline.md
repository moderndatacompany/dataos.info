# Big Number with Trendline
The Big Number with Trendline chart in Superset is a combination of a simple number display and a line graph. It shows you the current values and how they've changed over time. This combo is great for quickly understanding important insights. It's the perfect tool for highlighting key metrics and their trends, and it is useful for showcasing important data points like KPIs.

![Untitled](/interfaces/superset/charts_components/big_numb_trendline_interface.png)

On selecting the Big Number with Trendline chart, you can then proceed with its components. Common components such as METRIC, FILTERS, ROLLING FUNCTION, PERIOD, and MIN PERIOD are already covered in the '[Common Charts Components](../charts_components.md)' section for reference.


![Untitled](/interfaces/superset/charts_components/big_number_with_trendline.png)

 Let’s see its specific components one by one:

1. **TEMPORAL X-AXIS:**
    - The temporal X-axis displays time-related data for temporal analysis and is a mandatory component.
2. **TIME GRAIN:**
    - The time grain, defining the granularity or interval at which time is displayed (e.g., daily, weekly), is also a mandatory component.
3. **COMPARISON PERIOD LAG:**
    - The comparison period lag is an optional feature, allowing for the introduction of a lag in the comparison period for trend analysis.
4. **COMPARISON SUFFIX:**
    - The optional comparison suffix appends a descriptor (e.g., "lag") to metric names during comparison for clarity.
    
    For Example: the “lag” suffix is added to the comparison period lag (-0.9%).
    
5. **SHOW TIMESTAMP:**
    - The show timestamp option, which displays timestamps on data points for precision, is an optional feature.
6. **SHOW TREND LINE:**
    - The show trend line feature is optional and adds a trend line to visualize the overall trend in the data.
7. **START Y-AXIS AT 0:**
    - Sets the starting point of the Y-axis at zero for accurate representation. It is an optional setting.
8. **RULE:**
    - The rule, specifying the resampling rule or method applied, is an optional component.
9. **FILL METHOD:**
    - The fill method, determining how missing data points are handled during resampling, is also an optional feature.

<aside class="callout">
🗣 While the temporal X-axis and time grain are mandatory, the other components are optional, providing flexibility for customization based on analytical requirements and preferences.

</aside>