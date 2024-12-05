---
title: Policy
search:
  boost: 4
---

# :resources-policy: Policy

Policy is a [Resource](/resources/) in DataOS that defines a set of rules or guardrails governing the behavior of users, be it individuals or applications/services. Within DataOS, Policies are enforced using [Attribute Based Access Control (ABAC)](/resources/policy/core_concepts/#attribute-based-access-control-abac) and define what [predicates](/resources/policy/core_concepts/#predicate) a user (a [subject](/resources/policy/core_concepts/#subject) can perform on a dataset, API Path, or a Resource (an [object](/resources/policy/core_concepts/#object), thus defining the constraints of the relationship between the subject and object. To understand the key characteristics of Policy, refer to the following link: [Core Concepts](/resources/policy/core_concepts/).

## Types of Policies

DataOS offers two primary categories of policies: Access Policy and Data Policy. These policies play essential roles in governing user access, actions, and data management within the DataOS system.


=== "Access Policy"

    Access Policies serve as the initial layer of defense, overseeing user access and actions within the system. They establish a set of well-defined rules that determine whether a user, known as the [subject](/resources/policy/core_concepts/#subject), is authorized to perform a specific action, referred to as a [predicate](/resources/policy/core_concepts/#predicate), on a given dataset, API path, or other resources, known as [objects](/resources/policy/core_concepts/#object). These policies serve as regulatory mechanisms, effectively governing user interactions and ensuring that access to specific actions is either granted or denied. This decision is based on the evaluation of attributes associated with the subjects and objects involved in the access request.

    <div style="text-align: center;">
      <img src="/resources/policy/governance_policies_access_policy.png" alt="Access Policy" style="border:1px solid black; width: 80%; height: auto;">
    </div>



=== "Data Policy"

    In contrast, Data Policy operates as a secondary layer of control, regulating the visibility and interaction with specific data once access has been granted. It involves the implementation of techniques such as data masking or filtering to obscure or restrict the visibility of sensitive or restricted data based on predefined rules or conditions.

    For example, when working with a dataset that includes a column labeled `credit_card_number`, it is crucial to protect the sensitive information it contains from unintended exposure. Employing data masking policies or applying data anonymization methods becomes essential to secure the contents of this specific column.

    <div style="text-align: center;">
      <img src="/resources/policy/governance_policies_data_policy.png" alt="Data Policy" style="border:1px solid black; width: 80%; height: auto;">
    </div>

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

        You can apply the Mask policy, say to mask the column with ‘customer name’ in it, directly from the [Metis UI](/interfaces/metis/) via policy tags or via [DataOS CLI](/interfaces/cli/) by applying a manifest file. 

    === "Data Filtering Policy"

        Data filtering policies establish parameters for determining which data elements should be accessible to various users or systems. Proper implementation of data filtering (or simply row filtering) policies ensures that only authorized individuals can access specific data segments.

        For Example, in an e-commerce system, customer support agents may need access to customer order details. By applying a data filtering policy:

        - Agent A can only view order records associated with customers they are assigned to.
        - Agent B can only access order records for a specific geographic region.
        - Agent C, as a supervisor, has unrestricted access to all order records.

        With the data filtering policy in place, each agent can efficiently access the necessary information while maintaining data security and confidentiality.

## Structure of Policy manifest

=== "Access Policy"

    Access Policies are defined using a subject-predicate-object triad. The YAML syntax for an Access Policy is as follows:

    === "Syntax"

        ![Access Policy manifest](/resources/policy/access_policy.png)


    === "Code"

        ```yaml title="policy_manifest_structure.yml"
        --8<-- "examples/resources/policy/sample_access_policy.yml"
        ```

=== "Data Policy"

    The Data Policy is further divided in two section: filter data policy and masking data policy.

    === "Filter Data Policy"

        === "Syntax"

            ![Filter Data Policy manifest](/resources/policy/data_policy.png)


        === "Code"

            ```yaml title="sample_data_filter_policy.yml"
            --8<-- "examples/resources/policy/sample_data_policy(filter).yml"
            ```

    === "Masking Data Policy"

        === "Syntax"

            ![Masking Data Policy manifest](/resources/policy/data_policy.png)


        === "Code"

            ```yaml title="policy_manifest_structure.yml"
            --8<-- "examples/resources/policy/sample_mask_data_policy.yml"
            ```


## First Steps

Policy Resource in DataOS can be created by applying the manifest file using the DataOS CLI. To learn more about this process, navigate to the link: [First steps](/resources/policy/first_steps/).

## Configuration

Policy can be configured depending on the use case. For a detailed breakdown of the configuration options and attributes, please refer to the documentation: [Attributes of Policy manifest](/resources/policy/configurations/).

## Recipes

- [A end to end use-case on how to implement Access Policy](/resources/policy/how_to_guide/implementing_access_policy/)

- [A end to end use-case on how to implement Filter Data Policy](/resources/policy/how_to_guide/implementing_filter_data_policy/)

- [A end to end use-case on how to implement Masking Data Policy](/resources/policy/how_to_guide/implementing_masking_data_policy/)
