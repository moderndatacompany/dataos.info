# Dashboard Customization

Superset includes customizing your dashboard with a highly flexible CSS editor. You may want to change the background color or font of a dashboard, or you may want to do things like hiding particular elements, adjusting margins/padding, adding a splash of color, or making numerous other visual tweaks.

Let’s see how you can customize the dashboard using CSS:-

1. Access the dashboard.
2. Click on **EDIT DASHBOARD**, in the top right corner.
3. Click on the three ellipses (...) > **Edit CSS**.
4. On **Live CSS Editor**, you can write your CSS code.

## Background Color

To modify the background color of the entire dashboard, kindly implement the following CSS code:

```css
.dashboard-content {
  background-color: black;
}
```

![Untitled](/interfaces/superset/dashboard_customization/a.png)

Observe live updates as you make modifications.

Likewise, you have the option to alter the background color of all charts by utilizing the following CSS code:

```css
.chart-container {
  background-color: black;
}
```

![Untitled](/interfaces/superset/dashboard_customization/b.png)

To customize a specific chart, inspect the chart to obtain its unique chart ID. Subsequently, utilize the identified chart ID in the following CSS code for precise customization:

![Untitled](/interfaces/superset/dashboard_customization/j.png)

```css
#chart-id-1 {
  background-color: grey;
}
```

![Untitled](/interfaces/superset/dashboard_customization/c.png)

## Margin and Padding

Margin in Superset refers to the external space around the chart or dashboard container. It defines the clearance outside the element, providing separation from adjacent elements or the container's boundaries.

Padding in Superset refers to the internal space within the chart or dashboard container. It defines the clearance between the content (charts, text, etc.) and the container's borders.

Modify the margin and padding effortlessly with the provided CSS code:

```css
.chart-container {
  margin: 10px;
  padding: 5px;
}
```

![Untitled](/interfaces/superset/dashboard_customization/d.png)

## Fonts

Tailor the fonts within your dashboard using the following customization code.

### **Font Family**

Refine the aesthetic of your entire dashboard by adjusting the font family through the following CSS code:

```css
.dashboard-content {
  font-family: "pacifico", sans-serif;
}
```

![Untitled](/interfaces/superset/dashboard_customization/e.png)

### **Font color**

Adjust the font color of the chart's title seamlessly using CSS:

```css
.header-title {
  color: #ff9900;
}
```

![Untitled](/interfaces/superset/dashboard_customization/f.png)

### **Font size**

Modify the font size of the chart's title effortlessly through CSS:

```css
.header-title {
    font-size: 15px;
}

```

![Untitled](/interfaces/superset/dashboard_customization/g.png)

Explore various font sizes to achieve the desired visual impact.

### **Font weight**

Tailor the font weight to your preference using the following CSS command:

```css
.header-title {
  font-size: 18px;
  font-weight: bold;
}
```

### **Position**

Adjust the position of the chart's title effortlessly using the following CSS command:

```css
.header-title {
position: absolute;
top: 320px;
left: 40%;
transform: translateX(-50%);
}
```

![Untitled](/interfaces/superset/dashboard_customization/h.png)

**`position: absolute`**

When an element is positioned absolutely, it is removed from the normal flow of the document, and its position is calculated based on the nearest positioned ancestor (or the document itself if there is no positioned ancestor).

**`top: 320px`**

Sets the distance from the top of the containing element.

**`left:40%`**

Positions the left edge of the title at 40% of the containing element's width.

**`transform: translatex(-50%)`**

Used to horizontally center the title, adjusting it by 50% of its width.

## Hiding the Title

Hide chart titles at your discretion using the provided CSS code:

```css
.header-title {
    display: none !important;
}
```

![Untitled](/interfaces/superset/dashboard_customization/i.png)

<aside class="callout">
🗣 In Superset, <code>!important</code> can be used in custom CSS rules to ensure they take precedence over existing styles. While <code>!important</code> can be effective for overriding styles, it should be used sparingly to maintain code readability and avoid potential conflicts.

</aside>