# Observability

## API Endpoints

The following are the Nilus Manager (Nilus Server) endpoints that allow users to review and audit all deployed or currently running data pipelines:

!!! info "API Documentation"
    The following endpoints are available for monitoring and observability. The OpenAPI specification can be accessed through the provided links for detailed API documentation.

### **Health Check Endpoint**

**GET** `/nilus/research:nilus-server/health`

Returns the health status of the Nilus server.

### **Metrics Endpoint**

**GET** `/nilus/research:nilus-server/metrics`

Provides Prometheus-compatible metrics for monitoring pipeline performance.

### **Server Information**

**GET** `/nilus/research:nilus-server/info`

Returns general information about the Nilus server instance.

### **Pipeline Management**

**GET** `/nilus/research:nilus-server/api/v1/pipelines`

Lists all registered pipelines in the system.

**GET** `/nilus/research:nilus-server/api/v1/pipelines/{resource_id}/runs`

Retrieves run history for a specific pipeline.

**GET** `/nilus/research:nilus-server/api/v1/pipelines/{resource_id}/latest`

Gets the latest run information for a specific pipeline.

### **Pipeline Statistics**

**GET** `/nilus/research:nilus-server/api/v1/pipelines/stats`

Provides aggregate statistics across all pipelines.

**GET** `/nilus/research:nilus-server/api/v1/pipelines/{resource_id}/stats`

Returns statistics for a specific pipeline.

### **CDC-Specific Endpoints**

**GET** `/nilus/research:nilus-server/api/v1/cdc/offset-storage`

Retrieves CDC offset storage information for tracking replication progress.

**GET** `/nilus/research:nilus-server/api/v1/cdc/offset-keys`

Lists available offset keys for CDC operations.

**GET** `/nilus/research:nilus-server/api/v1/cdc/schema-history`

Provides schema evolution history for CDC operations.

!!! info "OpenAPI Documentation"
    For detailed API specifications, refer to the OpenAPI documentation available through the Nilus server endpoints.