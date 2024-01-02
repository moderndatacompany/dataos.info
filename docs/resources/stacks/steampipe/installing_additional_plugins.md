# Installing additional plugins with the Steampipe Stack

## Prerequisites

### **Docker Installed**

Ensure that Docker is installed and operational on the host system. Refer to the official [Docker](https://www.docker.com/) documentation for comprehensive instructions.

## Steps

### **Create a Dockerfile**

A Dockerfile is a script that contains a set of instructions to build a Docker image. Within your project directory create a file named Dockerfile and copy the below code in it. Within the Dockerfile specify additional plugins in the format given below. The details of supported plugins can be found on the [Steampipe Hub](https://hub.steampipe.io/plugins).

```docker
RUN steampipe plugin install {{plugin name}} --skip-config
```

#### **Dockerfile**

```docker
# Building a Go program
FROM golang:1.16 as builder
WORKDIR /app
COPY start.go .
RUN go mod init start
RUN CGO_ENABLED=0 GOOS=linux go build -o start

FROM ghcr.io/turbot/steampipe

USER root:0
RUN apt-get update -y \
 && apt-get install -y git
USER steampipe:0

# Installing defualt plugins
RUN steampipe plugin install csv --skip-config
RUN steampipe plugin install aws --skip-config
RUN steampipe plugin install config --skip-config
RUN steampipe plugin install googlesheets --skip-config
RUN steampipe plugin install salesforce --skip-config
RUN steampipe plugin install francois2metz/airtable --skip-config
RUN steampipe plugin install finance --skip-config
RUN steampipe plugin install exec --skip-config

# Clone the mod repository and set the working directory
RUN git clone --depth 1 https://github.com/turbot/steampipe-mod-aws-insights.git

# Copy the custom PostgreSQL configuration file into the container
COPY pgbouncer.ini /etc/pgbouncer/pgbouncer.ini

COPY --from=builder /app/start /start

ENTRYPOINT ["/start"]
```

Within the same directory create two additional files by the name [`pgbouncer.ini`](#pgbouncerini), and [`start.go`](#startgo) and copy the code provided below.

#### **pgbouncer.ini**

```bash
# pgbouncer.ini
IGNORE_STARTUP_PARAMETERS = search_path
```

#### **start.go**

```go
package main

import (
    "fmt"
    "io"
    "io/ioutil"
    "os"
    "path/filepath"
    "os/exec"
    "strings"
)

func main() {
    // Task 1: Run commands from plugins_install.yaml
    pluginsFile := "/etc/dataos/config/plugins_install.yaml"
    err := executePluginCommands(pluginsFile)
    if err != nil {
        fmt.Printf("Error executing plugin commands: %v\n", err)
        os.Exit(1)
    }

    // Task 2: Copy .spc files
    srcDir := "/etc/dataos/config"
    destDir := "/home/steampipe/.steampipe/config"
    err = copySpcFiles(srcDir, destDir)
    if err != nil {
        fmt.Printf("Error copying .spc files: %v\n", err)
        os.Exit(1)
    }

    // Start the steampipe service
    cmd := exec.Command("steampipe", "service", "start", "--foreground")
    cmd.Stdout = os.Stdout
    cmd.Stderr = os.Stderr
    if err := cmd.Run(); err != nil {
        panic(err)
    }
}

// Copy .spc files from srcDir to destDir
func copySpcFiles(srcDir, destDir string) error {
    filePattern := "*.spc"
    files, err := filepath.Glob(filepath.Join(srcDir, filePattern))
    if err != nil {
        return err
    }

    for _, file := range files {
        destFile := filepath.Join(destDir, filepath.Base(file))
        src, err := os.Open(file)
        if err != nil {
            return err
        }
        defer src.Close()

        dst, err := os.Create(destFile)
        if err != nil {
            return err
        }
        defer dst.Close()

        if _, err := io.Copy(dst, src); err != nil {
            return err
        }

        fmt.Printf("Copied %s to %s\n", file, destFile)
    }

    return nil
}

// Execute plugin commands from pluginsFile
func executePluginCommands(pluginsFile string) error {

    data, err := ioutil.ReadFile(pluginsFile)
    if err != nil {
        return err
    }

    commandLines := string(data)
    commands := parseCommands(commandLines)

    for _, cmd := range commands {
        fmt.Printf("Executing: %s\n", cmd)
        if err := runCommand(cmd); err != nil {
            return err
        }
    }

    return nil
}

// Parse commands from the YAML content
func parseCommands(data string) []string {
    commands := []string{}
    lines := strings.Split(data, "\n")
    for _, line := range lines {
        line = strings.TrimSpace(line)
        if strings.HasPrefix(line, "-") {
            commands = append(commands, line[1:])
        }
    }
    return commands
}

// Run a command
func runCommand(command string) error {
    cmdParts := strings.Fields(command)
    if len(cmdParts) == 0 {
        return nil
    }
    cmd := exec.Command(cmdParts[0], cmdParts[1:]...)
    cmd.Stdout = os.Stdout
    cmd.Stderr = os.Stderr
    return cmd.Run()
}
```

### **Build the Docker Image**

Open a terminal, navigate to the directory containing your Dockerfile, and execute the following command:

```shell
docker build -t {{image name}}:{{tag}} .
```

Substitute `{{image name}}` with your chosen image name and `{{tag}}` with the desired version or label.

### **Create a Stack**

After building the image, push into the container registry, and create a new Steampipe Stack or update an existing one using the provided YAML.

```yaml
name: "steampipe-v1"
version: v1alpha
type: stack
layer: user
description: "Steampipe service stack v1"
stack:
  name: steampipe
  version: "1.0"
  reconciler: "stackManager"
  # dataOsAddressJqFilters:
  #   - .inputs[].dataset
  secretProjection:
    type: "envVars"
  image:
    registry: docker.io
    repository: rubiklabs
    image: dataos-steampipe
    tag: 0.0.1-dev
    auth:
      imagePullSecret: dataos-container-registry
  command:
    - /entrypoint.sh
  arguments:
    - steampipe
    - service
    - start
    - --foreground
  stackSpecValueSchema:
    jsonSchema: |
      { "$schema": "http://json-schema.org/draft-01/schema#", "type": "object", "properties": {}}
  serviceConfig:
    configFileTemplate:
			
```

Utilize this new Stack to create a Steampipe Service.