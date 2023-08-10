# Case Scenario: Table Properties


## List Properties

To obtain the list of properties, execute the following command within the DataOS.

**Command**

```shell
dataos-ctl dataset properties -a {{udl}}
```

**Example**

```shell
dataos-ctl dataset properties -a dataos://icebase:retail/city
```

Output (Successful Execution)

```shell
INFO[0000] 📂 get properties...                          
INFO[0000] 📂 get properties...completed                 

           PROPERTY NAME           | PROPERTY VALUE  
-----------------------------------|-----------------
  write.metadata.compression-codec | gzip
```

Above, we can see the pre-defined property `write.metadata.compression-codec` whose value is `gzip`

## Add Properties

To add a single property the below code can be used. 

**Command**

```shell
dataos-ctl dataset add-properties -a {{udl}} \
-p "{{property-name}}:{{property-value}}"
```

To add multiple properties at the same time, use:

```shell
dataos-ctl dataset add-properties -a dataos://icebase:retail/city \
-p "{{property-name}}:{{property-value}}" \
-p "{{property-name}}:{{property-value}}"
```

**Example**

Let’s say we want to add a new property by the name `write.metadata.metrics.default` and set its value to `full`. To do this, execute the following code:

```shell
dataos-ctl dataset add-properties -a dataos://icebase:retail/city \
-p write.metadata.metrics.default:full
```

Output (on successful execution)

```shell
INFO[0000] 📂 add properties...                          
INFO[0000] 📂 add properties...completed
```

To check whether the property is added or not, run the list properties command:

```shell
dataos-ctl dataset properties -a dataos://icebase:retail/city
```

Output

```shell
INFO[0000] 📂 get properties...                          
INFO[0000] 📂 get properties...completed                 

           PROPERTY NAME           | PROPERTY VALUE  
-----------------------------------|-----------------
  write.metadata.metrics.default   | full            
  write.metadata.compression-codec | gzip
```

As we can see, the property has been successfully added.

## Remove Properties

To remove a property, the following command can be used.

**Command**

```shell
dataos-ctl dataset remove-properties -a {{udl}} \
-p "{{property-name}}" \
-p "{{property-name}}"
```

**Example**

Let’s say we want to remove the property `write.metadata.metrics.default`. To accomplish this, execute the following code:

```shell
dataos-ctl dataset remove-properties -a dataos://icebase:retail/city \
-p write.metadata.metrics.default
```

Output (successful execution)

```shell
INFO[0000] 📂 remove properties...                       
INFO[0001] 📂 remove properties...completed
```

To check whether the property is deleted or not, use the list properties command.

```shell
dataos-ctl dataset properties -a dataos://icebase:retail/city
```

```shell
INFO[0000] 📂 get properties...                          
INFO[0000] 📂 get properties...completed                 

           PROPERTY NAME           | PROPERTY VALUE  
-----------------------------------|-----------------
  write.metadata.compression-codec | gzip
```

As can be observed, the property is successfully deleted.