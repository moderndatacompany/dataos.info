# CLI

DataOS CLI is a text-based interface that allows users to interact with the DataOS context via command prompts. It offers a consistent experience across operating systems like MacOS, Linux, and Windows.

CLI provides several capabilities - programmable command completion, passing environment variables while creating or updating the configuration files, managing multiple DataOS contexts from a central location, a Terminal User Interface (TUI), and a host of other features.

The following document encapsulates the installation steps for CLI, initialization steps for the DataOS context, and the shell grammar for first-time users to understand the command structure.

## Installation

Follow the steps enumerated below to install the Command Line Interface. Check the prerequisites before moving forward.

### **Requirements**

 1. Get the following items from our **Customer Success** team:
    - DataOS prime apikey
    - Domain name of the DataOS context/instance
    - Version of the CLI to be installed
 2. Please ensure that the curl utility is installed on your system. To check, use this command:
    ```sh
    curl --version
    ```
    If curl is not installed, follow the steps to [download curl](./cli/read_on_curl_utility.md).

 3. Find out the operating system you are using, and the processor's architecture. The following is a list of supported Arch values:
     

     | Operating System | Processor | Arch |
     | --- | --- | --- |
     | `MacOS` | Intel | darwin-amd64 (works for both intel & amd chips)
     |  | AMD | darwin-amd64 |
     |  | M1 & M2| darwin-arm64 |
     | `Linux` | Intel | linux-386 |
     |  | AMD  | linux-amd64 |
     |  | M1 & M2 (64 bit) | linux-arm64 |
     | `Windows` | 32bit | 386|
     | | 64bit | amd64 (works for both intel & amd chips)|
  
   <aside class="callout">🗣️ Replace <b>{{placeholder}}</b> text in various commands with appropriate values before running the command.</aside>

### **Installation on MacOS**

1. Export the environment variable PRIME_APIKEY to pass it to the subsequent commands(replace **`prime_apikey`**  with the DataOS® API key to connect with the prime context).

    ```sh
    export PRIME_APIKEY="{{prime_apikey}}"

    ```

2. Determine processor architecture with the following command.
    ```
    uname -m
    ```
    Sample output:

    ```
    x86_64
    ```
    You can use this output with the "darwin" prefix as ARCH value in your shell commands to specify the architecture. The available values are `darwin-amd64`, `darwin-arm64` for different types of processors on macOS.

    <aside class="callout">🗣️ Contact the admin (DataOS operator in your organization) to get the correct and latest version of the CLI.</aside>

3. Download the DataOS CLI binary using the below command (replace the **`ARCH`** </span> value of the processor and the **`CLI_VERSION`** </span>to be installed):

    ```shell
    curl --silent --output dataos-ctl-{{ARCH}}.tar.gz --location --request GET "https://prime.tmdata.io/plutus/api/v1/files/download?name=dataos-ctl-{{ARCH}}.tar.gz&dir=cli-apps-{{CLI_VERSION}}&apikey=$PRIME_APIKEY"
    ```
    
    Example:

    A Mac user with intel-chip, installing the 2.8 version of the CLI would input the below command.
    
    ```shell
    curl --silent --output dataos-ctl-darwin-amd64.tar.gz --location --request GET "https://prime.tmdata.io/plutus/api/v1/files/download?name=dataos-ctl-darwin-amd64.tar.gz&dir=cli-apps-2.8&apikey=$PRIME_APIKEY"
    ```

4. *Optional step*: Download the checksum file using the following command (replace the **`ARCH`** value of the processor and the **`CLI_VERSION`** to be installed):

    ```shell
    curl --silent --output dataos-ctl-{{ARCH}}.tar.gz.sha256sum --location --request GET "https://prime.tmdata.io/plutus/api/v1/files/download?name=dataos-ctl-{{ARCH}}.tar.gz.sha256sum&dir=cli-apps-{{CLI_VERSION}}&apikey=$PRIME_APIKEY"
    ```

    Example:

    A Mac user with an intel-chip (identified as  **darwin-amd64** for the processor), installing the **2.8 version of the CLI** would input the below command.

    ```shell
    
    curl --silent --output dataos-ctl-darwin-amd64.tar.gz.sha256sum --location --request GET "https://prime.tmdata.io/plutus/api/v1/files/download?name=dataos-ctl-darwin-amd64.tar.gz.sha256sum&dir=cli-apps-2.8&apikey=$PRIME_APIKEY"
    ```
    

5. *Optional step*: Validate that the zip has not been tampered with.

    ```shell
    shasum -a 256 -c dataos-ctl-{{Arch}}.tar.gz.sha256sum
    ```
    Example:

    ```shell
    shasum -a 256 -c dataos-ctl-darwin-amd64.tar.gz.sha256sum
    ```

    If the zip file has been downloaded as expected, you should get the following output:

    ```shell
    dataos-ctl-darwin-amd64.tar.gz: OK
    ```

6. Extract the dataos-ctl binary.

    ```shell
    tar -xvf dataos-ctl-{{ARCH}}.tar.gz
    ```
    Example:

    ```shell
    tar -xvf dataos-ctl-darwin-amd64.tar.gz
    ```
    Here is the expected output:

    ```shell
    x darwin-amd64/
    x darwin-amd64/dataos-ctl
    ```

7. Run the following command to place the extracted dataos-ctl in a directory that is in your PATH. 

    ```shell
    export PATH=$PATH:$HOME/{{dir-name}}
    ```
    You will get the directory name from the output of the previous command. 
    Example:

    In this case, it is **`darwin-amd64/`**.
    ```
    export PATH=$PATH:$HOME/darwin-amd64/
    ```
    <br>

    > 🗣️  To access DataOS, you have to run this command every time you restart your computer’s terminal or open a new tab in the terminal. To avoid this, you should add the above path to your .zshrc file.
    > 
    > - To add the path to your .zshrc file, you can follow the steps given in this toggle list. Click the toggle icon.
    >     
    >     ```bash
    >     # make sure you are in your home directory "~/ (home/<user>)"
    >     # create a .zshrc file using the command below

    >     touch .zshrc
    >     
    >     # open the file using the command below

    >     ~/.zshrc
    >     
    >     # Copy & paste the path to your .zshrc file

    >     export PATH=$PATH:$HOME/.dataos/bin
    >     
    >     # close the .zshrc file window and load the file in the shell using

    >     source ~/.zshrc
    >     ```
    >     

You have successfully installed the CLI, now the next step is to [initialize](#initialize) the DataOS context. 


   <br>
    <div style="border: 2px dotted #e0e0e0; padding: 15px; border-radius:7px">
     **Debug**
     In case the output was not as expected, then the CLI executable file has not been correctly downloaded & extracted. Input the correct CLI version & ARCH values, and rerun the commands.
     <details><summary>Typical Errors</summary>
     1. Error after running the following command
     ```bash
     iamgroot@abcs-MacBook-Pro-2 ~ % shasum -a 256 -c dataos-ctl-darwin-amd64.tar.gz.sha256sum
     ```
     **Error Message**
     ```bash
     shasum: dataos-ctl-darwin-amd64.tar.gz.sha256sum: no properly formatted SHA checksum lines found
     ```
     2. Error after running the following command
     ```
     iamgroot@abcs-MacBook-Pro-2 ~ % tar -xvf dataos-ctl-darwin-amd64.tar.gz
     ```
     **Error message**
     ```bash
     tar: Error opening archive: Unrecognized archive format
     ```
     These messages indicate that the correct executable file has not been downloaded by the ```curl``` command
     </details>
     </div><br>


### **Installation on Linux**

1. Export the environment variable PRIME_APIKEY to pass it to the subsequent commands.

    ```bash
    export PRIME_APIKEY={{DataOS® prime apikey}}
    ```

2. Determine processor architecture.

    ```bash
    uname -p
    ```

    You will get the following output based on your processor. 

    ```bash
    amd64 
    ```
    
    if the output here appears as x86_64, it also means you have amd64 processor. The available ARCH values are linux-386, linux-amd64, linux-arm, linux-arm64.

    <aside class="callout">🗣️ Contact the admin (DataOS operator in your organization) to get the correct and latest version of the CLI.</aside>
    

3. Download the CLI binary file using the following command (replace the **`ARCH`** & **`CLI_version`** before executing the command).

    ```bash
    curl --silent --output dataos-ctl-linux-{{ARCH}}.tar.gz --location --request GET "https://prime.tmdata.io/plutus/api/v1/files/download?name=dataos-ctl-linux-{{ARCH}}.tar.gz&dir=cli-apps-{{CLI_version}}&apikey=$PRIME_APIKEY"
    
    ```

4. *Optional step*: Update the **`ARCH`** value & **`CLI_version`** in the following command to download the checksum file. 

    ```bash
    curl --silent --output dataos-ctl-linux-{{ARCH}}.tar.gz.sha256sum --location --request GET "https://prime.tmdata.io/plutus/api/v1/files/download?name=dataos-ctl-linux-{{ARCH}}.tar.gz.sha256sum&dir=cli-apps-{{CLI_VERSION}}&apikey=$PRIME_APIKEY"
    ```
    Example: 
    
    For CLI version 2.5 getting installed, the command would be:
    ```bash
    curl --silent --output dataos-ctl-linux-amd64.tar.gz.sha256sum --location --request GET "https://prime.tmdata.io/plutus/api/v1/files/download?name=dataos-ctl-linux-amd64.tar.gz.sha256sum&dir=cli-apps-2.5&apikey=$PRIME_APIKEY"
    ```


5. *Optional step*: Validate that the zip has not been tampered with. Update the **`ARCH`** value in the command.


    ```shell
    
    shasum -a 256 -c dataos-ctl-linux-{{ARCH}}.tar.gz.sha256sum
    ```

    Expected output after running the above command:

    ```bash
    dataos-ctl-linux-{{ARCH}}.tar.gz: OK
    ```

6. Extract the dataos-ctl binary. Update the **`ARCH`** value in the command


    ```shell
    
    tar -xvf dataos-ctl-linux-{{ARCH}}.tar.gz
    ```

    Expected output:

    ```bash
    x linux-{{ARCH}}/
    x linux-{{ARCH}}/dataos-ctl
    ```

7. Run the following command to place the extracted dataos-ctl in a directory that is in your PATH.

    ```shell
    export PATH=$PATH:$HOME/linux-{{ARCH}}
    ```
    
    Example:
    
    ```
    export PATH=$PATH:$HOME/linux-amd64
    ```

    > 🗣️  To access DataOS, you have to run this command every time you restart your computer’s terminal or open a new tab in the terminal. To avoid this, you should add the above path to your .bashrc file.
    > 
    > - To add the path to your .bashrc file, follow the below steps. 
    >     
    >     ```bash
    >     # make sure you are in your home directory "~/ (home/<user>)"
    >     # create a .bashrc file using the command below

    >     touch .bashrc
    >     
    >     # open the file using the command below

    >     xdg-open ~/.bashrc
    >     
    >     # copy & paste the path at the end of your .bashrc file

    >     export PATH=$PATH:$HOME/.dataos/bin
    >     
    >     # save and close the .bashrc file window and load the file in the shell using the command

    >     source ~/.bashrc
    >     ```
    >     

You have successfully installed the CLI, now the next step is to [initialize](#initialize) the DataOS context. 

### **Installation on Windows**

1. Check whether your system has an Intel 64 bit chip or an AMD chip. To find out the architecture, use the following command.
   ```
   wmic cpu get architecture
   ```
   Sample Output:
   ```
   Architecture
   9 # Required Value
   ```
    - If the required value is **0** or **x86,** then it's a 32-bit architecture; in that case, use the **`ARCH`** value as **386**.
    - If the required value is **6, 9,** or **x64**, then it's a 64-bit architecture; in that case, use the **`ARCH`** value as **amd64**.
   
    <aside class="callout">🗣️ Contact the admin (DataOS operator in your organization) to get the correct and latest version of the CLI.</aside>

2. Download the DataOS CLI .tar file using the following link in the browser (replace the **`ARCH`**, **`CLI_VERSION`**, and **`PRIME_APIKEY`** with respective values).
    ```
    https://prime.tmdata.io/plutus/api/v1/files/download?name=dataos-ctl-windows-{{ARCH}}.tar.gz&dir=cli-apps-{{CLI_VERSION}}&apikey={{PRIME_APIKEY}}
    ```
    
    Example:
    To install CLI version 2.8 for a windows machine with amd64 processor and Prime Apikey as abcdefgh12345678987654321, run the following command.

    ```
    https://prime.tmdata.io/plutus/api/v1/files/download?name=dataos-ctl-windows-amd64.tar.gz&dir=cli-apps-2.8&apikey=abcdefgh12345678987654321
    ```

3. *Optional step*: Download the checksum .shasum file using the following link in a browser (replace the **`ARCH`**, **`CLI_VERSION`**, and **`PRIME_APIKEY`** with respective values).
    ```
    https://prime.tmdata.io/plutus/api/v1/files/download?name=dataos-ctl-windows-{{ARCH}}.tar.gz.sha256sum&dir=cli-apps-{{CLI_VERSION}}&apikey={{PRIME_APIKEY}}
    ```
    Example:

    To install CLI version 2.8 for a windows machine with amd64 processor and Prime Apikey as abcdefgh12345678987654321, run the following command.

    ``` 
    https://prime.tmdata.io/plutus/api/v1/files/download?name=dataos-ctl-windows-amd64.tar.gz.sha256sum&dir=cli-apps-2.8&apikey=abcdefgh12345678987654321
    ```
    <aside class="callout">🗣️ Contact the admin(operator in your organization) to get the latest version of the CLI</aside>


4. *Optional step*: Validate that the .tar file has not been tampered with. Replace the **`tar-file-path`** with the path of the downloaded tar file. Also, open the .shasum file in a text editor and copy the hash value and paste it inside quotes in place of **`hash-value-from-shasum-file`**.
    ```
    (Get-FileHash -Algorithm SHA256 -Path {{tar-file-path}}).hash -eq '{{hash-value-from-shasum-file}}'
   
    ```
    Example:

    ```
    (Get-FileHash -Algorithm SHA256 -Path ./Downloads/dataos-ctl-windows-amd64.tar.gz).hash -eq '7d48cb3f60ab4821dd69dddd6291'
    ```

    Sample output:
   
    If the value is True, validation is successful.
   
5. The next step is to unzip the downloaded .tar file. To extract it, you will need an archiver utility like Winrar. 

6. Open Winrar and highlight the zipped .tar file (it should appear with other downloaded files in the lower part of the page), and click the **“Extract to”** button on the top. Place it in your chosen directory. 

   You will always use this directory to run DataOS. To open the DataOS from anywhere in the system, place the extracted file in a directory that is in your PATH. To add the directory in PATH, refer to [Setting the Path and Variables in Windows](cli/windows_path_setting.md).

You have successfully installed the CLI, now the next step is to [initialize](#initialize) the DataOS context. 

## Initialize DataOS Context

To initialize, run the init command.

```bash
dataos-ctl init
```

The initialization process will ask for the following inputs, depending on your user role:

```bash
dataos-ctl init

INFO[0000] The DataOS® is already initialized, do you want to add a new context? (Y,n)  
->Y   #input the answer: Y or n
INFO[0255] 🚀 initialization...
                        
INFO[0255] The DataOS® is not initialized, do you want to proceed with initialization? (Y,n)  
->Y

INFO[0269] Please enter a name for the current DataOS® Context?  
->{{name of the DataOS context}}
#for example 'kutumbakam'. You can write the name of your choice.
#your enterprise can have multiple contexts available for you to connect. Choose any one.
#you can always change the context through a CLI command, after login. 

INFO[0383] Please enter the fully qualified domain name of the DataOS® instance?  
->{{domain name}} 
#for example 'vasudhaiva-kutumbakam.dataos.app'
INFO[0408] entered DataOS®: kutumbakam : vasudhaiva-kutumbakam.dataos.app 

INFO[0408] Are you operating the DataOS®? (Y,n)         
->n  
#if you are the operator(admin) for your enterprise, type Y
#the installation steps, if you type Y, will change.
INFO[0452] 🚀 initialization...complete
```

<aside class="callout">🗣️ If you are your enterprise's operator/admin, then the installation steps for you will change after the last step. These are covered in the Operator Document for DataOS.</aside>

## Log in

After the successful initialization of DataOS context, you can log in to your account with the following command. 

```shell
dataos-ctl login
```

If your enterprise has multiple DataOS contexts, you can use the same command-line interface (CLI) that you just installed to access and use any of those contexts. You can switch between different DataOS contexts using a specific command with the CLI.

## Test CLI Installation

Run the following commands to ensure the successful installation of DataOS CLI. These commands will show the version and health status of the installed DataOS CLI.

```shell
dataos-ctl version
dataos-ctl health
```

## Update CLI

To update the CLI to a different version, just redo the steps mentioned earlier. However, make sure to modify the CLI version within these commands to match the specific version you intend to install.

## Command Reference

This section will help you get started on the command structure followed by DataOS CLI.

### **Structure of the DataOS CLI Command**

```bash
dataos-ctl <command> <subcommand> <flags parameters>
```
### **DataOS CLI Commands**

You can generate a list of all available commands with -h or —help
```bash
dataos-ctl -h
dataos-ctl --help
```
To get help for a specific command, use:
```bashdataos-ctl <name of command> --help
```


A command can have more sub-commands and flags under it. You can again use the CLI help command to get details on the subcommand.

```bash
dataos-ctl <command-name> <subcommand-name> -h
```

A subcommand, in turn, might have more commands in its hierarchy or might only contain flags.

In the example below, we have used the `get` command, followed by the flag -t. This flag must be followed by the name of the ‘type string’ (workflow, policy, depot, etc). The command below will give us the details of all the created depots (remove -a to list only the depots where you are the owner).


```bash
dataos-ctl get -t depot -a 

```

The string type ‘workflow’, being a runnable Resource of DataOS, must always be followed by the flag `-w <name of the workspace>`. The following command will list all the workflows running in the public workspace (remove -a to list only the workflows you are working on).

```bash
dataos-ctl get -t workflow -w public -a

```

Other DataOS Resources for which a workspace must always be defined are Secret, Service, Cluster, and Database (these are classified as **Workspace-level Resources**).

For Resources such as Depot, Policy, and Compute, Workspace has no meaning (these are classified as **Cluster-level Resources**). Hence you need not use the flag `-w <name of workspace>`.

**Workspace** is like a tenant in DataOS. It provides a way to segregate your private work from the rest of the organization’s. Workspaces also serve as a sandbox environment where you can freely explore and experiment with data without impacting the production environment. This functionality enables you to test and refine your projects before deploying them to the public workspace or making them available for broader usage.

<aside class="best-practice">
📖 Best Practice: It is part of the best practice to create a private workspace with your name and then work in it.

</aside>

To learn more, refer to [CLI Command Reference](cli/command_reference.md). The reference also contains the help content for all DataOS CLI commands.


## Linked Documents

- [Read on Curl utility](cli/read_on_curl_utility.md)

- [Setting the Path and Variables in Windows](cli/windows_path_setting.md)
