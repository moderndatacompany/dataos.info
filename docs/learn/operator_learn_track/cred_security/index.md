# Safeguarding credentials in DataOS

As a DataOS Operator, you understand that managing sensitive credentials is critical for ensuring secure and seamless platform operations. This module dives into Credential Security, equipping you with the tools and best practices needed to protect sensitive information within DataOS. Through a guided journey, you’ll learn how to prevent accidental exposure of credentials, establish robust security practices, and confidently manage sensitive credentials across workflows.

## Scenario

Imagine a scenario where your team accidentally commits database credentials to a public repository. While the issue is quickly fixed, it highlights the critical risks associated with poor credential management.

To prevent such incidents, this guide introduces you to the tools in DataOS for securing sensitive information. Your first task is to understand the distinction between **Secrets** and **Instance Secrets Resources**, foundational components for robust credential security.

## Quick concepts

In DataOS, credentials such as API tokens, database passwords, and certificates are protected using two key DataOS Resources:

1. **Instance Secrets**: A DataOS Resource accessible instance-wide. These secrets are ideal for credentials accessed by Resources in multiple Workspaces like code repository credentials or Instance-level Resources such as **Depots**.
2. **Secrets**: A Workspace-level DataOS Resource storing credentials with access restricted to specific Workspace Resources for targeted security. These are ideal when you want to reference secrets in Workspace-level Resources such as **Workflows**, **Worker**, **Services**, etc.

They help you to:

- Securely store sensitive data without embedding it directly into code or manifests.

- Define granular access controls at the secret level, ensuring only authorized users or applications can access credentials.

## Implementing credential security

Suppose, you want to secure credentials for a new Postgres Depot and store them separately. Since the Depot is an instance-level DataOS Resource, you’ll use Instance Secrets. You can refer this instance secret in you Depot manifest. To manage access, you’ll create two sets of Instance Secrets: one for read-only access and another for read-write access. Follow these steps to create the Instance Secret manifest file:

### **Step 1: Preparing manifest file**

1. **Identify the sensitive data**: Gather the credentials needed for the Postgres Depot, including `$POSTGRES_USERNAME` and `$POSTGRES_PASSWORD`.
2. **Draft the manifest structure**: Using a text editor, create a manifest file for read secrets with the following structure:
    a. Provide the following attributes:
        - `name`: Combine the name of the Depot and access control (e.g., `postgresdepot-r` for read access).
        - `description`: Provide proper description.
        - `acl`: Specify access control (`r` for read, `rw` for read-write).
    
    ```yaml
    # PostgreSQL Read Instance-secret manifest
    name: postgresdepot-r
    version: v1
    type: instance-secret
    description: Read instance secret for Postgres data source credentials
    layer: user
    instance-secret:
      type: key-value-properties
      acl: r
      data:
        username: $POSTGRES_USERNAME
        password: $POSTGRES_PASSWORD
    
    ```
    
    b. Create another manifest file for read-write secrets with this structure:
    
    ```yaml
    # PostgreSQL Read Write Instance-secret manifest
    name: postgresdepot-rw
    version: v1
    type: instance-secret
    description: Read-write instance secret for Postgres data source credentials
    layer: user
    instance-secret:
      type: key-value-properties
      acl: rw
      data:
        username: $POSTGRES_USERNAME
        password: $POSTGRES_PASSWORD
    
    ```
    
3. **Replace placeholders**: Replace `$POSTGRES_USERNAME` and `$POSTGRES_PASSWORD` with the actual credentials. Alternatively, use environment variables to keep your manifest secure.
    
    **Best practice:** Use environment variables to set credentials via the command line. This prevents accidental exposure in the manifest file.
    
    ```bash
    export POSTGRES_USERNAME=yourusername
    export POSTGRES_PASSWORD=yourpassword
    
    ```
    

### **Step 2: Applying  manifest file**

1. Open the CLI and navigate to the directory containing your manifest file.
2. Apply the manifest using the following command:
    
    ```bash
    dataos-ctl apply -f ./yourpath/postgres-r.yaml
    ```
    
3. Verify successful creation with:
    
    ```bash
    dataos-ctl get -t instance-secret
    ```
    

### **Step 3: Referencing Instance Secrets**

Use the Instance Secrets in your Depot manifest file to securely refer to the credentials without directly embedding them:

```yaml
name: postgresdepot
version: v2alpha
type: depot
layer: user
depot:
  type: postgresql
  description: Postgres data source connection
  external: true
  secrets:
    - name: postgresdepot-r
      allkeys: true

```

### **Step 4: Applying Depot manifest**

1. Open the CLI and apply the Depot manifest:
    
    ```bash
    dataos-ctl apply -f ./yourpath/postgresdepot.yaml
    ```
    
2. Verify the creation of Depot with the following command.:
    
    ```bash
    dataos-ctl get -t depot
    ```
    

## Building a secure foundation

By mastering Credential Security, you lay the groundwork for a robust and secure DataOS environment. These practices not only prevent breaches but also streamline workflows.

## Additional learning resources

Explore advanced use cases like storing credentials for code repositories or container registries using Secrets. Strengthen your understanding with these additional resources.

- [Secret Resource Documentation](https://dataos.info/resources/secret/)
- [Instance Secret Resource Documentation](https://dataos.info/resources/instance_secret/)

## Next step

Dive deeper into secure data source connectivity in the [Data Source Connectivity](/learn/dp_developer_learn_track/data_source_connectivity/) module to build on this foundation.
