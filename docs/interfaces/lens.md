# Lens

Lens is a consistent modeling layer capable of accessing and modeling data from disparate sources. It not only supports the ability to connect underlying data to real-world business objects but also enables you to formulate and delineate measures, KPIs, and relationships between different business concepts, thereby facilitating data-driven decision-making. Lens promotes data definition sharing and brings consensus among teams around data definitions, creating a unified and consolidated view of data across the organization. It is designed to break down data silos and foster mutual agreement between data producers and consumers by implementing Data Contracts.

<center>

![Picture](lens/lens.png)

</center>

<figcaption align = "center">Placement of Lens Ecosystem between Sources and Data Consumers</figcaption>

> A data modeling layer is an interface that lays over the underlying data and consistently exposes commonly understood business terms (such as product, customer, or revenue) to the end consumers. It allows business users to consume the data how they understand it, get what they need, and realize self-service without constantly relying on data engineers for data requests. 

## Supported data sources in Lens

Lens can be built on all sources that Depots support. Lens lets you connect to and access data from managed and unmanaged object storage like CSV, parquet, Amazon S3, Azure Blob Storage, streaming sources like Pulsar, and relational and non-relational databases like PostgreSQL, MySQL, BigQuery, etc.

For a comprehensive guide on creating and deploying a Lens, refer to the [Building a Lens](/interfaces/lens/building_lens/) section.

## Lens UI
On opening the Lens app, you can view all the Lenses created and available to consume.

![Lens Home Page](lens/lens_homepage.png)

<figcaption align = "center">Lenses</figcaption>
<br>

Clicking on the specific Lens will open the details where entities and their schema are displayed along with   the tabs to see the relationship of the entities and definitions.
![Lens Dtails](lens/lens_details.png)

<figcaption align = "center">Lens details</figcaption>

## Lens utilities

Lens Utilities offer additional functionality and tools to enhance the Lens experience, providing support for various operational and analytical use cases.

### **Lens Explorer**

Lens Explorer is a discover and analyze tool for answering questions about anything in the Ontology layer. Its intuitive graphical user interface (GUI) empowers organizations to achieve semantic access to their data, making it possible for everyone to derive insights from it. With Lens Explorer, users can effortlessly explore business ontologies, create visually appealing charts, and generate deep insights using a user-friendly interface.

Lens Explorer's drag-and-drop interface allows users to easily build customized segments, generate insights, and create a comprehensive view for their data from the deployed Lens. They can query Lens to get answers to complex data questions in an exploratory fashion. Lens Explorer can assist personas such as Business Analysts, Product Managers, Product Analysts, and many more to move faster in their data journey. To learn more, refer to [Lens Explorer](lens/lens_explorer/lens_explorer.md).

![Lens Dtails](lens/lens_details_explorer.png)

<figcaption align = "center">Lens Explorer</figcaption>
### **Lens Views**

The Lens Views utility encompasses readily-shareable views formulated atop Lenses. This tool enables users to store their crafted views while exploring Lenses, and seamlessly retrieve them at their convenience. These views include a diverse array of use cases and scenarios. A list of published views will be shown. Every view listed an owner’s name, Lens name, and associated time of creation. These views can be filtered by owners or their states(Draft, Published). Users can view the analysis with refreshed data by re-executing the query. 
 
<center>

![Graphical User Interface of the Lens Views](lens/lens_ecosystem/lens_views.png)

</center>

<figcaption align = "center">Graphical User Interface of the Lens Views</figcaption>

#### **Cloning a Lens view**
Users have the capability to clone a lens view and customize according to their requirements. Cloning streamlines the process of creating variations of a lens view, eliminating the need to recreate a view from scratch. Users can experiment freely with different data selections.

Follow the steps to create a clone of an existing Lens view:

1. Navigate to any published Lens View, then click on the **Clone View** icon. Confirm your selection to create a cloned view.
    ![Cloning Lens Views](lens/lens_ecosystem/clone_view.png)

    <figcaption align = "center">Clone a Lens view</figcaption>

2. Make the required modifications, then click **Run Query** to generate the view. After the query execution is complete, users will be presented with the option to **Save View**.
    ![Cloning Lens Views](lens/lens_ecosystem/save_cloned_view.png)

    <figcaption align = "center">Make changes and save the view</figcaption>
3. Input a new name and description for the cloned view to save it. The cloned view will be stored in Draft Mode. Access the cloned lens view by toggling the Drafts button.
    ![Draft mode Lens views](lens/lens_ecosystem/draft_views.png)

    <figcaption align = "center">Lens views in draft mode</figcaption>

<aside class="callout">🗣 Lens views in Draft mode are not eligible for cloning. Users are required to publish the view prior to initiating the cloning process. </aside>

#### **Editing an existing view**
Users can edit an existing Lens view that they own.
![Edit mode](lens/lens_ecosystem/edit_view.png)

<figcaption align = "center">Editing a view</figcaption>

## Elements of a Lens

The fundamental constituents of both Lens and contract encompass an amalgamation of data elements: fields, entities, dimensions, and measures. These elements collectively serve the purpose of outlining the composition and logic of data models. To know more about these elements, refer to 
[Elements of Lens](lens/elements_of_lens/elements_of_lens.md).

## Lens ecosystem

In addition to the lack of alignment between data producers and consumers, the absence of well-defined APIs can result in siloed data definitions within the tool, hindering collaboration among teams that use various business intelligence tools to model metrics.

To tackle this challenge, the Lens Ecosystem offers a solution by allowing the association of relevant semantics to raw data and subsequently making these ontologies accessible to all downstream consumers. This includes applications, tools, and users, enabling a cohesive and consistent understanding of the data across the entire ecosystem. Refer to [Lens Ecosystem ](lens/lens_ecosystem/lens_ecosystem.md) to discover further details.
