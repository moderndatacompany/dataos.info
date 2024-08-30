# Supported parameters for Tables and Views

## Table

> To draw a parallel with Lens 1.0, **‘Table’ is equivalent to the concept of ‘Entity’**.
> 

A table is a logical construct used to define an entity. It contains information about joins (relationships), dimensions, measures, and segments. Each table is defined in a separate YAML file. 

**Example**

In the example below the account table is defined for a sales analytics lens 

```yaml
tables:
  - name: account
    sql: {{ load_sql('account') }}
    description: Table containing information about the account
    data_source: icebase
    public: true

    dimensions:
      - name: customer_id
        column: customer_id
        type: string
        description: Concatenation for customer and product.
        primary_key: true
        
      - name: city
        column: city
        type: string
        description: City of the customer.        
        
    measures:
      - name: total_accounts
        type: number
        description: Total customers.
        sql: count(distinct {TABLE.customer_id})       
```

**Parameters Supported**

The table declaration involves the following parameters:

| **Parameter** | **Description** | **Possible Value** | **Best Practice** |
| --- | --- | --- | --- |
| **Field** | **Description** | **Pattern** | **Example** |
| --- | --- | --- | --- |
| `name` | Specify the name of the table:<br>- Should start with a letter only<br>- Can only contain letters, numbers, and underscores | ^[a-zA-Z][a-zA-Z0-9_]*$ | Use snake_case. For example: `sales_insight` |
| `sql` | Add a reference to the SQL file to map data to the table. SQL mapping is maintained in a separate file | NA | Keep SQL clearly named for easy maintenance.  |
| `description` | Description of the table's purpose | NA | Provide a concise yet informative description to aid understanding |
| `public` | Controls visibility of the table, i.e., whether the table is visible to all users or hidden | True, False | Use **`True`** for tables that should be widely accessible and **`False`** for those that are sensitive or irrelevant to most users​ |
| `joins` | Define the relationship with other tables. Left joins are created. The table within which the join is defined is on the left. | NA | Use joins judiciously to avoid transitive join issues |
| `dimensions` | Dimensions associated with the table for slicing and dicing data | NA | Define dimensions that are frequently used in filtering and grouping data​ |
| `measures` | Aggregation over a dimension | NA | Focus on measures that provide key business insights.  |
| `segments` | An array of segments can be defined. Segments are to filter data based on specific criteria | NA | Create segments that represent filter groups used in common business queries to enhance usability​  |


## Joins

The join parameter can be used to define the relationship between two tables. Lens2.0 employs left join for all joins it generates. It's important to note that the table (referred to as the base table) in which the join is specified will always be positioned on the left side of the join.

Three types of joins are supported: `one-to-one`, `one-to-many`, `many-to-one`

**Example:**

| Property  | Description |
| --- | --- |
| `name` | Candidate target table for joining with the base table |
| `relationship` | Type of join relationship with other tables - `one-to-one`, `one-to-many`,`many-to-one` |
| `sql` | Join clause for ex. base_table.key = target_table.key |

## Dimensions

The dimension declaration involves the following properties:

| **Property** | **Description** | **Possible Value** | **Best Practice** | **Example Usage** |
| --- | --- | --- | --- | --- |
| `name` | Unique identifier of the dimension | ^[a-zA-Z][a-zA-Z0-9_]*$ | Use snake_case. For example: **`order_date`** |  |
| `title` | Human-readable title of the dimension. Use ‘title’ to change the display name | String | Provide a clear and concise title for better readability and user understanding |  |
| `description` | Description of the dimension's purpose | String | Provide a detailed description to explain the dimension's business value |  |
| `column` | Add a reference to the column defined in the table’s SQL |  | You can define custom SQL in a table’s dimension but as a best practice, we recommend defining it in a table’s SQL. |  |
| `public` | Controls visibility of dimension, i.e. whether the dimension is visible to all users or hidden. If not mentioned explicitly, by default this property is true  | True, False | Set to **`True`** for key dimensions that should be visible by default |  |
| `primary_key` | The key on which the join relationship will be defined | Column name | Ensure each dimension has a unique primary key to maintain data integrity |  |
| `type` | The data type of the dimension | string, number, time, boolean | Choose the appropriate data type to ensure proper sorting and filtering​ |  |
| `meta` |  | Key-value pairs | Use metadata to provide additional context about the dimension, such as tags, or custom attributes |  |
| `case` | Defines dimension based on SQL conditions
- `when` parameters declare a series of SQL conditions and `labels` that are returned if the condition is true
- `else` parameter declares the default `label` that would be returned | SQL conditions and labels | Use for creating conditional dimensions |  |
| `format` | Specifies the format of the dimension, particularly useful for time |  |  |  |
| `sub_query` | Sub-query for the dimension. Set the flag to reference a measure in dimension |  | Use to define complex dimensions using sub-queries |  |
| `propagate_filters_to_sub_query` | Determines if filters should propagate to sub-queries | True, False | Use this property to control the behavior of filters in complex queries |  |

## Measures

The measure declaration involves the following properties:

| **Property** | **Description** | **Possible Value** | **Best Practice** | **Usage** |
| --- | --- | --- | --- | --- |
| `name` | Unique identifier of the measure | ^[a-zA-Z][a-zA-Z0-9_]*$ | Use snake_case. For example: **`total_revenue`** |  |
| `sql` | SQL expression to define the measure |  | In SQL, custom SQL expressions can be defined.<br>- Useful for specifying formulas.<br>- Helps calculate other measures in SQL. |  |
| `title` | Human-readable title of the measure | String | Provide a clear and concise title for better readability and user understanding |  |
| `type` | The data type of the measure | `time`, `string`, `number`, `boolean`, `count`, `sum`, `count_distinct`, `count_distinct_approx`, `avg`, `min`, `max` | Choose the appropriate type to match the measure's calculation method |  |
| `description` | Description of the measure's purpose | String | Highlight Purpose and Usage |  |
| `public` | Controls visibility of the measure | True, False | Set to **`True`** for key measures that should be visible by default |  |
| `filters` | Filters applied to the measure | SQL conditions | To aggregate a measure for a specific category, apply a filter.<br> For example, apply a filter for product category. | **Syntax:** `{table}.{dimension_name} = 'dimension_value'`<br> **e.g.** `sales.product_category = 'Electronics'` |
| `rollingWindow` | Defines a rolling window for time-based measures | { trailing: **`time period`** } | Use for calculating measures over a specific time window, such as trailing 7 days or trailing 1 month. | **Example:** <br><br>measures:<br>&nbsp;&nbsp;name: count_month<br>&nbsp;&nbsp;SQL: id<br>&nbsp;&nbsp;type: count<br>&nbsp;&nbsp;rolling_window:<br>&nbsp;&nbsp;&nbsp;&nbsp;trailing: 1 month<br>&nbsp;&nbsp;&nbsp;&nbsp;offset: end<br><br>- **`trailing`** and **`leading`** parameters define window size. <br>- **`offset`** can be `start` or `end` of the date range |
| `drillMembers` | Define drill-down fields on a measure | Array of dimensions | Define drill members to enable detailed exploration of a measure across dimensions specified on the dashboard |  |
| `format` | Format the output of measures |  |  |  |
| `meta` | Custom metadata |  |  |  |

## Segments

Segments are pre-defined groups of filters. 

The segment declaration involves the following properties 

| Property | Description | Possible Value |
| --- | --- | --- |
| `name` | Specify the name of the dimension | NA |
| `public` | Controls visibility of dimension, i.e. whether the dimension is visible to all users or hidden | `True`, `False` |
| `sql` | Add filter criteria:
table.{dimension} = “dimension_values” | NA |
| `meta` | Custom metadata. This is also used to define `secure` sub property | NA |