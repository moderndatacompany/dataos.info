# Data Movement Architecture

Nilus is designed to overcome the limitations of traditional data movement solutions. It provides a modern, cost-efficient approach to data movement. Its architecture emphasizes extensibility, allowing it to evolve in alignment with changing enterprise needs.

The framework facilitates the onboarding of new data sources and destinations with minimal configuration, maximizing developer efficiency and ensuring operational maintainability. Nilus abstracts the complexities of data movement into a standardized pipeline model, enabling the creation of consistent and maintainable ingestion workflows.


<figure>
  <img src="/resources/stacks/nilus/images/nilus-arch.avif" style="width:40rem;" />
  <figcaption><i>Architecture of Nilus</i></figcaption>
</figure>




The Nilus Manager (Nilus Server) underpins this architecture by providing metadata management and observability across all pipeline stages. It ensures that execution details, metrics, and logs generated during extraction, normalization, and loading are persisted and made queryable for monitoring and auditing.

The Nilus Manager functions as a FastAPI-based, containerized web service that powers the core metadata tracking and observability layer of Nilus pipelines. It integrates with a PostgreSQL backend to persist structured metadata about pipeline execution and to expose Prometheus metrics for monitoring. Observability of both batch and CDC pipelines is essential for understanding anomalous behaviors, monitoring performance, identifying failures, and supporting audit workflows. With structured observability, it becomes easier to analyze runtime metrics, detect inefficiencies, and enhance pipeline reliability.

**Key characteristics of the Nilus Manager**

- A PostgreSQL transactional database backend that enables SQL-based querying of pipeline metadata.
- Four primary tables in the `public` schema—`runs_info`, `extract_info`, `normalize_info`, and `load_info`—each responsible for capturing execution metadata and operational metrics for specific pipeline phases.
- Configurable data retention policies (e.g., 30, 60, or 90 days) to manage storage of pipeline metadata.
- Long-term persistence of all metadata in wide-row format within the DataOS Lakehouse (object storage) to support auditability and analytical workloads.

## Data Movement Mechanism

Nilus supports following data movement strategies to facilitate efficient data transfer and integration: 

### **Change Data Capture**

**Change Data Capture (CDC)** is a method used to identify and propagate row-level changes—such as inserts, updates, and deletes—from a source database to a target system. This process enables the target system to remain synchronized with the source without requiring full data reloads.

In Nilus, CDC implementation is designed to deliver high-fidelity, low-latency change streams from source databases to the DataOS Lakehouse.

* **Log tailing**: The CDC engine reads directly from database transaction logs (e.g., PostgreSQL WAL).
* **Event modeling**: Each change event is captured and serialized as a JSON object containing the operation type (`OPERATION`), the previous state (`BEFORE`), and the new state (`AFTER`).
* **Iceberg integration**: Change events are written directly to Apache Iceberg tables in the DataOS Lakehouse. This approach provides up-to-date views and enables time-travel querying capabilities.

**Challenges Addressed by Nilus CDC**

CDC implementations often face significant complexity due to variability in database systems and the requirements of downstream processing. Nilus abstracts these challenges, including:

* **Divergent database internals**: Variability in transaction log formats (e.g., WAL, binlog, redo), permissions, retention policies, and schema changes can disrupt CDC pipelines.
* **Delivery semantics**: Ensuring exactly-once delivery across distributed systems requires careful coordination to prevent data duplication or loss.
* **Infrastructure simplification**: Traditional CDC stacks rely on components such as Kafka and Kafka Connect, which introduce operational overhead. Nilus CDC eliminates the need for Kafka, reducing infrastructure complexity.
* **Event ordering**: Out-of-order or late-arriving events are reconciled using Iceberg's atomic commit semantics.
* **Snapshot coordination**: Bootstrapping from an initial snapshot to continuous log-based ingestion is prone to gaps or duplication if not managed correctly.
* **Schema evolution**: Changes in the source schema must be reliably mapped to typed columnar formats and reflected in Iceberg metadata without compromising data integrity.
* **Operational concerns**: Check-pointing, fault recovery, throughput management, and data governance are essential to ensuring reliable CDC performance and are handled internally by Nilus.

### **Batch**

Batch data ingestion is the process of collecting and transferring large volumes of data at scheduled intervals from a source system into a data warehouse, data lake, or lakehouse. Rather than processing data in real time (as in streaming), batch ingestion groups data into chunks ("batches") and loads them periodically, like every hour, day, or week.

In Nilus, Batch ingestion is simple and cost-effective, as it involves scheduled processing that reduces infrastructure costs. Nilus batch ingestion offers several benefits and considerations:

* **Operational simplicity and ease of implementation:** Nilus batch ingestion streamlines data transfer processes, reducing setup complexity.
* **Efficient handling of high-volume data transfers:** Capable of moving large datasets effectively, optimizing throughput.
* **Suitable for off-peak scheduling to reduce system load:** Can be scheduled during low-traffic periods, minimizing impact on production systems.

## Data Flow in Nilus

Nilus organizes the data flow into three distinct stages, ensuring clarity, modularity, and scalability.

### **Extract**

The Extract phase is the entry point into the Nilus pipeline, responsible for interfacing directly with source systems to retrieve raw data. Nilus supports two primary extraction patterns — batch and CDC (change data capture).

* Batch extraction is typically used for bulk data movement, such as periodic imports from enterprise data warehouses or business applications. It is optimized for high-throughput and reliability, ensuring that even large datasets can be moved efficiently and consistently.
* In contrast, CDC caters to real-time monitoring of all the changes occurring on the target dataset/schema/database in the source. Here, Nilus captures all the inserts, updates, and deletes since the last sync, greatly improving performance and reducing the volume of data that needs to be processed.
* Extraction is schema-aware, meaning Nilus leverages schema hints and metadata to guide the process, ensuring the correct interpretation of source data types and structures.

### **Normalize**

Once raw data is extracted, the Normalize phase begins. This stage is critical for ensuring consistency. The goal of normalization in Nilus is to transform disparate source data into a unified, consumable format that aligns with the target data models used in the DataOS Lakehouse.

* Normalization involves multiple processes, beginning with schema inference and schema evolution handling. Nilus automatically detects the structure of incoming data and adapts gracefully to changes such as added columns or new data types. It intelligently flattens complex and nested structures based on the user-defined configurations, producing normalized relational tables.
* A particularly important feature of normalization is variant handling. Source systems may contain data with inconsistencies - fields that occasionally change type or structure. Nilus identifies and resolves these variations to produce a clean, type-consistent dataset.
* This entire process is optimized for speed and scalability, with configurable controls over memory usage, file sizes, and concurrency levels to ensure smooth and predictable processing.

### **Load**

The final stage of the Nilus pipeline is the Load phase, which is responsible for persisting the normalized data into the DataOS Lakehouse. This phase is engineered for reliability and operational excellence, ensuring that data lands in the lakehouse accurately, completely, and ready for downstream consumption.

* The load process begins with schema migration, where Nilus applies necessary schema changes to the destination to accommodate updates or new data structures introduced upstream. To maintain scalability and efficiency, loading is performed in chunks. This chunked loading approach divides large datasets into smaller segments, which are processed in parallel, improving throughput and reducing risk.
* To ensure data consistency and avoid duplication, Nilus employs idempotent load operations. Even if the load process is retried due to transient issues, the system guarantees that duplicate records are not created (unless the source contains duplicates). Robust error handling and recovery mechanisms are in place to detect issues during loading and automatically recover when possible.
* Finally, comprehensive monitoring and logging capabilities provide transparency and traceability, enabling teams to audit, troubleshoot, and optimize loading operations with confidence via prometheus metrics and detailed logs.

