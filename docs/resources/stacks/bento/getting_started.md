# Bento: First Steps

Bento is a resilient stream processing stack designed to simplify data flow management.

For new users, setting up Bento in a local environment is recommended as part of best practices. This approach allows for comprehensive testing of data pipelines before deploying them to a production environment.

Once the local setup is complete, guidance is available for transitioning to DataOS and expanding pipeline capabilities. Refer to the step-by-step guide for detailed instructions on each stage of the process.

## Install

Firstly, let's get started by installing the Bento stack. The installation process is a breeze, that involves a single command to be executed on the command line:  

```bash
curl -Lsf https://warpstreamlabs.github.io/bento/sh/install | bash # Downloads the latest stable version
```

### **Use Docker**

Ensure that the Docker is installed in the system. If Docker is not installed, refer to the ["Install Docker Engine"](https://docs.docker.com/engine/install/) guide for installation instructions.
Once Docker is successfully installed, the environment is ready for data processing.

Now pull the latest official Bento image using Docker, run the following command:

```bash
docker pull ghcr.io/warpstreamlabs/bento
```

## Building a stream pipeline

After installing Bento, users can begin experimenting with its available components. A Bento stream pipeline is configured using a single YAML configuration file.

The following example demonstrates how to create a simple pipeline that reads data from a file and writes it to the console:

```yaml
input:
    http_client:
      url: https://api.chucknorris.io/jokes/random
      verb: GET
      headers:
        Content-Type: application/JSON
output:
  stdout:
    codec: lines
```

This YAML configuration instructs Bento to read data from the specified file and write it to the console as a stream of lines. The `codec: lines` setting ensures that each line of data is separated by a new line character.

After preparing the pipeline configuration, save it.(example: `pipeline.yaml`). To start Bento, run the following command:

```bash
bento -c ${path-of-the-config-file}
```

**Example input and Expected Output**

```bash
bento -c /home/Desktop/pipeline.yaml # Path of the file

# Expected Output
INFO Running main config from specified file       @service=bento bento_version=1.5.2 path=/home/Desktop/pipeline.yaml
INFO Listening for HTTP requests at: http://0.0.0.0:4195  @service=bento
INFO Launching a Bento instance, use CTRL+C to close  @service=bento
INFO Output type stdout is now active              @service=bento label="" path=root.output
INFO Input type http_client is now active          @service=bento label="" path=root.input
{"categories":[],"created_at":"2020-01-05 13:42:20.262289","icon_url":"https://api.chucknorris.io/img/avatar/chuck-norris.png","id":"nNSiXMgCSqKuioZGWqhW3g","updated_at":"2020-01-05 13:42:20.262289","url":"https://api.chucknorris.io/jokes/nNSiXMgCSqKuioZGWqhW3g","value":"What happened to the crew of the Mary Celeste? Chuck Norris."}
{"categories":[],"created_at":"2020-01-05 13:42:29.296379","icon_url":"https://api.chucknorris.io/img/avatar/chuck-norris.png","id":"J6EKCG24SxyUfG9XBC4GcQ","updated_at":"2020-01-05 13:42:29.296379","url":"https://api.chucknorris.io/jokes/J6EKCG24SxyUfG9XBC4GcQ","value":"Chuck Norris never 'visits' a foreign land... he invades it"}
{"categories":[],"created_at":"2020-01-05 13:42:25.352697","icon_url":"https://api.chucknorris.io/img/avatar/chuck-norris.png","id":"EhRxaBmuRZe5luWPpRN9uA","updated_at":"2020-01-05 13:42:25.352697","url":"https://api.chucknorris.io/jokes/EhRxaBmuRZe5luWPpRN9uA","value":"Gloria Gaynor: I Will Survive Chuck Norris's Version: They Won't Survive"}
{"categories":[],"created_at":"2020-01-05 13:42:25.628594","icon_url":"https://api.chucknorris.io/img/avatar/chuck-norris.png","id":"oKXJfzLRT0KNV47A9VbCvQ","updated_at":"2020-01-05 13:42:25.628594","url":"https://api.chucknorris.io/jokes/oKXJfzLRT0KNV47A9VbCvQ","value":"At exactly April 8 of 2008, at 11:45 and 20 seconds, Chuck Norris stomped his foot. At exactly April 8 of 2001, at 11:45 and 21 seconds, in the closest city to the area exactly 6734 kilometers east away from where Chuck Norris stomped his foot the second earlier, there was a major earthquake."}
^CINFO Received SIGINT, the service is closing       @service=bento
```

The console should now display the streamed contents from the API in real time, indicating that the Bento pipeline is active.

To stop the current stream, press `Ctrl + C` (on Windows/Linux) or `Command + C` (on macOS). This action is necessary to terminate the stream; otherwise, it will continue running indefinitely.

## Deep Dive

The following outlines the primary sections of a Bento YAML configuration file:

- `input`: Defines the data sources or inputs for the pipeline.
- `pipeline`: Specifies the processing logic, including nodes and their configurations.
- `output`: Describes where the processed data should be delivered.

Here’s an example structure:

```yaml
input:
  stdin: {}

pipeline:
  processors: []

output:
  stdout: {}
```
This structure forms the foundation for building Bento pipelines.

### **Input**

The [Inputs](/resources/stacks/bento/components/inputs/) section defines the data sources that Bento will use for processing. These sources can include APIs, file systems, or Kafka streams.

For example, to configure an HTTP input for fetching data from an API, use the following syntax:

```yaml
input:
  http_client:
    url: https://api.chucknorris.io/jokes/random
    verb: GET
    headers:
      Content-Type: application/JSON
```

This configuration directs Bento to fetch data from the specified API endpoint using an HTTP GET request.

### **Pipeline**

The `pipeline` section defines processors that transform the incoming data. Bento uses Blob[Bloblang](/resources/stacks/bento/bloblang/walkthrough/)lang, a flexible language designed for data transformation.

The [`processors`](/resources/stacks/bento/components/processors/) are specified as a subsection within the `pipeline` section. The following example demonstrates basic Bloblang transformations:

```yaml
pipeline:
  processors:
    - bloblang: |
        root = {
          "id": content.id,
          "name": content.name,
          "email": content.email,
          "phone": content.phone
        }
```

No prior knowledge of Bloblang is required to get started. Comprehensive guidance is available to help users understand Bloblang concepts, from basic principles to advanced techniques. For detailed instructions, visit the [Bloblang Guide](/resources/stacks/bento/bloblang/walkthrough/).

### **Output**

The `output` section defines where the transformed data will be stored. Outputs can include file systems, message queues, DataOS depots, or HTTP endpoints.  

In the following example, a file output is configured to store transformed data in a local file:  

```yaml
output:
  file:
    path: /home/Desktop/new.txt
    codec: lines
```

In this example:  
- The `file` field specifies the output type as a file system.  
- The `path` defines the location where the output file will be saved.  
- The `codec` is set to `lines`, ensuring each record is written as a separate line.  

This configuration stores transformed data efficiently in a local text file.

### **Example Code**

For the purposes of this guide, the Chuck Norris Jokes API will be used as an example. This API is selected due to its simplicity and ease of integration.

To begin, a Bento configuration file must be created. This file defines the inputs, outputs, and any required Bloblang transformations. The following example provides a starting point for this configuration file:

```yaml
input:
  http_client:
    url: https://api.chucknorris.io/jokes/random
    verb: GET
    headers:
      Content-Type: application/JSON

output:
  file:
    path: /home/Desktop/new.text # Path of the output file
    codec: lines # Writes every new 

pipeline:
  processors:
  - bloblang: |
      root = {
        "joke": this.value
      }
```

In this configuration file, an HTTP input is defined to retrieve a random Chuck Norris joke from the API. Additionally, a file output is specified to store the joke locally. A Bloblang processor is included to transform the data before it is written to the file.

To execute this configuration, save it as a `.yaml` (example: `pipeline.yaml`) file and run the following command:

```bash
bento -c /home/Desktop/pipeline.yaml
```

<aside class="callout">
🗣️ Remember to stop the current stream by pressing0 Ctrl + C (on Windows/Linux) or Command + C (on macOS). This action is necessary to terminate the stream; otherwise, it will continue running indefinitely.</a>.
</aside>

Before proceeding, it is recommended to review both the input and the processed output. To inspect the input, copy the specified URL into a web browser to observe the raw data. Next, review the content inside the output file to understand how the Bloblang processor has transformed the data.

This step ensures a clear understanding of the data flow and the applied transformations.

**Before Processing**

```bash
{
  "categories": [],
  "created_at": "2020-01-05 13:42:26.766831",
  "icon_url": "https://assets.chucknorris.host/img/avatar/chuck-norris.png",
  "id": "wNubD0vrQ-OCZFjBQUDOKA",
  "updated_at": "2020-01-05 13:42:26.766831",
  "url": "https://api.chucknorris.io/jokes/wNubD0vrQ-OCZFjBQUDOKA",
  "value": "Jesus Walked on water. Chuck Norris Swam on land"
}
```

**After Processing**

```bash
{"joke":"Jesus Walked on water. Chuck Norris Swam on land"}
```

Now, let's break down the Bloblang transformation a bit further. Here's what the code is doing:

```yaml
bloblang
root = {
  "joke": this.value
}
```

This transformation takes the incoming data and creates a new object with a single key-value pair. The key is "joke", and the value is the joke itself. the code essentially just extracting the joke from the API response and storing it in a more structured format.

In summary, this configuration demonstrates how to set up a Bento pipeline with minimal code. The pipeline retrieves Chuck Norris jokes from an API, processes the data using a Bloblang transformation, and stores the result locally.