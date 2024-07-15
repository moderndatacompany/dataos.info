# Create a Policy

In DataOS, both access and data policies are configured via the singular Policy Resource. However, the two policy-types have their own YAML configuration and different underlying implementation.

### **Create a Policy manifest**

To create a Policy, the first step is to create a Policy manifest file. A sample Policy manifest is given below:

???note "Example Policy manifest"

    === "Access Policy"

        ```yaml
        # Resource meta section (1)
        version: v1
        name: test-policy-01
        type: policy
        layer: user
        description: Policy allowing iamgroot user to query workbench
        # Policy specific  section (2)
        policy:
          access:
            name:  test-policy-01
            description: this is to test access policy
            collection: default
            subjects:
              tags:
              - users:id:iamgroot      
            predicates:
              - read
              - select
            objects:
              tags:
                - dataos:resource:cluster:minerva:system   #minerva cluster access
                - dataos:system:minerva:table:icebase:retail:city  
                - dataos:type:secret:icebase_r_r  #read specific secret
                - dataos:type:secret:icebase_rw_rw  #read specific secret
                - dataos:system:ds:dataset:icebase:retail:city  #read dataset
            allow: true           # Granting access
        ```
                         
        1.  [Resource meta section](#resource-meta-section) within a manifest file comprises metadata attributes universally applicable to all [Resource-types](/resources/types_of_dataos_resources/). To learn more about how to configure attributes within this section, refer to the link: [Attributes of Resource meta section](/resources/resource_attributes/).

        2.  [Policy-specific section](#policy-specific-section) within a manifest file comprises attributes specific to the Policy Resource. This section is different for Access and Data Policy .To learn more about how to configure attributes of Policy-specific section, refer to the link: [Attributes of Policy manifest](/resources/policy/manifest_attributes/).

    === "Data Policy"

        === "Filter"

            ```yaml
            name: mydatapolicy
            version: v1 
            type: policy 
            tags: 
              - policy
            description: This is a sample policy manifest file
            owner: iamgroot
            layer: user
            policy:
              data:
                type: filter
                name: "filtericebasecity"
                description: 'data policy to filter data on zip code'
                dataset_id: "icebase.retail.city"
                priority: 1
                selector:
                  user:
                    match: all
                    tags:
                      - "users:id:aayushisolanki"
                filters:
                  - column: city_name
                    operator: equals
                    value: "Verbena"
            ```
        === "Masking"
        
            ```yaml
            name: bucketage
            version: v1
            type: policy
            layer: user
            description: "data policy to filter zip data"
            policy:
              data:
                priority: 1
                type: mask
                depot: icebase
                collection: retail
                dataset: customer
                selector:
                  column:
                    tags:
                      - PII.Age
                  user:
                    match: any
                    tags:
                      - "users:id:iamgroot"
                mask:
                  operator: bucket_number
                  bucket_number:
                    buckets:
                      - 5
                      - 12
                      - 18
                      - 25
                      - 45
                      - 60
                      - 70
                name: age_masking_policy
                description: An age bucket is formed by grouping the ages together. Based on defined
                  age buckets, the age of individuals is redacted and anonymized. If an
                  individual’s age falls under a defined bucket, it is replaced with the
                  lowest value of the bucket.
            ```

The Policy manifest file is structurally comprised of the following sections:

- [Resource meta section](#resource-meta-section)
- [Policy-specific section](#policy-specific-section)


#### **Resource meta Section**

To create a Policy YAML in DataOS, the initial step involves configuring the [Resource Section](/resources/resource_attributes) in a YAML file. This section defines various properties of the Policy Resource. The following is an example YAML configuration for the Resource Section:

=== "Syntax"

    ```yaml
    name: ${my-policy}
    version: v1 
    type: policy 
    tags: 
      - ${dataos:type:resource}
      - ${dataos:type:cluster-resource}
    description: ${This is a sample policy YAML configuration} 
    owner: ${iamgroot}
    layer: ${user}
    ```

=== "Sample"

    ```yaml
    name: my_policy
    version: v1 
    type: policy 
    tags: 
      - policy
      - access
    description: Policy manifest
    owner: iamgroot
    layer: users
    ```

!!! info 

      The `layer` field can have value either user/system in case of Policy. 

      For policies that govern authorization for system level resources such as API Paths, `layer` is *system*, while for user `layer` authorization such as access to UDL addresses it is *user*.


#### **Policy-specific section**

The Policy-specific Section focuses on the configurations specific to the Policy Resource. Each Policy-type has its own YAML syntax.

=== "Access Policy"

    Access Policies are defined using a [subject-predicate-object](/resources/policy/understanding_abac_pdp_and_pep#attribute-based-access-control-abac) triad. The YAML syntax for an Access Policy is as follows:

    === "Syntax"

        ```yaml
        policy:
          access:
            name: ${test-access-policy}
            description: ${this is a description of policy}
            collection: default
            subjects:
              tags:
                - ${roles:id:user}
                - ${roles:id:pii-reader}
            predicates:
              - ${read}
            objects:
              <tags/paths>:
                - ${tag/path}
            allow: ${true}
        ```
    === "Sample"

        ```yaml
        policy:
          access:
            name: test-access-policy
            description: this is a description of policy
            collection: default
            subjects:
              tags:
                - roles:id:user
                - roles:id:pii-reader
            predicates:
              - "read"
            objects:
              path:
                - "dataos://icebase:retail/city"
            allow: true
        ```

=== "Data Policy"

    === "Filter"

        === "Syntax"

            ```yaml
            policy:
              data:
                type: filter
                name: ${filterpolicyname}
                description: ${sample data policy to filter data}
                dataset_id: ${depot.collection.dataset_name}
                priority: ${100}
                selector:
                  user:
                  match: ${all|any}
                  tags:
                      - ${roles:id:user}
                      - ${roles:id:pii_reader}
                filters:
                  - column: ${column_name}
                    operator: ${equals}
                    value: ${"value"}
            ```
        === "Sample"

            ```yaml 
            policy:
              data:
                type: filter
                name: "filtericebasecity"
                description: 'data policy to filter data on zip code'
                dataset_id: "icebase.retail.city"
                priority: 100
                selector:
                  user:
                    match: any
                    tags:
                      - "roles:id:user"
                      - "roles:id:pii_reader"
                filters:
                  - column: zip_code
                    operator: not_equals
                    value: "452001"
            ```
    === "Masking"

        === "Syntax"

            ```yaml
            policy:
              data:
                type: mask
                name: ${email_masking_policy}
                description: to mask private mail address
                priority: 1
                
                depot: ${depot name}
                collection: ${collection name}
                dataset: ${dataset name}
                selector:
                  column:
                    tags:
                      - ${PII.Email}
                  user:
                    match: ${all}
                    tags:
                      - ${"users:id:iamgroot"}
                mask:
                  operator: ${hash}
                  ${hash}:
                    algo: sha256
            ```
        === "Sample"

            ```yaml
            policy:
              data:
                type: mask
                name: email_masking_policy
                description: to mask private mail address
                priority: 1
                depot: icebase
                collection: retail
                dataset: customer
                selector:
                  column:
                    tags:
                      - PII.Email
                  user:
                    match: all
                    tags:
                      - "users:id:iamgroot"
                mask:
                  operator: hash
                  ${hash}:
                    algo: sha256
            ```


### **Apply the Policy manifest**

After creating the manifest file for the Policy Resource, it's time to apply it to instantiate the resource in the DataOS environment. To apply the Policy YAML file, utilize the [`apply`](/interfaces/cli/command_reference#apply) command.

=== "Command"

    ```shell
    dataos-ctl resource apply -f ${yaml-file-path} -w ${workspace-name}
    ```

    Replace the `${yaml-file-path}` and `${workspace-name}` with respective absolute or relative file path of the Policy manifest and the Workspace name in which the Resource is to be instantiated.

=== "Example"

    ```shell
    dataos-ctl resource apply -f resources/policy.yaml -w public
    # Expected Output
    INFO[0000] 🛠 apply...                                   
    INFO[0000] 🔧 applying filtericebasecity:v1:policy...    
    INFO[0001] 🔧 applying filtericebasecity:v1:policy...created 
    INFO[0001] 🛠 apply...complete  
    ```

## Manage a Policy

### **Verify Policy Creation**

To confirm that your Policy has been successfully created, you can verify it using two methods:

**Check Policy in a Workspace:** Use the following command to list the Policy created by you in a specific Workspace:

=== "Command"
     ```shell
     dataos-ctl get -t policy -w ${workspace-name}
     ```

=== "Example"
     ```shell
     dataos-ctl get -t policy -w curriculum
     ```

**Retrieve All Policy in a Workspace:** To retrieve the list of all Policy created in the Workspace, add the `-a` flag to the command:

=== "Command"
     ```shell
     dataos-ctl get -t policy -w curriculum -a
     ```

=== "Example"
     ```shell
     dataos-ctl get -t policy -w curriculum -a
     ```

You can also access the details of any created Policy through the DataOS GUI in the Resource tab of the [Operations App](/interfaces/operations/).


#### **Debugging a Policy**

When a Policy encounters errors, data developers can employ various tactics to diagnose and resolve issues effectively. Here are the recommended debugging techniques:

- **Get Policy details**

    - Retrieve detailed information about the Policy to gain deeper insights into its configuration and execution status. This can be accomplished using the following command:

        === "Command"
            ```shell
            dataos-ctl resource get -t policy -w ${workspace-name} -n ${policy-name} -d
            ```
        === "Example"
            ```shell
            dataos-ctl resource get -t policy -w public -n access_policy -d
            ```

    - Review the output to identify any discrepancies or misconfigurations in the Policy that could be contributing to the error.
