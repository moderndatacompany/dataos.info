# Grant Requests


This guide provides the end-to-end process for creating and approving grant requests use-cases to and users.

## Scenario

A user named Iamgroot attempts to access the Workbench but encounters access restrictions. Realizing he does not have the necessary permissions, he submits a grant request to an operator, seeking the required access rights to proceed.

## Steps

Follow the steps below to request access to the Workbench UI and gain the necessary permissions to interact with depots and sources.

### **Step 1: Initial Access Attempt**

Iamgroot, a user within the system, attempts to access the Workbench UI but encounters an access restriction message indicating that they do not have the necessary permissions to view or interact with the Workbench.


### **Step 2: Grant Request Submission**

Realizing that they lack the required access rights, Iamgroot submits a grant request to an operator for permission to access the Workbench UI. The request contains all the necessary information, such as the required actions (e.g., view depots, run queries) and attributes for the access.

The request details submitted by Iamgroot include:

```yaml
policy_use_case_id: view-workbench-app
name: View workbench App
description: View and query depots and sources through workbench application.
category: query
authorization_atoms:
  - workbench-app-access-workbench-ui
  - workbench-app-save-cluster
  - workbench-app-delete-saved-bench
  - workbench-app-clone-saved-bench
  - workbench-app-save-bench
  - workbench-app-run-query
subjects:
   - users:id:iamgroot

```

### **Step 3: Operator Reviews the Request**

The operator, accesses the Grant Request tab in the system, where they can review Iamgroot’s submitted request. The operator confirms the request details and determines that the access should be granted.


### **Step 4: Grant Request Approval**

The operator proceeds to approve Iamgroot’s grant request. Upon approval, Iamgroot will be granted the necessary permissions to access the Workbench UI and perform actions like running queries, saving clusters, and interacting with the Workbench interface.

### **Step 4: Access Granted**

After the approval from the operator, Iamgroot is now able to access the Workbench UI as per the granted permissions. They can now view depots, run queries, save clusters, and utilize the full functionality of the Workbench.