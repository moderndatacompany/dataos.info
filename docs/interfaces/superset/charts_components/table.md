In Superset, a table chart is a visual representation of tabular data, displaying information in rows and columns.

![Untitled](/interfaces/superset/charts_components/table_interface.png)


Common components such as METRIC, FILTERS, ROW LIMIT, ROLLING FUNCTION, PERIOD, and MIN PERIOD are already covered in the '[Common Charts Components](../charts_components.md)' section for reference.

![Untitled](/interfaces/superset/charts_components/table.png)

Let’s see its specific components one by one:

1. **QUERY MODE:**
    - The mode in which the query is executed provides options like 'Aggregate' for summarizing data and 'Raw Records’ for displaying detailed, unaggregated information.
2. **TIME GRAIN:**
    - The granularity or interval at which time-related data is displayed.
3. **COLUMNS:**
    - Represents individual fields or attributes in the raw data when the 'Raw Records' mode is selected.
4. **PERCENTAGE METRICS:**
    - Metrics are expressed as percentages, providing additional insights.
5. **SERVER PAGINATION:**
    - Enables server-side pagination for efficient handling of large datasets.
6. **SERVER PAGE LENGTH:**
    - Specifies the number of rows to be fetched from the server in each pagination request. When set to 0, it means no pagination.
7. **ORDERING:**
    - Specifies the ordering of the data, allowing users to sort the raw records based on a selected column.
8. **SORT DESCENDING:**
    - Sorts the table values in decreasing order.
9. **SHOW TOTALS:**
    - Option to display the total values for selected metrics.