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

<center>

|Name|Tags|
|---|---|
|[aws_dyanamodb](/resources/stacks/benthos/components/caches/aws_dyanamodb/)|AWS|
|[aws_s3](/resources/stacks/benthos/components/caches/aws_s3/)|AWS|
|[couchbase](/resources/stacks/benthos/components/caches/couchbase/)|Couchbase|
|[file](/resources/stacks/benthos/components/caches/file/)|Local|
|[gcp_cloud_storage](/resources/stacks/benthos/components/caches/gcp_cloud_storage/)|GCP|
|[memcached](/resources/stacks/benthos/components/caches/memcached/)|Memcached|
|[memory](/resources/stacks/benthos/components/caches/memory/)|Memory|
|[mongodb](/resources/stacks/benthos/components/caches/mongodb/)|MongoDB|
|[multilevel](/resources/stacks/benthos/components/caches/multilevel/)|Multiple Cache Level|
|[redis](/resources/stacks/benthos/components/caches/redis/)|Redis|
|[ristretto](/resources/stacks/benthos/components/caches/ristretto/)|Ristretto|

</center>