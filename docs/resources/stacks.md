# Stacks

In DataOS, Stacks are programming paradigms that facilitate the processing and management of data. They serve as extension points for runnable [DataOS Resources](../resources.md), [Workflow](./workflow.md), and [Service](./service.md), offering configurable attributes to meet specific requirements and enhance functionality.

As a [DataOS Resource](../resources.md), each Stack is defined by unique attributes and metadata that define its intended purpose and capabilities.

DataOS provides a comprehensive set of built-in stacks while also allowing the flexibility to add custom stacks as needed.

## Built-in Stacks in DataOS

### **Flare**

[Flare](./stacks/flare.md) is a powerful declarative Stack designed specifically for large-scale data processing tasks.

### **Benthos**

[Benthos](./stacks/benthos.md) is a high-performance, resilient, and declarative stream processing Stack.

### **Beacon**

[Beacon] Stack is a standalone HTTP server that exposes API endpoints on top of a Postgres database. It offers a single flavor `beacon+rest` that enables exposure of REST APIs on Postgres database.

### **Alpha**

[Alpha](./stacks/alpha.md) Stack is a declarative DevOps SDK used for seamless deployment of data applications into production environments.

### **Data Toolbox**

The [Data Toolbox](./stacks/data_toolbox.md) Stack provides functionality to update Iceberg metadata versions to the latest available or to any specific version.

### **Scanner**

The [Scanner](./stacks/scanner.md) Stack in DataOS is a Python-based framework that allows developers to extract metadata from external source systems (such as RDBMS, Data Warehouses, Messaging services, etc.) as well as components/services within the DataOS environment.

These built-in stacks offer a wide range of capabilities, empowering data developers to efficiently build, process, and manage data within the DataOS ecosystem.
