# Dashboard Customization

Customize your dashboards to improve the user experience and better align with the look and feel of your organization.

## Layout Elements

Superset has a variety of layout elements that can be used to organize and segment your content on dashboards. To add one, navigate to the LAYOUT ELEMENTS tab and drag and drop it to your dashboard:

<div style="text-align: center;">
  <img src="/interfaces/superset/dashboard_customization/1.png" alt="Untitled image" style="border:1px solid black; width: 80%; height: auto;">
</div>


### Tabs

Tabs are used to segment your charts into different groups.

<div style="text-align: center;">
  <img src="/interfaces/superset/dashboard_customization/1.png" alt="Untitled image" style="border:1px solid black; width: 80%; height: auto;">
</div>


<aside class="callout">
🗣 Remember to drag and drop the tabs element at the very beginning of your dashboard.
</aside>

### Row & Column

Rows and Columns can be added to configure the chart layout further.

<div style="text-align: center;">
  <img src="/interfaces/superset/dashboard_customization/3.png" alt="Untitled image" style="border:1px solid black; width: 80%; height: auto;">
</div>

Similar to columns, Incorporating column elements into your dashboard requires adequate space allocation. If space becomes limited, consider adjusting the ratios of existing charts to create room.

<div style="text-align: center;">
  <img src="/interfaces/superset/dashboard_customization/4.png" alt="Untitled image" style="border:1px solid black; width: 80%; height: auto;">
</div>

### Header

Header is used to add titles.

<div style="text-align: center;">
  <img src="/interfaces/superset/dashboard_customization/5.png" alt="Untitled image" style="border:1px solid black; width: 80%; height: auto;">
</div>

### Text

Text can be used to add text and advanced features, such as images, markdown, and HTML content.

<div style="text-align: center;">
  <img src="/interfaces/superset/dashboard_customization/6.png" alt="Untitled image" style="border:1px solid black; width: 80%; height: auto;">
</div>

### Divider

Divider is useful to isolate the parts of your dashboard.

<div style="text-align: center;">
  <img src="/interfaces/superset/dashboard_customization/7.png" alt="Untitled image" style="border:1px solid black; width: 80%; height: auto;">
</div>

## **Adding Tables to Dashboards**

Adding tables to your dashboards, using HTML with the **Text** element, is also possible. For example:

```markup
<table>
  <tr>
    <th>Header 01</th>
    <th>Header 02</th>
  </tr>
  <tr>
    <td>First Row First Column</td>
    <td>First Row Second Column</td>
  </tr>
  <tr>
    <td>Second Row First Column</td>
    <td>Second Row Second Column</td>
  </tr>
</table>
```

Just paste the above HTML code into the text element by replacing the header titles and other values with respective column names and their actual values.

<div style="text-align: center;">
  <img src="/interfaces/superset/dashboard_customization/8.png" alt="Untitled image" style="border:1px solid black; width: 80%; height: auto;">
</div>

## Color Palettes

As part of the chart creation process, creators specify a color palette. On the dashboard level, it is possible to specify a single **categorical** **color palette** that all charts would use on your dashboard - the chart color palette would still be used when viewing the chart directly, or on other dashboards. Today, the sequential color palette is specified at the chart level and can be configured from the "Chart Builder" view of the compatible charts (e.g., World Maps, Heatmap, Country Map, deck.gl Polygon).

To set up a dashboard-level color palette:

1. Access your dashboard.
2. Click on **EDIT DASHBOARD**, in the top right corner.
3. Click on the three ellipses in the top right corner > **Edit properties**.
4. Choose a palette under the **COLOR SCHEME** drop-down.
5. Save changes.

Superset would use the same color for metrics/dimensions displayed on multiple charts (in the same tab). However, suppose you want to have more control over the columns that are applied to each dimension. In that case, you can manually specify the colors (using hexadecimal or RGBA code) on the dashboard JSON metadata. To do so:

1. Access the dashboard.
2. Click on **EDIT DASHBOARD**, in the top right corner.
3. Click on the three ellipses (...) > **Edit properties**.
4. Expand the **ADVANCED** section.
5. Under the **JSON METADATA** inside “color_scheme” write your color scheme name of which colors you want for your labels then under label_colors give the label name and color code of your choice. For example:


<div style="text-align: center;">
  <img src="/interfaces/superset/dashboard_customization/9.png" alt="Untitled image" style="border:1px solid black; width: 80%; height: auto;">
</div>


Just change the color_scheme with your desired color_scheme and under the label_colors write your label name along with your desired color code.