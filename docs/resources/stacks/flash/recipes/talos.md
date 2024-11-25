# How to consume cached datasets via Talos APIs?

To expose cached datasets as Data APIs via [Talos APIs](/resources/stacks/talos/), follow these steps to configure Flash as the data source for your Talos API.

## Prerequisites

Before proceeding, ensure the following are set up:

- [Flash service is set up](/resources/stacks/flash/flash_service/).
- Docker is installed and initialized.

## Steps

### **1. Create a repository and configuration file**

Create a new repository, open it in a code editor (e.g., VS Code), and create a `config.yaml` file with the following configuration. Update the `name`, `description`, `version`, `DataOS context`, `Flash` source type, and the source `Flash` service name.

```yaml
name: flash
description: A talos-flash app
version: 0.1.6
auth:
  heimdallUrl: https://liberal-donkey.dataos.app/heimdall
logLevel: 'DEBUG'
sources:
  - name: flash  # Source name
    type: flash  # Source type (Flash)
    flashName: 'public:flash-service'  # Name of the Flash service
```

### **2. Create a docker compose file**

In the same repository, create a `docker-compose.yaml` file. Update the `volumes` path `/home/iamgroot/Desktop/talos-examples/lens` with your repository's actual path. Also, replace `DATAOS_RUN_AS_USER` with your DataOS username and `DATAOS_RUN_AS_APIKEY` with your DataOS API key.

```yaml
version: "2.2"
services:
  talos:
    image: rubiklabs/talos:0.1.6
    ports:
      - "3000:3000"
    volumes:
      - .:/etc/dataos/work  # Update with your repository path
    environment:
      DATAOS_RUN_AS_USER: ${{iamgroot}}  # Replace with your DataOS username
      DATAOS_RUN_AS_APIKEY: ${{Dyiuyuidy98837686bbdhkjhugIPOPHGgGHTIOnsd68FH=}}  # Replace with your DataOS API key
      DATAOS_FQDN: liberal-donkey.dataos.app  # DataOS environment URL
    tty: true
```

### **3. Create API definition and SQL files**

Create a folder named `apis` in your repository. Inside the `apis` folder, create two files:
- `customer.sql`: This file will contain the SQL query to retrieve data from the cached dataset.
- `customer.yaml`: This file defines the API endpoint and the source of the data.

**`customer.sql`**

```sql
SELECT * FROM mycustomer LIMIT 20;
```

**`customer.yaml`**

```yaml
urlPath: /flash/customers  # API endpoint to access cached data
description: List customers from the customer table
source: flash  # Data source
```

### **4. Apply the Talos Service**

To deploy and apply the Talos Service, follow the steps provided [here](/resources/stacks/talos/set_up/#steps).

This will expose the cached dataset from Flash as a Talos API, allowing clients to query the data through the API endpoint.