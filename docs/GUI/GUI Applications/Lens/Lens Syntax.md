# Lens Syntax

Lens defines the business data model and it can refer to other lenses. The general syntax to define entity mapping in a Lens -

```yaml
name: ['Name of Lens']
owner: ['Owner Name']
entities:
  - name: ['Entity Name']
    sql:
      query: 
        SELECT
        * 
        FROM
	      table_name['Write a query to connect to the required data']
      columns:
       - name: field_name	
    # Add all directly mapped columns to your underlying data table in field			
    fields:        
      - name: field_name
        type: [string, number, date, bool]
        column: ['column present in the underlying data table']
	      primary: true
    # Add all custom dimension 
    dimensions:
      - name: dimension_name
        type: [string, number, date, bool]
        sql_snippet: ['custom sql query to calculate dimension']
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

## An example Lens

```yaml
name: ordered_product
contract: retail
owner: XYZ
entities:
  - name: product
    sql:
      query: SELECT * FROM icebase.supply_chain.product_info
    fields:
      - name: product_id
			  description: Unique identifier of a product
        type: string
        column: product_id
        primary: true
    dimensions:
      - name: product_name
        type: string
        sql_snippet: product_name
      - name: category
        type: string
        sql_snippet: category
      - name: brands
        type: string
        sql_snippet: brands
      - name: size
        type: string
        sql_snippet: size
```

Let’s also add order entity to this lens

```yaml
    - name: order
			sql:
        query:
          SELECT 
            order_id, 
            product_ids AS "product_id", 
            quantities, 
            order_amount
          FROM 
            icebase.supply_chain.retail_order_line_item
			fields:
		    - name: order_id
	        type: string
	        sql_snippet: order_id
	        primary: true
			measures:
        - name: order_quantity
					type: sum 
          sql_snippet: quantities
        - name: total_order_value
					type: sum
          sql_snippet: order_amount
			dimensions:
				- name: ordered_at
					type: date
					sql_snippet: ordered_at
				- name: product_id
          type: string
					sql_snippet: product_id   
        - name: ordered_amount
          type: number  
					sql_snippet: order_amount
			relationships:
        - type: N:1
          field: product_id
          target: 
            name: Product
            field: product_id
					verified: true
```