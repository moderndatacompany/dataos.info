# Pagination in Bento
## Overview
Pagination in Bento is an essential mechanism for managing the processing of large data streams effectively. By partitioning data into manageable chunks or "pages," users can regulate the flow of data through their pipelines, ensuring optimal performance and resource utilization.

## Concepts
* **Pages:** In Bento, pages serve as discrete sections of the data stream, each containing a subset of the total data. Pages are defined by parameters such as size limits and are instrumental in facilitating efficient data processing.

* **API Keys:** Navigation between pages is facilitated through API keys, which provide references to adjacent pages. These keys enable seamless traversal through the dataset, allowing users to access and process data incrementally.

* **Limitations:** Pages impose constraints on the volume of data they can accommodate, serving to prevent resource exhaustion and maintain system stability. Users can specify parameters such as the maximum number of messages or data size per page.

## Configuration
Pagination configuration in Bento involves specifying parameters related to page size, interval, and navigation. These settings are typically defined in the configuration file, allowing users to customize pagination behavior to suit their specific requirements.

## Usage
Pagination can be applied across various components within the Bento pipeline to regulate data flow at different stages of processing. Users can incorporate pagination settings into input sources, processing stages, and output destinations, enabling fine-grained control over data processing operations.

## Example:
First, we'll create a YAML file where pagination will be configured.

### Input Section
<details>
  <summary><strong>YAML Configurations</strong></summary>

```yaml
input:
  label: "consume_data_page_indicator"
  http_server:
    address: "0.0.0.0:4295"
    path: /tablePaginator
    allowed_verbs:
      - POST
    timeout: 5s
    rate_limit: ""
  processors:
  - label: "input_log"
    log:
      level: INFO
      message: 'table paginator - received hit with query ${! json("query")}'
  # - label: "send_a_response_back"
  #   sync_response: {}
```
</details>





#### Explanation:

- **label:** The label assigned to this input component, indicating its purpose or function within the pipeline. In this case, it's labeled as `consume_data_page_indicator`.

- **http_server:**
  - Configuration for an HTTP server, specifying its properties.
  - **address:** The IP address and port on which the HTTP server will listen for incoming requests. Here, it's set to `0.0.0.0:4295`.
  - **path:** The URL path at which the server will accept requests. In this case, it's `/tablePaginator`.
  - **allowed_verbs:** The HTTP methods allowed for incoming requests. Only POST requests are allowed.
  - **timeout:** The maximum duration for which the server will wait for a request to be processed before timing out, set to 5 seconds.
  - **rate_limit:** Optional field for configuring rate limiting on incoming requests. It's currently left empty, indicating no rate limiting is applied.

- **input_log Processor:**
  - This processor logs information about incoming requests.


### Processor Section

<details>
  <summary><strong>YAML Configurations</strong></summary>

```yaml
pipeline:
  processors:
    - label: "fetch_table_page"
      branch:
        request_map: 'root = this'
        processors:
          - bloblang: |
              root = ""
              meta query = this.query
          
          - log:
              level: INFO
              message: 'https://fun-bluefish.dataos.app/metis/api/v1/tables?${! meta("query")}'
          - http:
              url: 'https://fun-bluefish.dataos.app/metis/api/v1/tables?${! meta("query")}'
              verb: GET
              headers:
                apikey: cmFrZXNoX3Rlc3RpbmcuZDVjYjQ1NDgtMzdlMC00YzlhLThlMjQtMjJlZjhiMThhMzk3
                Content-Type: application/json
        result_map: 'root = this'
    - label: "call_next_page_if_applicable"
      branch:
        request_map: 'root = this.paging'
        processors:
          - label: "conditional_check"
            switch:
              - check: this.exists("after")
                processors:
                  - bloblang: |
                      root = {}
                      root.query = "after=" + this.after
                  - http:
                      url: "http://localhost:4295/tablePaginator"
                      verb: POST
                      retries: 0
                      timeout: 120s
                      successful_on:
                        - 408
                      headers:
                        Content-Type: application/json
    - label: "process_json_response"
      bloblang: |
        root = this.data
    - label: "unarchive_json_array"
      unarchive:
        format: json_array
    - label: "split_array"
      split:
        size: 1
    - label: "log_processor_message"
      log:
        level: INFO
        message: '${! json("name") }'
    - bloblang: root = deleted()
``` 
</details>

#### Explanation:

- **fetch_table_page Processor:**
  - This processor initiates the fetching of a table page from an API.
  - It branches the data flow, setting up a query parameter using Bloblang and logging the URL of the API endpoint.
  - Then, it sends an HTTP GET request to the specified URL, including the query parameter and required headers.
  - The result of the HTTP request is mapped back to the root of the message.

- **call_next_page_if_applicable Processor:**
  - This processor checks if a next page exists based on pagination parameters.
  - If a next page exists, it constructs a query parameter for the next page and sends a POST request to a local endpoint (`http://localhost:4295/tablePaginator`) using Bloblang to modify the message payload.

- **process_json_response Processor:**
  - This processor handles the JSON response data from the API by setting the root of the message to the JSON data.

- **unarchive_json_array Processor:**
  - This processor unarchives the JSON data assuming it's in JSON array format.

- **split_array Processor:**
  - This processor splits the JSON array into individual messages, each containing one element of the array.

- **log_processor_message Processor:**
  - This processor logs the value of the "name" field from the JSON data.

- **bloblang Processor:**
  - This processor deletes the message.



Upon the execution of the provided YAML configuration, the resulting output will manifest as follows.

``` shell
bento -c /home/pagination-bento/paginator.yaml
INFO Running main config from specified file       @service=bento bento_version=4.24.0 path=/home/pagination-bento/paginator.yaml
INFO Listening for HTTP requests at: http://0.0.0.0:4195  @service=bento
INFO Receiving HTTP messages at: http://0.0.0.0:4295/tablePaginator  @service=bento label=consume_data_page_indicator path=root.input
INFO Launching a bento instance, use CTRL+C to close  @service=bento
```

Following the execution of the above mentioned YAML configuration, the subsequent step involves creating another Bento YAML file containing the following endpoint configurations.

<details>
  <summary><strong>YAML Configurations</strong></summary>

```yaml
input:
  generate:
    mapping: 'root = {}'
    interval: '@every 1s'
    count: 1
  processors:
    - label: "call_tables_paginator" 
      branch:
        request_map: |
            root = {}
            root.query = "after="
        processors:
          - branch:
              request_map: root = this
              processors:
                - http:
                    url: "http://localhost:4295/tablePaginator"
                    verb: POST
                    retries: 0
                    timeout: 120s
                    headers:
                      Content-Type: application/json
                - log:
                    level: INFO
                    message: "Requst sent to databaseSourcePaginator" 
 ```
</details> 

#### Explanation:

1. **Input Generation:**
   - The input component generates data periodically at every 1 second interval: `@every 1s`, emitting one message per interval (`count: 1`).

2. **Processors:**

   - **call_tables_paginator Processor:**
     - This processor branches the data flow into two paths. 
     - The `request_map` field sets up a query parameter for pagination. In this case, it initializes an empty object `root` and sets `root.query = "after="`, likely preparing for pagination.
     - Within the branch, there are two processors:
       - The HTTP processor sends a POST request to the URL `http://localhost:4295/tablePaginator`. It specifies additional parameters such as retries, timeout, and headers.
       - After the HTTP request is made, the log processor logs a message at INFO level indicating that the request has been sent.

#### Logic:
- The input generates data periodically.
- The data is processed by the `call_tables_paginator` processor, which sets up a query parameter for pagination and sends a POST request to an external service. The response from this service is handled in previous YAML configuration.



Upon implementing the provided YAML configuration in another terminal tab, the output generated will resemble the following pattern:

<details>
  <summary><strong>Terminal Output</strong></summary>

```shell
INFO https://fun-bluefish.dataos.app/metis/api/v1/tables?after=aWNlYmFzZS5pY2ViYXNlLmNsaS5jaXR5XzAx  @service=bento label="" path=root.pipeline.processors.0.branch.processors.1
INFO table paginator - received hit with query after=aWNlYmFzZS5pY2ViYXNlLmh1YnNwb3QuY29tcGFueV9wcm9wZXJ0eV9oaXN0b  @service=bento label=input_log path=root.input.processors.0
INFO customer_profiles                             @service=bento label=log_processor_message path=root.pipeline.processors.5
INFO consumer_info                                 @service=bento label=log_processor_message path=root.pipeline.processors.5
INFO consumer_medical_history                      @service=bento label=log_processor_message path=root.pipeline.processors.5
INFO consumer_purchase                             @service=bento label=log_processor_message path=root.pipeline.processors.5
INFO prescriptions_info                            @service=bento label=log_processor_message path=root.pipeline.processors.5
INFO purchase_transaction_data                     @service=bento label=log_processor_message path=root.pipeline.processors.5
INFO dc_info                                       @service=bento label=log_processor_message path=root.pipeline.processors.5
INFO dc_inventory_info                             @service=bento label=log_processor_message path=root.pipeline.processors.5
INFO dc_inventory_iot                              @service=bento label=log_processor_message path=root.pipeline.processors.5
INFO gcs_write_hadoop_13                           @service=bento label=log_processor_message path=root.pipeline.processors.5
INFO https://fun-bluefish.dataos.app/metis/api/v1/tables?after=aWNlYmFzZS5pY2ViYXNlLmh1YnNwb3QuY29tcGFueV9wcm9wZXJ0eV9oaXN0b  @service=bento label="" path=root.pipeline.processors.0.branch.processors.1
INFO gcs_write_hive_13                             @service=bento label=log_processor_message path=root.pipeline.processors.5
INFO association_type                              @service=bento label=log_processor_message path=root.pipeline.processors.5
INFO company                                       @service=bento label=log_processor_message path=root.pipeline.processors.5
INFO company_property_history                      @service=bento label=log_processor_message path=root.pipeline.processors.5
INFO contact                                       @service=bento label=log_processor_message path=root.pipeline.processors.5
INFO contact_company                               @service=bento label=log_processor_message path=root.pipeline.processors.5
INFO contact_form_submission                       @service=bento label=log_processor_message path=root.pipeline.processors.5
INFO contact_list                                  @service=bento label=log_processor_message path=root.pipeline.processors.5
INFO contact_list_member                           @service=bento label=log_processor_message path=root.pipeline.processors.5
INFO contact_property_history                      @service=bento label=log_processor_message path=root.pipeline.processors.5
INFO table paginator - received hit with query after=aWNlYmFzZS5pY2ViYXNlLmh1YnNwb3QuZGVhbF9waXBlbGluZQ==  @service=bento label=input_log path=root.input.processors.0
INFO https://fun-bluefish.dataos.app/metis/api/v1/tables?after=aWNlYmFzZS5pY2ViYXNlLmh1YnNwb3QuZGVhbF9waXBlbGluZQ==  @service=bento label="" path=root.pipeline.processors.0.branch.processors.1
INFO table paginator - received hit with query after=aWNlYmFzZS5pY2ViYXNlLmh1YnNwb3QuZW1haWxfZXZlbnRfZHJvcHBlZ  @service=bento label=input_log path=root.input.processors.0
INFO deal                                          @service=bento label=log_processor_message path=root.pipeline.processors.5
INFO deal_company                                  @service=bento label=log_processor_message path=root.pipeline.processors.5
INFO deal_contact                                  @service=bento label=log_processor_message path=root.pipeline.processors.5
INFO deal_pipeline                                 @service=bento label=log_processor_message path=root.pipeline.processors.5
INFO deal_pipeline_stage                           @service=bento label=log_processor_message path=root.pipeline.processors.5
INFO deal_property_history                         @service=bento label=log_processor_message path=root.pipeline.processors.5
INFO deal_stage                                    @service=bento label=log_processor_message path=root.pipeline.processors.5
INFO email_campaign                                @service=bento label=log_processor_message path=root.pipeline.processors.5
INFO email_event                                   @service=bento label=log_processor_message path=root.pipeline.processors.5
INFO email_event_bounce                            @service=bento label=log_processor_message path=root.pipeline.processors.5
INFO https://fun-bluefish.dataos.app/metis/api/v1/tables?after=aWNlYmFzZS5pY2ViYXNlLmh1YnNwb3QuZW1haWxfZXZlbnRfZHJvcHBlZA @service=bento label="" path=root.pipeline.processors.0.branch.processors.1
INFO email_event_click                             @service=bento label=log_processor_message path=root.pipeline.processors.5
INFO email_event_deferred                          @service=bento label=log_processor_message path=root.pipeline.processors.5
INFO email_event_delivered                         @service=bento label=log_processor_message path=root.pipeline.processors.5
INFO email_event_dropped                           @service=bento label=log_processor_message path=root.pipeline.processors.5
INFO email_event_open                              @service=bento label=log_processor_message path=root.pipeline.processors.5
INFO email_event_sent                              @service=bento label=log_processor_message path=root.pipeline.processors.5
INFO email_event_spam_report                       @service=bento label=log_processor_message path=root.pipeline.processors.5
INFO email_event_status_change                     @service=bento label=log_processor_message path=root.pipeline.processors.5
INFO email_event_suppressed                        @service=bento label=log_processor_message path=root.pipeline.processors.5
INFO email_subscription                            @service=bento label=log_processor_message path=root.pipeline.processors.5
```
</details>

