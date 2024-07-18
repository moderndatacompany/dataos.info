---
title: CLI Stack
search:
  boost: 2
---

# CLI Stack

The DataOS Command-Line Interface (CLI) interface, or the **dataos-ctl**, can be operated as a [Stack](/resources/stacks/), allowing users to programmatically execute CLI commands using the YAML manifest and automate the process of command execution and Resource lifecycle management.

The dataos-ctl stack can be orchestrated using a [Workflow](/resources/workflow/) Resource, where each job executes the command once and concludes the process upon completion. This plays a pivotal role in enabling Continuous Integration and Continuous Deployment (CI/CD) workflows that integrate multiple CLI commands, creating a cohesive and automated deployment process.

## Necessity of CLI Stack

The **dataos-ctl** Stack significantly enhances the developer experience by simplifying resource lifecycle management. In the absence of the CLI stack, data developers faced a fragmented experience when managing resource lifecycles. Tasks such as creating a Depot involved multiple steps, including creating a YAML manifest, applying it through the DataOS CLI shell, and validating the creation with a separate get command.

With the CLI stack, data developers can now manage the entire lifecycle of resources seamlessly. By crafting a single YAML manifest for a Workflow, developers can execute the apply command using the CLI stack within a job that incorporates the specifications for the depot. Subsequently, executing the get command is seamlessly integrated into the Workflow as another job with a dependency on the initial job. This eliminates the need for manual back-and-forth transitions between the code editor and command line shell.

## How to use CLI Stack?

Utilizing CLI Stack involves a series of logical steps, as outlined below:

1. [Create an Instance Secret manifest](#create-an-instance-secret)
2. [Apply the Instance Secret manifest](#apply-the-instance-secret-manifest)
3. [Create a Workflow manifest](#create-a-workflow-manifest)
4. [Apply the Workflow manifest](#apply-the-workflow-manifest)
5. [Verify Workflow creation](#verify-workflow-creation)
6. [Check Workflow Logs to validate execution](#check-workflow-logs-to-validate-execution)

### **Create an Instance Secret manifest**

To execute a resource using this stack, users need to provide their API key and User ID. This information can be supplied using the an Instance secret. First create an instance secret Resource and then refer this secret within the Workflow Resource.

To fetch the details about the User ID and User API Key token, execute the following commands after logging into DataOS:

```shell
dataos-ctl user get

# Sample Output
INFO[0000] 😃 user get...                                
INFO[0000] 😃 user get...complete                        

      NAME     │     ID      │  TYPE  │        EMAIL         │              TAGS               
───────────────┼─────────────┼────────┼──────────────────────┼─────────────────────────────────
  IamGroot     │  **iamgroot**   │ person │   iamgroot@tmdc.io   │ roles:id:data-dev,              
               │             │        │                      │ roles:id:operator,              
               │  # user_id  │        │                      │ roles:id:system-dev,            
               │             │        │                      │ roles:id:user,                  
               │             │        │                      │ users:id:iamgroot
```

For User API key token, execute the commands:

```shell
# if apikey token already exists execute
dataos-ctl user apikey get

# if no apikey token exists, create a new one using
dataos-ctl user apikey create

# Sample Output

INFO[0000] 🔑 user apikey get...                         
INFO[0000] 🔑 user apikey get...complete                 

                   TOKEN                     │  TYPE  │      EXPIRATION      │    NAME                   
────────────────────────────────────────────────────────────────────────────────────────────
  **abcdefghijklmnopqrstuvwxyzabcdefghijklmnop** │ apikey │ 2023-12-29T14:00:00Z │ token_abcd
				# dataos_user_apikey_token
```

Replace `${{dataos_user_id}}` and `${{dataos_user_apikey_token}}` with values obtained from the commands above in the Secret Manifest provided below:

```yaml
# Resource meta section
name: ${{dataos-ctl-user-apikey}} 
version: v1
type: instance-secret
layer: user

# Instance-secret specific section
instance-secret:
  type: key-value
  acl: rw
  data:
    USER_ID: ${{dataos_user_id}} 
    APIKEY: ${{dataos_user_apikey_token}}
```

### **Apply the Instance Secret manifest**

```shell
dataos-ctl apply -f ${{instance secret yaml file path}}

# Expected Output
INFO[0000] 🛠 apply...                                   
INFO[0000] 🔧 applying dataos-ctl-user-apikey:v1:instance-secret... 
INFO[0002] 🔧 applying dataos-ctl-user-apikey:v1:instance-secret...created 
INFO[0002] 🛠 apply...complete
```

### **Create a Workflow manifest**

The DataOS CLI Stack can be orchestrated using the Resource-type Workflow. 

The Sample YAML for a Workflow that creates a Volume, checks its status, and deletes it is provided below:

```yaml
# Resource meta section
name: dataos-ctl-volume-lifecycle-01
version: v1
type: workflow

# Workflow-specific section
workflow:
  dag:

# First Job
  - name: create-volume
    spec:
      stack: dataos-ctl # dataos-ctl stack name
      compute: runnable-default

		# Referred Instance secrets 
      dataosSecrets:
      - name: dataos-ctl-user-apikey # Instance secret name same as declared above
        allKeys: true
        consumptionType: envVars

		# Stack-specific section
      stackSpec:
        arguments:
        - resource
        - apply
        - -f
        - /etc/dataos/config/manifest.yaml
        - -w
        - ${CURRENT_WORKSPACE}

		# Manifest for the Resource against which the above command is executed
        manifest:
          version: v1beta
          name: "temp001"
          type: volume
          volume:
            size: 1Gi
            accessMode: ReadWriteMany
            type: temp

# Second Job
  - name: get-volume
    spec:
      stack: dataos-ctl
      compute: runnable-default

		# Referred Instance secrets 
      dataosSecrets:
      - name: dataos-ctl-user-apikey
        allKeys: true
        consumptionType: envVars

		# Stack-specific section
      stackSpec:
        arguments:
        - resource
        - get
        - -t
        - volume
        - -n
        - temp001
        - -w
        - ${CURRENT_WORKSPACE}
    dependencies:
    - create-volume # Second Job dependent on successful execution of First Job
```

### **Apply the Workflow manifest**

```shell
dataos-ctl apply -f ${{workflow yaml file path}} -w ${{workspace name}}

# Sample and Expected Output
dataos-ctl apply -f workflow/volume_lifecycle.yml
INFO[0000] 🛠 apply...                                   
INFO[0000] 🔧 applying(public) dataos-ctl-volume-lifecycle-01:v1:workflow... 
INFO[0005] 🔧 applying(public) dataos-ctl-volume-lifecycle-01:v1:workflow...created 
INFO[0005] 🛠 apply...complete
```

### **Verify Workflow creation**

```shell
dataos-ctl get -t workflow -w ${{workspace name}}

# Sample Output
INFO[0000] 🔍 get...
INFO[0001] 🔍 get...complete

          NAME        | VERSION |   TYPE   | WORKSPACE | STATUS | RUNTIME |   OWNER
----------------------|---------|----------|-----------|--------|---------|-------------
  **cnt-product-demo-01 | v1      | workflow | public**    | active | running |   iamgroot
```

### **Check Workflow Logs to validate execution**

Copy the name to Workspace from the output table of the [`get`](/interfaces/cli/command_reference/#get) command and use it as a string in the delete command.

```shell
dataos-ctl -i "${{copy the name to workspace in the output table from get command}}" --node ${{failed node name from get runtime command}} log

# Sample
dataos-ctl -i "dataos-ctl-volume-lifecycle-01 | v1      | workflow | public" log                                                                                             
# Expected Output
INFO[0000] 📃 log(public)...                             
INFO[0003] 📃 log(public)...complete                     

        NODE NAME       │ CONTAINER NAME │ ERROR  
────────────────────────┼────────────────┼────────
  create-volume-execute │ main           │        

-------------------LOGS-------------------
time="2023-12-29T05:43:58Z" level=info msg="🛠 apply..."
time="2023-12-29T05:43:58Z" level=info msg="🔧 applying(public) temp001:v1beta:volume..."
time="2023-12-29T05:43:59Z" level=info msg="🔧 applying(public) temp001:v1beta:volume...created"
time="2023-12-29T05:43:59Z" level=info msg="🛠 apply...complete"
time="2023-12-29T05:44:00.092Z" level=info msg="sub-process exited" argo=true error="<nil>"

      NODE NAME      │ CONTAINER NAME │ ERROR  
─────────────────────┼────────────────┼────────
  get-volume-execute │ main           │        

-------------------LOGS-------------------
time="2023-12-29T05:44:08Z" level=info msg="🔍 get..."
time="2023-12-29T05:44:08Z" level=info msg="🔍 get...complete"

   NAME   | VERSION |  TYPE  | WORKSPACE | STATUS | RUNTIME |   OWNER     
----------|---------|--------|-----------|--------|---------|--------------
  temp001 | v1beta  | volume | public    | active |         |  iamgroot  

time="2023-12-29T05:44:09.135Z" level=info msg="sub-process exited" argo=true error="<nil>"
```

## Case Scenario

- [How to apply a Service and get runtime status of it using CLI Stack?](/resources/stacks/cli_stack/apply_a_service_and_get_runtime_status_using_cli_stack/)