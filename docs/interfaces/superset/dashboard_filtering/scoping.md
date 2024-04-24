# Scoping

We'll introduce the concept of scoping, which can be accessed via the **Scoping** tab for most filter types, and its capability to offer control over the application of filters to specific charts.

<p align="center">
  <img src="/interfaces/superset/dashboard_filtering/scoping/Untitled%20(10).png" alt="Your Image Description" />
</p>

To access the **Scoping** tab, navigate to the Filter Bar on your dashboard and choose "Add/Edit Filters". Within the Filters window, select the filter you wish to adjust the scoping for, and then click on the **Scoping** tab.

To change the scoping of a **Cross Filter,** please see [Cross-filtering](./cross_filtering.md).

## **Scoping a Filter**

Scoping offers detailed control over which charts are affected by an applied filter. To access scoping options, follow the steps outlined above to select the **Scoping** tab.

The default scoping of the filters varies based on the type of filter:

- **Time Grain Filter**: Applies to all charts by default.
- **Value Filter, Numerical Range Filter, Time Column Filter, and Time Range Filter**: Applies to all charts powered by the specified dataset by default.

**Applying Filters Across Datasets**

If your dashboard is powered by multiple datasets, you can adjust the scoping of your filter to apply to all charts that share a common column name.

**Example:** If you have two datasets powering your charts (e.g., *Global Vehicle Sales* and *World Bank Data*) and both datasets share the same column name ("country_abrv"), you can extend the scope of your *Country* value filter to apply to all charts that use these two datasets.

This default scoping can then be modified by accessing the **Scoping** tab.

<p align="center">
  <img src="/interfaces/superset/dashboard_filtering/scoping/Untitled%20(11).png" alt="Your Image Description" />
</p>

To specify individual charts that can be filtered, choose **Apply to specific panels**.

All charts and tabs within the dashboard are displayed in a hierarchical outline format, with a checkbox assigned to each one.

To prevent a chart from being filtered, simply deselect the corresponding checkbox. In the example below, we took the following actions:

- **Deselected a Tab**: Filters will not be applied to all charts within the **Explore Trends** tab.
- **Deselected Individual Charts**: Filters will not be applied to the 'Most Dominant Platforms' and 'Popular Genres Across Platforms' charts.

<p align="center">
  <img src="/interfaces/superset/dashboard_filtering/scoping/Untitled%20(12).png" alt="Your Image Description" />
</p>