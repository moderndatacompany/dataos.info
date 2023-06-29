# Creating Secrets

To create a Secret resource in DataOS, you can define the secret in a YAML file and then create the object using the `apply` command in the CLI. The YAML file will define various configurations of the Secret resource, such as name, version, type, etc. The `apply` command will create the secret in DataOS and make it available to other resources.

## Implementation Procedure

### **Create a YAML File for the Secret Resource**

Create a YAML file for the Secret resource, specifying the various fields. A sample file is given below. To learn more about the various fields within the Secret YAML, click on the link below.

```yaml
version: v1 # Manifest Version
name: testing # Name of the Secret Resource
type: secret # Resource type here is Secret
description: a very special test secret # Description of the Secret Resource
secret: # Secret Section
  type: key-value 
  acl: r # Access Control List (ACL) - r|rw
  data: # Data Section (specify the credentials here as key-value pair
    username: iamgroot # Key-Value Pairs
    password: asgard@thor
```

### **Apply the Secret YAML**

Apply the Secret YAML via the CLI, by specifying the YAML’s path and the workspace. The apply command is given below.

```bash
dataos-ctl apply -f <path/secret.yaml> -w <name of the workspace>
```

**Sample**

```yaml
dataos-ctl apply -f Desktop/mysecret.yaml -w public
# Expected Output
INFO[0000] 🛠 apply...                                   
INFO[0000] 🔧 applying(public) testing:v1:secret... 
INFO[0007] 🔧 applying(public) testing:v1:secret...created 
INFO[0007] 🛠 apply...complete
```

### **Validate the Resource**

Use the get command to validate whether, the Secret resource has been properly created within the DataOS environment.

```yaml
dataos-ctl get -t secret -w <workspace>
```

**Sample**

```yaml
dataos-ctl get -t secret -w public
# Expected Output
INFO[0000] 🔍 get...                                     
INFO[0001] 🔍 get...complete                             

       NAME       | VERSION |  TYPE  | WORKSPACE | STATUS | RUNTIME |    OWNER     
------------------|---------|--------|-----------|--------|---------|--------------
     testing      |   v1    | secret | public    | active |         |   iamgroot
```