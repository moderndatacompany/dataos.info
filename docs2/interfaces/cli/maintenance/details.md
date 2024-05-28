# Maintenance Command Group
You run the following `maintenance` sub commands by appending them to *dataos-ctl maintenance*.

## `collect-garbage`
Collect Garbage on the DataOS®

```shell

Usage:
  dataos-ctl maintenance collect-garbage [flags]

Flags:
  -d, --duration string     the duration to calculate the age of resources that are eligible for garbage collection (default "168h")
  -h, --help                help for collect-garbage
  -k, --kubeconfig string   kubeconfig file location
  -l, --layer string        the layer to target in the DataOS, user|system (default "user")
```

## `create-docker-secret`
Creates a Docker Secret for K8S

```shell

Usage:
  dataos-ctl maintenance create-docker-secret [flags]

Flags:
      --heimdallSecretId string         heimdall secret id to get the docker registry username and password from
  -h, --help                            help for create-docker-secret
  -k, --kubeconfig string               kubeconfig file location
  -n, --namespace string                namespace where to store the docker secret
  -p, --password string                 password of the docker registry
  -g, --region string                   region of the docker registry
  -r, --registry string                 docker registry
  -s, --secretName string               name of the secret to store the docker secret
      --targetHeimdallSecretId string   heimdall secret id to store the resulting docker secret
  -t, --type string                     type of docker registry (docker|ecr)
  -u, --username string                 username of the docker registry
```

