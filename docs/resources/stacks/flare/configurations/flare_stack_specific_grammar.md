# Flare Stack-specific Section Gramamr
```yaml
flare:
  driver:
    coreLimit: {{1000m}}
    cores: {{1}}
    memory: {{1024m}}
  executor:
    coreLimit: {{1000m}}
    cores: {{1}}
    instances: {{1}}
    memory: {{1024m}}
  job:
    explain: {{true}}
    logLevel: {{INFO}}
    streaming: # Streaming Section
    {}
    inputs: #Inputs Section
    {}
    outputs: #Outputs Section
    {}
    steps: # Steps Section
    {}
    assertions: # Assertions Section
    {}
    actions: # Actions Section
    {}
```

## Configuration Fields

### **`flare`**
**Description:** Flare Stack specific section. <br>
**Data Type:** object <br>
**Requirement:** mandatory <br>
**Default Value:** none <br>
**Possible Value:** none <br>
**Example Usage:**
```yaml
flare: {}
```

---

### **`driver`**
**Description:** the driver is the controller node of the operation and controls the operations of the workflow. <br>
**Data Type:** object <br>
**Requirement:** optional <br>
**Default Value:** none <br>
**Possible Value:** none <br>
**Example Usage:**
```yaml
driver:
  coreLimit: 1000m
  cores: 1
  memory: 1024m
```

---

### **`executor`**
**Description:** the executor is the worker node that performs the operations defined in the workflow and sends the result back to the driver. It must interface with the cluster manager in order to actually get physical resources and launch executors. <br>
**Data Type:** object <br>
**Requirement:** optional <br>
**Default Value:** none <br>
**Possible Value:** none <br>
**Example Usage:**
```yaml
executor:
  coreLimit: 2000m
  cores: 2
  instances: 2
  memory: 1024m
```

---

### **`job`**
**Description:** jobs can be defined as the steps to complete any action such as loading initial data, updating data, or writing data to sink. <br>
**Data Type:** object <br>
**Requirement:** mandatory <br>
**Default Value:** none <br>
**Possible Value:** none <br>
**Example Usage:**
```yaml
job: {}
```

---

### **`explain`**
**Description:** use this flag to print the spark logical/physical plans in the logs. <br>
**Data Type:** boolean <br>
**Requirement:** optional <br>
**Default Value:** false <br>
**Possible Value:** true/false <br>
**Example Usage:**
```yaml
explain: true
```

---

### **`logLevel`**
**Description:** a log level is a piece of information from a given log message that distinguishes log events from each other. It helps in finding runtime issues with your Flare Stack and in troubleshooting. <br>
**Data Type:** string <br>
**Requirement:** optional <br>
**Default Value:** INFO <br>
**Possible Value:** INFO / WARN / DEBUG/ ERROR <br>
**Example Usage:**
```yaml
logLevel: INFO
```

---


### **`streaming`**
**Description:** the streaming section contains key-value properties related to executing the stream jobs. <br>
**Data Type:** object <br>
**Requirement:** optional <br>
**Default Value:** none <br>
**Possible Value:** none <br>
**Additional Information:** more information regarding the `streaming` section can be found [here](./streaming.md) <br>
**Example Usage:**
```yaml
streaming: {}
```

---

### **`inputs`**
**Description:** contains dataset details for reading data from supported data sources. <br>
**Data Type:** object <br>
**Requirement:** mandatory <br>
**Default Value:** none <br>
**Possible Value:** none <br>
**Additional Information:** more information regarding the `inputs` section can be found [here](./inputs.md) <br>
**Example Usage:**
```yaml
inputs: {}
```

---

### **`steps`**
**Description:** one or more sequences to execute the steps defined for performing any transformation or applying any flare function or command. <br>
**Data Type:** object <br>
**Requirement:** mandatory <br>
**Default Value:** none <br>
**Possible Value:** none <br>
**Additional Information:** more information regarding the `steps` section can be found [here](./steps.md) <br>
**Example Usage:**
```yaml
steps: {}
```

---

### **`outputs`**
**Description:** contains dataset details for writing data to supported data sources. <br>
**Data Type:** object <br>
**Requirement:** mandatory <br>
**Default Value:** none <br>
**Possible Value:** none <br>
**Additional Information:** more information regarding the `outputs` section can be found [here](./outputs.md) <br>
**Example Usage:**
```yaml
outputs: {}
```

---

### **`assertions`**
**Description:** assertions allow you to perform validation checks on top of pre-written datasets. They are defined under the assertions section. <br>
**Data Type:** object <br>
**Requirement:** optional <br>
**Default Value:** none <br>
**Possible Value:** none <br>
**Additional Information:** more information regarding the `assertions` section can be found [here](./assertions.md) <br>
**Example Usage:**
```yaml
assertions: {}
```

---

### **`actions`**
**Description:** Iceberg-specific actions are defined in the actions section. <br>
**Data Type:** object <br>
**Requirement:** optional <br>
**Default Value:** none <br>
**Possible Value:** none <br>
**Additional Information:** more information regarding the `actions` section can be found [here](./actions.md) <br>
**Example Usage:**
```yaml
actions: {}
```