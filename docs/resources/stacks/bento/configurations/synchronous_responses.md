# Synchronous Responses

In a regular Bento pipeline, messages will flow in one direction, and acknowledgments flow in the other:

```
    ----------- Message ------------->

Input (AMQP) -> Processors -> Output (AMQP)

    <------- Acknowledgement ---------
```

However, Bento has support for a number of protocols where this limitation is not the case.

For example, HTTP is a request/response protocol, and so our `http_server` input is capable of returning a response payload after consuming a message from a request.

When using these protocols, it's possible to configure Bento stream pipelines that allow messages to pass in the opposite direction, resulting in response messages at the input level:

```
           --------- Request Body -------->

Input (HTTP Server) -> Processors -> Output (Sync Response)

           <--- Response Body (and ack) ---
```

## Routing Processed Messages Back

It's possible to route the result of any Bento processing pipeline directly back to an input with a `sync_response` output:

```yaml
input:
  http_server:
    path: /post
pipeline:
  processors:
    - mapping: root = content().uppercase()
output:
  sync_response: {}
```

Using the above example, sending a request 'foo bar' to the path `/post` returns the response 'FOO BAR'.

It's also possible to combine a `sync_response` output with other outputs using a [`broker`](../components/inputs/broker.md):

```yaml
input:
  http_server:
    path: /post
output:
  broker:
    pattern: fan_out
    outputs:
      - kafka:
          addresses: [ TODO:9092 ]
          topic: foo_topic
      - sync_response: {}
        processors:
          - mapping: root = content().uppercase()
```

Using the above example, sending a request 'foo bar' to the path `/post` passes the message unchanged to the Kafka topic `foo_topic` and also returns the response 'FOO BAR'.

<aside style="padding:15px; border-radius:5px;">

🗣 It's safe to use these mechanisms even when combining multiple inputs with a broker, a response payload will always be routed back to the original source of the message.

</aside>


## Returning Partially Processed Messages

It's possible to set the state of a message to be the synchronous response before processing is finished by using the `sync_response` processor. This allows you to further mutate the payload without changing the response returned to the input:

```yaml
input:
  http_server:
    path: /post

pipeline:
  processors:
    - mapping: root = "%v baz".format(content().string())
    - sync_response: {}
    - mapping: root = content().uppercase()

output:
  kafka:
    addresses: [ TODO:9092 ]
    topic: foo_topic
```

Using the above example, sending a request 'foo bar' to the path `/post` passes the message 'FOO BAR BAZ' to the Kafka topic `foo_topic`, and also returns the response 'foo bar baz'.

However, it is important to keep in mind that due to Bento' strict delivery guarantees, the response message will not actually be returned until the message has reached its output destination and an acknowledgment can be made.

## Routing Output Responses Back

Some outputs, such as `http_client`, have the potential to propagate payloads received from their destination after sending a message back to the input:

```yaml
input:
  http_server:
    path: /post
output:
  http_client:
    url: http://localhost:4196/post
    verb: POST
    propagate_response: true
```

With the above example, a message received from the endpoint `/post` would be sent unchanged to the address `http://localhost:4196/post`, and then the response from that request would get returned back. This basically turns Bento into a proxy server with the potential to mutate payloads between requests.

The following config turns Bento into an HTTP proxy server that also sends all request payloads to a Kafka topic:

```yaml
input:
  http_server:
    path: /post
output:
  broker:
    pattern: fan_out
    outputs:
      - kafka:
          addresses: [ TODO:9092 ]
          topic: foo_topic
      - http_client:
          url: http://localhost:4196/post
          verb: POST
          propagate_response: true
```