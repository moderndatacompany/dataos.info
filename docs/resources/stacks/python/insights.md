# Retrieve insights from the Semantic Model
This section provides the steps to retrieve insights from the Semantic Model using Python as a Stack.

## Prerequisites

Ensure you have met the requirements listed [in this section.](/resources/stacks/python/#pre-requisites) 

## Step 1. Create/Select a Repository

Create or select any repository in GitHub or Bitbucket where the Python code will be added.

## Step 2. Create base directory

Inside that repository, add a folder named `app`, which will include the Python scripts with the `.py` extension, a requirements file with a `.txt` extension, and `.streamlit` folder with `config.toml` file, which will include Streamlit-specific configurations.

```sql
python-stack/
└── app/                       # baseDir (referenced in service manifest)
    ├── main.py                # main code (required)
    └── requirements.txt       # Dependencies (required)
```

## Step 3. Add the Python code and dependencies

In the files with the `.py` extension, add the Python script, and in the `requirements.txt` file, add the requirements to run the Python scripts as given below.

<aside class="callout">
💡 The <code>${{...}}</code> syntax in the URL and other fields in the code represents placeholders that must be replaced with your actual values (such as your DataOS FQDN, workspace, or lens name). These are not environment variables and will not be automatically substituted.
</aside>

<details>
    <summary>main.py</summary>
    
    ```python
    import requests
    import json
    
    # API endpoint
    url = "https://${{dataos-fqdn}}/lens2/api/${{workspace}}:${{lens-name}}$/v2/load"
    
    # Replace with your actual API key
    api_key = "<api key here>"
    
    # Headers
    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
    }
    
    # Payload
    payload = {
    "query": {
    "measures": [
    "customers.average_customer_income",
    "customers.count"
    ],
    "dimensions": [
    "customers.customer_key"
    ],
    "segments": [],
    "filters": [],
    "timeDimensions": [],
    "limit": 10,
    "offset": 0,
    "order": []
    }
    }
    
    # Make POST request
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    
    # Handle response
    if response.status_code == 200:
    data = response.json()
    
    # Assuming API returns a "data" array with dimension + measure keys
    rows = data.get("data", [])
    
    if rows:
    print(f"{'Customer Key':<20} {'Avg Income':<20} {'Count':<10}")
    print("-" * 50)
    for row in rows:
    customer_key = row.get("customers.customer_key")
    avg_income = row.get("customers.average_customer_income")
    count = row.get("customers.count")
    
    print(f"{customer_key:<20} {avg_income:<20} {count:<10}")
    else:
    print("No data returned.")
    else:
    print("Error:", response.status_code, response.text)
    ```
</details>
   
**requirements.txt**
    
```bash
requests
```
  
    

The above script retrieves customer-related analytical data from the `sports-data-27` Lens (semantic model). It queries the `customers` entity to fetch two key measures: the average customer income (`customers.average_customer_income`) and the total number of customers (`customers.count`), grouped by the customer key (`customers.customer_key`). The API call limits the results to 10 records, returning aggregated insights that can be used to analyze income distribution and customer volume across unique customer identifiers

## Step 4. Push the changes

Once the repository and the code are ready to be deployed, push the changes by executing the commands below.

```bash
git add .
git commit -m "Retrieving insights from semantic model"
git push -u origin main
```

## Step 5. Secure repository credentials within DataOS

If the app code is in a private Git repository, credentials must be secured in DataOS using secrets. These secrets are referred to during repository sync:

- **GitHub:** Create a Personal Access Token (PAT), then store it in DataOS as a secret. [Guide](/resources/instance_secret/repositories/git/) | [GitHub PAT docs](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic)
- **Bitbucket:** Generate an App Password (API token) with repo permissions, then store it in DataOS as a secret. [Guide](/resources/instance_secret/repositories/bitbucket/) | [Bitbucket docs](https://support.atlassian.com/bitbucket-cloud/docs/create-an-api-token/)

## Step 6. Create a Python Service manifest file

Create a Service Resource manifest file using the template given below by replacing the given values with the actual values.

```yaml
name: python-service
version: v1
type: service
tags:
  - service
  - python-stack
  - dataos:type:resource
  - dataos:resource:service
  - dataos:layer:user
  - dataos:workspace:public
description: Python Service Sample
owner: iamgroot
workspace: public
service:
  servicePort: 8050
  ingress:
    enabled: true
    path: /test_sample
    noAuthentication: true
  replicas: 1
  stack: python3:1.0
  logLevel: INFO
  dataosSecrets:
    - name: bitbucket-cred
      allKeys: true
      consumptionType: envVars
  compute: runnable-default
  resources:
    requests:
      cpu: 1000m
      memory: 1536Mi
  stackSpec:
    repo:
      baseDir: queries/pyservice
      syncFlags:
        - '--ref=main'
      url: https://bitbucket.org/queries/
```

## Step 7. Apply the Service manifest file

Apply the Service manifest file by executing the command below.

```bash
dataos-ctl resource apply -f ${{path-to-manifest-file}}
```

## Step 8. Verify the Service

Validate the Service by executing the command below.

```bash
dataos-ctl resource get -t service -n ${{service-identifier}} -w ${{workspace}}
```

**Example:**

```bash
dataos-ctl resource get -t service -w public -n my-python-app-test
# Expected output:
INFO[0000] 🔍 get...                                     
INFO[0001] 🔍 get...complete                             

         NAME        | VERSION |  TYPE   | WORKSPACE | STATUS |  RUNTIME  |    OWNER     
---------------------|---------|---------|-----------|--------|-----------|--------------
  my-python-app-test | v1      | service | public    | active | running:1 | iamgroot  

```

## Step 9. Validate the code execution

To validate if the Python script executed without any errors, run the following command.

```bash
dataos-ctl resource log -t service -w public -n ${{service-identifier}}
```

**Example Output:**
    
```bash
/etc/dataos/work
Collecting requests (from -r requirements.txt (line 1))
    Downloading requests-2.32.5-py3-none-any.whl.metadata (4.9 kB)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 434.2/434.2 MB 123.3 MB/s eta 0:00:00
    Installing build dependencies: started
    Installing buila93ea872cc3393d8bbe9ad30bc3fc3b363735ef54988973
Installing collected packages: pytz, py4j, watchdog, urllib3, tzdata, typing-extensions, tornado, toml, tenacity, smmap, six, rpds-py, pyspark, pyarrow, protobuf, pillow, packaging, numpy, narwhals, MarkupSafe, idna, click, charset_normalizer, certifi, cachetools, blinker, attrs, requests, referencing, python-dateutil, jinja2, gitdb, pyflare, pydeck, pandas, jsonschema-specifications, gitpython, jsonschema, altair, streamlit
Successfully installed MarkupSafe-3.0.2 altair-5.5.0 attrs-25.3.0 blinker-1.9.0 cachetools-5.5.2 certifi-2025.8.3 charset_normalizer-3.4.3 click-8.2.1 gitdb-4.0.12 gitpython-3.1.45 idna-3.10 jinja2-3.1.6 jsonschema-4.25.1 jsonschema-specifications-2025.9.1 narwhals-2.5.0 numpy-2.3.3 packaging-24.2 pandas-2.2.2 pillow-11.3.0 protobuf-6.32.1 py4j-0.10.9.9 pyarrow-21.0.0 pydeck-0.9.1 pyflare-1.1.5 pyspark-4.0.1 python-dateutil-2.9.0.post0 pytz-2025.2 referencing-0.36.2 requests-2.32.5 rpds-py-0.27.1 six-1.17.0 smmap-5.0.2 streamlit-1.45.0 tenacity-9.1.2 toml-0.10.2 tornado-6.5.2 typing-extensions-4.15.0 tzdata-2025.2 urllib3-2.5.0 watchdog-6.0.0
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager, possibly rendering your system unusable. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv. Use the --root-user-action option if you know what you are doing and want to suppress this warning.

[notice] A new release of pip is available: 25.0.1 -> 25.2
[notice] To update, run: pip install --upgrade pip
Customer Key         Avg Income           Count     
--------------------------------------------------
11599                20000                1         
11505                60000                1         
11508                60000                1         
11785                40000                1         
11041                60000                1         
11484                40000                1         
11082                130000               1         
11293                60000                1         
11257                120000               1         
11249                130000               1         

```

