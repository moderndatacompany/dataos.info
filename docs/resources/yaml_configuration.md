# YAML configuration files

This page has information on features of YAML which will be useful while writing the configuration files for DataOS Resources.

1. Parse multiple entities and resource-instances in a single YAML file.
To do this, use three dashes `---` to separate the two entities. For example, we can create a Depot while using the reference of a Secret in the same config file.
    
    ```yaml
    version: v1
    name: s3-pos-rw
    type: secret
    secret:
      type: key-value-properties
      acl: rw
      data:
        accesskeyid: 
        secretkey: 
        awsaccesskeyid: 
        awssecretaccesskey: 
    ---
    version: v1
    name:
    type: depot
    tags:
    layer: user
    depot:
      type: S3
      description:
      spec:
        bucket: 
        relativePath:
      external: true
    # using the 'Secret' created & stored previously
      dataosSecrets:   
        - name: s3-pos-rw
          workspace: public
          keys: 
            - public_s3-pos-rw
    ```
    
2. YAML supports mapping, which are unordered collections of key-value pairs. Mappings are represented using a colon followed by whitespace.
    
    ```yaml
    person:
      name: John Doe
      age: 30
    ```
    
    In the above example, `person` is a mapping with keys `name` & `age`, and their corresponding values.
    
3. YAML supports lists & arrays using the dash `-`  followed by a space. The list, in turn can have mappings or objects or simple key-value pairs.
    
    ```yaml
    fruits:
      - apple: no
      - banana:  
          price: 24
          rotten: yes
      - orange: dozen
    ---
    vegetables:
      - donoteat
      - tastesbad
    ```
    
    In the above example, `fruits` is a list of objects, while `vegetables` is an array.
    Mappings & arrays can also be declared using the *flow style* syntax.
    
    ```yaml
    fruits: [apple: no, orange: dozen]
    vegetables: [donoteat, tastesbad]
    ```
    
4. The objects at the same hierarchical level are interchangeable in order. For example, a new Secret is created using the following config file:
    
    ```yaml
    version: v1
    name: s3-pos-rw
    type: secret
    secret:
      type: key-value-properties
      acl: rw
      data:
        accesskeyid: {{access key id}}
        secretkey: {{secret key}}
        awsaccesskeyid: {{aws access key id}}
        awssecretaccesskey: {{aws secret access key}}
    ```
    
    The same secret can be created by using applying this config file:
    
    ```yaml
    version: v1
    type: secret
    name: s3-pos-rw
    secret:
      acl: rw
      type: key-value-properties
      data:
        accesskeyid: {{access key id}}
        secretkey: {{secret key}}
        awsaccesskeyid: {{aws access key id}}
        awssecretaccesskey: {{aws secret access key}} 
    ```
    
    Note that the order of objects is different in the two cases. Yet, both the config files are parsed in exactly the same manner, and will create the same Secret.
    
5. The number of spaces used for indentation at the same hierarchical level of the config file must be same. This is specifically important when creating a nested list of objects.
    
    ```yaml
    version: v1
    name:
    description: This is a sample template
    workflow:
      title:
      schedule:
          cron:
          concurrencyPolicy:
      dag: 
    			# Job 1 (There should be at least one job within a DAG)
          - name:
    			  title:
            spec:
              stack: {{stack1-version}}
              compute:
    
          # Job 2
          - name:
    			  title:
            spec:
              stack: {{stack2-version}}
              compute:
    
            dependencies:
              - 
    ```
    
    The attributes, `title`, `schedule` and `dag` are at the same hierarchical level, hence each has the same indentation of two spaces. While the nested objects within these fields, like the `cron`, list of `jobs` and `spec` have indentations of four spaces.
    
6. The pipe character is used to represent multiline string. This is useful when dealing with complex or larger data. For example,
    
    ```yaml
    flare:
      job:
        inputs:
          - name:
        steps:
          - sequence:
              - name:
              doc: 
              sql: |
                SELECT *
                FROM my_table
                WHERE condition = 'some_value';
        outputs: 
    ```