# Query Pushdown SSL Postgres

## Code Snippet 1: Database Migration File

```sql
CREATE TABLE IF NOT EXISTS order_summary(
  __metadata jsonb NOT NULL,
  total_products INT NULL,
  total_order_quantity INT NULL,
  total_shipment_cost INT NULL,
  shipment_type varchar(255) NULL,
  order_id varchar(255) NULL,
  order_ts TIMESTAMP WITH TIME ZONE NULL,
  retailer_type varchar(255) NULL,
  retailer_name varchar(255) NULL,
  retailer_chain varchar(255) NULL,
  retailer_state varchar(255) NULL,
  retailer_city varchar(255) NULL,
  created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT (NOW() at time zone 'utc'),
  updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT (NOW() at time zone 'utc'),
  PRIMARY KEY (order_id)
);

CREATE TABLE IF NOT EXISTS order_summary_search (
  total_products INT NULL,
  total_order_quantity INT NULL,
  total_shipment_cost INT NULL,
  shipment_type varchar(255) NULL,
  order_id varchar(255) NULL,
  order_ts TIMESTAMP WITH TIME ZONE NULL,
  retailer_type varchar(255) NULL,
  retailer_name varchar(255) NULL,
  retailer_chain varchar(255) NULL,
  retailer_state varchar(255) NULL,
  retailer_city varchar(255) NULL,
  document_vectors tsvector NOT NULL,
  cdc_at timestamp without time zone NOT NULL,
  UNIQUE(order_id)
);

CREATE
OR REPLACE FUNCTION update_order_summary_table() RETURNS TRIGGER AS $ update_order_summary_table $ DECLARE new_uuid VARCHAR(255);

BEGIN new_uuid = new.order_id;

BEGIN
INSERT INTO
  order_summary_search (
    total_products,
    total_order_quantity,
    total_shipment_cost,
    shipment_type,
    order_id,
    order_ts,
    retailer_type,
    retailer_name,
    retailer_chain,
    retailer_state,
    retailer_city,
    document_vectors,
    cdc_at
  )
SELECT
  s_view.total_products,
  s_view.total_order_quantity,
  s_view.total_shipment_cost,
  s_view.shipment_type,
  s_view.order_id,
  s_view.order_ts,
  s_view.retailer_type,
  s_view.retailer_name,
  s_view.retailer_chain,
  s_view.retailer_state,
  s_view.retailer_city,
  (
    setweight(to_tsvector('BLANKSEARCHEXPR'), 'A') || setweight(
      to_tsvector(
        coalesce(
          array_to_string(
            regexp_split_to_array(s_view.order_id, '\\\\/|:|\\\\.|\\\\s'),
            ', '
          ),
          ''
        )
      ),
      'A'
    )
  ) AS document_vectors,
  NOW() AS cdc_at
FROM
  (
    SELECT
      total_products,
      total_order_quantity,
      total_shipment_cost,
      shipment_type,
      order_id,
      order_ts,
      retailer_type,
      retailer_name,
      retailer_chain,
      retailer_state,
      retailer_city
    FROM
      order_summary
    WHERE
      order_id = new_uuid
  ) AS s_view ON CONFLICT (order_id) DO
UPDATE
SET
  total_products = excluded.total_products,
  total_order_quantity = excluded.total_order_quantity,
  total_shipment_cost = excluded.total_shipment_cost,
  shipment_type = excluded.shipment_type,
  order_id = excluded.order_id,
  order_ts = excluded.order_ts,
  retailer_type = excluded.retailer_type,
  retailer_name = excluded.retailer_name,
  retailer_chain = excluded.retailer_chain,
  retailer_state = excluded.retailer_state,
  retailer_city = excluded.retailer_city,
  document_vectors = excluded.document_vectors,
  cdc_at = excluded.cdc_at;

RETURN NULL;

END;

END;

$ update_order_summary_table $ LANGUAGE plpgsql;

CREATE CONSTRAINT TRIGGER update_order_summary_table
AFTER
INSERT
  OR
UPDATE
  ON order_summary DEFERRABLE INITIALLY DEFERRED FOR EACH ROW EXECUTE PROCEDURE update_order_summary_table();

CREATE INDEX part_doc_vec_idx ON order_summary_search USING GIN (document_vectors);
```

## Code Snippet 2: Database Resource YAML

```yaml
version: v1
name: ordersumdb
type: database
description: part search database.
tags:
  - database
database:
  migrate:
    includes:
      - /migrations_poc
    command: up
```

## Code Snippet 3: Beacon Service YAML

```yaml
version: v1
name: order-summary-search
type: service
tags:
  - syndicate
  - service
service:
  replicas: 1
  compute: runnable-default
  ingress:
    enabled: true
    stripPath: true
    path: /order-summary/api/v1
    noAuthentication: true
  stack: beacon+rest
  envs:
    PGRST_OPENAPI_SERVER_PROXY_URI: https://touched-rattler.dataos.app/order-summary/api/v1/order-summary/api/v1
  beacon:
    source:
      type: database
      name: ordersumdb
      workspace: public
  topology:
  - name: database
    type: input
    doc: order search database connection
  - name: rest-api
    type: output
    doc: serves up the order search database as a RESTFUL API
    dependencies:
      - database
```

## Code Snippet 4: Flare Job YAML

```yaml
---
version: v1
name: order-summ-data
type: workflow
description: This jobs query lens and write data to postgres table
workflow:
  title: Order Summary
  dag:
    - name: order-summary-data
      title: Order Summary
      spec:
        stack: flare:5.0
        compute: runnable-default
        stackSpec:
          job:
            explain: true
            inputs:
              - name: input_order
                query: |
                  SELECT
                    "product.total_products" as total_products,
                    "order_shipment.total_order_quantity" as total_order_quantity,
                    cast("order_shipment.total_shipment_cost" as int) as total_shipment_cost,
                    "order_shipment.shipment_type" as shipment_type,
                    "order.order_id" as order_id,
                    "order.order_date" as order_ts,
                    "retailer.type" as retailer_type,
                    "retailer.name" as retailer_name,
                    "retailer.chain" as retailer_chain,
                    "retailer.state" as retailer_state,
                    "retailer.city" as retailer_city
                  FROM
                    LENS (
                      SELECT
                        "product.total_products",
                        "order_shipment.total_order_quantity",
                        "order_shipment.total_shipment_cost",
                        "order_shipment.shipment_type",
                        "order.order_id",
                        "order.order_date",
                        "retailer.type",
                        "retailer.name",
                        "retailer.chain",
                        "retailer.state",
                        "retailer.city"
                      FROM
                        supplychain
                    )
                options:
                  SSL: "true"
                  driver: "io.trino.jdbc.TrinoDriver"

            logLevel: INFO

            outputs:
              - name: output01
                depot: dataos://ordersumdbdatabase:public?acl=rw
                driver: org.postgresql.Driver
            steps:
              - sink:
                - sequenceName: input_order
                  datasetName: order_summary
                  outputName: output01
                  outputType: JDBCQuery
                  outputOptions:
                    query:
                      INSERT INTO order_summary (__metadata, total_products, total_order_quantity, total_shipment_cost, shipment_type, order_id, order_ts,  retailer_type, retailer_name, retailer_chain, retailer_state, retailer_city) VALUES ( to_json(?::JSONB), ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?) ON CONFLICT (order_id) DO UPDATE SET __metadata = excluded.__metadata, total_products = excluded.total_products, total_order_quantity = excluded.total_order_quantity, total_shipment_cost = excluded.total_shipment_cost, shipment_type=excluded.shipment_type, order_id = excluded.order_id, order_ts = excluded.order_ts, retailer_type = excluded.retailer_type, retailer_name= excluded.retailer_name, retailer_chain= excluded.retailer_chain, retailer_state= excluded.retailer_state, retailer_city= excluded.retailer_city
```