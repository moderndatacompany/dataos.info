# How to manage/iterate the Data Product?

After successfully deploying the Data Product, it’s time to observe the results if the Data Product incorporates with your use-case or not, If the Data Product does not match the goal then you can iterate the process until your goal is achieved. 

## **Manage the Data Product**

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

When clicking on your Data Product on Metis, clicking on the kebab menu of the right-corner you will have the option to delete the metadata from Metis as you can see below:

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/f6fba555-8d87-46a8-8ec1-55274402da17/Untitled.png)