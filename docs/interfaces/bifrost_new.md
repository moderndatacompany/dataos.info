# Bifrost

Bifrost is a Graphical User Interface that enables you to create and manage access policies for applications, services, people & datasets. It is backed by the governance engine of DataOS, [Heimdall](../architecture.md#heimdall).

All policies in DataOS are implemented as [ABAC](../interfaces/bifrost_new/abac_implementation_in_dataos.md)
 (Attribute Based Access Control) policies, giving users fine-grained control over all aspects of the operating system and their data landscape. To make the user interface intuitive, Bifrost appears to follow RBAC, but underneath it is still ABAC implementation of access control. The following page explains in detail how this framework is implemented in DataOS click [here](../interfaces/bifrost_new/abac_implementation_in_dataos.md).


<aside class="callout">

    🗣 Using Bifrost requires operator-level permissions; in other words, the `roles:id:operator` tag must be assigned to the user. All other users will have ‘view-only’ permission.

</aside>

## How does Bifrost work?

DataOS enforces a zero default denial stance, requiring users must explicitly request access to perform any action within the system. It establishes a continuous authorization mechanism, where access permissions are dynamically evaluated each time a user attempts an action. Access is granted only if the user has the requisite permissions at that precise moment. Bifrost is a tool to implement this philosophy,  backed by Heimdall, the governance engine of DataOS implementing Attribute-Based Access Control (ABAC).

Understanding how Bifrost works involves focusing on key concepts that are defined as followings:

## User

An application or a person can serve as a User. Consider the User as the [subject](./bifrost_new/abac_implementation_in_dataos.md#subject) of the ABAC policy. Get the details of  'User' in Bifrost from [here](../interfaces/bifrost_new/users.md).

## Use-cases

A use case in Bifrost defines actions a user wants to perform on a specific [object](./bifrost_new/abac_implementation_in_dataos.md#object). Get the details of how use cases are created and assigned [here](../interfaces/bifrost_new/use_cases.md).

## Grant

A grant is how the Subject-Predicate-Object is linked, and an access policy is generated. This is where you assign use-cases to users, giving them access to specific parts of the system or data. Get the details of Grants [here](../interfaces/bifrost_new/grants.md).

## Role

While the ability to grant specific Use-Cases to individual users is necessary for fine-grained access control, it is pragmatic to be able to group these users. We call these groups Roles. To know more about Roles click [here](../interfaces/bifrost_new/roles.md).

## Grant Requests

The Grant Request section in Bifrost streamlines the process of managing access permissions requests. Users can initiate grant requests through the Bifrost UI or via [CLI](../interfaces/cli.md), detailing their desired access permissions. Administrators track pending requests, prioritize responses, and meticulously review details before approving or rejecting requests in alignment with organizational policies and security requirements. To know more about Grant Requests click [here](../interfaces/bifrost_new/grant_requests.md).

## How does Heimdall facilitate authorization?

[Objects](./bifrost_new/abac_implementation_in_dataos.md#object) represent resources exposed by the system or applications/services running on top of it, identified by either a path or a set of tags. When a user attempts to execute a [predicate](./bifrost_new/abac_implementation_in_dataos.md#predicate) on an object within a service or system, Heimdall can be utilized to authorize this action. This interaction pattern is elucidated through understanding PDP and PEP.

**Policy Decision Point (PDP)**

True to its name, the Policy Decision Point (PDP) is responsible for making policy decisions. It maintains a data structure comprising all the policies and provides an API that receives a user token (to ascertain the subject), the predicate being requested, and the target object. Based on existing policies, it responds by either granting or refusing permission.

**Policy Enforcement Point (PEP)**

A Provider or Policy Enforcement Point (PEP) signifies the service at the point of access. Upon being accessed, it interacts with the Policy Decision Point (PDP), providing it with the necessary information to authorize the current context. Depending on the response received from the PDP, the PEP either permits or denies the user's intended action. For instance, when information enters the system, the proxy verifies if certain API paths are allowed or blocked. If the Policy Decision Point (PDP) indicates denial, the proxy decides not to forward the request.

## Heimdall Primitives

Heimdall primitives are components of the Heimdall, the authentication, authorization, and governance engine within DataOS. This section provides access to various primitives and configurations related to access control and security. To know more click [here](./bifrost_new/heimdall_primitives.md)

### **Policies**

DataOS [Policy](../resources/policy.md) within Heimdall Primitives is a rule defining the association of tags with subjects, predicates, other tags, or paths linked with objects to allow or deny access. Additionally, it imposes specific conditions on metadata, thereby governing access permissions to DataOS resources and environments.

### **Tag-Namespaces**

A Tag-Namespace is a container or group of tags. For instance `roles:**`is a container or group for different tags starting with "roles" like `roles:id:system-dev` or `roles:id:pii-reader`. Tag-Namespaces are organized into three distinct categories serving specific purposes. One category is for creating tags assigned to subjects within an access policy. Another category is designated for tags assigned to objects in the policy. Lastly,  is a category employed for conveying non-mandatory information about either the subject or object involved in the policy.

During the installation of DataOS, system tags, and default policies are generated to facilitate core functionality. These tags encompass the following predefined Tag-Namespaces by default:

- `users:**`
- `roles:**`
- `dataos:workspace:**`
- `dataos:system:**`

However, these are not the exclusive tags created during the installation process.

<aside class="callout">
🗣 New tag namespaces can be created to mimic the organizational structure for a particular use case.
</aside>

#### **How to create a Tag-Namespace?**

To create a Tag-Namespace, four fields need to be specified. These fields, along with their descriptions and examples, are outlined in the table below:

| Fields | Description | Example |
| --- | --- | --- |
| Name | declare a name for the Tag-Namespace  | test namespace |
| GLOB | define its glob pattern | `test:**` |
| Type | depending on how the tags in this group will be used, declare one of these three values: subject/object/inform  | subject |
| Description | describe in short the purpose for which the tags in this namespace will be created | Tag-Namespace created specifically to create test-roles for users |

For instance, let’s create a new tag group called `testers`

To create a new Tag-Namespace Open Bifrost navigate to Heimdall Primitives

- Click on Tag-Namespace
- Now click on create Tag-Namespace button

<center>![tag_namespace.png](../interfaces/bifrost_new/tag_namespace.png)</center>
<center>users will be directed to a page where all existing Tag-Namespaces are listed 
</center>

- The Tag-Namespace will be configured with the following details, as depicted in the figure below:

  - Name: tester
  - GLOB: tester:**
  - Type: subject
  - Description: tester group

![tag_namespace_config.png](../interfaces/bifrost_new/tag_namespace_config.png)

- A success message will be displayed confirming that the new Tag-Namespace has been added successfully. 

### **Tags**

A tag is an attribute following a fixed glob pattern, as defined by its Tag-Namespace. The tag can be of two types subject or object. For instance, `dataos:layer:system` is a object type tag and `users:id:iamgroot` is a subject type tag.

 Under the "**Tags**" section, users can access a list of tags organized as follows:

![list_of_tags.png](../interfaces/bifrost_new/list_of_tags.png)

<!-- 
**How  to create a Tag?**

When creating tags, it's crucial to note that each tag is within a specific tag-namespace, preventing the creation of random or unstructured tags within the system. -->

### **Collections**

The diagram below summarizes how you can provide access through Bifrost.

![bifrost.png](../interfaces/bifrost_new/Bifrost.png)

