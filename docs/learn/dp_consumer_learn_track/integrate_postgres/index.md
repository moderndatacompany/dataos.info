# Integration with Postgres

In this topic, you'll learn how to effectively consume the 'Product360' Data Product through Postgres after confirming that it meets your use case requirements. This guide provides step-by-step instructions to help you connect and query the Data Product seamlessly.

<aside class="callout">
🗣

Note that, the consumption of the Data Product through Postgres will be unavailable in the Data Products that do not have the semantic model.

</aside>

## Prerequisites

To maximize your learning experience, ensure you have the following in place:

- An established connection with Postgres.
- PSQL  client installation.

## Steps to  consume Data Products

Follow the below steps to consume the Data Product via Postgres.

### 1. Access the Postgres section

Navigate to the **Access Options** tab of your Data Product (Product360) and select the **Postgres** section.

![pg_tab.png](/learn/dp_consumer_learn_track/integrate_postgres/pg_tab.png)

In the connection details section, you’ll be provided with the host address, port name, database details, username, and the password. Your DataOS API key is the password, you can create the DataOS API key in the token section of the DataOS profile.

![pg_apikey.png](/learn/dp_consumer_learn_track/integrate_postgres/pg_apikey.png)

### 2. Copy the connection string

Copy the provided connection string.

![pg_connection.png](/learn/dp_consumer_learn_track/integrate_postgres/pg_connection.png)

### 3. Test the connection

In your terminal, paste the copied coonection string and press enter, when prompt for the password provide your DataOS API key.

```bash
psql -h tcp.splendid-shrew.dataos.app -p 6432 -U iamgroot -d lens:public:cross-sell-affinity
Password for user iamgroot:
```

### 4. Ready to query

<aside class="callout">
🗣

Note that you can only query the Metrics, Entities, and logical tables sourced from the semantic model (Lens).

</aside>

Once connected, you're ready to execute queries. For example, you can run the following command to retrieve data:

```bash
lens:public:cross-sell-affinity=> write your query here
# example
lens:public:cross-sell-affinity=> select * from cross_sell_opportunity_score limit 10
```

## Next step

If you want to consume the Data Product via GraphQL, refer to the next topic.

[Integration with GraphQL](/learn/dp_consumer_learn_track/integrate_graphql/)