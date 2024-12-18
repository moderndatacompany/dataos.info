# Working with Payload

!!! abstract "Quick Guide"
    To quickly get started with payloads in Lens, follow the [quick guide on working with payloads](/quick_guides/working_with_payload/). It covers the essentials of payload structure and demonstrates how to adjust your queries using JSON to efficiently filter and sort data.


## Introduction

In the context of **Lens**, a **payload** refers to the data sent within the body of an API request, typically in **JSON format**, to define specific query instructions. This payload includes measures, dimensions, filters, and other query components used to interact with Lens’s data models. It serves as the essential data package the client sends to Lens’s API, allowing the system to process and return results based on the query defined in the payload. The payload specifies the actual query logic, such as aggregations or filters, that Lens will act upon to retrieve the desired data.

Payloads are crucial for structuring and transmitting data to APIs, enabling seamless interactions with AI/ML models and tools like Lens for exploring and analyzing data.

> The Lens uses structured JSON objects in the request body to define the query parameters, such as measures, dimensions, filters, and time dimensions.

## Understanding Lens UI

Before working with payloads, let’s first explore where to locate the necessary tools and settings within the Lens UI:

1. Navigate to the Home Page of DataOS.
2. Select the Lens Icon.
    
    <div style="text-align: left; padding-left: 1em;">
        <img src="/resources/lens/working_with_payloads/lens_icon.png" alt="Iris board" style="max-width: 100%; height: auto; border: 1px solid #000;">
    </div>

3. This will open the Lens interface
    
      <div style="text-align: center;">
        <img src="/resources/lens/working_with_payloads/lens_ui.png" alt="Iris board" style="max-width: 90%; height: auto; border: 1px solid #000;">
      </div> 

4. The link on the Lens interface will redirect you to the Metis section, where you can select your desired Lens from the list of available resources.

5. After selecting your Lens, click on **Lens Studio** to open the interface where you can craft your queries and begin working with payloads.

      <div style="text-align: center;">
        <img src="/resources/lens/working_with_payloads/lens_studio.png" alt="Iris board" style="max-width: 90%; height: auto; border: 1px solid #000;">
        <figcaption> Lens Studio Explore Page </figcaption>
      </div>

**Elements of Lens Studio:**

1. **Tables and Views** On the left panel, you can see the list of tables and views.
2. **Selecting Dimensions and Measures** Click on a table or view to expand and see its dimensions and measures. Select the ones you need for your analysis.
3. **Building Queries** Select dimensions and measures to create your queries.
4. **Running Queries** Click the 'Run Query' button to execute your query and see the results.
5. **Filters:** Filters allow users to narrow down data based on specific criteria, such as ranges, categories, or exact values.
6. **Visualizing Data:** Switch between table, chart, and pivot views to visualize your data in different formats.
7. **Payload  `{}` :** WithPayloads allow you to dynamically adjust queries, enabling filtering, sorting, and aggregation according to user needs. This functionality extends beyond what can be achieved through the UI alone.
 

## Query Format

The JSON payload provided specifies a query configuration with the following key properties:

| **Elements** | **Description** |
|--------------|-----------------|
| **`measures`** | An array of measures |
| **`dimensions`** | An array of dimensions. |
| **`filters`** | An array of objects, describing filters. |
| **`timeDimensions`** | A convenient way to specify a time dimension with a filter. |
| **`segments`** | An array of segments. A segment is a named filter, created in the data model. |
| **`limit`** | A row limit for your query. |
| **`offset`** | The number of initial rows to be skipped for your query. The default value is `0`. |
| **[`order`](/resources/lens/working_with_payload/#order-format)** | An object, where the keys are measures or dimensions to sort and their corresponding values are either `asc` or `desc`. The order in which the fields are sorted is determined by the sequence of keys within the object. |
| **[`timezone`](/resources/lens/working_with_payload/#time-dimension-format)** | You can set the desired time zone in the [TZ Database Name](https://en.wikipedia.org/wiki/Tz_database) format, e.g., `America/Los_Angeles`. |


### **Order format**

**Default ordering**

When the `order` property is not explicitly defined in the query, the results are sorted by default according to the following sequence:

- **Time Dimension:** Results are first ordered by the initial time dimension with granularity, in ascending order. If no time dimension with granularity is present.

- **Measure:** Next, results are sorted by the first measure found, in descending order. If no measure is specified.

- **Dimension:** Finally, if neither of the above are available, results are ordered by the first dimension, in ascending order.

**Alternative order format:** You can control the sequence of the `order` specification using an alternative format for ordering, which is an array of tuples:

**Example Payload and Result:** *This query will give you the first 10 customers sorted alphabetically by their first name. For those with the same first name, the list will be further ordered by age, from oldest to youngest.*

<div style="text-align: center;">
    <img src="/resources/lens/working_with_payloads/image(1).png" alt="Iris board" style="max-width: 90%; height: auto; border: 1px solid #000;">
    <figcaption> ordering </figcaption>
</div>


### **Filters Formats**

A filter object contains the following properties:

- **`member`:** Dimension or measure to be used in the filter, for example: `stories.isDraft`. See below on the difference between filtering dimensions vs filtering measures.

- **`operator`:** An operator to be used in the filter. Only some operators are available for measures. For dimensions the available operators depend on the type of the dimension. 

- **`values`:** An array of values for the filter. Values must be of type string. If you need to pass a date, pass it as a string in `YYYY-MM-DD` format.

**Filtering Dimensions vs Filtering Measures**

Filters are applied differently to dimensions and measures.

<aside class="callout">
💡 When you filter on a dimension, you are restricting the raw data before any calculations are made. When you filter on a measure, you are restricting the results after the measure has been calculated.

</aside>

**Filter Operators**

**_Let’s explore each by using appropriate examples_**

#### **`equals`**

Use it when you need an exact match. It supports multiple values.

- Applied to measures.
- **Dimension types:** `string`, `number`, `time`.
    
**Example Payload and Result:** Retrieving the customer IDs and countries for customers based in the USA, limited to 10 results. You can see the results in Table Section 

<div style="text-align: center;">
    <img src="/resources/lens/working_with_payloads/image(2).png" alt="Iris board" style="max-width: 90%; height: auto; border: 1px solid #000;">
    <figcaption>equals</figcaption>
</div>

#### **`notEquals`**
The opposite operator of `equals`. It supports multiple values.

- Applied to measures.
- **Dimension types: `string`, `number`, `time`.**

**Example Payload and Result:** Retrieving the customer IDs and countries for customers who are not based in the USA, limited to 10 results.

<div style="text-align: center;">
    <img src="/resources/lens/working_with_payloads/image(3).png" alt="Iris board" style="max-width: 90%; height: auto; border: 1px solid #000;">
    <figcaption> notEquals </figcaption>
</div>

#### **`contains`** 
The contains filter functions as a wildcard, case-insensitive LIKE operator. It typically utilizes the ILIKE operator in SQL backends, with values enclosed in `%` symbols. This filter supports multiple values.
    
- **Dimension types: `string`.**
    
**Example Payload and Result:** Retrieving the Product IDs associated with a given designer's name, while limiting the results to 10


<div style="text-align: center;">
    <img src="/resources/lens/working_with_payloads/image(4).png" alt="Iris board" style="max-width: 90%; height: auto; border: 1px solid #000;">
    <figcaption> contains </figcaption>
</div>

#### **`notContains`** 

The opposite operator of `contains`. Supports multiple values.

- **Dimension types: `string`**

**Example Payload and Result:**
    
<div style="text-align: center;">
    <img src="/resources/lens/working_with_payloads/image(5).png" alt="Iris board" style="max-width: 90%; height: auto; border: 1px solid #000;">
    <figcaption> notContains </figcaption>
</div>

#### **`startsWith`** 

The `startsWith` filter acts as a case-insensitive `LIKE` operator with a wildcard at the end. In the majority of SQL backends, it uses the `ILIKE`
operator with `%` at the end of each value. It supports multiple values.

- **Dimension types: `string`.**

**Example Payload and Result:** This query retrieves up to 10 product IDs and their associated designer names, filtering for designers whose names start with 'Ja'.

<div style="text-align: center;">
    <img src="/resources/lens/working_with_payloads/image(6).png" alt="Iris board" style="max-width: 90%; height: auto; border: 1px solid #000;">
    <figcaption> startsWith </figcaption>
</div>
 

#### **`notStartsWith`** 

The opposite operator of `startsWith`.

**Example Payload and Result:** This query retrieves up to 10 product IDs and their associated designer names, filtering for designers whose names does not start with 'Ja'.
 
<div style="text-align: center;">
    <img src="/resources/lens/working_with_payloads/image(7).png" alt="Iris board" style="max-width: 90%; height: auto; border: 1px solid #000;">
    <figcaption> notStartsWith </figcaption>
</div>
 

#### **`endsWith`** 

The `endsWith` filter acts as a case-insensitive `LIKE` operator with a wildcard at the beginning. In the majority of SQL backends, it uses the `ILIKE` operator with `%` at the beginning of each value. It supports multiple values.

- **Dimension types: `string`.**

**Example Payload and Result:** This query retrieves up to 10 product IDs and their associated designer names, filtering for designers whose names ends with 'e'.
     
     
<div style="text-align: center;">
  <img src="/resources/lens/working_with_payloads/image(8).png" alt="Iris board" style="max-width: 90%; height: auto; border: 1px solid #000;">
  <figcaption> endsWith </figcaption>
</div>

#### **`notEndsWith`** 
The opposite operator of `endsWith`.

**Example Payload and Results:** This query retrieves up to 10 product IDs and their associated designer names, filtering for designers whose names does not ends with 'e'.

<div style="text-align: center;">
  <img src="/resources/lens/working_with_payloads/image(9).png" alt="Iris board" style="max-width: 90%; height: auto; border: 1px solid #000;">
  <figcaption> notEndsWith </figcaption>
</div>

#### **`gt`** 
The `gt` operator means **greater than** and is used with measures or dimensions of type `number`.

- Applied to measures.
- **Dimension types: `number`.**

**Example Payload and Results:** Retrieves records where the product price is greater than 100.

<div style="text-align: center;">
  <img src="/resources/lens/working_with_payloads/image(10).png" alt="Iris board" style="max-width: 90%; height: auto; border: 1px solid #000;">
  <figcaption> gt </figcaption>
</div>

 

#### **`gte`** 
The `gte` operator means **greater than or equal to** and is used with measures
or dimensions of type `number`.

- Applied to measures.
- **Dimension types: `number`.**

**Example Payload and Results:** Filter products based on their price, returning details for products priced more than `125.51`.*

<div style="text-align: center;">
  <img src="/resources/lens/working_with_payloads/image(12).png" alt="Iris board" style="max-width: 90%; height: auto; border: 1px solid #000;">
  <figcaption> gte </figcaption>
</div>

#### **`lt`** 
The `lt` operator means **less than** and is used with measures or dimensions of type `number`.

- Applied to measures.
- **Dimension types: `number`.**

**Example Payload and Results:** Filter products based on their price, returning details for products priced below `125.51`.
<div style="text-align: center;">
  <img src="/resources/lens/working_with_payloads/image(13).png" alt="Iris board" style="max-width: 90%; height: auto; border: 1px solid #000;">
  <figcaption> lt </figcaption>
</div>

#### **`lte`**  
The `lte` operator means **less than or equal to** and is used with measures or
dimensions of type `number`.

- Applied to measures.
- **Dimension types: `number`.**

**Example Payload and Results:** Filter products based on their price, returning details for products priced at or below `125.51`.

<div style="text-align: center;">
  <img src="/resources/lens/working_with_payloads/image(14).png" alt="Iris board" style="max-width: 90%; height: auto; border: 1px solid #000;">
  <figcaption> lte </figcaption>
</div>

#### **`set`** 
Operator `set` checks whether the value of the member **is not** `NULL`. You
don't need to pass `values` for this operator.

- Applied to measures.
- **Dimension types: `number`, `string`, `time`.**

**Example Payload and Results:** The query retrieves products where the price information is not missing (NOT NULL). This can help identify products for which pricing details have not been recorded.

<div style="text-align: center;">
  <img src="/resources/lens/working_with_payloads/image(15).png" alt="Iris board" style="max-width: 90%; height: auto; border: 1px solid #000;">
  <figcaption> set </figcaption>
</div>

#### **`notSet`** 

An opposite to the `set` operator. It checks whether the value of the member **is** `NULL`. You don't need to pass `values` for this operator.

- Applied to measures.
- **Dimension types: `number`, `string`, `time`.**

**Example Payload and Results:** The query retrieves products where the price information is missing ( NULL). This can help identify products for which pricing details have not been recorded. In our data we did not have any null values hence the data is not available means NULL data is not available.

<div style="text-align: center;">
  <img src="/resources/lens/working_with_payloads/image(16).png" alt="Iris board" style="max-width: 90%; height: auto; border: 1px solid #000;">
  <figcaption> notSet </figcaption>
</div>

#### **`inDateRange`**

The operator `inDateRange` is used to filter a time dimension into a specific
date range. The values must be an array of dates with the following format
'YYYY-MM-DD'. If only one date specified the filter would be set exactly to this
date.

- **Dimension types: `time`.**

**Example Payload and Results:** Return the total number of customers who registered between **January 1, 2022**, and **January 31, 2023**.

<div style="text-align: center;">
  <img src="/resources/lens/working_with_payloads/image(17).png" alt="Iris board" style="max-width: 90%; height: auto; border: 1px solid #000;">
  <figcaption> inDateRange </figcaption>
</div>

#### **`notInDateRange`** 

opposite operator to `inDateRange`, use it when you want to exclude specific dates. The values format is the same as for `inDateRange`.

- **Dimension types: `time`.**

**Example Payload and Results:** Return the total number of customers who did not registered between May 01, 2022, and January 31, 2023.

<div style="text-align: center;">
  <img src="/resources/lens/working_with_payloads/image(18).png" alt="Iris board" style="max-width: 90%; height: auto; border: 1px solid #000;">
  <figcaption> notInDateRange </figcaption>
</div>

#### **`beforeDate`** 

Use it when you want to retrieve all results before some specific date. The
values should be an array of one element in `YYYY-MM-DD` format.

- **Dimension types: `time`.**

**Example Payload and Results:** Total number of customers who registerd before January 31, 2023.

<div style="text-align: center;">
  <img src="/resources/lens/working_with_payloads/image(19).png" alt="Iris board" style="max-width: 90%; height: auto; border: 1px solid #000;">
  <figcaption> beforeDate </figcaption>
</div>

#### **`afterDate`**

The same as `beforeDate`, but is used to get all results after a specific date.

- **Dimension types: `time`.**

**Example Payload and Results:** It returns the total number of customers who registered after **January 31, 2023.

<div style="text-align: center;">
  <img src="/resources/lens/working_with_payloads/image(20).png" alt="Iris board" style="max-width: 90%; height: auto; border: 1px solid #000;">
  <figcaption> afterDate </figcaption>
</div>

### **Time Dimensions Format**

Since grouping and filtering by a time dimension is quite a common case, Lens
provides a convenient shortcut to pass a dimension and a filter as a
`timeDimension` property.

- **`dimension`** Time dimension name.
- **`dateRange`** An array of dates with the following format `YYYY-MM-DD` or in
`YYYY-MM-DDTHH:mm:ss.SSS` format. Values should always be local and in query
`timezone`. Dates in `YYYY-MM-DD` format are also accepted. Such dates are
padded to the start and end of the day if used in start and end of date range
interval accordingly. Please note that for timestamp comparison, `=` and `<=`
operators are used. It requires, for example, that the end date range date
`2020-01-01` is padded to `2020-01-01T23:59:59.999`. If only one date is
specified it's equivalent to passing two of the same dates as a date range.
You can also pass a string with a **relative date range**, for example, `last quarter`.
- **`granularity`** A granularity for a time dimension. It supports the following
values `second`, `minute`, `hour`, `day`, `week`, `month`, `quarter`, `year`.
If you pass `null` to the granularity, Lens will only perform filtering by a
specified time dimension, without grouping.
    
#### **`dateRange`**

You can also use a string with a relative date range in the `dateRange` property, for example:
    
**Example Payload:**

    
```json
{
  "measures": ["customer.total_customers"],
  "timeDimensions": [
    {
      "dimension": "customer.register_date",
      "dateRange": "last year",
      "granularity": "year"
    }
  ]
}
```

**Result:**

<div style="text-align: center;">
  <img src="/resources/lens/working_with_payloads/daterange.png" alt="Iris board" style="max-width: 90%; height: auto; border: 1px solid #000;">
  <figcaption> afterDate </figcaption>
</div>

### **Boolean logical operators**

>**Note:** You can not put dimensions and measures filters in the same logical operator.
 
Filters can contain `or` and `and` logical operators. Logical operators have only one of the following properties:

- `or` An array with one or more filters or other logical operators
- `and` An array with one or more filters or other logical operators

**Example Payload and results:** The JSON payload is used to query a product database to retrieve products that have a minimum `average_margin`(Measure) of 112, and where the `cost` is at least 30 and the price is at least 100. The result will include the product name, cost, and price, with a maximum of 10 records returned starting from the first record.

<div style="text-align: center;">
  <img src="/resources/lens/working_with_payloads/image(21).png" alt="Iris board" style="max-width: 90%; height: auto; border: 1px solid #000;">
  <figcaption> or and and operator </figcaption>
</div>


