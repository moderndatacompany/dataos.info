# How to govern an Instance Secret?

After an Instance Secret is created, a DataOS Operator can control and manage access to it.

To access an Instance Secret a user must have the following tag assigned:

- `roles:id:data-dev`

                               

Alternatively,  a user must have the following use case assigned:

- `Manage All Instance-level Resources of DataOS in user layer`

<aside class="callout">
🗣️ Note that the "data-dev" tag grants permission to manage all Resources within DataOS, whereas the "Manage All Instance-level Resources of DataOS in the user layer" use case provides specific permission to manage only instance-level Resources.
</aside>



## How to manage read-only or read-write access?

An operator can define users' access level when creating Instance Secrets by setting different ACL levels. To grant read-only access, the operator creates an Instance Secret with `acl: r`, while for both read and write access, they create one with `acl: r` and another with `acl: rw`.

## How to assign a tag to a user?

Follow the below steps to assign a tag to a user:

1. Go to the Bifrost app.

      <center>
      <img src="/resources/instance_secret/bifrost_homepage.png" alt="Bifrost Governance" style="width:55rem; border: 1px solid black; padding: 5px;" />
      <figcaption><i>DataOS Home</i></figcaption>
      </center>


2. Search for the user you want to assign the tag to.

      <center>
      <img src="/resources/instance_secret/user_search.png" alt="Bifrost Governance" style="width:55rem; border: 1px solid black; padding: 5px;" />
      <figcaption><i>Bifrost Governance</i></figcaption>
      </center>

3. In the "tags" section, click "Add Role" and choose the tag you want to assign to the user. In this case, select "Data Dev - roles:id:data-dev".

      <center>
      <img src="/resources/instance_secret/tag.png" alt="Bifrost Governance" style="width:55rem; border: 1px solid black; padding: 5px;" />
      <figcaption><i>Bifrost Governance</i></figcaption>
      </center>

## How to assign a use case to a user?

Follow the below steps to assign a use case to a user:

1. Go to the Bifrost app.

      <center>
      <img src="/resources/instance_secret/bifrost_homepage.png" alt="Bifrost Governance" style="width:55rem; border: 1px solid black; padding: 5px;" />
      <figcaption><i>DataOS Home</i></figcaption>
      </center>

2. Search for the user you want to assign the tag to.

      <center>
      <img src="/resources/instance_secret/user_search.png" alt="Bifrost Governance" style="width:55rem; border: 1px solid black; padding: 5px;" />
      <figcaption><i>Bifrost Governance</i></figcaption>
      </center>

3. In the "Grants" section,  click "Grant Use-case" and select the use-case you want to assign to the user.

      <center>
      <img src="/resources/instance_secret/user_grant.png" alt="Bifrost Governance" style="width:55rem; border: 1px solid black; padding: 5px;" />
      <figcaption><i>Bifrost Governance</i></figcaption>
      </center>