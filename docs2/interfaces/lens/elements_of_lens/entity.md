# Entity

> 🗣 An object in a data model is referred to as a data entity.


An entity is your business objects such as Products, Orders, Customers, Suppliers, etc. in more layman's terms, your real-world objects. These entities interact with various business touchpoints and power your day-to-day business operations.

## Properties

### `name`

There are specific rules to follow when naming entities within a Lens -

- As a convention entity name should start with a lowercase letter.
- It can contain a letter, number, or ‘_’.
- It needs a minimum length of 2 characters and cannot exceed 128 characters.

While naming an entity, you can stick to lower_case_with_underscores.

### `sql`

This will also allow aggregating or filter the data to construct the desired entity.

SQL properties at a glance

| Property | Description |
| --- | --- |
| query | SQL query to generate a table that the entity will reference |
| column | All the columns that are referenced in the fields |
| tables | Tables that are referred to in the supplied SQL query |
| lenses | Lenses that are referred to in the supplied SQL query |

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

Columns must be specified in addition to the query property. It cannot be left empty. 

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
    fields:
      - name: uuid
        type: string
        primary: true
        column: uuid
    dimensions:
    ----
    ----
```

You can also reference and reuse the SQL expression of an existing entity to create a new entity. For instance 

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

### `extends`

An entity can be extended to reuse all declared elements. In the example below, the selected_product entity is created by referencing the activity_stream entity.

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

### `tags`

Multiple tags can be added to a lens. They aid in discoverability.

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

Within an entity other than the above-mentioned properties we also define elements such as fields, dimensions, measures, and relationships.

## Entity definition syntax

The general syntax to define entity mapping within a Lens

```yaml
name: ['Name of Lens']
contract: ['Name of Contract you are referring to']
owner: ['Owner Name']
entities:
  - name: ['Entity Name']
    SQL:
      query: > 
        SELECT
        * 
        FROM
	      table_name['Write a query to connect to the required data']						
    fields:        
      - name: col_name
        type: [string, number, date, bool]
        column: ['column_name']
	      primary: true
    dimensions:
      - name: col_name
        type: [string, number, date, bool]
        sql_snippet: 
				hidden: [true, false]
				sub_query: [true, false]
    measures:
      - name: name_of_measure
        sql_snippet: ['column or custom sql query to calculate measure']
        type: [sum, min, max, avg, count, count_distinct, count_distinct_approx, running_total, number]
				hidden: [true, false]
		relationships:
			- type: [1:N, N:1, 1:1]
				field: ['field name']
				target:
					name: ['Related entity name']
					field: ['primary field']
				sql_snippet: ['additional join conditions']
```