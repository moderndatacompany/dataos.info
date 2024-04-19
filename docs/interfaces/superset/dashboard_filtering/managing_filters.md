# Managing Filters

Let's explore a few filter management features provided by Superset.

## **How to Add a Filter and Divider**

Within the "Add and edit filters" window, click on "+ Add filters and dividers," then in the submenu, choose "Filter." This action generates a new filter in the Filters panel with the placeholder text "[untitled].”

<p align="center">
  <img src="/interfaces/superset/dashboard_filtering/managing_filters/Untitled%20(10).png" alt="Your Image Description" />
</p>

A divider serves as a header text field, accompanied by an optional description, which can be utilized to introduce sets of filters or simply divide filters.

## **How to Delete a Filter**

To delete a filter, in the Filters panel, select the trash bin icon for a filter.

<p align="center">
  <img src="/interfaces/superset/dashboard_filtering/managing_filters/Untitled%20(11).png" alt="Your Image Description" />
</p>

Once you click on the bin icon, Superset will prompt you to confirm if you wish to restore the deletion (i.e., undo your action). If you opt to restore, select "Restore Filter"; otherwise, the deletion will proceed as intended. Alternatively, you can choose "Undo?" as an option.

<aside class="callout">
🗣 The "Undo?" and "Restore Filter" options appear on a 5-second timer, allowing you to undo any changes or restore the filter to its previous state. If no action is taken within this time frame, the filter will be deleted.

</aside>

<p align="center">
  <img src="/interfaces/superset/dashboard_filtering/managing_filters/Untitled%20(12).png" alt="Your Image Description" />
</p>

## **How to View Applied Filters (via chart icon)**

To view the filters applied to a specific chart, you can click on the filter icon located at the top right corner of the chart. The number displayed alongside the icon indicates the total count of filters applied to that chart.

<p align="center">
  <img src="/interfaces/superset/dashboard_filtering/managing_filters/Untitled%20(13).png" alt="Your Image Description" />
</p>

Clicking on this icon triggers a tooltip to appear, showcasing the applied filters. The provided image illustrates the application of two defined filters.

## **How to Clear All Filters**

Clearing all filters removes your filter selections, but it does not remove the filters themselves.

To clear all filters, simply select **Clear All** on the dashboard.

<p align="center">
  <img src="/interfaces/superset/dashboard_filtering/managing_filters/Untitled%20(14).png" alt="Your Image Description" />
</p>

After doing so, all selections made within the filters are removed.

<p align="center">
  <img src="/interfaces/superset/dashboard_filtering/managing_filters/Untitled%20(15).png" alt="Your Image Description" />
</p>

<aside class="callout">
🗣 Please note that clearing all filters differs from permanently removing a filter. To permanently remove a filter, you need to access the "Add and edit filters" window by selecting "+ Add/Edit Filters" on the dashboard. From there, proceed with deleting the filter as described earlier.

</aside>

## **Active Filter Highlight**

To easily associate filters with charts and tabs, Superset automatically applies a blue border glow to charts and tabs that include data from a selected filter.

<p align="center">
  <img src="/interfaces/superset/dashboard_filtering/managing_filters/Untitled%20(16).png" alt="Your Image Description" />
</p>

.and after we place the cursor over the filter, you will notice that charts and tabs are highlighted with a glowing blue border.

## **Filter Out of Scope**

If you've created a filter on a tab and subsequently switched to another tab utilizing a distinct dataset, the filters originally set on the first tab will be labeled as "Filters out of scope”.

<p align="center">
  <img src="/interfaces/superset/dashboard_filtering/managing_filters/Untitled%20(17).png" alt="Your Image Description" />
</p>

In short, the **Filters out of scope** section is an indicator that filtered data exists in a different tab(s).