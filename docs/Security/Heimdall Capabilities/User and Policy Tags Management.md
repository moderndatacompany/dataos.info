# User and Policy Tags Management

Heimdall acts as a Tag Manager and allows you to delegate access to the resources based on tags. Note that some of the tags are system-generated, but custom tags can be created manually as per your resource's context.

System tags and default policies are created when DataOS installation is done. These tags are created for the core functionality. 

Some of the tags which are created in the system are:

- users:id:testuser
- roles:id:operator
- roles:id:app-user
- roles:id:data-dev

There are multiple tag namespaces that are available. For example, the user tag namespace is `users:id:`, similarly for  roles, `roles:id:`

New tag namespaces and tags can be created to mimic the organizational structure for a particular use case. Tags can also be managed using `dataos-ctl`.

# Tags for Requesting Access

Different types of users, as denoted logically by the tags assigned to them, will be attached to all the policies defined against those tags. You can use tags to conditionally allow or deny policies based on whether a resource has a specific tag. For example, if a particular user John Doe has tags:

`roles:id:data-dev` `roles:direct:metis` `users:id:testuser`

The policies created with the above-given tags as subjects will apply to the user John Doe.
Based on a particular use case, the system administrator can create all the requisite policies against a tag or a set of tags and apply them using DataOS CLI. To remove the permissions, the policies must be deleted using the DataOS CLI commands.

The following section lists all the `dataos-ctl` commands for tag and policy management. 

## Tag Management using DataOS CLI Commands

Tags can be created and deleted using the following commands.

### User Tag Command

Manage DataOS user's tags using the following command.

```bash
Usage:
dataos-ctl user tag [command]

Available Commands:
add         Add tags to a user
delete      Delete tags from a user

Flags:
-h, --help   help for tag

Use "dataos-ctl user tag [command] --help" for more information about a command.
```

### Add/ Delete Tags

```bash
# Commands to add/delete tag

# Add tags to any other users
dataos-ctl user tag add -i '<DataOS-username>' -t '<tagName>'
dataos-ctl user tag add -i 'testuser' -t 'dataos:u:testpolicy'

# Assign self tag
dataos-ctl user tag add  -t '<tagName>' 

# Delete tags to any other users
dataos-ctl user tag delete -i '<DataOS-username>' -t '<tagName>'

# Deleting self tag
dataos-ctl user tag delete  -t '<tagName>'
```

> Note: You need ‘Operator’ level permissions to add or delete tags for any user.
> 

## Policy Management using DataOS CLI Commands

Refer to the following commands for creating and managing policies.

### Apply Policy

```bash
➜  ~ dataos-ctl apply -f <path/filename.yaml> 
```

### Get the List of Policies

```bash
➜  ~ dataos-ctl get -t policy -a
INFO[0000] 🔍 get...                                     
INFO[0000] 🔍 get...complete                             

                 NAME                 | VERSION |  TYPE  | WORKSPACE | STATUS | RUNTIME |          OWNER           
--------------------------------------|---------|--------|-----------|--------|---------|--------------------------
  audit-receiver-peer-tags            | v1      | policy |           | active |         | dataos-resource-manager  
  blender-paths                       | v1      | policy |           | active |         | dataos-resource-manager  
  blender-read-icebase                | v1      | policy |           | active |         | dataos-resource-manager  
  default-toolbox-user-tags           | v1      | policy |           | active |         | dataos-resource-manager  
  depot-manager-paths                 | v1      | policy |           | active |         | dataos-resource-manager  
  depot-manager-tag                   | v1      | policy |           | active |         | dataos-resource-manager  
  depotservice-paths                  | v1      | policy |           | active |         | surajsinghgahlot         
  depotservice-tags                   | v1      | policy |           | active |         | dataos-resource-manager  
  developer-metis-paths               | v1      | policy |           | active |         | dataos-resource-manager  
  developer-poros-paths               | v1      | policy |           | active |         | dataos-resource-manager  
  fingerprint-peer-tags               | v1      | policy |           | active |         | dataos-resource-manager  
  metis-paths                         | v1      | policy |           | active |         | dataos-resource-manager  
  metis-tags                          | v1      | policy |           | active |         | dataos-resource-manager  
  operator-paths                      | v1      | policy |           | active |         | dataos-resource-manager  
  operator-permissions                | v1      | policy |           | active |         | dataos-resource-manager  
  operator-read-all-depots            | v1      | policy |           | active |         | dataos-resource-manager  
  pii-hash                            | v1      | policy |           | active |         | dataos-resource-manager  
  pii-reader                          | v1      | policy |           | active |         | dataos-resource-manager  
```

### Delete a Policy

```bash
➜  ~ dataos-ctl delete -t policy -n <name of the policy> 
```

> 🗣 Tags /attributes-based access policies are easy to build and understand. At run time, all other components communicate with Heimdall to get the required access to the enterprise data based on tags. To learn more about how users can access DataOS resources and perform actions with various tags, refer to [Tag-based Authorization](../Authorization/Tag-based%20Authorization.md)