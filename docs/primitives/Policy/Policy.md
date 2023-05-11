# Policy

DataOS Policy is a rule defining what tags are associated with subjects, predicates, other tags, or paths associated with objects, and additional conditions on metadata to allow or deny access to DataOS resource/environment. This allows a very flexible approach to policy definition, that complements the ever-changing set of subjects and objects in enterprises.

With attribute-based access control(ABAC), DataOS makes policy decisions using the attributes of users, objects, and actions involved in the request. 

## Types of Policies

There are two types of policies in DataOS- Access and Data policies, and both are managed through the primitive named “Policy.”

### Access Policy

Access policy is a security measure regulating individuals who can view, use, or access a restricted DataOS environment/resource.

The Access policy type is implemented using an Attribute-Based Access Control paradigm. More specifically, we leverage the attribute tags of Subjects and the attribute tags or paths of Objects to evaluate a set of policies when determining if a specific Predicate (action) should be allowed or denied. For example, based on the Policy (given in the YAML below), a user with the tag `roles:id:testuser` can read secrets or specific Depots to connect to data.

An access policy has three main components:

<center>

![Access policy to allow read access for specific depot](./MicrosoftTeams-image_(111).png)

</center>

<figcaption align = "center">Access policy to allow read access for specific depot</figcaption>

<br>

To learn how Access Policies are created refer to the [Creating Policies](./Policy.md) page. 

### Data Policy

Data policies are a collection of statements that describe the rules controlling the integrity, security, quality, and use of data during its lifecycle and state change. You can create data policies to guide what data the user sees once they access a dataset.

You can set up data policies in the following two ways:

- Global - covers all the columns based on tags. Will only support column masking.
- Local - covers columns of a specific dataset. Will support column masking and row-level filters.

These policies selectively mask/filter data and provide multiple views for users and groups based on their access and visibility rules.

#### Masking Policy

A data masking policy defines the logic that replaces (masks) the original sensitive data with fictitious data to maintain the privacy of sensitive data. For example, PII data can be shown with an appropriate mask, replaced with a "####" string, or with some hash function.

The following examples show what the masked data might look like after the masking policy is applied.

| Type | Original Value | Masked Value |
| --- | --- | --- |
| Email ID | john.smith@gmail.com | bkfgohrnrtseqq85@bkgiplpsrhsll16.com |
| SSN | 987654321 | 867-92-3415 |
| Credit card number | 8671 9211 3415 4546 | #### #### #### #### |

#### Masking Strategies

Masking strategies can be defined in the YAML files and applied. These strategies may be simple or complex depending on the information security needs of the organization. 

To learn more about creating masking policy go to this link: [Creating Policies](./Policy.md). 

Here is a list of operators/rules through which you can define masking definitions.

Here is an example of a data policy that masks the personal information in a dataset. A data policy has the following main components:

<center>


![Data policy to mask personal identification information](./MicrosoftTeams-image_(110).png)

</center>

<figcaption align = "center">Data policy to mask personal identification information</figcaption>
<br>

#### Filtering Policy

The filtering policy constrains data visibility for end users. You can define a policy to remove rows from the query's result set based on comparison operators set on a column, such as some users cannot see ' Florida' region data. Filter policy can be defined in the YAML file and applied at the time of the query. To create filtering policies, click [Creating Policies](./Policy.md).

## Policy Execution

Whenever a user tries to perform a predicate(action) on a particular object from a service or a system, that particular service can leverage the authorization service to authorize this action and enforce the authorization decisions. DataOS implements unique Policy Decision Point(PDP) and Policy Execution Point(PEP) services based on tags associated with Subjects and Objects. 

To learn more, click here:
[PDP and PEP](./PDP%20and%20PEP/PDP%20and%20PEP.md).

## Creating Policies

DataOS establishes policies to define which combinations of user/ subject/ environmental attributes are needed to perform an action with an object/resource. You can write such policies to grant and deny access.

The YAML tags field in both subjects and objects is an array of string arrays. The following page has rules that will help you to define required expressions:
[Rules for AND/OR Logic](./Rules%20for%20AND%20OR%20Logic.md).

While creating a policy in the YAML file, provide various configuration properties, set permissions, and then create that “Policy” object using the `apply` command in CLI.

To learn more about creating a DataOS policy, refer to the following pages:

- [Creating Access Policy](./Creating%20Access%20Policy.md)

- [Creating Data Policy (Masking)](./Creating%20Data%20Policy%20(Masking).md)

- [Creating Data Policy (Filtering)](./Creating%20Data%20Policy%20(Filtering).md)

You can also refer to the use case for a step-by-step guide demonstrating the policy creation process in the
[Policy Implementation Use Case](./Policy%20Implementation%20Use%20Case/Policy%20Implementation%20Use%20Case.md) page.