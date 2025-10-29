# Salesforce

**Salesforce** is a cloud-based customer relationship management (CRM) platform that helps businesses manage sales, customer interactions, and business processes. It provides tools for sales automation, customer service, marketing, analytics, and application development.

!!! info
    Salesforce does not support Depot. To configure connections, use service account credentials provided through the Instance Secret Resource in URI.


## Prerequisites

The following are the requirements for enabling Batch Data Movement in Salesforce:

1. Salesforce is not integrated with Depot. Therefore, direct credentials are required to establish the connection.
2. To create an instance secret for your Nilus workflow, contact the DataOS admin or DataOS Operator. Once created, this secret can be referenced within the Nilus Workflow to facilitate the connection securely.

Salesforce is not integrated with Depot. Therefore, direct credentials are required to establish the connection via URI, which needs the following parameters:

* `username`: Salesforce account username
* `password`: Salesforce account password
* `token`: Salesforce security token (generated/reset in Salesforce settings)
* `domain`: Salesforce instance domain

To create an instance secret for your Nilus workflow, contact the DataOS admin or DataOS Operator.

??? note "DataOS Instance Secret for Salesforce"

    ```yaml
    version: v1 
    name: salesforce-cred 
    type: instance-secret 
    description: salesforce cred for connection with dataos
    layer: user
    instance-secret: 
      type: key-value
      acl: r 
      data: 
        SALESFORCE_USERNAME:  (base64 encoded value)
        SALESFORCE_PASSWORD: (base64 encoded value)
        SALESFORCE_TOKEN: (base64 encoded value)
        # SALESFORCE_DOMAIN: (base64 encoded value)
    ```



Once created, this secret can be referenced within the Nilus Workflow to facilitate the connection securely. The syntax of URI is as follows:

```yaml
address: "salesforce://?username={SALESFORCE_USERNAME}&password={SALESFORCE_PASSWORD}&token={SALESFORCE_TOKEN}"
```

## Sample Workflow Config

```yaml
name: wf-salesforce-account
version: v1
type: workflow
tags:
    - salesforce_account
    - nilus_batch
workflow:
  dag:
    - name: sf-account
      spec:
        stack: nilus:1.0
        compute: runnable-default
        logLevel: INFO
        resources:
          requests:
            cpu: 1000m
            memory: 1500Mi
        dataosSecrets:
          - name: salesforce-cred
            allKeys: true
            consumptionType: envVars
        envs:
          DATAOS_WORK_DIR: /etc/dataos/work
        stackSpec:
          source:
            address: "salesforce://?username={SALESFORCE_USERNAME}&password={SALESFORCE_PASSWORD}&token={SALESFORCE_TOKEN}&domain=b3JnZmFybS1hN2NhNjdkNzZkLWRldi1lZC5kZXZlbG9wLm15Cg=="
            options:
              source-table: account
              columns: "name,industry,annualrevenue"
          sink:
            address: dataos://icebaselh:salesforce_objects/account?acl=rw
            options:
              incremental-strategy: replace
              aws_region: us-west-2

```

!!! info
    Ensure that all placeholder values and required fields (e.g., connection `addresses`, `compute`, and access credentials) are properly updated before applying the configuration to a DataOS workspace.


Deploy the manifest file using the following command:

```bash
dataos-ctl resource apply -f ${{path to the Nilus Workflow YAML}}
```

## Supported Attribute Details

Nilus supports the following source options for Salesforce:

| Option         | Required | Description                                                        |
| -------------- | -------- | ------------------------------------------------------------------ |
| `source-table` | Yes      | Salesforce object name (e.g., `account`, `opportunity`)            |
| `columns`      | No       | Optional list of fields to extract (default: all available fields) |

## Supported Objects

Nilus supports a subset of standard Salesforce objects. Each object has a **write disposition** that determines how data is loaded.

### **Replace Mode (Full Load)**

Objects always loaded in full:

| Object                   | Description                                                   |
| ------------------------ | ------------------------------------------------------------- |
| `user`                   | Information about users who have access to the Salesforce org |
| `user_role`              | Role definitions and hierarchy information                    |
| `contact`                | Contact details associated with accounts                      |
| `lead`                   | Information about potential opportunities                     |
| `campaign`               | Marketing campaign details                                    |
| `product` (Product2)     | Product catalog information                                   |
| `pricebook` (Pricebook2) | Price book definitions                                        |
|`custom:<custom_object_name>`	|Track and store data that’s unique to your organization. For more information about custom objects in Salesforce, To know more, visit [Custom Objects](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_custom_objects.htm)|

### **Append Mode (Incremental)**

Objects that support incremental loading as well (tracked automatically):

| Object                     | Tracking Field   | Description                                         |
| -------------------------- | ---------------- | --------------------------------------------------- |
| `opportunity`              | SystemModstamp   | Sales opportunities and related details             |
| `opportunity_line_item`    | SystemModstamp   | Products or services associated with an opportunity |
| `opportunity_contact_role` | SystemModstamp   | Contact roles associated with an opportunity        |
| `account`                  | LastModifiedDate | Customer/organization account details               |
| `campaign_member`          | SystemModstamp   | Links contacts or leads to campaigns                |

### **Field Handling**

* All available fields are retrieved automatically.
* **Compound fields** are excluded (except for `Name`).
* System fields (`SystemModstamp`, `LastModifiedDate`) are included for tracking.

### **Incremental Loading**

Salesforce objects with append mode support **automatic incremental loading**.

* **Tracking fields**:
    * `SystemModstamp` → most objects
    * `LastModifiedDate` → `account`
* Nilus automatically uses these fields — do **not** configure `incremental-key`.
* Only new or modified records are loaded.
