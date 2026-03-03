# HubSpot

**HubSpot** is a cloud-based CRM platform used for managing marketing, sales, customer service, and operations workflows.

Nilus supports HubSpot as a **batch ingestion source**, allowing ingestion of CRM objects such as companies, contacts, deals, and custom objects into supported destinations (Lakehouse, PostgreSQL, Databricks, etc.).

!!! info
    HubSpot CRM object ingestion in Nilus functions as **a full refresh**. The ingestion process replaces the existing dataset entirely, as **incremental loading is not supported**. Always set `incremental-strategy` to `replace`. Each run re-fetches the complete dataset of CRM objects.

## Prerequisites

The following are the requirements for enabling Batch Data Movement from HubSpot:

### **Authentication**

* **HubSpot Private App access token** required for direct connections(usually starts with `pat-`).

* For creation of PAT in HubSpot, visit the [Documentation](https://developers.hubspot.com/docs/apps/legacy-apps/private-apps/overview#make-api-calls-with-your-app%E2%80%99s-access-token)

* Sample HubSpot Private App access token lookes like:

    ```bash
    pat-na1-8675309-abcd-1234-efgh-5678-ijklmnop9012
    ```

    **Token Structure Breakdown**
    - pat: Indicates it is a Private App Token.
    - na1: Refers to the data hosting region (e.g., North America).
    - The rest: A unique, secure string generated for your specific app.

### **Network Access**

* Outbound access from Nilus runtime to `https://api.hubapi.com`.

### **Required HubSpot Scopes**

* Your Private App must have access to the objects you ingest.
* Example scopes: `crm.objects.contacts.read`, `crm.objects.companies.read`, `crm.objects.deals.read`, `crm.schemas.read`.
* If missing, ingestion will fail with `403` errors.

### **Required Parameters**

* `api_key`: HubSpot Private App access token

### **Source Address**

Nilus connects to HubSpot via a Direct connection URI as shown below:

```yaml
address: hubspot://?api_key=<private-app-token>
```

## Sample Workflow Config

```yaml
name: nb-hubspot-test-01
version: v1
type: workflow
tags:
    - workflow
    - nilus-batch
description: Nilus Batch Workflow Sample for HubSpot to DataOS Lakehouse
workspace: research
workflow:
  dag:
    - name: nb-job-01
      spec:
        stack: nilus:1.0
        compute: runnable-default
        logLevel: INFO
        resources:
          requests:
            cpu: 500m
            memory: 512Mi
        stackSpec:
          source:
            address: hubspot://?api_key=${HUBSPOT_API_KEY}
            options:
              source-table: companies
          sink:
            address: dataos://testawslh
            options:
              dest-table: hubspot.batch_companies
              incremental-strategy: replace
```

!!! info
    Ensure that all placeholder values and required fields (e.g., connection addresses, slot names, and access credentials) are properly updated before applying the configuration to a DataOS workspace.



Deploy the manifest file using the following command:

```bash
dataos-ctl resource apply -f ${{path to the Nilus Workflow YAML}}
```


## Supported Attribute Details

Nilus supports the following source options for HubSpot:

| Option         | Required | Description                                                                 |
| -------------- | -------- | --------------------------------------------------------------------------- |
| `source-table` | Yes      | CRM object name (e.g., `companies`, `contacts`, `deals`, `custom:<object_name>`) |

HubSpot supports the following CRM objects as `source-table` values:

| Object                              | Description              | Type   |
| ----------------------------------- | ------------------------ | ------ |
| `companies`                         | Organization records      | Replace |
| `contacts`                          | Leads and customers       | Replace |
| `deals`                             | Sales deals               | Replace |
| `tickets`                           | Support tickets           | Replace |
| `products`                          | Product catalog           | Replace |
| `quotes`                            | Sales quotes              | Replace |
| `schemas`                           | Object schema definitions | Merge   |
| `custom:<object_name>`              | Custom object             | Replace |
| `custom:<object_name>:<associations>` | Custom object with associations | Replace |

### **Custom Object Examples**

1. To ingest a custom object:
    
    ```bash
    custom:<custom_object_name>
    ```
    
    Example:
    
    ```yaml
    source:
        address: hubspot://?api_key={HUBSPOT_API_KEY}
        options:
        source-table: custom:invoices
    ```
    
2. To include associations:
    
    ```bash
    custom:<custom_object_name>:<associations>
    ```
    
    Example:
    
    ```yaml
    source:
        address: hubspot://?api_key={HUBSPOT_API_KEY}
        options:
        source-table: custom:invoices:contacts,deals
    ```
`<associations>` is passed directly to HubSpot’s associations parameter (comma-separated list).


!!! info "Core Concepts"
    
    1. **Data Handling**
        
        * Full dataset retrieved per run.
        * Pagination handled automatically.
        * Schema inferred from API response.
        * Nested JSON fields preserved as structured data.
        * Associations returned as nested arrays (if requested).

    2. **Data Volume Considerations**
        
        * HubSpot APIs are rate-limited.
        * Large CRM datasets may require multiple API calls.
        * Full refresh can be slow for large accounts.

## Common Errors

| Error Code | Error Message   | Mitigations                                                                 |
| ---------- | --------------- | --------------------------------------------------------------------------- |
| 429        | Too Many Requests | Reduce pipeline frequency; Retry after backoff; HubSpot API quota exceeded; Reduce job frequency; Stagger parallel loads |
| 401        | Unauthorized    | Invalid or expired token; Verify token validity; Ensure correct scopes assigned; Confirm Private App is active |
| 403        | Forbidden       | Missing required object scopes; Verify token validity; Ensure correct scopes assigned; Confirm Private App is active |


