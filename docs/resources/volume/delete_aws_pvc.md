# Steps to delete Volume data from AWS Cloud Storage

Follow the steps below to delete the Volume data from AWS Cloud Storage.

## Pre-requisites

- Ensure that no Resources are dependent on the volume being deleted. For instance, if a Service is utilizing a Volume of type CloudPersistent, that Service must be deleted prior to removing the volume data from AWS.

- Ensure that the individual has the necessary permissions to execute `kubectl` commands.

## 1. Get the Volume identifier

Whenever a Volume Resource is provisioned, in the backend, a corresponding Volume Identifier is generated in Kubernetes Cluster. To retrieve this identifier, execute the following command:

=== "Command"

    ```bash
    kubectl get pvc -a
    ```

=== "Expected Output"

    ```bash
    NAMESPACE       NAME                                               STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS       VOLUMEATTRIBUTESCLASS   AGE
    caretaker       pulsar-bookie-ledgers-pulsar-bookie-4              Bound    pvc-8d8a3912-1102-4c1f-a9b9-d1c27d6de       50Gi       RWO            disk-premium-delete <unset>                 
    caretaker       redis-data-redis-caretaker-master-0                Bound    pvc-ed98c71e-1093-46d8-bd0a-ff4985e0        100Gi      RWO            disk-premium-delete <unset>                 5d19h
    caretaker       redis-data-redis-sql-workbench-master-0            Bound    pvc-de4f597e-460e-4f31-821c-8ca7f159        5Gi        RWO            disk-premium-delete <unset>                 10d
    heimdall        redis-data-redis-heimdall-cache-master-0           Bound    pvc-6344689e-1f2f-4974-97d8-088041c7d507    10Gi       RWO            disk-premium-delete <unset>                 10d
    juicefs-system  redis-data-redis-storage-meta-master-0             Bound    pvc-da2a84c6-f0b9-4952-8b77-4dbefb4b842a    50Gi       RWO            disk-premium-delete <unset>                 10d
    public          persistent-v                                       Bound    pvc-34ab82f8-f18c-4ee0-85c5-2230d1505464    5Gi        RWX            juicefs-retain       <unset>                 10d
    sandbox         persistent-v                                       Bound    pvc-428581ed-dc67-4cdd-907b-e24f3fe533c5e   5Gi        RWX            juicefs-retain       <unset>                 10d
    sentinel        data-thanos-ruler-0                                Bound    pvc-36eb4fb6-5e76-4eb8-acba-0a6f0a26c1d1    5Gi        RWO            disk-premium-delete <unset>                 10d

    ```
For example, a Volume named `redis-data-redis-storage-meta-master-0` of type `CloudPersistent` was created. In the Kubernetes cluster, this resulted in the generation of a corresponding Volume Identifier: `pvc-da2a84c6-f0b9-4952-8b77-4dbefb4b842a`.


## 2. Search the Volume identifier in AWS Cloud

- In the AWS portal, open the "Volumes" section and search the Volume Identifier `pvc-da2a84c6-f0b9-4952-8b77-4dbefb4b842a`.

    <div style="text-align: center;">
      <img src="/resources/volume/awspvc.png" alt="AWS" style="border:1px solid black; width: 100%; height: auto;">
      <figcaption><i>AWS Cloud</i></figcaption>
    </div>

- Click on the `kubernetes.io/created-for/pv/name = pvc-da2a84c6-f0b9-4952-8b77-4dbefb4b842a`.

    <div style="text-align: center;">
      <img src="/resources/volume/awspvcsearch.png" alt="AWS" style="border:1px solid black; width: 100%; height: auto;">
      <figcaption><i>AWS Cloud</i></figcaption>
    </div>

## 3. Delete the Volume

Select the Volume and click on the "Actions" button, then select "Detach Volume".    

<div style="text-align: center;">
  <img src="/resources/volume/awspvcdel.png" alt="AWS" style="border:1px solid black; width: 100%; height: auto;">
  <figcaption><i>AWS Cloud</i></figcaption>
</div>

This will delete the Volume permanently from the AWS Cloud.
