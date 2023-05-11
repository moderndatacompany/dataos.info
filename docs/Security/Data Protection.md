# Data Protection

DataOS utilizes encryption at various points to protect your data during its life cycle from origin to destination, including encryption of data at rest and data in transit and ensuring high data availability and redundancy.

# Encryption of Data at Rest

DataOS considers all customer data confidential and encrypts data at rest, leveraging the cloud service provider’s encryption algorithm to protect against physical security breaches. Every cloud provider has a slightly different way of encrypting, but storage is generally encrypted using encryption keys that are generated and rotated automatically by the cloud provider. Encryption keys can also be explicitly defined and managed as determined by the customer’s security policies. Data stored in the default DataOS depots (e.g., Icebase, Fastbase, PostGRE) is encrypted at rest at the storage level using AES-256, leveraging the cloud service provider’s default storage encryption.

This enables customers to guard against unauthorized access, illegal copying, and other security threats, ensuring data and firmware integrity at all times.

# Encryption of Data in Transit

DataOS employs all necessary security measures to help ensure customer data is protected during transit. It does this by encrypting the data before transmission, authenticating the endpoints, and decrypting and verifying the data upon arrival.

Internal data transfer within DataOS: Default DataOS depots utilize secure and updated versions of protocols like TLS 1.2 instead of SSL for data transfer. All data accessed from applications occurs over HTTPS using TLS 1.2.

External data transfer outside DataOS: From data ingestion and syndication to external depots, source and sink systems define the protocols and security. DataOS utilizes current versions of connector libraries and chooses the most secure option available for connecting to these external depots.

## Best Practices to secure PostgreSQL Database

DataOS uses the Postgres database for storing the data generated for the ‘System’ level as well as ‘User’ level activities.  In DataOS, all the Postgres instances live in a private subnet. They have no access from outside, to the public Internet, or from anywhere. 

The following best practices are followed to secure a PostgreSQL database and protect sensitive data from security threats:
1. `User authentication`: DataOS policies are implemented to restrict access to the database based on IP addresses and network security groups. [should we mention OIDC here?]
2. `Encryption`:  SSL encryption is enabled for all client-server communication to protect sensitive data in transit.
3. `Access controls`:  Attribute/Role-based access controls are defined and enforced to limit user access to only the data and database operations they need.
3. `Firewall rules`: Firewall rules are implemented to restrict incoming and outgoing network traffic to only necessary ports and IP addresses.
4. `Regular backups`: Regular backups of database data are scheduled, and backups are stored in a secure location to ensure data recovery in case of an outage or disaster.
5. `Database auditing`: Database activity is monitored and logged to track and detect suspicious activity, and an auditable trail of database operations is provided.
6. `Operating system security`: The operating system is kept up to date with the latest security patches and ensures that only authorized users have access to the operating system.
7. `Regular security updates`:  PostgreSQL is regularly updated to the latest version, which includes security patches and enhancements.
8. `Data validation`: All user input and use parameterized queries are validated to prevent SQL injection attacks.
9. `Threat monitoring`: Security threats and vulnerabilities are monitored for and responded to by staying up to date with the latest security best practices and tools.

# Data Availability and Redundancy

Availability and redundancy features vary across cloud service providers, but blob storage and disk storage are highly available and redundant based on provisioning configurations. Storage provisioning configurations are tuned to suit your business requirements during DataOS deployment. As you ingest data, it can be synchronously and transparently replicated across availability zones. Disk backups are performed every night, and seven days of these snapshots are retained.

# Data Protection Policies

Policies are essential components of a data protection program, you can create data policies to guide what data the user sees once they access a dataset. Data Policies define what data protection strategies (masking and filtering) can be defined to protect sensitive data from unauthorized access.

To learn more, refer to
[Policy](../About%20DataOS/Primitives%20Resources/Policy.md).