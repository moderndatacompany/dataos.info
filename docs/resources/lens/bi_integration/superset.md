
## Superset

## Pre-requisites

- **Curl**: Ensure you have `curl` installed on your system. For Windows users, you may need to use `curl.exe`. 
- **Lens API Endpoint**: The API endpoint provided by Lens to sync the data with meta endpoint access.
- **Access Credentials**: For Superset, you will need access credentials such as username, password, and host.

The following `curl` command is used to synchronize data from Lens to a Superset. It posts configuration details required for integration.

**Step 1: Run the curl command**

To sync your Lens model with Superset, execute the following curl command:

=== "Syntax"

    ```bash
    curl --location --request POST 'https://<DATAOS_FQDN>/lens2/sync/api/v1/superset/public:<LENS-NAME>' \
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
    curl --location --request POST 'https://liberal-donkey.dataos.app/lens2/sync/api/v1/superset/public:company-intelligence' \
    --header 'apikey: aueniekQa==' \
    --header 'Content-Type: application/json' \
    --data-raw '
    {
        "username": "adder_1",
        "password": "adder_1",
        "host": "https://superset-liberal-donkey.dataos.app""
    }
    ```

**Command Parameters:**

- **`URL`**: `https://liberal-donkey.dataos.app/lens2/sync/api/v1/superset/public:sales360` This is the endpoint for syncing with Superset.

- **`DataOS FQDN`: any current DataOS  FQDN. For example,** `liberal-donkey.dataos.app`

- **`--header 'Content-Type: application/json'`**: This specifies the content type as JSON.

- **`Lens_Name`: Your lens name. Example `sales360`.**

- **`API_Key`: Your DataOS API key in your `docker-compose.yaml`.**

Upon initiation, you will receive a response:

```bash
{
    "message": "started"
}
...
{
    "message": "Superset project creation and sync completed successfully."
}
```

Once you execute the command in the terminal, the results will be visible in the Superset app, as demonstrated below:

Please follow the steps outlined to see the result:

**Step 2 Go to DataOS**: Select Superset.

  <div style="text-align: center;">
      <img src="/resources/lens/bi_integration/superset2.png" alt="Superset Configuration" style="max-width: 80%; height: auto; border: 1px solid #000;">
  </div>

**Step 3 Navigate to Datasets Tab:** Here, each entity will be available in the form of datasets.

  <div style="text-align: center;">
      <img src="/resources/lens/bi_integration/superset3.png" alt="Superset Configuration" style="max-width: 80%; height: auto; border: 1px solid #000;">
  </div>

Everything is set up now. Explore and perform further analysis in Superset.