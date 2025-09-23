# Manage access permission for the Python application

This section provides a step-by-step guide on how to manage access permissions for a Python application using Bifrost Governance. By leveraging OpenID Connect (OIDC) and Bifrost Governance, you can define granular access policies, create reusable "use cases," and assign these permissions to individual users or roles.

Use cases in Bifrost Governance are reusable templates that bundle together a set of permissions.

## Prerequisites

Ensure you meet the following requirements.

- In the Python Service configuration, `noAuthentication` must be false.
- The Python Service should be running and accessible.
- DataOS API token.

## Create the use cases specific to a Python application

Once the OIDC is set up, follow the steps below to create a use case for accessing a Python application using Bifrost Governance.

1. Access Bifrost Governance.
    
    <div style="text-align: center;">
      <figure>
        <img src="/resources/stacks/python/bifrosthome.png" 
            alt="Bifrost Governance" 
            style="border: 1px solid black; width: 80%; height: auto; display: block; margin: auto;">
        <figcaption style="margin-top: 8px; font-style: italic;">Bifrost Governance</figcaption>
      </figure>
    </div>
    
2. Navigate to the “Use Cases” section.
    
    <div style="text-align: center;">
      <figure>
        <img src="/resources/stacks/python/usecase.png" 
            alt="Bifrost Governance" 
            style="border: 1px solid black; width: 80%; height: auto; display: block; margin: auto;">
        <figcaption style="margin-top: 8px; font-style: italic;">Bifrost Governance</figcaption>
      </figure>
    </div>
    
3. Click on the “Create Use Case” button and paste the code below with some specific updates.
    
    This code defines two distinct use cases for an application hosted at `st_auth` ingress path configured in the Python Service manifest file:
    
    - `read-st-auth`: Provides read-only access. confi
    - `manage-st-auth`: Provides full read/write/delete access.

    === "Read"
        ```yaml
        ---
        id: read-st-auth
        name: 'Read St Auth'
        description: 'Read St Auth'
        category: stauth
        authorization_atoms:
        - get-path-ingress
        values:
        - authorization_atom_id: get-path-ingress
          variable_values:
          - path: /st_auth/**
        ```

    === "Manage"
        ```yaml
        ---
        id: manage-st-auth
        name: 'Manage St Auth'
        description: 'Manage St Auth'
        category: stauth
        authorization_atoms:
        - get-path-ingress
        - delete-path-ingress
        - put-path-ingress
        - post-path-ingress
        values:
        - authorization_atom_id: get-path-ingress
          variable_values:
          - path: /st_auth/**
        - authorization_atom_id: put-path-ingress
          variable_values:
          - path: /st_auth/**
        - authorization_atom_id: post-path-ingress
          variable_values:
          - path: /st_auth/**
        - authorization_atom_id: delete-path-ingress
          variable_values:
        - path: /st_auth/**
        ```
    
    Similarly, you can configure the use case for your particular Python application by updating the `id`, `name`, `description`, and the `path` variable in the code above.
    
4. Then click on the “Create” button, and it is done.
    
    <div style="text-align: center;">
      <figure>
        <img src="/resources/stacks/python/usecasefile.png" 
            alt="Bifrost Governance" 
            style="border: 1px solid black; width: 80%; height: auto; display: block; margin: auto;">
        <figcaption style="margin-top: 8px; font-style: italic;">Bifrost Governance</figcaption>
      </figure>
    </div>
    

## Assign use cases to a specific user

Once the use cases specific to the Python application are created, the next step is to assign those use cases to the users who need to access the application.

1. Open Bifrost Governance.
    
    <div style="text-align: center;">
      <figure>
        <img src="/resources/stacks/python/bifrosthome.png" 
            alt="Bifrost Governance" 
            style="border: 1px solid black; width: 80%; height: auto; display: block; margin: auto;">
        <figcaption style="margin-top: 8px; font-style: italic;">Bifrost Governance</figcaption>
      </figure>
    </div>
    
2. Under the “Users” section, select the user to whom the use cases need to be assigned.

    <div style="text-align: center;">
      <figure>
        <img src="/resources/stacks/python/users.png" 
            alt="Bifrost Governance" 
            style="border: 1px solid black; width: 80%; height: auto; display: block; margin: auto;">
        <figcaption style="margin-top: 8px; font-style: italic;">Bifrost Governance</figcaption>
      </figure>
    </div>

3. Under the Grant section, click on “Grant Use Case”.

    <div style="text-align: center;">
      <figure>
        <img src="/resources/stacks/python/usergrant.png" 
            alt="Bifrost Governance" 
            style="border: 1px solid black; width: 80%; height: auto; display: block; margin: auto;">
        <figcaption style="margin-top: 8px; font-style: italic;">Bifrost Governance</figcaption>
      </figure>
    </div>

4. Select the use case specific to the Python application which is created previously.

    <div style="text-align: center;">
      <figure>
        <img src="/resources/stacks/python/usecasegrant.png" 
            alt="Bifrost Governance" 
            style="border: 1px solid black; width: 80%; height: auto; display: block; margin: auto;">
        <figcaption style="margin-top: 8px; font-style: italic;">Bifrost Governance</figcaption>
      </figure>
    </div>

5. Click on “Grant”. Once the use case is granted, it is listed under the “Grants” section as shown below.

    <div style="text-align: center;">
      <figure>
        <img src="/resources/stacks/python/grant.png" 
            alt="Bifrost Governance" 
            style="border: 1px solid black; width: 80%; height: auto; display: block; margin: auto;">
        <figcaption style="margin-top: 8px; font-style: italic;">Bifrost Governance</figcaption>
      </figure>
    </div>

## Assign use cases to a group of users with a specific role

Alternatively, instead of assigning use cases to a single user, one can assign use cases to a group of users having a specific role assigned.

1. Open Bifrost Governance.

    <div style="text-align: center;">
      <figure>
        <img src="/resources/stacks/python/bifrosthome.png" 
            alt="Bifrost Governance" 
            style="border: 1px solid black; width: 80%; height: auto; display: block; margin: auto;">
        <figcaption style="margin-top: 8px; font-style: italic;">Bifrost Governance</figcaption>
      </figure>
    </div>

2. Navigate to the Roles section.
    
    <div style="text-align: center;">
      <figure>
        <img src="/resources/stacks/python/roles.png" 
            alt="Bifrost Governance" 
            style="border: 1px solid black; width: 80%; height: auto; display: block; margin: auto;">
        <figcaption style="margin-top: 8px; font-style: italic;">Bifrost Governance</figcaption>
      </figure>
    </div>
    
3. Click on the “Data Dev” role, as in this scenario, we will grant permission to each user with the “data-dev” role tag to access the Python application by assigning the use case. 
    
    <div style="text-align: center;">
      <figure>
        <img src="/resources/stacks/python/datadev.png" 
            alt="Bifrost Governance" 
            style="border: 1px solid black; width: 80%; height: auto; display: block; margin: auto;">
        <figcaption style="margin-top: 8px; font-style: italic;">Bifrost Governance</figcaption>
      </figure>
    </div>
    
4. Navigate to the “Grants” section and click on the “Grant Use Case” button.
    
    <div style="text-align: center;">
      <figure>
        <img src="/resources/stacks/python/rolesgrants.png" 
            alt="Bifrost Governance" 
            style="border: 1px solid black; width: 80%; height: auto; display: block; margin: auto;">
        <figcaption style="margin-top: 8px; font-style: italic;">Bifrost Governance</figcaption>
      </figure>
    </div>
    
5. Select the use case created for your Python application.
    
    <div style="text-align: center;">
      <figure>
        <img src="/resources/stacks/python/rolesusecase.png" 
            alt="Bifrost Governance" 
            style="border: 1px solid black; width: 80%; height: auto; display: block; margin: auto;">
        <figcaption style="margin-top: 8px; font-style: italic;">Bifrost Governance</figcaption>
      </figure>
    </div>
    
6. Once the use case is granted, it is listed under the “Grants” section as shown below.
    
    <div style="text-align: center;">
      <figure>
        <img src="/resources/stacks/python/taggrant.png" 
            alt="Bifrost Governance" 
            style="border: 1px solid black; width: 80%; height: auto; display: block; margin: auto;">
        <figcaption style="margin-top: 8px; font-style: italic;">Bifrost Governance</figcaption>
      </figure>
    </div>

    