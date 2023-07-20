# Flare Steps Section Grammar

In the `steps` section, a series of sequences are defined to execute the necessary actions for performing transformations or applying Flare Functions and SQL queries.

## Structure of Steps Section

```yaml
steps:
  - sequence:
    - name: top_100_accounts
      doc: this step is to document
      sql: select * from account_connect limit 100
      classpath: io.dataos.custom.step.Step.class
      functions:
        - name: set_type
          columns:
            account_id: string
      commands:
        - name: persist
          sequenceName: account_connect
          mode: MEMORY_AND_DISK
```

## Configuration Fields


### **`steps`**
<b>Description:</b> specifies flare steps section attributes. This may include one or more sequences to execute the steps defined for performing any transformation or applying any flare function or command.  <br>
<b>Data Type:</b> list of objects <br>
<b>Requirement:</b> mandatory <br>
<b>Default Value:</b> none <br>
<b>Possible Value:</b> none <br>
<b>Example Usage:</b>

```yaml
steps:
  - sequence:
    - name: transformation-1 
      sql: select * from account limit 10 
    - name: transformation-2 
      sql: select * from account limit 30 
```

---

### **`sequence`**
<b>Description:</b> sequence contain a list of steps to be executed in a sequential manner. One can add multiple such sequences. One can envision each intermediate step in a sequence as an action that results in a view that can be referred to in subsequent steps or outputs. In this section, flare will try to run supplied SQL and associated functions and commands. <br>
<b>Data Type:</b> object <br>
<b>Requirement:</b> mandatory <br>
<b>Default Value:</b> none <br>
<b>Possible Value:</b> none <br>
<b>Example Usage:</b>

```yaml
sequence:
  {} 
```

---

### **`name`**
<b>Description:</b> name assigned to one of the views you want to sink as an output dataset. <br>
<b>Data Type:</b> string <br>
<b>Requirement:</b> mandatory <br>
<b>Default Value:</b> none <br>
<b>Possible Value:</b> none <br>
<b>Example Usage:</b>

```yaml
name: top_100_accounts
```

---

### **`doc`**
<b>Description:</b> description of SQL/transformation <br>
<b>Data Type:</b> string <br>
<b>Requirement:</b> optional <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> any string<br>
<b>Example Usage:</b>

```yaml
doc: this step is to document
```

---

### **`sql`**
<b>Description:</b> sql steps to transform your data. <br>
<b>Data Type:</b> string <br>
<b>Requirement:</b> optional <br>
<b>Default Value:</b> none <br>
<b>Possible Value:</b> valid sql expression<br>
<b>Example Usage:</b>

```yaml
sql: select * from account_connect limit 100
```

---

### **`classpath`**
<b>Description:</b> custom logic/step implemented by the user and present in the classpath. <br>
<b>Data Type:</b> string <br>
<b>Requirement:</b> optional <br>
<b>Default Value:</b> none <br>
<b>Possible Value:</b> valid class name<br>
<b>Example Usage:</b>

```yaml
classpath: io.dataos.custom.step.Step.class
```

---

### **`functions`**
<b>Description:</b> flare functions declaration <br>
<b>Data Type:</b> object <br>
<b>Requirement:</b> optional <br>
<b>Default Value:</b> none <br>
<b>Possible Value:</b> any valid flare functions provided in the doc [here](../functions.md) <br>
<b>Example Usage:</b>

```yaml
functions:
  - name: set_type 
    columns:
    account_id: string 
```

---

### **`commands`**
<b>Description:</b> commands declaration <br>
<b>Data Type:</b> object <br>
<b>Requirement:</b> optional <br>
<b>Default Value:</b> none <br>
<b>Possible Value:</b> name: persist/unpersist, sequenceName: any valid sequence name <br>
<b>Example Usage:</b>

```yaml
commands:
  - name: persist
    sequenceName: account_connect
    mode: MEMORY_AND_DISK
```
