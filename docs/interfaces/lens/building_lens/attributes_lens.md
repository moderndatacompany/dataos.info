# Attributes of Lens YAML

## Syntax of a Lens YAML

The general syntax to define entity mapping within a Lens.

```yaml
name: {{lens-name}}
description: {{lens-description}}
owner: {{owner-name}}
entities:
  - name: {{entity-name}}
    sql:
      query: 
        {{query statement:SELECT * FROM table_name}}
      columns:
       - name: {{column-name}}
      verified: {{true | false}}
      tables:
        - {{table_name}}
    fields:        
      - name: {{field-name}}
        type: {{string | number | date | bool}}
        column: {{column present in the underlying data table}}
        primary: {{true | false}}
    dimensions:
      - name: {{dimension-name}}
        type: {{string | number| date | bool}}
        sql_snippet: {{custom SQL query to calculate dimension}}
        hidden: {{true | false}}
        sub_query: {{true | false}}
    measures:
      - name: {{name-of-measure}}
        sql_snippet: {{column or custom SQL query to calculate measure'}}
        type: {{sum| min| max| avg| count| count_distinct| count_distinct_approx| running_total| number}}
        hidden: {{true | false}}
    relationships:
      - type: {{1:N | N:1| 1:1}}
        field: {{field-name}}
        target:
          name: {{Related entity name}}
          field: {{primary field}}
        sql_snippet: {{additional join conditions}}
```

Below is a brief summary of each section and its respective attributes to help you quickly grasp the configuration. For in-depth information on their properties and usage, please click on the individual attribute or refer to [Details for Configuration Attributes.](/interfaces/lens/building_lens/attributes_lens/#configuration-attributes) 

## Lens Meta Section

This section helps users quickly understand the Lens's purpose, ownership, and usage. The Lens Meta section typically includes:

| Attributes | Description |
| --- | --- |
| name | Name of the Lens |
| description | Description for the Lens |
| owner | Owner of the Lens |
| tags | tags for discoverability |

## Entities Section

The entities are the core components that interact with different aspects of your business and drive day-to-day operations. Each identified entity has the following attributes.

| Attribute | Description |
| --- | --- |
| name | Name of the entity |
| description | description of an entity |
| SQL | A query that runs against your data source to extract the entity table |
| fields | Unique identifiers for an entity |
| dimensions | Categorical or time-based data that helps in adding context to the measures |
| measures | Aggregated columns are calculated using SQL expressions. Measures are the foundation for defining metrics. |
| relationships | Defines the relationship of entities with other entities. An entity can be joined to other entities and have one-to-one, one-to-many, or many-to-one relationships. |
| extends | This allows you to extend an existing entity to use all declared elements of the entity. |

### SQL

This section defines the query to map identified entity with physical data.

| Attributes | Description |
| --- | --- |
| query | SQL query to generate a table that the entity will reference |
| columns | All the columns that are referenced in the fields |
| tables | Tables that are referred to in the supplied SQL query |
| lenses | Lenses that are referred to in the supplied SQL query |

### Fields

**Fields** contain direct mappings to the underlying data source columns. Mention all the columns in the field that directly map to your underlying table.

| Attribute |  | Description |
| --- | --- | --- |
| name |  | Name of the field |
| type |  | Type of the field |
|  | string | Use this type when the field contains letters or special characters. |
|  | number | Assign this type to fields containing integers or numbers. |
|  | date | Choose this type for fields that contain date values. |
|  | bool | Use this type when a field contains boolean values. |
| description |  | Description of the field |
| column |  | Maps your field to the column in the physical table |
| primary |  | Use this property to explicitly state whether the field needs to be considered a primary key. |

### Dimensions

**Dimensions** are columns containing qualitative data; they are groupable and can be used to query measures to varying levels of granularity. Dimensions can be:

- An attribute that can directly reference a column of the underlying table or
- A derived value calculated using an SQL expression

| Attribute |  | Description |
| --- | --- | --- |
| name |  | Name of the dimension |
| description |  | Description of the dimension |
| type |  | Type of the dimension. Refer https://www.notion.so/dimensions |
|  | string | Typically used when the dimension contains letters or special characters.  |
|  | number | Dimension containing an integer or number can be assigned the type number. |
|  | date | Use a date type for the dimension if the SQL expression expects to return a value of the type date. |
|  | bool | Used when a dimension contains boolean values |
| sql_snippet |  | A query to extract dimensions from the physical table. It can either be a one-to-one mapping to a column of your physical table, or you can define a custom query. |
| sub_query |  | Allows referencing measures from other entities. It’s of boolean type. |
| hidden |  | It will hide the dimension from the user interface if set to true. |

### Measures

**Measures** are essentially aggregated numerical values that stem from the quantitative columns of the underlying table. They are not limited to simple aggregations; you can also define more intricate and customized calculations using SQL snippets. A measure is an aggregated column that helps define business-specific metrics.

| Attribute | Sub property | Description |
| --- | --- | --- |
| name |  | Name of the measure |
| description |  | Description of the measure |
| type |  | Type of the measure. |
|  | number | All numerical values returned after expression execution. |
|  | count | Count of all values. |
|  | count_distinct | Count all distinct values. |
|  | count_distinct_approx | Gives an approx count of values in a column. |
|  | sum | Calculate the sum across all values. |
|  | average | Calculate the average across all values. |
|  | min | Calculate the minimum across all values. |
|  | max | Calculate the maximum across all values. |
|  | running_total | Calculates cumulative sum. The granularity will return the value's sum if it is not defined. |
| sql_snippet |  | Based on the measure(aggregation) type, you can specify the aggregated column or define a custom query. |
| rolling_window |  | You can aggregate column values within a defined window, just like the SQL window function. |
| hidden |  | It will hide the dimension from the user interface if set to true. |

### Relationships

Relationships in data modeling are like connections between different data entities. They help you combine information from various sources to answer specific questions. These connections are typically one-way, similar to a left join in SQL, with one entity as the main focus. It's important to consider this direction when using relationships to ensure you get the results you need.

A defined relationship simplifies querying dimensions and measures from multiple entities. Entities would be joined based on the defined keys and relationships. Once the relationship and fields are declared in the model, Lens will automatically generate join logic to render columns correctly. 

| Attribute | Sub-Property | Description |
| --- | --- | --- |
| field |  | The field on which the join will be defined. Its ‘primary’ property is set to true (Primary Key) |
| target |  | Target entity to join |
|  | name | The entity you need to join. |
|  | field | Join will be performed using this field of the entity |
| description |  |  |
| type |  | Type of the relationship  |
|  | 1:1 | A one-to-one relationship with the other entity. A record in one entity is associated with exactly one record in another. |
|  | 1:N | One to many relationships with the other entity. A record in one entity is associated with multiple records in another entity. |
|  | N:1 | Many to one relationship with the other entity. Relationship between more than one record of an entity with a single record in another entity.  |
| sql_snippet |  | If you have more than one clause in your join statement, you can add a query for it. |

## Configuration Attributes

Details of the attributes are here:

### `entities`

**Description**: Entities describe business objects such as customers, products, and users or business-specific activities such as web and app events, downloads, and purchases.

**Example Usage:**

```yaml
entities:
 
```

### `name`

**Description:** name of the entity representing a business object.

There are specific rules to follow when naming entities within a Lens -

- As a convention entity name should start with a lowercase letter.
- It can contain a letter, number, or ‘_’.
- It needs a minimum length of 2 characters and cannot exceed 128 characters.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | Mandatory |  | product_info |

Example:

```yaml
entities:
  - name: retailer_info
```

### `description`

**Description:** Provide a description of the Lens.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | Mandatory |  |  |
|  |  |  |  |

```yaml
name: retail_supply_chain
description: Data Model for Sports Retail data

```

### `tags`

Multiple tags can be added to an entity. They aid in discoverability.

```yaml
entities:
	- name: product
		sql: 
      query: SELECT * FROM icebase.test.products
      ---
      ---
    tags:
      - product
      - brand
```

### `sql`

**Description:** This section provides a way to write SQL and other properties to construct the entity.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | Mandatory |  |  |

**Example Usage:**

```yaml
entities:
  - name: product
    sql:
```

### `query`

**Description:** A query that runs against your data source to extract the entity table. This will also allow aggregating or filtering the data to construct the desired entity.

**Example Usage:**

Within the SQL ‘query’ property, you can pass in the SQL query to generate the entity from the underlying tables.  A general form of SQL query is `select * from table_name`, but you can add any valid SQL query.

```yaml
entities:
  - name: product
    sql:
      query: SELECT * FROM icebase.test.products
```

OR

```yaml
entities:
- name: user_activity
	sql:
		query:  SELECT
		        *,
		        row_number() over(partition by session_id order by created_on) as row_num,
		        lag(created_on) over ( partition by session_id order by created_on ) last_act_time
		        FROM
		        icebase.campaign.click_stream
```

You can also reference and reuse the SQL expression of an existing entity to create a new entity.

```yaml
entities:
  - name: activity_stream
    sql:
      query: SELECT * FROM icebase.entity_360.campaign_stream
      -----
      -----
    fields:
		-----
    -----
  - name: purchased_order
	  sql:
      query: SELECT * FROM ${activity_stream.sql()} where activity = 'purchased_order'
```

### `columns`

**Description**: All the columns that are referenced in the query as fields. Columns must be specified in addition to the query property. It cannot be left empty. 

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | Mandatory |  | valid column name |

**Example Usage:**

```yaml
sql: 
			query: SELECT * FROM icebase.test.products
      # add all the column names referred to in the fields
	    columns:
			  - name: product_id
```

### `tables`

**Description**: Tables that are referred to in the supplied SQL query.

**Example Usage:**

```yaml
entities:
  - name: product
    sql:
      query: SELECT * FROM icebase.test.products
			columns:
        - name: uuid
      verified: true
      tables:
        - icebase.test.products
```

### `lenses`

Description: Lenses that are referred to in the supplied SQL query (if any).

Example Usage:

```yaml

```

## `extends`

An entity can be extended to reuse all declared elements. In the example below, the **selected_product** entity is created by referencing the **activity_stream** entity.

```yaml
name: sample
contract: test01
owner: iamgroot
entities:
  - name: activity_stream
    sql:
      query: SELECT * FROM icebase.entity_360.campaign_stream
    fields:
			------
			------
    dimensions:
			------
			------
	- name: selected_product
		extend: activity_stream
    # referencing extended entity in the sql
		sql:
			query: SELECT * FROM ${activitystream.sql()} where activity = 'selected_product'
		fields:
			------
			------
```

### `fields`

**Description:** Fields, also known as attributes or columns, are individual data elements within an entity. Each field represents a specific piece of information about the entity.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | Mandatory |  |  |

**Example Usage:**

```yaml
entities:
# Let's create our first entity 'retailer'
  - name: retailer
    sql:
      query: 
      >
        SELECT *
        FROM
          icebase.supply_chain.retailer_info
      columns:
        - name: retailer_id
        - name: type
        - name: name
        - name: chain
        - name: state
        - name: city
      verified: true
      tables:
        - icebase.supply_chain.retailer_info
    fields:
      - name: retailer_id
        type: string
        description: unique identifier of the retailer
        column: retailer_id
        primary: true
```

### `name`

**Description:** Name of the field.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | Mandatory |  |  |

### `type`

**Description:** Type of the field.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | Mandatory |  |  |

### `description`

**Description:** Description of the field.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | Mandatory |  |  |

### `columns`

**Description:** It maps your field to the column in the physical table.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | Mandatory |  |  |

### `primary`

**Description:** Use this property to explicitly state whether the field needs to be considered a primary key.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | Mandatory |  |  |

### `Dimensions`

Description: The Lens dimensions are columns containing qualitative data; they are groupable and can be used to query measures to varying levels of granularity.

Dimensions can be - 

- An attribute that can directly reference a column of the underlying table, or
- A derived value calculated using a SQL expression

For instance, dimensions for a *Customer entity* might include first name, last name, email, phone, location, and age. 

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | Mandatory |  |  |

**Example Usage:**

```yaml

```

### name

**Description:** Name of the dimension.

Similar to naming entities and fields, the following rules can be adopted when naming dimensions.

- The dimension name should start with a lowercase letter.
- It can contain a letter, number, or ‘_’
- It needs a minimum length of 2 characters and cannot exceed 128 characters.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | Mandatory |  |  |

**Example Usage:**

```yaml

```

### description

**Description:** Description of the dimension to better understand the defined dimension. They also add clarity around its purpose and usage.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | Mandatory |  |  |

**Example Usage:**

```yaml

```

### type

**Description:** nsion. You can assign various types to a dimension. Dimension’s **expected value type** includes -

`string`, `number`, `date`, `bool`

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | Mandatory |  | string, number, date, bool |

**Example Usage:**

```yaml

```

### sql_snippet

**Description:** A query to extract dimensions from the physical table. You can add any valid SQL expression to define a dimension. A field, dimension, or measure must already be defined if referenced while defining a dimension.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | Mandatory |  |  |

**Example Usage:**

```yaml
dimensions:
     - name: duration
       type: number
       sql_snippet: day(current_date - created_on)
```

## `sub_query`

Within the dimension, you can use the subquery feature to reference measures from other entities. 

<aside>
🗣 **Note:** sub_query can only be used to refer to a measure.

</aside>

In this example, we are referencing the measure **sum_amount** in dimension **total.**

```yaml
name: sample
contract: test01
owner: xxx
entities:
  - name: order
    sql:
      query: SELECT * FROM icebase.retail.orders
    fields:
			------
			------
    dimensions:
			------
		measures:
		 - name: **sum_amount**
		   type: sum
			 sql_snippet: order_amount
		
			
	- name: customer
		sql:
			query: SELECT * FROM icebase.retail.customers
		fields:
			------
			------
		dimensions:
	    - name: **total**
        type: number
				sql_snippet: $(**order.sum_amount**)
				sub_query: true
```

A correlated subquery in SQL will look like this -

```sql
SELECT 
    customer_name,
    city,
    (SELECT SUM(order_amount) , customer_id
     FROM orders
     JOIN customers ON orders.customer_id = customers.id) as total
FROM
    customers group by customer_id
ORDER BY total DESC
LIMIT 5;
```

## `hidden`

Hidden can be used to hide a dimension from the User Interface. Dimensions mainly used for deriving another dimension or measure and not needed for exploration can be hidden.

## Measure

## `name`

For naming a measure, the following rules should be adopted.

- The measure’s name should start with a lowercase letter.
- It can contain a letter, number, or ‘_’
- It needs a minimum length of 2 characters and cannot exceed 128 characters.

## `description`

Adding descriptions about a measure helps bring consensus between teams around the measure definition. 

## `type`

You can work with different types when defining measures. The `sql_snippet` parameter is required for all measures. You can reference a column directly, specify the aggregate type, or specify SQL expression to calculate a measure.

Supported **measure types:**

| Type | Description |
| --- | --- |
| number | All numerical values returned after expression execution. |
| count | Count of all values. |
| count_distinct | Count all distinct values. |
| count_distinct_approx | Gives an approx count of values in a column. |
| sum | Calculate the sum across all values. |
| average | Calculate the average across all values. |
| min | Calculate the minimum across all values. |
| max | Calculate the maximum across all values. |
| running_total | Calculates cumulative sum. The granularity will return the value's sum if it is not defined. |

Let’s dive into different types that can be assigned to a measure

## `number`

A valid SQL expression that returns a number or an integer can be assigned a number type. You can use a ‘number’ type measure if your expression results in an aggregated value.

```yaml
measure:
 - name: add_to_cart_activity_frequency
   type: number
   sql_snippet: count_if (events_event_name = 'Add_to_Cart')
```

## `count`

Gives the count of values for a column. It’s similar to the SQL count function. It accepts a valid sql expression as long as it returns a column. The count type expects a column.

```yaml

	entity:
- name: product
  sql:
   - query: SELECT * FROM icebase.test.products
   ----
   ----
	fields:
	 - name: quantity
     type: number
     column: quantity
   ----
   ----
	measure:
	 - name: total_quantity
	   type: count
	   sql_snippet: ${product.quantity}
```

## `count_distinct`

Measure declared as type ‘count_distinct’ calculates the count of unique values within a column. Measure type ‘count_distinct’ expects a column from the sql_snippet.

## `count_distinct_approx`

Measure declared as type ‘count_distinct_approx’ returns the approximate number of unique non-null values. It provides responsiveness in cases where the dataset is large and there are large no. of distinct values.

## `sum`

Measure declared as type ‘sum’ calculates the sum of values within a column. Measure type ‘sum’ expects a column from the sql_snippet.

```yaml
# measure to calculate total sales
measure:
 - name: total_sales
   sql_snippet: ${orders.amount}
   type: sum
```

## `avg`

Measure declared as type ‘avg’ returns an average of values within a column. Measure type ‘avg’ expects a column from the sql_snippet.

```yaml
# measure to calculate avg sales 
measure:
 - name: avg_sales
   sql_snippet: ${orders.amount}
   type: avg
```

## `min`

Measure declared as type ‘min’ returns a minimum of values given in the snippet. Measure type ‘min’ expects a column from the sql_snippet.

```yaml
entity:
 - name: orders
   sql:
    - query: select * from icebase.test.orders
   ----
   ----
# measure to identify the first purchase date
	 measure:
	  - name: first_purchase_date
      sql_snippet: ${orders.created_on} 
      type: min
```

## `max`

Measure declared as type ‘min’ returns a maximum of values in a column. Measure type ‘min’ expects a column from the sql_snippet.

## `running_total`

Typically measure having the type running_total calculates the cumulative sum of values. It does a summation of current values and previous values in a column. For instance, it’s helpful when you want to get revenue till a specific date or stock in inventory to date.

```yaml
# measure to calculate stock till a specific date
	 measure:
	  - name: stock_till_date
      sql_snippet: ${product.quantity} 
      type: running_total
```

## `sql_snippet`

Allows you to define complex SQL expressions that column type measure is incapable of. It needs to be ensured that the measure type is correctly specified based on the value that sql_snippet is expected to return.

```yaml
measure:
 - name: month_since_signup
   sql_snippet: date_diff('month' , min(created_on) , current_date)
   type: number
```

## `rolling_window`

To calculate an aggregated measure within a defined window(day, week, month, etc.), you can use the rolling window property. 

The ‘**Offset**’ parameter value can be set as *start* or *end* depending on the date range you select. 

**‘Leading’ and ‘Trailing’ parameters** define the window size. The trailing parameter specifies the size of a window part before the offset point and the leading parameter specifies the size after the offset point. The window size can be defined using the combination of integer and time period → `(+/-Integer)(minute | hour | day | week | month | year)`. Use the keyword unbounded to define an infinite size for the window.

```yaml
name: sample
contract: test01
owner: xxx
entities:
  - name: order
    sql:
      query: SELECT * FROM icebase.retail.orders
    fields:
			------
			------
    dimensions:
			------
		measures:
		- name: count_of_cust_rolling_window
      sql_snippet: ${entity_id}
      type: count
      rolling_window:
         trailing: 1 month
         offset: start
```

## `hidden`

If the value is set to true the measure will not be shown on the user interface.

# Relationships

## `type`

It helps you define the type of relationship between joined entities. Following are the supported relationship types -

| Type | Description |
| --- | --- |
| 1:1 | A one-to-one relationship with the other entity. A record in one entity is associated with exactly one record in another. |
| 1:N | One to many relationships with the other entity. A record in one entity is associated with multiple records in another entity. |
| N:1 | Many to one relationship with the other entity. Relationship between more than one record of an entity with a single record in another entity.  |

## `field`

The joining key of the main entity that will be used to join the entities.

```yaml
entities:
 - name: order
----
----
----
# Defining N:1(many orders associated with one customer) relationship of orders entity with customer. 
# Referring to customer_index field of order's entity in the field property
	 relationships:
	  - type: N:1
	    field: customer_index
```

## `target`

The target entity with which you want to join your main entity.

| Properties | Description |
| --- | --- |
| name | Name the target entity with which the main entity needs to be joined. |
| field | Key that will be used in joining two entities |

```yaml
entities:
 - name: order
----
----
----
	 relationships:
	  - type: N:1
	    field: customer_id
# target entity with which main entity will be joined
      target:
# name of the target entity
        name: customer
# field that will be used to join two entities
        field: customer_id
      verified: true
```

## `description`

The description helps build context among teams. You can add descriptions to share the context of established relationships and defined criteria.

## `sql_snippet`

The sql_snippet property aids in adding further criteria in the join clause. You can use ‘and’ or ‘or’ keywords to add the requirements.

```yaml
relationships:
  - type: 1:N
    field: entity_id
    target:
      name: checkedout
      field: entity_id
 # additional criteria in the join clause
    sql_snippet: and  ${visitedcampaign.ts_} < ${checkedout.ts_}
    verified: true
```