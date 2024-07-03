# Operate Command Group
You run the following `operate` sub commands by appending them to *dataos-ctl operate*.


Operate the DataOS.

```bash
Usage:
dataos-ctl operate [command]

Available Commands:
apply        Apply manifest
chart-export Exports a Helm Chart from a Chart Registry
git          Git component manifests
install      Install components
ping         Ping
upgrade      Upgrade components
view         View DataOS® Operator Services
zip          Zip install files

Flags:
  -h, --help   help for operate

Use "dataos-ctl operate [command] --help" for more information about a command.
```

**Operate Apply**

Apply manifest on the DataOS.

```bash
Usage:
dataos-ctl operate apply [flags]

Flags:
-h, --help                  help for apply
-f, --manifestFile string   Single Manifest File Location
-n, --namespace string      Namespace
```

**Operate Chart-Export**

Exports a Helm Chart from a Chart Registry.

```bash
Usage:
dataos-ctl operate chart-export [flags]

Flags:
    --accessKey string      The AWS Access Key for ECR Chart Registry
    --accessSecret string   The AWS Access Secret for ECR Chart Registry
-c, --chart string          The chart ref
-d, --exportDir string      The directory to export the Helm chart
-h, --help                  help for chart-export
    --region string         The AWS Region for ECR Chart Registry
    --registry string       The AWS ECR Chart Registry
```

**Operate Get-Secret**

Gets a secret from Heimdall.

```bash
Usage:
dataos-ctl operate get-secret [flags]

Flags:
-h, --help        help for get-secret
-i, --id string   The secret id
```

**Operate Git**

Git component manifests on the DataOS.

```bash
Usage:
dataos-ctl operate git [flags]

Flags:
-e, --email string   Operator email
-h, --help           help for git
-l, --localOnly      Perform local only
-n, --name string    Operator name
-p, --push           Push changes
-r, --resetGitDir    Reset the local git directory
```

**Operate Install**

When you create a new server, you want to install new applications on the server. Use this command to install one or more applications/components on the server.

```bash
Usage:
dataos-ctl operate install [flags]

Flags:
-h, --help                    help for install
-i, --imagesFile string       Installation Images File Location
-f, --installFile string      Installation Manifest File Location
-n, --noGitOps                Do not push changes to the GitOps repo in DataOS®
    --oldReleaseManifest      Use old install manifest format
    --renderOnly              Render only
-r, --replaceIfExists         Replace existing resources
-s, --secretsFile string      Installation Secrets File Location
    --useExternalPostgresql   Use external postgresql
-v, --valuesFile string       Installation Values File Location
```

**Operate Ping**

```bash
Usage:
dataos-ctl operate ping [flags]

Flags:
-h, --help   help for ping
```

**Operate Upgrade**

Upgrade components on the DataOS.

```bash
Usage:
dataos-ctl operate upgrade [flags]

Flags:
-h, --help                    help for upgrade
-i, --imagesFile string       Installation Images File Location
-f, --installFile string      Installation Manifest File Location
    --oldReleaseManifest      Use old install manifest format
-s, --secretsFile string      Installation Secrets File Location
    --useExternalPostgresql   Use external postgresql
-v, --valuesFile string       Installation Values File Location
```

**Operate View**

View DataOS Operator Services from the local machine without going to server. You can create a data pipe from server to local machine.

```bash
Usage:
dataos-ctl operate view [flags]

Flags:
-h, --help                            help for view
-p, --localPort int                   The starting local port to port-forward services to (default 8081)
-s, --servicesToPortForward strings   The comma separated list of services to port-forward local: 
                                        metis,cerebro,aurora-beanstalkd,git,prometheus,
                                        service-mesh,cruise-control,kibana,spark-history
```

```bash
➜  ~ dataos-ctl operate view -s metis
INFO[0000] 📚 metis view...                              
INFO[0000] 🔭 metis port-forward..                       
INFO[0003] close connections hit enter/return?
INFO[0004] 🔭 metis port-forward.. ready
INFO[0004] : metis http://localhost:8081
```

> 📌 **Note**: Config File ".dataos.ck.config" should be present in the folder  "[/Users/[username]/.dataos/context].
> 