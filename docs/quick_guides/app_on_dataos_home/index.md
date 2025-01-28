# Listing Your App on DataOS Home

!!! info "Information"
    This guide provides step-by-step instructions to list an app built with Streamlit, Django, Flask, or other frameworks on DataOS home for seamless access and management.

## Prerequisites

Ensure your app is up and running before proceeding with the steps below. This can be achieved by deploying it using the **Container Stack**.

### **Step 1: Open the `service.yaml` File**

Locate and open the `service.yaml` file that was created to deploy your application to the DataOS environment using the Container Stack.

### **Step 2: Add `appDetailSpec` Property**

Under the `ingress` section of the `service.yaml` file, add the `appDetailSpec` property.

### **Step 3: Provide the Required Information**

Fill in the `appDetailSpec` section with the following details:

| **Key** | **Description** | **Example Value** |
| --- | --- | --- |
| `name` | The name of the application. | `"MyApp"` |
| `title` | The title or description of the application. | `"My Application"` |
| `releaseLevel` | The release level of the application (e.g., beta). | `"beta"` |
| `description` | A brief description of the application. | `"This is a sample app."` |
| `icon` | Application icon in Base64 format (optional). | `"base64string..."` |
| `section` | The category or section of the application. | `"Business"` |
| `path` | The path or URL associated with the application. | `"/myapp/home"` |
| `keyword` | Keywords related to the application. | `["analytics", "data"]` |
| `isInternal` | Indicates if the application is for internal use. | `true` |
| `disabled` | Indicates if the application is currently disabled. | `false` |
| `navigation` | Additional navigation-related settings. |  |

**Example `service.yaml`**

Below is an example of how the `service.yaml` file should look after adding the `appDetailSpec` property:

```yaml
version: v1
name: streamlit-calculator
type: service
service:
  replicas: 1
  servicePort: 8502
  ingress:
    enabled: true
    noAuthentication: true
    path: /streamlit/calculator
    stripPath: true
    appDetailSpec: '{
      "name": "Calculator",
      "title": "Calculator",
      "releaseLevel": "alpha",
      "description": "A simple and easy-to-use calculator for quick and accurate basic calculations.",
      "section": "Demo",
      "path": "/streamlit/calculator/",
      "keyword": "Simple Calculator",
      "isInternal": false,
      "disabled": false,
      "navigation": []
    }'
  stack: container
  compute: runnable-default
  envs:
    SECRET: "--config /etc/dataos/config/secret.conf"
  configs:
    secret.conf: app/secret.json
  resources:
    requests:
      cpu: 100m
      memory: 100Mi
    limits:
      cpu: 250m
      memory: 250Mi
  stackSpec:
    image: deep2407/test_streamlit:0.1.7
    command:
      - streamlit
    arguments:
      - run
      - calculator.py
      - --server.port=8502
      - --server.address=0.0.0.0
```

### **Step 4: Adding an App Icon**

If you want to customize your app icon, ensure it is in SVG format, which can then be encoded into a Base64 string.

1. Use the command-line tool to encode an SVG image:
    
    ```
    base64 -i <file_path>
    ```
    
2. Alternatively, use an online converter: [Base64 SVG Encoder](https://base64.guru/converter/encode/image/svg)

Once encoded, add the Base64 string as the value for the `icon` key within the `appDetailSpec`.

### **Step 5: Apply the service YAML**

```yaml
dataos-ctl apply -f <filepath/filename>
```

## Application Visibility on DataOS Home

Once the updated `service.yaml` is applied, your app icon will appear on the DataOS home page alongside other applications, as shown below:
![image.png](/quick_guides/app_on_dataos_home/cal_app_dataos_home.png)

## Next Step

To secure your deployed app with authentication and authorization, refer to the guide:

[**Securing Deployed Apps on DataOS**](/quick_guides/secure_deployed_app/)