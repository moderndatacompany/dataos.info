# Product Data Viewer App with Category-wise Sales Chart

# Import necessary libraries
import pandas as pd
from trino.dbapi import connect
from trino.auth import BasicAuthentication
import streamlit as st
import altair as alt
import webbrowser
import requests
from streamlit.components.v1 import components

# Function to fetch data and return pandas dataframe
@st.cache(persist=True, show_spinner=False, ttl=100)
def fetch_data(query, _cur):
    _cur.execute(query)
    rows = _cur.fetchall()
    columns = [desc[0] for desc in _cur.description]
    formatted_columns = [col.replace("_", " ").title() for col in columns]
    df = pd.DataFrame(rows, columns=formatted_columns)
    return df

# Streamlit app
def main():
    st.markdown("<h2 style='text-align: center; color: black;'>Product Data Viewer</h2>", unsafe_allow_html=True)
    st.write("\n")
    st.write("\n")
    st.markdown("**Please Enter Product ID: (Sample Product IDs SKU1, SKU2, SKU3, SKU4)**")

    product_id = st.text_input("", value="")

    if len(product_id) < 1:
        st.write("Please enter a valid Product ID")
    else:
        st.write("Fetching data for Product ID: {}".format(product_id))

        # Connect to Trino database
        with connect(
            host="tcp.liberal-donkey.dataos.app",
            port="7432",
            auth=BasicAuthentication(
                "iamgroot",
                "dG9rZW5fcGVycdfafuiawfa29uYWxseV9pbGxlZ2FsbHlfd2lzZV9qYWd1YXIuNDJjZTEwZlZDk3MDNjODI3"
            ),
            http_scheme="https",
            http_headers={"cluster-name": "postgresdptest"}
        ) as conn:
            cur = conn.cursor()
            query = f"SELECT * FROM postgresdp.public.product_data WHERE product_id = '{product_id}'"
            data = fetch_data(query, cur)

            if data.empty:
                st.write("Please enter a valid Product ID")
            else:
                st.subheader("*Product Information*")

                col1, col2, col3 = st.columns(3)
                with col1:
                    st.markdown("***Product ID:***")
                    st.write(data.at[0, 'Product Id'])

                with col3:
                    st.markdown("***Product Name:***")
                    st.write(data.at[0, 'Product Name'])

                st.markdown("""-------------""")

                col1, col2, col3 = st.columns(3)
                with col1:
                    st.markdown("***Brand Name:***")
                    st.write(data.at[0, 'Brand Name'])

                with col3:
                    st.markdown("***Category Name:***")
                    st.write(data.at[0, 'Category Name'])

                st.markdown("""-------------""")

                col1, col2, col3 = st.columns(3)
                with col1:
                    st.markdown("***List Price:***")
                    st.write(data.at[0, 'List Price'])

                with col3:
                    st.markdown("***Sale Price:***")
                    st.write(data.at[0, 'Sale Price'])

                st.markdown("""-------------""")

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