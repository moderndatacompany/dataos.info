# Security

DataOS includes a multitude of security features like the protection of data at rest or in transit, authentication and authorization of users, creation of audit feeds and capturing logs, and more. DataOS ensures data is always fit for purpose - we carefully consider all security concerns
involved in data collection, sharing, and use, as well as rapid data integration and access restriction.

> 🗣 DataOS uses a zero-trust network perspective by implementing internal security measures and continuously validating for security configuration before granting access to applications and data.

# Secure by Design

DataOS provides all the key security measures required to protect your data, including network and infrastructure security, host and endpoint security, data encryption by default, logging and monitoring, identity and access control, governance, and compliance.

DataOS implements a robust set of security features and enables customers to guard against unauthorized access, illegal copying, and other security threats, ensuring data and firmware integrity at all times.

<img src="Security/MicrosoftTeams-image_(88).png"
        alt="Caption"
        style="display: block; margin: auto" />

> 🗣 Given its exhaustive governance capabilities, DataOS, a first-of-its-kind unified data operating system, was recognized as a Representative Vendor in Gartner's "Market Guide for Data and Analytics Governance Platforms,” published in December 2021.

## Authentication

DataOS uses Federated Identity Management for user authentication. DataOS leverages external identity management solutions for login and user creation like OIDC. The identity provider is configured during DataOS deployment. In DataOS, the Heimdall (Governance Engine) service acts as a portal to external identity providers through connectors. 

To know more, refer to
[Authentication](Security/Authentication.md).

## Authorization

Authorization allows or restricts actions that authenticated users can perform on the DataOS platform. Our tag-based governance mechanism provides access control based on roles, attributes, and tags. This empowers teams to set up conditional access controls like the ability to access datasets, applications, and resources by specific users or groups.

To know more, refer to
[Authorization](Security/Authorization.md).

> 🗣 DataOS’s innovative ABAC implementation uses tags and conditions to define policy, which allows you to implement very coarse-grained access controls, like role-based access controls or even very fine-grained access controls to individual items and attributes. In DataOS, policies are defined, and users and their tags are managed in Heimdall.

## Data Protection

DataOS, the modern data fabric, protects your data regardless of where you move, store, or analyze your data. DataOS is built with a security framework that guarantees your data's availability, integrity, and confidentiality at all times.

<img src="Security/MicrosoftTeams-image_(101).png"
        alt="Caption"
        style="display: block; margin: auto" />
        
To know more, refer to
[Data Protection](Security/Data%20Protection.md).

## Network Communication

You may need DataOS to communicate with external third-party data solutions to deliver a wide range of services. All communications between DataOS and external data solutions must be authorized and initiated within DataOS. Network communication gives you visibility into the network traffic flow between your services, applications, and availability zones.

To know more, refer to
[Network Security](Security/Network%20Security.md).

## Auditing and Logging 

DataOS, by default, comes with the functionality to create a dedicated dataset for auditing events happening across DataOS applications and services.  To add visibility and auditability, this dataset contains the who, what, where, and when of activity that occurs across your DataOS environment in the form of audit logs. 

Log datasets can be consumed and analyzed as needed using standard DataOS primitives. Audit datasets and logs can also be syndicated to external systems, if defined by your operations and security processes, to analyze and deeply contextualize events.

> 🗣 DataOS has a depot dedicated to logs from applications and services running within the platform. All applications and services within the DataOS stream compress their logs into the Logging Depot, which utilizes cloud blob storage by default.

## Compliance with Regulatory Frameworks

DataOS can help your organization build a fully compliant data solution, enabling you to process sensitive and personal data in accordance with the law. It provides all the primitives needed for organizations to be data compliant and to implement many data regulatory and privacy-compliant standards like GDPR, CCPA, and PCI DSS. 

DataOS also has provisions to automate identifying sensitive data that needs to be secured or even just cataloged to comply with government regulations.

<img src="Security/Screen_Shot_2023-01-02_at_2.14.33_PM.png"
        alt="Caption"
        style="display: block; margin: auto" />

To learn more, refer to
[Compliance](Security/Compliance.md).

# Heimdall- Governance Engine

Heimdall is the authentication, authorization, and governance engine component of DataOS. It implements a sound security strategy with both authentication and authorization. With a strong strategy in place, Heimdall can consistently verify who every user is and what they can do— preventing unauthorized access to dataOS resources. DataOS has added Vault support for secrets to the Heimdall Engine as a new authentication option for environments and databases.

To learn more, refer to:

- [Security](Security/Heimdall%20Capabilities.md)

- [Heimdall Capabilities](Security/Heimdall%20Capabilities.md)