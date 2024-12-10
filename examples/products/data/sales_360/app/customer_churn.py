import streamlit as st
import pandas as pd
from trino.dbapi import connect
from trino.auth import BasicAuthentication
from datetime import datetime, timedelta

# Function to fetch data from Trino database based on query
@st.cache(allow_output_mutation=True)
def fetch_data(query):
    conn = connect(
        host="tcp.liberal-donkey.dataos.app",
        port=7432,
        auth=BasicAuthentication("aayushisolanki", "dG9rZW5fdXN1YWxseV9wcmV2aW91c2x5X2RpdmluZV9tb25ncmVsLmU4M2EwOWJiLTRmZTMtNGZjMS1iMTY5LWY0NTI2MDgyZDUwZg=="),
        http_scheme="https",
        http_headers={"cluster-name": "system"}
    )
    data = pd.read_sql(query, conn)
    conn.close()
    return data

# Query to fetch churned customers with contact details
churned_customers_query = """
WITH customer_activity AS (
    SELECT
        c.customer_id,
        c.first_name,
        c.last_name,
        c.email_id,
        c.phone_number,
        MAX(t.transaction_date) AS last_transaction_date
    FROM
        icebase.sales_360.customer c
    LEFT JOIN
        icebase.sales_360.transactions t ON CAST(c.customer_id AS VARCHAR) = t.customer_id
    GROUP BY
        c.customer_id, c.first_name, c.last_name, c.email_id, c.phone_number
)

SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    c.email_id,
    c.phone_number,
    CASE
        WHEN ca.last_transaction_date < DATE_FORMAT(CURRENT_DATE - INTERVAL '90' DAY, '%Y-%m-%d') THEN 'Churned'
        ELSE 'Not Churned'
    END AS churn_status
FROM
    icebase.sales_360.customer c
LEFT JOIN
    customer_activity ca ON c.customer_id = ca.customer_id
"""

# Function to filter churned and not churned customers
def filter_customers(df, churn_status):
    filtered_df = df[df['churn_status'] == churn_status]
    return filtered_df

# Streamlit UI
def main():
    st.title('Churned Customer Details')

    # Fetch churned customers data
    churned_customers = fetch_data(churned_customers_query)

    # Sidebar filter for churn status
    st.sidebar.title('Filters')
    selected_status = st.sidebar.radio('Select Customer Status', ['Churned', 'Not Churned'])

    # Display filtered customer data
    st.subheader(f'{selected_status} Customers')
    filtered_customers = filter_customers(churned_customers, selected_status)
    st.dataframe(filtered_customers)

if __name__ == "__main__":
    main()
