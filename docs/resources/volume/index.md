---
title: Volume
search:
  boost: 2
---


# :material-storage-tank-outline: Volume

A Volume [Resource](/resources/) in DataOS is a directory accessible to Pod containers, offering persistence and shared storage capabilities. 

Files stored on disk within a container are temporary and do not persist beyond the container's lifecycle, which presents some problems for non-trivial applications when running in containers. This ephemeral nature means that any data written to the container's filesystem will be lost when the container restarts or is deleted. When such an event occurs, the system restarts the container with a clean slate, leading to the loss of all files created or modified during its lifetime. 

Additionally, when multiple containers are running within a Pod and need to share files, setting up and accessing a shared filesystem can be complex and error-prone.

The Volume Resource solves these problems by providing persistent and shared storage solutions for containerized applications, addressing the challenges posed by the ephemeral nature of container storage:

1. **Persistence:**
    - Ensures that data remains available even if the container restarts or is rescheduled.
2. **Shared Storage**:
    - Allows multiple containers in a Pod to access a shared filesystem easily.

## Getting started: Volume

Volume Resource in DataOS can be created by applying the manifest file using the DataOS CLI. To learn more about this process, navigate to the link: [Volume: Get started](/resources/volume/getting_started/)

## Configuration

Volume can be configured to different size, accessMode and type. The specific configurations may vary depending on the use case. For a detailed breakdown of the configuration options and attributes, please refer to the documentation: [Attributes of Volume manifest](/resources/volume/configuration/).