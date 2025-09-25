# Vizro Implementation

This section provides the steps to implement the Vizro framework to build a dashboard using the Python Stack. 

<div style="text-align: center;">
    <figure>
    <img src="/resources/stacks/python/vizro.png" 
        alt="Vizro Dashboard" 
        style="border: 1px solid black; width: 80%; height: auto; display: block; margin: auto;">
    <figcaption style="margin-top: 8px; font-style: italic;">Vizro Dashboard</figcaption>
    </figure>
</div>

## Prerequisites

Before starting to implement the Vi framework using Python Stack, ensure you have met the requirements listed [in this section.](/resources/stacks/python/#pre-requisites) 

## Step 1. Create/Select a Repository

Create or select any repository in GitHub or Bitbucket where the Python code will be added.

## Step 2. Create base directory

Inside that repository, add a folder named `app`, which will include the Python script with the `.py` extension and a requirements file with a `.txt` extension.

```sql
python-stack/
└── app/                        # baseDir (referenced in service/stack manifest)
    ├── main.py                 # Application entry point (required)
    └── requirements.txt        # Dependencies (required)
```

## Step 3. Add the Python code and dependencies

In the file with the `.py` extension, add your Python script, and in the `requirements.txt` file, add the requirements to run the Python script as given in the example below.

**Example:**

<details>
    <summary>main.py</summary>
    
    ```python
    import vizro.plotly.express as px
    from vizro import Vizro
    import vizro.models as vm
    
    df = px.data.iris()
    
    page = vm.Page(
        title="My first dashboard",
        components=[
            vm.Graph(figure=px.scatter(df, x="sepal_length", y="petal_width", color="species")),
            vm.Graph(figure=px.histogram(df, x="sepal_width", color="species")),
        ],
        controls=[
            vm.Filter(column="species"),
        ],
    )
    
    dashboard = vm.Dashboard(pages=[page])
    # Configure Vizro with the custom URL base pathname
    app = Vizro(url_base_pathname="/test_sample/").build(dashboard)
    
    if __name__ == "__main__":
        app.run(port=8050, host="0.0.0.0")
    ```
</details>  
    
**requirements.txt**
    
```bash
vizro
plotly
pandas
```
    

## Step 4. Push the changes

Once the repository and the code are ready to be deployed, push the changes by executing the commands below.

```bash
git add .
git commit -m "chore: provision repo with baseDir, script, and requirements file"
git push -u origin main
```

## Step 5. Secure repository credentials within DataOS

If the app code is in a private Git repository, credentials must be secured in DataOS using secrets. These secrets are referred to during repository sync:

- **GitHub:** Create a Personal Access Token (PAT), then store it in DataOS as a secret. [Guide](/resources/instance_secret/repositories/git/) | [GitHub PAT docs](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic)
- **Bitbucket:** Generate an App Password (API token) with repo permissions, then store it in DataOS as a secret. [Guide](/resources/instance_secret/repositories/bitbucket/) | [Bitbucket docs](https://support.atlassian.com/bitbucket-cloud/docs/create-an-api-token/)

## Step 6. Create a Python Service manifest file

Create a Service Resource manifest file using the template given below by replacing the placeholders with the actual values.

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
      baseDir: python-stack/app/
      syncFlags:
        - '--ref=main'
      url: https://bitbucket.org/python-stack/
```

## Step 7. Apply the Service manifest file

Apply the Service manifest file by executing the command below.

```yaml
dataos-ctl resource apply -f ${{path-to-manifest-file}}
```

## Step 8. Verify the Service

Validate the Service by executing the command below.

```yaml
dataos-ctl resource get -t service -n ${{service-identifier}} -w ${{workspace}}
```

**Example:**

```yaml
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

??? note "Example"
    
    ```bash
    dataos-ctl resource log -t service -w public -n python-vizro           
    
    # Expected Output
    
    INFO[0000] 📃 log(public)...                             
    INFO[0001] 📃 log(public)...complete                     
    
                   NODE NAME               │     CONTAINER NAME     │ ERROR  
    ───────────────────────────────────────┼────────────────────────┼────────
      python-vizro-jvii-d-596c66f9dc-smfxd │ python-vizro-jvii-main │        
    
    -------------------LOGS-------------------
    /etc/dataos/work
    Collecting vizro (from -r requirements.txt (line 1))
      Downloading vizro-0.1.44-py3-none-any.whl.metadata (12 kB)
    Collecting plotly (from -r requirements.txt (line 2))
      Downloading plotly-6.3.0-py3-none-any.whl.metadata (8.5 kB)
    Collecting pandas (from -r requirements.txt (line 3))
      Downloading pandas-2.3.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (91 kB)
    Collecting autoflake (from vizro->-r requirements.txt (line 1))
      Downloading autoflake-2.3.1-py3-none-any.whl.metadata (7.6 kB)
    Collecting black (from vizro->-r requirements.txt (line 1))
      Downloading black-25.1.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.manylinux_2_28_x86_64.whl.metadata (81 kB)
    Collecting dash-ag-grid>=31.3.1 (from vizro->-r requirements.txt (line 1))
      Downloading dash_ag_grid-32.3.1-py3-none-any.whl.metadata (5.7 kB)
    Collecting dash-bootstrap-components>=2 (from vizro->-r requirements.txt (line 1))
      Downloading dash_bootstrap_components-2.0.4-py3-none-any.whl.metadata (18 kB)
    Collecting dash-mantine-components>=1 (from vizro->-r requirements.txt (line 1))
      Downloading dash_mantine_components-2.2.1-py3-none-any.whl.metadata (4.6 kB)
    Collecting dash>=3.1.1 (from vizro->-r requirements.txt (line 1))
      Downloading dash-3.2.0-py3-none-any.whl.metadata (10 kB)
    Collecting flask-caching>=2 (from vizro->-r requirements.txt (line 1))
      Downloading Flask_Caching-2.3.1-py3-none-any.whl.metadata (2.2 kB)
    Collecting packaging (from vizro->-r requirements.txt (line 1))
      Downloading packaging-25.0-py3-none-any.whl.metadata (3.3 kB)
    Collecting pydantic>=2.7.0 (from vizro->-r requirements.txt (line 1))
      Downloading pydantic-2.11.7-py3-none-any.whl.metadata (67 kB)
    Collecting wrapt>=1 (from vizro->-r requirements.txt (line 1))
      Downloading wrapt-1.17.3-cp312-cp312-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl.metadata (6.4 kB)
    Collecting narwhals>=1.15.1 (from plotly->-r requirements.txt (line 2))
      Downloading narwhals-2.4.0-py3-none-any.whl.metadata (11 kB)
    Collecting numpy>=1.26.0 (from pandas->-r requirements.txt (line 3))
      Downloading numpy-2.3.3-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (62 kB)
    Collecting python-dateutil>=2.8.2 (from pandas->-r requirements.txt (line 3))
      Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
    Collecting pytz>=2020.1 (from pandas->-r requirements.txt (line 3))
      Downloading pytz-2025.2-py2.py3-none-any.whl.metadata (22 kB)
    Collecting tzdata>=2022.7 (from pandas->-r requirements.txt (line 3))
      Downloading tzdata-2025.2-py2.py3-none-any.whl.metadata (1.4 kB)
    Collecting Flask<3.2,>=1.0.4 (from dash>=3.1.1->vizro->-r requirements.txt (line 1))
      Downloading flask-3.1.2-py3-none-any.whl.metadata (3.2 kB)
    Collecting Werkzeug<3.2 (from dash>=3.1.1->vizro->-r requirements.txt (line 1))
      Downloading werkzeug-3.1.3-py3-none-any.whl.metadata (3.7 kB)
    Collecting importlib-metadata (from dash>=3.1.1->vizro->-r requirements.txt (line 1))
      Downloading importlib_metadata-8.7.0-py3-none-any.whl.metadata (4.8 kB)
    Collecting typing-extensions>=4.1.1 (from dash>=3.1.1->vizro->-r requirements.txt (line 1))
      Downloading typing_extensions-4.15.0-py3-none-any.whl.metadata (3.3 kB)
    Collecting requests (from dash>=3.1.1->vizro->-r requirements.txt (line 1))
      Downloading requests-2.32.5-py3-none-any.whl.metadata (4.9 kB)
    Collecting retrying (from dash>=3.1.1->vizro->-r requirements.txt (line 1))
      Downloading retrying-1.4.2-py3-none-any.whl.metadata (5.5 kB)
    Collecting nest-asyncio (from dash>=3.1.1->vizro->-r requirements.txt (line 1))
      Downloading nest_asyncio-1.6.0-py3-none-any.whl.metadata (2.8 kB)
    Collecting setuptools (from dash>=3.1.1->vizro->-r requirements.txt (line 1))
      Downloading setuptools-80.9.0-py3-none-any.whl.metadata (6.6 kB)
    Collecting cachelib>=0.9.0 (from flask-caching>=2->vizro->-r requirements.txt (line 1))
      Downloading cachelib-0.13.0-py3-none-any.whl.metadata (2.0 kB)
    Collecting annotated-types>=0.6.0 (from pydantic>=2.7.0->vizro->-r requirements.txt (line 1))
      Downloading annotated_types-0.7.0-py3-none-any.whl.metadata (15 kB)
    Collecting pydantic-core==2.33.2 (from pydantic>=2.7.0->vizro->-r requirements.txt (line 1))
      Downloading pydantic_core-2.33.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (6.8 kB)
    Collecting typing-inspection>=0.4.0 (from pydantic>=2.7.0->vizro->-r requirements.txt (line 1))
      Downloading typing_inspection-0.4.1-py3-none-any.whl.metadata (2.6 kB)
    Collecting six>=1.5 (from python-dateutil>=2.8.2->pandas->-r requirements.txt (line 3))
      Downloading six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
    Collecting pyflakes>=3.0.0 (from autoflake->vizro->-r requirements.txt (line 1))
      Downloading pyflakes-3.4.0-py2.py3-none-any.whl.metadata (3.5 kB)
    Collecting click>=8.0.0 (from black->vizro->-r requirements.txt (line 1))
      Downloading click-8.2.1-py3-none-any.whl.metadata (2.5 kB)
    Collecting mypy-extensions>=0.4.3 (from black->vizro->-r requirements.txt (line 1))
      Downloading mypy_extensions-1.1.0-py3-none-any.whl.metadata (1.1 kB)
    Collecting pathspec>=0.9.0 (from black->vizro->-r requirements.txt (line 1))
      Downloading pathspec-0.12.1-py3-none-any.whl.metadata (21 kB)
    Collecting platformdirs>=2 (from black->vizro->-r requirements.txt (line 1))
      Downloading platformdirs-4.4.0-py3-none-any.whl.metadata (12 kB)
    Collecting blinker>=1.9.0 (from Flask<3.2,>=1.0.4->dash>=3.1.1->vizro->-r requirements.txt (line 1))
      Downloading blinker-1.9.0-py3-none-any.whl.metadata (1.6 kB)
    Collecting itsdangerous>=2.2.0 (from Flask<3.2,>=1.0.4->dash>=3.1.1->vizro->-r requirements.txt (line 1))
      Downloading itsdangerous-2.2.0-py3-none-any.whl.metadata (1.9 kB)
    Collecting jinja2>=3.1.2 (from Flask<3.2,>=1.0.4->dash>=3.1.1->vizro->-r requirements.txt (line 1))
      Downloading jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
    Collecting markupsafe>=2.1.1 (from Flask<3.2,>=1.0.4->dash>=3.1.1->vizro->-r requirements.txt (line 1))
      Downloading MarkupSafe-3.0.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.0 kB)
    Collecting zipp>=3.20 (from importlib-metadata->dash>=3.1.1->vizro->-r requirements.txt (line 1))
      Downloading zipp-3.23.0-py3-none-any.whl.metadata (3.6 kB)
    Collecting charset_normalizer<4,>=2 (from requests->dash>=3.1.1->vizro->-r requirements.txt (line 1))
      Downloading charset_normalizer-3.4.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (36 kB)
    Collecting idna<4,>=2.5 (from requests->dash>=3.1.1->vizro->-r requirements.txt (line 1))
      Downloading idna-3.10-py3-none-any.whl.metadata (10 kB)
    Collecting urllib3<3,>=1.21.1 (from requests->dash>=3.1.1->vizro->-r requirements.txt (line 1))
      Downloading urllib3-2.5.0-py3-none-any.whl.metadata (6.5 kB)
    Collecting certifi>=2017.4.17 (from requests->dash>=3.1.1->vizro->-r requirements.txt (line 1))
      Downloading certifi-2025.8.3-py3-none-any.whl.metadata (2.4 kB)
    Downloading vizro-0.1.44-py3-none-any.whl (928 kB)
       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 928.2/928.2 kB 22.0 MB/s eta 0:00:00
    Downloading plotly-6.3.0-py3-none-any.whl (9.8 MB)
       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 9.8/9.8 MB 117.2 MB/s eta 0:00:00
    Downloading pandas-2.3.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (12.0 MB)
       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 12.0/12.0 MB 157.7 MB/s eta 0:00:00
    Downloading dash-3.2.0-py3-none-any.whl (7.9 MB)
       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.9/7.9 MB 41.1 MB/s eta 0:00:00
    Downloading dash_ag_grid-32.3.1-py3-none-any.whl (4.0 MB)
       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.0/4.0 MB 159.3 MB/s eta 0:00:00
    Downloading dash_bootstrap_components-2.0.4-py3-none-any.whl (204 kB)
    Downloading dash_mantine_components-2.2.1-py3-none-any.whl (1.3 MB)
       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.3/1.3 MB 20.7 MB/s eta 0:00:00
    Downloading Flask_Caching-2.3.1-py3-none-any.whl (28 kB)
    Downloading narwhals-2.4.0-py3-none-any.whl (406 kB)
    Downloading numpy-2.3.3-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (16.6 MB)
       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 16.6/16.6 MB 132.8 MB/s eta 0:00:00
    Downloading pydantic-2.11.7-py3-none-any.whl (444 kB)
    Downloading pydantic_core-2.33.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.0 MB)
       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.0/2.0 MB 250.9 MB/s eta 0:00:00
    Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
    Downloading pytz-2025.2-py2.py3-none-any.whl (509 kB)
    Downloading tzdata-2025.2-py2.py3-none-any.whl (347 kB)
    Downloading wrapt-1.17.3-cp312-cp312-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl (88 kB)
    Downloading autoflake-2.3.1-py3-none-any.whl (32 kB)
    Downloading black-25.1.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.manylinux_2_28_x86_64.whl (1.8 MB)
       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.8/1.8 MB 479.8 MB/s eta 0:00:00
    Downloading packaging-25.0-py3-none-any.whl (66 kB)
    Downloading annotated_types-0.7.0-py3-none-any.whl (13 kB)
    Downloading cachelib-0.13.0-py3-none-any.whl (20 kB)
    Downloading click-8.2.1-py3-none-any.whl (102 kB)
    Downloading flask-3.1.2-py3-none-any.whl (103 kB)
    Downloading mypy_extensions-1.1.0-py3-none-any.whl (5.0 kB)
    Downloading pathspec-0.12.1-py3-none-any.whl (31 kB)
    Downloading platformdirs-4.4.0-py3-none-any.whl (18 kB)
    Downloading pyflakes-3.4.0-py2.py3-none-any.whl (63 kB)
    Downloading six-1.17.0-py2.py3-none-any.whl (11 kB)
    Downloading typing_extensions-4.15.0-py3-none-any.whl (44 kB)
    Downloading typing_inspection-0.4.1-py3-none-any.whl (14 kB)
    Downloading werkzeug-3.1.3-py3-none-any.whl (224 kB)
    Downloading importlib_metadata-8.7.0-py3-none-any.whl (27 kB)
    Downloading nest_asyncio-1.6.0-py3-none-any.whl (5.2 kB)
    Downloading requests-2.32.5-py3-none-any.whl (64 kB)
    Downloading retrying-1.4.2-py3-none-any.whl (10 kB)
    Downloading setuptools-80.9.0-py3-none-any.whl (1.2 MB)
       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 483.2 MB/s eta 0:00:00
    Downloading blinker-1.9.0-py3-none-any.whl (8.5 kB)
    Downloading certifi-2025.8.3-py3-none-any.whl (161 kB)
    Downloading charset_normalizer-3.4.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (151 kB)
    Downloading idna-3.10-py3-none-any.whl (70 kB)
    Downloading itsdangerous-2.2.0-py3-none-any.whl (16 kB)
    Downloading jinja2-3.1.6-py3-none-any.whl (134 kB)
    Downloading MarkupSafe-3.0.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (23 kB)
    Downloading urllib3-2.5.0-py3-none-any.whl (129 kB)
    Downloading zipp-3.23.0-py3-none-any.whl (10 kB)
    Installing collected packages: pytz, zipp, wrapt, urllib3, tzdata, typing-extensions, six, setuptools, retrying, pyflakes, platformdirs, pathspec, packaging, numpy, nest-asyncio, narwhals, mypy-extensions, markupsafe, itsdangerous, idna, click, charset_normalizer, certifi, cachelib, blinker, annotated-types, Werkzeug, typing-inspection, requests, python-dateutil, pydantic-core, plotly, jinja2, importlib-metadata, black, autoflake, pydantic, pandas, Flask, flask-caching, dash, dash-mantine-components, dash-bootstrap-components, dash-ag-grid, vizro
    Successfully installed Flask-3.1.2 Werkzeug-3.1.3 annotated-types-0.7.0 autoflake-2.3.1 black-25.1.0 blinker-1.9.0 cachelib-0.13.0 certifi-2025.8.3 charset_normalizer-3.4.3 click-8.2.1 dash-3.2.0 dash-ag-grid-32.3.1 dash-bootstrap-components-2.0.4 dash-mantine-components-2.2.1 flask-caching-2.3.1 idna-3.10 importlib-metadata-8.7.0 itsdangerous-2.2.0 jinja2-3.1.6 markupsafe-3.0.2 mypy-extensions-1.1.0 narwhals-2.4.0 nest-asyncio-1.6.0 numpy-2.3.3 packaging-25.0 pandas-2.3.2 pathspec-0.12.1 platformdirs-4.4.0 plotly-6.3.0 pydantic-2.11.7 pydantic-core-2.33.2 pyflakes-3.4.0 python-dateutil-2.9.0.post0 pytz-2025.2 requests-2.32.5 retrying-1.4.2 setuptools-80.9.0 six-1.17.0 typing-extensions-4.15.0 typing-inspection-0.4.1 tzdata-2025.2 urllib3-2.5.0 vizro-0.1.44 wrapt-1.17.3 zipp-3.23.0
    WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager, possibly rendering your system unusable. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv. Use the --root-user-action option if you know what you are doing and want to suppress this warning.
    
    [notice] A new release of pip is available: 25.0.1 -> 25.2
    [notice] To update, run: pip install --upgrade pip
    INFO:dash.dash:Dash is running on http://0.0.0.0:8050/test_sample/
    
    Dash is running on http://0.0.0.0:8050/test_sample/
    
     * Serving Flask app 'main'
     * Debug mode: off
    INFO:werkzeug:WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
     * Running on all addresses (0.0.0.0)
     * Running on http://127.0.0.1:8050
     * Running on http://10.213.9.205:8050
    INFO:werkzeug:Press CTRL+C to quit
    INFO:werkzeug:10.213.1.236 - - [11/Sep/2025 09:09:19] "GET /test_sample/ HTTP/1.1" 200 -
    INFO:werkzeug:10.213.1.236 - - [11/Sep/2025 09:09:19] "GET /test_sample/_dash-component-suites/vizro/static/css/datepicker.v0_1_44m1757581727.css HTTP/1.1" 200 -
    INFO:werkzeug:10.213.1.236 - - [11/Sep/2025 09:09:19] "GET /test_sample/_dash-component-suites/vizro/static/css/dropdown.v0_1_44m1757581727.css HTTP/1.1" 200 -
    INFO:werkzeug:10.213.1.236 - - [11/Sep/2025 09:09:19] "GET /test_sample/_dash-component-suites/vizro/static/css/container.v0_1_44m1757581727.css HTTP/1.1" 200 -
    INFO:werkzeug:10.213.1.236 - - [11/Sep/2025 09:09:19] "GET /test_sample/_dash-component-suites/vizro/static/css/aggrid.v0_1_44m1757581727.css HTTP/1.1" 200 -
    INFO:werkzeug:10.213.1.236 - - [11/Sep/2025 09:09:19] "GET /test_sample/_dash-component-suites/vizro/static/css/vizro-bootstrap.v0_1_44m1757581727.min.css HTTP/1.1" 200 -
    INFO:werkzeug:10.213.1.236 - - [11/Sep/2025 09:09:19] "GET /test_sample/_dash-component-suites/vizro/static/css/figures.v0_1_44m1757581727.css HTTP/1.1" 200 -
    INFO:werkzeug:10.213.1.236 - - [11/Sep/2025 09:09:19] "GET /test_sample/_dash-component-suites/vizro/static/css/code.v0_1_44m1757581727.css HTTP/1.1" 200 -
    INFO:werkzeug:10.213.1.236 - - [11/Sep/2025 09:09:19] "GET /test_sample/_dash-component-suites/vizro/static/css/flex-grid.v0_1_44m1757581727.css HTTP/1.1" 200 -
    INFO:werkzeug:10.213.1.236 - - [11/Sep/2025 09:09:19] "GET /test_sample/_dash-component-suites/vizro/static/css/index.v0_1_44m1757581727.css HTTP/1.1" 200 -
    INFO:werkzeug:10.213.1.236 - - [11/Sep/2025 09:09:19] "GET /test_sample/_dash-component-suites/vizro/static/css/tabs.v0_1_44m1757581727.css HTTP/1.1" 200 -
    INFO:werkzeug:10.213.1.236 - - [11/Sep/2025 09:09:19] "GET /test_sample/_dash-component-suites/vizro/static/css/slider.v0_1_44m1757581727.css HTTP/1.1" 200 -
    INFO:werkzeug:10.213.1.236 - - [11/Sep/2025 09:09:19] "GET /test_sample/_dash-component-suites/vizro/static/css/layout.v0_1_44m1757581727.css HTTP/1.1" 200 -
    INFO:werkzeug:10.213.1.236 - - [11/Sep/2025 09:09:19] "GET /test_sample/_dash-component-suites/vizro/static/css/scroll_bar.v0_1_44m1757581727.css HTTP/1.1" 200 -
    INFO:werkzeug:10.213.1.236 - - [11/Sep/2025 09:09:19] "GET /test_sample/_dash-component-suites/vizro/static/css/tooltip.v0_1_44m1757581727.css HTTP/1.1" 200 -
    INFO:werkzeug:10.213.1.236 - - [11/Sep/2025 09:09:19] "GET /test_sample/_dash-component-suites/vizro/static/css/tiles.v0_1_44m1757581727.css HTTP/1.1" 200 -
    INFO:werkzeug:10.213.1.236 - - [11/Sep/2025 09:09:19] "GET /test_sample/_dash-component-suites/vizro/static/css/table.v0_1_44m1757581727.css HTTP/1.1" 200 -
    INFO:werkzeug:10.213.1.236 - - [11/Sep/2025 09:09:19] "GET /test_sample/_dash-component-suites/vizro/static/css/mantine_dates.v0_1_44m1757581727.css HTTP/1.1" 200 -
    INFO:werkzeug:10.213.1.236 - - [11/Sep/2025 09:09:19] "GET /test_sample/_dash-component-suites/dash/deps/react-dom@18.v3_2_0m1757581726.3.1.min.js HTTP/1.1" 200 -
    INFO:werkzeug:10.213.1.236 - - [11/Sep/2025 09:09:19] "GET /test_sample/_dash-component-suites/vizro/static/css/vizro_overwrites.v0_1_44m1757581727.css HTTP/1.1" 200 -
    INFO:werkzeug:10.213.1.236 - - [11/Sep/2025 09:09:19] "GET /test_sample/_dash-component-suites/dash/deps/polyfill@7.v3_2_0m1757581726.12.1.min.js HTTP/1.1" 200 -
    INFO:werkzeug:10.213.1.236 - - [11/Sep/2025 09:09:19] "GET /test_sample/_dash-component-suites/dash/deps/react@18.v3_2_0m1757581726.3.1.min.js HTTP/1.1" 200 -
    INFO:werkzeug:10.213.1.236 - - [11/Sep/2025 09:09:19] "GET /test_sample/_dash-component-suites/dash_bootstrap_components/_components/dash_bootstrap_components.v2_0_4m1757581727.min.js HTTP/1.1" 200 -
    INFO:werkzeug:10.213.1.236 - - [11/Sep/2025 09:09:19] "GET /test_sample/_dash-component-suites/vizro/static/js/actions/build_action_loop_callbacks.v0_1_44m1757581727.js HTTP/1.1" 200 -
    INFO:werkzeug:10.213.1.236 - - [11/Sep/2025 09:09:19] "GET /test_sample/_dash-component-suites/dash/deps/prop-types@15.v3_2_0m1757581726.8.1.min.js HTTP/1.1" 200 -
    INFO:werkzeug:10.213.1.236 - - [11/Sep/2025 09:09:19] "GET /test_sample/_dash-component-suites/vizro/static/js/models/checklist.v0_1_44m1757581727.js HTTP/1.1" 200 -
    INFO:werkzeug:10.213.1.236 - - [11/Sep/2025 09:09:19] "GET /test_sample/_dash-component-suites/vizro/static/js/models/dropdown.v0_1_44m1757581727.js HTTP/1.1" 200 -
    INFO:werkzeug:10.213.1.236 - - [11/Sep/2025 09:09:19] "GET /test_sample/_dash-component-suites/vizro/static/js/models/container.v0_1_44m1757581727.js HTTP/1.1" 200 -
    INFO:werkzeug:10.213.1.236 - - [11/Sep/2025 09:09:19] "GET /test_sample/_dash-component-suites/vizro/static/js/models/dashboard.v0_1_44m1757581727.js HTTP/1.1" 200 -
    INFO:werkzeug:10.213.1.236 - - [11/Sep/2025 09:09:19] "GET /test_sample/_dash-component-suites/dash_ag_grid/dash_ag_grid.v32_3_1m1757581727.min.js HTTP/1.1" 200 -
    INFO:werkzeug:10.213.1.236 - - [11/Sep/2025 09:09:19] "GET /test_sample/_dash-component-suites/vizro/static/js/models/page.v0_1_44m1757581727.js HTTP/1.1" 200 -
    INFO:werkzeug:10.213.1.236 - - [11/Sep/2025 09:09:19] "GET /test_sample/_dash-component-suites/vizro/static/js/models/range_slider.v0_1_44m1757581727.js HTTP/1.1" 200 -
    INFO:werkzeug:10.213.1.236 - - [11/Sep/2025 09:09:19] "GET /test_sample/_dash-component-suites/dash_mantine_components/dash_mantine_components.v2_2_1m1757581726.js HTTP/1.1" 200 -
    INFO:werkzeug:10.213.1.236 - - [11/Sep/2025 09:09:19] "GET /test_sample/_dash-component-suites/vizro/static/js/models/slider.v0_1_44m1757581727.js HTTP/1.1" 200 -
    INFO:werkzeug:10.213.1.236 - - [11/Sep/2025 09:09:19] "GET /test_sample/_dash-component-suites/dash/dcc/dash_core_components.v3_2_0m1757581726.js HTTP/1.1" 200 -
    INFO:werkzeug:10.213.1.236 - - [11/Sep/2025 09:09:19] "GET /test_sample/_dash-component-suites/dash/dash-renderer/build/dash_renderer.v3_2_0m1757581726.min.js HTTP/1.1" 200 -
    INFO:werkzeug:10.213.1.236 - - [11/Sep/2025 09:09:19] "GET /test_sample/_dash-component-suites/dash/html/dash_html_components.v3_0_4m1757581726.min.js HTTP/1.1" 200 -
    INFO:werkzeug:10.213.1.236 - - [11/Sep/2025 09:09:19] "GET /test_sample/_dash-component-suites/dash/dcc/dash_core_components-shared.v3_2_0m1757581726.js HTTP/1.1" 200 -
    INFO:werkzeug:10.213.1.236 - - [11/Sep/2025 09:09:19] "GET /test_sample/_dash-component-suites/dash/dash_table/bundle.v6_0_4m1757581726.js HTTP/1.1" 200 -
    INFO:werkzeug:10.213.1.236 - - [11/Sep/2025 09:09:20] "GET /test_sample/_dash-dependencies HTTP/1.1" 200 -
    INFO:werkzeug:10.213.1.236 - - [11/Sep/2025 09:09:20] "GET /test_sample/_dash-layout HTTP/1.1" 200 -
    INFO:werkzeug:10.213.1.236 - - [11/Sep/2025 09:09:20] "GET /test_sample/_dash-component-suites/vizro/static/css/fonts/inter-variable-font.ttf HTTP/1.1" 200 -
    INFO:werkzeug:10.213.1.236 - - [11/Sep/2025 09:09:20] "POST /test_sample/_dash-update-component HTTP/1.1" 200 -
    INFO:werkzeug:10.213.1.236 - - [11/Sep/2025 09:09:21] "GET /test_sample/_dash-component-suites/dash/dcc/async-graph.js HTTP/1.1" 200 -
    INFO:werkzeug:10.213.1.236 - - [11/Sep/2025 09:09:21] "GET /test_sample/_dash-component-suites/dash/dcc/async-dropdown.js HTTP/1.1" 200 -
    INFO:werkzeug:10.213.1.236 - - [11/Sep/2025 09:09:21] "GET /test_sample/_dash-component-suites/plotly/package_data/plotly.min.js HTTP/1.1" 200 -
    INFO:werkzeug:10.213.1.236 - - [11/Sep/2025 09:09:21] "GET /test_sample/_dash-component-suites/vizro/static/css/fonts/material-symbols-outlined.woff2 HTTP/1.1" 200 -
    INFO:werkzeug:10.213.1.236 - - [11/Sep/2025 09:09:21] "GET /test_sample/_favicon.ico?v=3.2.0 HTTP/1.1" 200 -
    INFO:werkzeug:10.213.1.236 - - [11/Sep/2025 09:09:21] "POST /test_sample/_dash-update-component HTTP/1.1" 200 -
    
    ```

## Step 10. Access the web app

Once the Service starts running, users can access the dashboard in the endpoint configured in `ingress.path`.

```bash
https://${{dataos-fqdn}}/${{ingress-path}}/
```

**Example:**

```bash
https://liberal-katydid.dataos.app/test_sample/
```