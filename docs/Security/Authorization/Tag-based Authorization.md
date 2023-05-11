# Tag-based Authorization

Within DataOS, administrators can easily change access rights to resources, applications, and APIs. This is done by providing a tag-based authorization framework where each tag gives the user access to perform specific actions on a specific part or user of the system. Every user (application or person) has an identity in DataOS. The user is granted access permissions based on this identity. 

The identity is recognized by our Policy Decision Point (Heimdall) based on the tags associated with it. These tags themselves are defined and created using various IAM policies. The Identity and Access Management (IAM) policies are stored as YAML documents. 

A policy within DataOS is a Resource that defines the permissions for a user (person or application) in the manner of a subject-predicate-object relationship. 

To learn more about creating such policies, refer to
[Policy](../../About%20DataOS/Primitives%20Resources/Policy.md).

As a DataOS user (person), it would help you to visualize the authorization framework to be broadly made up of two types of tags:

## Limited-access tags

These tags provide limited permissions to users (person) so that they can undertake specific actions on the components and applications of DataOS. They are always in the format:

`roles:id:<role name>`

The table given below lists all such tags which are available by default. 

| Tag | Description | Authorization | Explanation |
| --- | --- | --- | --- |
| roles:id:user | By default, this tag is assigned to all new users. It allows a minimum level of access to DataOS resources. | - To create, update and delete their own user profiles. <br> <br> - To read other user profiles. <br> <br> - To various API paths (access limited to specific API operations such as GET & POST) - precise details can be obtained by going through the Policies’ details on Operations Center. | In simple terms, the user can access DataOS GUI and perform ‘read’ action around most applications, for instance, the user will have permission to read depots. |
| roles:id:data-dev | Tag to provide access to the user layer of DataOS | - Authorization to a greater number of resources and components <br> <br> - To more API paths within the platform (nearly all API paths to components/resources in the User-layer). <br> <br> - To perform more API operations (including PUT & DELETE) on the servers connected via the above API paths- precise details can be obtained by going through the Policies’ details on Operations Center. | This is the tag you should assign to all the data developers in your organization. <br> <br> - User can perform CRUD operations on DataOS Resources in the User-layer (Depot, Workflow, Service, Database, Secret) <br> <br> - Perform CRUD operations within public & sandbox workspaces, as well as create new workspaces. <br> <br> - ‘Read’ access for cluster-level DataOS Resources (Depot, Compute, Policy). <br> <br> - As a consequence of the above set of authorizations, the user will be able to use various Stacks of DataOS (for instance create and run Flare jobs, Benthos service, etc.) <br> <br> - Can add or remove tags for other users with the same (or lower) authorization level, i.e. `roles:id:data-dev` and `roles:id:user` |
| roles:id:system-dev | Access to the system layer of DataOS | Authorization to work with workspaces in system-layer of DataOS | This tag allows the user to perform CRUD operations on resources in the System-layer |
| roles:id:operator | To become administrator of DataOS | Administrative level authorization | - This allows the user to perform all the API operations or predicates (CRUD, POST, PUT, PATCH, GET et. al.) on the paths <br>- Assign or remove tags of all the users. <br> - Make changes in the system files; access all resources in both user and system layers  |
| roles:id:pulsar-admin | To access pulsar | Authorizes the user to read, write and manage Pulsar | In simple terms, this tag allows the user to create, use and delete fastbase-type depot. A corollary is that you will need this tag to access services that use |

## Admin-level tags

These tags provide administrator-level permissions to a user for performing actions on a specific application. These tags are always in the format

`roles:direct:<application name>`

| Tag | Description | Authorisation | Explanation |
| --- | --- | --- | --- |
| roles:direct:metis | To become administrator of metis application |  |  |
| roles:direct:querybook | To become admin of the Querybook application |  |  |
| roles:direct:themis | To become admin of Themis application | Provides both read & write permissions to Themis | It is the default policy required to access & use Themis |

> 🗣️ Tags for Application
These tags authorize applications to interact with one another. There are numerous such tags within DataOS, but broadly you will come across two kinds: <br> - The tags which have the format `users:id:<application name>` are user-layer level tags; and <br> - Tags of the format `dataos:<application/resource type>:<application/resource name>` are system-layer level tags.

These allow or restrict the interactions between various applications, resources, and components of DataOS. An example of such a tag is `users:id:gateway`. This tag authorizes the Gateway application to access paths, resources, and other applications in DataOS. Likewise, the tag `dataos:layer:user` is used to refer to the components & resources in the User-layer of DataOS.

A tag `roles:id:app-user` is used to bundle certain applications together. When another application is assigned this tag, it can perform specific API operations on all the other applications in the bundle.

> Although it is not required, an administrator can create customized tags by applying an IAM policy within DataOS.