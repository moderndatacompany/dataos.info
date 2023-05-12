# Query Pushdown Streamlit Application

## Code Snippet 1: Migrations for Database

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

## Code Snippet 2: Database Primitive/Resource YAML

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
        stack: flare:3.0
        compute: runnable-default
        flare:
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

## Code Snippet 5: Streamlit Application Code

```python
import webbrowser

import requests
import streamlit as st
from streamlit.components.v1 import components

api_url = "https://touched-rattler.dataos.app/order-summary/api/v1/order_summary_search?document_vectors=phfts(english).{0}"

st.markdown("<h1 style='text-align: center; color: black;'>Order 360</h1>", unsafe_allow_html=True)

st.write("\n")
st.write("\n")
st.markdown("Please Enter Order Id: (Sample Order ID ORD-5000, ORD-5001, ORD-5002...)")
order_id = st.text_input("", value="")

if len(order_id) < 8:
    st.write("Please enter valid order id")
else:
    st.write("API Call: {}".format(api_url.format(order_id)))
    try:
        data = requests.get(api_url.format(order_id)).json()
        if len(data) == 0:
            st.write("Please enter valid order id")
        else:
            st.subheader("*Order Information*")

            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown("*Order Id:*")
                st.write(data[0]['order_id'])

            with col3:
                st.markdown("*Timestamp:*")
                st.write(data[0]['order_ts'])

            st.markdown("""-------------""")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.markdown("*Total Products:*")
                st.write("{0}".format(data[0]['total_products']))

            with col3:
                st.markdown("*Total Quantities:*")
                st.write("{0}".format(data[0]['total_order_quantity']))

            st.markdown("""-------------""")

            st.subheader("*Customer Information*")

            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown("*Name:*")
                st.write(data[0]['retailer_name'])
            with col2:
                st.markdown("*Type:*")
                st.write(data[0]['retailer_type'])
            with col3:
                st.markdown("*Chain:*")
                st.write(data[0]['retailer_chain'])

            st.markdown("""-------------""")

            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown("*State:*")
                st.write(data[0]['retailer_state'])

            with col2:
                st.markdown("*City:*")
                st.write(data[0]['retailer_city'])

            st.markdown("""-------------""")

            st.subheader("*Shipment Information*")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown("*Shipment Type:*")
                st.write(data[0]['shipment_type'])
            with col3:
                st.markdown("*Shipment Cost:*")
                st.write("{0}".format(data[0]['total_shipment_cost']))

    except:
        print()
```

## Code Snippet 6: Docker File

```docker
FROM python:3.7.6
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD streamlit run decision-product.py --server.port 8501 --server.address "0.0.0.0" --server.baseUrlPath /decission_product
```

## Code Snippet 7: Requirements File

```python
altair==4.2.0
attrs==22.1.0
backports.zoneinfo==0.2.1
blinker==1.5
cachetools==5.2.0
certifi==2022.9.24
charset-normalizer==2.1.1
click==8.1.3
commonmark==0.9.1
cycler==0.11.0
decision==0.3.1
decorator==5.1.1
entrypoints==0.4
fonttools==4.37.3
gitdb==4.0.9
GitPython==3.1.27
graphviz==0.20.1
idna==3.4
importlib-metadata==4.12.0
importlib-resources==5.9.0
Jinja2==3.1.2
jsonschema==4.16.0
kiwisolver==1.4.4
MarkupSafe==2.1.1
matplotlib==3.5.3
numpy==1.21.6
packaging==21.3
pandas==1.3.5
Pillow==9.2.0
pkgutil-resolve-name==1.3.10
protobuf==3.20.1
pyarrow==9.0.0
pydeck==0.8.0b3
Pygments==2.13.0
Pympler==1.0.1
pyparsing==3.0.9
pyrsistent==0.18.1
python-dateutil==2.8.2
pytz==2022.2.1
pytz-deprecation-shim==0.1.0.post0
requests==2.28.1
rich==12.5.1
seaborn==0.12.0
semver==2.13.0
six==1.16.0
smmap==5.0.0
streamlit==1.13.0
toml==0.10.2
toolz==0.12.0
tornado==6.2
trino==0.316.0
typing-extensions==4.3.0
tzdata==2022.4
tzlocal==4.2
urllib3==1.26.12
validators==0.20.0
zipp==3.8.1
```