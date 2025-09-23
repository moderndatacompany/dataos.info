# Streamlit Implementation

This section provides the steps to implement the Streamlit framework to build a web application using the Python Stack. 

<div style="text-align: center;">
    <figure>
    <img src="/resources/stacks/python/streamlit.png" 
        alt="Streamlit App" 
        style="border: 1px solid black; width: 80%; height: auto; display: block; margin: auto;">
    <figcaption style="margin-top: 8px; font-style: italic;">Streamlit App</figcaption>
    </figure>
</div>



## Pre-requisites

Before starting to implement the Streamlit framework using Python Stack, ensure you have met the requirements listed [in this section.](/resources/stacks/python/#pre-requisites) 

## Step 1. Create/Select a Repository

Create or select any repository in GitHub or Bitbucket where the Python code will be added.

## Step 2. Create base directory

Inside that repository, add a folder named `app`, which will include the Python scripts with the `.py` extension, a requirements file with a `.txt` extension, and `.streamlit` folder with `config.toml` file, which will include Streamlit-specific configurations.

```sql
python-stack/
└── app/                        # baseDir (referenced in service/stack manifest)
    ├── main.py                 # Application entry point (required)
    ├── requirements.txt        # Dependencies (required)
    ├── app_ui.py               # Streamlit UI logic
    └── .streamlit/             # Streamlit-specific configuration folder
        └── config.toml         # Custom Streamlit configuration
```

## Step 3. Add the Python code and dependencies

In the files with the `.py` extension, add your Python script, in the `requirements.txt` file, add the requirements to run the Python scripts, and in the `config.toml`, add streamlit-specific configurations as given in the example below.

**Example:**

=== "app_ui.py"
    
    ```python
    # app_ui.py
    import streamlit as st
    
    def run_app():
        st.set_page_config(page_title="Demo App", layout="centered")
    
        st.title("🚀 Streamlit App on DataOS Stack")
        st.write("This is a simple Streamlit app deployed using a custom Python 3.12 stack.")
    
        name = st.text_input("Enter your name:")
        if name:
            st.success(f"Hello, {name}! Welcome to DataOS Streamlit deployments.")
    ```

=== "main.py"
    
    ```python
    # main.py
    import os
    from app_ui import run_app  # Import the user's Streamlit app
    
    def main():
        # Check if already running inside Streamlit to avoid recursion
        if not os.getenv("IS_RUNNING_STREAMLIT"):
            os.environ["IS_RUNNING_STREAMLIT"] = "1"
            os.system(f"streamlit run {__file__}")
            return
    
        # Call the actual app function
        run_app()
    
    if __name__ == "__main__":
        main()
    ```
    
=== "requirements.txt"
    
    ```bash
    streamlit==1.45.0
    pandas==2.2.2
    numpy>=1.24.0
    requests
    ```
    
=== "config.toml"
    
    ```toml
    # .streamlit/config.toml
    [server]
    port = 8050
    address = "0.0.0.0"
    baseUrlPath = "test_sample"
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

- **GitHub:** Create a Personal Access Token (PAT), then store it in DataOS as a secret. [Guide](https://dataos.info/resources/instance_secret/repositories/git/) | [GitHub PAT docs](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic)
- **Bitbucket:** Generate an App Password (API token) with repo permissions, then store it in DataOS as a secret. [Guide](https://dataos.info/resources/instance_secret/repositories/bitbucket/) | [Bitbucket docs](https://support.atlassian.com/bitbucket-cloud/docs/create-an-api-token/)

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
      baseDir: queries/pystack-streamlit
      syncFlags:
        - '--ref=main'
      url: https://bitbucket.org/queries/
```

<aside class="callout">
🗣 The ingress path defined in the Service manifest file must match the base URL path configured in `.streamlit/config.toml`. A mismatch here will cause the ingress to fail.

</aside>

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

<details>
    <summary>Example</summary>
    
    ```bash
    dataos-ctl resource log -t service -w public -n my-python-app-test
    INFO[0000] 📃 log(public)...                             
    INFO[0001] 📃 log(public)...complete                     
    
                      NODE NAME                  │        CONTAINER NAME        │ ERROR  
    ─────────────────────────────────────────────┼──────────────────────────────┼────────
      my-python-app-test-6831-d-57cbf95b7c-zz4j9 │ my-python-app-test-6831-main │        
    
    -------------------LOGS-------------------
    /etc/dataos/work
    Collecting streamlit==1.45.0 (from -r requirements.txt (line 1))
      Downloading streamlit-1.45.0-py3-none-any.whl.metadata (8.9 kB)
    Collecting pandas==2.2.2 (from -r requirements.txt (line 2))
      Downloading pandas-2.2.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (19 kB)
    Collecting numpy>=1.24.0 (from -r requirements.txt (line 3))
      Downloading numpy-2.3.2-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (62 kB)
    Collecting requests (from -r requirements.txt (line 4))
      Downloading requests-2.32.5-py3-none-any.whl.metadata (4.9 kB)
    Collecting altair<6,>=4.0 (from streamlit==1.45.0->-r requirements.txt (line 1))
      Downloading altair-5.5.0-py3-none-any.whl.metadata (11 kB)
    Collecting blinker<2,>=1.5.0 (from streamlit==1.45.0->-r requirements.txt (line 1))
      Downloading blinker-1.9.0-py3-none-any.whl.metadata (1.6 kB)
    Collecting cachetools<6,>=4.0 (from streamlit==1.45.0->-r requirements.txt (line 1))
      Downloading cachetools-5.5.2-py3-none-any.whl.metadata (5.4 kB)
    Collecting click<9,>=7.0 (from streamlit==1.45.0->-r requirements.txt (line 1))
      Downloading click-8.2.1-py3-none-any.whl.metadata (2.5 kB)
    Collecting packaging<25,>=20 (from streamlit==1.45.0->-r requirements.txt (line 1))
      Downloading packaging-24.2-py3-none-any.whl.metadata (3.2 kB)
    Collecting pillow<12,>=7.1.0 (from streamlit==1.45.0->-r requirements.txt (line 1))
      Downloading pillow-11.3.0-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (9.0 kB)
    Collecting protobuf<7,>=3.20 (from streamlit==1.45.0->-r requirements.txt (line 1))
      Downloading protobuf-6.32.0-cp39-abi3-manylinux2014_x86_64.whl.metadata (593 bytes)
    Collecting pyarrow>=7.0 (from streamlit==1.45.0->-r requirements.txt (line 1))
      Downloading pyarrow-21.0.0-cp312-cp312-manylinux_2_28_x86_64.whl.metadata (3.3 kB)
    Collecting tenacity<10,>=8.1.0 (from streamlit==1.45.0->-r requirements.txt (line 1))
      Downloading tenacity-9.1.2-py3-none-any.whl.metadata (1.2 kB)
    Collecting toml<2,>=0.10.1 (from streamlit==1.45.0->-r requirements.txt (line 1))
      Downloading toml-0.10.2-py2.py3-none-any.whl.metadata (7.1 kB)
    Collecting typing-extensions<5,>=4.4.0 (from streamlit==1.45.0->-r requirements.txt (line 1))
      Downloading typing_extensions-4.15.0-py3-none-any.whl.metadata (3.3 kB)
    Collecting watchdog<7,>=2.1.5 (from streamlit==1.45.0->-r requirements.txt (line 1))
      Downloading watchdog-6.0.0-py3-none-manylinux2014_x86_64.whl.metadata (44 kB)
    Collecting gitpython!=3.1.19,<4,>=3.0.7 (from streamlit==1.45.0->-r requirements.txt (line 1))
      Downloading gitpython-3.1.45-py3-none-any.whl.metadata (13 kB)
    Collecting pydeck<1,>=0.8.0b4 (from streamlit==1.45.0->-r requirements.txt (line 1))
      Downloading pydeck-0.9.1-py2.py3-none-any.whl.metadata (4.1 kB)
    Collecting tornado<7,>=6.0.3 (from streamlit==1.45.0->-r requirements.txt (line 1))
      Downloading tornado-6.5.2-cp39-abi3-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (2.8 kB)
    Collecting python-dateutil>=2.8.2 (from pandas==2.2.2->-r requirements.txt (line 2))
      Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
    Collecting pytz>=2020.1 (from pandas==2.2.2->-r requirements.txt (line 2))
      Downloading pytz-2025.2-py2.py3-none-any.whl.metadata (22 kB)
    Collecting tzdata>=2022.7 (from pandas==2.2.2->-r requirements.txt (line 2))
      Downloading tzdata-2025.2-py2.py3-none-any.whl.metadata (1.4 kB)
    Collecting charset_normalizer<4,>=2 (from requests->-r requirements.txt (line 4))
      Downloading charset_normalizer-3.4.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (36 kB)
    Collecting idna<4,>=2.5 (from requests->-r requirements.txt (line 4))
      Downloading idna-3.10-py3-none-any.whl.metadata (10 kB)
    Collecting urllib3<3,>=1.21.1 (from requests->-r requirements.txt (line 4))
      Downloading urllib3-2.5.0-py3-none-any.whl.metadata (6.5 kB)
    Collecting certifi>=2017.4.17 (from requests->-r requirements.txt (line 4))
      Downloading certifi-2025.8.3-py3-none-any.whl.metadata (2.4 kB)
    Collecting jinja2 (from altair<6,>=4.0->streamlit==1.45.0->-r requirements.txt (line 1))
      Downloading jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
    Collecting jsonschema>=3.0 (from altair<6,>=4.0->streamlit==1.45.0->-r requirements.txt (line 1))
      Downloading jsonschema-4.25.1-py3-none-any.whl.metadata (7.6 kB)
    Collecting narwhals>=1.14.2 (from altair<6,>=4.0->streamlit==1.45.0->-r requirements.txt (line 1))
      Downloading narwhals-2.4.0-py3-none-any.whl.metadata (11 kB)
    Collecting gitdb<5,>=4.0.1 (from gitpython!=3.1.19,<4,>=3.0.7->streamlit==1.45.0->-r requirements.txt (line 1))
      Downloading gitdb-4.0.12-py3-none-any.whl.metadata (1.2 kB)
    Collecting six>=1.5 (from python-dateutil>=2.8.2->pandas==2.2.2->-r requirements.txt (line 2))
      Downloading six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
    Collecting smmap<6,>=3.0.1 (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit==1.45.0->-r requirements.txt (line 1))
      Downloading smmap-5.0.2-py3-none-any.whl.metadata (4.3 kB)
    Collecting MarkupSafe>=2.0 (from jinja2->altair<6,>=4.0->streamlit==1.45.0->-r requirements.txt (line 1))
      Downloading MarkupSafe-3.0.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.0 kB)
    Collecting attrs>=22.2.0 (from jsonschema>=3.0->altair<6,>=4.0->streamlit==1.45.0->-r requirements.txt (line 1))
      Downloading attrs-25.3.0-py3-none-any.whl.metadata (10 kB)
    Collecting jsonschema-specifications>=2023.03.6 (from jsonschema>=3.0->altair<6,>=4.0->streamlit==1.45.0->-r requirements.txt (line 1))
      Downloading jsonschema_specifications-2025.9.1-py3-none-any.whl.metadata (2.9 kB)
    Collecting referencing>=0.28.4 (from jsonschema>=3.0->altair<6,>=4.0->streamlit==1.45.0->-r requirements.txt (line 1))
      Downloading referencing-0.36.2-py3-none-any.whl.metadata (2.8 kB)
    Collecting rpds-py>=0.7.1 (from jsonschema>=3.0->altair<6,>=4.0->streamlit==1.45.0->-r requirements.txt (line 1))
      Downloading rpds_py-0.27.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.2 kB)
    Downloading streamlit-1.45.0-py3-none-any.whl (9.9 MB)
       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 9.9/9.9 MB 58.3 MB/s eta 0:00:00
    Downloading pandas-2.2.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (12.7 MB)
       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 12.7/12.7 MB 161.8 MB/s eta 0:00:00
    Downloading numpy-2.3.2-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (16.6 MB)
       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 16.6/16.6 MB 147.7 MB/s eta 0:00:00
    Downloading requests-2.32.5-py3-none-any.whl (64 kB)
    Downloading altair-5.5.0-py3-none-any.whl (731 kB)
       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 731.2/731.2 kB 306.7 MB/s eta 0:00:00
    Downloading blinker-1.9.0-py3-none-any.whl (8.5 kB)
    Downloading cachetools-5.5.2-py3-none-any.whl (10 kB)
    Downloading certifi-2025.8.3-py3-none-any.whl (161 kB)
    Downloading charset_normalizer-3.4.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (151 kB)
    Downloading click-8.2.1-py3-none-any.whl (102 kB)
    Downloading gitpython-3.1.45-py3-none-any.whl (208 kB)
    Downloading idna-3.10-py3-none-any.whl (70 kB)
    Downloading packaging-24.2-py3-none-any.whl (65 kB)
    Downloading pillow-11.3.0-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (6.6 MB)
       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.6/6.6 MB 190.1 MB/s eta 0:00:00
    Downloading protobuf-6.32.0-cp39-abi3-manylinux2014_x86_64.whl (322 kB)
    Downloading pyarrow-21.0.0-cp312-cp312-manylinux_2_28_x86_64.whl (42.8 MB)
       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 42.8/42.8 MB 142.6 MB/s eta 0:00:00
    Downloading pydeck-0.9.1-py2.py3-none-any.whl (6.9 MB)
       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.9/6.9 MB 169.9 MB/s eta 0:00:00
    Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
    Downloading pytz-2025.2-py2.py3-none-any.whl (509 kB)
    Downloading tenacity-9.1.2-py3-none-any.whl (28 kB)
    Downloading toml-0.10.2-py2.py3-none-any.whl (16 kB)
    Downloading tornado-6.5.2-cp39-abi3-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (443 kB)
    Downloading typing_extensions-4.15.0-py3-none-any.whl (44 kB)
    Downloading tzdata-2025.2-py2.py3-none-any.whl (347 kB)
    Downloading urllib3-2.5.0-py3-none-any.whl (129 kB)
    Downloading watchdog-6.0.0-py3-none-manylinux2014_x86_64.whl (79 kB)
    Downloading gitdb-4.0.12-py3-none-any.whl (62 kB)
    Downloading jinja2-3.1.6-py3-none-any.whl (134 kB)
    Downloading jsonschema-4.25.1-py3-none-any.whl (90 kB)
    Downloading narwhals-2.4.0-py3-none-any.whl (406 kB)
    Downloading six-1.17.0-py2.py3-none-any.whl (11 kB)
    Downloading attrs-25.3.0-py3-none-any.whl (63 kB)
    Downloading jsonschema_specifications-2025.9.1-py3-none-any.whl (18 kB)
    Downloading MarkupSafe-3.0.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (23 kB)
    Downloading referencing-0.36.2-py3-none-any.whl (26 kB)
    Downloading rpds_py-0.27.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (386 kB)
    Downloading smmap-5.0.2-py3-none-any.whl (24 kB)
    Installing collected packages: pytz, watchdog, urllib3, tzdata, typing-extensions, tornado, toml, tenacity, smmap, six, rpds-py, pyarrow, protobuf, pillow, packaging, numpy, narwhals, MarkupSafe, idna, click, charset_normalizer, certifi, cachetools, blinker, attrs, requests, referencing, python-dateutil, jinja2, gitdb, pydeck, pandas, jsonschema-specifications, gitpython, jsonschema, altair, streamlit
    Successfully installed MarkupSafe-3.0.2 altair-5.5.0 attrs-25.3.0 blinker-1.9.0 cachetools-5.5.2 certifi-2025.8.3 charset_normalizer-3.4.3 click-8.2.1 gitdb-4.0.12 gitpython-3.1.45 idna-3.10 jinja2-3.1.6 jsonschema-4.25.1 jsonschema-specifications-2025.9.1 narwhals-2.4.0 numpy-2.3.2 packaging-24.2 pandas-2.2.2 pillow-11.3.0 protobuf-6.32.0 pyarrow-21.0.0 pydeck-0.9.1 python-dateutil-2.9.0.post0 pytz-2025.2 referencing-0.36.2 requests-2.32.5 rpds-py-0.27.1 six-1.17.0 smmap-5.0.2 streamlit-1.45.0 tenacity-9.1.2 toml-0.10.2 tornado-6.5.2 typing-extensions-4.15.0 tzdata-2025.2 urllib3-2.5.0 watchdog-6.0.0
    WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager, possibly rendering your system unusable. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv. Use the --root-user-action option if you know what you are doing and want to suppress this warning.
    
    [notice] A new release of pip is available: 25.0.1 -> 25.2
    [notice] To update, run: pip install --upgrade pip
    
    Collecting usage statistics. To deactivate, set browser.gatherUsageStats to false.
    
      You can now view your Streamlit app in your browser.
    
      URL: http://0.0.0.0:8050/test_sample_st01
    
    ```
</details>    

## Step 10. Access the web app

Once the Service starts running, users can access the web app using the base URL configured in `config.toml` as shown in the example below.

```bash
https://${{dataos-fqdn}}/${{baseUrlPath}}/
```

**Example:**

```bash
https://liberal-katydid.dataos.app/test_sample/
```