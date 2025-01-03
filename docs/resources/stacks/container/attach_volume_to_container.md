# Attaching Volume to the Container Stack

## Create the Volume manifest

To attach a Volume with a Container create a Volume first.

```yaml
name: persistent-v # Name of the Resource
version: v1beta # Manifest version of the Resource
type: volume # Type of Resource
tags: # Tags for categorizing the Resource
  - dataos:volume # Tags
  - volume # Additional tags
description: Common attributes applicable to all DataOS Resources
layer: user
volume:
  size: 5Gi  #100Gi, 50Mi, 10Ti, 500Mi
  accessMode: ReadWriteOnce  #ReadWriteOnce, ReadOnlyMany.
  type: persistent
```

## Create the Container Stack

Refer the created Volume Resource in the `persistentVolume` attribute of the Container manifest file. The `persistentVolume` section specifies the volume's name (persistent-v) and the directory (mymount) where it will be mounted inside the container. This allows the container to use the volume for persistent storage

```yaml
version: v1
name: volume-mount
type: service
service:
  compute: runnable-default
  replicas: 1
  logLevel: INFO
  servicePort: 5433
  resources:
    requests:
      cpu: 1000m
      memory: 1024Mi
    limits:
      cpu: 1100m
      memory: 4096Mi
  stack: container
  envs:
    DEPOT_SERVICE_URL: "https://emerging-hawk.dataos.app/ds/api/v2"
    HEIMDALL_SERVICE_URL: "https://emerging-hawk.dataos.app/heimdall/api/v1"
    RUN_AS_USER_APIKEY: "--"
  persistentVolume:
    name: persistent-v
    directory: mymount
  stackSpec:
    image: iamgroot/pgduck:0.0.10
    command:
      - tail
      - -f
      - /etc/issue
```