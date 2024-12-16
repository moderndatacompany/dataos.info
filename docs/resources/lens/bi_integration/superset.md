# Superset

<aside class="callout">
💡 For a streamlined and user-friendly integration with Superset, use the Data Product Hub interface. This approach allows you to easily integrate your Lens model's semantic model with Superset, eliminating the need to manually work with `curl` commands.

To get started with Superset integration through the Data Product Hub, refer to the link below:

<a href="/interfaces/data_product_hub/activation/bi_sync/superset/">Access the Superset integration guide</a>.
</aside>


## Prerequisites

- **Curl**: Ensure `curl` is installed on the system. For Windows users, `curl.exe` may be required.

- **Lens API endpoint**: The API endpoint provided by Lens to sync semantic model, enabling integration with Superset.

- **Access credentials**: Access credentials such as username, password, and host are required for Superset.

Superset requires the login credentials (username and password) and the host address where Superset is hosted. The command establishes a database and table with a live connection to the Lens model in Superset, enabling direct interaction with and visualization of data from Lens within the Superset environment.

## Steps

To sync the Lens model with Superset, follow these steps:

**Step 1: Run the curl command**

Copy the curl command syntax below and replace the placeholders with the actual values.

=== "Syntax"

    ```bash
    curl --location --request POST 'https://<DATAOS_FQDN>/lens2/sync/api/v1/superset/<WORKSPACE_NAME>:<LENS-NAME>' \
    --header 'apikey: <apikey>' \
    --header 'Content-Type: application/json' \
    --data-raw '
    {
        "username": "<superset username>",
        "password": "<superset password>",
        "host": "https://superset-<DATAOS_FQDN>"
    }
    ```

=== "Example"

    ```bash
    curl --location --request POST 'https://liberal-monkey.dataos.app/lens2/sync/api/v1/superset/public:company-intelligence' \
    --header 'apikey: aueniekQa==' \
    --header 'Content-Type: application/json' \
    --data-raw '
    {
        "username": "adder_1",
        "password": "adder_1",
        "host": "https://superset-liberal-monkey.dataos.app"
    }
    ```

**Command parameters:**

- **`URL`**: `https://liberal-monkey.dataos.app/lens2/sync/api/v1/superset/public:quality360`. This is the endpoint for syncing with Superset.

- **`DataOS FQDN`**: Current DataOS FQDN, e.g., `liberal-monkey.dataos.app`.

- **`--header 'Content-Type: application/json'`**: Specifies the content type as JSON.

- **`Lens_Name`**: Name of the Lens, e.g., `quality360`.

- **`API_Key`**: DataOS API key. The DataOS API key for the user can be obtained by executing the command below.

    ```bash
    dataos-ctl user apikey get
    ```

Upon initiation, a response will be received:

```bash
{
    "message": "started"
}
...
{
    "message": "Superset project creation and sync completed successfully."
}
```

Once the command is executed in the terminal, results will be visible in the Superset app as demonstrated below:

Please follow the steps outlined to see the result:

**Step 2 Go to DataOS**: Go to DataOS and select Superset.

  <div style="text-align: center;">
      <img src="/resources/lens/bi_integration/superset2.png" alt="Superset Configuration" style="max-width: 80%; height: auto; border: 1px solid #000;">
  </div>

**Step 3 Navigate to Datasets tab:** Here, each entity will appear as a dataset.

  <div style="text-align: center;">
      <img src="/resources/lens/bi_integration/superset3.png" alt="Superset Configuration" style="max-width: 80%; height: auto; border: 1px solid #000;">
  </div>

The setup is complete. Further exploration and analysis can be performed in Superset.


## Data policies and security

Any data masking, restrictions, or permissions defined by the publisher will automatically be enforced for all viewers of the report, ensuring consistent data security and compliance. However, the behavior of data policies (e.g., masking) depends on who is the user of the Superset.