# OpenID Connect

OpenID Connect 1.0 is a simple identity layer on top of the OAuth 2.0 protocol.  It allows Clients to verify the identity of the End-User, based on the authentication performed by an Authorization Server, as well as to obtain basic profile information about the End-User using exposed REST API.

OpenID Connect allows clients of all types, including Web-based, mobile, and JavaScript clients, to request and receive information about authenticated sessions and end-users. It adds an additional token called an ID token. The specification suite is extensible, allowing participants to use optional features such as encryption of identity data, the discovery of OpenID Providers, and session management when required.

When a DataOS user sends a sign-in request, Heimdall uses OpenID Connect for authentication and authorization and then builds identities that uniquely identify users and the group to which they belong.

<img src="OpenID%20Connect/MicrosoftTeams-image_(107).png"
        alt="Caption"
        style="display: block; margin: auto" />

# Configure OIDC Connector Properties

Various Identity Platforms/Cloud providers such as Azure and Google cloud help you add identity and access management functionality to your applications. 

DataOS supports Microsoft and Google OIDC connectors enabling client applications to rely on authentication that is performed by an OpenID Connect Provider (Heimdall in this case) to verify the identity of a user. You need to configure the OIDC connector properties like this.

## Microsoft OIDC Connector

```yaml
oidc_connectors: |-
    connectors:
      - type: microsoft
        id: tmdc-microsoft
        name: TMDC Users
        config:
          clientID: <clientID>
          clientSecret: <clientSecret>
          redirectURI: <redirectURI>
          tenant: <tenant>
          emailToLowercase: true
          groupNameFormat: id
```

## Google OIDC Connector

```yaml
oidc_connectors: |-
    connectors:
      - type: google
        id: tmdc-google
        name: TMDC Users
        config:
          clientID: <clientID>
          clientSecret: <clientSecret>
          redirectURI: <redirectURI>
          emailToLowercase: true
          groupNameFormat: id
```

## Important Parameters

The following parameters are required to define the Microsoft OIDC connector.

| Parameter | Description |
| --- | --- |
| type | The specific vendor name of the OIDC connector. |
| id | id of the connector. |
| name | Name of the connector. |
| client_secret | The client secret that you obtain from the API Certificate and secrets option. |
| Tenant | You can use the {tenant} value in the path of the request to control who can sign in to the application. The allowed values are common, organizations, consumers, and tenant identifiers. Critically, for guest scenarios where you sign a user from one tenant into another tenant, you must provide the tenant identifier to correctly sign them into the resource tenant. The value of the tenant varies based on the application's sign-in audience, for example, you can define tenant value such that users with a personal Microsoft account or an organizational account are able to sign in. |
| client_id | The Application (client) ID that the Azure/GCP portal – App registrations experience assigned to your app. |
| redirect_uri | The redirect URI of your app, where authentication responses can be sent and received by your app. It must exactly match one of the redirect URIs you registered in the portal, except that it must be URL-encoded. If not present, the endpoint will pick one registered redirect_uri at random to send the user back to. |
| groupNameFormat | The format name to use groups. Here, group names are used as id format. |

# Group Tag Mapping

To simplify the authorization process, groups are created with multiple user tags. These tags will be assigned to the group users. A  group is a way to attach policies to multiple users at one time. 

You can use groups to specify policies for a collection of users, making those policies easier to manage/apply. For example, you could have a group called Operators, define user tags, and attach policies to these tags that operators typically need. Any user in that operator group automatically has the permissions assigned to the group. If a new user joins your organization and should have operator-level privileges, you can assign the appropriate policies by adding the user to the Operator group. Similarly, if you want to revoke permissions, you can remove him or her from the Operator groups.

Heimdall performs authorization based on the policies defined against these tags under a group id.

These groups and users must be defined under the section of OIDC so that Heimdall can use them by mentioning their ID for authorization. 


> 💡 These groups and user tags are created as per the organizational requirements and managed by the client.


Here are some of the examples of groups:

1. DefaultUser Group 

2. DataSpecialists Group 

3. Operator Group etc.

Every group has a unique id, which is mentioned under the `groupname` parameter*. Below is the `grouptag_mapping` resource definition.*

```yaml
group_tag_mapping: |-
    group_tag_map:
      - group_name: <group_id>
        user_tags:
          - dataos:u:user
          - dataos:u:depot-reader
      - group_name: <group_id>
        user_tags:
          - dataos:u:user
          - dataos:u:developer
          - dataos:u:system-developer
          - dataos:u:depot-reader
          - dataos:u:depot-manager
      - group_name: <group_id>
        user_tags:
          - dataos:u:user
          - dataos:u:developer
          - dataos:u:system-developer
          - dataos:u:depot-reader
          - dataos:u:depot-manager
      - group_name: <group_id>
        user_tags:
          - dataos:u:user
          - dataos:u:operator
      - group_name: <group_id>
        user_tags:
          - dataos:u:user
          - dataos:u:operator
```

From above, we can see a different set of user *tags is given under every group* name. So whenever a new user is available, he/she will be added to a particular group *name to authorize sets of user* tags under that particular group_name.

### user_tags

Each user_tag contains a set of policies. Different types of users, as denoted logically by the tags assigned to them, will be attached to all the policies defined against those tags.

> NOTE: A set of user *tags under each group* name can be changed according to business requirements.
>