# Core concepts 

## Identity

An identity represents a real-world entity such as a:

- Human user  
- Service account  
- Application or system workload  

In DataOS, identities are the foundation of governance because every request to access a resource or dataset originates from an identity.

<aside class="callout">

 🗣 Identities are not created or managed inside DataOS. DataOS relies on a trusted **Identity Provider (IdP)** (for example, Azure AD, Okta, Google Workspace) as the system of record for identity existence and validity.

</aside>


## Authentication

Authentication is the process of verifying identity.

It answers the question: **“Who are you?”**

Authentication typically happens through an external Identity Provider using:

- Username/password  
- Single Sign-On (SSO)  
- Tokens (OAuth, JWT)  
- Multi-factor authentication (MFA)

Once authentication succeeds, the user is known to the system.

## Authorization

Authorization determines what an authenticated identity is permitted to do inside DataOS.

It answers the question: “What actions can you perform on which resources?”

Authorization in DataOS is implemented using centralized policies defined in the **Policy Resource**.

Authorization decisions are based on:

- Identity context (tags, roles, groups)
- Requested action (predicate)
- Target resource or dataset (object)

## PDP (Policy Decision Point)

The Policy Decision Point (PDP) is the component responsible for evaluating authorization requests. The PDP:

- Receives the access request context
- Matches it against applicable policies
- Produces a decision: ✅ Allow  or ❌ Deny  

The PDP is the “brain” of policy enforcement.

## PEP (Policy Enforcement Point)

The Policy Enforcement Point (PEP) is the component that enforces the authorization decision. The PEP:

- Intercepts requests from users or services
- Sends them to the PDP for evaluation
- Enforces the result (allow or deny)

The PEP is the “gatekeeper” that ensures policies are applied consistently across platform.

## Subject

A subject is the entity making the request. Subjects can include:

- Users  
- Roles  
- Services  
- Applications  

In DataOS, subjects are identified using tags, such as:

- `users:id:iamgroot`
- `roles:id:data-dev`

Subjects provide the context used to determine which policies apply.

## Object

An object is the target resource that the subject wants to access or operate on. Objects can include:

- DataOS Resources (Depots, Clusters, APIs)
- Datasets or tables
- Specific API paths

Objects are identified using:

- `paths`: `dataos://lakehouse:retail/city`, 
- `tags`: 

**Example:**

```yaml
objects:
  paths:
    - dataos://lakehouse:sales/orders

## Predicate

A predicate is the action the subject wants to perform on the object. Common predicates include:

- `read`
- `write`
- `create`
- `update`
- `delete`
- `execute`
- `access`

<aside class="callout">

Predicates are evaluated as `OR` conditions, since a request authorizes only one action at a time.

</aside>
---

## Policy Resource

The Policy Resource is the centralized governance mechanism in DataOS where policies are defined and managed.

It provides:

- Consistent authorization logic  
- Fine-grained control across resources  
- Declarative governance using YAML-based policies  

The Policy Resource supports two major categories:

- **Access Policies**
- **Data Policies**

## Access Policy

An Access Policy controls **who can perform what action on which DataOS resource**.

It governs platform-level access, such as:

- Who can read a Depot  
- Who can query a dataset  
- Who can access an API endpoint  

Access policies operate at the **resource level**.

**Example**

```yaml
policy:
  access:
    subjects:
      tags:
        - "roles:id:data-analyst"
    predicates:
      - "read"
    objects:
      paths:
        - "dataos://lakehouse:retail/city"
    allow: true
```

## Authorization Atoms

Authorization atoms are the smallest building blocks of an authorization decision in DataOS. An authorization atom is composed of:

- **Predicate** → *What action are they trying to perform?*  
- **Object** → *What resource or data are they trying to access?*  

Together, these form the atomic unit of policy evaluation. For example, 

## Grant request

A grant request is a formal request made by a user or team to obtain access to a governed resource. Grant requests are part of the governance workflow and ensure:

- Access is intentional

- Access is reviewed

- Access is compliant

## Collection

A collection represents the tenant or governance boundary within which policies are evaluated. DataOS uses a single default collection:

```yaml
collection: default
```