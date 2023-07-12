# Flare Streaming Section Grammar

Within the Flare Job's `streaming` section, users can define the attributes for streaming. 

## Structure of the `streaming` Section

```yaml
streaming:
  triggerMode: ProcessingTime #(Optional)
  triggerDuration: 10 seconds #(Optional)
  outputMode: append #(Optional)
  checkpointLocation: /tmp/checkpoint #(Optional)
  forEachBatchMode: true #(Optional)
  extraOptions:
    opt: val #(Optional)
```
<center><i> Flare Streaming Section YAML Configuration </i></center>

## Configuration Fields

### **`streaming`**
<b>Description:</b> set options for each batch streaming writing or setting default streaming configuration.<br>
<b>Data Type:</b> object <br>
<b>Requirement:</b> optional<br>
<b>Default Value:</b> none <br>
<b>Possible Value:</b> none <br>
<b>Example Usage:</b>

```yaml
streaming:
  {}
```

---

### **`triggerMode`**
<b>Description:</b> sets the trigger mode<br>
<b>Data Type:</b> string <br>
<b>Requirement:</b> optional <br>
<b>Default Value:</b> none <br>
<b>Possible Value:</b> ProcessingTime/Once/Continuous/AvailableNow<br>
<b>Example Usage:</b>

```yaml
triggerMode: ProcessingTime
```

---

### **`triggerDuration`**
<b>Description:</b>sets the trigger duration if the trigger is ProcessingTime/Continuous <br>
<b>Data Type:</b> string <br>
<b>Requirement:</b> optional <br>
<b>Default Value:</b> none <br>
<b>Possible Value:</b> ProcessingTime/Once/Continuous/AvailableNow<br>
<b>Example Usage:</b>

```yaml
triggerDuration: 10 seconds
```

---

### **`outputMode`**
<b>Description:</b> Output Mode <br>
<b>Data Type:</b> string <br>
<b>Requirement:</b> optional <br>
<b>Default Value:</b> none <br>
<b>Possible Value:</b> append/replace/complete<br>
<b>Example Usage:</b>

```yaml
outputMode: append
```

---

### **`checkpointLocation`**
<b>Description:</b> Specifies checkpoint location <br>
<b>Data Type:</b> string <br>
<b>Requirement:</b> optional <br>
<b>Default Value:</b> none <br>
<b>Possible Value:</b> valid path<br>
<b>Example Usage:</b>

```yaml
checkpointLocation: /tmp/checkpoint
```

---

### **`forEachBatchMode`**
<b>Description:</b> use forEachBatchMode when writing streams enables writing to all available writers and to write to multiple outputs. <br>
<b>Data Type:</b> boolean <br>
<b>Requirement:</b> optional <br>
<b>Default Value:</b> false <br>
<b>Possible Value:</b> true/false<br>
<b>Example Usage:</b>

```yaml
forEachBatchMode: true
```

---

### **`extraOptions`**
<b>Description:</b> add any other options supported by the DataStreamWriter <br>
<b>Data Type:</b> map <br>
<b>Requirement:</b> optional <br>
<b>Default Value:</b> none <br>
<b>Possible Value:</b> none<br>
<b>Example Usage:</b>

```yaml
extraOptions:
   opt: val 
```