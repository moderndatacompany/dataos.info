# Amazon Redshift Depots


To read/write data on the Redshift data source, you first need to create a Depot on top of it. In case you haven’t created a Redshift Depot navigate to the link: [Redshift Depot](/resources/depot/depot_config_templates/amazon_redshift/).

## Read Config

Once you have set up a Redshift Depot, you can start reading data from it. 


**Sample Read configuration manifest**

Let’s take a case scenario where the dataset is stored in Redshift Depot and you have to read data from the source, perform some transformation steps and write it to Lakehouse (e.g. Icebase) within the DataOS. The read config manifest will be as follows:

Sample Input section

```yaml
inputs:
  - name: cities
    dataset: dataos://redshift:public/city_01
    format: Redshift
```
???tip "Sample read configuration manifest"

    ```yaml title="redshift_depot_read.yml"
    --8<-- "examples/resources/stacks/flare/redshift_depot_read.yml"
    ```

## Write Config

Sample Output section

```yaml
outputs:
  - name: cities
    dataset: dataos://redshift:public/sanity_redshift_write?acl=rw
    format: redshift
    options:
      saveMode: append
```

Sample write configuration manifest

???tip "Sample write configuration manifest"

    ```yaml title="redshift_depot_write.yml"
    --8<-- "examples/resources/stacks/flare/redshift_depot_write.yml"
    ```