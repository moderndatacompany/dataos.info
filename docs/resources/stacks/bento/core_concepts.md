# Core Concepts

## Key features of Bento

Bento offers a wide range of features that make it an ideal solution for stream processing, including:

- **No Runtime Dependencies:** Bento utilizes static binaries with no runtime library dependencies, simplifying deployment.

- **Resilient:** Built with an in-process transaction model, Bento ensures at-least-once delivery without persisting messages during transit. It gracefully handles back pressure by temporarily stopping consumption when output targets block traffic.

- **Scalability:** Bento is designed for horizontal scalability, allowing seamless scaling as data volume increases.

- **Declarative Configuration:** Bento employs a declarative approach, eliminating the need for code compilation or building.

- **Observability:** Integration with Prometheus enables the collection of logs and metrics for better observability.

- **Cloud Native:** Bento is compatible with integration frameworks, log aggregators, and ETL workflow engines, making it a cloud-native solution that can complement traditional data engineering tools or serve as a simpler alternative.

- **Extensible:** Bento supports extension through Go plugins or subprocesses.

- **Stateless and Fast:** Bento is designed to be stateless and horizontally scalable. However, it can interact with other services to perform stateful operations.

- **Flexibility:** Bento allows connectivity with various sources and sinks using different brokering patterns. It facilitates single message transformation, mapping, schema validation, filtering, hydrating, and enrichment through interactions with other services, such as caching.

- **Bloblang:** Bento includes a built-in lit mapping language, Bloblang, which enables deep exploration of nested structures for extracting required information.

- **Payload Agnostic:** Bento supports structured data in JSON, Avro, or even binary formats, providing flexibility in data processing.

- **Real-time Data Processing:** Bento is designed for real-time data processing, making it suitable for scenarios requiring immediate ingestion and processing of generated data.

- **High Configurability:** Bento offers high configurability, allowing the construction of complex data processing pipelines that transform and enrich data during ingestion.