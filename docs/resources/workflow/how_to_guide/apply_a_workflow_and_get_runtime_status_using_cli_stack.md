# Apply a Workflow and get runtime status using CLI Stack

The dataos-ctl stack called [CLI Stack](/resources/stack/cli_stack) can be orchestrated using a Workflow Resource, where each job executes the command once and concludes the process upon completion. This plays a pivotal role in enabling Continuous Integration and Continuous Deployment (CI/CD) workflows that integrate multiple CLI commands, creating a cohesive and automated deployment process.

## How to use CLI Stack?

Utilizing CLI Stack involves a series of logical steps, as outlined below:

1. [Create an Instance Secret manifest](#create-an-instance-secret-manifest)
2. [Apply the Instance Secret manifest](#apply-the-instance-secret-manifest)
3. [Create a Workflow manifest](#create-a-workflow-manifest)
4. [Apply the Workflow manifest](#apply-the-workflow-manifest)
5. [Verify Workflow creation](#verify-workflow-creation)
6. [Check Workflow Logs to validate execution](#check-workflow-logs-to-validate-execution)

### **Create an Instance Secret manifest**

To execute a resource using this stack, users need to provide their API key and User ID. This information can be supplied using the an Instance secret. First create an instance secret Resource and then refer this secret within the Workflow Resource.

To fetch the details about the User ID and User API Key token, execute the following commands after logging into DataOS:


=== "Command 1"

    To fetch the details about the User ID

    ```shell
    dataos-ctl user get
    # Sample Output
    INFO[0000] 😃 user get...                                
    INFO[0000] 😃 user get...complete                        

          NAME     │     ID      │  TYPE  │        EMAIL         │              TAGS               
    ───────────────┼─────────────┼────────┼──────────────────────┼─────────────────────────────────
      IamGroot     │ iamgroot    │ person │   iamgroot@tmdc.io   │ roles:id:data-dev,              
                  │             │        │                      │ roles:id:operator,              
                  │  # user_id  │        │                      │ roles:id:system-dev,            
                  │             │        │                      │ roles:id:user,                  
                  │             │        │                      │ users:id:iamgroot
    ```

=== "Command 2"

    For User API key token, if apikey token already exists execute command:

   

    ```shell
    dataos-ctl user apikey get
    #Expected Output
    |               TOKEN                                                       │  TYPE  │        EXPIRATION         │                  NAME                               
    ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
      jjjjjk5lX21hbGFtdXRlLmI4ZjRlNzc2LTYyNTAtNGI4MC05YTZhLTMwMzI3N2Y3Y2JhZQ==  │ apikey │ 2024-06-18T19:30:00+05:30 │ token_newly_entirely_divine_malamute     
      dG9rZW5faGFyZGx5X3BoLmI3NTcwZmFjLWZlNmEtNDE4NC1iNjA3LTc5MjM1ODVlNDQxYQ==  │ apikey │ 2024-06-28T05:30:00+05:30 │ token_hardly_physically_model_maggot     
      kkloZWxpY2F0ZV9zaGVlcC4xNmRkOTYwOS1mMjRhLTRiMWEtYTc0ZC0OTJjOTExYjE0ZTQ==  │ apikey │ 2024-06-28T05:30:00+05:30 │ token_grossly_socially_delicate_sheep    
    ```


=== "Command 3"

    If no apikey token exists, create a new one using the following command:

    ```shell
    dataos-ctl user apikey create
    # Sample Output
    INFO[0000] 🔑 user apikey get...                         
    INFO[0000] 🔑 user apikey get...complete                 

                       TOKEN                     │  TYPE  │      EXPIRATION      │    NAME                   
    ────────────────────────────────────────────────────────────────────────────────────────────
      abcdefghijklmnopqrstuvcdefghijklmnop │ apikey │ 2023-12-29T14:00:00Z │ token_abcd
            # dataos_user_apikey_token
    ```

Replace `${dataos_user_id}` and `${dataos_user_apikey_token}` with values obtained from the commands above in the Secret Manifest provided below:

=== "Syntax"

    ```yaml title="instance_secret_template.yml" hl_lines="12-13" 
    # Resource meta section
    name: ${dataos-ctl-user-apikey} 
    version: v1
    type: instance-secret
    layer: user

    # Instance-secret specific section
    instance-secret:
      type: key-value
      acl: rw
      data:
        USER_ID: ${dataos_user_id} 
        APIKEY: ${dataos_user_apikey_token}
    ```

=== "Example"


    ```yaml title="instance_secret_example.yml" hl_lines="12-13" 
    # Resource meta section
    name: dataos-ctl-user-apikey
    version: v1
    type: instance-secret
    layer: user

    # Instance-secret specific section
    instance-secret:
      type: key-value
      acl: rw
      data:
        USER_ID: iamgroot
        APIKEY: abcdefghijklmnopqrstuvwxyzabcd
    ```

### **Apply the Instance Secret manifest**


=== "Command"

    ```shell
    dataos-ctl apply -f ${instance secret yaml file path}
    ```

=== "Example"

    ```shell
    dataos-ctl apply -f home/iamgroot/workflow/instance_secret.yaml

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
--8<-- "examples/resources/workflow/apply_a_workflow_and_get_runtime_status_using_cli_stack.yaml"
```

### **Apply the Workflow manifest**

```shell
dataos-ctl apply -f ${workflow yaml file path} -w ${workspace name}

# Sample and Expected Output
dataos-ctl apply -f workflow/volume_lifecycle.yml
INFO[0000] 🛠 apply...                                   
INFO[0000] 🔧 applying(public) dataos-ctl-workflow-lifecycle-02:v1:workflow... 
INFO[0003] 🔧 applying(public) dataos-ctl-workflow-lifecycle-02:v1:workflow...created 
INFO[0003] 🛠 apply...complete                          
```

### **Verify Workflow creation**

```shell
dataos-ctl get -t workflow -w ${workspace name}

# Sample Output
INFO[0000] 🔍 get...                                     
INFO[0001] 🔍 get...complete                             

                NAME               | VERSION |   TYPE   | WORKSPACE | STATUS |  RUNTIME  |     OWNER       
-----------------------------------|---------|----------|-----------|--------|-----------|-----------------
  dataos-ctl-workflow-lifecycle-02 | v1      | workflow | public    | active | succeeded | iamgroot
  
  wf-tmdc-01                       | v1      | workflow | public    | active | succeeded | iamgroot
```

### **Check Workflow Logs to validate execution**

Copy the name to Workspace from the output table of the [`get`](/interfaces/cli/command_reference#get) command and use it as a string in the delete command.

=== "Command"

    ```shell
    dataos-ctl -i "${copy the name to workspace in the output table from get command}" --node ${failed node name from get runtime command} log
    ```

=== "Example"

    ```shell
    dataos-ctl -i "dataos-ctl-volume-lifecycle-01 | v1      | workflow | public" log                                                                                             
    # Expected Output

    INFO[0000] 📃 log(public)...                             
    INFO[0000] 📃 log(public)...complete                     

          NODE NAME       │ CONTAINER NAME │ ERROR  
    ───────────────────────┼────────────────┼────────
      get-workflow-execute │ main           │        

    -------------------LOGS-------------------
    time="2024-06-18T12:54:38Z" level=info msg="🔍 get..."
    time="2024-06-18T12:54:39Z" level=info msg="🔍 get...nothing"
    time="2024-06-18T12:54:39.818Z" level=info msg="sub-process exited" argo=true error="<nil>"

            NODE NAME        │ CONTAINER NAME │ ERROR  
    ──────────────────────────┼────────────────┼────────
      create-workflow-execute │ main           │        

    -------------------LOGS-------------------
    time="2024-06-18T12:54:18Z" level=info msg="🛠 apply... "
    time="2024-06-18T12:54:18Z" level=info msg="🔧 applying(public) wf-tmdc-01:v1:workflow..."
    time="2024-06-18T12:54:24Z" level=info msg="🔧 applying(public) wf-tmdc-01:v1:workflow...updated"
    time="2024-06-18T12:54:24Z" level=info msg="🛠 apply...complete"
    time="2024-06-18T12:54:24.734Z" level=info msg="sub-process exited" argo=true error="<nil>"
    ```