# Getting Started

Welcome to the world of Benthos, a resilient stream processing stack that enables you to handle your data flows with ease!

If you're new to the game, fret not! We've got you covered with this step-by-step guide to getting you started. The first step is to become familiar with Benthos on your local system, which is considered part of the best practices to thoroughly test your data pipelines before unleashing them into the wilds of production. 

From there, we'll guide you through the transition to DataOS and beyond. Follow along with our expert guidance and before you know it, you'll be a Benthos whiz.

## Install

Firstly, let's get started by installing the Benthos stack. The installation process is a breeze, that involves a single command to be executed on the command line:  

```bash
curl -Lsf https://sh.benthos.dev | bash # Downloads the latest stable version
```

### Use Docker

If you have docker installed, you can pull the latest official Benthos image with:

```bash
docker pull jeffail/benthos
docker run --rm -v /path/to/your/config.yaml:/benthos.yaml jeffail/benthos
```

### **Homebrew**

On macOS, Benthos can be installed via Homebrew:

```bash
brew install benthos
```

Once you have successfully installed the stack, you're ready to dive in and start processing data.

## Building a stream pipeline

Once you have Benthos installed, you can start experimenting with the different components that Benthos provides. A Benthos stream pipeline is configured with a single YAML config file. Let's start by creating a simple pipeline that reads data from a file and writes it to the console. Here's the code:

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

This YAML configuration instructs Benthos to read data from the specified file and write it to the console as a stream of lines. The `codec: lines` setting ensures that each line of data is separated by a new line character.

Once you have your pipeline configuration ready, save it to a file (let's call it `pipeline.yaml`) and run the following command to start Benthos:

```bash
benthos -c <path-of-the-config-file>
```

**Example**

```bash
benthos -c /home/Desktop/pipeline.yaml # Path of the file

# Expected Output
INFO Running main config from specified file       @service=benthos path=pipeline.yaml
INFO Launching a benthos instance, use CTRL+C to close  @service=benthos
INFO Listening for HTTP requests at: http://0.0.0.0:4195  @service=benthos
{"categories":[],"created_at":"2020-01-05 13:42:28.420821","icon_url":"https://assets.chucknorris.host/img/avatar/chuck-norris.png","id":"J2-jeEq5QwKh4LiuwKpCvw","updated_at":"2020-01-05 13:42:28.420821","url":"https://api.chucknorris.io/jokes/J2-jeEq5QwKh4LiuwKpCvw","value":"Chuck Norris shaves with a hunting knife. \"Shaving\" consists of cutting a new mouth-hole every morning. That's how tough his beard is."}
{"categories":[],"created_at":"2020-01-05 13:42:27.496799","icon_url":"https://assets.chucknorris.host/img/avatar/chuck-norris.png","id":"2itjvbXZTcScUiuAMoOPLA","updated_at":"2020-01-05 13:42:27.496799","url":"https://api.chucknorris.io/jokes/2itjvbXZTcScUiuAMoOPLA","value":"Chuck Norris can slit your throat with his pinkie toenail."}
```

Voila! You should now see the contents from the API streaming in real time on your console. You've just created your first Benthos pipeline. 

Before you take a deep dive into the realm of Benthos, stop the current stream by pressing `Ctrl + C` or `Command + C`, or else it would keep going on for eternity.

## Let’s Dive Deeper

That was just the trailer. Now it's time to experiment and explore the many other features that Benthos has to offer. Trust us, you'll love it! 

But before that, let’s understand the structure of Benthos YAML config in more detail.

The main sections that make up a config are `input`, `pipeline`, and `output`. Kind of like this:

```yaml
input:
  stdin: {}

pipeline:
  processors: []

output:
  stdout: {}
```

### **Input**

Inputs are the sources of data that Benthos will use to process. They can be anything from APIs, file systems, or even Kafka streams. The configurations of the input sources are specified in the `input` section.

For example, you can use an HTTP input to fetch data from an API like below

```yaml
input:
  http_client:
    url: https://api.chucknorris.io/jokes/random
    verb: GET
    headers:
      Content-Type: application/JSON
```

There are many-many supported sources that you will get tired of getting to know of.

### **Pipeline**

Next up, we have the `pipeline` section. Within the pipeline, we define processors to transform the data we have fetched from the API. Bloblang is a powerful and flexible language that Benthos uses to perform transformations. In this example, we will be applying some basic Bloblang transformations to the data. The `processors` are defined as a sub-section with the `pipeline` section as elucidated below:

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

Don’t worry if you don’t understand even a single word of Bloblang. We will teach you like a kid, and you will be a hero from zero in no time.

### **Output**

Finally, we will use outputs to store the transformed data. Outputs can be anything from file systems, message queues, DataOS depots, or even HTTP endpoints. In this example, we will be using a file output to store the transformed data in a local file.

```yaml
output:
  file:
    path: /home/Desktop/new.text 
    codec: lines 
```

And that’s it! You have survived the theory part, now go back to your code editor.

### **Back to Code**

Now let's choose a random API to work with. For the purposes of this guide, we'll use the Chuck Norris Jokes API. Not only is it a great source of entertainment, but it's also a simple and straightforward API to work with.

To get started, we'll need to create a Benthos configuration file. In this file, we'll define our inputs, outputs, and any necessary Bloblang transformations. Here's a configuration file to get us started:

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

In this configuration file, we've defined an HTTP input to retrieve a random Chuck Norris joke from the API. We've also defined a file output to store the joke locally on our machine. Finally, we've added a Bloblang processor to transform the data before writing it to the file.

Now let’s put it all together, save it in a YAML file, and execute it using the command given below

```bash
benthos -c /home/Desktop/pipeline.yaml
```

And there you have it! But before you go dancing in the park, check out both the input (by copying the URL in any browser) and the processed output (inside the output file). This would help you understand what the Bloblang processor is doing.

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

This transformation takes the incoming data and creates a new object with a single key-value pair. The key is "joke", and the value is the joke itself. We're essentially just extracting the joke from the API response and storing it in a more structured format.

That’s it! With just a few lines of code, we've set up a Benthos pipeline to retrieve Chuck Norris jokes from an API, transform the data using Bloblang, and store the result locally on our machine. Now go forth and use your newfound powers for good (or for laughter)!