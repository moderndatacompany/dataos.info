# Governance

Nilus inherits and integrates seamlessly with DataOS's built-in governance layer, ensuring secure, role-based access to its ingestion workflows and services, configurations, observability endpoints, and data access patterns.

### **Governing Access to Observability APIs**

Nilus exposes observability endpoints for tracking pipeline health, reviewing logs, and accessing operational metrics. To ensure these endpoints are securely accessed only by intended personas, such as platform engineers or operational users, governance is enforced using Bifrost.

Access control is managed through a **use-case** artifact in Bifrost. This artifact defines the set of API paths and HTTP methods that are allowed, and must be explicitly granted to a **user tag** (representing a user group or persona). Only users associated with this tag will be permitted to interact with the observability endpoints.

??? note "Step 1: Creating the Bifrost Use Case (if not created already)"

    ```yaml
    id: nilus-api-access  
    name: 'Nilus API Access'
    description: 'This will allow users to access the API endpoints of Nilus'
    category: data
    authorization_atoms:
      - get-path-ingress
    values:
    - authorization_atom_id: get-path-ingress
      variable_values:
      - path: /nilus/**
    ```

??? note "Step 2: Grant the use-case create above to a specific user group (or a user)"

    ![Grant Use Case](../../.gitbook/assets/image%20(9).png)

