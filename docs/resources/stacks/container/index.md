---
title: Container Stack
search:
  boost: 2
---

# Container Stack

Container [Stack](/resources/stacks/) is a declarative DevOps software development kit (SDK) to publish data-driven applications in production. As a cohesive Stack, it seamlessly integrates with web-server-based application images constructed atop DataOS, empowering users to leverage DataOS's [Compute](/resources/compute/) Resource to execute external tools or applications. With Container Stack, application development is no longer bound by programming language constraints, as it enables the fluid deployment of diverse applications onto a robust, flexible infrastructure.

When deploying an application using Container Stack, the containerized image contains all the essential functionalities and logic required for the application, while execution of the image occurs within DataOS via the utilization of Container Stack, which can be invoked or called within a [Service](/resources/service/), [Worker](/resources/worker/) or a [Workflow](/resources/workflow/) Resource.

<!--## Syntax of Container Stack manifest

![Container Manifest Configuration Syntax](/resources/stacks/container/container_syntax.png)

<center><i>Container manifest configuration syntax</i></center>-->

## Getting Started with Container Stack

### **Deploying Images from a Public DockerHub Repository**

To begin the journey with Container Stack, let’s take an image already available on the public DockerHub repository and run it atop DataOS through Container Stack. To know more, navigate to the link below:

[Deploying Images on Public DockerHub ](/resources/stacks/container/deploying_images_on_public_dockerhub/)

### **Deploying Images from a Private DockerHub Repository**

You can also deploy custom-built images from a private DockerHub repository. To know more about this case scenario, navigate to the link below:

[Deploying images on a Private DockerHub ](/resources/stacks/container/deploying_images_on_a_private_dockerhub/)

## Components of Container Stack

```yaml
# Resource Section
name: ${container-stack}
version: v1
type: ${workflow/service}
workflow/service: # Workflow/Service Specific Section
# ...
# ...
# ...
  stack: container # Stack (Here it's Container)
  envs:
  	LOG_LEVEL: ${info} # Log Level
# Container Stack-specific Section
  container:
    image: ${swagger/swagger-ui} # Path of the Docker Image
    command: # Command
      - ${streamlit}
    arguments: # Arguments
      - ${run}
      - ${app.py}
```

### **Resource meta section**

Container Stack can be orchestrated via a [Workflow](/resources/workflow/),[Worker](/resources/worker/), or a [Service](/resources/service/). Workflow, Worker, and Service are [DataOS Resources](/resources/) and are both provisioned as runnable. 

### **Container Stack-specific Section**

**`container`**

All the configuration fields and values for the Container Stack are provided within the Container-specific section.

```yaml
container:
  {} # All the fields and values for the Container stack are specified here
```

**`image`**

The path to the respective Docker Image within the DockerHub repository.

**Type:** string

**Default:** NA

```yaml
image: swagger/swagger-ui # Path of the Docker Image
```

**`command`**

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

**Syntax:**

```yaml
command: 
  - streamlit
```

**`arguments`**

The arguments are the additional arguments apart form the primary command specified within the Dockerfile, as described above.

```yaml
arguments:
  - run
  - app.py
```

## Recipes

[How to deploy a Streamlit App on DataOS?](/resources/stacks/container/build_a_streamlit_app_on_dataos/)

[Container Stack within a Workflow](/resources/stacks/container/container_stack_within_a_workflow/)

[Creating shortcut for Container Stack based applications](/resources/stacks/container/container_stack_based_app_shortcut/)

[Attaching a Volume to a Container Stack](/resources/stacks/container/attach_volume_to_container/)