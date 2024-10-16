# Superset

## Prerequisites

- **Curl**: Ensure `curl` is installed on the system. For Windows users, `curl.exe` may be required.

- **Lens API endpoint**: The API endpoint provided by Lens to sync data with meta endpoint access.

- **Access credentials**: Access credentials such as username, password, and host are required for Superset.

Superset requires the login credentials (username and password) and the host address where Superset is hosted. The command establishes a database and table with a live connection to the Lens model in Superset, enabling direct interaction with and visualization of data from Lens within the Superset environment.

## Steps

**Step 1: Run the curl command**

To sync the Lens model with Superset, follow these steps:

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

- **`URL`**: `https://liberal-monkey.dataos.app/lens2/sync/api/v1/superset/public:sales360`. This is the endpoint for syncing with Superset.

- **`DataOS FQDN`**: Current DataOS FQDN, for example, `liberal-monkey.dataos.app`.

- **`--header 'Content-Type: application/json'`**: Specifies the content type as JSON.

- **`Lens_Name`**: Name of the Lens, for example, `sales360`.

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
`

Once the command is executed in the terminal, results will be visible in the Superset app as demonstrated below:

Please follow the steps outlined to see the result:

**Step 2 Go to DataOS**: Select Superset.

  <div style="text-align: center;">
      <img src="/resources/lens/bi_integration/superset2.png" alt="Superset Configuration" style="max-width: 80%; height: auto; border: 1px solid #000;">
  </div>

**Step 3 Navigate to Datasets tab:** Here, each entity will be available in the form of datasets.

  <div style="text-align: center;">
      <img src="/resources/lens/bi_integration/superset3.png" alt="Superset Configuration" style="max-width: 80%; height: auto; border: 1px solid #000;">
  </div>

The setup is complete. Further exploration and analysis can be performed in Superset.


## Data policies and security

Any data masking, restrictions, or permissions defined by the publisher will automatically be enforced for all viewers of the report, ensuring consistent data security and compliance. However, the behavior of data policies (e.g., masking) depends on who is the user of the Superset.