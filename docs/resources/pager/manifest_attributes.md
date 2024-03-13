# Attributes of Pager manifest

## Structure of a Pager manifest

```yaml
pager:
  conditions:
    - valueJqFilter: ${value-jq-filter}
      operator: ${operator}
      value: ${value}
  output:
    email:
      emailTargets:
        - ${email}
        - ${email}
    msTeams:
      webHookUrl: ${web-hook-url}
    webHook:
      url: ${web-hook-url}
      headers: 
        ${key}: ${value}
      authorization:
        token: ${token}
        customHeader: ${customHeader}
      verb: ${http-operation}
      bodyTemplate: ${body-template}
```


## `pager`

**Description:** The `pager` attribute is a mapping that encapsulates attributes-specific for configuring a Pager's functionalities, including conditions and output destinations.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | mandatory | none | valid Pager-specific attributes |

**Example Usage:**

```yaml
pager:
  conditions:
    - valueJqFilter: .properties.name
      operator: equals
      value: malfunctiondatatool
    - valueJqFilter: .properties.incident_type
      operator: equals
      value: malfunctionsystem
  output:
    webHook:
      url: https://example.com/webhook
      verb: post
```

---

### **`conditions`**

**Description:** The `conditions` attribute defines the conditions that the Pager Service will use as an input for matching conditions against all active Pagers, identifying the one that meets the specified criteria, and then execute it for triggering pager alert. A single conditions involves declaration of three specific attributes

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list of mapping | mandatory | none | none |

**Example Usage:**

```yaml
pager:
  conditions:
    - valueJqFilter: "${string}"
      operator: "${equals}"
      value: "string"
```

---

### **`output`**

**Description:** The `output` attribute under `pager` specifies the destinations where pager notifications will be sent.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | mandatory | none | none |

**Example Usage:**

```yaml
pager:
  output:
    email:
      emailTargets:
        - "<email 1>"
        - "<email 2>"
    msTeams:
      webHookUrl: 
    webHook:
      url: "${webhook-url}"
      headers: <object>
      authorization:
        token: "${token}"
        customHeader: "${customHeader}"
      verb: GET
      bodyTemplate: "<string>"
```

---

### **`email`**

**Description:** The `email` attribute under `pager.output` specifies email destinations for pager notifications.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | mandatory | none | none |

**Example Usage:**

```yaml
pager:
  output:
    email:
      emailTargets:
        - "<email 1>"
        - "<email 2>"
```

---

### **`emailTargets`**

**Description:** The `emailTargets` attribute under `pager.output.email` specifies the email addresses to which pager notifications will be sent.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list | mandatory | none | none |

**Example Usage:**

```yaml
pager:
  output:
    email:
      emailTargets:
        - "<email 1>"
        - "<email 2>"
```

---

### **`msTeams`**

**Description:** The `msTeams` attribute under `pager.output` specifies the Microsoft Teams webhook URL for pager notifications.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | mandatory | none | none |

**Example Usage:**

```yaml
pager:
  output:
    msTeams:
      webHookUrl: 
```

---

### **`webHook`**

**Description:** The `webHook` attribute under `pager.output` specifies a webhook destination for pager notifications.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | mandatory | none | none |

**Example Usage:**

```yaml
pager:
  output:
    webHook:
      url: "${webhook-url}"
      headers: <object>
      authorization:
        token: "${token}"
        customHeader: "${customHeader}"
      verb: GET
      bodyTemplate: "<string>"
```

---

### **`url`**

**Description:** The `url` attribute under `pager.output.webHook` specifies the URL of the webhook destination for pager notifications.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | valid URL |

**Example Usage:**

```yaml
pager:
  output:
    webHook:
      url: "${webhook-url}"
```

---

### **`headers`**

**Description:** The `headers` attribute under `pager.output.webHook` specifies any additional headers to be included in the webhook request.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| object | optional | none | valid HTTP headers |

**Example Usage:**

```yaml
pager:
  output:
    webHook:
      headers: 
        Content-Type: "application/json"
```

---

### **`authorization`**

**Description:** The `authorization` attribute under `pager.output.webHook` specifies the authorization details for accessing the webhook URL.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | optional | none | none |

**Example Usage:**

```yaml
pager:
  output:
    webHook:
      authorization:
        token: "${token}"
        customHeader: "${customHeader}"
```

---

### **`token`**

**Description:** The `token` attribute under `pager.output.webHook.authorization` specifies the authorization token for accessing the webhook URL.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | valid authorization token |

**Example Usage:**

```yaml
pager:
  output:
    webHook:
      authorization:
        token: "${token}"
```

---

### **`customHeader`**

**Description:** The `customHeader` attribute under `pager.output.webHook.authorization` specifies any custom header to be included in the webhook request for authorization purposes.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | valid HTTP header |

**Example Usage:**

```yaml
pager:
  output:
    webHook:
      authorization:
        customHeader: "${customHeader}"
```

---

### **`verb`**

**Description:** The `verb` attribute under `pager.output.web

Hook` specifies the HTTP verb to be used in the webhook request (e.g., GET, POST, PUT, DELETE).

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | GET, POST, PUT, DELETE |

**Example Usage:**

```yaml
pager:
  output:
    webHook:
      verb: GET
```

---

### **`bodyTemplate`**

**Description:** The `bodyTemplate` attribute under `pager.output.webHook` specifies the template to be used for the body of the webhook request.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | valid template string |

**Example Usage:**

```yaml
pager:
  output:
    webHook:
      bodyTemplate: "<string>"
```