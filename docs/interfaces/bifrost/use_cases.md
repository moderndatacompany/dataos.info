# Use-Cases

A use-case consists of a combination of [predicates](/interfaces/bifrost/abac_implementation_in_dataos/#predicate) (actions) and [objects](/interfaces/bifrost/abac_implementation_in_dataos/#object) (entities upon which actions are performed), defining a specific set of permissions or actions granted to users. When you grant a use case to a user, establishing a link between the subject and the use-case. This connection, in the back end, results in the creation of an access policy.

These Use-Cases can be broken down into smaller, more granular permissions, or bundled together. For instance, if a user has access to read lens, it's likely they should also have access to manage lenses, as managing encompasses the ability to create and update lenses, in addition to reading them. Each use-case may involve predicates such as delete, get, patch, and post, which collectively determine the actions a user can perform.

Assigning a use-case proves especially valuable in scenarios where granting access to the entire set of entities associated with a role is not desired. Instead, it enables a highly restricted set of permissions tailored to a specific task. 

For instance, if a data analyst or user within your company needs to query a specific dataset within a collection, granting access to all datasets in that collection is not advisable. In such cases, assigning a use-case to that particular user appears more appropriate. By granting access to a specific dataset, you achieve a higher level of granularity in data access. Further refinement of data access can be achieved through authorization atoms. 

The ‘**Use-Cases**’ tab in Bifrost lists all the possible actions needed to perform on various services and applications of DataOS as shown below. 

<center>
  <div style="text-align: center;">
    <img src="/interfaces/bifrost/use_cases/usecases.png" alt="Use-Cases" style="width: 80%; border: 1px solid black; heigt:auto">
    <figcaption>Use-Cases tab in Bifrost</figcaption>
  </div>
</center>


Upon selecting any listed use-case, a window appearing from the right has the details around the selected use-case such as Info, Authorization Atoms, Variables and Grant.

The Info section furnishes details such as the use-case's name, ID, and category, indicating its classification.

Clicking on a predicate reveals further details and the object, specifying where the action will take place. For instance, clicking on the "**get**" predicate unveils the object as an API path, typically defined as ${path}, offering flexibility in path updates without altering or even granting access to multiple API parts within a single use-case. Authorization atoms outline the permissions and actions available for a particular service or application. 

To update the path value, navigate to the Variable section, where the actual path for the specific use-case is located.

Lastly, In the grant section, you'll find a subsection labeled "**Subject**" where you can determine who has been granted access to the use-case thus far.

<div style="text-align: center;">
    <img src="/interfaces/bifrost/use_cases/grant_usecases.png" alt="grant_usecases" style="width: 80%; height: auto; border: 1px solid black;">
    <figcaption>Grant Use-Cases</figcaption>
</div>

## How to grant a use case to a role?

Granting a use-case to a role follows the same steps as [granting a use-case to a user](/interfaces/bifrost/users/#how-to-grant-a-use-case-to-a-user) but instead of navigating to users, you'll go to roles and select any existing role. Let's demonstrate this process by adding a use case named “Minerva Cluster Access" to the  `role:id:testrole`

1. Navigate to Roles and select the "test role".
2. Navigate to the grants section. Click on the "**Grant Use-Case**" button.
3. Enter "Minerva Cluster Access" in the search bar and select from the displayed options. 
4. Click on the Grant to add a Use-Case to the role.

A success message will be displayed confirming that the use case has been successfully added to the role.

## How to create a new Use-Case?

In addition to granting the current use cases, you have the option to generate a new use case by creating a YAML use-case artifact. This is particularly useful if you identify a combination of predicate and object that isn't already present but could be relevant to your organization. To create a new use-case follow the below steps:

1. Navigate to the Use-Cases tab in Bifrost

2. Click on create Use-Case 

3. Enter the use-case manifest file

A sample Use-Case manifest is given below:

???tip "Sample Use-Case manifest"
    ```yaml
    # Enter the Yaml Use-Case Artifact
    id: write-depot-dataset
    name: 'Write Depot - Dataset'
    description: 'write depot and its datasets using specific dataset elements'
    category: data
    authorization_atoms:
      - write-dataset
      - write-depot-service-paths
      - post-path-ingress
      - put-path-ingress
    values:
    - authorization_atom_id: post-path-ingress
      variable_values:
      - path: /ds/api/v2**
    - authorization_atom_id: put-path-ingress
      variable_values:
      - path: /ds/api/v2**
    ```
Note: When granting a new use-case, it is essential to specify whether full access is desired or if limited access should be granted.

For instance:

- To grant access to the entire depot, dataset, and tables, use the following address format:

```shell
dataos://******
```

- If access is to be restricted to specific tables, utilize the address format below:

```shell
dataos://icebase:emr_healthcare/*
```

- To grant access specifically on icebase, employ the address format demonstrated:

```shell
dataos://icebase:******
```

Alternatively, you can apply the following sample access policy manifest 

???tip "Sample access policy manifest"
    ```yaml
    name: access-policy-workspace
    version: v1
    type: policy
    tags:
      - data product
      - dataos:workspace:curriculum 
      - curriculum 
    description: access policy to allow a user to work in a specific workspace
    layer: user 
    policy:
      access:
        subjects:
          tags:
            - users:id:iamgroot
        predicates:
          - read
          - create
          - update
          - delete 
          - create_in
          - delete_in
          - read_in
          - update_in
        objects:
          tags:
            - dataos:layer:user
            - dataos:type:resource
            - dataos:workspace:curriculum
            - dataos:resource:database
            - dataos:resource:cluster
            - dataos:resource:service
            - dataos:resource:workflow
            - dataos:resource:worker
            - dataos:resource:volume
            - dataos:resource:secret
        allow: true
    ```

## How to edit a Use-Case? 

To edit a Use-Case, you have two options. The first method is to delete the existing Use-Case and create a new one with the desired modifications. The second method involves editing the Use-Case that was generated during installation, as it's included in the installation file.

## How to delete a Use-Case?

To delete a Use-Case:

- Navigate to the Use-Case section within Bifrost.
- Locate and select the specific use-case you wish to delete.
- Scroll down to the options and choose "**Delete Use-Case.**"