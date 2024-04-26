# On-demand Computing

On-demand computing is a delivery model that provides users with flexible access to computing resources, including computing power, storage, and memory, as and when they are needed. This model eliminates the need for users to provision resources upfront for peak levels of business activity, as resources are allocated on an as-needed and when-needed basis. With on-demand computing, users can scale their resources up or down to meet changing business requirements, ensuring optimal resource utilization and cost efficiency.

## Tightly Coupled Storage and Compute

Traditional data warehouses are designed with a tight coupling between storage and compute, where the same cluster handles both data storage and computation. However, the storage and compute requirements for different workloads are not always linear and can vary significantly. This coupling often leads to underutilization or scarcity of resources, resulting in suboptimal utilization of the provisioned capacity.

In scenarios where enterprises need to scale compute capabilities while keeping storage relatively constant, such as during high-traffic periods or end-of-quarter consolidations, the traditional approach falls short. Scaling both functions simultaneously becomes impractical and costly. Decoupling storage and compute enables independent scaling, allowing enterprises to pay for the resources they use, based on their specific needs.

Additionally, the traditional cluster configuration lacks a shared data cluster. This leads to the need for multiple clusters to handle different types of workloads, resulting in data duplication as the required data is copied or moved to the respective workload clusters. This approach hampers data accessibility and introduces complexity.

## Decoupled Compute and Storage

Decoupling compute and storage provides the flexibility to scale each component independently, based on the specific requirements of different workloads. Enterprises can provision larger or smaller compute resources as needed. For example, running complex reporting queries that require extensive data scanning may warrant a larger compute cluster for a limited duration, while ad-hoc analysis on smaller datasets may require a long-running smaller cluster. This decoupling empowers enterprises to design their compute infrastructure to address specific needs and optimize resource allocation.

This decoupling is beneficial for managing both batch and interactive workloads. Different workloads, such as ETL processes, dashboard queries, periodic reports, and ad-hoc queries, have varying requirements in terms of dataset and cluster capabilities. By decoupling storage and compute, each department or team can have its own analytics setup, aligned with their specific application lifecycle and budget constraints. This approach results in significant cost savings and operational efficiencies, as resources are provisioned only when needed, in the required amount, and for the necessary duration.

## On-Demand Compute in DataOS

DataOS offers a powerful on-demand compute capability, allowing users to define and maintain a pool of resources, including networks, servers, storage, applications, and services. This resource pool caters to varying resource demands and computing requirements for various workloads.

When working with data in DataOS, which is stored in Depots using the Iceberg table format, users have the freedom to bring their own compute resources. The storage in DataOS follows the lake house pattern, providing an open data format. By maintaining data as a single source of truth, DataOS enables business and IT teams to access the required data, according to governance policies, without the need for data movement to local clusters. This streamlines data provisioning across the organization, ensuring efficiency and optimization.

Users can create Minerva query engine clusters within DataOS, allowing them to query data through depots in the system. Users can attach and create their own clusters within the DataOS instance, with billing attributed to their specific use cases. This approach enables cost-efficient resource allocation.

When deploying data processing jobs with Flare or querying data on Workbench, users can request the required compute resources. By understanding the nature of different queries and the optimal compute for each type, users can make informed decisions on performance and cost trade-offs, adjusting the compute accordingly.