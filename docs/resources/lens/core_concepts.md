# Elements of Lens

<div style="text-align: center;">
    <img src="/resources/lens/tables_views.png" alt="Iris board" style="max-width: 80%; height: auto; border: 1px solid #000;">
    <figcaption> Tables and Views </figcaption>
</div>

## Table

A table is a logical construct used to define an entity. It contains information about joins (relationships), dimensions, measures, and segments. Each table is defined in a separate YAML file. 

> To draw a parallel with common data modelling concepts, **‘Table’ is equivalent to the concept of ‘Entity’**.
> 

We'll use a sample database with two tables, owner and contacts to illustrate the concepts throughout this page:

`owner` Table

| owner_id | owner_name     | owner_email          | city         |
|----------|----------------|----------------------|--------------|
| 1        | Alice Johnson  | alice@example.com    | New York     |
| 2        | Bob Smith      | bob@example.com      | San Francisco|
| 3        | Charlie Brown  | charlie@example.com  | Los Angeles  |
| 4        | David Williams | david@example.com    | Chicago      |
| 5        | Emma Davis     | emma@example.com     | Miami        |

`contacts` Table

| contact_id | owner_id | contact_name   | contact_email         | phone_number    |
|------------|----------|----------------|-----------------------|-----------------|
| 1          | 1        | John Doe       | john.doe@example.com  | 123-456-7890    |
| 2          | 2        | Jane Smith     | jane.smith@example.com| 987-654-3210    |
| 3          | 3        | Michael Brown  | michael.b@example.com | 555-123-4567    |
| 4          | 4        | Sarah Johnson  | sarah.j@example.com   | 444-222-3333    |
| 5          | 5        | Robert Wilson  | robert.w@example.com  | 777-888-9999    |


**Example**

In the example below the account table is defined for a sales analytics lens:

```yaml
tables:
  - name: owner
    sql: {{ load_sql('owner') }}
    description: Table containing information about the owners.
    data_source: icebase
    public: true   
```
You can also use the `tables` attribute to accommodate more complex SQL queries:

```yaml
tables:
  - name: owner
    sql: >
      SELECT *
      FROM owner_id, email
      WHERE owner.owner_id = contacts.owner_id
```

Within each tables dimensions, measures, and segments are defined. Joins are used to define relations between tables.

<!-- Note that tables attribute support extended functionality, and data blending. -->
 
**Attribute**

The table declaration involves the following attributes:

| **Property** | **Description** | **Possible Value** | **Best Practice** |
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

The join parameter can be used to define the relationship between two tables. Lens employs left join for all joins it generates. It's important to note that the table (referred to as the base table) in which the join is specified will always be positioned on the left side of the join.

There are three types of join relationships (one_to_one, one_to_many, and many_to_one) and a few other concepts.

**Attributes**

| Property  | Description |
| --- | --- |
| `name` | Candidate target table for joining with the base table |
| `relationship` | Type of join relationship with other tables - `one-to-one`, `one-to-many`,`many-to-one` |
| `sql` | Join clause Syntax: base_table.key = target_table.key |

**Example:**

In this example, we define the base table and outline its relationship with another table. Specifically, multiple transactions can reference the same product, establishing a `many-to-one` relationship between the transactions table and the products table. In this context, the placeholder {TABLE} refers to the base table, which is the transactions table.

``` title="owner.yaml"
tables:
  - name: owner
    sql: {{ load_sql('owner') }}
    description: Table containing information about owner records.
    joins:
      - name: contacts
        relationship: one_to_many
        sql: "{TABLE.owner_id}= {contacts.owner_id}"   
``` 

## Dimensions

Dimensions represent the properties of a single data point in the table.

```yaml title="owner.yaml"
tables:

  - name: owner
    sql: {{ load_sql('owner') }}
    description: Table containing information about owner records.
    
    dimensions:
      - name: owner_id
        type: string
        description: Unique identifier for each owner.
        sql: owner_id
        primary_key: true
        public: true

      - name: email
        type: string
        description: Email address of the owner.
        sql: email
```

The dimension declaration involves the following properties:

| **Property** | **Description** | **Possible Value** | **Best Practice** |
| --- | --- | --- | --- | 
| `name` | Unique identifier of the dimension | ^[a-zA-Z][a-zA-Z0-9_]*$ | Use snake_case. <br> For example: **`order_date`** |  
| `title` | Human-readable title of the dimension. Use ‘title’ to change the display name | String | Provide a clear and concise title for better readability and user understanding |  
| `description` | Description of the dimension's purpose | String | Provide a detailed description to explain the dimension's business value |  
| `column` | Add a reference to the column defined in the table’s SQL |   You can define custom SQL in a table’s dimension but as a best practice, we recommend defining it in a table’s SQL. | |  
| `public` | Controls visibility of dimension, i.e. whether the dimension is visible to all users or hidden. If not mentioned explicitly, by default this property is true  | True, False | Set to **`True`** for key dimensions that should be visible by default |  
| `primary_key` | The key on which the join relationship will be defined | Column name | Ensure each dimension has a unique primary key to maintain data integrity |  
| `type` | The data type of the dimension | string, number, time, boolean | Choose the appropriate data type to ensure proper sorting and filtering​ |  
| `meta` |  | Key-value pairs | Use metadata to provide additional context about the dimension, such as tags, or custom attributes |  
| `case` | Defines dimension based on SQL conditions <br><br> - `when` parameters declare a series of SQL conditions and `labels` that are returned if the condition is true <br>- `else` parameter declares the default `label` that would be returned | SQL conditions and labels | Use for creating conditional dimensions |  
| `format` | Specifies the format of the dimension, particularly useful for time |  |   |
| `sub_query` | Sub-query for the dimension. Set the flag to reference a measure of one table in dimension of another |  | Use to define complex dimensions using sub-queries |  
| `propagate_filters_to_sub_query` | Determines if filters should propagate to sub-queries | True, False | Use this property to control the behavior of filters in complex queries |  

## Measures

Measures are quantifications — fields like order subtotal, quantity of items purchased, or duration spent on a specific page. Measures are therefore computable. Say you have a measure, quantity of items purchased: you can do things like calculate the average quantity ordered, sort by descending quantities, sum all quantities, and so on.

**Measure Additivity:**

Additivity is a property of measures that tells us if we can break down or combine measure values across different categories. In simpler terms, it means that if we have a measure for a group of dimensions (like sales for different regions), we can add or combine these values to get a measure for a smaller subset of those dimensions (like sales for a specific region).

Additivity of a measure depends on its type. Only measures with the following types are considered additive: count, count_distinct_approx, min, max, sum. Measures with all other types are considered non-additive.

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


```yaml owner.yaml
tables:
  - name: owner
    sql: {{ load_sql('owner') }}
    description: Table containing information about owners.
    
    measures:
      - name: count
        sql: customer_id
        type: count_distinct
        description: Total number of owners.
```

## Segments

Segments are pre-defined groups of filters. 

The segment declaration involves the following properties 

| Property | Description | Possible Value |
| --- | --- | --- |
| `name` | Specify the name of the dimension | NA |
| `public` | Controls visibility of dimension, i.e. whether the dimension is visible to all users or hidden | `True`, `False` |
| `sql` | Add filter criteria: table.{dimension} = “dimension_values” | NA |
| `meta` | Custom metadata. This is also used to define `secure` sub property | NA |

To know more about segments click [here](/resources/lens/working_with_segments/)


``` owners.yaml
tables:
  - name: owners
    # ...

    segments:
      - name: active_owners
        sql: "{TABLE}.status = 'active'"
```

A more thorough introduction can be found in [Working with Segments](/resources/lens/working_with_segments/).

## Views

Views sit on top of the data graph of cubes and create a abstraction of whole data model with which data consumers can interact. They serve as a layer for defining metrics, providing a simplified interface for end-users to interact objectively with key metrics instead of the entire data model.

A view reference serves as a way to access dimensions, measures, and segments from multiple logical tables. It does not define any measures, dimensions, or segments on its own.

In the example below, we create the `transaction_analysis` view which includes select members from transactions, and products tables:

```yaml
views:
  - name: owner_contact_analysis
    description: View containing detailed information about owners and their associated contacts
    public: true

    tables:
      - join_path: owners
        prefix: true
        includes:
          - owner_id
          - owner_name
          - owner_status
          - owner_value
          - owner_city

      - join_path: contacts
        prefix: true
        includes:
          - contact_id
          - contact_name
          - contact_email
          - contact_phone
          - contact_owner_id
```
A more thorough introduction can be found in [Working with Views](/resources/lens/working_with_views/).

