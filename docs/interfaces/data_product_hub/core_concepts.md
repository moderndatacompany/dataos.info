# Core concepts

Various new terminologies must first be understood for better comprehension of the Data Product Hub. In this section, a detailed explanation of each new terminologies is provided.

The 'Customer Churn Prediction' Data Product will be used to explain each terminology with examples.

## Metrics

A Metric is an entity that, by default, provides a logical view of a logical table, containing only one measure and a time dimension. This means that a Metric represents a specific data point or calculation over time, focusing on one key measure, such as average spent per category, retention rate, or churn rate, and linking it to a time period for analysis. In the Data Product Hub, Metrics are populated by the data model ([Lens model](/resources/lens/)). For information on how these Metrics are populated in the Data Product Hub, please refer to [this section](/resources/lens/working_with_views/).

<center>
<img src="/interfaces/data_product_hub/metrics.png" alt="DPH" style="width:40rem; border: 1px solid black;" />
<figcaption><i>Metrics Tab</i></figcaption>
</center>


For example, in the 'Average Spent Per Category' metric, which shows a total amount spent of 65.24, along with a -30.71% decline in the spending percentage, this metric is populated from the data model (Lens model) as shown below. Similarly, other metrics are populated in the same way.

=== "Title"
    <center>
    <img src="/interfaces/data_product_hub/matric2.png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    <figcaption><i>Title</i></figcaption>
    </center>

=== "Description"
    <center>
    <img src="/interfaces/data_product_hub/metric3.png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    <figcaption><i>Description</i></figcaption>
    </center>

=== "Domain"
    <center>
    <img src="/interfaces/data_product_hub/metric4.png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    <figcaption><i>Domain</i></figcaption>
    </center>

=== "Use case"
    <center>
    <img src="/interfaces/data_product_hub/metric5.png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    <figcaption><i>Use case</i></figcaption>
    </center>

=== "Tier"
    <center>
    <img src="/interfaces/data_product_hub/metric6.png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    <figcaption><i>Tier</i></figcaption>
    </center>

---

## Perspective

A Perspective is a saved exploration of the Data Product. Anyone can create a Perspective for any Data Product that has an exposed data model (Lens model). To explore the Data Product, simply navigate to the Explore page, where the Data Product can be explored in detail. For more information about the Explore section, please refer to [this link](/interfaces/data_product_hub/exploration/). Below are some images showcasing exploration, saving the exploration as perspective 

## Entity

## View






