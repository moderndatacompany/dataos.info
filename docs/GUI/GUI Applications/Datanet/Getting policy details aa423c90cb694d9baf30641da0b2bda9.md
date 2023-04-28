# Getting policy details

1. Sign in to your DataOS instance with your username and password.

2. On the **DataOS Datanet** page, click on **Policies**.

![governance-policies-datanet.png](Getting%20policy%20details/governance-policies-datanet.png)

3. For Access policies, Click on **Access Policy**.

![governance-policies-accesspolicy.png](Getting%20policy%20details/governance-policies-accesspolicy.png)

> 📌 **Note**: You must have 'Operator' privileges to access this information.
> 

The following information appears on the screen.

| Field | Description |
| --- | --- |
| Allow/Deny | Permission to access the resource |
| Subject | User/system who wants permission to perform the action |
| Predicate | Action to be performed such as read, write, get post |
| Object | Target to perform action on based on the tags |

4. For Masking policies, Click on **Mask Policy**.

![governance-policies-maskpolicy.png](Getting%20policy%20details/governance-policies-maskpolicy.png)

The following information appears on the screen.

| Field | Description |
| --- | --- |
| Priority | Permission to access the resource |
| Depot | Depot on which access permission is given, ** indicates all depots |
| Collection | Collection on which access permission is given, ** indicates all collections |
| Dataset | Dataset on which access permission is given, ** indicates all datasets |
| Columns | Columns on which masking strategy is applied |
Name | Policy name |
| Formula | Formula for masking strategy |
| Users | Users or tags who have this policy applied |
| Desc | Short description of the policy defined |

For example, a default PII policy is defined to protect sensitive information in your data. So, any column of any collection and dataset with dataos:f:pii tag is not visible to any user with tag dataos-user (default tag for all logged-in users) as the defined policy hashes the column values. But sometimes, you want some of the users to access this information. So the other policy is defined to override the default PII policy. Any column of any collection and dataset with the tag dataos:f:pii is visible to the user who has dataos:u:pii-reader tag.

5. For Filtering policies, Click on **Filter Policy**.

![governance-policies-filterpolicies.png](Getting%20policy%20details/governance-policies-filterpolicies.png)

The following information appears on the screen.

| Field | Description |
| --- | --- |
| Priority | Permission to access the resource |
| Depot | Name of the Depot |
| Collection | Name of the collection |
| Dataset | Name of the dataset |
| Name | Policy name |
| Formula | Formula for filter criterion |
| Users | Users or tags who has this policy applied |
| Desc | Short description of the policy defined |