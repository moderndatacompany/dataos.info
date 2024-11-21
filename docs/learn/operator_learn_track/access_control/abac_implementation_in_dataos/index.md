
# ABAC Implementation in DataOS

An Access Policy in DataOS defines permissions based on the ABAC authorization strategy. In ABAC (Attribute-based Access Control), the subject and objects of the policy are identified by their attributes. An attribute in Attribute-Based Access Control (ABAC) refers to any characteristic or property utilized to regulate access, with tags being a common attribute employed to identify subjects and objects. The attributes of both the subject and the object are defined and declared separately.


### **Tag-Namespace**

A tag-namespace is a grouping or container for tags that follow the same glob pattern. Tag-namespaces allow you to categorize tags for better organization and policy enforcement.

**Examples:**

- **`roles:`** – Namespace for roles, e.g., `roles:id:operator`
- **`dataos:system:`** – Namespace for system resources, e.g., `dataos:system:api`

There are three primary categories of tag-namespaces in DataOS:

- **Subject tags**: Tags assigned to users or applications (e.g., `roles:id:admin`, `users:id:metis`, `users:id:iamgroot`).
- **Object tags**: Tags assigned to resources (e.g., `dataos:resource:dataset`, `/api/v1/resource`).
- **Non-mandatory tags**: Tags that provide optional, informational data about subjects or objects (e.g., `dataos:info:location`).

### **Tag**

A tag is a specific attribute following a predefined glob pattern defined within its tag-namespace. Tags serve as identifiers for subjects, objects, and predicates.

For instance:

- **Subjects**: Tags for users or applications, such as `users:id:iamgroot` (identifying the user "Iamgroot") or `roles:id:developer` (identifying the "developer" role).
- **Objects**: Tags for resources or services, such as `dataos:resource:dataset` (identifying a dataset resource) or `/api/v1/metis/**` (identifying an API path).
- **Predicates**: Tags for actions like `read`, `write`, `delete`, or any CRUD (Create, Read, Update, Delete) operation.

### **Subject**

The subject refers to the user or application trying to perform an action. The subject is identified by a tag, typically associated with their role or identity.

**Examples:**

- `users:id:iamgroot`: Identifies the user "Iamgroot."
- `roles:id:data-scientist`: Identifies a role assigned to a set of users.

In DataOS, the subject must have appropriate tags assigned for the access control policies to be applied.

### **Object**

The object is the Resource on which the action is to be performed. This could be a dataset, application, API path, or any other resource. Objects are identified by tags or paths.

**Examples:**

- `dataos:resource:secret`: Identifies a resource of type "secret."
- `/api/v1/data/**`: Identifies an API path for accessing data.

The object's tag or path helps determine what resources can be acted upon by the subject.

### **Predicate**

A predicate specifies the action that the subject wants to perform on the object. Actions are typically CRUD or other HTTP operations such as `get`, `post`, `put`, `delete`, etc.

- **DataOS User Actions**:
    - `create`: Creates a new resource (e.g., a new dataset on a specific path).
    - `read`: Grants permission to read the data.
    - `update`: Updates the data.
    - `delete`: Deletes the data.
- **DataOS Application Actions** (API operations):
    - `get`: Retrieves the resource (content or data).
    - `post`: Creates a new resource.
    - `put`: Replaces an existing resource.
    - `patch`: Modifies a resource's content.
    - `delete`: Deletes a resource.

### **Example scenario**

Consider a scenario where you have the following tags for a user named Iamgroot:

- `roles:id:data-dev`:The user is assigned to the "data-dev" role.
- `users:id:iamgroot`: user tag to identify the user named "Iamgroot".

And the following path for a Depot:

- `dataos:resource:dataset` (Identifying a address of the Depot)

## Next step

Next, you create a Policy to provide appropriate permissions to user.

[Policy](/learn/operator_learn_track/access_control/policy/)