---
search:
  exclude: true
---

# Working with Transitive Joins

## Overview

Joins are powerful concepts within Lens, allowing you to define relationships between two entities. You can query multiple measures and dimensions from different entities without worrying about join logic. Under the hood, Lens will generate the join logic to perform joins.

Before defining the relationship between entities, it is imperative to understand the direction of joins to get accurate results. And, in cases where you have to join entities that don’t have a direct relationship with each, carefully considering the join type and where you are defining the relationship helps generate the right results.

## Transitive Joins

Let’s explore different join scenarios and whether they will work or not.

We have a retail lens

```yaml
name: retail
description: Retail lens on Transactional  Data
contract: xxx
owner: iamgroot
```

Let’s say we have three entities Transaction, Product, and Customer. 

Customer

```yaml
- name: customer
  description: A Customer entity having information about customers
  sql:
  -----
  -----
  -----
  fields:
    - name: ids
      description: Unique identifier of a customer
      type: string
      primary: true
      column: id
    - name: customer_index
      type: number
      column: customer_index
  dimensions:
    - name: payment_method
      type: string
      sql_snippet: case when annual_income='$100k-$150k' then 'Credit Card' when annual_income='$25k-$35k' then 'Debit Card' when annual_income='$50k-$75k' then 'Credit Card' when annual_income='$75k-$100k' then 'Cash' when annual_income='<$15k' then 'EMI' when annual_income='$15k-$25k' then 'Cheque' when annual_income='$35k-$50k' then 'Electronic Mobile Payment' when annual_income='$150k-$200k' then 'Cash' else 'Crypto Currency' end
    - name: annual_income_avg
      type: number
      sql_snippet: case when annual_income='$100k-$150k' then 125000 when annual_income='$25k-$35k' then 30000 when annual_income='$50k-$75k' then 60000 when annual_income='$75k-$100k' then 87500 when annual_income='<$15k' then 7500 when annual_income='$15k-$25k' then 20000 when annual_income='$35k-$50k' then 42500 when annual_income='$150k-$200k' then 175000 else 200000 end
```

Product

```yaml
- name: product
  description: A product item that can be sold
  sql:
  -----
  -----
  fields:
    - name: product_id
      description: Unique identifier of a Product
      type: string
      primary: true
      column: product_id
    - name: product_name
      type: string
      column: product_name
    - name: category_name
      type: string
      column: product_name
    - name: sale_price
      type: number
      column: product_name
    - name: list_price
      type: number
      column: product_name
    - name: brand_name
      type: string
      column: product_name
  dimensions:
    - name: refund_count_per_users
      type: number
      sql_snippet: ${transaction.refund_count_per_user}
      sub_query: true
  measures:
    - name: avg_refund_count_users
      type: avg
      sql_snippet: refund_count_per_users
```

Suppose you want to query a measure from a product and slice and dice it with a dimension from a customer entity. In that case, you will need to have either direct or an associative relationship b/w both entities. Currently, there is no direct relationship between the customer and the product entity.

Transaction

```yaml
entities:
  - name: transaction
    sql:
    ------
    fields:
      - name: order_ids
        type: string
        column: order_id
        primary: true
    -----
    -----
    dimensions:
    -----
    -----
      - name: received_any_campaign
        type: string
        sql_snippet: case when created_on not  between current_date and current_date + interval '-2' month and campaign_id is null then true else false end
    measures:
      - name: avg_order_amount
        sql_snippet: saleprice * quantity
        type: avg
      - name: second_purchase
        sql_snippet: case when cardinality(array_distinct(array_agg(created_on order by created_on))) > 1 then true else false end
        type: number
```

Though, both customer and product entities have direct relationships with transactions. One way to establish a relationship between the customer and product entity is to define a many-to-one relationship within the transaction entity with both the product and customer entity.

```yaml
  relationships:
    - type: N:1
      field: sku_id
      target:
        name: product
        field: product_id
      verified: true
    - type: N:1
      field: customer_index
      target:
        name: customer
        field: customer_index
      verified: true
```

Joins are directed. If Lens cannot resolve a join path between two entities, it will throw an error. In the above case, within the transaction entity, we had defined, Transaction → Product(Left Join transaction with the product) and Transaction → Customer(Left Join transaction with the customer). Thus, Customer ← Transaction → Product results in an association between the customer and product entity.

Suppose you have defined a relationship between transaction and product within the transaction entity, i.e., Transaction → Product (Left join Transaction with Product). 

```yaml
entities:
  - name: transaction
    -----
    -----
    fields:
    -----
    -----
    dimensions:
      - name: year
        type: number
        sql_snippet: year(created_on)
        ----
        ----
    measures:
        ----
        ----
      - name: second_purchase
        sql_snippet: case when cardinality(array_distinct(array_agg(created_on order by created_on))) > 1 then true else false end
        type: number
    relationships:
      - type: N:1
        field: sku_id
        target:
          name: product
          field: product_id
        verified: true
```

And the relationship between customer and transaction is defined in the customer entity, i.e., Customer → Transaction(Left Join Customers with Transaction). 

```yaml
  - name: customer
    description: A Customer entity having information about customers
    sql:
    -------
    -------
    fields:
    -------
    -------
    dimensions:
      - name: payment_method
        type: string
        sql_snippet: case when annual_income='$100k-$150k' then 'Credit Card' when annual_income='$25k-$35k' then 'Debit Card' when annual_income='$50k-$75k' then 'Credit Card' when annual_income='$75k-$100k' then 'Cash' when annual_income='<$15k' then 'EMI' when annual_income='$15k-$25k' then 'Cheque' when annual_income='$35k-$50k' then 'Electronic Mobile Payment' when annual_income='$150k-$200k' then 'Cash' else 'Crypto Currency' end
      - name: annual_income_avg
        type: number
        sql_snippet: case when annual_income='$100k-$150k' then 125000 when annual_income='$25k-$35k' then 30000 when annual_income='$50k-$75k' then 60000 when annual_income='$75k-$100k' then 87500 when annual_income='<$15k' then 7500 when annual_income='$15k-$25k' then 20000 when annual_income='$35k-$50k' then 42500 when annual_income='$150k-$200k' then 175000 else 200000 end
    relationships:
      - type: 1:N
        field: customer_index
        target:
          name: transaction
          field: customer_index
        verified: true
```

This results in Customer → Transaction → Product. As A→B(read ‘→’ as ‘is related to) and B→C, it will automatically infer the join path between customer and product.

## Limitations

If you have defined a relationship between product and transaction within the product entity, i.e., Product → Transaction(Left join product with the transaction). 

```yaml
- name: product
    description: A product item that can be sold
    sql:
      query: SELECT * FROM icebase.campaign.products
     -----
     -----
    fields:
      - name: product_id
        description: Unique identifier of a Product
        type: string
        primary: true
      -----
      -----
    dimensions:
    ----
    ----
    measures:
    ----
    ----
    relationships:
      - type: 1:N
        field: product_id
        target:
          name: transaction
          field:  sku_id
        verified: true
```

And, if a relationship between customer and product is defined, i.e., Customer → Transaction resulting in Customer → Transaction ← Product. The lens will never be able to resolve the joint path between customer and product. Thus, you will not be able to join these three entities.

```yaml
  - name: customer
    description: A Customer entity having information about customers
    sql:
      query: SELECT * FROM icebase.campaign.customers
      -----
      -----
    fields:
      - name: ids
        description: Unique identifier of a customer
        type: string
        primary: true
        column: id
    dimensions:
    -----
    -----
    -----
    relationships:
      - type: 1:N
        field: customer_index
        target:
          name: transaction
          field: customer_index
        verified: true
```