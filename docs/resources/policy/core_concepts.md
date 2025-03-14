# Understanding Core Concepts of Policy

## Attribute Based Access Control (ABAC)

DataOS leverages Attribute-Based Access Control (ABAC) to facilitate fine-grained access control and authorization. ABAC policies in DataOS are guided by the evaluation of attributes, also known as 'tags', associated with the user making the request, the requested resource, and the intended action.

To achieve this, DataOS relies on the subject-predicate-object triad:

### **Subject**

Users or applications/services identified by sets of tags that initiate resource requests.

### **Object**

Resources that can be exposed by the system itself or applications/services running on top of DataOS. Objects are identified using UDL addresses, API paths, or sets of tags.

### **Predicate**

The specific action or operation a user desires to perform, such as a read/write operation on a path, HTTP operation on an API path, or data masking or filtering techniques.

Policy decisions in DataOS are made by evaluating the tags (or attributes) associated with subjects and objects. These tags are matched against a set of policies to determine whether a particular predicate should be allowed for a given subject and object combination.

## PDP and PEP

Whenever a user attempts to perform a predicate on a resource, this interaction pattern can be better comprehended through an understanding of [Policy Decision Points (PDP)](#policy-decision-point-pdp) and [Policy Enforcement Points (PEP)](#policy-enforcement-point-pep).

### **Policy Decision Point (PDP)**

True to its name, the Policy Decision Point (PDP) is responsible for making policy decisions. It maintains a data structure comprising all the policies and provides an API that receives a user token (to ascertain the subject), the predicate being requested, and the target object. Based on existing policies, it responds by either granting or refusing permission.

### **Policy Enforcement Point (PEP)**

A Policy Enforcement Point (PEP) signifies the service at the point of access. Upon being accessed, it interacts with the Policy Decision Point (PDP), providing it with the necessary information to authorize the current context. Depending on the response received from the PDP, the PEP either permits or denies the user's intended action. For instance, during ingress, the proxy validates whether specific API paths are permissible or restricted and refrains from proxying the request if the PDP indicates denial.

<div style="text-align: center;">
  <img src="/resources/policy/pdp_and_pep.png" alt="PDP and PEP" style="border:1px solid black; width: 80%; height: auto;">
</div>

In this context, [Heimdall](/architecture/#heimdall) serves as the PDP for access policies, and [Data Policies](/resources/policy/#data-policy). The rest of the system's services function as PEPs, liaising with Heimdall for all authorization-related matters.

## Policy Implementation Mechanism

In the DataOS ecosystem, the [Heimdall](/architecture/#heimdall) governance engine operates as the Policy Decision Point (PDP) for Access Policies, while the [Minerva Gateway](/architecture/#gateway) serves as the PDP for Data Policies. Both these elements jointly supervise the enforcement of policies across a range of Policy Enforcement Points (PEP), distributed throughout the DataOS ecosystem. Learn more about Policy implementation in DataOS, [here](/resources/policy/how_to_guide/implementing_access_policy/).