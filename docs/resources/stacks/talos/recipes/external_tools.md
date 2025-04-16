## Fetching Data Exposed by Talos from Third-Party Tools

Talos APIs can be accessed by external tools in the same way as any other REST APIs. These APIs can be used to integrate data into third-party applications, including dashboards and business intelligence tools.

This section outlines the process of creating a dashboard in [**AppSmith**](https://www.appsmith.com/), an open-source developer tool that facilitates rapid application development. AppSmith allows users to build UI components by dragging and dropping pre-built widgets while securely connecting to APIs.

### **Steps to Create a Dashboard on AppSmith Using a Talos API Key**

1. **Access AppSmith**
    - Navigate to [AppSmith's official website](https://www.appsmith.com/).
    - Click the **“Start for free”** and then **“Start on Cloud”** button to access the cloud version of AppSmith.
    
    <div style="text-align: center;">
      <img src="/resources/stacks/talos/recipes/et_image_0.png" style="border:1px solid black; width: 60%; height: auto;">
    </div>
    
2. **Sign In to AppSmith**
    - The login page will be displayed. Sign in using an existing account or create a new one.
    - After signing in, the AppSmith interface will be displayed.
    
    <div style="text-align: center;">
      <img src="/resources/stacks/talos/recipes/et_image_1.png" style="border:1px solid black; width: 60%; height: auto;">
    </div>
    
3. **Create a New Workspace**
    - Click the **"+"** button on the left panel to create a new workspace.
    
    <div style="text-align: center;">
      <img src="/resources/stacks/talos/recipes/et_image_2.png" style="border:1px solid black; width: 60%; height: auto;">
    </div>
    
4. **Create a New Application**
    - Inside the workspace, create a new application.
    
    <div style="text-align: center;">
      <img src="/resources/stacks/talos/recipes/et_image_3.png" style="border:1px solid black; width: 60%; height: auto;">
    </div>
    
5. **Connect Data to the Application**
    - Select a UI element from the left panel, e.g. Chart.
    
    <div style="text-align: center;">
      <img src="/resources/stacks/talos/recipes/et_image_4.png" style="border:1px solid black; width: 60%; height: auto;">
    </div>
    
    - Now on the right panel, click the **"Connect data"** button.
    
    <div style="text-align: center;">
      <img src="/resources/stacks/talos/recipes/et_image_5.png" style="border:1px solid black; width: 60%; height: auto;">
    </div>
    
    - Select the **"Authenticated API"** option.
    
    <div style="text-align: center;">
      <img src="/resources/stacks/talos/recipes/et_image_6.png" style="border:1px solid black; width: 60%; height: auto;">
    </div>
    
    - In the **URL** section, enter the Talos API endpoint URL.
    - Set the **Authentication Type** to **Bearer** and enter the DataOS API key.
    - Click **"Save"** to store the configuration.
    
    <div style="text-align: center;">
      <img src="/resources/stacks/talos/recipes/et_image_7.png" style="border:1px solid black; width: 60%; height: auto;">
    </div>
    
6. **Create and Execute an API Request**
    - On the same interface, create a new API request.
    
    <div style="text-align: center;">
      <img src="/resources/stacks/talos/recipes/et_image_8.png" style="border:1px solid black; width: 60%; height: auto;">
    </div>
    
    - Click **"Run"** to execute the API call. The response will be displayed in the execution panel.
    
    <div style="text-align: center;">
      <img src="/resources/stacks/talos/recipes/et_image_9.png" style="border:1px solid black; width: 60%; height: auto;">
    </div>
    
7. **Build a Dashboard**
    - Add visual components by dragging and dropping widgets.
    - Select the required data and configure visual elements accordingly.
    
    <div style="text-align: center;">
      <img src="/resources/stacks/talos/recipes/et_image_10.png" style="border:1px solid black; width: 60%; height: auto;">
    </div>
    
This process enables seamless integration of Talos API data into AppSmith, allowing users to build interactive dashboards.

