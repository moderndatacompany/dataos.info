# Rate Limit

A rate limit is a strategy for limiting the usage of a shared resource across parallel components in a Bento instance or potentially across multiple instances. They are configured as a resource:

```yaml
rate_limit_resources:
  - label: foobar
    local:
      count: 500
      interval: 1s
```

And most components that hit external services have a field `rate_limit` for specifying a rate-limit resource to use, identified by the `label` field. For example, if we wanted to use our `foobar` rate limit with an `http_client` input, it would look like this:

```yaml
input:
  http_client:
    url: TODO
    verb: GET
    rate_limit: foobar
```

By using a rate limit in this way, we can guarantee that our input will only poll our HTTP source at the rate of 500 requests per second.

Some components don't have a `rate_limit` field, but we might still wish to throttle them by a rate limit, in which case we can use the `rate_limit` processor that applies back pressure to a processing pipeline when the limit is reached. For example, if we wished to limit the consumption of lines of a `csv` file input to a specified rate limit, we can do that with the following:

```yaml
input:
  csv:
    paths:
      - ./foo.csv
  processors:
    - rate_limit:
        resource: foobar
```

You can find out more about resources in this [document](/resources/stacks/bento/configurations/resources/).

<div style="text-align: center;" markdown="1">

|Name|Tags|
|---|---|
|[local](/resources/stacks/bento/components/rate_limit/local/)|Local|
|[redis](/resources/stacks/bento/components/rate_limit/redis/)|Redis |

</div>