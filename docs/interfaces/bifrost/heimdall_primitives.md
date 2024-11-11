
### **Providers**

In DataOS, all resources or applications function as Policy Enforcement Points (PEPs) when interacted with by other resources, applications, or users. Here, you can also access the authorization atoms associated with each provider. For instance, when inspecting the authorization atoms for Lens, you may discover permissions like saving charts, running queries, viewing tabs, saving results, and accessing attribute information. Likewise, the “Ingress Service” Provider governs and controls access to all ingress services within the DataOS network. Similarly, other providers like Metis contain distinct authorization atoms for various actions such as deleting, writing, and reading, as well as root access, such as admin user privileges.

#### **How to register a PEP Provider?**

When adding a new application to the DataOS environment, it's imperative to register it as a PEP to enable interaction. To register a new PEP provider, the following details are required:

- **Version**: Indicates the version of the PEP provider. For new applications in dataos, the version is typically set to `0.1.0`.
- **ID**: Unique identifier for the PEP provider.
- **Name**: Name of the PEP provider.
- **Description**: Brief description of the PEP provider's purpose.
- **Authorization Atoms:** Define authorization atoms for the PEP provider. Authorization atoms consist of predicates and objects, specifying the conditions under which access is granted or denied.

For instance, when inspecting the authorization atoms for Lens, you may discover permissions or actions like saving charts, running queries, viewing tabs, saving results, and accessing attribute information. Similarly, other providers like Metis contain distinct authorization atoms for various actions such as deleting, writing, and reading, as well as route access, such as admin user privileges. Once authorization atoms are created for the PEP provider, they can be combined in various combinations to address different Use-Cases.

Utilize the provided sample manifest template as a reference for registering the new PEP provider:

???tip "Sample manifest"

      ```yaml
      #YAML to register a new PEP provider on Bifrost
      version: 0.0.1
      id: gateway-pep-provider
      name: Gateway PEP
      description: PEP to manage access to Minerva clusters
      authorization_atoms:
        - id: cluster-access
          description: authorization atom to select clusters for running Minerva queries
          predicate: select
          tags: 
            - dataos:resource:cluster:${cluster}
      ```

Ensure to replace `${cluster}` with the appropriate value when granting access.

Once the PEP provider is registered, follow these steps to view and manage it on Bifrost:

- The newly registered PEP (named Gateway PEP) will appear in the list of PEP Providers under the Heimdall Primitives.
- Click on the PEP provider to view its details.
- Click on an Authorization Atom to get its specific details.
- If needed, you can delete the provider after it is created.