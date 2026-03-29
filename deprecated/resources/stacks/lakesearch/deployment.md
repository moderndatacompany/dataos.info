# Steps to deploy Lakesearch Stack

Follow the below steps to deploy the Lakesearch Stack within DataOS.

1. Create a manifest file for Lakesearch Stack, paste the below code, and replace `${{dataos-fdqn}}` with an actual dataos-fdqn such as `unique-haddock.dataos.app`.

    <details>
      <summary>lakesearch_stack.yaml</summary>
        ```yaml
        name: "lakesearch-v1"
        version: v1alpha
        type: stack
        layer: user
        description: "dataos lakesearch stack v1alpha Latest Public Image 0.3.4"
        stack:
        name: lakesearch
        version: "1.0"
        reconciler: stackManager
        secretProjection:
            type: "propFile"
        image:
            registry: docker.io
            repository: rubiklabs
            image: lakesearch
            tag: 0.3.4
            auth:
            imagePullSecret: dataos-container-registry
        environmentVars:
            GIN_MODE: release
            HEIMDALL_URL: "https://${{dataos-fdqn}}/heimdall/"
            DEPOT_SERVICE_URL: "https://${{dataos-fdqn}}/ds"
            LAKESEARCH_CONFIG_PATH: /etc/dataos/config/lakesearch.yaml
            SEARCHD_URL: http://localhost:9308
            SEARCHD_TEMPLATE_PATH: /etc/searchd/searchd.conf.tmpl
            ENABLE_SET_ULIMITS: true
            PROJECT_ROOT_PATH: /go/src/bitbucket.org/rubik_/lakesearch
            LAKESEARCH_GRPC_SERVER_PORT: 4090
            PUSHGATEWAY_URL: http://thanos-query-frontend.sentinel.svc.cluster.local:9090
        stackSpecValueSchema:
            jsonSchema: |
            {
                "$schema": "http://json-schema.org/draft-07/schema#",
                "type": "object",
                "properties": {
                "lakesearch": {
                    "type": "object",
                    "properties": {
                    "index_tables": {
                        "items": {
                        "properties": {
                            "name": {
                            "type": "string"
                            },
                            "description": {
                            "type": "string"
                            },
                            "tags": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            }
                            },
                            "properties": {
                            "type": "object"
                            },
                            "columns": {
                            "items":{
                                "properties": {
                                "name": {
                                    "type": "string"
                                },
                                "description": {
                                    "type": "string"
                                },
                                "tags": {
                                    "type": "array",
                                    "items": {
                                    "type": "string"
                                    }
                                },
                                "type": {
                                    "type": "string"
                                },
                                "knn": {
                                    "type": "object",
                                    "properties": {
                                    "knn_type": {
                                        "type": "string"
                                    },
                                    "knn_dims": {
                                        "type": ["integer", "number"]
                                    },
                                    "hnsw_similarity": {
                                        "type": "string"
                                    },
                                    "hnsw_m": {
                                        "type": ["integer", "number"]
                                    },
                                    "hnsw_ef_construction": {
                                        "type":["integer", "number"]
                                    }
                                    },
                                    "required": ["knn_dims", "hnsw_similarity"]
                                }
                                },
                                "required": ["name", "type"]
                            },
                            "type": "array"
                            }
                        },
                        "required": ["name", "columns"]
                        },
                        "type": "array"
                    },
                    "source": {
                        "type": "object",
                        "properties": {
                        "datasets": {
                            "type": "array",
                            "items": {
                            "properties": {
                                "name": {
                                "type": "string"
                                },
                                "dataset": {
                                "type": "string"
                                },
                                "options": {
                                "type": "object",
                                "properties": {
                                    "region": {
                                    "type": "string"
                                    },
                                    "endpoint": {
                                    "type": "string"
                                    }
                                }
                                }
                            },
                            "required": ["name", "dataset"]
                            }
                        },
                        "postgres": {
                            "type": "string"
                        },
                        "flash": {
                            "type": "string"
                        },
                        "depot": {
                            "type": "string"
                        },
                        "options": {
                            "type": "object"
                        }
                        },
                        "oneOf": [
                        { "required": ["datasets"] },
                        { "required": ["postgres"] },
                        { "required": ["flash"] },
                        { "required": ["depot"] }
                        ]
                    },
                    "indexers": {
                        "items": {
                        "properties": {
                            "index_table": {
                            "type": "string"
                            },
                            "base_sql": {
                            "type": "string"
                            },
                            "options": {
                            "type": "object",
                            "properties": {
                                "start": {
                                "type": ["integer", "number"]
                                },
                                "step": {
                                "type": ["integer", "number"]
                                },
                                "batch_sql": {
                                "type": "string"
                                },
                                "throttle": {
                                "type": "object",
                                "properties": {
                                    "min": {
                                    "type": "integer"
                                    },
                                    "max": {
                                    "type": "integer"
                                    },
                                    "factor": {
                                    "type": "number"
                                    },
                                    "jitter": {
                                    "type": "boolean"
                                    }
                                },
                                "required": ["min", "max", "factor"]
                                }
                            },
                            "required": ["step", "batch_sql"]
                            },
                            "disable": {
                            "type": "boolean"
                            }
                        },
                        "required": ["index_table", "base_sql", "options"]
                        },
                        "type": "array"
                    }
                    }
                }
                }
            }

        serviceConfig:
            configFileTemplate: |
            lakesearch.yaml: |
            {{ toYaml .ApplicationSpec.StackSpec | indent 2 }}
            containerResourceTemplate: |
            container:
                name: "{{.Name}}{{.Stamp}}-indexer"
                image: "{{.Image}}"
                imagePullPolicy: IfNotPresent
                command:
                - "/usr/bin/lakesearch"
                ports:
                - containerPort: 4080
                volumeMounts:
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
                envFrom:
                - secretRef:
                    name: "{{.Name}}-{{.Type}}{{.Stamp}}-env"
                {{ if .EnvironmentVarsFromSecret }}
                {{- range $secName := .EnvironmentVarsFromSecret }}
                - secretRef:
                name: "{{$secName}}"
                {{- end }}
                {{- end }}
            sidecars:
                - name: "{{.Name}}{{.Stamp}}-searcher"
                image: "{{.Image}}"
                imagePullPolicy: IfNotPresent
                command:
                - /usr/bin/lakesearch
                ports:
                    - containerPort: 9306
                    - containerPort: 9308
                    - containerPort: 9312
                securityContext:
                    privileged: true
                volumeMounts:
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
                envFrom:
                - secretRef:
                    name: "{{.Name}}-{{.Type}}{{.Stamp}}-env"
                {{ if .EnvironmentVarsFromSecret }}
                {{- range $secName := .EnvironmentVarsFromSecret }}
                - secretRef:
                    name: "{{$secName}}"
                {{- end }}
                {{- end }}
                env:
                    - name: MODE
                    value: searchd
        ```

    </details>
        
    
    <aside class="callout">
    
    🗣️ Make sure to include the latest version and image tag of the Stack. To obtain this information, contact your DataOS administrator.
    
    </aside>
    
3. Apply the manifest file by executing the below command:
    
    ```bash
    dataos-ctl resource apply -f ${{path-to-the-yaml-file}} --disable-interpolation
    ```
    
    <aside class="callout">
    
    🗣️ When DataOS processes a manifest file, it automatically replaces placeholders such as `${{variable}}` or `{{value}}` with values from the environment or other sources. Using the `--disable-interpolation` flag ensures that these placeholders remain unchanged in the applied resource, preventing any automatic substitution or evaluation.
    
    </aside>
    
4. Validate the deployment by executing the below command.
    
    ```bash
    dataos-ctl resource get -t stack
    ```
    
    Expected output:
    
    ```bash
    INFO[0000] 🔍 get...                                     
    INFO[0000] 🔍 get...complete                             
    
                NAME            | VERSION | TYPE  | WORKSPACE | STATUS | RUNTIME |       OWNER        
    ----------------------------|---------|-------|-----------|--------|---------|--------------------          
      lakesearch-v4             | v1alpha | stack |           | active |         | iamgroot       
    
    ```
    

After deploying the Stack successfully, next step is to run a Lakesearch Service.
