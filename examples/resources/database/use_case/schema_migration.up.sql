CREATE TABLE if not EXISTS product_data (
    product_id VARCHAR PRIMARY KEY,
    product_name VARCHAR,
    product_description VARCHAR,
    list_price INTEGER,
    sale_price INTEGER,
    brand_name VARCHAR,
    size_name VARCHAR,
    size_description VARCHAR,
    department_name VARCHAR,
    category_name VARCHAR
);
