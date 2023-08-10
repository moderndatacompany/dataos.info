# Policy

Policy is a fundamental [Resource](../resources.md) in DataOS that defines a set of rules or guardrails governing the behavior of users, be it individuals or applications/services. Within DataOS, Policies are enforced using [Attribute Based Access Control (ABAC)](./policy/understanding_abac_pdp_and_pep.md#attribute-based-access-control-abac) and define what [predicates](./policy/understanding_abac_pdp_and_pep.md#predicate) a user (a [subject](./policy/understanding_abac_pdp_and_pep.md#subject)) can perform on a dataset, API Path, or a Resource (an [object](./policy/understanding_abac_pdp_and_pep.md#object)), thus defining the constraints of the relationship between the subject and object.

In DataOS, policies are expressed as a distinct [Resource](./) in a declarative YAML format. This approach allows for the separation of policies from application code, promoting modularity, easy maintenance, and reducing the need for extensive redeployment. Additionally, DataOS distinguishes between the [Policy Decision Point (PDP)](./policy/understanding_abac_pdp_and_pep.md#policy-decision-point-pdp) and the [Policy Enforcement Point (PEP)](./policy/understanding_abac_pdp_and_pep.md#policy-enforcement-point-pep). The PDP makes policy decisions based on predefined rules and attributes, while the PEP enforces these decisions, ensuring access control and compliance. This clear separation of concerns simplifies policy management, fostering scalability, extensibility, and maintainability in the DataOS ecosystem.

[Understanding ABAC, PDP and PEP](./policy/understanding_abac_pdp_and_pep.md)

## Types of Policies

DataOS offers two primary categories of policies: [Access Policy](#access-policy) and [Data Policy](#data-policy). These policies play essential roles in governing user access, actions, and data management within the DataOS system.

### **Access Policy**

Access Policies serve as the initial layer of defense, overseeing user access and actions within the system. They establish a set of well-defined rules that determine whether a user, known as the [subject](./policy/understanding_abac_pdp_and_pep.md#subject), is authorized to perform a specific action, referred to as a [predicate](./policy/understanding_abac_pdp_and_pep.md#predicate), on a given dataset, API path, or other resources, known as [objects](./policy/understanding_abac_pdp_and_pep.md#object). These policies serve as regulatory mechanisms, effectively governing user interactions and ensuring that access to specific actions is either granted or denied. This decision is based on the evaluation of attributes associated with the subjects and objects involved in the access request.

![Configuration of Access Policy](./policy/access_policy.png)

<center><i>Access Policy YAML configuration</i></center>

### **Data Policy**

In contrast, Data Policy operates as a secondary layer of control, regulating the visibility and interaction with specific data once access has been granted. It involves the implementation of techniques such as data masking or filtering to obscure or restrict the visibility of sensitive or restricted data based on predefined rules or conditions.

For example, when working with a dataset that includes a column labeled `credit_card_number`, it is crucial to protect the sensitive information it contains from unintended exposure. Employing data masking policies or applying data anonymization methods becomes essential to secure the contents of this specific column.

![Data Policy YAML configuration](./policy/data_policy.png)

<center><i>Data Policy YAML configuration</i></center>

Within Data Policy, we have two separate types one is the [Data Masking Policy](#data-masking-policy), and another is the [Data Filtering Policy](#data-filtering-policy). 

#### **Data Masking Policy**

Data masking policies are designed to protect sensitive information by replacing original data with fictitious yet structurally similar data. This ensures that the privacy of sensitive data is maintained while keeping the data useful for purposes such as testing and development. 

Data masking is particularly beneficial for Personally Identifiable Information (PII), where original data can be represented through masking, replacement with a placeholder (such as "####"), or obfuscation through a hash function.

Upon the application of a data masking policy, the original data is transformed, as illustrated in the sample example table below:

| Data Category | Original Value | Masked Value |
| --- | --- | --- |
| Email ID | john.smith\@gmail.com | bkfgohrnrtseqq85\@bkgiplpsrhsll16.com |
| Social Security Number (SSN) | 987654321 | 867-92-3415 |
| Credit Card Number | 8671 9211 3415 4546 | #### #### #### #### |

Such a policy ensures the protection of sensitive details, including but not limited to names, titles, addresses, etc.

You can apply the Mask policy, say to mask the column with ‘customer name’ in it, directly from the Metis UI via policy tags or via DataOS CLI by applying a YAML file. 

#### **Data Filtering Policy**

Data filtering policies establish parameters for determining which data elements should be accessible to various users or systems. Proper implementation of data filtering (or simply row filtering) policies ensures that only authorized individuals can access specific data segments.

For Example, in an e-commerce system, customer support agents may need access to customer order details. By applying a data filtering policy:

- Agent A can only view order records associated with customers they are assigned to.
- Agent B can only access order records for a specific geographic region.
- Agent C, as a supervisor, has unrestricted access to all order records.

With the data filtering policy in place, each agent can efficiently access the necessary information while maintaining data security and confidentiality.

## Creating a Policy

In DataOS, both access and data policies are configured via the singular Policy Resource. However, the two policy-types have their own YAML configuration and different underlying implementation.

### **YAML Configuration File**

#### **Resource Section Configuration**

To create a Policy YAML in DataOS, the initial step involves configuring the Resource Section in a YAML file. This section defines various properties of the Policy Resource. The following is an example YAML configuration for the Resource Section:

```yaml
name: {{my-policy}}
version: v1 
type: policy 
tags: 
  - {{dataos:type:resource}}
  - {{dataos:type:cluster-resource}}
description: {{This is a sample policy YAML configuration}} 
owner: {{iamgroot}}
layer: {{user}}
```
<center><i>Resource Section YAML configuration</i></center>

The `layer` field can have value either user/system in case of Policy. 

For policies that govern authorization for system level resources such as API Paths, `layer` is *system*, while for user `layer` authorization such as access to UDL addresses it is *user*.

Additionally, the Resource section offers various configurable fields, which can be explored further on this [link.](../resources/resource_grammar.md)



#### **Policy-specific Section Configuration**

The Policy-specific Section focuses on the configurations specific to the Policy Resource. Each Policy Resource-type has its own YAML syntax.

**Access Policy Syntax**

Access Policies are defined using a subject-predicate-object triad. The YAML syntax for an Access Policy is as follows:

```yaml
policy:
  access:
    subjects:
      tags:
        - {{roles:id:user}}
        - {{roles:id:pii-reader}}
    predicates:
      - {{read}}
    objects:
      <tags/paths>:
        - {{tag/path}}
    allow: {{true}}
```
<center><i>Policy-specific Section YAML configuration (Access Policy Syntax)</i></center>

The table below summarizes varioues attributes/fields within the access policy YAML.

<center>

| Field | Data Type | Default Value | Possible Value | Requirement |
| --- | --- | --- | --- | --- |
| [`policy`](./policy/policy_specific_section_grammar.md#policy) | object | none | none | mandatory |
| [`access`](./policy/policy_specific_section_grammar.md#access) | object | none | none | mandatory |
| [`subjects`](./policy/policy_specific_section_grammar.md#subjects) | object | none | none | mandatory |
| [`tags`](./policy/policy_specific_section_grammar.md#tags) | list of strings | none | a valid DataOS tag | mandatory |
| [`predicates`](./policy/policy_specific_section_grammar.md#predicates) | list of strings | none | http or crud operations | mandatory |
| [`objects`](./policy/policy_specific_section_grammar.md#objects) | object | none | none | mandatory |
| [`paths`](./policy/policy_specific_section_grammar.md#paths) | list of strings | none | api paths, udl paths | mandatory |
| [`allow`](./policy/policy_specific_section_grammar.md#allow) | boolean | false | true/false | optional |

</center>

Here, the `subject` represents the user, the `object` denotes the target (such as an API path or resource) that the user interacts with, and the `predicate` represents the action performed. The `allow` field determines whether the policy grants or restricts access for the user to perform the specified action on the designated object. Refer to the [Policy Section-specific Grammar](./policy/policy_specific_section_grammar.md) for more details on configuring subjects, predicates, and objects.

**Data Policy Syntax**

A data policy is defined using the following YAML syntax:

```yaml
policy:
  data:
    dataset: {{dataset name}}
    collection: {{collection name}}
    depot: {{depot name}}
    priority: 90
    selector:
      user:
      tags:
        - {{roles:id:user}}
      column:
        {}
    type: {{filter/mask}}
    <filter/mask>:
      {{masking or filtering specific attributes/fields}}
```
<center><i>Policy-specific Section YAML configuration (Data Policy Syntax)</i></center>

The table below summarizes the various attributes/fields within a data policy YAML.

<center>

| Field | Data Type | Default Value | Possible Value | Requirement |
| --- | --- | --- | --- | --- |
| [`policy`](./policy/policy_specific_section_grammar.md#policy) | object | none | none | mandatory |
| [`data`](./policy/policy_specific_section_grammar.md#data) | object | none | none | mandatory |
| [`depot`](./policy/policy_specific_section_grammar.md#depot) | string | none | any valid depot name or regex pattern | optional |
| [`collection`](./policy/policy_specific_section_grammar.md#collection) | string | none | any valid collection name or regex pattern | optional |
| [`dataset`](./policy/policy_specific_section_grammar.md#dataset) | string | none | any valid dataset name or regex pattern | optional |
| [`priority`](./policy/policy_specific_section_grammar.md#priority) | number | none | 0-100 | mandatory |
| [`selector`](./policy/policy_specific_section_grammar.md#selector) | object | none | none | mandatory |
| [`user`](./policy/policy_specific_section_grammar.md#user) | object | none | none | mandatory |
| [`tags`](./policy/policy_specific_section_grammar.md#tags) | list of strings | none | a valid DataOS tag | mandatory |
| [`column`](./policy/policy_specific_section_grammar.md#column) | object | none | true/false | optional |
| [`name`](./policy/policy_specific_section_grammar.md#column) | list of strings | none | valid column name | optional |
| [`type`](./policy/policy_specific_section_grammar.md#type) | string | none | mask/filter | mandatory |
| [`filter/mask`](./policy/policy_specific_section_grammar.md#type) | object | none | none | mandatory |

</center>


For detailed information on configuring the YAML file for a Data Policy, refer to the following [link](./policy/policy_specific_section_grammar.md).



### **Applying the YAML File**

After creating the YAML configuration file for the Policy resource, it's time to apply it to instantiate the resource in the DataOS environment. To apply the Policy YAML file, utilize the `apply` command.

```shell
dataos-ctl apply -f {{yaml-file-path}}
```

## Policy Implementation Mechanism

In the DataOS ecosystem, the **Heimdall** governance engine operates as the Policy Decision Point (PDP) for Access Policies, while the **Minerva Gateway** serves as the PDP for Data Policies. Both these elements jointly supervise the enforcement of policies across a range of Policy Enforcement Points (PEP), distributed throughout the DataOS ecosystem. Learn more about Policy implementation in DataOS, [here.](./policy/implementation_of_data_and_access_policy.md)

## Policy Configuration Templates

In this section, a collection of pre-configured Policy Resource Templates are provided, tailored to meet the requirements of different scenarios. To know more navigate to the following [link](./policy/policy_configuration_templates.md)

## Case Scenarios

For detailed examples and practical implementations of Policy Resource, refer to the following Policy Resource Case Scenarios:

[Implementing Access Policy](./policy/case_scenarios/implementing_access_policy.md)

[Implementing Data Masking Policy](./policy/case_scenarios/implementing_data_masking_policy.md)

[Implementing Data Filtering Policy](./policy/case_scenarios/implementing_data_filtering_policy.md)