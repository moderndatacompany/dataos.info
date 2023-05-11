# Authentication

DataOS uses Federated Identity Management for user authentication.  The identity provider is configured during DataOS deployment. In DataOS, the Heimdall (Governance Engine) service acts as a portal to external identity providers through connectors. Heimdall provides an OpenID Connect interface to all DataOS applications and services, regardless of the external identity management solution’s protocol. Once a user successfully logs into the external identity provider, Heimdall will proxy or issue a JSON web token that is then used for identity verification in DataOS applications and services.

When an authorized user logs into DataOS for the first time, a user entity is created in DataOS through the federated identity provider and Heimdall. The user entity can be tagged according to the configured external group defined during DataOS deployment. Admins can easily manage users, their attributes, and tags in the DataOS Operations Center.

### OpenID Connect(OIDC)

Heimdall, the DataOS governance engine, is built upon an open-source implementation of the OpenID Connect standard for token-based authorization for secure user management.

OpenID Connect 1.0 is a simple identity layer on top of the OAuth 2.0 protocol.  It allows Clients to verify the identity of the End-User, based on the authentication performed by an Authorization Server, as well as to obtain basic profile information about the End-User using exposed REST API.

When a DataOS user sends a sign-in request, Heimdall uses OpenID Connect for authentication and authorization and then builds identities that uniquely identify users and the group to which they belong.

To learn more, refer to
[OpenID Connect](Authentication/OpenID%20Connect.md).