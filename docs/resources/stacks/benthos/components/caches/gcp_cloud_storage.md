# gcp_cloud_storage

Tags: GCP

<aside>
🗣 **BETA**

This component is mostly stable, but breaking changes could still be made outside of major version releases if a fundamental problem with the component is found.

</aside>

Use a Google Cloud Storage bucket as a cache.

```yaml
# Config fields, showing default values
label: ""
gcp_cloud_storage:
  bucket: ""
  content_type: ""
```

It is not possible to atomically upload cloud storage objects exclusively when the target does not already exist; therefore, this cache is not suitable for deduplication.

## Fields[](https://www.benthos.dev/docs/components/caches/gcp_cloud_storage#fields)

### `bucket`[](https://www.benthos.dev/docs/components/caches/gcp_cloud_storage#bucket)

The Google Cloud Storage bucket to store items in.

**Type:** `string`

---

### `content_type`[](https://www.benthos.dev/docs/components/caches/gcp_cloud_storage#content_type)

Optional field to explicitly set the Content-Type.

**Type:** `string`