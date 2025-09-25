# Custom Destination

Nilus includes different [Supported Destination](/resources/stacks/nilus/supported_destinations/), but you can also push data to any target system by implementing a Custom Destination.

Custom destinations let you:

* Send data to APIs, webhooks, queues, or proprietary systems.
* Control batching, serialization, retries, and error handling.
* Convert Nilus runtime batches (e.g., PyArrow / row-like structures) into JSON or other formats.
* Run post-load hooks for notifications, metrics, or cleanup.

> Place your destination files in a repository and reference them directly in your Nilus workflow (`repo` block + `sink.address: custom://<ClassName>`). Nilus will sync and execute your code.

!!! warning
    **Dependency Management for Custom Destination**

    - Only include **new dependencies** required by the custom source or destination.
    - Do **not** add libraries that are already part of the existing environment.
    - This prevents duplication and avoids version conflicts.

    **Pre-Installed Packages:** See the [requirements.txt](/resources/stacks/nilus/requirments.txt), to know the installed packages or [Download](/resources/stacks/nilus/requirments.zip).   
    



## Key Components

1. **Destination Function (`@nilus.destination`)**

   Receives a batch (`items`) and table metadata (`table`), transforms it, and sends it to your system.

2. **Wrapper Class (`CustomDestination`)**

   Defines which function Nilus should call and how run parameters (dataset/table names) are passed.

3. **Serialization**

   Normalizes PyArrow mixed Python types into a safe format such as JSON.

4. **Configuration**

   Point `sink.address` at your custom class and set `dest-table` in `sink.options`.

## Base Class Pattern

A typical custom destination wrapper looks like this:

```python
from nilus import CustomDestination

class MyCustomDestination(CustomDestination):
    """Custom destination wiring for Nilus."""

    def nilus_dest(self, uri: str, **kwargs):
        """Return the destination function to run."""
        return my_destination_func

    def nilus_run_params(self, uri: str, table: str, **kwargs):
        """Return run parameters (dataset/table names)."""
        parts = table.split(".")
        if len(parts) == 2:
            return {"dataset_name": parts[0], "table_name": parts[1]}
        return {"dataset_name": "default", "table_name": table}

    def post_load(self) -> None:
        """Optional hook after a successful load."""
        pass
```

## Destination Function Pattern

The destination function **delivers batches** to your system:

```python
import nilus
from typing import Any, Dict, List
import datetime, decimal, uuid, json, requests

# JSON serialization helper
def json_serializer(obj):
    if isinstance(obj, (datetime.datetime, datetime.date, datetime.time)):
        return obj.isoformat()
    if isinstance(obj, datetime.timedelta):
        return str(obj)
    if isinstance(obj, decimal.Decimal):
        return float(obj)
    if isinstance(obj, uuid.UUID):
        return str(obj)
    if hasattr(obj, "as_py"):  # PyArrow scalar
        return obj.as_py()
    if hasattr(obj, "__dict__"):
        return obj.__dict__
    raise TypeError(f"Not JSON serializable: {type(obj)}")

# Convert Nilus batches to JSON-safe dicts
def convert_pyarrow_to_json(items) -> List[Dict[str, Any]]:
    if hasattr(items, "to_pylist"):          # PyArrow Table/RecordBatch
        return items.to_pylist()
    if isinstance(items, (list, tuple)):     # Iterable of rows
        out = []
        for row in items:
            if hasattr(row, "to_pydict"):
                out.append(row.to_pydict())
            elif isinstance(row, dict):
                norm = {}
                for k, v in row.items():
                    if hasattr(v, "as_py"):
                        v = v.as_py()
                    if isinstance(v, (datetime.datetime, datetime.date, datetime.time)):
                        v = v.isoformat()
                    elif isinstance(v, decimal.Decimal):
                        v = float(v)
                    elif isinstance(v, uuid.UUID):
                        v = str(v)
                    norm[k] = v
                out.append(norm)
            else:
                out.append(row)
        return out
    try:
        return list(items)
    except Exception:
        return []

# Example destination
@nilus.destination
def my_destination_func(items, table):
    table_name = table.get("name", "unknown")
    records = convert_pyarrow_to_json(items)
    if not records:
        return

    payload = {
        "table": table_name,
        "data": records,
        "metadata": {
            "count": len(records),
            "timestamp": datetime.datetime.now().isoformat(),
        },
    }

    body = json.dumps(payload, default=json_serializer)
    resp = requests.post(
        "https://your-api.example.com/ingest",
        data=body,
        headers={"Content-Type": "application/json"},
        timeout=30,
    )
    resp.raise_for_status()
```

## Example Implementations

Here's a streamlined guide to help you implement custom destination for user-defined connectors effectively.



**Step 1: Webhook Destination (simple batched POST)**

```python
@nilus.destination
def webhook_destination_func(items, table):
    table_name = table.get("name", "unknown")
    records = convert_pyarrow_to_json(items)
    if not records:
        return

    payload = {"table": table_name, "data": records, "timestamp": datetime.datetime.now().isoformat()}
    resp = requests.post(
        "https://webhook.site/your-endpoint",
        data=json.dumps(payload, default=json_serializer),
        headers={"Content-Type": "application/json"},
        timeout=30,
    )
    resp.raise_for_status()
    print(f"✅ Sent {len(records)} records to {table_name}")

class WebhookDestination(CustomDestination):
    def nilus_dest(self, uri: str, **kwargs):
        return webhook_destination_func
    def nilus_run_params(self, uri: str, table: str, **kwargs):
        return {"table_name": table}
    def post_load(self) -> None:
        pass
```



**Step 2: API Destination (with Nilus load metadata)**

```python
@nilus.destination
def api_destination_func(items, table):
    table_name = table.get("name", "unknown")
    records = convert_pyarrow_to_json(items)
    if not records:
        print(f"📭 No items to send for table {table_name}")
        return

    payload = {
        "table": table_name,
        "data": records,
        "schema": table.get("columns", {}),
        "metadata": {
            "load_id": records[0].get("_dlt_load_id") if records else None,
            "item_count": len(records),
            "data_type": "json_converted_from_pyarrow",
            "timestamp": datetime.datetime.now().isoformat(),
        },
    }

    body = json.dumps(payload, default=json_serializer)
    resp = requests.post(
        "http://0.0.0.0:7654/webhook",
        data=body,
        headers={"Content-Type": "application/json"},
        timeout=30,
    )
    resp.raise_for_status()
    print(f"✅ API destination sent {len(records)} items for {table_name}")

class ApiDestination(CustomDestination):
    def nilus_dest(self, uri: str, **kwargs):
        return api_destination_func
    def nilus_run_params(self, uri: str, table: str, **kwargs):
        parts = table.split(".")
        if len(parts) == 2:
            return {"dataset_name": parts[0], "table_name": parts[1]}
        return {"dataset_name": "default", "table_name": table}
    def post_load(self) -> None:
        pass
```





**Step 3: Local Test Webhook Server (optional helper)**

```python
# dummy_server.py
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import datetime

app = FastAPI(title="Test Webhook Server", version="1.0.0")
received_data = []

@app.post("/{path:path}")
async def catch_all_post(path: str, request: Request):
    try:
        body = await request.body()
        try:
            json_data = await request.json()
        except:
            json_data = None

        received_data.append({
            "timestamp": datetime.datetime.now().isoformat(),
            "path": f"/{path}",
            "headers": dict(request.headers),
            "body_size": len(body),
            "json_data": json_data,
        })
        return JSONResponse(status_code=200, content={"status": "success"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": "error", "message": str(e)})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7654)
```





## Deployment Configuration 

After creating the source files for your custom destination, deploy them using the Workflow as follows:

### **Repository Structure**

Custom destination must follow a standard Python package layout:

```bash
my-custom-destinations/
├── __init__.py
├── api_destination.py            # destination function + helpers
├── nilus_custom_destination.py   # CustomDestination wrapper
└── utils.py                      # optional shared helpers
```

### **Workflow Configuration**

To deploy the custom source, reference the repository in a Nilus Workflow:

```yaml
repo:
  url: "https://github.com/your-repo"
  syncFlags:
    - "--ref=main"
  baseDir: "examples/custom_destination"

source:
  address: postgresql://user:pass@localhost:5432/db
  options:
    source-table: "public.users"

sink:
  address: custom://ApiDestination   # must match class name
  options:
    dest-table: "processed.users"
    incremental-strategy: append
```

### **Data Processing Notes**

* `items` can be a PyArrow `Table`/`RecordBatch` or iterable of rows.
* `table` contains metadata (e.g., `name`, `columns`).
* Nilus load metadata fields (e.g., `_dlt_load_id`) may appear in rows.
* Use `convert_pyarrow_to_json` and `json_serializer` for safe type conversion.

## Best Practices

1. **Error Handling**
     1. Raise errors for HTTP/driver issues and implement retry/backoff mechanisms for transient failures.
     2. Log response codes and handle partial failures appropriately.
     3. Ensure protection against processing empty batches.
2. **Batching & Throughput**
     1. Break down large payloads into smaller chunks (e.g., 500-5,000 records per request).
     2. Reuse HTTP sessions or SDK clients.
     3. Follow the downstream rate limits.
3. **Serialization**
     1. Normalize timestamps to ISO-8601 format.
     2. Convert decimal values to strings or floats according to your target schema.
     3. Ensure keys and values are sanitized to meet API requirements.
4. **Security**
     1. Store secrets in environment variables or instance secrets; avoid hardcoding.
     2. Utilize HTTPS/TLS for all network communications.
     3. Refrain from logging sensitive information.
5. **Observability**
     1. Track the number of records sent, number of batches processed, and retry attempts.
     2. Monitor latency and error rates.
     3. Include correlation IDs (load_id, table_name) for tracing purposes.

### **Quick Checklist**

Ensure you verify the following when creating a custom destination:

* Destination function created with `@nilus.destination`.
* `CustomDestination` subclass implemented.
* Workflow uses `sink.address: custom://<ClassName>`.
* Secrets configured via environment / Instance Secrets.
* (Optional) Local webhook server tested.

