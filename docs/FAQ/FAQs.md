# FAQs

Let us address your questions and concerns here.

- <span style="color:maroon">Why is the hierarchy in UDLs different from in Workbench? In UDL we use Depot —> Collection —> Datasets, while in Workbench we use Catalog —> Schema —> Tables.</span>
    
    This has been done intentionally. While in Workbench, you query only relational databases, Depots can address all sorts of data sources, including non-relational databases and file systems. If a depot has been created for an unstructured data source, it would not make sense to have schemas and tables within it.
    
    Moreover, the Catalogs in Workbench include more than just the data sources you address using depots.
    

- <span style="color:maroon">When we check the list of Depots on the CLI or Operations Center, we see Runtime as running:1 for some of them. What does it mean? Check the screenshot below.</span>
    
    ```jsx
    dataos-ctl get -t depot -a
    
           NAME      | VERSION | TYPE  | WORKSPACE | STATUS |  RUNTIME  |          OWNER           
    -----------------|---------|-------|-----------|--------|-----------|--------------------------
      azure          | v1      | depot |           | active | running:1 | iamgroot                            
      blender        | v1      | depot |           | active |           | dataos-resource-manager  
      customer       | v1      | depot |           | active | running:1 | thor             
      demosqlserver  | v1      | depot |           | active |           | testuser
    ```
    
    It indicates that the a metastore (e.g. Hive metastore) is running behind the scene for that particular depot. This happens when the data source is unstructured and doesn’t support introspection by the depot service. In depots, typically, you will see the running:1 status for blob storages like GCS, AWS S3 and Azure ABFSS. The Metastore server allows you to create tabulation of your unstructured data.
    
    You can check the runtime for DataOS Resources other than depots as well. The numeral 1,2,3… represent the number of pod replicas which are being used to run that particular resource.
    

- <span style="color:maroon">Why do I get the expired token error when I try to run a command on DataOS CLI? This is the error which shows up:</span>
    
    ```yaml
    ERRO[0001] Unauthorized - {"error":{"status":401,"message":"could not verify the token : oidc: token is expired (Token Expiry: 2022-09-24 06:42:39 +0000 UTC)"},"allow":false}
    ```
    
    By default, you are automatically logged out of the DataOS context every 24 hours. All you need to do is login again using the following command:
    
    ```yaml
    dataos-ctl login
    ```
    
    You *do not* need to install or even initialize the DataOS context again, only login.
    
<br>

> Reach out to us if you have more questions. We will be happy to help you out.
Email id: dataosdocs@tmdc.io
>