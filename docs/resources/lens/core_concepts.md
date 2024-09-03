---
title: Model-first Approach
search:
  exclude: true
---

# The Model-First Approach

The model-first approach emphasizes the logical organization and design of data from the outset to address both immediate tactical queries and overarching strategic inquiries in business operations.

By transitioning from ad-hoc data organization and querying methods to a well-defined logical modeling layer, this approach enables data and business intelligence teams to unlock enhanced capabilities. It simplifies the retrieval of metric variants, reduces maintenance overhead, and allows for seamless modifications to models. This strategic shift ensures that downstream datasets and dashboards remain up-to-date, empowering teams to iterate and adapt quickly while fostering a data-driven culture.

To effectively implement this model-first approach, it’s essential to follow a structured process that guides the logical organization of data. Below are the key steps that outline how to adopt this approach and maximize its benefits.

## Steps to Adopt the Model-First Approach

Implementing a model-first approach involves a series of well-defined steps that guide data teams in logically organizing and modeling their data.

## The Approach

### **Define the Goal**

The goal represents the overarching objective of the organization or domain. It reflects the desired outcome or impact that the organization aims to achieve.

### **Outline Value Objectives**

Value objectives are specific outcomes or benefits that contribute to achieving the overarching goal. These objectives are tangible, measurable, and aligned with customer needs, business objectives, and strategic priorities.

<center>
  <div style="text-align: center;">
    <img src="/resources/lens/goal_value_tree.jpg" alt="lens_example" style="width: 80%; border: 1px solid black; height: auto">
    <figcaption>Goal Value Tree</figcaption>
  </div>
</center>

### **Determine Drivers**

Drivers are the specific metrics or indicators used to assess the achievement of the value objective. Examples include revenue growth rates, booked deal value, and targets achieved.

### **Define Measures and Dimensions**

Measures encompass aggregate values, while dimensions represent categorical attributes such as product categories, customer segments, or geographic regions.

## The Design

After establishing your goals, value objectives, drivers, measures, and dimensions, the next crucial step is designing the data model. This involves conceptually representing business objects, their relationships, and the rules governing them within the Lens 2.0 framework.

**Business Views:** Tailor your data model by creating business views that encapsulate the identified drivers and metrics. These views are designed to provide targeted insights into specific value objectives, such as 'account engagement' or 'sales funnel analysis'. By organizing data into these focused perspectives, you ensure that complex data is distilled into actionable insights, directly aligned with your strategic goals.

**Tables:** To build these business views, tables serve as the foundational components. They organize measures and dimensions into coherent structures that represent distinct business objects comprehensively. In this step, the integration of these components allows for the creation of logical, detailed models that drive your analytical processes forward.

This approach simplifies the retrieval of metric variants, reduces maintenance overhead, and allows for seamless modifications to models. Consequently, downstream datasets and dashboards remain current, enabling teams to iterate and adapt with agility.