# Relationships

The relationship makes it easy for users to query dimensions and measure from multiple entities. It allows users to define relations between different entities. All joins are generated as Left Joins. The entity in which the relationship is defined serves as the main table for the left join. Considering the direction of joining is imperative to get the desired results.

## Properties

### **`type`**

It helps you define the type of relationship between joined entities. Following are the supported relationship types -

| Type | Description |
| --- | --- |
| 1:1 | A one-to-one relationship with the other entity. A record in one entity is associated with exactly one record in another. |
| 1:N | One to many relationships with the other entity. A record in one entity is associated with multiple records in another entity. |
| N:1 | Many to one relationship with the other entity. Relationship between more than one record of an entity with a single record in another entity.  |

### **`field`**

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

### **`target`**

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

### **`description`**

The description helps build context among teams. You can add descriptions to share the context of established relationships and defined criteria.

### **`sql_snippet`**

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