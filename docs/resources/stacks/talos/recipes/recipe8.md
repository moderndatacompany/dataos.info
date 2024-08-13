# How to fetch data exposed by Talos from the third-party tools?

Similarly, with any other Rest APIs, the API created by Talos can be used by external tools to create dashboards or applications. In this section, we will see how to create a dashboard on AppSmith, an open-source developer tool that enables the rapid development of applications. You can drag and drop pre-built widgets to build UI and connect securely to your APIs using its data sources. 

## Steps to create the dashboard on AppSmith using Talos API Key

1. Go to [AppSmith's](https://www.appsmith.com/) official website, and navigate to the Try Cloud button.
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/4fd09937-62b0-4c4b-82fb-74d83dfcc144/image.png)
    
2. You will be redirected to the login page of AppSmith as shown below:
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/97e6fd4e-3a11-4e41-8bb3-2ccad2e018af/image.png)
    
3. After signing in, you will be redirected to the AppSmith interface where you can start creating dashboard as shown below:
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/1e50e235-21af-495a-99e1-d65b80a332aa/image.png)
    
4. Create a new workspace, by clicking on the `+` on the left panel as shown below.
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/a74a8dca-b10b-4de9-bfd3-7fde3000af71/image.png)
    
5. Create a new application as shown below.
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/04e84441-5afc-44f2-ac94-bdab33b07a99/image.png)
    
6. Add the visuals of your preference to create a dashboard by drag and drop. By default, it will create visuals on the sample data as shown below.
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/a461aa07-e54b-4f1d-8370-d9306d0899a8/image.png)
    
7. To connect the data, on the right panel, navigate to the Connect data button.
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/4eb59182-1eb6-40dd-acd5-87f54b4205b0/image.png)
    
8. Then select `Authenticated API` option as shown below.
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/fcd44e5c-02ad-4190-b75d-9e6ffe3bbfa0/image.png)
    
9. In the `URL` section give your API endpoint URL and select `Bearer` as Authentication Type and give your DataOS API key.
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/84adad19-92ef-46bd-b0c6-51347a2328d0/image.png)
    
10. Then click on save.
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/6c7613fa-e402-45d9-a8b9-27d8fdfa8f12/image.png)
    
11. Then on the same interface, create a new API as shown below.
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/07df0b07-676d-4e2b-b3d8-c5386db35974/image.png)
    
12. Then click on `Run` , execution will look like the following.
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/6c314262-e09c-431b-b243-c8dc2e8816f6/image.png)
    
13.