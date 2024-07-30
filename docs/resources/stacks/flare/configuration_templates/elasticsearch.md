# Elasticsearch Depots

To start executing Flare Jobs on Elasticsearch Depots, you first need to set up an Elasticsearch Depot. If you haven’t done it, navigate to the following link: [Elasticsearch Depot](/resources/depot/depot_config_templates/elasticsearch/).

## Read Configuration


For reading the data from an Elasticsearch depot, we need to configure the following property `name`, `dataset`, `format`, and Elasticsearch-specific property `es.nodes.wan.only` within `options` in the `inputs` section of the YAML. For instance, if your dataset name is `input`, the UDL address is `dataos://elasticsearch:default/elastic_write`  and the `format` set to `elasticsearch`. Then the inputs section will be as follows-

```yaml
inputs:
   - name: input
     dataset:  dataos://elasticsearch:default/elastic_write
     format: elasticsearch
     options:
        es.nodes.wan.only: 'true'
```
By setting `es.nodes.wan.only`, the connector will limit its network usage and instead of connecting directly to the target resource shards, it will make connections to the Elasticsearch cluster only.

**Sample Read configuration manifest**

Let’s take a case scenario where we read the dataset from Elasticsearch depot and store it in the Lakehouse within the DataOS. The read config manifest will be as follows:

!!!tip "Sample Read configuration manifest"

    ```yaml title="elasticsearch_depot_read.yml"
    --8<-- "examples/resources/stacks/flare/elasticsearch_depot_read.yml"
    ```

## Write Configuration

For writing the data to an Elasticsearch Depot, we need to configure the `name`, `dataset`, `format`, in the `outputs` section of the manifest. For instance, if your dataset name is `output01`, the dataset is to be stored at the location `dataos://elasticsearch:default/elastic_write` and the file format is `elasticsearch`. Then the inputs section will be as follows-

```yaml
outputs:
	- name: output01
	  dataset: dataos://elasticsearch:default/elastic_write?acl=rw
    format: elasticsearch
```

**Sample Read configuration manifest**

Let’s take a case scenario where we have to write the dataset to the an Elasticsearch Depot from the thirdparty Depot. The write config manifest will be as follows:

```yaml title="elasticsearch_depot_read.yml"
--8<-- "examples/resources/stacks/flare/elasticsearch_depot_write.yml"
```