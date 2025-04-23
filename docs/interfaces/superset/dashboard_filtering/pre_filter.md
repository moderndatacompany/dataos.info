# Pre Filter Data

we will learn how to limit the availability of specified values within a filter using the **Pre-filter available values** configuration option.

## Filter Configuration Options

The following configuration options are available for these filter types:

|  | Value | Numerical Range | Time Range | Time Column | Time Grain |
| --- | --- | --- | --- | --- | --- |
| Parent-child | ✔ |  |  |  |  |
| Pre-filter available values | ✔ | ✔ |  |  |  |
| Sort filter values | ✔ |  | ✔ | ✔ | ✔ |
| Single value |  | ✔ |  |  |  |

## Pre-filter Data

In the [Parent-child Filter,](/interfaces/superset/dashboard_filtering/parent_child_filter/) we utilized the "Values are dependent on other filters" option to establish a parent-child relationship between the **Select Item Type** and **Select Item** value filters, respectively.

Recall that in the **Select Item Type** filter, all available item types were present as selectable options in the dropdown.

Now, let's consider if we only wanted to display specific item types in the **Select Item Type** filter. This can be easily achieved through the "Pre-filter available values" setting, which simply restricts the number of selectable values in a filter.

To begin, select the "Select Item Type" filter previously created and, in the *Filter Configuration* panel, opt for **Pre-filter available values**. A **Pre-Filter** field emerges.

Upon selecting the **Pre-Filter** field, a sub-menu appears featuring two tabs: **Simple** and **Custom SQL**.

The **Simple** tab allows you to link a column with a defined value through operators (e.g., equals, not equals, <, >, etc.). Meanwhile, the **Custom SQL** tab permits you to input your own custom SQL code to specify pre-filtered values for a column.

In this instance, our objective is to limit the options to just **rum**, **tequila**, and **vodka**. To achieve this, select the column **item_type**, the operator **IN** (as there will be multiple options), and input the values **rum**, **tequila**, and **vodka**. If you also wish to filter by time range, simply select the **No filter** button and configure accordingly.

Upon completion, remember to click **Save** for the pre-filter and then **Save** again for the filter as a whole.

The configuration should look as follows:


<div style="text-align: center;">
  <img src="/interfaces/superset/dashboard_filtering/pre_filter/Untitled%20(10).png" alt="Your Image Description" style="border:1px solid black; width: 80%; height: auto;">
</div>

Navigating back to the dashboard, you can see that the **Select Platform** filter now only displays the three pre-filtered values:


<div style="text-align: center;">
  <img src="/interfaces/superset/dashboard_filtering/pre_filter/Untitled%20(11).png" alt="Your Image Description" style="border:1px solid black; width: 80%; height: auto;">
</div>