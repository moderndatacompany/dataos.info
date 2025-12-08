# Google Sheets

Nilus supports **Batch ingestion** from Google Sheets, allowing users to pull spreadsheet data into any supported destination. Each workflow run fetches the **full snapshot** of the sheet (or specified range).

!!! info
    Google Sheets does **not support Depot**. To configure connections, use **service account credentials** supplied via an Instance Secret.



## Prerequisites

The following are required to enable Batch Data Movement from Google Sheets.

### **Google Cloud Service Account**

To enable API-based access:

1. Create or select a Google Cloud project.

2. Enable the necessary APIs:


    - **Google Sheets API**
    - **Google Drive API**
  
3. Create a **Service Account**

    *(IAM & Admin → Service Accounts)*

4. Generate and download the **JSON key file**

    *(Service Account → Keys → Add Key → JSON)*

5. Share the **Google Sheet** with the service account’s email:
    - Email ends with: `@<project>.iam.gserviceaccount.com`
    - Only **Viewer** access is required.

### **Spreadsheet Access**

* Ensure the service account has been granted permission to view the sheet.
* Extract the **Spreadsheet ID** from the URL:

```bash
https://docs.google.com/spreadsheets/d/<spreadsheetId>/edit#gid=0
                                            ↑ This part
```

**Example**

URL: `https://docs.google.com/spreadsheets/d/fkdUQ2bjdNfUq2CA/edit#gid=0`

Spreadsheet ID: `fkdUQ2bjdNfUq2CA`



### **Source Address**

Nilus utilizes a URI-style address format to configure Google Sheets ingestion. When configuring, ensure that only one of the following parameters is supplied:

- `credentials_path`: The file system path to the service account JSON file.
- `credentials_base64`: The Base64-encoded contents of the JSON file.


=== "Using credentials_path"
    ```yaml
    address: gsheets://?credentials_path=/etc/dataos/secret/<instance_secret_name>_<json_file_name>.json
    ```
    


=== "Using credentials_base64"
    ```yaml
    address: gsheets://?credentials_base64=<base64_encoded_json>
    ```

??? note "Google Sheet Instance Secret Manifest"

    Since the Google Sheet connector doesn't support Depot in DataOS, users must create an Instance Secret and use it to connect to the GA account by pointing to their service account credentials.

    ```yaml
    name: gsheetssecret
    version: v1
    type: instance-secret
    description: "write secret"
    layer: user
    instance-secret:
      type: key-value-properties
      acl: rw
      files:
        json_key_file: /Users/folder/Documents/gsheets-secrets.json #path to the json locally. 

    ```
    !!! warning
        It is important to note that the name of instance secrete should not contain any special character, it must be in a single word(as shown in above example manifest) without `-` and `_` to work properly. 


**URI Parameters**

| Parameter            | Required        | Description                           |
| -------------------- | --------------- | ------------------------------------- |
| `credentials_path`   | One of required | File path to the service account JSON |
| `credentials_base64` | One of required | Base64-encoded JSON contents          |



## Sample Workflow Config

```yaml
name: google-sheets-src-test
version: v1
type: workflow
tags:
  - google-sheet
  - workflow
  - nilus-batch
description: Nilus Batch Service Sample
# workspace: public
workflow:
  dag:
    - name: google-sheet-src
      spec:
        stack: nilus:1.0
        compute: runnable-default
        resources:
          requests:
            cpu: 100m
            memory: 256Mi
        logLevel: Info
        dataosSecrets:
          - name: gsheetssecret
            allKeys: true
            consumptionType: propFile
        stackSpec:
          source:
            address: gsheets://?credentials_path=/etc/dataos/secret/gsheetssecret_gsheets-secrets.json
            options:
              source-table: "1OblKaJc2HwoprRNHSH9eKRdPlx1M45tUuzf5x9k_TNY.EMP_DATA" 
          sink:
            address: dataos://testawslh
            options:
              dest-table: "sandbox.gsheet_src_test"
              incremental-strategy: replace
```

!!! info
    Ensure that all placeholder values (such as secrets, compute, and destinations) are properly configured before deployment.



## Supported Attribute Details

Nilus supports the following source options for Google Sheets.

### **Source Options**

| Option         | Required | Description                                              |
| -------------- | -------- | -------------------------------------------------------- |
| `source-table` | Yes      | Specifies spreadsheet ID, sheet name, and optional range |



### **Defining Sheet and Range**

`source-table` controls which sheet (and optionally which rows/columns) are ingested.

**Supported Formats**

| Format                                    | Meaning                      |
| ----------------------------------------- | ---------------------------- |
| `fkdUQ2bjdNfUq2CA.Sheet1`                 | Entire sheet                 |
| `fkdUQ2bjdNfUq2CA.Sheet1!A:D`             | Column range A to D          |
| `fkdUQ2bjdNfUq2CA.Sheet1!A2:D100`         | Specific rows + columns      |
| `fkdUQ2bjdNfUq2CA.'Summary Sheet'!A1:C50` | Sheet name containing spaces |

**Examples**

```yaml
source:
  address: gsheets://?credentials_path=/path/to/file.json
  options:
    # Full sheet
    source-table: fkdUQ2bjdNfUq2CA.Sheet1

    # Column range
    # source-table: fkdUQ2bjdNfUq2CA.Sheet1!A:D

    # Explicit rows and columns
    # source-table: fkdUQ2bjdNfUq2CA.Sheet1!A2:D100

    # Sheet with spaces
    # source-table: fkdUQ2bjdNfUq2CA.'Summary Sheet'!A1:C50
```

!!! warning
    Google Sheets is **always a full snapshot source**. Nilus does not detect:

    - New rows
    - Row updates
    - Deleted rows

### **Behavior by Destination Strategy**

| Strategy  | Result                                               |
| --------- | ---------------------------------------------------- |
| `append`  | Full sheet appended each run → duplicates created    |
| `replace` | Table is overwritten with latest snapshot            |
| `merge`   | Not supported unless destination handles merge logic |

!!! tip "Recommendation"
    Using `append` will generate duplicates. For production workloads, use:

    ```yaml
    incremental-strategy: replace
    ```

**Example**

```yaml
source:
  address: gsheets://?credentials_path=/secrets/gsheets-sa.json
  options:
    source-table: fkdUQ2bjdNfUq2CA.Sheet1

sink:
  address: lakehouse://my-lakehouse
  options:
    dest-table: analytics.sheet1_data
    incremental-strategy: replace
    aws_region: us-east-1
```



## Troubleshooting

| Issue                   | Cause                                 | Fix                                       |
| ----------------------- | ------------------------------------- | ----------------------------------------- |
| `403 Permission denied` | Sheet not shared with service account | Share the sheet and grant Viewer access   |
| “Invalid Credentials”   | Wrong path or corrupt base64 string   | Re-download or re-encode JSON file        |
| Sheet not found         | Invalid sheet name or ID              | Verify `source-table` syntax              |
| Slow ingestion          | Very large sheets / large ranges      | Restrict to smaller A1 ranges             |
| Duplicate rows          | Using append mode                     | Switch to `incremental-strategy: replace` |

