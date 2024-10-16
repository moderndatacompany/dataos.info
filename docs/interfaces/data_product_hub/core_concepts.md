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
    <img src="/interfaces/data_product_hub/metrics_title.png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    <figcaption><i>Title</i></figcaption>
    </center>

=== "Description"
    <center>
    <img src="/interfaces/data_product_hub/metrics_description.png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    <figcaption><i>Description</i></figcaption>
    </center>

=== "Domain"
    <center>
    <img src="/interfaces/data_product_hub/metrics_domain.png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    <figcaption><i>Domain</i></figcaption>
    </center>

=== "Use case"
    <center>
    <img src="/interfaces/data_product_hub/metrics_usecase.png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    <figcaption><i>Use case</i></figcaption>
    </center>

=== "Tier"
    <center>
    <img src="/interfaces/data_product_hub/metric_tier.png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    <figcaption><i>Tier</i></figcaption>
    </center>

---

## Perspectives

A [Perspective](/interfaces/data_product_hub/discovery/#perspectives) is a saved exploration of a Data Product. A Perspective can be created for any Data Product that has an exposed data model ([Lens model](/resources/lens/)). To explore a [Data Product](/products/data_product/), navigate to the [Explore page](/interfaces/data_product_hub/exploration/), where the Data Product can be explored in detail. After exploration, the exploration can be saved as a Perspective, which can then be accessed in the Perspective tab. Below are images showcasing the exploration process, saving an exploration as a Perspective, and how to access a saved Perspective. To save and access the Perspective, please refer to [this section](/interfaces/data_product_hub/discovery/#perspectives).

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

In the Data Product Hub, an [input](/interfaces/data_product_hub/discovery/#inputs-tab) is a dataset fed into the Data Product. A Data Product can have multiple inputs, as shown below. An input is populated from the input dataset referenced in the Data Product manifest file. For example in the 'Customer Churn Prediction' Data Product the input `customer` is populated from the address `dataos://icebase:customer_relationship_management/customer` referred in its manifest file, as shown below.

<center>
<img src="/interfaces/data_product_hub/input.png" alt="DPH" style="width:40rem; border: 1px solid black;" />
<figcaption><i>Input</i></figcaption>
</center>


## Outputs

In the Data Product Hub, an [output](/interfaces/data_product_hub/discovery/#outputs-tab) is a materialized dataset generated from the Data Product. A Data Product can have multiple outputs, as shown below. An output is populated from the output dataset referenced in the Data Product manifest file. For example in the 'Customer Churn Prediction' Data Product the output `churn_probability_per_customer` is populated from the address `dataos://icebase:customer_relationship_management/churn_probability_per_customer` referred in its manifest file, as shown below.

<center>
<img src="/interfaces/data_product_hub/output.png" alt="DPH" style="width:40rem; border: 1px solid black;" />
<figcaption><i>Output</i></figcaption>
</center>


## Data APIs

A [data API](/interfaces/data_product_hub/discovery/#data-apis-tab) refers to an application programming interface (API) that allows applications to interact with and retrieve data from a data source, such as a database or data warehouse, in a structured and controlled manner. Data APIs are used to enable communication between software applications and databases, allowing developers to query, filter, and manipulate data without directly interacting with the underlying data storage systems. Within DataOS, one can create the data APIs using [Talos Stack](/resources/stacks/talos/).

## Tier

Tier is a classification for Data Products based on their purpose, whether by medallion architecture, source-aligned, or based on specific entities or consumers. For example, in the 'Customer Churn Prediction' Data Product, its tier is labeled as `Business Certified` which basically means the Data Product is business oriented. Similarly, each organization can have its own predefined tiers. Tier is populated from the Data Product manifest file.

<center>
<img src="/interfaces/data_product_hub/tier.png" alt="DPH" style="width:40rem; border: 1px solid black;" />
<figcaption><i>Tier</i></figcaption>
</center>

**Tier Categories** 

The following are the tier categories defined within the organization. Similarly, tiers can be categorized into different categories as per the choice.

- `Business Certified`: This tier indicates that the Data Product is designed with a business-oriented focus, ensuring that it meets specific business requirements and standards.

- `Consumer`: Data Products in this category are intended for data consumers, providing easily accessible and understandable data for their needs.

- `Consumer Aligned`: This tier indicates that the Data Product is aligned with consumer needs and preferences, ensuring that the data is relevant and useful for a specific audience.

- `DataCOE Approved`: This designation indicates that the Data Product has been approved by the Data Center of Excellence (DataCOE), signifying adherence to best practices and standards.

- `Deprecated`: This tier signifies that the Data Product is no longer recommended for use and may be phased out or replaced in the future.

- `Internal Use Only`: Data Products in this category are restricted to internal stakeholders within the organization, not intended for external consumption.

- `Limited Availability`: This tier indicates that the Data Product has restricted access, limiting its use to a specific user group.

- `Source Aligned`: This designation signifies that the Data Product is closely aligned with the original data sources, ensuring consistency and integrity in data representation.


## Domain

Each organization is structured into various departments based on different workloads, such as sales, manufacturing, marketing, and others, which are referred to as domains. For example, 'Customer Churn Prediction' Data Product falls under the marketing domain which have inputs, outputs, and a data model specific to the marketing domain. Domain for each Data Product is defined in its manifest file.

<center>
<img src="/interfaces/data_product_hub/domain.png" alt="DPH" style="width:40rem; border: 1px solid black;" />
<figcaption><i>Domain</i></figcaption>
</center>

## Use case

A use case defines a specific scenario in which a Data Product can be utilized to achieve a particular objective or solve a specific problem. Use cases illustrate how data can be applied in real-world situations, helping stakeholders understand the practical applications of the Data Product. For instance, the 'Customer Churn Prediction' Data Product falls under the customer segmentation use case, which focuses on identifying distinct groups of customers based on behavior and characteristics. This allows organizations to tailor their strategies and improve customer retention. Each use case is defined within the Data Product manifest file, outlining its intended purpose and the context in which it should be used.

<center>
<img src="/interfaces/data_product_hub/usecase.png" alt="DPH" style="width:40rem; border: 1px solid black;" />
<figcaption><i>Use case</i></figcaption>
</center>







