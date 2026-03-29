# Governance

After running the Lakesearch Service successfully, an Operator can govern who can access the endpoints, by assigning the `Manage Lakesearch` use case using the Bifrost Governance.

<aside class="callout">

Use case grants are only valid for users with the `roles:id:user` and `users:id:iamgroot` tags. Users with the `roles:id:data-dev` tag do not need to be assigned a use case, as they can already access the endpoint. To check the tags a user have to execute the `dataos-ctl user get -i ${{user-id}}` command on DataOS CLI, the expected output will look like the following for the user ID `iamgroot` :

```bash
INFO[0000] 😃 user get...                                
INFO[0000] 😃 user get...complete                        

    NAME   │    ID    │  TYPE  │      EMAIL       │              TAGS               
───────────┼──────────┼────────┼──────────────────┼─────────────────────────────────
  IamGroot │ iamgroot │ person │ iamgroot@tmdc.io │ roles:id:user,                  
           │          │        │                  │ users:id:iamgroot               

```

</aside>

Steps to assign the use case:

1. Navigate to the Bifrost Governance on the DataOS home page.

    <div style="text-align: center;">
    <img src="/resources/stacks/lakesearch/images/bifrost.png" alt="Lakesearch" style="border:1px solid black; width: 60%; height: auto;">
    </div>

    
2. Navigate to the Users tab and search for the user whom you want to assign the use case.
    
    <div style="text-align: center;">
    <img src="/resources/stacks/lakesearch/images/buser.png" alt="Lakesearch" style="border:1px solid black; width: 60%; height: auto;">
    </div>
    
3. Click on the user, navigate to the Grants tab, and click Grant Use-Case.
    
    <div style="text-align: center;">
    <img src="/resources/stacks/lakesearch/images/gusecase.png" alt="Lakesearch" style="border:1px solid black; width: 60%; height: auto;">
    </div>
   
4. Search for the manage Lakesearch use case and click on the Grant. This action will grant permission to access the Lakesearch endpoint to the users.
    
    <div style="text-align: center;">
    <img src="/resources/stacks/lakesearch/images/grant.png" alt="Lakesearch" style="border:1px solid black; width: 60%; height: auto;">
    </div>
