# file

Tags: Local

Stores each item in a directory as a file, where an item ID is the path relative to the configured directory.

## YAML Configurations

```yaml
# Config fields, showing default values
label: ""
file:
  directory: ""
```

This type currently offers no form of item expiry or garbage collection and is intended to be used for development and debugging purposes only.

## Fields

### **`directory`**

The directory within which to store items.

**Type:** `string`