---
search:
  exclude: true
---

# Building Audience

There are different analytical use cases that various business personas might want to power. One such widely used use case is creating audiences. 

> 🗣 Audience: A group of people sharing common behavior, traits, characteristics, and interests.

Let’s deep dive into how you can define a lens that can help you power different audience use cases.

## Identifying recently signed-up users who made their second purchase

We want to find all the users who have recently signed up within the last two months and have made their second purchase for a product category within the previous 30 days. 

Let’s start with defining the Lens. 

```yaml
entities:
 - name: orderline
   sql:
    - query: 
      SELECT
      *,
      cast(order_id AS varchar) AS order_ids,
      concat(cast(order_id AS varchar), '-', cast(created_on AS varchar)) AS uuid
      FROM
      icebase.campaign.transactions
     columns:
		 -------
     -------
```

We need to slice and dice measures by dimensions like order_ids, created_on, customer_index, sku_id

We will need to define measures to get their last purchase, several months that have passed since the user signed up, and several times they have placed the order. 

```yaml
   measures:
    - name: last_purchase
			type: number
      sql_snippet: min(day(current_date - ${orderline.created_on}))
    - name: month_since_signup
      type: number
      sql_snippet: date_diff('month' , min(${orderline.created_on}) , current_date)
    - name: order_count
      type: count_distinct
      sql_snippet: ${orderline.order_ids)
```

Apart from an order entity, we will also need a product entity that will help us to narrow down our results to a specific product category. 

```yaml
entities:
 - name: product
   sql:
    - query: SELECT * FROM icebase.campaign.products
      columns: 
       - name: product_id
       - name: brand_name
       - name: category_name
      verified: true
      tables:
        - icebase.campaign.products
```

Following fields are needed within the product entity. 

```yaml
   fields:
    - name: product_id
      type: string
      column: product_id
      primary: true
    - name: brand_name
      type: string
      column: brand_name
    - name: category_name
      type: string
      column: category_name 
```

We will also need a city entity to narrow down to a specific state, let’s also define fields within the city entity.

```yaml
entities:
 - name: city
   sql:
    - query: SELECT * FROM icebase.campaign.city
      columns: 
      -----
      -----
   fields:
    - name: city_id
      type: string
      column: city_id
      primary: true
    - name: state
      type: string
      column: state_name
```

To be able to query measures from different data sources, we need to define the relationship between these entities. Once the relationship is defined Lens can perform join under the hood. We will define the relationship with the order entity. The order has an N:1 relationship with the product and city entity.

```yaml
entities:
 - name: order
 ---
 ---
 ---
   relationships:
    - type: N:1
      field: sku_id
      target:
        name: product
        field: product_id
    - type: N:1
      field: city_id
      target:
        name: city
        field: city_id
      verified: true
 - name: product
 ----
 ----
 ----
 - name: city
 ----
 ----
 ----
```

To know more about supported join types, refer here.

Once Lens is defined and deployed you can start querying the Lens to get the audience. So, we need - 

> 🗣 List of customers who have signed up within the last two months, have made their first purchase within the last 30 days from a Men’s Polo category, and are residents of New York City.

## Use Cases

Similarly, you can build a different audience. Given below is a set of example audiences to help you get started with building an audience.

| Use Case | Description | What’s Needed? <br> [You can include the following measures to implement the use case]
| --- | --- | --- |
| Customer’s Abandoning Cart | List all the customers who ATC a lot but then end the session before buying the product. <br> The reasons for abandoning a cart can be a high shipping cost or unavailability of size or unavailability of desired payment options. | dimensions - <br> `category_name` <br> `payment_type` <br> `shipping_cost` <br> <br> measures - <br> `avg time to purchase post atc` <br> `ATC rate` <br>  `avg conversion time` |
| A cohort of Active Users  | All the active users in a state who have: <br> - Signed up within the last 6 months <br> - Haven’t joined the app in the last 30 days <br> - Was active recently might be within the last 2 months <br> - And has placed an order in the last 6 months | dimensions - <br> `state_name` <br> `event_type` <br> `sign_up_month` <br> `last_active_month` <br> <br> measures - <br> `month_since_signup` |
| Inactive High-Value Customers | Reactivating the high-value customers who haven’t made a purchase in the last 30 days. <br> This can be the set of customers who have - <br>- Customer Lifetime value higher than a certain threshold <br> - Have performed multiple events in the app <br> - Haven’t made | dimensions - <br> `channel` <br> `event_type` <br><br> measures - <br> `event_count` <br> `CLV` <br> `order_count_in_last_30_days` |
| Likely to churn users | List all users that have viewed a product above a certain price point, but have not completed any order in  the last 30 days and were active 30 to 90 days ago, and are likely to churn(Might be product price is affecting the purchase). <br>After Identifying customers at risk of churn you can understand their pain points & engage these customers through campaigns & discounts. In the above list, we can also include customers who gave a low rating or NPV | dimensions - <br>`category_name` <br> `order_date` <br>  `product_price` <br> <br> measure <br> `event_count_last_30_days` <br> `order_count` <br> `repeat_purchase` <br> `session_count` |
| User with low cart Items | We need a list of new joiners who have fewer items in the cart during checkout. <br> Users can be prompted to increase items in the cart while they are at the checkout page. This will help increase AOV. | dimensions - <br>`category_name` <br> `event_type` <br> `new_user` <br> `received_any_campaign` (in last 2 months) <br> `order_amount` <br><br> measure <br> `count_of_line_items` <br>  OR <br> `no_of_items_in_cart`  |