# Lens

Lens  is a logical modeling layer designed to empower analytical engineers, the key architects of business intelligence, with a model-first approach. By leveraging Lens , data products can be created to inform decision-making, ensuring that data is logically organized and aligned with business objectives from the outset. To understand about the Model-first approach click [here](/resources/lens/core_concepts/)

As a core resource within the DataOS ecosystem, Lens  enhances the entire data product lifecycle, delivering substantial improvements in developer experience, consumption patterns, and overall data management.

> The data modeling layer serves as an interface that overlays the underlying data, consistently presenting business users with familiar and well-defined terms like "product," "customer," or "revenue." This abstraction enables users to access and consume data in a way that aligns with their understanding, facilitating self-service analytics and reducing dependence on data engineers for ad-hoc data requests. 

<div style="text-align: center;">
    <img src="/resources/lens/lens.png" alt="Untitled(5)" style="max-width: 100%; height: auto; border: 1px solid #000;">
   <figcaption>Placement of Lens Ecosystem between Sources and Data Consumers<figcaption>
</div>

                                                    
## Key features of Lens 

Lens  is engineered to handle complex and large-scale data models with ease. Key features include:

**Code Modularity:** The platform supports modular code structures, simplifying the maintenance of extensive models, especially when dealing with entities, dimensions, and measures. This modularity facilitates efficient development and management, enabling teams to navigate large codebases without unnecessary complexity.

**YAML Boilerplate Generation:** Lens  offers a tailored template generator through its VS Code plugin, streamlining the creation of Lens YAML files. This enhancement reduces the manual effort involved in setting up and ensures consistency across models.

**Advanced Linter Capabilities:** With refined linter functionalities, Lens  provides more relevant and precise error detection during deployment. This improvement helps developers address issues more effectively, reducing the time spent troubleshooting generic or irrelevant errors.

**Real-time Verification and Validation:** A local development environment in Lens  enables real-time inspection and validation of models, minimizing the back-and-forth often associated with SQL syntax errors. The inclusion of a web app for model inspection further enhances the development process, ensuring that issues are identified and resolved before deployment.

**Customizable Views:** Lens  introduces customizable views, allowing users to create multiple data slices tailored to their specific business needs. These views can be easily edited, queried, and seamlessly integrated with BI tools, offering greater flexibility in data analysis and reporting.

### **Interoperability Enhancements**

Lens  is designed to work seamlessly with external applications and tools, making it easier to integrate with existing workflows:

**API Support:** With the addition of Postgres API, Rest API, and GraphQL support, Lens  simplifies application development, enabling smoother interactions with external systems and reducing the need for manual translation of LQL to SQL.

**First-Class Integration:** Lens  offers robust integration with Superset, with ongoing efforts to extend this seamless connectivity to Tableau and PowerBI. This integration ensures that data models can be effectively utilized across various BI platforms, enhancing the overall analytics experience.

### **Performance Enhancements**

Lens  is optimized for performance, particularly when working with large datasets:

**Query Engine:** Lens  supports Themis, a Spark-native query engine, which further boosts performance, ensuring that data teams can handle large-scale queries with improved efficiency and speed.


## Lens Local Set-up

**Pre-requisites**

Before setting up Lens 2.0, ensure you have the following dependencies installed on your system

1. Docker  (Docker to run Lens 2 in an isolated environment on our local system)
2. Docker-compose  (Lens leverages Docker Compose for configuring multi-container Docker applications)
3. Postman App/Postman VSCode Extension (For querying and testing lens)
4. VS Code (Code editor to build Lens Model YAMLs)
5. VS Code Plugin (This is optional. It will aid in creating Lens 2.0 views and tables)

To install the above prerequisites, refer to the detailed doc [here](/resources/lens/prerequisites).

If you are familiar with how to set up and run a Lens Project and you have an existing Lens Model that you want to run, directly jump to this step

## How to consume Lens ?

Now that Lens  has successfully run locally without any errors, you can proceed to utilize it by querying or [consuming Lens](https://www.notion.so/How-to-Consume-Lens-2-0-5aead18ee43443cf95c14c622216b575?pvs=21). By consuming Lens locally using GraphQL REST APIs and SQL APIs, you are testing its functionality before deploying it. This ensures that everything works as expected in your local environment before moving to the deployment phase. 

## Deploy

> Follow these straightforward [steps to deploy Lens ](https://www.notion.so/Deploying-Lens-98553d2e1a7d425080cee8247b49f457?pvs=21), making it accessible for others in your organization to use.
> 

## Consume Deployed Lens

> Consume a deployed lens using different tools and technologies.
> 

[Consuming a deployed Lens using Python](https://www.notion.so/Consuming-a-deployed-Lens-using-Python-eb076e56737f4f29bf7f82a641348b9a?pvs=21)

[Consuming a deployed Lens using a SQL client](https://www.notion.so/Consuming-a-deployed-Lens-using-a-SQL-client-c9c5114fa1c544c6830793df29c26006?pvs=21)

[Consuming a deployed Lens using Lens  Studio Explore](https://www.notion.so/Consuming-a-deployed-Lens-using-Lens-2-0-Studio-Explore-c93d4c4844bf4730b596408086600fcd?pvs=21)

[Consuming lens via GraphQL](https://www.notion.so/Consuming-lens-via-GraphQL-f9d939acb6de4541a8ea407a6e2ab549?pvs=21)

[Consuming Lens via Iris Board](https://www.notion.so/Consuming-Lens-via-Iris-Board-f41294582ed446759f533b6e67d8aa08?pvs=21)

[Sync with BI Tools](https://www.notion.so/Sync-with-BI-Tools-9894b393535c45219024159ac23dfc8f?pvs=21)

## Configuration

lens studio

https://liberal-donkey.dataos.app/lens2/studio/public:sales-intelligence/explore

iris board

- we make views in the lens folder to make irsi dashboard

https://liberal-donkey.dataos.app/lens2/studio/public:sales-intelligence/explore

[Installing Pre-requisites for Lens Local Dev](https://www.notion.so/Installing-Pre-requisites-for-Lens2-0-Local-Dev-b0e77b419f854081b6e59a06f20f4d0f?pvs=21)

[rough](https://www.notion.so/rough-85bd95185b2b40fea1764c2b8d3d2036?pvs=21)

[Lens Local Set up](https://www.notion.so/Lens-Local-Set-up-5e0c742506304ec286d42bae32428509?pvs=21)

[How to Consume Lens ](https://www.notion.so/How-to-Consume-Lens-2-0-5aead18ee43443cf95c14c622216b575?pvs=21)

[Deploying Lens](https://www.notion.so/Deploying-Lens-98553d2e1a7d425080cee8247b49f457?pvs=21)

```bash
export PGPASSWORD='dG9rZW5fZ3JhdGVmdWxseV9ldmVubHlfb3Blbl9naWJib24uYzQ3MjAyNjItYTQ1ZC00MzM1LWE5ZjgtOGZjYWI2NDNjNzRl' && psql -U postgres -h localhost -p 25432 -d postgres

```