# How to fetch data exposed by Talos from the third-party tools?

Similarly, with any other Rest APIs, the API created by Talos can be used by external tools to create dashboards or applications. In this section, we will see how to create a dashboard on AppSmith, an open-source developer tool that enables the rapid development of applications. You can drag and drop pre-built widgets to build UI and connect securely to your APIs using its data sources. 

## Steps to create the dashboard on AppSmith using Talos API Key

- Go to [AppSmith's](https://www.appsmith.com/) official website, and navigate to the Try Cloud button.

  <div style="text-align: center;">
    <img src="/resources/stacks/talos/image.png" style="border:1px solid black; width: 80%; height: auto;">
  </div>
    
    
- You will be redirected to the login page of AppSmith as shown below:
    
<div style="text-align: center;">
  <img src="/resources/stacks/talos/image%20(1).png" style="border:1px solid black; width: 80%; height: auto;">
</div>

    
- After signing in, you will be redirected to the AppSmith interface where you can start creating dashboard as shown below:
    
<div style="text-align: center;">
  <img src="/resources/stacks/talos/image%20(2).png" style="border:1px solid black; width: 60%; height: auto;">
</div>


    
- Create a new workspace, by clicking on the `+` on the left panel as shown below.

<div style="text-align: center;">
  <img src="/resources/stacks/talos/image%20(3).png" style="border:1px solid black; width: 60%; height: auto;">
</div>


    
- Create a new application as shown below.

<div style="text-align: center;">
  <img src="/resources/stacks/talos/image%20(4).png" style="border:1px solid black; width: 60%; height: auto;">
</div>


    
- To connect the data, on the right panel, navigate to the Connect data button.

<div style="text-align: center;">
  <img src="/resources/stacks/talos/image%20(5).png" style="border:1px solid black; width: 60%; height: auto;">
</div>



    
- Then select `Authenticated API` option as shown below.

<div style="text-align: center;">
  <img src="/resources/stacks/talos/image%20(6).png" style="border:1px solid black; width: 60%; height: auto;">
</div>

     
    
- In the `URL` section give your API endpoint URL and select `Bearer` as Authentication Type and give your DataOS API key.

<div style="text-align: center;">
  <img src="/resources/stacks/talos/image%20(7).png" style="border:1px solid black; width: 60%; height: auto;">
</div>

     
    
- Then click on Save.

<div style="text-align: center;">
  <img src="/resources/stacks/talos/image%20(8).png" style="border:1px solid black; width: 60%; height: auto;">
</div>

     
    
- Then on the same interface, create a new API as shown below.

<div style="text-align: center;">
  <img src="/resources/stacks/talos/image%20(9).png" style="border:1px solid black; width: 60%; height: auto;">
</div>

     
    
- Then click on `Run` , execution will look like the following.

<div style="text-align: center;">
  <img src="/resources/stacks/talos/image%20(10).png" style="border:1px solid black; width: 60%; height: auto;">
</div>

     
    
- Add the visuals of your preference to create a dashboard by drag and drop by selecting the data.

<div style="text-align: center;">
  <img src="/resources/stacks/talos/image%20(11).png" style="border:1px solid black; width: 60%; height: auto;">
</div>

     