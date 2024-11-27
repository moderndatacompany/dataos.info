# Access Management

Learn how DataOS manages access control through policies that define who can access resources and perform specific actions. This module covers key concepts like Policy Decision Point (PDP), Policy Enforcement Point (PEP), and the Bifrost GUI, which simplifies creating and managing access policies. You'll also explore how authentication and authorization work together to secure DataOS environments, ensuring resources are accessible only to authorized users, services, and applications.

## Scenario

As a DataOS operator, you’re responsible for securing access to critical resources. You must ensure users and services have the necessary permissions to perform their roles while minimizing risks. Using DataOS’s dynamic policies and the Bifrost interface, you define precise access controls that protect sensitive data.

## Overview

Access control management in DataOS controls who can access specific resources and what actions they can perform. It is governed by policies that define access rights and conditions. By defining and enforcing these policies, you can ensure that only authorized entities interact with your resources, thereby maintaining a secure DataOS environment. DataOS enforces a default deny by denying all actions unless explicitly allowed. It also follows the least privilege principle by creating fine-grained policies providing only the minimal access necessary for each user, role, or service. Policies are dynamically evaluated and enforced to ensure proper access control.

## Authentication

Before any user or application can access DataOS resources, they must authenticate. Authentication in DataOS is managed through OIDC-compliant identity providers, which verify users' and applications' identities. DataOS integrates with third-party OIDC-compliant identity providers, allowing customers to use their existing identity management systems for authentication. This enables seamless authentication workflows and centralized user management.

When users or applications log in to DataOS, the platform communicates with the external identity provider to authenticate them. Upon successful authentication, the identity provider issues a token that DataOS uses to grant the user or application access to the platform.

You have been tasked to add a new employee to the respective Identity Management System used in your organization. Use the any of the following guide to do the same.

- [Adding Users in Azure AD](/learn/operator_learn_track/access_control/authentication/adding_user_in_azure_ad/): Learn how to add and manage users in Azure AD for use with DataOS.
- [Adding Users in Keycloak](/learn/operator_learn_track/access_control/authentication/adding_user_in_keycloak/): Follow this guide to add users in Keycloak and integrate them with DataOS.


## Authorization

Once users have been authenticated, the next critical step for a DataOS operator is to ensure that each user has the appropriate level of access to resources, based on their role. This is achieved by implementing the correct Access Policies. Before proceeding with the creation of these policies, it is essential to understand the underlying strategy employed by DataOS for policy management.

To gain a comprehensive understanding of DataOS's approach to access control, familiarize yourself with the Attribute-Based Access Control (ABAC) strategy:

- Learn more about ABAC in DataOS: [ABAC Implementation in DataOS](/learn/operator_learn_track/access_control/abac_implementation_in_dataos/)

Once you have developed a thorough understanding of the ABAC framework, you can proceed with the implementation of the Access Policy:

- Implementing the Policy: [Policy](/learn/operator_learn_track/access_control/policy/)


## Bifrost

In DataOS, access control is managed using Attribute-Based Access Control (ABAC), which gives fine-grained control over who can access resources. However, creating and managing these policies can be complex, especially when there are many Users, Roles, and Resources to manage. To make this easier, DataOS provides Bifrost, a Graphical User Interface (GUI) that simplifies the process of creating, updating, and enforcing access control policies. Bifrost presents a role-based interface, which is easier to understand and manage. Administrators can define policies based on roles, making it simpler to assign access rights. While Bifrost looks role-based, it still uses the underlying ABAC system to ensure access control is fine-tuned and flexible.

Bifrost organizes key access control concepts into the following components:

- [Users](/learn/operator_learn_track/access_control/users/): In DataOS, a user can be a person or an application. 
    
- [Roles](/learn/operator_learn_track/access_control/roles/): Roles group users who need the same level of access to resources. 
    
- [Use-cases](/learn/operator_learn_track/access_control/use_cases/): This defines the specific action a user wants to perform on a resource. Use cases are combinations of objects and predicates.
    
- [Grants](/learn/operator_learn_track/access_control/grants/): Grants link a subject (user) to a Use-case, defining the subject's access permissions to a specific resource.

- [Grant Requests](/learn/operator_learn_track/access_control/grant_requests/): In Bifrost, users can initiate a grant request if they want additional access permissions.

