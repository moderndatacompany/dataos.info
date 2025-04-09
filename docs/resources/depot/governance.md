# How to govern a Depot?

After a Depot is created, a developer can control and manage access to it. This section involves governance aspect of a Depot.


<aside class="callout">
🗣️ Keep in mind that the name and permission level of each tag and use case can vary across organizations, depending on how they choose to manage them.
</aside>

To access a Depot a user must have the following tags assigned:

- `roles:id:data-dev`

Alternatively,  a user must have the following use case assigned:

- `Manage All Instance-level Resources of DataOS in user layer`

<aside class="callout">
🗣️ Note that the "data-dev" tag grants permission to manage all Resources within DataOS, whereas the "Manage All Instance-level Resources of DataOS in the user layer" use case provides specific permission to manage only instance-level Resources.
</aside>

## How to assign a tag to a user?

Follow the below steps to assign a tag to a user:

1. Go to the Bifrost app.

    <div style="text-align: center;">
      <img src="/resources/depot/bifrost_homepage.png" alt="Hierarchical Structure of a Data Source within DataOS" style="border:1px solid black; width: 80%; height: auto;">
      <figcaption><i>Bifrost Governance</i></figcaption>
    </div>

1. Search for the user you want to assign the tag to.

    <div style="text-align: center;">
      <img src="/resources/depot/user_search.png" alt="Hierarchical Structure of a Data Source within DataOS" style="border:1px solid black; width: 80%; height: auto;">
      <figcaption><i>Bifrost Governance</i></figcaption>
    </div>


1. In the "tags" section, click "Add Role" and choose the tag you want to assign to the user. In this case, select "Data Dev - roles:id:data-dev".

    <div style="text-align: center;">
      <img src="/resources/depot/tag.png" alt="Hierarchical Structure of a Data Source within DataOS" style="border:1px solid black; width: 80%; height: auto;">
      <figcaption><i>Bifrost Governance</i></figcaption>
    </div>

## How to assign a use case to a user?

Follow the below steps to assign a use case to a user:

1. Go to the Bifrost app.

    <div style="text-align: center;">
      <img src="/resources/depot/bifrost_homepage.png" alt="Hierarchical Structure of a Data Source within DataOS" style="border:1px solid black; width: 80%; height: auto;">
      <figcaption><i>DataOS Home</i></figcaption>
    </div>


1. Search for the user you want to assign the tag to. 

    <div style="text-align: center;">
      <img src="/resources/depot/usecase1.png" alt="Hierarchical Structure of a Data Source within DataOS" style="border:1px solid black; width: 80%; height: auto;">
      <figcaption><i>Bifrost Governance</i></figcaption>
    </div>


1. In the "Grants" section,  click "Grant Use-case" and select the use-case you want to assign to the user.

    <div style="text-align: center;">
      <img src="/resources/depot/usecase.png" alt="Hierarchical Structure of a Data Source within DataOS" style="border:1px solid black; width: 80%; height: auto;">
      <figcaption><i>Bifrost Governance</i></figcaption>
    </div>
