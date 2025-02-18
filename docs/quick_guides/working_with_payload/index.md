# Working with Payloads in Lens

!!! info "Information"
    Welcome to the quick guide on working with payloads in Lens! A payload contains specific query logic. You can dynamically adjust your query to filter and sort the data in various ways, all by tweaking the payload. This guide will walk you through the basics of payload structure, and how you can easily tailor your queries using JSON.

A **payload** in Lens is simply a request for data, written in JSON format. It tells Lens what information you need and how to get it. By adjusting the payload, you can select specific data, apply filters, sort results, and more—all with great flexibility.

## Why Use Payloads?

Payloads give you **control** over your data queries. While the Lens UI makes basic queries easy, using payloads allows for:

- Custom filters
- Complex aggregations
- Advanced sorting
- Flexible time dimensions

## Core Components of a Payload

The **payload** includes key details like:

| **Element** | **Description** |
| --- | --- |
| `measures` | Numeric data you want (e.g., sales totals, revenue). |
| `dimensions` | Categorical data like product names, regions, or customer types. |
| `filters` | Conditions to limit the data (e.g., show only sales from the last month). |
| `timeDimensions` | Add a time-based filter (e.g., filter results by date range or time period). |
| `segments` | Named filters created in the data model to simplify common queries. |
| `limit` | Restrict the number of rows returned by the query (e.g., return only the top 10 results). |
| `offset` | Skip a number of rows before showing results (e.g., start at row 11 if `offset: 10`). |
| `order` | Specify how to sort the results (e.g., order by name or date). |
| `timezone` | Specify the timezone for your query (e.g., `America/Los_Angeles`).  |

---

Here’s what a typical JSON payload looks like. This example will help you visualize how it works:

This query retrieves data about the average transaction amount for customers, including details such as the customer's first name, email ID, and age. Simple, right?

```json
{
  "measures": [
    "transactions.average_transaction_amount"
  ],
  "dimensions": [
    "customer.first_name",
    "customer.email_id",
    "customer.age"
  ],
  "segments": [],
  "filters": [],
  "timeDimensions": [],
  "order": [],
  "limit": 10,
  "offset": 0
}
```

## How Payloads Work in Lens

Payloads let you easily adjust measures, dimensions, filters, and sorting to get the data you need.

### **Viewing Payloads in the Lens UI**

Before diving into working with payloads, it’s essential to know where you can access and work with them within the Lens UI.

1. **Open Metis**: Navigate to the **Resources > Lens** section in the Metis app to see a list of available Lenses.
2. **Select a Lens**: Click on the name of the Lens you’re working with to open it.
    
    ![metis_lenses.png](/quick_guides/working_with_payload/metis_lenses.png)
    
3. **Explore in Studio**: Once in the detailed view, click **Explore in Studio** to launch the Studio interface.
    
    ![lens_model_metis.png](/quick_guides/working_with_payload/lens_model_metis.png)
    
4. **View Payload**: Inside the Lens UI, click on the `{}` icon to view the JSON payload for your current query.
    
    ![payload_option_lensui.png](/quick_guides/working_with_payload/payload_option_lensui.png)
    
5. **Working with Payloads**:This is where you can edit the filters to customize payload.
    
    ![json_payload_lensui.png](/quick_guides/working_with_payload/json_payload_lensui.png)
    

Now it’s your turn to try building a payload! 

## Using Payloads: Try It Yourself

Once you’re comfortable viewing payloads, try modifying them:

1. **Adjust the Sorting**: Use the `order` property to sort results by name or revenue.
2. **Change the Filters**: Add new filters to focus on different categories or time periods.

### **Understanding the `Order` Property**

The **`order`** property controls the sorting of your results. If you don’t specify an order, Lens defaults to sorting by time dimensions (if present), followed by measures, and finally by dimensions.

Want to change the order? You can. Just specify how you want the data sorted.  You can sort by multiple fields by using an **array of tuples**, which allows for more complex ordering.

> For example, sort by customer name alphabetically, then by age in descending order.
> 

```json
"customer": [
  ["customer.firstName", "asc"],
  ["customer.age", "desc"]
]
```

![order_ex.png](/quick_guides/working_with_payload/order_ex.png)

### **Filtering Your Data**

A key part of querying data in Lens is filtering. Filters allow you to narrow down your dataset by specifying conditions on measures or dimensions. The basic structure of a filter looks like this:

A filter object includes:

- **member**: The dimension or measure being filtered (e.g., `customer.age`).
- **operator**: The filter operator (varies by dimension type, limited for measures).
- **values**: An array of string values. For dates, use the format `YYYY-MM-DD`.

```json
"filters": [
    {
      "and": [
        {
          "member": "customer.age",
          "operator": "lt",
          "values": [
            "30"
          ]
        },
        {
          "member": "customer.gender",
          "operator": "equals",
          "values": [
            "FEMALE"
          ]
        }
      ]
    }
  ]
```

In this example, you're asking for data where the female customer age is less than 30.

![filter_payload.png](/quick_guides/working_with_payload/filter_payload.png)

#### **Filter Operators**

Filter operators let you refine your data queries. Here are the main ones:

- **`equals`**: Matches exact values.
- **`notEquals`**: Excludes exact values.
- **`contains`**: Matches values containing a substring.
- **`notContains`**: Excludes values containing a substring.
- **`startsWith`**: Matches values starting with a substring.
- **`notStartsWith`**: Excludes values starting with a substring.
- **`endsWith`**: Matches values ending with a substring.
- **`notEndsWith`**: Excludes values ending with a substring.

These operators help with exact matches, wildcard searches, and filtering based on numerical or date ranges. For more details and examples, check out the [Filter Operators: Example Scenarios](/quick_guides/working_with_payload/filter_operator_example_scenarios/).

<aside class="callout">
🗣 When you filter on a <b>dimension</b>, you're narrowing down the raw data <b>before</b> any calculations take place. For example, if you filter by "customer age < 50," only the data for customers under 50 is used in the calculations.

On the other hand, when you filter on a <<b>>measure</b>, you're filtering <b>after</b> calculations are done. For instance, if you filter by "average sales > $100," you're applying the filter after the system has already calculated the average sales for each group.

</aside>

#### **Time Dimensions Format**

In Lens, time dimensions allow you to group and filter data by time. Use the `timeDimensions` property in your payload:

- **`dimension`**: Name of the time dimension.
- **`dateRange`**: Array of dates in `YYYY-MM-DD` or `YYYY-MM-DDTHH:mm:ss.SSS` format, using local time and the query’s timezone. Single dates are padded to cover the entire day (`start/end`).
- **`granularity`**: Grouping level. Options: `second`, `minute`, `hour`, `day`, `week`, `month`, `quarter`, `year`. `Null` skips grouping, performing only filtering.

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

<div style="text-align: left; padding-left: 1em;">
<img src="/quick_guides/working_with_payload/time_dim.png" alt="time_dim.png" style="max-width: 50%; height: auto; border: 1px solid #000;">
</div>

#### **Boolean Logical Operators**

Use boolean logical operators to combine multiple filters:

- **`or`**: Matches if any of the filters are true.
- **`and`**: Matches only if all filters are true.

**Example Payload and Results:**

This query retrieves products with an **average margin** (measure) of at least 112, and both **cost** and **price** at least 30 and 100, respectively. The results show the product name, cost, and price, with a limit of 10 records.

![boolean_filter.png](/quick_guides/working_with_payload/boolean_filter.png)

> Note: You cannot mix dimension and measure filters in the same logical operator.
>