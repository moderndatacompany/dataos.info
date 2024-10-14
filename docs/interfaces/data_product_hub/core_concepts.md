# Core concepts

Various new terminologies must first be understood for better comprehension of the Data Product Hub. In this section, a detailed explanation of each new terminologies is provided.

The 'Customer Churn Prediction' Data Product will be used to explain each terminology with examples.

## Metrics

A [Metric](/interfaces/data_product_hub/discovery/#metrics) is an entity that, by default, provides a [logical view](/resources/lens/concepts/#views) of a [logical table](/resources/lens/concepts/#table), containing only one measure and a time dimension. This means that a Metric represents a specific data point or calculation over time, focusing on one key measure, such as average spent per category, retention rate, or churn rate, and linking it to a time period for analysis. In the Data Product Hub, Metrics are populated by the data model ([Lens model](/resources/lens/)). For information on how these Metrics are populated in the Data Product Hub, please refer to [this section](/resources/lens/working_with_views/).

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

## Perspectives

A [Perspective](/interfaces/data_product_hub/discovery/#perspectives) is a saved exploration of a Data Product. A Perspective can be created for any Data Product that has an exposed data model ([Lens model](/resources/lens/)). To explore a [Data Product](/product/data_product/), navigate to the [Explore page](/interfaces/data_product_hub/exploration/), where the Data Product can be explored in detail. After exploration, the exploration can be saved as a Perspective, which can then be accessed in the Perspective tab. Below are images showcasing the exploration process, saving an exploration as a Perspective, and how to access a saved Perspective. To save and access the Perspective, please refer to [this section](/interfaces/data_product_hub/discovery/#perspectives).

=== "Explore section"
    <center>
    <img src="/interfaces/data_product_hub/exploration2.png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    <figcaption><i>Explore section</i></figcaption>
    </center>

=== "Save the Perpective"
    <center>
    <img src="/interfaces/data_product_hub/exploration1.png" alt="DPH" style="width:30rem; border: 1px solid black;" />
    <figcaption><i>Save Perspective</i></figcaption>
    </center>

=== "Access the Perspective"
    <center>
    <img src="/interfaces/data_product_hub/exploration3.png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    <figcaption><i>Perspective tab</i></figcaption>
    </center>

---

## Inputs

In the Data Product Hub, an input is a dataset fed into the Data Product. A Data Product can have multiple inputs, as shown below. An input is populated from the input dataset referenced in the Data Product manifest file. For example in the 'Customer Churn Prediction' Data Product the input `customer` is populated from the address `dataos://icebase:customer_relationship_management/customer` referred in its manifest file, as shown below.

<center>
<img src="/interfaces/data_product_hub/input.png" alt="DPH" style="width:40rem; border: 1px solid black;" />
<figcaption><i>Input</i></figcaption>
</center>


## Outputs

In the Data Product Hub, an output is a materialized dataset generated from the Data Product. A Data Product can have multiple outputs, as shown below. An output is populated from the output dataset referenced in the Data Product manifest file. For example in the 'Customer Churn Prediction' Data Product the output `churn_probability_per_customer` is populated from the address `dataos://icebase:customer_relationship_management/churn_probability_per_customer` referred in its manifest file, as shown below.

<center>
<img src="/interfaces/data_product_hub/output.png" alt="DPH" style="width:40rem; border: 1px solid black;" />
<figcaption><i>Output</i></figcaption>
</center>

## Semantic models

A semantic model is a [data model](/resources/lens/overview/) derived from the [Lens](/resources/lens/). It is fed by the inputs to structure the data in a more meaningful way.


## Data APIs

## Quality

Accuracy
Completeness
Freshness
Schema
Uniqueness
Validity


## Tier

## Domain

## Use case

## Schema

## 







