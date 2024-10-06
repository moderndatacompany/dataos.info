Before setting up Lens on your local system, ensure you meet the following requirements.

| **Dependency** | **Purpose** |
| --- | --- |
| **Docker** | Runs Lens in an isolated environment on your local system. |
| **Docker Compose** | Configures and manages multi-container Docker applications for Lens. |
| **Postman App/Postman VSCode Extension** | Queries and tests Lens to ensure your setup functions correctly. |
| **VS Code** | Builds and manages Lens Model YAMLs as a code editor. |
| **VS Code Plugin (Optional)** | Enhances development experience by aiding in creating Lens views and tables. |

### **Docker**

Docker is required to run Lens in an isolated environment on a local system. This guide provides instructions for installing Docker if it is not already installed. If Docker is already installed, you can jump to the [next step](/resources/lens/installing_prerequisites/#visual-studio-code) in the setup process.

**Checking for Existing Installation**

Before proceeding with the installation, verify whether Docker is already installed on the system by running the following command in the terminal or command prompt:

```bash
docker --version
```

If Docker is installed, a version number similar to the following will be displayed:

```bash
Docker version 20.10.7, build f0df350
```

If Docker is not installed, follow the appropriate installation guide for particular operating system:

- **Linux:** Follow the installation guide for the Docker engine for Linux here: [Install Docker on Linux](https://docs.docker.com/desktop/install/linux-install/). It is recommended that you install the Docker Desktop version.
- **Windows:** Follow the installation guide of the Docker engine for Windows here: [Install Docker on Windows](https://docs.docker.com/desktop/install/windows-install/).
- **macOS:** Follow the installation guide of the Docker engine for Linux here: [Install Docker on macOS](https://docs.docker.com/desktop/install/mac-install/).

**Docker Login**

Before pulling or pushing images from or to a private repository, it is necessary to log in to Docker Hub using the command line. The docker login command can be used to authenticate with Docker Hub by providing the Docker Hub username and password.

=== "Syntax"     

    ```bash
    docker login --username=${DOCKERHUB_USERNAME}
    ```


=== "Example"

    ```bash
    docker login --username=lensuser01
    ```
After executing the command, replacing ${DOCKERHUB_USERNAME} with the actual Docker Hub username, the system will prompt for the Docker account password.

```bash
docker login --lensuser01
Password:
 
#expected_output

WARNING! Your password will be stored unencrypted in /home/tomandjerry/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded
```

<aside class="callout">
💡 To obtain the username and password required to pull the Lens image, contact the DataOS Administrator or Operator within your organization.
</aside>


**Pull the Image**

To pull a Docker image from a registry, use the docker pull command. If no tag is specified, Docker will automatically pull the latest version of the image. This command is required to fetch images from public or private registries.

=== "Syntax"

    ```bash
    docker pull [REGISTRY_HOST/]USERNAME/IMAGE[:TAG]
    ```

=== "Example"

    ```bash
    docker pull lensuser01/lens2:0.35.55-01    
    ```

<aside class=callout>
💡  Tags are used to identify specific versions of an image and can be updated over time. Ensure the latest image tag or the tag specified in the docker-compose YAML is pulled.
</aside>

**Docker Compose**

Lens utilizes Docker Compose to configure multi-container Docker applications through a YAML manifest file. This guide outlines the process for checking an existing Docker Compose installation, installing it if needed, and validating the installation.

**Checking for Existing Installation**

Before installing Docker Compose, it is advisable to check if it is already installed on the system.
    
```bash
docker-compose --version
```
This command will return the installed version of Docker Compose, if present. For example:

``` bash
docker-compose version 1.29.2, build 5becea4c
```
    
**Installing Docker Compose**

If Docker Compose is not installed, refer to the following link to [install Docker Compose](https://docs.docker.com/compose/install/).

### **Visual Studio Code**

Lens includes a Visual Studio Code extension that enhances the efficiency and precision of crafting Lens YAML configurations. To use this extension, Visual Studio Code (VS Code) must be installed on the local system. The following instructions and links provide guidance for installing VS Code on various operating systems.

**Installation Links by Operating System**

- **Linux**: Follow the detailed steps to install VS Code on your Linux system by accessing the [Install VS Code on Linux guide](https://code.visualstudio.com/docs/setup/linux).

- **Windows**: To install VS Code on a Windows machine, refer to the [Install VS Code on Windows guide](https://code.visualstudio.com/docs/setup/windows).

- **MacOS**: For MacOS users, installation instructions can be found in the [Install VS Code on macOS guide](https://code.visualstudio.com/docs/setup/mac).


<!-- ### **Lens2 VS Code Extension**

After installing VS Code, the development environment can be enhanced by installing the Lens VS Code extension:

1. Open Visual Studio Code on the computer.

2. Click on the Extensions view icon in the Sidebar or press **Ctrl+Shift+X**.

3. In the Extensions view, type **lens2** into the search field and press **Enter** and Click **Install**.

<center>
  <div style="text-align: center;">
    <img src="/resources/lens/installing_prerequisites/lens_extension.png" alt="lens_example" style="width: 40%; border: 1px solid black; height: auto">
    <figcaption>lens2 VS Code Extension</figcaption>
  </div>
</center>

**Note:** The dataos-lens2 extension depends on the **Red Hat YAML extension**. Ensure that it is also installed, using a similar procedure.

<center>
  <div style="text-align: center;">
    <img src="/resources/lens/installing_prerequisites/redhat_extension.png" alt="lens_example" style="width: 40%; border: 1px solid black; height: auto">
    <figcaption>Red Hat YAML Extension</figcaption>
  </div>
</center>

Type the following commands to quickly generate Lens2 tables, views, dimensions, measures, joins, preaggregations and segments:

- lens2_tables
- lens2_views
- lens2_measure
- lens2_dimension

<center>
  <div style="text-align: center;">
    <img src="/resources/lens/installing_prerequisites/lens2extension.gif" alt="lens_example" style="width: 60%; border: 1px solid black; height: auto">
    <figcaption>typing lens2_tables and click enter to getYAML Template .</figcaption>
  </div>
</center> -->

### **Python**

Lens utilizes the Python programming language for tasks such as setting up directory structures and creating virtual environments for managing workloads and dependencies. To begin using Lens, Python must be installed on the system.

**Checking for Existing Installation**

```bash
python3 --version
#Expected_Output
Python 3.8.14
```

- The expected output should be **`Python 3.X`** or another version that is greater than 3.7.  If the existing version is not greater than 3.7, update Python to a newer version.

**Installing Python** 

If Python is not already installed on the system, follow the steps below to download and install the appropriate version.

1. **Access the Installation Guide**: Visit the [Python Installation Guide](https://realpython.com/installing-python/#how-to-install-python-on-windows). This guide provides detailed instructions for installing Python on various operating systems, including Windows, macOS, and Linux.

2. **Download Python**: From the guide, select the link corresponding to the operating system and download the latest version of Python.
          
  <aside class="callout">
  🗣️ Ensure that the version is 3.7 or higher to meet Lens requirements.
  </aside>
        
3. **Install Python**: Run the downloaded installer. Be sure to check the box that says "Add Python 3.x to PATH" before clicking "Install Now". This step is crucial as it makes Python accessible from the command line.

4. **Verify Installation**: After installation, open a command line interface and run the following  command to check the installed version of Python:
          
    ```bash
    python3 -V
    ```
   - The expected output should be **`Python 3.X`** or another version that is greater than 3.7.

5. **Update Python**: If installed version of Python is older than 3.7, follow the guide on [Updating Python](https://ioflood.com/blog/update-python-step-by-step-guide/) to upgrade to a newer version that meets the Lens prerequisites.
    
### **Postman**

Postman is a tool that allows data developers to perform querying and testing within the Lens environment by sending API requests through an intuitive user interface. Follow the [Postman Installation Guide](https://learning.postman.com/docs/getting-started/installation/installation-and-updates/) to install Postman on your local system.


**Install Postman VS Code Extension**:

Alternatively, you can also install Postman Extension on your Code Editor.

- Search for **Postman** in the VS Code Extensions Marketplace and install the Postman extension.

- Open the extension within VS Code to start creating and sending requests directly from the editor.
    
<div style="text-align: center;">
    <img src="/resources/lens/installing_prerequisites/postman_extension.png" alt="Postman Extension" style="max-width: 40%; height: auto; border: 1px solid #000;">
</div>

- Once installed, you can access the Postman extension by clicking on the Postman icon in the Activity Bar on the side of VS Code.

With all prerequisites including Docker, VS Code, Python, and Postman installed, you are now ready to build Lens models on your system. 


## Next Steps

[Lens Model Folder Setup](/resources/lens/lens_model_folder_setup/)
