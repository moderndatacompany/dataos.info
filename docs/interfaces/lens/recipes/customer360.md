---
search:
  exclude: true
---

# Customer360

The 360-degree view of the customer includes every interaction, from a website inquiry to a product purchase to a customer support ticket. A comprehensive 360-degree view of the customers has economic benefits like increased revenues with better cross-selling and up-selling opportunities. Organizations can also support better customer experience for more personalized marketing experiences - driving higher conversation rates and revenues.

Customer 360 allows businesses to target specific clusters of customers with communications that are much more relevant for their particular behavior - and thus generate much higher response rates, plus increased loyalty and customer lifetime value. Businesses today have extensive data on their existing customers - such as purchase history, browsing history, prior campaign response patterns, and demographics - that can be used to identify specific groups of customers that can be addressed.

The biggest challenges in implementing a customer 360 are the fragmentation and inconsistency of data. This data is often stored in various data stores and across disparate systems, lacking a standardized format, exact dimensions, or a consensus on definitions. The issue is multifaceted for teams designing the customer 360, as they must decide on a list of measures. Questions arise, such as whether these measures are understood across the organization, which set of records should be considered in measure calculations, what the roll-up strategy should be, and which dimensions should be considered for aggregations.

> DataOS Lens can address the above challenges.

## Customer360 Lens

Customer 360 Lens is a implementation of DataOS Lens following the activity-schema standard. At its core, an activity schema is a data modeling paradigm consisting of two major concepts - customer and their activity stream. It models an entity taking a sequence of activities over time. For example, a customer(entity) viewed a web page(activity),  purchased a product(activity), raised a complaint(activity) etc. Each row in the activity stream represents a single activity taken by the entity at a time. Every activity has metadata associated with it beyond the customer, the activity, and the timestamp. A ‘purchased product’ activity will want to store the actual SKU id of the product, brand, supplier, and product price. One can extend this concept to create company 360, product 360, vendor 360, etc.

There are two core entities to the customer360 Lens - customer and activity stream. Then one can extend the activity stream entity to create complementary entities to support different use cases. Here we have three entities that are extensions of the activity stream

1. order placed stream
2. order rejected stream
3. order invoiced stream

One can answer the following questions from the lens which can be analyzed across customer and product dimensions

1. RFM measures
2. Percentage of orders rejected or invoiced
3. The average number of days taken to invoice an order
4. Customers with the count of rejected orders last month greater than the annual average
5. Many more.

| Entity | Related To | Relationship | Fields and Dimensions | Measure |
| --- | --- | --- | --- | --- |
| customer | `order_placed`, <br> `order_rejected`, <br> `order_invoiced` | `1:N`, <br> `1:N`, <br> `1:N` | `customer_id`, `customer_name`, `email`, `phone_number`, `address`, `customer_no`, `state`, `county_name`, `zip`, `premise_code`, `license_classification`, `license_type`, `channel_code`, `selling_division_name`, `site`, `consent` | `count_customers`, `percentage_email`, `percentage_phone`, `percentage_address` |
| order_placed | `order_rejected`, <br> `order_invoiced` | `1:1`, <br> `1:1` | `activity_uuid`, `entity_id`, `order_id`, `product_id`, `product_classification`, `cases`, `order_value`, `request_delivery_date`, `activity_occurence`, `activity_repeated_at`, `brand_name`, `supplier_name`, `product_category`, `order_no` | `recency`, `frequency`, `monetary` |
| order_rejected | `customer` | `N:1` | `activity_uuid`, `entity_id`, `ref_order_id`, `activity_ts`, `product_id`, `order_reject_code`, `order_status_code`, `order_delivery_status`, `cases`, `bottles`, `order_value`, `request_delivery_date`, `activity_occurence`, `activity_repeated_at` |  `recency`, `frequency` |
| order_invoiced | `customer` | `N:1` | `activity_uuid`, `entity_id`, `ref_order_id`, `activity_ts`, `product_id`, `brand_name`, `supplier_name`, `product_category`, `product_classification`, `cases`, `bottles`, `order_value`, `request_delivery_date`, `activity_occurence`, `activity_repeated_at` |  |

```yaml
name: customer_360
description: Data Model to answer any questions around a customer.
contract: customer_360
owner: iamgroot
tags:
  - c360
  - activity_schema
  - segment
entities:
  - name: customer
    sql:
      query: >
        SELECT * FROM icebase.audience.customers_large_data
      columns:
        - name: customer_id
        - name: customer_name
        - name: email
        - name: phone_number
        - name: address
        - name: customer_no
        - name: site
        - name: state
        - name: county_name
        - name: zip
        - name: premise_code
        - name: status
        - name: license_classification
        - name: license_type
        - name: channel_code
        - name: channel_name
        - name: selling_division_name
        - name: consent
      verified: true
      tables:
        - icebase.audience.customers_large_data
    fields:
      - name: customer_id
        type: string
        description: unique identifier of the customer
        column: customer_id
        primary: true
        tags:
          - customer_identifier
      - name: customer_name
        type: string
        description: Business name the customer operates under
        column: customer_name
        tags:
          - name_identifier
      - name: email
        type: string
        description: email address of the customer
        column: email
        tags:
          - email_identifier
      - name: phone_number
        type: string
        description: contact number of the customer
        column: phone_number
        tags:
          - phone_identifier
      - name: address
        type: string
        description: postal address of the customer
        column: address
        tags:
          - address_identifier
      - name: customer_no
        type: string
        description: customer identifier only unique within the site
        column: customer_no
      - name: state
        type: string
        description: state code where the customer physical address is located
        column: state
      - name: county_name
        type: string
        description: name of the county
        column: county_name
      - name: zip
        type: string
        description: ZIP code associate with the customer physical address
        column: zip
      - name: premise_code
        type: string
        description: premise code - on prem, off prem
        column: premise_code
      - name: status
        type: string
        description: customer status - active, inactive, suspended
        column: status
      - name: license_classification
        type: string
        description: used to identify customer tier
        column: license_classification
      - name: license_type
        type: string
        description: type of license
        column: license_type
      - name: channel_code
        type: string
        description: indicates whether chain is a grocery, hotel etc
        column: channel_code
      - name: selling_division_name
        type: string
        description: internal division responsible for the order
        column: selling_division_name
      - name: site
        type: string
        description: site number
        column: site
      - name: channel_name
        type: string
        description: channel description
        column: channel_name

      - name: consent
        type: string
        description: consent to use data for recommendation
        column: consent
    measures:
      - name: count_customers
        sql_snippet: ${customer.customer_id}
        type: count
        description: count of total customers
        hidden: true
        tags:
          - total_customers
      - name: percentage_email
        sql_snippet: round(100*count(${customer.email})/cast(count(*) as double),2)
        type: number
        description: percentage customers with email
        hidden: true
        tags:
          - email_reachability
      - name: percentage_phone
        sql_snippet: round(100*count(${customer.phone_number})/cast(count(*) as double),2)
        type: number
        description: percentage customers with email
        hidden: true
        tags:
          - phone_reachability
      - name: percentage_address
        sql_snippet: round(100*count(${customer.address})/cast(count(*) as double),2)
        type: number
        description: percentage customers with email
        hidden: true
        tags:
          - address_reachability
    relationships:
      - type: 1:N
        field: customer_id
        target:
          name: order_placed
          field: entity_id
        verified: true
      - type: 1:N
        field: customer_id
        target:
          name: order_rejected
          field: entity_id
        verified: true
      - type: 1:N
        field: customer_id
        target:
          name: order_invoiced
          field: entity_id
        verified: true
  - name: order_placed
    sql:
      query: >
        SELECT 
          activity_uuid, 
          entity_id,
          trim(feature1) as order_id,
          activity_ts,
          trim(feature2) as product_id,
          trim(feature3) as brand_name,
          trim(feature4) as supplier_name,
          trim(feature5) as product_category,
          trim(feature6) as product_classification,
          cast(feature7 as double) as cases,
          cast(feature8 as double) as bottles,
          cast(feature9 as double) as order_value,
          feature10 as request_delivery_date,
          activity_occurence,
          activity_repeated_at
        FROM icebase.audience.activity_streams_large_data where activity = 'order_placed'
      columns:
        - name: activity_uuid
        - name: entity_id
        - name: activity_ts
        - name: order_id
        - name: product_id
        - name: brand_name
        - name: supplier_name
        - name: product_category
        - name: product_classification
        - name: cases
        - name: bottles
        - name: order_value
        - name: request_delivery_date
        - name: activity_occurence
        - name: activity_repeated_at
      verified: true
      tables:
        - icebase.audience.activity_streams_large_data
    fields:
      - name: activity_uuid
        type: string
        description: unique identifier of the activity event
        column: activity_uuid
        primary: true
      - name: entity_id
        type: string
        description: customer identifier
        column: entity_id
      - name: order_id
        type: string
        description: order identifier
        column: order_id
      - name: activity_ts
        type: date
        description: timestamp of the moment when activity_occured
        column: activity_ts
      - name: product_id
        type: string
        description: product identifier
        column: product_id
      - name: product_classification
        type: string
        description: classification of the product
        column: product_classification
      - name: cases
        type: number
        description: count of cases the order was placed for
        column: cases
      - name: bottles
        type: number
        description: count of bottles the order was placed for
        column: bottles
      - name: order_value
        type: number
        description: value of the order placed
        column: order_value
      - name: request_delivery_date
        type: date
        description: requested delivery date
        column: request_delivery_date
      - name: activity_occurence
        type: number
        description: how many times this activity has happened to this customer
        column: activity_occurence
      - name: activity_repeated_at
        type: date
        description: The date of the next instance of this activity for this customer
        column: activity_repeated_at
      - name: brand_name
        type: string
        description: name of the brand
        column: brand_name
      - name: supplier_name
        type: string
        description: name of the supplier
        column: supplier_name
      - name: product_category
        type: string
        description: category of the product
        column: product_category
    dimensions:
      - name: order_no
        type: string
        description: unique order_no for a customer
        sql_snippet: concat(${order_placed.entity_id},'-',split_part(${order_placed.order_id},'-',1))
        hidden: true
    measures:
      - name: recency
        sql_snippet: day(current_date - ${order_placed.activity_ts})
        type: min
        description: days since last order was placed
      - name: frequency
        sql_snippet: ${order_placed.order_no}
        type: count_distinct
        description: count of total activities
      - name: monetary
        sql_snippet: ${order_placed.order_value}
        type: sum
        description: total order value
    relationships:
      - type: 1:1
        field: order_id
        target:
          name: order_rejected
          field: ref_order_id
      - type: 1:1
        field: order_id
        target:
          name: order_invoiced
          field: ref_order_id

  - name: order_rejected
    sql:
      query: >
        SELECT 
          activity_uuid, 
          entity_id,
          trim(feature1) as ref_order_id,
          activity_ts,
          trim(feature2) as product_id,
          trim(feature3) as order_reject_code,
          trim(feature4) as order_status_code,
          trim(feature5) as order_delivery_status,
          cast(feature7 as double) as cases,
          cast(feature8 as double) as bottles,
          cast(feature9 as double) as order_value,
          feature10 as request_delivery_date,
          activity_occurence,
          activity_repeated_at
        FROM icebase.audience.activity_streams_large_data where activity = 'order_rejected'
      columns:
        - name: activity_uuid
        - name: entity_id
        - name: ref_order_id
        - name: activity_ts
        - name: product_id
        - name: order_reject_code
        - name: order_status_code
        - name: order_delivery_status
        - name: cases
        - name: bottles
        - name: order_value
        - name: request_delivery_date
        - name: activity_occurence
        - name: activity_repeated_at
      verified: true
      tables:
        - icebase.audience.activity_streams_large_data
    fields:
      - name: activity_uuid
        type: string
        description: unique identifier of the activity event
        column: activity_uuid
        primary: true
      - name: entity_id
        type: string
        description: customer identifier
        column: entity_id
      - name: ref_order_id
        type: string
        description: order identifier
        column: ref_order_id
      - name: activity_ts
        type: date
        description: timestamp of the moment when activity_occured
        column: activity_ts
      - name: product_id
        type: string
        description: product identifier
        column: product_id
      - name: cases
        type: number
        description: count of cases the order was placed for
        column: cases
      - name: bottles
        type: number
        description: count of bottles the order was placed for
        column: bottles
      - name: order_value
        type: number
        description: value of the order placed
        column: order_value
      - name: request_delivery_date
        type: date
        description: requested delivery date
        column: request_delivery_date
      - name: activity_occurence
        type: number
        description: how many times this activity has happened to this customer
        column: activity_occurence
      - name: activity_repeated_at
        type: date
        description: The date of the next instance of this activity for this customer
        column: activity_repeated_at
      - name: order_reject_code
        type: string
        description: code for rejection
        column: order_reject_code
      - name: order_status_code
        type: string
        description: code for order status
        column: order_status_code
      - name: order_delivery_status
        type: string
        description: status of order delivery
        column: order_delivery_status
    dimensions:
      - name: order_no
        type: string
        description: unique order_no for a customer
        sql_snippet: concat(${order_rejected.entity_id},'-',split_part(${order_rejected.ref_order_id},'-',1))
        hidden: true
    measures:
      - name: recency
        sql_snippet: day(current_date - ${order_rejected.activity_ts})
        type: min
        description: days since last order was cancelled
      - name: frequency
        sql_snippet: ${order_rejected.order_no}
        type: count_distinct
        description: count of total order cancelled

  - name: order_invoiced
    sql:
      query: >
        SELECT 
          activity_uuid, 
          entity_id,
          trim(feature1) as ref_order_id,
          activity_ts,
          trim(feature2) as product_id,
          trim(feature3) as brand_name,
          trim(feature4) as supplier_name,
          trim(feature5) as product_category,
          trim(feature6) as product_classification,
          cast(feature7 as double) as cases,
          cast(feature8 as double) as bottles,
          cast(feature9 as double) as order_value,
          feature10 as request_delivery_date,
          activity_occurence,
          activity_repeated_at
        FROM icebase.audience.activity_streams_large_data where activity = 'order_invoiced'
      columns:
        - name: activity_uuid
        - name: entity_id
        - name: ref_order_id
        - name: activity_ts
        - name: product_id
        - name: brand_name
        - name: supplier_name
        - name: product_category
        - name: product_classification
        - name: cases
        - name: bottles
        - name: order_value
        - name: request_delivery_date
        - name: activity_occurence
        - name: activity_repeated_at
      verified: true
      tables:
        - icebase.audience.activity_streams_large_data
    fields:
      - name: activity_uuid
        type: string
        description: unique identifier of the activity event
        column: activity_uuid
        primary: true
      - name: entity_id
        type: string
        description: customer identifier
        column: entity_id
      - name: ref_order_id
        type: string
        description: order identifier
        column: ref_order_id
      - name: activity_ts
        type: date
        description: timestamp of the moment when activity_occured
        column: activity_ts
      - name: product_id
        type: string
        description: product identifier
        column: product_id
      - name: product_classification
        type: string
        description: product classification
        column: product_classification
      - name: cases
        type: number
        description: case quantity
        column: cases
      - name: bottles
        type: number
        description: bottle quantity
        column: bottles
      - name: order_value
        type: number
        description: order value
        column: order_value
      - name: activity_occurence
        type: number
        description: how many times this activity has happened to this customer
        column: activity_occurence
      - name: activity_repeated_at
        type: date
        description: The date of the next instance of this activity for this customer
        column: activity_repeated_at
```