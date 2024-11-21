# Grant Requests

This guide provides the end-to-end process for creating and approving grant requests use-cases to and users.

## Scenario

A user named Iamgroot attempts to access the Workbench but encounters access restrictions. Realizing he does not have the necessary permissions, he submits a grant request to an operator, seeking the required access rights to proceed.

## Steps

Follow the steps below to request access to the Workbench UI and gain the necessary permissions to interact with depots and sources.

### **Step 1: Initial Access Attempt**

Iamgroot, a user within the system, attempts to access the Workbench UI but encounters an access restriction message indicating that they do not have the necessary permissions to view or interact with the Workbench.

![no access](/learn/operator_learn_track/access_control/grant_requests/image (11).png)

### **Step 2: Grant Request Submission**

Realizing that they lack the required access rights, Iamgroot navigates to Grant Requests tab in Bifrost to submit a grant request to operator for permission to access the Workbench UI. 

![no access](/learn/operator_learn_track/access_control/grant_requests/bifrost_gr.png)

The grant request dialog box appears. Iamgroot then paste the below grant request.

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

The request contains all the necessary information, such as the required actions (e.g., view depots, run queries) and attributes for the access.

`policy_use_case_id`: Identifies the specific use case id for which the policy is created, in this case, `view-workbench-app`.

`name`: "View workbench App" specifies the name of the access request being submitted.

`description`: Describes the intended actions, which include viewing and querying depots and sources via the Workbench application.

`category`: This policy falls under the "query" category, indicating it involves querying data.

`authorization_atoms`: These are the specific actions or permissions the policy grants. In this case, the policy provides access to various features within the Workbench app, including:

- **workbench-app-access-workbench-ui:** Access to the Workbench UI.
- **workbench-app-save-cluster:** Permission to save a cluster configuration.
- **workbench-app-delete-saved-bench:** Permission to delete a saved workbench.
- **workbench-app-clone-saved-bench:** Permission to clone a saved workbench.
- **workbench-app-save-bench:** Permission to save a workbench.
- **workbench-app-run-query:** Permission to run queries.
- **subjects:** Specifies the entity requesting access. In this case, the user Iamgroot is requesting permission to access the Workbench app, specifically identified by users:id:iamgroot.

This grant request ensures that the user Iamgroot has the necessary permissions to interact with the Workbench app and its related actions, such as viewing, saving, and querying workbenches.

The request details submitted by Iamgroot is as shown below:

![grant request yaml](/learn/operator_learn_track/access_control/grant_requests/grant_request_yaml.png)

### **Step 3: Operator Reviews the Request**

The operator, accesses the Grant Request tab in the system, where they can review Iamgroot’s submitted request.

![grant request yaml](/learn/operator_learn_track/access_control/grant_requests/requested_log.png)

The operator reviews the grant request to verify the details to determine whether access should be granted, and then clicks the 'Approve Grant Request' button.

### **Step 4: Grant Request Approval**

As he click on 'Approve Grant Request' button the confirmation dialog box appears, asking operator to confirm the Grant.

![confirmation_msg](/learn/operator_learn_track/access_control/grant_requests/image (8).png)

### **Step 4: Access Granted**

After the approval from the operator, the grant log status changes from requested to approved

![apporved log](/learn/operator_learn_track/access_control/grant_requests/approved_log.png)

Iamgroot is now able to access the Workbench UI as per the granted permissions. They can now view depots, run queries, save clusters, and utilize the full functionality of the Workbench.

![confirmation_msg](/learn/operator_learn_track/access_control/grant_requests/workkbench.png)

 