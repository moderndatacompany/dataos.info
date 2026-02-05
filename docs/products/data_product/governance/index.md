---
search:
  exclude: true
---

## Are you a first-time user?

If you are new to DataOS Governance, start here to understand:

- [The core governance concepts used across DataOS](/products/data_product/governance/core_concepts/)
- [How requests are evaluated]()
- [How access control and data governance fit together]()

# Governance of DataOS

Governance in DataOS refers to the set of controls and policies that ensure **secure, compliant, and appropriate use of data and platform resources** throughout the data lifecycle.

When we talk about **access management and governance in DataOS**, we are referring to the complete flow through which a request is evaluated:

Each stage in this flow answers a specific question:

| Layer | Question Answered | What It Controls | Description |
| --- | --- | --- | --- |
| **Authentication** | Who is the user? | Identity trust | **Authentication** verifies that identity and establishes trust. |
| **Authorization** | What can they do? | Resource access: Using Policy Resource - Access Policy | **Authorization** determines what actions that identity is allowed to perform. |
| **Data policies** | What data do they see? | Data exposure: Using Policy Resource - Data Filter Policy and Data Masking Policy | Data policies further constrain what data is exposed after access is granted. |

This layered approach ensures that:

- A user must first be **identified and authenticated**
- Only then can they be **authorized to interact with platform resources**
- And finally, **data-level policies** determine what data is visible once access is granted

Before diving into implementation details, it is important to understand the [core governance concepts]() used throughout DataOS.

## Understand the flow

When a user signs in to DataOS and lands on the home page, only **authentication** has occurred.

When a user or service interacts with DataOS through the UI, CLI, APIs, or a data consumption interface, such as:

- Opening a Data Product
- Querying a dataset
- Accessing data through a consumption interface

DataOS generates an **authorization request** for that resource.

This request represents the intent to operate on a DataOS Resource or data asset. DataOS evaluates this request using **DataOS Policy** to determine whether the request should be **allowed or denied**.

DataOS then:

1. Identifies which policies apply based on the identity context (such as `roles` identified by `tags`)
2. Evaluates those policies against the requested operation and resource
3. Determines whether the request should be allowed or denied

Once authorized, the subject can perform actions or operations on resources in DataOS. 

For example, a user identified as `dataos:user:iamgroot` signs in to DataOS and successfully lands on the home page, confirming that authentication has completed. 

When the user attempts to read a Depot named `sales-depot`, DataOS generates an authorization request representing the intent for the subject `dataos:user:iamgroot` to perform the action `Read` on the resource `Depot:sales-depot`. 

DataOS evaluates the applicable Access Policies and determines whether the request should be allowed or denied, and if access is granted, any applicable Data Policies are applied before the response is returned.

## Authentication

Authentication is the first step in DataOS access management, where a user or system’s identity is verified through a trusted **Identity Provider (IdP)**. The user provides credentials (password, OTP, SSO token, etc.), the IdP validates them, and confirms the identity (e.g., “Yes, this is Alice”).

This stage answers: **“Who are you?”**

Once authentication is successful, the user is identified but **no permissions are checked yet**. DataOS then proceeds to **authorization** to determine what the authenticated identity is allowed to do.

## Authorization

Authorization determines **what an authenticated identity is allowed to do inside DataOS**.

Authorization in DataOS is implemented using policies defined in a centralized **Policy Resource**.

DataOS supports two types of policies:

- **Access Policies** — control who can perform which actions on DataOS resources
- **Data Policies** — control how data is exposed after access is granted

Together, these policies enable consistent and fine-grained governance across the platform.

## Access Policy

Access Policy establishes a set of well-defined rules that determine whether a user, known as the `subject`, is authorized to perform a specific `predicate` (or action), on a given dataset, API path, or other resources, known as `objects`.

DataOS offers capabilities to define, enforce, and manage user access policies across DataOS Resources, including:

- Depot
- Datasets
- Clusters or query engines

[extra](https://www.notion.so/extra-2f5c5c1d487680d7b52ee365170ca0b6?pvs=21)

[Learn to create an access policy](https://www.notion.so/Learn-to-create-an-access-policy-2f5c5c1d487680b8baf8de84b5a8602d?pvs=21)

[Templates](https://www.notion.so/Templates-2f5c5c1d4876809dbd84f0fc675f9384?pvs=21)

[Create a resource level policy](https://www.notion.so/Create-a-resource-level-policy-2f7c5c1d48768038a6d1d85428cd8196?pvs=21)

### How an Authorization Request Is Evaluated

An authorization request in DataOS typically includes:

- The **subject** (for example, the roles or groups associated with the user)
- The **predicate** (such as reading or querying data)
- The **object** (for example, a Resource, dataset, or table)

When a request is received, DataOS evaluates all applicable **DataOS policies** to determine whether the requested action is permitted.

[Policy Evaluation Logic](https://www.notion.so/Policy-Evaluation-Logic-2f5c5c1d4876809dbd9cd2994a7078ff?pvs=21)

### Policy-based decision making

DataOS policies define **who can perform which actions on which resources**.

During evaluation:

- If a matching policy explicitly allows the request, access proceeds
- If a matching policy explicitly denies the request, access is denied
- If no matching allow policy exists, access is denied by default

This evaluation is deterministic and consistent across the platform.

## Data Policy

While access management controls **whether** data can be accessed, data governance controls **what data is exposed** once access is granted.

### Data masking

Data masking transforms sensitive values so they are not exposed in their original form. Common techniques include:

- Redaction (replacing values with a fixed placeholder)
- Hashing (e.g., MD5 or similar algorithms)

Masking is typically applied at query or model level and is transparent to consumers.

### Data filtering (row-level security)

Data filtering controls **which rows are visible** to a user based on conditions such as:

- User group membership
- Geographic region
- Business unit or responsibility

Unlike masking, filtering removes rows entirely from query results.

### Importance of masking and filtering

These techniques are critical for:

- Protecting personally identifiable information (PII)
- Supporting regional or team-based data isolation
- Enabling shared data products without duplicating datasets
- Meeting compliance and audit requirements

In DataOS, masking and filtering are implemented using **policy-driven mechanisms** applied consistently across consumption interfaces.

---

## Governance User Flow in DataOS

The governance flow in DataOS can be understood as a sequence of decisions applied as a user interacts with the platform.

### Conceptual flow

```
User authenticates
        ↓
Access policies evaluated
        ↓
Resource access granted or denied
        ↓
Data request executed
        ↓
Data masking and filtering applied
        ↓
Governed data returned to user
```

