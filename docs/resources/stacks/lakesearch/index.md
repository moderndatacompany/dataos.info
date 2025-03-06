---
title: Lakesearch
search:
  boost: 2/4
---

# Lakesearch

Lakesearch is a [Stack](/resources/stacks/) within DataOS that provides the scalable full-text search solution for the DataOS Lakehouse. It allows app developers to enable full-text search on top of [DataOS Lakehouse](/resources/lakehouse/) tables with an ability to scale the indexing and searching capabilities to meet business requirements. For a better understanding of Lakesearch architecture please refer to [this link.](/resources/stacks/lakesearch/architecture) 

<div style="text-align: center;">
  <img src="/resources/stacks/lakesearch/images/arch.jpg" alt="Lakesearch" style="border:1px solid black; width: 70%; height: auto;">
</div>


The examples below illustrate the search functionality of Lakesearch where a user can access the API endpoint.

<details>
    <summary>Search by keywords</summary>

    Endpoint: `https://unique-haddock.dataos.app/lakesearch/public:testingls/api/v2/index/:index_name/keywords?word=alabama&limit=3`

        ```json
        # Result
        {
        "keywords": [
            {
            "docs": "767",
            "hits": "767",
            "keyword": "alabama"
            }
        ]
        }
        ```
</details>
    
<details>
    <summary>Search by table name (index name)</summary>
    
    Endpoint: `https://unique-haddock.dataos.app/lakesearch/public:testingls/api/v2/index/city/search`


        ```json
        # Result        
        {
            "took": 0,
            "timed_out": false,
            "hits": {
                "total": 1,
                "total_relation": "gte",
                "hits": [
                    {
                        "_id": 36003,
                        "_score": 1,
                        "_source": {
                            "state_name": "Alabama",
                            "version": "202501090702",
                            "@timestamp": 1739964871,
                            "city_id": "CITY6",
                            "zip_code": 36003,
                            "city_name": "Autaugaville",
                            "county_name": "Autauga County",
                            "state_code": "AL",
                            "ts_city": 1736406148
                        }
                    }
                ]
            }
        }
        ```
        
</details>

<details>
    <summary>Search by similar word</summary>

    Endpoint: `https://unique-haddock.dataos.app/lakesearch/public:testingls/api/v2/index/:index_name/suggestions?word=auta`

        ```json
        # Result
        {
            "suggestions": [
                {
                    "distance": 2,
                    "docs": 339,
                    "suggestion": "utah"
                },
                {
                    "distance": 3,
                    "docs": 1806,
                    "suggestion": "south"
                },
                {
                    "distance": 3,
                    "docs": 1566,
                    "suggestion": "dakota"
                }
            ]
        }
        ```
    
</details>
    

## Structure of Lakesearch Service manifest file

<div style="text-align: center;">
  <figure>
    <img src="/resources/stacks/lakesearch/images/ls.jpg" alt="Lakesearch Service structure" style="border:1px solid black; width: 100%; height: auto;">
    <figcaption style="margin-top: 8px; font-style: italic;">Lakesearch Service Structure</figcaption>
  </figure>
</div>


## How to deploy Lakesearch Stack within DataOS?

The Stack is deployed by a DataOS operator. Before starting the deployment of Lakesearch Stack within DataOS, check if it already exists by executing the below command, which will list all the deployed Stacks within the DataOS environment along with their flavor, version, and image:

```bash
dataos-ctl develop stack versions 
```

<details>
    <summary>Expected output</summary>

    ```bash
        STACK      │ FLAVOR  │ VERSION │                       IMAGE                       │     IMAGE PULL SECRET      
    ──────────────────┼─────────┼─────────┼───────────────────────────────────────────────────┼────────────────────────────
    beacon          │ graphql │ 1.0     │ docker.io/rubiklabs/beacon:postgraphile-4.10.0.d1 │ dataos-container-registry  
    beacon          │ rest    │ 1.0     │ docker.io/postgrest/postgrest:v12.2.3             │ dataos-container-registry  
    benthos         │         │ 3.0     │ docker.io/rubiklabs/benthos4:0.0.49               │ dataos-container-registry  
    benthos         │         │ 4.0     │ docker.io/rubiklabs/benthos4:0.0.49               │ dataos-container-registry  
    bundlebenthos   │         │ 4.0     │ docker.io/rubiklabs/benthos-ds:0.8.28             │ dataos-container-registry  
    container       │         │ 1.0     │                                                   │                            
    dataos-ctl      │         │ 1.0     │ docker.io/rubiklabs/dataos-ctl:2.26.39            │ dataos-container-registry  
    dataos-resource │ apply   │ 1.0     │ docker.io/rubiklabs/dataos-ctl:2.26.39            │ dataos-container-registry  
    dataos-resource │ delete  │ 1.0     │ docker.io/rubiklabs/dataos-ctl:2.26.39            │ dataos-container-registry  
    dataos-resource │ run     │ 1.0     │ docker.io/rubiklabs/dataos-ctl:2.26.39            │ dataos-container-registry  
    dlthub          │ python  │ 1.0     │ docker.io/rubiklabs/dataos-dlthub:0.0.8-dev       │ dataos-container-registry  
    dlthub          │ python  │ 1.0     │ docker.io/rubiklabs/dataos-dlthub:0.0.8-dev       │ dataos-container-registry  
    flare           │         │ 5.0     │ docker.io/rubiklabs/flare5:7.3.18                 │ dataos-container-registry  
    flare           │         │ 6.0     │ docker.io/rubiklabs/flare6:8.0.26                 │ dataos-container-registry  
    flash           │ python  │ 4.0     │ docker.io/rubiklabs/flash:0.0.37-dev              │ dataos-container-registry  
    flash           │ python  │ 1.0     │ docker.io/rubiklabs/flash:0.0.44-dev              │ dataos-container-registry  
    lakesearch      │         │ 2.0     │ docker.io/rubiklabs/lakesearch:0.3.3-exp.01       │ dataos-container-registry  
    lakesearch      │         │ 3.0     │ docker.io/rubiklabs/lakesearch:0.2.6-exp.05       │ dataos-container-registry  
    lakesearch      │         │ 4.0     │ docker.io/rubiklabs/lakesearch:0.3.3-exp.02       │ dataos-container-registry  
    lakesearch      │         │ 5.0     │ docker.io/rubiklabs/lakesearch:0.3.3              │ dataos-container-registry  
    lakesearch      │         │ 6.0     │ docker.io/rubiklabs/lakesearch:0.3.4              │ dataos-container-registry  
    nilus-cdc       │         │ 1.0     │ docker.io/rubiklabs/nilus-cdc:0.0.0-exp.01        │ dataos-container-registry  
    scanner         │         │ 2.0     │ docker.io/rubiklabs/scanner:4.8.26                │ dataos-container-registry  
    scanner         │         │ 1.0     │ docker.io/rubiklabs/dataos-scanner:0.1.28         │ dataos-container-registry  
    soda            │ python  │ 1.0     │ docker.io/rubiklabs/dataos-soda:0.0.30            │ dataos-container-registry  
    soda            │ python  │ 2.0     │ docker.io/rubiklabs/dataos-soda:0.0.27-dev        │ dataos-container-registry  
    stream-monitor  │         │ 1.0     │ docker.io/rubiklabs/monitor-api:0.17.2            │ dataos-container-registry  
    ststack         │ python  │ 1.0     │ docker.io/library/python:3.10.12-slim             │                            
    talos           │         │ 1.0     │ docker.io/rubiklabs/talos:0.1.26                  │ dataos-container-registry  
    talos           │         │ 2.0     │ docker.io/rubiklabs/talos:0.1.25                  │ dataos-container-registry  
    toolbox         │         │ 1.0     │ docker.io/rubiklabs/dataos-tool:0.3.9             │ dataos-container-registry  
    ```

</details>

If you do not find the Lakesearch in the result, it is time to deploy the Stack. Remember that only the user with an ‘operator’ tag can execute the above command. 

### **Pre-requisites**

### **Steps**

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

## How to set up a Lakesearch Service?

Once the Lakesearch Stack is available, follow the steps given in the links below to create a Lakesearch Service . The Lakesearch Service retrieves data from the source and indexes each column from one or multiple tables, making it searchable.

### **Pre-requisites**

A user must have the following requirements met before setting up a Lakesearch Service.

- A user is required to have knowledge of Python.

- Ensure that DataOS CLI is installed and initialized in the system. If not the user can install it by referring to [this section.](https://dataos.info/interfaces/cli/installation/)
- A user must have the following tags assigned.
    
    ```bash
    dataos-ctl user get                
    INFO[0000] 😃 user get...                                
    INFO[0001] 😃 user get...complete                        
    
          NAME     │     ID      │  TYPE  │        EMAIL         │              TAGS               
    ───────────────┼─────────────┼────────┼──────────────────────┼─────────────────────────────────
        Iamgroot   │   iamgroot  │ person │  iamgroot@tmdc.io    │ roles:id:data-dev,                            
                   │             │        │                      │ roles:id:user,                  
                   │             │        │                      │ users:id:iamgroot
    ```
    
- If the above tags are not available, a user can contact a DataOS operator to assign the user with one of the following use cases using the Bifrost Governance. A DataOS operator can create new usecases as per the requirement.

    <div style="text-align: center;">
    <figure>
    <img src="/resources/stacks/lakesearch/images/usecase.png" alt="usecases" style="border:1px solid black; width: 100%; height: auto;">
    <figcaption style="margin-top: 8px; font-style: italic;">Bifrost Governance</figcaption>
    </figure>
    </div>

    
- Ensure the Lakesearch Stack is available in the DataOS Environment.


### **Create a Lakesearch Service**

Follow the below links to create a Lakesearch Service with different functionalities:

- [Normal Lakesearch Service](/resources/stacks/lakesearch/service/)
- [Lakesearch Service with query rewriter](/resources/stacks/lakesearch/rewriter/)
- [Lakesearch Service with vector embedding](/resources/stacks/lakesearch/vector_embedding/)

For a detailed breakdown of the configuration options and attributes of a Lakesearch Service, please refer to the documentation: [Attributes of Lakesearch Service manifest](/resources/stacks/lakesearch/configurations/).

## How to perform index-based searches?

A user can start searching for the index, keywords, or similar words by accessing the Lakesearch Service API endpoint. Some basic index searching is given below, to know in detail about index searching, please refer [to this link](/resources/stacks/lakesearch/index_searching/).

### **Searching for an index**

A user can access the endpoint either by curl command or using any API platform.

- To get the list of all the indices, a user can execute the following curl command in the terminal.
    
    ```bash
    curl -X GET "https://unique-haddock.dataos.app/lakesearch/public:testingls/api/v2/index" \                           
    -H "Authorization: Bearer dG9rZW5fZGlzdhlkg3RseV9tYWlubHlfdXBlkmF5LjU1ZmE1ZWQyLWUwNDgtNGI3Yi1hNGQ2LWNlNjA1YTAzZTE4YQ=="
    ```
    
    Expected output:
    
    ```json
    [
        "__indexer_state",
        "city"
    ]
    ```
    
- To get the details of an individual index by name execute the below curl command.
    
    ```bash
    curl -X GET "https://unique-haddock.dataos.app/lakesearch/public:testingls/api/v2/index/city/search" \
    -H "Authorization: Bearer dG9rZW5fZGlzdGluY3Rhklf9tYWlubHlfdXBfklF5LjU1ZmE1ZWQyLWUwNDgtNGI3Yi1hNGQ2LWNlNjA1YTAzZTE4YQ=="
    ```
    
    Expected output:
    
    ```bash
    {
        "took": 0,
        "timed_out": false,
        "hits": {
            "total": 1,
            "total_relation": "gte",
            "hits": [
                {
                    "_id": 36003,
                    "_score": 1,
                    "_source": {
                        "state_name": "Alabama",
                        "version": "202501090702",
                        "@timestamp": 1739964871,
                        "city_id": "CITY6",
                        "zip_code": 36003,
                        "city_name": "Autaugaville",
                        "county_name": "Autauga County",
                        "state_code": "AL",
                        "ts_city": 1736406148
                    }
                }
            ]
        }
    }
    ```
    

### **Searching for a keyword**

To search by the exact keyword execute the following curl command.

```bash
curl -X GET "https://unique-haddock.dataos.app/lakesearch/public:testingls/api/v2/index/city/keywords?word=alabama" \ 
-H "Authorization: Bearer dG9rZW5fZGlzdGluY3RseV9tYWlubHlfdXBfcmFU1Zlo1ZWQyLWUwNDgtNGI3Yi1hNGQ2LWNlNjA1YTAzZTE4YQ=="
```

Expected output:

```bash
{
    "keywords": [
        {
            "docs": "767",
            "hits": "767",
            "keyword": "alabama"
        }
    ]
}
```

### **Searching for a similar word**

To search by the similar word execute the following curl command.

```bash
curl -X GET "https://unique-haddock.dataos.app/lakesearch/public:testingls/api/v2/index/city/suggestions?word=alaba&limit=2" \
-H "Authorization: Bearer dG9rZW5fZGlzluY3RseV9tYWlubHlfcmF5LjU1ZmE1ZWQyLWplNDgtNGI3Yi1hNGQ2LWNlNjA1YTAzZTE4YQ=="

```

Expected output:

```json
{
    "suggestions": [
        {
            "distance": 2,
            "docs": 767,
            "suggestion": "alabama"
        },
        {
            "distance": 4,
            "docs": 90,
            "suggestion": "island"
        }
    ]
}
```


## Managing deleted records in Lakesearch

When records that have already been indexed in Lakesearch are deleted from the source table, they remain accessible through the search API unless explicitly handled. To manage this, Lakesearch supports **soft deletes**, ensuring that deleted records are appropriately excluded from search results.

### **Soft delete mechanism**

Lakesearch relies on two additional columns in the Lakehouse table:

1. **`_delete` (Boolean)** – Tracks whether a record should be considered deleted. By default, all records have `_delete = false`.
2. **Timestamp column** (e.g., `updated_at` or `last_modified_date`) – Records the last modification time.

When a record needs to be removed from search results:

- It is marked as **`_delete = true`**.
- The `updated_at` timestamp is refreshed to reflect the change.

This ensures that Lakesearch recognizes the update and removes the record from indexed search results.

### **Handling hard deletes**

If a record is permanently deleted from the source table, a mechanism must be in place to update `_delete = true` in the corresponding Lakehouse table record. If this update is **not** performed, Lakesearch remains unaware of the deletion, and the record will still be retrievable via the search API.

By implementing this process, Lakesearch ensures data consistency while allowing controlled deletion without losing historical traceability.

## Best practices

This section involves recommends dos and don’ts while configuring a Lakesearch Service.

- For large datasets, always use the partition indexer when configuring the LakeSearch Service. It divides the indexes into two parts, significantly reducing the time required to index all tables.
    

## FAQs

This section will contain answers to common questions about LakeSearch. Currently, no FAQs are available, but we will update this section as relevant questions arise.