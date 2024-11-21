# Access Control

In this module, you will learn the basic concepts and components of DataOS Policy and how DataOS uses Bifrost, a GUI, to create and manage access policies for applications, services, people & datasets. Additionally, you will learn about two critical concepts in access control: Policy Decision Point (PDP) and Policy Enforcement Point (PEP). These concepts are crucial for understanding how DataOS Policies are processed and how access is granted or denied.

## Scenario

Imagine you are a DataOS operator tasked with managing access control in a large organization. Your role involves ensuring that users, applications, and services can access the resources they need, while maintaining security and minimizing risks by enforcing strict policies.

## Introduction

Access management in DataOS controls who can access specific resources and what actions they can perform. It is governed by policies that define access rights and conditions. By defining and enforcing these policies, you can ensure that only authorized entities interact with your resources, thereby maintaining a secure DataOS environment.

DataOS enforces a default deny by denying all actions unless explicitly allowed. It also follows the least privilege principle by creating fine-grained policies providing only the minimal access necessary for each user, role, or service. Policies are dynamically evaluated and enforced to ensure proper access control.

### **Authentication**

Before any user or application can access DataOS resources, they must authenticate. Authentication in DataOS is managed through OIDC-compliant identity providers, which verify users' and applications' identities. DataOS integrates with third-party OIDC-compliant identity providers, allowing customers to use their existing identity management systems for authentication. This enables seamless authentication workflows and centralized user management.

When users or applications log in to DataOS, the platform communicates with the external identity provider to authenticate them. Upon successful authentication, the identity provider issues a token that DataOS uses to grant the user or application access to the platform.

You have been tasked to add a new employee to the respective Identity Management System used in your organization. Use the any of the following guide to do the same.

- [Adding Users in Azure AD](/learn/operator_learn_track/access_control/authentication/adding_user_in_azure_ad/): Learn how to add and manage users in Azure AD for use with DataOS.
- [Adding Users in Keycloak](/learn/operator_learn_track/access_control/authentication/adding_user_in_keycloak/): Follow this guide to add users in Keycloak and integrate them with DataOS.


### **Authorization**

The next step is authorization, which determines what actions an authenticated user or application can perform. Access Control are the rules that govern this process, defining what users or applications can do with specific resources within DataOS.

Now that users are authenticated, as a DataOS operator, your next step is to ensure that each user has the correct access to resources based on their role. This requires implementing the appropriate Access Policy. Before you create these policies, it's essential to understand the strategy that DataOS uses for policy implementation.

Learn more about the ABAC (Attribute-Based Access Control) strategy used in DataOS:

[ABAC Implementation in DataOS](/learn/operator_learn_track/access_control/abac_implementation_in_dataos/)


[Policy](/learn/operator_learn_track/access_control/policy)


### **Bifrost**

In DataOS, access control is managed using Attribute-Based Access Control (ABAC), which gives fine-grained control over who can access resources. However, creating and managing these policies can be complex, especially when there are many users, roles, and resources to manage. To make this easier, DataOS provides Bifrost, a Graphical User Interface (GUI) that simplifies the process of creating, updating, and enforcing access control policies.

Bifrost presents a role-based interface, which is easier to understand and manage. Administrators can define policies based on roles, making it simpler to assign access rights. While Bifrost looks role-based, it still uses the underlying ABAC system to ensure access control is fine-tuned and flexible.

Bifrost organizes key access control concepts into the following components:

- **User**: In DataOS, a user can be a person or an application. The user is a subject in the access control system and is identified by a tag.
    
[Users](/learn/operator_learn_track/access_control/users/)
    
- **Role**: Roles group users who need the same level of access to resources. For example, all data scientists in an organization might share the same role, allowing them to access the same datasets and perform similar actions.
    
[Roles](/learn/operator_learn_track/access_control/roles/)
    
- **Use case**: This defines the specific action a user wants to perform on a resource (e.g., `view dataset,` `edit dataset,` etc.). Use cases are combinations of objects and predicates.
    
[Use-cases](/learn/operator_learn_track/access_control/use_cases/)
    
- **Grant**: Grants link a subject (user) to a Use-Case, defining the subject's access permissions to a specific resource. For example, a grant might allow Iamgroot to view a specific dataset.

[Grants](/learn/operator_learn_track/access_control/grants/)

- **Grant Request**: In Bifrost, users can initiate a grant request if they want additional access permissions.

[Grant Requests](/learn/operator_learn_track/access_control/grant_requests/)