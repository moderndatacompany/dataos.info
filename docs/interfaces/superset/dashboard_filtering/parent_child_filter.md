# Parent-child Filter

Within this section, we'll delve into setting up a parent-child filter using the "Values are dependent on other filters" configuration option. A parent-child filter creates an association between filters, wherein one filter's options rely on another. This setup converts an existing filter into a sub-filter of a parent.

The following options are available for these filter types:

|  | Value | Numerical Range | Time Range | Time Column | Time Grain |
| --- | --- | --- | --- | --- | --- |
| Parent-child | ✔ |  |  |  |  |
| pre-filter available values| ✔ | ✔ |  |  |  |
| sort filter values | ✔ |  | ✔ | ✔ | ✔ |
| single value |  | ✔ |  |  |  |

Before delving into the explanation of a parent-child configuration, we need to perform some brief preparatory steps.

### **Preparation: Create Two Value Filters**

To begin, we'll create a Value type filter named "Select Item Type", utilizing the **item_type** column. For the configuration, simply enable the **Can select multiple values** option in the Filter Settings panel.

<div style="text-align: center;">
  <img src="/interfaces/superset/dashboard_filtering/parent_child/Untitled%20(10).png" alt="Your Image Description" style="border:1px solid black; width: 70%; height: auto;">
</div>

After this is all set, select **Save**.

Next, select **+ Add/Edit Filters** — the *Add and edit filters* window appears.

<aside class="callout">

🗣 When you launch the *Add and edit filters* window, it displays the topmost filter by default. To create another filter, be sure to select **+ Add filters and dividers** and then choose **Filter** in the sub-menu.
</aside>

<div style="text-align: center;">
  <img src="/interfaces/superset/dashboard_filtering/parent_child/image.png" alt="Your Image Description" style="border:1px solid black; width: 30%; height: auto;">
</div>

As mentioned above, select **+ Add filters and dividers** and then choose **Filter** in the sub-menu.

Then create a **Value** type filter called "Select Item" that uses the **item_name** column. Like before, we will select the **Can select multiple values** option in the *Filter Settings* panel.


<div style="text-align: center;">
  <img src="/interfaces/superset/dashboard_filtering/parent_child/Untitled%20(11).png" alt="Your Image Description" style="border:1px solid black; width: 70%; height: auto;">
</div>

When done, select **Save**.

<div style="text-align: center;">
  <img src="/interfaces/superset/dashboard_filtering/parent_child/Untitled%20(12).png" alt="Your Image Description" style="border:1px solid black; width: 30%; height: auto;">
</div>

Now, let's have a closer look at how each configuration option works.


## Create a Parent-Child Filter Relationship

**Option available for this Filter Type: Value**

This option facilitates turning a filter into a sub-filter of an existing one. In this scenario, we'll designate the **Item** filter as a sub-filter of the **Item Type** filter, making the **Item Type** filter the parent.

The aim is to enable users to initially choose one or more gaming platforms, and then further refine their selection by prompting them to choose one or more genres within the selected platform.

To commence, select the **Select Item** filter and, within the *Filter Configuration* panel, opt for **Values are dependent on other filters**.

Upon selecting this, a **Values Dependent On** dropdown menu will appear — proceed to choose **Select Item Type** as the parent filter, then click **Save**.


<div style="text-align: center;">
  <img src="/interfaces/superset/dashboard_filtering/parent_child/Untitled%20(13).png" alt="Your Image Description" style="border:1px solid black; width: 60%; height: auto;">
</div>

Upon examining the dashboard's filter section, you'll observe that the number of available options is indicated in each dropdown field. In the provided image, there are 9 item type options and 77 item options.

<div style="text-align: center;">
  <img src="/interfaces/superset/dashboard_filtering/parent_child/Untitled%20(14).png" alt="Your Image Description" style="border:1px solid black; width: 30%; height: auto;">
</div>

As our parent filter is **Select Item Type**, let's proceed by selecting **tequila**. Subsequently, the **Select Item** field will automatically update to exhibit only those items supported within the specified item type, in this instance, the tequila item type exclusively supports 7 items.

<div style="text-align: center;">
  <img src="/interfaces/superset/dashboard_filtering/parent_child/Untitled%20(15).png" alt="Your Image Description" style="border:1px solid black; width: 30%; height: auto;">
</div>

Let's proceed by selecting the 7 available items bearing in mind that the "Can select multiple values" option permits us to choose more than one option — and then click on **Apply Filters**.

Here's a look at a dashboard table displaying results that match the defined criteria:

<div style="text-align: center;">
  <img src="/interfaces/superset/dashboard_filtering/parent_child/Untitled%20(16).png" alt="Your Image Description" style="border:1px solid black; width: 60%; height: auto;">
</div>

Parent-child filters like this prove useful as they allow users to efficiently drill down and refine their data by establishing a relationship between multiple filters.