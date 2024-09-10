# Data Governance

You can govern data access based on individual user or user groups, allowing you to control the level of data visibility and interaction according to each group's role. Follow the below section to create a user group. In this section, we will guide you to create user groups. 

## Authentication
To ensure that only authorized users access your Talos application, it's essential to identify who sends the request. This process, called authentication. To enable Authentication in Talos Data API, specify your current dataos heimdall url in `config.yaml` as shown below. 

```yaml
auth:
  heimdallUrl: https://${{cheerful-maggot.dataos.app}}/heimdall
```

## Add User group 

Add user groups to control the access to API in `config.yaml`.

```yaml
auth:
  heimdallUrl: https://${{cheerful-maggot.dataos.app}}/heimdall
  userGroups:
    - name: reader
      description: This is a reader's group
      includes:
        - roles:id:data-dev
        - roles:id:data-guru
      excludes:
        - users:id:iamgroot
    - name: default
      description: Default group to accept everyone
      includes: "*"
```

**name**: defines the user group by name

**description**: describes the user group

**Includes**: refers to user roles that should be included 

**Excludes**: refers to user id/roles that should be excluded

**‘*’**: refers to allow everyone 



<aside class="callout">
🗣 Note that after Heimdall authentication, the DataOS environment grants default access to all users. However, by defining user groups in the `config.yaml` file, you can tailor access permissions to include or exclude specific users or roles based on your requirements.

</aside>