# Eventhub

DataOS provides the capability to connect to Eventhub data using Depot. The Depot facilitates access to all documents that are visible to the specified user, allowing for text queries and analytics.

## Requirements

To establish a connection with Eventhub, the following information is required:

- Endpoint
- Eventhub Shared Access Key Name
- Eventhub Shared Access Key

## Template

To create a Depot of Eventhub, in the type field you will have to specify type 'EVENTHUB', and utilize the following template:

=== "v1"

    ```yaml
    name: {{"sanityeventhub01"}}
    version: v1
    type: depot
    tags:
      - {{Eventhub}}
      - {{Sanity}}
    layer: user
    depot:
      type: "EVENTHUB"
      compute: {{runnable-default}}
      spec:
        endpoint: {{"sb://event-hubns.servicebus.windows.net/"}}
      external: {{true}}
      connectionSecret:
        - acl: rw
          type: key-value-properties
          data:
            eh_shared_access_key_name: {{$EH_SHARED_ACCESS_KEY_NAME}}
            eh_shared_access_key: {{$EH_SHARED_ACCESS_KEY}}
    ```

=== "v2alpha"

    ```yaml
    name: {{"sanityeventhub01"}}
    version: v2alpha
    type: depot
    tags:
      - {{Eventhub}}
      - {{Sanity}}
    layer: user
    depot:
      type: "EVENTHUB"
      compute: {{runnable-default}}
      eventhub:
        endpoint: {{"sb://event-hubns.servicebus.windows.net/"}}
      external: {{true}}
      connectionSecret:
        - acl: rw
          type: key-value-properties
          data:
            eh_shared_access_key_name: {{$EH_SHARED_ACCESS_KEY_NAME}}
            eh_shared_access_key: {{$EH_SHARED_ACCESS_KEY}}
    ```
