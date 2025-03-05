# Using CUE

> 🗣 EXPERIMENTAL
CUE support is experimental. It may change for some time to improve CUE's ability to type-check Bento configurations at the expense of causing new validation errors when moving from one Bento release to the next.


[CUE](https://cuelang.org/) is a powerful configuration language that makes it easier and safer to build Bento configurations. It achieves this by validating and type-checking configurations as well as allowing you to build useful utilities that reduce boilerplate. In this guide, we will see how to build a Bento configuration using CUE, export it to YAML, and execute it.

## Prerequisites

Before you get started, ensure that you have installed CUE by [following this guide](https://cuelang.org/docs/install/). If this is your first time working with it, then it's a great idea to step through the [CUE tutorial](https://cuelang.org/docs/tutorials/) and familiarize yourself with the language.

## Create

Create a directory for the CUE module that will contain our bento configuration:

```bash
mkdir hello-cue
cd hello-cue
cue mod init example.com/hello-cue
touch config.cue
```

> CUE modules must start with a hostname. This will typically be the URL of your repository. For example: cue mod init github.com/bentodev/hello-cue.
> 

The `bento list` command will generate a CUE package containing the types we'll need to build our configuration. Let's write this package into our project:

```bash
mkdir bento
bento list --format cue > bento/schema.cue
```

At this point, you should now have the following directory structure:

```bash
hello-cue/
    bento/
        schema.cue
    cue.mod/
        pkg/
        usr/
        module.cue
    config.cue
```

We are now ready to write our Bento config in CUE. Let's start by editing our `config.cue` to include the following snippet:

```yaml
import "example.com/hello-cue/bento"

bento.#Config & {
  input: {
    generate: {
      mapping: """
      root = { "message": "Hello, CUE!" }
      """
    }
  }

  pipeline: {
    processors: [
      {
        mapping: """
        root = this
        root.id = uuid_v4()
        """
      }
    ]
  }

  output: {
    stdout: {}
  }
}
```

Let's see what this will look like as YAML by running `cue export` while in the `hello-cue` directory:

```bash
cue export --out yaml config.cue
```

This should output something like this:

```yaml
input:
  generate:
    mapping: 'root = { "message": "Hello, CUE!" }'
pipeline:
  processors:
    - mapping: |-
        root = this
        root.id = uuid_v4()
output:
  stdout: {}
tests: []
```

We can run this with Bento to see that it indeed works:

```bash
bento -c <(cue export --out yaml config.cue)
```

When you are satisfied with the results, terminate the Bento process and let's move on to look at some of the nice features that we get with CUE.

## Enhance

The `config.cue` above looks eerily like JSON. This is because CUE is a superset of JSON and shares its syntax. However, we can shorten our configuration to reduce identation and curly brackets. Let's rewrite `config.cue` to look like this:

```yaml
import "example.com/hello-cue/bento"

bento.#Config & {
  input: generate: mapping: """
  root = { "message": "Hello, CUE!" }
  """

  pipeline: processors: [
    {
      mapping: """
      root = this
      root.id = uuid_v4()
      """
    }
  ]

  output: stdout: {}
}
```

If you run the same `cue export` command from earlier, you'll notice that the YAML output is the same.

Next, we'll look at what some error handling patterns might look like with CUE. One typical technique to detect messages with errors is to use the `switch` output to wrap another output with some error detection and handling. Another pattern involves limiting the number of retries on a given output that is misbehaving and rejecting or dropping messages with some useful logging. If we combine all these concepts together we get:

```yaml
output:
  switch:
    cases:
      - check: errored()
        output:
          reject: "failed to process message: ${! error() }"
      - output:
          retry:
            max_retries: 5
            output:
              gcp_pubsub:
                project: "sample-project"
                topic: "sample-topic"
```

There are quite a few lines of YAML here and we seem to be going sideways as we compose more functionality. We can try and make this more manageable with CUE!

Let's create a new file in our `hello-cue` directory called `bento/helpers.cue`:

```bash
touch bento/helpers.cue
```

In this file, add the following snippet:

```yaml
package bento

#Guarded: self = {
  // The desired output that will be wrapped with error handling mechanisms
  #output: #Output

  // The error text to emit if the output receives any messages which contained
  // processing errors
  #errorMessage: string

  // The number of retries to attempt on the desired output (default is 3)
  #maxRetries: uint | *3

  // The error message to emit if the retry attempts are exhausted
  #retryErrorMessage: string

  // Whether to drop or reject any failed messages
  #errorHandling: "drop" | "reject"

  switch: cases: [
    {
      check: "errored()"
      output: {
        if self.#errorHandling == "reject" { reject: self.#errorMessage }

        if self.#errorHandling == "drop" {
          drop: {}
          processors: [{ log: message: self.#errorMessage }]
        }
      }
    },
    {
      output: fallback: [
        {
          retry: {
            max_retries: self.#maxRetries
            output: self.#output
          }
        },
        {
          if self.#errorHandling == "reject" { reject: self.#retryErrorMessage }

          if self.#errorHandling == "drop" {
            drop: {}
            processors: [{ log: message: self.#retryErrorMessage }]
          }
        }
      ]
    }
  ]
}
```

Now, let's get back to `config.cue` and edit a few bits while leveraging this helper:

```yaml
import "example.com/hello-cue/bento"

bento.#Config & {
  input: generate: {
    count: 1
    interval: "0"
    mapping: """
    root = { "message": "Hello, CUE!" }
    """
  }

  output: bento.#Guarded & {
    #errorMessage: "failed to process message: ${! error() }"

    #maxRetries: 3
    #retryErrorMessage: "failed to output message after \(#maxRetries) retries"

    #errorHandling: "drop"

    #output: http_client: {
      url: "http://localhost:4195/sad-blob"
      retries: 0
    }
  }
}
```

If you rerun `cue export` now, you'll see that we've wrapped our output with a couple of error-handling mechanisms. We also had access to powerful CUE features like conditional fields based on `#errorHandling`, default values, and interpolations.

```yaml
input:
  generate:
    count: 1
    interval: "0"
    mapping: 'root = { "message": "Hello, CUE!" }'
output:
  switch:
    cases:
      - check: errored()
        output:
          drop: {}
          processors:
            - log:
                message: 'failed to process message: ${! error() }'
      - output:
          fallback:
            - retry:
                max_retries: 3
                output:
                  http_client:
                    url: http://localhost:4195/sad-blob
                    retries: 0
            - drop: {}
              processors:
                - log:
                    message: failed to output message after 3 retries
tests: []
```

The final directory structure of your hello-cue project should look like this:

```bash
hello-cue/
    bento/
        schema.cue
        helpers.cue
    cue.mod/
        pkg/
        usr/
        module.cue
    config.cue
```

## Included CUE types

The `bento.cue` file we emitted earlier contains a number of useful types that we can use when build configuration files and helpers. These include:

- `bento.#Config`

This definition describes the format of a Bento config file. You'll want to use it at the top of your configuration file to validate its overall structure.

- `bento.#Input`
- `bento.#Output`
- `bento.#Processor`
- `bento.#RateLimit`
- `bento.#Buffer`
- `bento.#Cache`
- `bento.#Metric`
- `bento.#Tracer`

Each of these definitions is a disjunction that holds all the corresponding components in Bento. In other words, a CUE field that is specified as `bento.#Input`, such as `myfield: bento.#Input`, must resolve to a valid Bento input.

## Wrap up

Being able to define helper packages and definitions like `#Guarded` and reusing them across your Bento configurations is a really powerful feature of CUE. This will allow you to share consistent good practices without messy boilerplate across projects and teams!