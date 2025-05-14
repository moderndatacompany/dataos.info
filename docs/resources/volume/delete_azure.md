# Steps to delete Volume data from Azure Cloud Storage

Follow the steps below to delete the Volume data from Azure Cloud Storage.

## Pre-requisites

- Ensure that no Resources are dependent on the volume being deleted. For instance, if a Service is utilizing a Volume of type CloudPersistent, that Service must be deleted prior to removing the volume data from Azure.

- Ensure that the individual has the necessary permissions to execute `kubectl` commands.

## 1. Get the Volume identifier

Whenever a Volume Resource is provisioned, in the backend, a corresponding Volume Identifier is generated in Kubernetes Cluster. To retrieve this identifier, execute the following command:

=== "Command"

    ```bash
    kubectl get pvc -n public
    ```

=== "Expected Output"

    ```bash
    NAME                       STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS          VOLUMEATTRIBUTESCLASS     AGE
    cola-volume                Bound    pvc-26574dc5-89ee-4269-abcf-38d8d48801e     50Gi       RWO            juicefs-retain        <unset>                  18d
    lake-search-store-volume   Bound    pvc4fc91598-4b00-482d-87cf-f3aa34c9f58b     0Gi        RWO            juicefs-retain        <unset>                  14d
    ls-test-01                 Bound    pvc4f73155c-2505-4f63-91ac-0fae6dac94aa     8Gi        RWO            disk-premium-delete   <unset>                  28d
    ls-vol-02                  Bound    pvc6e5d2d2d-d3da-4c33-81a3-229d9910c5f      8Gi        RWO            disk-premium-delete   <unset>                  16d
    ncdc-vol-01                Bound    pvc98d352e6-fee6-4395-84a9-2f9d645a986      8Gi        RWO            disk-premium-delete   <unset>                  17d
    ncdc-vol-02                Bound    pvcf19b6419-9b7f-4153-b614-830cfcb5fa64     8Gi        RWO            disk-premium-delete   <unset>                  17d
    ncdc-vol-03                Bound    pvc85d525f7-79e4-41ae-b2c1-420bf860368f     8Gi        RWO            disk-premium-delete   <unset>                  15d
    ncdc-vol-04                Bound    pvcb0db9bd9-0ab0-4eb8-8f9f-03a72a0e5e3b     8Gi        RWO            juicefs-retain        <unset>                  15d
    persistent-v               Bound    pvc-8b75b7bcf-5bc8-4a3c-ada7-ba859553392    8Gi        RWX            disk-premium-retain   <unset>                  18h
    testvolume                 Bound    pvc-5d4c5939-3702-4b77-8d87-37117b78bb1c    8Gi        RWX            juicefs-delete        <unset>                  29d
    volume01test               Bound    pvc7843f55c-9ec5-417e-a5d0-f8e98478228      1Gi        RWX            juicefs-delete        <unset>                  13d
    volumetest                 Pending                                                                                              <unset>                  13d
    volumetesttemp             Bound    pvcf5e856c03-3555-42be-9e47-e34b54b4e0c     8Gi        RWO            juicefs-delete        <unset>                  13d

    ```
For testing purpose, a Volume named `testvolume` of type `CloudPersistent` was created. In the Kubernetes cluster, this resulted in the generation of a corresponding Volume Identifier: `pvc-5d4c5939-3702-4b77-8d87-37117b78bb1c`.


## 2. Search the Volume identifier in Azure Cloud

- In the Azure portal, go to the "Kubernetes services" under the "Azure services" section.

    <div style="text-align: center;">
      <img src="/resources/volume/azureui.png" alt="Microsoft Azure" style="border:1px solid black; width: 100%; height: auto;">
      <figcaption><i>Microsoft Azure</i></figcaption>
    </div>


- Go to the "Disks" section, and search the `pvc-5d4c5939-3702-4b77-8d87-37117b78bb1c` created with `testvolume`. 

    <div style="text-align: center;">
      <img src="/resources/volume/pv001.png" alt="Microsoft Azure" style="border:1px solid black; width: 100%; height: auto;">
      <figcaption><i>Microsoft Azure</i></figcaption>
    </div>

    <div style="text-align: center;">
      <img src="/resources/volume/pv002.png" alt="Microsoft Azure" style="border:1px solid black; width: 100%; height: auto;">
      <figcaption><i>Microsoft Azure</i></figcaption>
    </div>



## 3. Delete the Volume

Click on the "Delete" button and select "OK".

<div style="text-align: center;">
  <img src="/resources/volume/pv003.png" alt="Microsoft Azure" style="border:1px solid black; width: 100%; height: auto;">
  <figcaption><i>Microsoft Azure</i></figcaption>
</div>

This will delete the Volume permanently from the Azure Cloud.




