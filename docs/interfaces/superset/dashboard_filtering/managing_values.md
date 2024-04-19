# Managing Values

we will introduce filter settings that enable you to manage values within filters.

## **Filter Settings**

The following settings options are available for these filter types:

|  | Value | Numerical Range | Time Range | Time Column | Time Grain |
| --- | --- | --- | --- | --- | --- |
| Description | ✔ | ✔ | ✔ | ✔ | ✔ |
| Default values | ✔ | ✔ | ✔ | ✔ | ✔ |
| Value required | ✔ | ✔ | ✔ | ✔ | ✔ |
| Select first value by default | ✔ |  |  |  |  |
| Select multiple values | ✔ |  |  |  |  |
| Dynamic search | ✔ |  |  |  |  |
| Inverse selection | ✔ |  |  |  |  |

---

## **Default and Multiple Values**

**Options available for these Filter Types: All (default values) | Value (multiple values)**

The **Filter has default value** option that empowers you to designate default values for a filter. Upon selecting this option, a **Default Value** dropdown menu emerges, populated with data from the selection made in the **Column** field (applicable to **Value** and **Numerical range** filter types).

If the **Time range** filter type is chosen, then a default time range value can be designated. Similarly, if the **Time column** filter type is selected, a default time column value can be assigned, and so forth.

Simply pick an option to apply as a default value.

**Need to allow more than one value?**

Mark the checkbox, **Can select multiple values**, to enable the selection of multiple default values.

For instance, let's create a **Value** filter utilizing the **item_type** column. By activating **Can select multiple values**, we can specify multiple default values in the **Filter has default value** field — in this scenario, we'll opt for the "beer" and "liqueur" item types.

<p align="center">
  <img src="/interfaces/superset/dashboard_filtering/managing_values/Untitled%20(10).png" alt="Your Image Description" />
</p>


The configuration would look as follows:

<p align="center">
  <img src="/interfaces/superset/dashboard_filtering/managing_values/Untitled%20(11).png" alt="Your Image Description" />
</p>
and the filter, "Item Type" would feature the two pre-selected default values:

<p align="center">
  <img src="/interfaces/superset/dashboard_filtering/managing_values/Untitled%20(12).png" alt="Your Image Description" />
</p>

---

## **Filter Value is Required**

**Option available for these Filter Types: All**

When **Filter value is required** is activated, a filter option must be specified before the filter can be applied. This measure is implemented for performance reasons, ensuring that a user does not inadvertently execute a large query.

---

## **Select First Filter Value by Default**

**Option available for this Filter Type: Value**

The **Select first filter value by default** option picks the first item from a column's data and presents it as a default value for a filter. When utilizing this setting, the **Filter has default value** field that cannot be configured.

**About this setting**

The **Select first filter value by default** setting is primarily utilized as a precautionary measure to prevent inadvertently executing resource-intensive queries on the dashboard.

An exemplary scenario involves employing a dataset with frequently changing values, such as homes for sale in a rapidly evolving market. This setting allows Preset to dynamically select a value; in this case, the first item that appears in the data.

To witness this in operation, try enabling this option for the **Select Item** filter.

<p align="center">
  <img src="/interfaces/superset/dashboard_filtering/managing_values/Untitled%20(13).png" alt="Your Image Description" />
</p>
The first data point in the item_type column is "1800 Taquila”, after saving, you'll notice that the **1800 Taquila** value is automatically pre-selected as a default value for the **Select Item**  filter.

<p align="center">
  <img src="/interfaces/superset/dashboard_filtering/managing_values/Untitled%20(14).png" alt="Your Image Description" />
</p>



## **Dynamically Search All Filter Values**

**Option available for this Filter Type: Value**

This option facilitates dynamic searching when selecting a filter value, meaning that values matching the typed text will appear as selectable options.

<p align="center">
  <img src="/interfaces/superset/dashboard_filtering/managing_values/Untitled%20(15).png" alt="Your Image Description" />
</p>

This advanced setting is particularly advantageous when dealing with extensive datasets. By default, each filter loads a maximum of 1,000 choices when the page is loaded. If your column contains more than 1,000 values, enabling **Dynamically search all filter values** supports large datasets and enhances the user-friendliness of the value selection process.

**Warning**

Exercise caution when using this option, as it may exert additional strain on your database.

## **Inverse Selection**

**Option available for this Filter Type: Value**

Before proceeding, please select **Clear All**. Ensure that **Select first filter value by default** in the **Select Genre** filter (if selected previously) is deselected, and then click **Save**.

There are instances where most filter values are selected except for a few. In such cases, the inverse selection tool proves to be quite handy.

Instead of including filter values, the inverse selection option enables you to exclude specific filter values (i.e., Filter by all values except for the ones you select).

To utilize this feature, navigate to the **Select Item** filter, and within the *Filter Settings* panel, select **Inverse selection**. Then, click **Save**.

<p align="center">
  <img src="/interfaces/superset/dashboard_filtering/managing_values/Untitled%20(16).png" alt="Your Image Description" />
</p>

Now let's observe it in action. In the example below, we have chosen the F1800 Tequila, Corona, and Modelo Item values — take note of the "No" circle-with-bar icon displayed next to the selected icons. Upon applying this filter, all Item values will be showcased on the dashboard, excluding the F1800 Tequila, Corona, and Modelo

<p align="center">
  <img src="/interfaces/superset/dashboard_filtering/managing_values/Untitled%20(17).png" alt="Your Image Description" />
</p>

To undo a selected value, simply re-select it — the exclusion action works as a toggle.