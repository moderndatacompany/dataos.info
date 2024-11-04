# Worker: Core Concepts

## Key Characteristics

- **Continuous Execution**: Workers are built to run perpetually, performing their assigned tasks without a defined end time.
- **No Ingress**: Workers do not have ingress ports like [Services](/resources/service/).
- **Throughput-Based**: Workers are throughput-based and do not require synchronous responses.
- **Lightweight**: Workers are lightweight compared to [Services](/resources/service/), as they do not require multiple open network ports. This makes them faster to deploy and more efficient.
- **Specialized Execution**: Worker is a self-contained system, an independent entity, ideal for executing specific tasks within a larger application, providing focused functionality.
- **Autoscalability**: Workers can be autoscaled to handle larger workloads, making them highly adaptable.
- **Robustness**: Workers are perfect for use cases where robustness and continuous execution are essential.

## Workflow, Service, and Worker: Key Differences

[Workflow](/resources/workflow/), [Service](/resources/service/), and Worker are distinct runnable [DataOS Resources](/resources/), each with unique roles in the ecosystem. Data developers often face the dilemma of deciding when to use a Workflow, a Service, or a Worker in the DataOS environment. To aid in this decision-making process, the following table compares Workflow, Service, and Worker comprehensively, helping developers understand their distinct characteristics and optimal use cases within the DataOS ecosystem.

| Characteristic | Workflow | Service | Worker |
| --- | --- | --- | --- |
| *Overview* | Workflows orchestrate sequences of tasks, jobs, or processes, terminating upon successful completion or failure. | Services are long-running processes that continuously operate, serve, and process API requests. | Workers execute specific tasks or computations continuously without a defined end time. |
| *Execution Model* | Workflows process data in discrete chunks, following predefined DAGs (Directed Acyclic Graphs). | Services expose API endpoints and ingress ports for external data or request intake. They don’t have DAGs. | Workers perform continuous task execution independently, without synchronous inputs or ingress ports. |
| *Data Dependency* | Workflows follow predefined orders or DAGs, depending on data input sequences. | Services rely on incoming data through ingress ports for logic execution. | Workers are throughput-based and do not require synchronous inputs or ingress ports. |
| *Stack Orchestration* | Yes | Yes | Yes |
| *Scope* | Workspace-level | Workspace-level | Workspace-level |
| *Use Cases* | 1. Batch Data Processing Pipelines: Ideal for orchestrating complex data processing pipelines.<br>2. Scheduled Jobs: Perfect for automating tasks at specific intervals, such as data backups and ETL processes.  | 1. API Endpoints: Used to create API endpoints for various purposes, such as data retrieval and interaction with external systems.<br>2. User Interfaces: Suitable for building interfaces that interact with data or services. | 1. Continuous Processing: Perfect for tasks like real-time analytics, and event-driven operations.<br>2. Independence: Ideal for creating independent systems that perform specific tasks indefinitely. |

