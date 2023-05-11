# Heimdall Capabilities

Heimdall allows authentication and authorizes users to access company data in a manner that meets security, privacy, and compliance requirements. 

The Heimdall application has the following capabilities:

- [Policy Decision Point](Heimdall%20Capabilities.md)
- [User Management](Heimdall%20Capabilities.md)
- [User and Policy Tags Management](Heimdall%20Capabilities.md)
- [Token and Secret Provider](Heimdall%20Capabilities.md)

# Policy Decision Point

Heimdall is a comprehensive policy design, deployment, and execution environment. The Policy Framework is the decision-making component in DataOS. It allows you to specify, deploy, and execute the governance strategies. Heimdall is the DataOS component that is the source of truth for all Access policy decisions. At run time, all other components communicate with it to get the required access to the enterprise data. 

### How does authorization with Heimdall works?

The objects are resources that are exposed either by the system or some applications or services running on top of the system. These resources are identified by either a path or a set of tags.

Whenever a user tries to perform a predicate(action) on a particular object from a service or a system, that specific service(PEP) calls the PDP with the requisite information to authorize the current context. Heimdall acts as the PDP for access policies, and all the other services in the system act as a PEP and then communicate with Heimdall for all authorization purposes. Heimdall has a data structure containing all the policies. It exposes an API that takes in a user token (to identify the subject), the predicate being requested, and the object being targeted. Based on the policies created, Heimdall responds with either allowed or denied. PEP lets the user/system perform the respective action or otherwise denies it.

<img src="Heimdall%20Capabilities/MicrosoftTeams-image_(97).png"
        alt="Caption"
        style="display: block; margin: auto" />

For data policies, the Gateway service acts as the PDP, and accordingly, filtering and masking are applied to the requested data. Data Policies are stored with Poros. 

To learn more about how the data policies are applied through the gateway, refer to 
[Gateway Service](Heimdall%20Capabilities/Gateway%20Service.md).

# User Management

Heimdall implements a sound security strategy with both authentication and authorization. With a strong strategy in place, Heimdall can consistently verify who every user is and what they have access to do—preventing unauthorized access to dataOS resources.

Heimdall is built upon an open-source implementation of the OpenID Connect standard for token-based authorization and Lightweight Directory Access Protocol (LDAP) for secure user management.

### OpenID Connect(OIDC)

OpenID Connect 1.0 is a simple identity layer on top of the OAuth 2.0 protocol. When a DataOS user sends a sign-in request, Heimdall uses OpenID Connect for authentication and authorization and then builds identities that uniquely identify users and the group to which they belong.

To learn more, refer to
[OpenID Connect](Authentication/OpenID%20Connect.md).

### Lightweight Directory Access Protocol(LDAP)

The Lightweight Directory Access Protocol, or LDAP, is one of the core authentication protocols used by DataOS. LDAP provides a means to manage user and group membership stored in Active Directory. 

The  LDAP  database has a flexible schema. In other words, not only can LDAP store username and password information, but it can also store a variety of attributes-core user identities:

- Users
- Attributes about those users
- Group membership privileges

This information is used to enable authentication to DataOS resources such as applications, storage, primitives, or services. Once configured, users can log in to DataOS using their Active Directory Username and Password. The LDAP database would then validate whether the user would have access to DataOS or not. That validation would be done by passing the user’s credentials.

Once a user is authenticated, Heimdall then applies authorization controls to ensure users can access the data they need and perform specific functions, depending on the rules (policies) established for different types of users.

# Users and Policy Tags Management

Tags play a vital role in DataOS by improving discoverability and governance. The ability to add metadata to resources using tags allows you to label resources and DataOS entities, such as users and roles, in a manner that aligns with your business requirements.

All policies defined for a given set of tags will be associated with the various types of users, as to allow/deny access to the DataOS resources. all the requisite policies against a tag or a set of tags can be applied using DataOS CLI. 

When the tag and access policy-related commands are applied through the CLI, the resource manager, Poros, communicates them to the Governance engine, Heimdall. Heimdall then securely stores these tags and access policies in its database and uses them as a reference when making access policy decisions.
[User and Policy Tags Management](Heimdall%20Capabilities/User%20and%20Policy%20Tags%20Management.md).

# Token and Secret Provider

Heimdall plays an important role in Secrets management. It stores, accesses, and centrally manages digital authentication credentials, which include sensitive data such as passwords, keys, APIs, tokens, and certificates. These secrets are used to authenticate a user or machine in order to access resources or services within the DataOS ecosystem.

Heimdall helps you protect the secrets needed to access your data sources and other services. It enables you to securely store, manage, and retrieve database credentials, API keys, and other secrets throughout their lifecycle. Heimdall enables you to control access to secrets using fine-grained permissions whenever the users or applications want to retrieve credentials.

Heimdall also creates an API Access Token, a security token that contains Claims about the Authentication of a user by an Authorization Server. The user uses this token to make requests to the resources within the DataOS environment. It ensures that only users with a valid token are allowed to attempt to connect to the target resource/service.

Refer to [Creating API Keys and Token](Heimdall%20Capabilities/Creating%20API%20Keys%20and%20Token.md) to learn more about generating tokens in DataOS.