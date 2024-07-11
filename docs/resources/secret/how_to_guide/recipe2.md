# Referencing Secrets to Pull Images from Private Container Registry

Following the successful creation of a Secret Resource, it can seamlessly pull images from the container registries. This approach obviates the need to embed sensitive authentication information directly within the resource configuration.

Container registries, pivotal for storing and managing images, including essential details like registry type, access credentials, and repository information, can efficiently reference pertinent secrets. This ensures a secure and streamlined process for pulling images from a private container registry without exposing sensitive authentication data within the configuration files.

=== "secret"
    ```yaml title="secret_image.yaml"
    --8<-- "examples/resources/secret/docker_image/secret_image.yaml"
    ```

=== "pull-image"    
    ```yaml title="refer_image_secret.yaml"
    --8<-- "examples/resources/secret/docker_image/alpha.yaml"
    ```