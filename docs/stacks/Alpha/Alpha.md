# Alpha

Alpha Stack is a declarative DevOps software development kit (SDK) to publish data-driven applications in production. As a cohesive stack, it seamlessly integrates with web-server-based application images constructed atop DataOS, empowering users to leverage DataOS's compute resources to execute external tools or applications. With Alpha Stack, application development is no longer bound by programming language constraints, as it enables the fluid deployment of diverse applications onto a robust, flexible infrastructure.

When deploying an application using Alpha Stack, the containerized image contains all the essential functionalities and logic required for the application, while execution of the image occurs within DataOS via the utilization of Alpha Stack, which can be invoked or called within a Service or a Workflow Primitive/Resource.

## Getting Started with Alpha Stack

### Deploying Images from a Public DockerHub Repository

To begin the journey with Alpha Stack, let’s take an image already available on the public DockerHub repository and run it atop DataOS through Alpha Stack. To know more, navigate to the link below:

[Deploying Images on Public DockerHub ](./Deploying%20Images%20on%20Public%20DockerHub/Deploying%20Images%20on%20Public%20DockerHub.md)

### Deploying Images from a Private DockerHub Repository

You can also deploy custom-built images from a private DockerHub repository. To know more about this case scenario, navigate to the link below:

[Deploying images on a Private DockerHub ](./Deploying%20images%20on%20a%20Private%20DockerHub.md)

## Components of Alpha

```yaml
# PRIMITIVE/RESOURCE SECTION
version: v1
name: alpha-stack
type: workflow/service
workflow/service: # Properties Specific to Workflow/Service
# ...
# ...
# ...
  stack: alpha # Stack (Here it's Alpha)
	secrets:
		- newSecret # Secret (Resource/Primitive) to be referred within Alpha
	envs:
		LOG_LEVEL: info # Log Level
  alpha:

# ALPHA STACK SECTION
    image: swagger/swagger-ui # Path of the Docker Image
		command: # Command
			- streamlit
    arguments: # Arguments
      - run
			- app.py
```

## Primitive/Resource Section

Alpha Stack can be implemented or executed via a Workflow or as a Service. Workflow/Service are core DataOS primitives and are both provisioned as runnable. To know more about the YAML configurations for a Workflow/Service, refer to any of the below two sections:

[Workflow](./../../Primitives/Workflow/Workflow.md)

[Service](./../../Primitives/Service/Service.md)

## Alpha Stack Section

### `alpha`

All the configuration fields and values for the Alpha Stack are provided within the Alpha section.

```yaml
alpha:
	{} # All the fields and values for the Alpha stack are specified here
```

### `image`

The path to the respective Docker Image within the DockerHub repository.

Type: string

Default: NA

```yaml
image: swagger/swagger-ui # Path of the Docker Image
```

### `command`

This includes the commands that are mentioned within the CMD section of the Docker file.

For e.g., If the below is your Docker File, then the commands are provided within the CMD section:

```docker
# Dockerfile

FROM python:3.8-slim-buster

RUN pip install streamlit

WORKDIR /app
COPY app.py .

CMD ["streamlit", "run", "app.py"]
#     command      arguments 1 & 2
```

Syntax:

```yaml
command: 
	- streamlit
```

### `arguments`

The arguments are the additional arguments apart form the primary command specified within the Dockerfile, as described above

```yaml
arguments:
  - run
	- app.py
```

## Recipes

[Build a Streamlit App on DataOS](../Alpha/Build%20a%20Streamlit%20App%20on%20DataOS/Build%20a%20Streamlit%20App%20on%20DataOS.md)

[Alpha Stack within a Workflow ](./Alpha%20Stack%20within%20a%20Workflow.md)