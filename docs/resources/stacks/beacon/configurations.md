# Structure of a Beacon Service YAML

```yaml
version: v1 
name: beacon-service 
type: service 
service:
	# ...
	# ...
	# ... 
  stack: beacon+rest 
	envs:
    PGRST_OPENAPI_SERVER_PROXY_URI: https://${{dataos-context}}/${{path}}

# Beacon Stack-specific Section
  beacon:
    source: 
      type: database 
      name: retail01 
      workspace: public 
	  topology: 
	  - name: database 
	    type: input
	    doc: retail database connection
	  - name: graphql-api
	    type: output
	    doc: serves up the retail database as a GraphQL API
	    dependencies:
	    - database
```

## Environment Variables

### **`PGRST_OPENAPI_SERVER_PROXY_URI`**

While creating a Beacon Service with a `beacon+rest` stack, you need to specify the environment variable `PGRST_OPENAPI_SERVER_PROXY_URI` given below:

```yaml
envs:
  PGRST_OPENAPI_SERVER_PROXY_URI: https://${{dataos-context}}/${{database-path}}
# Replace the ${{dataos-context}} and ${{database-path}} with your DataOS Full Context Name and Postgres Datbase path respectively
```

## Beacon Stack-specific Section

### **`source`**

<b>Description:</b> the Source section contains attributes for the data source <br>

| **Data Type**    | **Requirement** | **Default Value** | **Possible Value** |
|------------------|-----------------|-------------------|-------------------|
| mapping          | mandatory       | none              | none              |

<b>Example Usage:</b>

```yaml
source:
  type: database
  name: retail01 
  workspace: public
```

---

### **`type`**

<b>Description:</b> type of source <br>

| **Data Type**    | **Requirement** | **Default Value** | **Possible Value** |
|------------------|-----------------|-------------------|-------------------|
| string          | mandatory       | none              | database           |

<b>Example Usage:</b>

```yaml
type: database
```

---

### **`name`**

<b>Description:</b> data source name <br>

| **Data Type**    | **Requirement** | **Default Value** | **Possible Value** |
|------------------|-----------------|-------------------|-------------------|
| string          | mandatory       | none              | any string confirming the regex         |

<b>Example Usage:</b>

```yaml
name: ordersumdb
```

---

### **`workspace`**

<b>Description:</b> DataOS workspace where the source exists. <br>

| **Data Type**    | **Requirement** | **Default Value** | **Possible Value** |
|------------------|-----------------|-------------------|-------------------|
| string          | mandatory       | public              | any available workspace within DataOS         |

<b>Example Usage:</b>

```yaml
name: ordersumdb
```

---

### **`topology`**

<b>Description:</b> topology refers to the physical or logical arrangement of the different components of a PostgreSQL system, such as inputs, outputs, etc. <br>

| **Data Type**    | **Requirement** | **Default Value** | **Possible Value** |
|------------------|-----------------|-------------------|-------------------|
| list of mappings          | mandatory       | none              | none         |

<b>Example Usage:</b>

```yaml
topology:
- name: database 
  type: input 
  doc: retail database connection 
- name: graphql-api 
  type: output 
  doc: serves up the retail database as a REST API 
  dependencies: 
  - database
```

### **`name`**

<b>Description:</b> name of a particular topology. <br>

| **Data Type**    | **Requirement** | **Default Value** | **Possible Value** |
|------------------|-----------------|-------------------|-------------------|
| string          | mandatory       | none              | any string         |

<b>Example Usage:</b>

```yaml
name: database
```

---

### **`type`**

<b>Description:</b> types of topology. <br>

| **Data Type**    | **Requirement** | **Default Value** | **Possible Value** |
|------------------|-----------------|-------------------|-------------------|
| string          | mandatory       | none              | input/output         |

<b>Example Usage:</b>

```yaml
type: input
```

---

### **`doc`**

<b>Description:</b> this field is to document the steps done in this step <br>

| **Data Type**    | **Requirement** | **Default Value** | **Possible Value** |
|------------------|-----------------|-------------------|-------------------|
| string          | optional       | none              | any string         |

<b>Example Usage:</b>

```yaml
doc: serves up the retail database as a REST API 
```

---

### **`dependencies`**

<b>Description:</b> this field is used to define the dependencies between steps. <br>

| **Data Type**    | **Requirement** | **Default Value** | **Possible Value** |
|------------------|-----------------|-------------------|-------------------|
| string          | mandatory       | none              | valid name within the topology         |

<b>Example Usage:</b>

```yaml
dependencies: 
  - database
```