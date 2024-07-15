# How to manage/iterate the Data Product?

After successfully deploying the Data Product, it’s time to observe the results if the Data Product incorporates with your use-case or not, If the Data Product does not match the goal then you can iterate the process until your goal is achieved. 

## Manage the Data Product

### **Validate the Data Product**

To check if you have created a Data Product run the following command. It will list all the data products created by you.

```bash
dataos-ctl product get
```

**Example Usage:**

```bash
dataos-ctl product get
# expected output
product get...                             
product get...complete                     

  TYPE | VERSION |     NAME      | STATUS |    OWNER     
-------|---------|---------------|--------|--------------
  data | v1alpha |     dp-test   | active | iamgroot  
  

```

### **Delete the Data Product**

To delete the Data Product execute the following command.

```bash
dataos-ctl product delete -f ${path-to-dp-manifest-file}
```

**Example Usage:**

```bash
dataos-ctl product delete -f /home/iamgroot/office/data_products/firstdp.yaml
# Expected Output
INFO[0000] 🗑 product delete...                          
INFO[0000] 🗑 deleting data:v1alpha:dp-test... 
INFO[0000] 🗑 deleting data:v1alpha:dp-test...deleted 
INFO[0000] 🗑 product delete...complete 
```

**Alternative commands to delete the Data Product:**

- using `-i` identifier.
    
    ```bash
    dataos-ctl product delete -i TYPE:VERSION:NAME
    ```
    
    **Example Usage:**
    
    ```bash
    dataos-ctl product delete -i data:v1alpha:dp-test
    # Expected Output
    INFO[0000] 🗑 product delete...                          
    INFO[0000] 🗑 deleting data:v1alpha:dp-test... 
    INFO[0000] 🗑 deleting data:v1alpha:dp-test...deleted 
    INFO[0000] 🗑 product delete...complete 
    ```
    
- using `-t` type.
    
    ```bash
    dataos-ctl product delete -t data -n name -v version
    ```
    
    **Example Usage:**
    
    ```bash
    dataos-ctl product delete -t data -n dataproduct -v v1alpha
    # Expected Output
    INFO[0000] 🗑 product delete...                          
    INFO[0000] 🗑 deleting data:v1alpha:dp-test... 
    INFO[0000] 🗑 deleting data:v1alpha:dp-test...deleted 
    INFO[0000] 🗑 product delete...complete 
    ```
    

### **Delete the metadata of the Data Product from Metis:**

When clicking on your Data Product on Metis, clicking on the menu of the right-corner you will have the option to delete the metadata from Metis as you can see below:

![delete](/products/data_product/how_to_guides/delete.png)

## Iterate the Data Product
Iterating a Data Product involves refining and enhancing it based on feedback, performance metrics, and evolving business requirements. If you need to iterate your Data Product based on feedback from data consumers, follow these steps:

- **Collect Feedback:** Gather feedback from users and stakeholders regarding the Data Product's performance, usability, and effectiveness in solving the intended problem.

- **Analyze Feedback:** Identify common issues and suggestions for improvements. Prioritize these based on impact and feasibility.

- **Plan Iteration:** Define the scope of changes needed to address the feedback. Create a plan that includes tasks, timelines, and resources required for the iteration.

- **Implement Changes:** Update the Data Product according to the iteration plan. This might involve modifying data sources, transformation logic, data models, or visualization techniques.

- **Validate Changes:** Ensure that the changes meet the intended goals and do not introduce new issues. Validate the updated Data Product through testing and user acceptance.

- **Deploy Updated Product:** Deploy the updated Data Product to the production environment.

- **Monitor and Iterate Again:** After deployment, monitor the Data Product's performance and continue to collect feedback. Iterate the process as needed to achieve the desired results.

By following these steps, you can continuously improve your Data Product to better meet user needs and business objectives.