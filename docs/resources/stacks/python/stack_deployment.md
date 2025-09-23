# Deploy Python Stack

This guide walks you through the process of setting up and deploying the Python Stack in your DataOS environment. The Python Stack must be defined and registered by a DataOS operator before developers can use it to deploy applications. 

## Prerequisites

The user must have a DataOS Operator tag, as only operators are authorized to deploy Stacks. To verify this, execute the command below.

```bash
dataos-ctl user get
# expected output:
dataos-ctl user get                
INFO[0000] 😃 user get...                                
INFO[0000] 😃 user get...complete                        

      NAME     │     ID      │  TYPE  │        EMAIL         │              TAGS               
───────────────┼─────────────┼────────┼──────────────────────┼─────────────────────────────────
      Groot    │  iamgroot   │ person │   iamgroot@tmdc.io   │ roles:id:data-dev,              
               │             │        │                      │ roles:id:operator,              
               │             │        │                      │ roles:id:system-dev,            
               │             │        │                      │ roles:id:user,                  
               │             │        │                      │ users:id:iamgroot   
```

## Steps to deploy Python as a Stack

### **1. Create a Stack manifest file**

Create a Python Stack manifest file using the template given below.

<details>
    <summary>python_stack.yaml</summary>

```yaml
name: python-3-12
version: v1alpha
type: stack
tags:
    - dataos:type:resource
    - dataos:resource:stack
    - dataos:layer:user
description: dataos python stack v1alpha version 1
layer: user
stack:
    name: python3
    version: '1.0'
    reconciler: stackManager
    image:
    registry: docker.io
    repository: library
    image: python
    tag: 3.12-slim-bullseye
    stackSpecValueSchema:
    jsonSchema: >
        { "$schema": "http://json-schema.org/draft-07/schema#", "type": "object",
        "properties": { "repo": { "type": "object", "properties": { "url": {
        "type": "string" }, "syncFlags": { "type": "array", "items": { "type":
        "string" } }, "baseDir": { "type": "string" } }, "required": [ "url",
        "baseDir" ] } }, "required": [ "repo" ] }
    serviceConfig:
    containerResourceTemplate: |
        {{- $repo := .ApplicationSpec.StackSpec.repo }}
        initContainers:
        - command:
            - /git-sync
            args:
            - --repo={{ getNested $repo "url" }}
            - --one-time=true
            - --root=/etc/dataos/work
            {{- if hasKey $repo "syncFlags" }}
            {{- range $flag := getNested $repo "syncFlags" }}
            - {{ $flag }}
            {{- end }}
            {{- end }}
            image: docker.io/tmdcio/git-sync:latest
            imagePullPolicy: IfNotPresent
            name:  "{{.Name}}{{.Stamp}}-ic"
            {{ if .ApplicationSpec.Resources -}}
            resources:
        {{toYaml .ApplicationSpec.Resources | indent 4}}
            {{- end }}
            volumeMounts:
            - mountPath: /etc/dataos/work
            name: workdir
            envFrom:
            - secretRef:
                name: "{{.Name}}-{{.Type}}{{.Stamp}}-env"
            {{ if .EnvironmentVarsFromSecret }}
            {{- range $secName := .EnvironmentVarsFromSecret }}
            - secretRef:
                name: "{{$secName}}"
            {{- end }}
            {{- end }}
        container:
        name: {{.Name}}{{.Stamp}}-main
        image: "{{.Image}}"
        imagePullPolicy: IfNotPresent
        command:
        - sh
        - -c
        - |
            # cd into the work root
            cd /etc/dataos/work &&
            pwd &&
            # move into your repo’s baseDir
            cd {{ getNested $repo "baseDir" }} &&
            # install dependencies from requirements.txt
            pip install --no-cache-dir -r requirements.txt &&
            # finally, hand off to the real entrypoint
            exec "$@"
        - --
        args:
        - python3
        - main.py
        envFrom:
        - secretRef:
            name: "{{.Name}}-{{.Type}}{{.Stamp}}-env"
        {{ if .EnvironmentVarsFromSecret }}
        {{- range $secName := .EnvironmentVarsFromSecret }}
        - secretRef:
            name: "{{$secName}}"
        {{- end }}
        {{- end }}
        volumeMounts:
        {{ if .HasSecretRefs }}
        - name: dataos-secret-mount
            mountPath: "{{.DataOsSecretMountPath}}"
            readOnly: true
        {{- end }}
        - name: workdir
            mountPath: /etc/dataos/work
        {{ if .HasConfigConfs }}
        - name: dataos-config-mount
            mountPath: "{{.DataOsConfigMountPath}}"
            readOnly: true
        {{- end }}
        {{ if .ApplicationSpec.TempVolume -}}
        - name: {{.Name}}-{{.Type}}{{.Stamp}}-tdm
            mountPath: "{{.DataTempMountPath}}"
            subPath: {{.Name}}{{.Stamp}}
        {{- end }}
        {{ if .ApplicationSpec.PersistentVolume -}}
        - name: {{.Name}}-{{.Type}}{{.Stamp}}-pdm
            mountPath: "{{.DataPersistentMountPath}}/{{.ApplicationSpec.PersistentVolume.Directory}}"
            subPath: "{{.ApplicationSpec.PersistentVolume.Directory}}"
        {{- end }}
        {{ if .Volumes }}
        {{- range $volume := .Volumes }}
        - name: {{$volume.Name}}
            mountPath: "{{$volume.MountPath}}"
            readOnly: {{$volume.ReadOnly}}
            {{ if $volume.SubPath }}
            subPath: "{{$volume.SubPath}}"
            {{- end }}
        {{- end }}
        {{- end }}
        {{ if .ApplicationSpec.Resources -}}
        resources:
        {{toYaml .ApplicationSpec.Resources | indent 4}}
        {{- end }}
        env:
            - name: POD_NAME
            valueFrom:
                fieldRef:
                fieldPath: metadata.name
        {{ if .ApplicationSpec.EnvironmentVars }}
            {{- range $conf, $value := .ApplicationSpec.EnvironmentVars }}
            - name: {{$conf}}
            value: {{ $value | quote }}
            {{- end }}
        {{- end}}
    dataOsAddressJqFilters:
    - .depots
    secretProjection:
    type: envVars
```
</details>

### **2. Apply the Stack manifest file**

Apply the Python Stack by executing the command below.

```bash
dataos-ctl resource apply -f ${{file-path}} --disable-interpolation
```

<aside class="callout">
🗣 If the manifest file is applied without the `--disable-interpolation` flag, DataOS will try to substitute any placeholders (for example, values wrapped in `${{ }}`) with environment variables at runtime, which can cause unintended replacements or deployment errors; using the flag ensures the manifest is applied exactly as written, preserving template variables and preventing misconfigurations.
</aside>

### **3. Verify the deployment**

Verify if the Python Stack is successfully deployed and ready to use by executing the command below.

```bash
dataos-ctl get -t stack -a
#expected output:
            NAME            | VERSION | TYPE  | WORKSPACE | STATUS | RUNTIME |       OWNER        
----------------------------|---------|-------|-----------|--------|---------|--------------------
  beacon-graphql-v1         | v1alpha | stack |           | active |         | dataos-manager     
  bento-v4                  | v1alpha | stack |           | active |         | dataos-manager     
  flare-v7                  | v1alpha | stack |           | active |         | dataos-manager     
  lakesearch-v2             | v1alpha | stack |           | active |         | iamloki         
  python-3-12               | v1alpha | stack |           | active |         | iamgroot           
```

With the Python Stack successfully deployed in your DataOS environment, you are now ready to build and run Python-based applications. Developers can deploy any Python application by configuring a Python Service that runs on top of the registered Python Stack. To know more about this, please [refer to this link](/resources/stacks/python/#getting-started-with-python-stack).