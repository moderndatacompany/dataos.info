# CLI

DataOS CLI is a text-based interface that allows users to interact with the DataOS context via command prompts. It offers a consistent experience across different operating systems, such as MacOS, Linux, and Windows.

CLI provides several capabilities - progammable command completion, passing environment variables while creating or updating the configuration files, managing multiple DataOS contexts from a central location, a Terminal User Interface(TUI), and a host of other features.

The following document, encapsulates the installation steps for CLI, initialization steps for the DataOS context, and the shell grammar for the first-time users to understand the command structure.

## Installation

Follow the steps enumerated below to install the Command Line Interface. Check the pre-requisites before moving forward.

**Requirements**

 1. Please ensure that the curl utility is installed on your system. To check, use this command:
    ```sh
    curl --version
    ```
    If curl is not installed, follow the steps to [download curl](./cli/read_on_curl_utility.md).

 2. Get the following items from our Customer Success team:
    - DataOS prime apikey
    - The domain name of the DataOS context/instance
    - Version of the CLI to be installed
 3. Find out the operating system you are using, and the architecture of the processor. This is the list of possible Arch values which are supported:
     

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
  
### **Installation on MacOS**

1. Export the environment variable PRIME_APIKEY to pass it to the next commands( replace <span style="color:red"> {{DataOS® prime apikey}} </span> with the API key to connect with the prime context).

    ```sh
    export PRIME_APIKEY="{{DataOS® prime apikey}}"

    ```

2. Download the checksum file using the following command (replace the <span style="color:red">{{ARCH}}</span> value of the processor and the <span style="color:red">{{CLI_VERSION}}</span> to be installed):

    ```html
    curl --silent --output dataos-ctl-{{ARCH}}.tar.gz.sha256sum --location --request GET "https://prime.tmdata.io/plutus/api/v1/files/download?name=dataos-ctl-{{ARCH}}.tar.gz.sha256sum&dir=cli-apps-{{CLI_VERSION}}&apikey=$PRIME_APIKEY"

    # For example, a mac user with intel-chip, installing the 2.8 version of the CLI will input the below command
    
    #curl --silent --output dataos-ctl-darwin-amd64.tar.gz.sha256sum --location --request GET "https://prime.tmdata.io/plutus/api/v1/files/download?name=dataos-ctl-darwin-amd64.tar.gz.sha256sum&dir=cli-apps-2.8&apikey=$PRIME_APIKEY"

    # 2.8 is the CLI version getting installed
    # darwin-amd64 is the processor
    # Contact the admin(DataOS operator in your organisation) to get the correct version of the CLI
    ```

3. Download the DataOS CLI binary using the below command (replace the <span style="color:red"> {{ARCH}} </span> value of the processor and the <span style="color:red"> {{CLI_VERSION}} </span>to be installed):

    ```jsx

    curl --silent --output dataos-ctl-{{ARCH}}tar.gz --location --request GET "https://prime.tmdata.io/plutus/api/v1/files/download?name=dataos-ctl-{{ARCH}}.tar.gz&dir=cli-apps-{{CLI_VERSION}}&apikey=$PRIME_APIKEY"

    # For example, a mac user with intel-chip, installing the 2.8 version of the CLI will input the below command
    
    #curl --silent --output dataos-ctl-darwin-amd64.tar.gz --location --request GET "https://prime.tmdata.io/plutus/api/v1/files/download?name=dataos-ctl-darwin-amd64.tar.gz&dir=cli-apps-2.8&apikey=$PRIME_APIKEY"

    # Contact the admin(DataOS operator in your organisation) to get the latest version of the CLI
    ```

4. Validate that the zip has not been tampered with (*this is an optional step*).

    ```jsx
    shasum -a 256 -c dataos-ctl-{{Arch}}.tar.gz.sha256sum
    
    # example:
    #shasum -a 256 -c dataos-ctl-darwin-amd64.tar.gz.sha256sum
    ```

    If the zip file has been downloaded as expected, you should get the following output:

    ```
    dataos-ctl-darwin-amd64.tar.gz: OK
    ```

5. Extract the dataos-ctl binary.

    ```jsx
    tar -xvf dataos-ctl-{{ARCH}}.tar.gz

    #example: tar -xvf dataos-ctl-darwin-amd64.tar.gz
    ```

    This is the expeced output:

    ```
    x darwin-amd64/
    x darwin-amd64/dataos-ctl
    ```

6. Run the following command to place the extracted dataos-ctl in a directory that is in your PATH. 

    ```jsx
    export PATH=$PATH:$HOME/{{dir-name}}
    # You will get the directory name from the output of the previous command
    # In the above case, it is darwin-amd64/
    # For example, export PATH=$PATH:$HOME/darwin-amd64/
    ```
<br>



    > 🗣️  To access DataOS, you have to run this command every time you restart your computer’s terminal or open a new tab in the terminal. If you are too lazy to do that, you should add the above path in your .zshrc file
    > 
    > - To add the path to you .zshrc file, you can follow the steps given in this toggle list. Click the toggle icon.
    >     
    >     ```bash
    >     #make sure you are in your home directory "~/ (home/<user>)"
    >     #create .zshrc file using the command below
    >     touch .zshrc
    >     
    >     #open the file using the command below
    >     ~/.zshrc
    >     
    >     #simply copy & paste the path to your .zshrc file
    >     export PATH=$PATH:$HOME/.dataos/bin
    >     
    >     #close the .zshrc file window and load the file in the shell using
    >     source ~/.zshrc
    >     ```
    >     

You have successfully installed the CLI, now the next step is to [initialize](#initialize) it. 


   <br>
    <div style="border: 2px dotted #e0e0e0; padding: 15px; border-radius:7px">
     **Debug**
     In case the output was not as expected, then the CLI executable file has not been correctly downloaded & extracted. Input the correct version of the CLI & ARCH values, and rerun the commands.
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
    #sample example
    #if the output here comes as x86_64, it also means you have amd64 processor
    ```

3. Update the <span style="color:red">{{ARCH}}</span> value & <span style="color:red">{{CLI_version}}</span> in the following command to download the checksum file. The available ARCH values are 386, amd64, arm, arm64.

    ```bash
    curl --silent --output dataos-ctl-linux-{{ARCH}}.tar.gz.sha256sum --location --request GET "https://prime.tmdata.io/plutus/api/v1/files/download?name=dataos-ctl-linux-{{ARCH}}.tar.gz.sha256sum&dir=cli-apps-{{CLI_VERSION}}&apikey=$PRIME_APIKEY"

    #2.5 is the CLI version getting installed
    #Contact the admin(operator in your organisation) to get the latest version
    #example: curl --silent --output dataos-ctl-linux-amd64.tar.gz.sha256sum --location --request GET "https://prime.tmdata.io/plutus/api/v1/files/download?name=dataos-ctl-linux-amd64.tar.gz.sha256sum&dir=cli-apps-2.5&apikey=$PRIME_APIKEY"
    ```

4. Download the CLI binary file using the following command.

    ```bash
    curl --silent --output dataos-ctl-linux-{{ARCH}}.tar.gz --location --request GET "https://prime.tmdata.io/plutus/api/v1/files/download?name=dataos-ctl-linux-{{ARCH}}.tar.gz&dir=cli-apps-{{CLI_version}}&apikey=$PRIME_APIKEY"
    #replace the {{ARCH}} & {{CLI_version}} before executing the command.
    ```

5. Validate that the zip has not been tampered (optional step).

    ```jsx
    #update the {{ARCH}} value in the command

    shasum -a 256 -c dataos-ctl-linux-{{ARCH}}.tar.gz.sha256sum
    ```

    Expected output after running the above command:

    ```bash
    dataos-ctl-linux-{{ARCH}}.tar.gz: OK
    ```

6. Extract the dataos-ctl binary.

    ```jsx
    #update the {{ARCH}} value in the command

    tar -xvf dataos-ctl-linux-{{ARCH}}.tar.gz
    ```

    Expected output:

    ```bash
    x linux-{{ARCH}}/
    x linux-{{ARCH}}/dataos-ctl
    ```

7. Run the following command to place the extracted dataos-ctl in a directory that is in your PATH.

    ```jsx
    export PATH=$PATH:$HOME/linux-{{ARCH}}
    # Update the {{ARCH}} value in the command
    # Example: export PATH=$PATH:$HOME/linux-amd64
    ```

    > 🗣️  To access DataOS, you have to run this command every time you restart your computer’s terminal or open a new tab in the terminal. To avoid this, you should add the above path in your .bashrc file
    > 
    > - To add the path to you .bashrc file, follow the below steps. 
    >     
    >     ```bash
    >     #make sure you are in your home directory "~/ (home/<user>)"
    >     #create .bashrc file using the command below
    >     touch .bashrc
    >     
    >     #open the file using the command below
    >     xdg-open ~/.bashrc
    >     
    >     #simply copy & paste the path at the end of your .bashrc file
    >     export PATH=$PATH:$HOME/.dataos/bin
    >     
    >     #save and close the .bashrc file window and load the file in the shell using the command
    >     source ~/.bashrc
    >     ```
    >     

You have successfully installed the CLI, now the next step is to [initialize](#initialize) it. 

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
    - If the required value is **0** or **x86,** then it's a 32-bit architecture; in that case, use the **{{ARCH}}** value as **386**.
    - If the required value is **6, 9,** or **x64**, then it's a 64-bit architecture; in that case, use the **{{ARCH}}** value as **amd64**.
2. Download the checksum .shasum file using the following link in a browser. Replace the <span style="color:red">{{ARCH}}</span>, <span style="color:red">{{CLI_VERSION}}</span>, and <span style="color:red">{{PRIME_APIKEY}}</span> with respective values.
   ```
   https://prime.tmdata.io/plutus/api/v1/files/download?name=dataos-ctl-windows-{{ARCH}}.tar.gz.sha256sum&dir=cli-apps-{{CLI_VERSION}}&apikey={{PRIME_APIKEY}}
   # Replace the {{ARCH}}, {{CLI_version}}, and {{PRIME_APIKEY}} in the link
   # Suppose, amd64 is the processor
   # 2.8 is the CLI version getting installed
   # Prime Apikey is abcdefgh12345678987654321
   # Contact the admin(operator in your organisation) to get the latest version of the CLI
   # Example: https://prime.tmdata.io/plutus/api/v1/files/download?name=dataos-ctl-windows-amd64.tar.gz.sha256sum&dir=cli-apps-2.8&apikey=abcdefgh12345678987654321
   ```
3. Download the DataOS CLI .tar file using the following link in the browser (replace the <span style="color:red">{{ARCH}}</span>, <span style="color:red">{{CLI_VERSION}}</span>, and <span style="color:red">{{PRIME_APIKEY}}</span> with respective values).
   ```
   https://prime.tmdata.io/plutus/api/v1/files/download?name=dataos-ctl-windows-amd64.tar.gz&dir=cli-apps-{{CLI_VERSION}}&apikey={{PRIME_APIKEY}}

   # Replace the {{ARCH}}, {{CLI_version}}, and {{PRIME_APIKEY}} before executing the command
   # Example: https://prime.tmdata.io/plutus/api/v1/files/download?name=dataos-ctl-windows-amd64.tar.gz&dir=cli-apps-2.8&apikey=abcdefgh12345678987654321
   ```  
4. Validate that the .tar file has not been tampered with(optional step).
   ```
   (Get-FileHash -Algorithm SHA256 -Path {{tar-file-path}}).hash -eq '{{hash-value-from-shasum-file}}'
   # Replace the {{tar-file-path}} with the path of the downloaded tar file
   # Open the .shasum file in a text editor and copy the hash value and paste it inside quotes in place of {{hash-value-from-shasum-file}}
   # Example: (Get-FileHash -Algorithm SHA256 -Path ./Downloads/dataos-ctl-windows-amd64.tar.gz).hash -eq '7d48cb3f60ab4821dd69dddd6291'
   # If the value is True, validation is successful
   ```
5. The next step is to unzip the downloaded .tar file, to extract it, you will need an archiver utility like Winrar. 

6. Open Winrar and highlight the zipped .tar file (it should appear with other downloaded files in the lower part of the page), and click the **“Extract to”** button on the top. Place it in your chosen directory.
Download the CLI binary by typing the given links in your web browser (according to the chip type AMD/Intel 64bit).

   <aside>🗣️ You will always use this directory to run DataOS. To open the DataOS from anywhere in the system, place the extracted file in a directory that is in your PATH. To add the directory in PATH, refer to [Setting the Path and Variables in Windows](cli/windows_path_setting.md).</aside>

You have successfully installed the CLI, now the next step is to [initialize](#initialize) it. 

## Initialize

To initialize, run the init command.

```bash
dataos-ctl init
```

The initialization process will ask for the following inputs, depending upon your user role:

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

<aside>If you are the operator/admin for your enterprise then the installation steps for you, after the last step, will change. These are covered in the Operator Document for DataOS.</aside>

## Log in

After the successful initialization of DataOS context, you can log into your account with the following command. 

```jsx
dataos-ctl login
```

If your enterprise has multiple DataOS contexts, you can use the same command-line interface (CLI) that you just installed to access and use any of those contexts. With the CLI, you can switch between different DataOS contexts using a specific command.

## Test

Run the following commands to ensure the successful installation of DataOS CLI. These commands will show the version and health status of the installed DataOS CLI.

```jsx
dataos-ctl version
dataos-ctl health
```

## Update

In order to update the CLI to a different version, simply rerun all the commands enumerated above. Remember to change the CLI version in the commands to the version you want to install.

## Command Reference

This section will help you get started on the command structure followed by DataOS CLI

### **Structure of the DataOS CLI Command**

```bash
dataos-ctl <command> <subcommand> <flags parameters>
```
### **DataOS CLI Commands**

<aside>
🗣️ You can generate a list of all available commands with -h or —help
`dataos-ctl -h`, or you can also use
`dataos-ctl --help`
To get help for a specific command, use:
`dataos-ctl <name of command> --help`

</aside>

A command can have more sub-commands and flags under it. To get details on the subcommand, you can again use the CLI help command.

```bash
dataos-ctl <command-name> <subcommand-name> -h
```

A subcommand, in turn, might have more commands in its hierarchy or might only contain flags.

In the example below, we have used the `get` command, followed by the flag -t. This flag must be followed by the name of the ‘type string’ (workflow, policy, depot, etc). 

```bash
dataos-ctl get -t depot -a 
# This will give us the details of all the created depots
# If you don't use -a, it will list only the depots where you are the owner
```

The string type ‘workflow’, being a runnable Resource of DataOS, must always be followed by the flag `-w <name of the workspace>`

```bash
dataos-ctl get -t workflow -w public -a
# This command will list all the workflows running in the public workspace
# If you don't use the flag -a, it will list only the workflows you are working on
```

Other DataOS Resources for which a workspace must always be defined are Secret, Service, Cluster, and Database (these are classified as **Workspace-level Resources**).

For Resources such as Depot, Policy, and Compute, Workspace has no meaning (these are classified as **Cluster-level Resources**). Hence you need not use the flag `-w <name of workspace>`.

**Workspace** is like a tenant in DataOS. It provides a way to segregate your private work from the rest of the organization’s. Workspaces also serve as a sandbox environment where you can freely explore and experiment with data without impacting the production environment. This enables you to test and refine your projects before deploying them to the public workspace or making them available for broader usage.

<aside>
📖 Best Practice: It is part of the best practice to create a private workspace with your name and then work in it.

</aside>

To learn more, refer to [CLI Command Reference](cli/command_reference.md). The reference also contains the help content for all DataOS CLI commands.


## Linked Documents

- [Read on Curl utility](cli/read_on_curl_utility.md)

- [Setting the Path and Variables in Windows](cli/windows_path_setting.md)