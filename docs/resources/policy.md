---
title: Policy
search:
  boost: 2
---

# :resources-policy: Policy

Policy is a [Resource](../resources.md) in DataOS that defines a set of rules or guardrails governing the behavior of users, be it individuals or applications/services. Within DataOS, Policies are enforced using [Attribute Based Access Control (ABAC)](./policy/understanding_abac_pdp_and_pep.md#attribute-based-access-control-abac) and define what [predicates](./policy/understanding_abac_pdp_and_pep.md#predicate) a user (a [subject](./policy/understanding_abac_pdp_and_pep.md#subject)) can perform on a dataset, API Path, or a Resource (an [object](./policy/understanding_abac_pdp_and_pep.md#object)), thus defining the constraints of the relationship between the subject and object.

The Policy Resource operates on "never trust, always verify" ethos. It enforce a default denial stance, requiring  users must explicitly request access to perform any action within the system. It establishes a continuous authorization mechanism, where access permissions are dynamically evaluated each time a user attempts an action. Access is granted only if the user has the requisite permissions at that precise moment.

In DataOS, a Policy is expressed as a distinct [Resource](./) in a declarative YAML format. This approach allows for the separation of policies from application code, promoting modularity, easy maintenance, and reducing the need for extensive redeployment. Additionally, DataOS distinguishes between the [Policy Decision Point (PDP)](./policy/understanding_abac_pdp_and_pep.md#policy-decision-point-pdp) and the [Policy Enforcement Point (PEP)](./policy/understanding_abac_pdp_and_pep.md#policy-enforcement-point-pep). The PDP makes policy decisions based on predefined rules and attributes, while the PEP enforces these decisions, ensuring access control and compliance. This clear separation of concerns simplifies policy management, fostering scalability, extensibility, and maintainability in the DataOS ecosystem.



<div class="grid cards" markdown>

-   :material-card-bulleted-settings-outline:{ .lg .middle } **Types of Policy in DataOS**

    ---

    Explore various policy types within the DataOS platform comprehensively.

    [:octicons-arrow-right-24: Types of Policies](#types-of-policies)


-   :material-list-box-outline:{ .lg .middle } **How to create and manage a Policy?**

    ---

    Learn how to create and manage a Policy in DataOS.

    [:octicons-arrow-right-24: Create and manage Policy](#creating-a-policy)

-   :material-network-pos:{ .lg .middle } **Policy Configuration Templates**

    ---

    Enhance Policy management with Configuration Templates
    
    [:octicons-arrow-right-24: Policy Templates ](#policy-configuration-templates)

-   :material-content-duplicate:{ .lg .middle } **Policy Implementation**

    ---

    Explore a detailed walkthrough to implement Policy

    [:octicons-arrow-right-24: Hands on Guide](#case-scenarios)

</div>


[Understanding ABAC, PDP and PEP](./policy/understanding_abac_pdp_and_pep.md)

## Types of Policies

DataOS offers two primary categories of policies: [Access Policy](#access-policy) and [Data Policy](#data-policy). These policies play essential roles in governing user access, actions, and data management within the DataOS system.

=== "Access Policy"

    Access Policies serve as the initial layer of defense, overseeing user access and actions within the system. They establish a set of well-defined rules that determine whether a user, known as the [subject](./policy/understanding_abac_pdp_and_pep.md#subject), is authorized to perform a specific action, referred to as a [predicate](./policy/understanding_abac_pdp_and_pep.md#predicate), on a given dataset, API path, or other resources, known as [objects](./policy/understanding_abac_pdp_and_pep.md#object). These policies serve as regulatory mechanisms, effectively governing user interactions and ensuring that access to specific actions is either granted or denied. This decision is based on the evaluation of attributes associated with the subjects and objects involved in the access request.

    ![Configuration of Access Policy](./policy/access_policy.png)

    <center><i>Access Policy YAML configuration</i></center>

=== "Data Policy"

    In contrast, Data Policy operates as a secondary layer of control, regulating the visibility and interaction with specific data once access has been granted. It involves the implementation of techniques such as data masking or filtering to obscure or restrict the visibility of sensitive or restricted data based on predefined rules or conditions.

    For example, when working with a dataset that includes a column labeled `credit_card_number`, it is crucial to protect the sensitive information it contains from unintended exposure. Employing data masking policies or applying data anonymization methods becomes essential to secure the contents of this specific column.

    ![Data Policy YAML configuration](./policy/data_policy.png)

    <center><i>Data Policy YAML configuration</i></center>

    Within Data Policy, we have two separate types one is the [Data Masking Policy](#data-masking-policy), and another is the [Data Filtering Policy](#data-filtering-policy). 

    === "Data Masking Policy"

        Data masking policies are designed to protect sensitive information by replacing original data with fictitious yet structurally similar data. This ensures that the privacy of sensitive data is maintained while keeping the data useful for purposes such as testing and development. 

        Data masking is particularly beneficial for Personally Identifiable Information (PII), where original data can be represented through masking, replacement with a placeholder (such as "####"), or obfuscation through a hash function.

        Upon the application of a data masking policy, the original data is transformed, as illustrated in the sample example table below:

        | Data Category | Original Value | Masked Value |
        | --- | --- | --- |
        | Email ID | john.smith\@gmail.com | bkfgohrnrtseqq85\@bkgiplpsrhsll16.com |
        | Social Security Number (SSN) | 987654321 | 867-92-3415 |
        | Credit Card Number | 8671 9211 3415 4546 | #### #### #### #### |

        Such a policy ensures the protection of sensitive details, including but not limited to names, titles, addresses, etc.

        You can apply the Mask policy, say to mask the column with ‘customer name’ in it, directly from the [Metis UI](../interfaces/metis.md) via policy tags or via [DataOS CLI](../interfaces/cli.md) by applying a YAML file. 

    === "Data Filtering Policy"

        Data filtering policies establish parameters for determining which data elements should be accessible to various users or systems. Proper implementation of data filtering (or simply row filtering) policies ensures that only authorized individuals can access specific data segments.

        For Example, in an e-commerce system, customer support agents may need access to customer order details. By applying a data filtering policy:

        - Agent A can only view order records associated with customers they are assigned to.
        - Agent B can only access order records for a specific geographic region.
        - Agent C, as a supervisor, has unrestricted access to all order records.

        With the data filtering policy in place, each agent can efficiently access the necessary information while maintaining data security and confidentiality.

## How to create and manage a Policy

In DataOS, both access and data policies are configured via the singular Policy Resource. However, the two policy-types have their own YAML configuration and different underlying implementation.

### **Create a Policy manifest**

To create a Policy, the first step is to create a Policy manifest file. A sample Policy manifest is given below:


???note "Example Policy manifest"

    === "Access Policy"

        ```yaml
        # Resource meta section (1)
        name: myaccesspolicy
        version: v1 
        type: policy 
        tags: 
          - access_policy
        description: This is a sample policy YAML configuration 
        owner: iamgroot
        layer: user

        # Policy specific section (2)
        policy:
          access:
            subjects:
              tags:
                - roles:id:user
                - roles:id:pii-reader
            predicates:
              - "read"
            objects:
              paths:
                - "dataos://icebase:retail/city"
            allow: true
        ```
                         
        1.  [Resource meta section](#resource-meta-section) within a manifest file comprises metadata attributes universally applicable to all [Resource-types](/resources/types_of_dataos_resources/). To learn more about how to configure attributes within this section, refer to the link: [Attributes of Resource meta section](/resources/resource_attributes/).

        2.  [Policy-specific section](#policy-specific-section) within a manifest file comprises attributes specific to the Policy Resource. This section is different for Access and Data Policy .To learn more about how to configure attributes of Policy-specific section, refer to the link: [Attributes of Policy manifest](/resources/policy/yaml_configuration_attributes/).

    === "Data Policy"

        === "Filter"

            ```yaml
            name: mydatapolicy
            version: v1 
            type: policy 
            tags: 
              - policy
            description: This is a sample policy YAML configuration
            owner: iamgroot
            layer: user
            policy:
              data:
                type: filter
                name: "filtericebasecity"
                description: 'data policy to filter data on zip code'
                dataset_id: "icebase.retail.city"
                priority: 1
                selector:
                  user:
                    match: all
                    tags:
                      - "users:id:aayushisolanki"
                filters:
                  - column: city_name
                    operator: equals
                    value: "Verbena"
            ```
        === "Masking"
        
            ```yaml
            name: bucketage
            version: v1
            type: policy
            layer: user
            description: "data policy to filter zip data"
            policy:
              data:
                priority: 1
                type: mask
                depot: icebase
                collection: retail
                dataset: customer
                selector:
                  column:
                    tags:
                      - PII.Age
                  user:
                    match: any
                    tags:
                      - "users:id:iamgroot"
                mask:
                  operator: bucket_number
                  bucket_number:
                    buckets:
                      - 5
                      - 12
                      - 18
                      - 25
                      - 45
                      - 60
                      - 70
                name: age_masking_policy
                description: An age bucket is formed by grouping the ages together. Based on defined
                  age buckets, the age of individuals is redacted and anonymized. If an
                  individual’s age falls under a defined bucket, it is replaced with the
                  lowest value of the bucket.
            ```

The Policy manifest file is structurally comprised of the following sections:

- [Resource meta section](#resource-meta-section)
- [Policy-specific section](#policy-specific-section)

#### **Resource meta Section**

To create a Policy YAML in DataOS, the initial step involves configuring the [Resource Section](./resource_attributes.md) in a YAML file. This section defines various properties of the Policy Resource. The following is an example YAML configuration for the Resource Section:

=== "Syntax"

    ```yaml
    name: ${{my-policy}}
    version: v1 
    type: policy 
    tags: 
      - ${{dataos:type:resource}}
      - ${{dataos:type:cluster-resource}}
    description: ${{This is a sample policy YAML configuration}} 
    owner: ${{iamgroot}}
    layer: ${{user}}
    ```

=== "Sample"

    ```yaml
    name: my_policy
    version: v1 
    type: policy 
    tags: 
      - policy
      - access
    description: Policy manifest
    owner: iamgroot
    layer: users
    ```



!!! info 

      The `layer` field can have value either user/system in case of Policy. 

      For policies that govern authorization for system level resources such as API Paths, `layer` is *system*, while for user `layer` authorization such as access to UDL addresses it is *user*.



Additionally, the Resource section offers various configurable attributes, which can be explored further on the link: [Attributes of Resource section.](../resources/resource_attributes.md)


#### **Policy-specific section**

The Policy-specific Section focuses on the configurations specific to the Policy Resource. Each Policy-type has its own YAML syntax.

=== "Access Policy"

    Access Policies are defined using a [subject-predicate-object](./policy/understanding_abac_pdp_and_pep.md#attribute-based-access-control-abac) triad. The YAML syntax for an Access Policy is as follows:

    === "Syntax"

        ```yaml
        policy:
          access:
            subjects:
              tags:
                - ${{roles:id:user}}
                - ${{roles:id:pii-reader}}
            predicates:
              - ${{read}}
            objects:
              <tags/paths>:
                - ${{tag/path}}
            allow: ${{true}}
        ```
    === "Sample"

        ```yaml
        policy:
          access:
            subjects:
              tags:
                - roles:id:user
                - roles:id:pii-reader
            predicates:
              - "read"
            objects:
              path:
                - "dataos://icebase:retail/city"
            allow: true
        ```
        <center><i>Policy-specific Section YAML configuration (Access Policy Syntax)</i></center>

    The table below summarizes varioues attributes/fields within the access policy YAML.

    <center>

    | Field | Data Type | Default Value | Possible Value | Requirement |
    | --- | --- | --- | --- | --- |
    | [`policy`](./policy/yaml_configuration_attributes.md#policy) | object | none | none | mandatory |
    | [`access`](./policy/yaml_configuration_attributes.md#access) | object | none | none | mandatory |
    | [`subjects`](./policy/yaml_configuration_attributes.md#subjects) | object | none | none | mandatory |
    | [`tags`](./policy/yaml_configuration_attributes.md#tags) | list of strings | none | a valid DataOS tag | mandatory |
    | [`predicates`](./policy/yaml_configuration_attributes.md#predicates) | list of strings | none | http or crud operations | mandatory |
    | [`objects`](./policy/yaml_configuration_attributes.md#objects) | object | none | none | mandatory |
    | [`paths`](./policy/yaml_configuration_attributes.md#paths) | list of strings | none | api paths, udl paths | mandatory |
    | [`allow`](./policy/yaml_configuration_attributes.md#allow) | boolean | false | true/false | optional |

    </center>

    Here, the [`subjects`](./policy/yaml_configuration_attributes.md#subjects) represents the user, the [`objects`](./policy/yaml_configuration_attributes.md#objects) denotes the target (such as an API path or resource) that the user interacts with, and the [`predicates`](./policy/yaml_configuration_attributes.md#predicates) represents the action performed. The [`allow`](./policy/yaml_configuration_attributes.md#allow) field determines whether the policy grants or restricts access for the user to perform the specified action on the designated object. Refer to the [Attributes of Policy-specific section](./policy/yaml_configuration_attributes.md) for more details on configuring subjects, predicates, and objects.

=== "Data Policy"

    === "Filter"

        === "Syntax"

            ```yaml
            policy:
              data:
                type: filter
                name: ${filterpolicyname}
                description: ${sample data policy to filter data}
                dataset_id: ${{depot.collection.dataset_name}}
                priority: ${100}}
                selector:
                  user:
                  match: ${all|any}
                  tags:
                      - ${roles:id:user}
                      - ${roles:id:pii_reader}
                filters:
                  - column: ${column_name}
                    operator: ${equals}
                    value: ${"value"}
            ```
        === "Sample"

            ```yaml 
            policy:
              data:
                type: filter
                name: "filtericebasecity"
                description: 'data policy to filter data on zip code'
                dataset_id: "icebase.retail.city"
                priority: 100
                selector:
                  user:
                    match: any
                    tags:
                      - "roles:id:user"
                      - "roles:id:pii_reader"
                filters:
                  - column: zip_code
                    operator: not_equals
                    value: "452001"
            ```
        The table below summarizes the various attributes within a Filter Data Policy manifest.

        <center>

        | Field        | Data Type       | Default Value | Possible Value                              | Requirement |
        |--------------|-----------------|---------------|---------------------------------------------|-------------|
        | [`policy`](./policy/yaml_configuration_attributes.md#policy)       | object          | none          | none                                        | mandatory   |
        | [`data`](./policy/yaml_configuration_attributes.md#data)           | object          | none          | none                                        | mandatory   |
        | [`depot`](./policy/yaml_configuration_attributes.md#depot)         | string          | none          | any valid depot name or regex pattern      | optional    |
        | [`collection`](./policy/yaml_configuration_attributes.md#collection)| string          | none          | any valid collection name or regex pattern | optional    |
        | [`dataset_id`](./policy/yaml_configuration_attributes.md#dataset_id)| string          | none          | any valid dataset identifier                | mandatory    |
        | [`priority`](./policy/yaml_configuration_attributes.md#priority)   | number          | none          | 0-100                                       | mandatory   |
        | [`selector`](./policy/yaml_configuration_attributes.md#selector)   | object          | none          | none                                        | mandatory   |
        | [`user`](./policy/yaml_configuration_attributes.md#user)           | object          | none          | none                                        | mandatory   |
        | [`tags`](./policy/yaml_configuration_attributes.md#tags_1)         | list of strings | none          | a valid DataOS tag                          | mandatory   |
        | [`column`](./policy/yaml_configuration_attributes.md#column)       | object          | none          | true/false                                  | optional    |
        | [`names`](./policy/yaml_configuration_attributes.md#names)         | list of strings | none          | valid column name                           | optional    |
        | [`tags`](./policy/yaml_configuration_attributes.md#tags_2)         | list of tags    | none          | valid column tag defined under a tag group  | optional    |
        | [`type`](./policy/yaml_configuration_attributes.md#type)           | string          | none          | mask/filter                                 | mandatory   |
        | [`filters`](./policy/yaml_configuration_attributes.md#filters)     | list            | none          | none                                        | mandatory   |
        | [`column`](./policy/yaml_configuration_attributes.md#column_1)     | string          | none          | any valid column name                       | mandatory   |
        | [`operator`](./policy/yaml_configuration_attributes.md#operator)   | string          | none          | any valid comparison operator (e.g., equals)| mandatory   |
        | [`value`](./policy/yaml_configuration_attributes.md#value)         | string          | none          | any valid value for comparison              | mandatory   |

        </center>

    === "Masking"

        === "Syntax"

            ```yaml
            policy:
              data:
                type: mask
                name: ${email_masking_policy}
                description: to mask private mail address
                priority: 1
                
                depot: ${depot name}
                collection: ${collection name}
                dataset: ${dataset name}
                selector:
                  column:
                    tags:
                      - ${PII.Email}
                  user:
                    match: ${all}
                    tags:
                      - ${"users:id:iamgroot"}
                mask:
                  operator: ${hash}
                  ${hash}:
                    algo: sha256
            ```
        === "Sample"

            ```yaml
            policy:
              data:
                type: mask
                name: email_masking_policy
                description: to mask private mail address
                priority: 1
                depot: icebase
                collection: retail
                dataset: customer
                selector:
                  column:
                    tags:
                      - PII.Email
                  user:
                    match: all
                    tags:
                      - "users:id:iamgroot"
                mask:
                  operator: hash
                  ${hash}:
                    algo: sha256
            ```

        The table below summarizes the various attributes within a Mask Data Policy manifest.

        <center>

        | Field | Data Type | Default Value | Possible Value | Requirement |
        | --- | --- | --- | --- | --- |
        | [`policy`](./policy/yaml_configuration_attributes.md#policy) | object | none | none | mandatory |
        | [`data`](./policy/yaml_configuration_attributes.md#data) | object | none | none | mandatory |
        | [`depot`](./policy/yaml_configuration_attributes.md#depot) | string | none | any valid depot name or regex pattern | optional |
        | [`collection`](./policy/yaml_configuration_attributes.md#collection) | string | none | any valid collection name or regex pattern | optional |
        | [`dataset`](./policy/yaml_configuration_attributes.md#dataset) | string | none | any valid dataset name or regex pattern | optional |
        | [`priority`](./policy/yaml_configuration_attributes.md#priority) | number | none | 0-100 | mandatory |
        | [`selector`](./policy/yaml_configuration_attributes.md#selector) | object | none | none | mandatory |
        | [`user`](./policy/yaml_configuration_attributes.md#user) | object | none | none | mandatory |
        | [`tags`](./policy/yaml_configuration_attributes.md#tags_1) | list of strings | none | a valid DataOS tag | mandatory |
        | [`column`](./policy/yaml_configuration_attributes.md#column) | object | none | true/false | optional |
        | [`names`](./policy/yaml_configuration_attributes.md#names) | list of column names | none | valid column name | optional |
        | [`tags`](./policy/yaml_configuration_attributes.md#tags_2) | list of tags | none | valid column tag defined under a tag group | optional |
        | [`type`](./policy/yaml_configuration_attributes.md#type) | string | none | mask/filter | mandatory |
        | [`mask`](./policy/yaml_configuration_attributes.md#mask) | object | none | none | mandatory |

        </center>

<!-- /[`filters`](./policy/yaml_configuration_attributes.md#filters) !-->

For detailed information on configuring the YAML file for a Data Policy, refer to the link: [Attributes of Policy-specific section.](./policy/yaml_configuration_attributes.md)



### **Applying the YAML File**

After creating the YAML configuration file for the Policy Resource, it's time to apply it to instantiate the resource in the DataOS environment. To apply the Policy YAML file, utilize the [`apply`](../interfaces/cli/command_reference.md#apply) command.


=== "Command"

    ```shell
    dataos-ctl resource apply -f ${yaml-file-path} -w ${workspace-name}
    ```

    Replace the `${yaml-file-path}` and `${workspace-name}` with respective absolute or relative file path of the Policy manifest and the Workspace name in which the Resource is to be instantiated.

=== "Example"

    ```shell
    dataos-ctl resource apply -f resources/policy.yaml -w public
    # Expected Output
    INFO[0000] 🛠 apply...                                   
    INFO[0000] 🔧 applying filtericebasecity:v1:policy...    
    INFO[0001] 🔧 applying filtericebasecity:v1:policy...created 
    INFO[0001] 🛠 apply...complete  
    ```

### **Verify Policy Creation**

To confirm that your Policy has been successfully created, you can verify it using two methods:

- **Check Policy in a Workspace:** Use the following command to list the Policy created by you in a specific Workspace:

=== "Command"
     ```shell
     dataos-ctl get -t policy -w ${workspace-name}
     ```

=== "Example"
     ```shell
     dataos-ctl get -t policy -w public
     ```

- **Retrieve All Policy in a Workspace:** To retrieve the list of all Policy created in the Workspace, add the `-a` flag to the command:

=== "Command"
     ```shell
     dataos-ctl get -t policy -w ${workspace-name} -a
     ```

=== "Example"
     ```shell
     dataos-ctl get -t policy -w public -a
     ```

You can also access the details of any created Policy through the DataOS GUI in the Resource tab of the [Operations App](/interfaces/operations/).

### **Managing a Policy**

#### **Debugging a Policy**

When a Policy encounters errors, data developers can employ various tactics to diagnose and resolve issues effectively. Here are the recommended debugging techniques:

- **Get Policy details**

    - Retrieve detailed information about the Policy to gain deeper insights into its configuration and execution status. This can be accomplished using the following command:

        === "Command"
            ```shell
            dataos-ctl resource get -t policy -w ${workspace-name} -n ${policy-name} -d
            ```
        === "Example"
            ```shell
            dataos-ctl resource get -t policy -w public -n access_policy -d
            ```

    - Review the output to identify any discrepancies or misconfigurations in the Policy that could be contributing to the error.

## Policy Implementation Mechanism

In the DataOS ecosystem, the [Heimdall](../architecture.md#heimdall) governance engine operates as the [Policy Decision Point (PDP)](./policy/understanding_abac_pdp_and_pep.md#policy-decision-point-pdp) for [Access Policies](#access-policy), while the [Minerva Gateway](../architecture.md#gateway) serves as the PDP for [Data Policies](#data-policy). Both these elements jointly supervise the enforcement of policies across a range of Policy Enforcement Points (PEP), distributed throughout the DataOS ecosystem. Learn more about Policy implementation in DataOS, [here.](./policy/implementation_of_data_and_access_policy.md)

## Policy Configuration Templates

In this section, a collection of pre-configured Policy Resource Templates are provided, tailored to meet the requirements of different scenarios. To know more navigate to the following [link](./policy/policy_configuration_templates.md)

## Case Scenarios

For detailed examples and practical implementations of Policy Resource, refer to the following Policy Resource Case Scenarios:

- [How to implement access policy?](./policy/case_scenarios/implementing_access_policy.md)

- [How to implement data masking policy?](./policy/case_scenarios/implementing_data_masking_policy.md)

- [How to implement data filtering policy?](./policy/case_scenarios/implementing_data_filtering_policy.md)