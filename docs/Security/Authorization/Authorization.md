# Authorization

### Attribute-Based Access Control(ABAC)

DataOS uses an attribute-based authorization model to grant or deny access to DataOS resources. Attributes are the characteristics or values of a component involved in an access event. 

> In DataOS, attributes are called Tags.

Access decisions are made based on attributes/tags about the subject or user making the access request, the resource being requested, and what action the user wants to perform with the resource. Resources are the applications, application operations, and data within DataOS. 

### Role-Based Access Control(RBAC)

Role-Based Access Control is a security paradigm whereby users are granted access to resources based on their role in the company. It involves grouping users and entitlements according to business functions or activities. 

ABAC enables the extension of the existing roles via attributes and policies. DataOS maps the role to a set of permissions — i.e., what the role is allowed to do. Attributes can be grouped to offer the context needed to make intelligent authorization decisions for a given role.

> DataOS implements ABAC in two layers – Access Policies and Data Policies. To learn more about DataOS Policies, refer to [Policy](../About%20DataOS/Primitives%20Resources/Policy.md).

Heimdall is the DataOS component that is the source of truth for all Access policy decisions. Tags /attributes-based policies are easy to build and understand. At run time, all other components communicate with it to get the required access to the enterprise data based on tags.  

To learn more about how users can access DataOS resources and perform actions with various tags, refer to
[Tag-based Authorization](Authorization/Tag-based%20Authorization.md).