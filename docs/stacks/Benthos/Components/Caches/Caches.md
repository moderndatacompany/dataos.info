# Caches

A cache is a key/value store which can be used by certain components for applications such as deduplication or data joins. Caches are configured as a named resource:

```yaml
cache_resources:
  - label: foobar
    memcached:
      addresses:
        - localhost:11211
      default_ttl: 60s
```

> It's possible to layer caches with read-through and write-through behaviour using the multilevel cache.
> 

And then any components that use caches have a field `resource` that specifies the cache resource:

```yaml
pipeline:
  processors:
    - cache:
        resource: foobar
        operator: add
        key: '${! json("message.id") }'
        value: "storeme"
    - mapping: root = if errored() { deleted() }
```

For the simple case where you wish to store messages in a cache as an output destination for your pipeline, check out the `cache` output. To see examples of more advanced uses of caches such as hydration and deduplication, check out the `cache` processor.

You can find out more about resources in this document.

[aws_dyanamodb](./aws_dyanamodb.md)

[aws_s3](./aws_s3.md)

[couchbase](./couchbase.md)

[file](./file.md)

[gcp_cloud_storage](./gcp_cloud_storage.md)

[memcached](./memcached.md)

[memory](./memory.md)

[mongodb](./mongodb.md)

[multilevel](./multilevel.md)

[redis](./redis.md)

[ristretto](./ristretto.md)