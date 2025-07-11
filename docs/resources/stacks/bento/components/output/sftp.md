# sftp

!!! waning "BETA"

        This component is mostly stable but breaking changes could still be made outside of major version releases if a fundamental problem with the component is found.

Writes files to an SFTP server. This processor was introduced in version 1.0.0.

## YAML Configuration

```yaml
# Config fields, showing default values
output:
  label: ""
  sftp:
    address: "" # No default (required)
    path: "" # No default (required)
    codec: all-bytes
    credentials:
      username: ""
      password: ""
      private_key_file: ""
      private_key_pass: ""
    max_in_flight: 64
```





In order to have a different path for each object you should use function interpolations described [here](/resources/stacks/bento/configurations/interpolation/).

## Performance

This output benefits from sending multiple messages in flight in parallel for improved performance. You can tune the max number of in flight messages (or message batches) with the field `max_in_flight`.

## Fields

---

### **`address`**

The address of the server to connect to.

Type: `string`

---

### **`path`**

The file to save the messages to on the server. This field supports interpolation functions.

Type: `string`

---

### **`codec`**

The way in which the bytes of messages should be written out into the output data stream. It's possible to write lines using a custom delimiter with the delim:x codec, where x is the character sequence custom delimiter.

Type: `string`
Default: `"all-bytes"`

| Option	| Summary |
|---|---|
|`all-bytes` |	Only applicable to file based outputs. Writes each message to a file in full, if the file already exists the old content is deleted.|
|`append` |	Append each message to the output stream without any delimiter or special encoding.|
|`delim:x` |	Append each message to the output stream followed by a custom delimiter.|
|`lines` |	Append each message to the output stream followed by a line break.|


```yaml
# Examples

codec: lines

codec: "delim:\t"

codec: delim:foobar
```


---

### **`credentials`**

The credentials to use to log into the target server.

Type: `object`

---

### **`credentials.username`**

The username to connect to the SFTP server.

Type: `string`
Default: `""`

---

### **`credentials.password`**

The password for the username to connect to the SFTP server.

!!! warning "Secret"

        This field contains sensitive information that usually shouldn't be added to a config directly, read Secret](/resources/stacks/bento/configurations/secrets/) page for more info.


Type: `string`
Default: `""`

---

### **`credentials.private_key_file`**

The private key for the username to connect to the SFTP server.

Type: `string`
Default: `""`

---

### **`credentials.private_key_pass`**

Optional passphrase for private key.

!!! warning "Secret"

        This field contains sensitive information that usually shouldn't be added to a config directly, read Secret](/resources/stacks/bento/configurations/secrets/) page for more info.

Type: `string`
Default: `""`

---

### **`max_in_flight`**

The maximum number of messages to have in flight at a given time. Increase this to improve throughput.

Type: `int`
Default: `64`

