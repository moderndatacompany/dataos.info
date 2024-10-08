# Common Chart Components

In Superset, every chart has its special components, but there are also common components that show up in various charts. Let's take a closer look at these common components.

<div style="text-align: center;">
  <img src="/interfaces/superset/charts_components/Untitled.png" alt="Untitled image" style="border:1px solid black; width: 80%; height: auto;">
</div>

### **1. Metrics (Mandatory)**

- Metrics represent the quantitative values or measurements to be visualized on the chart.

### **2. Dimension (Optional)**

- Dimensions are categorical data points providing additional context or grouping for the metrics.

<aside class="callout">
🗣 Note that the Dimension component can be mandatory for some charts but for most of the charts it is optional.

</aside>

### **3. ROW LIMIT (Optional)**

- Control the number of rows displayed on the chart to manage the data presentation.

### **4. SORT BY (Optional)**

- Specify a column or metric to define the sorting order for the displayed data.

### **5. Group By (Optional)**

- Group By allows you to categorize or group data based on a specific dimension or attribute.

### **6. Time (Mandatory)**

- The Time component is crucial for time-based analyses, facilitating the visualization of data trends over different time intervals.

### **7. Filters (Optional)**

- Filters narrow down displayed data based on specific conditions, refining the visualization.

### **8. Annotations (Optional)**

- Annotations are additional labels or notes added to specific points on the chart.

### **9. Rolling Window (Optional)**

A Rolling Window refers to a statistical analysis method applied to time-series data. It involves systematically analyzing data within a fixed-size window that moves across the dataset.

- **Rolling Function (Optional)** Defines the statistical operation applied within the rolling window (e.g., mean, sum).
- **Periods (Optional):** Specifies the size of the rolling window.
- **Min Periods (Optional):** Specifies the minimum number of periods required for calculation within the rolling window.

<aside class="callout">
🗣 Group By is optional for some charts, while Filters, Annotations, and Rolling Window are generally optional and can be applied based on analytical requirements.

</aside>

Enhance your understanding of chart components, tailored to specific characteristics of popular chart types:

- [Big Number with Trendline](/interfaces/superset/charts_components/big_number_trendline/)

- [Big Number](/interfaces/superset/charts_components/big_number/)

- [Table](/interfaces/superset/charts_components/table/)

- [Pivot Table](/interfaces/superset/charts_components/pivot_table/)

- [Line Chart](/interfaces/superset/charts_components/line_chart/)

- [Area Chart](/interfaces/superset/charts_components/area_chart/)

- [Bar Chart](/interfaces/superset/charts_components/bar_chart/)

- [Scatter Plot](/interfaces/superset/charts_components/scatter_plot/)

- [Pie Chart](/interfaces/superset/charts_components/pie_chart/)

- [World Map](/interfaces/superset/charts_components/world_map/)

- [Bar Chart (legacy)](/interfaces/superset/charts_components/bar_chart_legacy/)