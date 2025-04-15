# How to govern Scanner? 

An Operator or Administrator of an organization can control who can create, read, update, or delete the Scanner workflow by assigning roles or use cases via Bifrost. The following access permissions are required to create a Scanner:

!!! info

    Keep in mind that the name and permission level of each role and use-cases can vary across organizations, depending on how they choose to manage them.


If granting access through use-case, the following use-case is required:

**`Manage Workflow in User Specified Workspace`**

If access is granted using Role, the role that contains the Workflow-related use-case needs to be granted. For example, the Data-dev Role contains the use cases to create and manage the role.

The role Data-dev is identified as `roles:id:data-dev` tag.

## How to grant a use-case to a user?

### **Navigate to DataOS**

Log in to DataOS and select the Bifrost. The Bifrost interface will launch.


<img src="/resources/stacks/scanner/scanner_img/bifrost.png"  class="center" style="width:45rem; display: block; margin: 0 auto; box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.3);" />



### **Search the user**

In Bifrost, navigate to the Users tab and use the search box to locate the user to whom you want to assign the use case.

<img src="/resources/stacks/scanner/scanner_img/bifrost_user_iamgroot.png"  class="center" style="width:45rem; display: block; margin: 0 auto; box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.3);" />



### **Click on the User**

After selecting the user, their detailed information will be displayed. Proceed to the Grants tab to view and manage the permissions and use cases assigned to that user.

<img src="/resources/stacks/scanner/scanner_img/iamgroot_grants_tab.png"  class="center" style="width:45rem; display: block; margin: 0 auto; box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.3);" />


In Grants tab, click on the 'Grant Use-Case' button.


### **Search the desired use-case**

As you click on the 'Grant Use-Case' button, a search dialog box appears. Here, search the use-case.

<img src="/resources/stacks/scanner/scanner_img/search_use_case.png"  class="center" style="width:45rem; display: block; margin: 0 auto; box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.3);" />



### **Provide the name of the workspace**

As you click on the `Manage Workflow in User Specified Workspace` a dialog box will appear prompting you to enter the name of the workspace.  Provide the workspace name to which you want to grant user access for managing the Workflow (Scanner).  

!!! info

    Please note that you must specify the workspace name for each action (Read, Create, Update, and Delete) to ensure precise permission assignment.


For example, in the below image, the user has been granted permission to read Workflow (Scanner) in all workspace but can create update and delete only in the curriculum workspace.

<img src="/resources/stacks/scanner/scanner_img/use_case_dialog_box.png"  class="center" style="width:45rem; display: block; margin: 0 auto; box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.3);" />


After filling the dialog box form, click Grant. In this way the user's grant permissions will be updated and now he will be able to read Workflow (Scanner) in all workspaces but can manage the Workflow (Scanner) in the curriculum workspace only.
