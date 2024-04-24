# ABAC Implementation in DataOS

An access policy in DataOS defines permissions based on the ABAC authorization strategy. In ABAC (Attribute-based Access Control), the subject and objects of the policy are identified by their attributes. An attribute in Attribute-Based Access Control (ABAC) refers to any characteristic or property utilized to regulate access, with tags being a common attribute employed to identify subjects and objects. The attributes of both the subject and the object are defined and declared separately. 

Elements of Access Control in DataOS

| Term | Description | Example |
| --- | --- | --- |
| Subject | The user (application or person) who/which wants to perform a certain action | users:id:metis (tag identifying Metis application as the user)
users:id:iamgroot (tag identifying person with the name Iamgroot as the user) |
| Predicate | The action to be performed | get, put, post (other HTTP & CRUD operations) |
| Object | The entity on which the action is to be performed | dataos:resource:secret (the Secret resource-type as the object of the policy)
/metis/** (an API path as the object) |
| Tag | An attribute following a fixed glob pattern, as defined by its Tag-Namespace | dataos:layer:user
 or roles:id:operator |
| Tag-Namespace | A grouping or container for tags following the same glob pattern | roles:**
or  dataos:system:** |

## Tag-Namespace

A tag-namespace should be thought of as a container for tags. A specific glob pattern defines it. There are three categories of tag-namespaces in DataOS. The ones used to create tags to be assigned to subjects of an access policy, the ones that are to be assigned to the objects, and the ones that are used to convey non-mandatory information about the subject or object of the policy. 

Multiple tag namespaces are available. For example, the user tag namespace is `users:id:**`, similarly for  roles, `roles:id:**`

## Tags

Different types of users, as denoted logically by the tags assigned to them, will be attached to all the policies defined against those tags. You can use tags to conditionally allow policies based on whether a resource has a specific tag. For access policies, only those tags are allowed by Heimdall which have been categorized in a *Tag-Namespace.* Based on a particular use case, the system administrator can create all the requisite policies against a tag or a set of tags and apply them. 

For instance, if a particular user John Doe has tags:
`roles:id:data-dev` `roles:direct:metis` `users:id:testuser`

The policies created with the above-given tags as subjects will apply to John Doe.

<aside class="callout">
🗣 To remove the permissions, the policies must be deleted
</aside>

## Subject

The user (application or person) who/which wants to perform a certain action

The attribute of the *subject* of a policy is always identified by a *tag*. For instance, the tag for the user tag namespace is `users:id:**`, similarly for  roles, it’s `roles:id:**`

## Object

The object is a target resource on which the subject would like to perform actions. A tag or path identifies the object. You can specify multiple tags/paths.

The attribute of the *object* of a policy can be a tag or a path. For instance `users:id:depot-service` is the tag for object depot service  and `/ds/api/v3/**` is the path to the depot service

## Predicate

A predicate specifies whether an action is permitted or prohibited for the resource. While you present various potential actions in an array format, only one action will be taken at a time.

For instance, the following tables suggest possible actions in the `predicate` section.

**DataOS user:**

| Action | Description |
| --- | --- |
| create | Creates a new resource (for example dataset on a given path) |
| read | Read the data  |
| update | Update the data |
| delete | Delete the data  |

**DataOS Applications can perform API operations on resources:**

| Action | Description |
| --- | --- |
| get | Returns the resource(content/data) |
| post | Creates a new resource |
| put | Updates resources by replacing the resource information/content/data |
| patch | Modifies resource content |
| delete | Removes resource entirely |