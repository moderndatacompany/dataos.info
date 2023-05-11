# Lens: Right-to-Left Data Engineering Approach

The Lens is a core DataOS primitive designed to break data silos between data producers and consumers and bring consensus through Data Contracts. The Lens leverages existing contracts and maps all declared attributes within the business model to the underlying physical data. Furthermore, a Lens can also refer to other lenses.

> A Data Contract is a set of predetermined rules, an agreement, between business domain experts and data engineers that abstractly describes the data to be exchanged. These constructs enable users to frame their business models and data questions and functionally bring related business concepts (entities) together. Once data contracts are defined and mapped, users and applications can start consuming these models.


Lens allows you to define a data contract that expresses a business concept via entities, measures & dimensions and helps end users access data autonomously using common business terms.

## Contrasting Traditional and Lens Approach

Lens is an interface that makes analytics accessible to everyone, not just data engineers or analysts with niche SQL skills. Lens translates all incoming data questions into SQL and issues these SQL queries to Minerva to execute them against the customer’s data stores. It employs a right-to-left data engineering approach, that starts with what the business needs and how they need it and then puts into place the technology solution to address those needs. 

In order to comprehend the manner in which Lens utilizes the right-to-left methodology, a practical example is presented below to facilitate comprehension of this method.

*Suppose a retail company's marketing manager needs to comprehend a customer's omnichannel journey by developing a Customer360 that encompasses a broad range of up to 50-100 attributes, such as customer profiles, addresses, phone numbers, loyalty information, order information, and brand engagement across multiple channels.*

In the traditional approach, data is extracted from multiple sources and tables. A business user relies on data engineers to extract the governed information, which is time-consuming and frustrating for both parties. Moreover, even if the data is retrieved, it may not be in the required format, resulting in further delays in getting what was requested.

The Lens approach lets the business user define the outcome and end state, and the system automates the process of getting them the data. The Lens creates a logical model on top of the underlying data, which is very business-friendly. Business users can get the insights they want, reducing their reliance on the data engineering teams. Even if there are changes in the business logic, the business user can change the model as everything is defined logically without ever feeling apprehension of pipeline breakage. 

In summary, the Lens approach saves a lot of resources and costs.

## Advantages of Lens over Traditional Methods

Modeling data, designing fanciful dashboards and reports, and analyzing key KPIs is not new; it has been around for a long time. A missing element in this context has been an ecosystem that can provide teams/services/tools to model and access key business contexts collaboratively and consistently, providing a logical, business-friendly view of data. The Lens addresses this issue.

The advantages that Lens brings over the traditional method are summarized in the table below -

| Parameter | Traditional Way | Lens (The Modern Way) |
| --- | --- | --- |
| Flexibility | Data engineers and analysts had to redesign the data pipelines whenever new data, fact tables, or dimension tables were added or removed, resulting in a loss of time and money.  | Within Lens, if at any moment the underlying business logic, fact table, dimensional table, or data changes, data engineers and analysts can just come and declare without affecting the rest, as everything is defined on the logical tier. |
| Dependency | Business teams had too much dependency on the engineering teams - to get the right data, formulate logic into workflows, and build data models. Self-serve was barely there. | With Lens, business teams can define the model themselves using commonly understood business terms - reducing their dependency on engineering teams who can focus on mapping the entities to the underlying data. |
| Durability | Every time the underlying data or business logic changes, there is always a possibility of breakage of data pipelines. | As everything is defined logically within Lens, there is no fear of breakage of data pipelines in case the underlying data or business logic changes. |
| Consensus | No contract or agreement existed between the downstream application user and the organization regarding what they asked for and what they will receive. A lack of understanding of how business teams define metrics led data engineers to model metrics based on their logic, leading to more to and fro and rebuilding pipelines. | As the Lens is a data contract between business domain experts and data engineers, it gives a stronger guarantee regarding how data needs to be exposed. Business domain experts can declare what data models, measures, and metrics they need and which dimensions they wish to slice, dice, or roll up their measures and receive what they asked for. |
| Accessibility | Self-serve analytic tools enabled business teams to perform complex analyses and abstract the complexities of SQL. Still, they localize the models within the tool, making them inaccessible outside the tool they were embedded in. | Using Lens, data from disparate sources is universally accessible through commonly understood business concepts. |
| Cost | Traditionally, to analyze data define KPIs, and build dashboards, business folks had to stitch together multiple software, which all come at a price and require expertise to operate them, resulting in overhead expenditure for the organization. | With Lens, all these tasks can be taken care of in a simple, secure, governed, and cost-effective manner without any dependency on propriety software. Just point a Lens at existing / legacy data systems and get instant analysis without needing this middleware to be built out. |
| Programming Approach  | Every tool for Data Storage, Data Cataloging, Data Processing, Governance, and Data Movement requires its specific programming language. | Enables a more straightforward low-code/declarative approach to define and query semantic objects through YAML & abstracted SQL. |
| Time-Saving | Business domain experts and data engineering teams rely heavily on each other, resulting in delays.  | Using Lens, business domain experts can completely decouple themselves from data engineering and focus on defining the models, while Data engineers can focus on mapping the underlying data to the respective business entities. |
| Platform Dependency | Data consumption from various data platforms requires separate data pipelines for every use case. | It works with a variety of data platforms and with different data types, native data platform dialects, and extensions. Depending on the underlying data platforms, you can consume business concepts through downstream applications. |
| Modality | Business Teams, Data Scientists, and App Developers depend on several tools to build their specific use cases. | Multi-modal in nature. It gives much more stable ground not only for business teams but also for data scientists and app developers to use this to build on.  |
| Data Movement | Extensive data movement from legacy to the cloud involves high risk and cost. | Intelligent data movement (move only data that needs to be operationalized). This significantly reduces cost and risk. |
| Storage Usage | Multiple copies of data result in storage wastage and high storage costs. | Doesn't make copies of data, reducing storage costs. |