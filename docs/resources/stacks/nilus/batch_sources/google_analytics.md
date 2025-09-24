# Google Analytics

Google Analytics provides website and app engagement data that can be ingested into the DataOS Lakehouse for reporting and analysis. Nilus supports **Batch ingestion** from Google Analytics (both **Universal Analytics** and **GA4**) using scheduled workflows.

!!! info
    Google Analytics does not support Depot. To configure connections, use service account credentials provided through the Instance Secret Resource in the URI.


## Prerequisites

The following are the requirements for enabling Batch Data Movement in Google Analytics:

### **Google Cloud Project**

* A project in Google Cloud Platform (GCP).
* Enable the required API:
    * **Google Analytics Data API (GA4)** (for GA4 properties).

### **Service Account**

* Create a **service account** in GCP IAM.
* Download the **JSON key file** for authentication.

### **Grant Analytics Access**

* In Google Analytics Admin:
    * **Admin → Account Settings → Account Access Management**.
    * Add the service account email as a **User** with at least **Read & Analyze** permission.

### **Required Parameters**

The following are the parameters required:

* `credentials_path`: Path to the service account credentials JSON (alternative to base64)
* `credentials_base64`: Base64-encoded credentials JSON (alternative to path)
* `property_id`: Google Analytics Property ID (numeric)

**Credentials Format Example**

```json
{
  "client_email": "service-account@project.iam.gserviceaccount.com",
  "project_id": "your-project-id",
  "private_key": "-----BEGIN PRIVATE KEY-----\\n...\\n-----END PRIVATE KEY-----\\n",
  "private_key_id": "private-key-id"
}
```

### **Source Address**

Nilus uses a URI-style source address:

=== "Custom Report"
    ```yaml
    address: google_analytics://?credentials_path=/path/to/creds.json&property_id=123456789
    ```
=== "Realtime Report"
    ```yaml
    address: google_analytics://?credentials_base64={GA_CREDS}&property_id=123456789
    ```

!!! info
    Instance Secrets can securely facilitate connections to Google Analytics within the Nilus Workflow. To create an Instance Secret for your Nilus Workflow, contact the DataOS admin or DataOS Operator.


??? note "Google Analytics Instance Secret Manifest"

    Since the Google Analytics connector doesn't support Depot in DataOS, users must create an Instance Secret and use it to connect to the GA account by pointing to their service account credentials.

    **User Creation and Asset Setup**

    *   **Create Service Account (GCP IAM):**

        ```bash
        gcloud iam service-accounts create ga-service-account \
            --display-name="Nilus GA Service"
        ```

    *   **Assign Roles:**

        ```bash
        gcloud projects add-iam-policy-binding my-gcp-project \
            --member="serviceAccount:ga-service-account@my-gcp-project.iam.gserviceaccount.com" \
            --role="roles/viewer"
        ```
    * **Add to GA Property:**
          * In GA Admin, add the service account email as a **User**.
          * Assign the **Read & Analyze** permission.

    ```yaml
    name: testga-new
    version: v1
    type: instance-secret
    description: "write secret"
    layer: user
    instance-secret:
      type: key-value-properties
      acl: rw
      files:
        json_key_file: /Users/folder/Documents/ga-test-creds.json
    
    ```



## Sample Workflow Config

```yaml
name: google-analytics
version: v1
type: workflow
tags:
    - google-analytics
    - workflow
    - nilus-batch
description: Nilus Batch Service Sample
# workspace: public
workflow:
  dag:
    - name: google-analytics-source
      spec:
        stack: nilus:1.0
        compute: runnable-default
        resources:
          requests:
            cpu: 100m
            memory: 256Mi
        logLevel: Info
        dataosSecrets:
          - name: testga
            allKeys: true
            consumptionType: propFile
        stackSpec:
          source:
            address: googleanalytics://?credentials_path=/etc/dataos/secret/credentials.json&property_id=<Property_ID>
            options:
              source-table: "custom:date,deviceCategory:sessions" 
          sink:
            address: dataos://testawslh
            options:
              dest-table: "schema.google-analytics"
              incremental-strategy: append
```

!!! info
    Ensure that all placeholder values and required fields (e.g., connection `addresses`, `compute`, and access credentials) are properly updated before applying the configuration to a DataOS workspace.


Deploy the manifest file using the following command:

```bash
dataos-ctl resource apply -f ${{path to the Nilus Workflow YAML}}
```

## Supported Attribute Details

Nilus supports the following source options for Google Analytics:

<table data-full-width="false"><thead><tr><th>Option</th><th>Required</th><th>Description</th></tr></thead><tbody><tr><td><code>source-table</code></td><td>Yes</td><td>Report definition in <code>&#x3C;report_type>:&#x3C;dimensions>:&#x3C;metrics></code> format</td></tr></tbody></table>

!!! info "Core Concepts"
    

    1.  **Report Types**

        Nilus supports both **Custom Reports** (historical data) and **Realtime Reports** (last 60 minutes).
        
    2.  **Incremental Loading**

        Incrementality is handled automatically using **time-based dimensions** (`date`, `dateHour`, `dateHourMinute`). You do **not** configure `incremental-key`.

    3.  **Table Name Format**

        The `source-table` parameter follows this structure:

        ```yaml
        <report_type>:<dimensions>:<metrics>[:<minute_ranges>]
        ```

        * `report_type`: `custom` or `realtime`
        * `dimensions`: Comma-separated list (e.g., `date,country`)
        * `metrics`: Comma-separated list (e.g., `sessions,pageviews`)
        * `minute_ranges`: (Realtime only, optional) e.g., `0-30`

### **Common Dimensions & Metrics**

1. **Time-Based Dimensions**

    * `date` → YYYY-MM-DD
    * `dateHour` → YYYY-MM-DD-HH
    * `dateHourMinute` → YYYY-MM-DD-HH:mm
 
2. **Common Dimensions**
 
      `country`, `city`, `device`, `browser`, `operatingSystem`, `pageTitle`, `pagePath`
 
3. **Common Metric**
 
      `sessions`, `users`, `newUsers`, `activeUsers`, `screenPageViews`, `conversions`, `totalRevenue`


