# Fields

Fields are columns with a direct one-to-one mapping with the columns of your underlying data tables. Fields can contain unique identifiers too. Within a field, if the ‘primary’ property is set to True, Lens will use this as a joining key with other entities.

## Properties

### **`name`**

You need to use the following naming convention for assigning names to fields -

- It should start with a lowercase letter.
- It should contain a letter, number, or ‘_’
- It should have a minimum of 2 characters and cannot exceed 128 characters.

### **`description`**

Using the description property, you can describe and provide a better understanding of a field.

```yaml
entities:
 - name: product
   sql:
    - query: SELECT * FROM icebase.test.products
      ---
      ---
   fields:
    - name: uuid
      description: Unique product identifier
```

### **`type`**

The field supports the following column types -

- `string`
- `number`
- `date`
- `bool`

You can assign the appropriate types while declaring a field. It is recommended that the field type and the data type of the column referenced within the field match.

```yaml
entities:
 - name: product
   sql:
    - query: SELECT * FROM icebase.test.products
      ---
      ---
   fields:
    - name: uuid
      description: Unique product identifier
			type: string
```

A column must be defined as a dimension and cast into apt type if its data type is different from the field type.

### **`column`**

In this field, the property specifies the column that directly maps to your underlying data table. You cannot add a custom SQL expression.

```yaml
entities:
 - name: product
   sql:
    - query: SELECT * FROM icebase.test.products
      ---
      ---
   fields:
    - name: uuid
      description: Unique product identifier
			type: string
			column: product_id
```

### **`primary`**

This property sets the column as a primary key, enabling joins with other entities. This column will be used for matching records. It will essentially help avoid duplication of rows. 

```yaml
   fields:
    - name: uuid
      description: Unique product identifier
			type: string
			column: product_sku_id
			primary: true
```

To define a composite key you will have to define it in the SQL query of the entity itself, you cannot add sql expression in the field.

```yaml
entities:
 - name: product
   sql:
		 query: SELECT *,
						concat(cast(product_id AS varchar), '-', cast(product_sku AS varchar)) AS uuid
						FROM
						icebase.test.products
     ---
     ---
   fields:
    - name: uuid
      description: Unique product identifier
			type: string
			column: uuid
```