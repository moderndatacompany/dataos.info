# Create Application Token

## Prerequisites

Ensure that the user performing these steps has been assigned the `roles:id:operator` tag. This role is required to create and manage users.

## **Steps for an app-user creation and management via CLI**

This section details the steps to create an app-user, assign roles, generate API keys, and optionally delete the app-user in DataOS using the command-line interface (CLI).


### **1. Authenticate in the DataOS environment**

Authenticate in the DataOS environment by executing the following command in the DataOS CLI terminal:

```bash
dataos-ctl login
```

### **2. Create an app-user**

To create an app-user, execute the command below. Specify the name of the user, the type as `application`, and provide a unique user ID.

```bash
dataos-ctl user create -n <name-of-user> -t application -u <user-id>
```

<aside class="callout">
🗣 The user type must be set as `application`. Do not create a user with the type `person` for this purpose.

</aside>

**Example:**

The following command creates an app-user named `lakesearch_app_token` with the user ID `lakesearchapi`:

```bash
dataos-ctl user create -n lakesearch_app_token -t application -u lakesearchapi
```

### **3. Assign roles and permissions**

Grant roles and permissions to the app-user by applying tags.

**Syntax:**

```bash
dataos-ctl user tag add -i <user-id> -t roles:id:<role-name>
```

**Examples:**

To assign roles `system-dev` and `data-dev` to the app-user `lakesearchapi`, use:

```bash
dataos-ctl user tag add -i lakesearchapi -t roles:id:system-dev
dataos-ctl user tag add -i lakesearchapi -t roles:id:data-dev
```

Additional roles can be assigned as needed by repeating the command with appropriate role identifiers.

### **4. Generate API keys**

To enable the app-user to interact with external systems, generate an API key. Use the following **Syntax:**

```bash
dataos-ctl user apikey create -d <duration> -n <name-of-apikey> -i <user-id>
```

**Examples:**

- Create an API key for the `lakesearchapi` user valid for **9999 hours:**
    
    ```bash
    dataos-ctl user apikey create -d 9999h -n lakesearch_app_api -i lakesearchapi
    ```
    
- Generate an API key for a different app-user with a custom duration of **72 hours:**

    ```bash
    dataos-ctl user apikey create -d 72h -n lakesearch_app_api -i lakesearchapi
    ```