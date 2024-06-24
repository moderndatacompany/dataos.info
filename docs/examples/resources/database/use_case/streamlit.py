# Product Data Viewer App with Category-wise Sales Chart

# Import necessary libraries
import pandas as pd
from trino.dbapi import connect
from trino.auth import BasicAuthentication
import streamlit as st
import altair as alt

# Function to fetch data and return pandas dataframe
@st.cache(persist=True, show_spinner=False, ttl=100)
def fetch_data(query, cur):
    cur.execute(query)
    rows = cur.fetchall()
    columns = [desc[0] for desc in cur.description]
    formatted_columns = [col.replace("_", " ").title() for col in columns]
    df = pd.DataFrame(rows, columns=formatted_columns)
    return df

# Streamlit app
def main():
    st.title('Product Data Viewer')

    # Connect to Trino database
    with connect(
        host="tcp.liberal-donkey.dataos.app",
        port="7432",
        auth=BasicAuthentication(
            "aayushisolanki",
            "dG9rZW5fcHJvYmFibHlfZm9ybWVybHlfbGlnaHRfZ2FubmV0LmMzYjZlZDA0LTVlYTItNDQ5Yi1hMmMwLTM3YTE3NjhkMjgyOA=="
        ),
        http_scheme="https",
        http_headers={"cluster-name": "databasetestcluster"}
    ) as conn:

        cur = conn.cursor()

        # Fetch data from Trino
        query = "SELECT * FROM productdb.public.product_data"
        data = fetch_data(query, cur)

    # Display fetched data
    st.write("## Fetched Data:")
    st.write(data)

    # Show summary statistics
    st.write("## Summary Statistics:")
    st.write(data.describe())

    # Show interactive scatter plot for List Price vs Sale Price
    st.write("## Interactive Scatter Plot: List Price vs Sale Price")
    scatterplot = alt.Chart(data).mark_circle().encode(
        x='List Price',
        y='Sale Price',
        tooltip=['Product Name', 'Brand Name', 'List Price', 'Sale Price']
    ).interactive()
    st.altair_chart(scatterplot, use_container_width=True)

    # Show distribution of List Price
    st.write("## Distribution of List Price:")
    hist_chart = alt.Chart(data).mark_bar().encode(
        alt.X("List Price", bin=True),
        y='count()',
        tooltip=['count()']
    ).interactive()
    st.altair_chart(hist_chart, use_container_width=True)

    # Show category-wise sales chart
    st.write("## Category-wise Sales:")
    category_sales_chart = alt.Chart(data).mark_bar().encode(
        x='Category Name',
        y='sum(Sale Price)',
        tooltip=['Category Name', 'sum(Sale Price)']
    ).properties(
        width=700,
        height=400
    ).interactive()
    st.altair_chart(category_sales_chart, use_container_width=True)

if __name__ == "__main__":
    main()
