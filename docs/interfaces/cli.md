# CLI

<!DataOS is controlled at the command-line by standardized YAML directives using a configurable set of Resources. This allows fine-grained control of every function, workload and data products.>
DataOS CLI is a text-based interface that allows users to interact with the DataOS context via command prompts. It is agnostic of the operating system or processor of the local machines, that is to say that it works in the same manner irrespective of whether you are on MacOS, Linux or Windows.

CLI provides several capabilities - progammable command completion, passing environment variables while creating or updating the configuration files, managing multiple DataOS contexts from a central location, a Terminal User Interface, and a host of other features.

The following document, encapsulates the installation steps for CLI, initialization steps for the DataOS context, and the shell grammar for the first-time users to understand the command structure.

## Installation

Follow the steps enumerated below to install the Command Line Interface. Check the pre-requisites before moving forward.

**Requirements**

 1. Please ensure that the curl utility is installed on your system. To check, use this command:

        curl --version

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

1. Export the environment variable PRIME_APIKEY to pass it to the next commands.

    ```sh
    export PRIME_APIKEY="{{DataOS® prime apikey}}"

    #{{DataOS® prime apikey}} should be replaced by the API key to connect with the prime context
    ```

2. Download the checksum file using the following command (replace the <span style="color:red">{{ARCH}}</span> value of the processor and the <span style="color:red">{{CLI_VERSION}}</span> to be installed):

    ```html
    curl --silent --output dataos-ctl-{{<span style="color:red">ARCH</span>}}.tar.gz.sha256sum --location --request GET "https://prime.tmdata.io/plutus/api/v1/files/download?name=dataos-ctl-{{ARCH}}.tar.gz.sha256sum&dir=cli-apps-{{CLI_VERSION}}&apikey=$PRIME_APIKEY"

    # For example, a mac user with intel-chip, installing the 2.8 version of the CLI will input the below command
    
    #curl --silent --output dataos-ctl-darwin-amd64.tar.gz.sha256sum --location --request GET "https://prime.tmdata.io/plutus/api/v1/files/download?name=dataos-ctl-darwin-amd64.tar.gz.sha256sum&dir=cli-apps-2.8&apikey=$PRIME_APIKEY"

    # 2.8 is the CLI version getting installed
    # darwin-amd64 is the processor
    # Contact the admin(DataOS operator in your organisation) to get the correct version of the CLI
    ```

3. Download the DataOS CLI binary using the below command (replace the {{ARCH}} value of the processor and the {{CLI_VERSION}} to be installed):

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
6. Run the following command 


    ```jsx
    export PATH=$PATH:$HOME/.dataos/bin
    ```
<br>



    > 📌  To access DataOS, you have to run this command every time you restart your computer’s terminal or open a new tab in the terminal. If you are too lazy to do that, you should add the above path in your .zshrc file
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

Yay! You have successfully installed the CLI, now let’s initialize. 

   <br>
    <div style="border: 2px dotted #e0e0e0; padding: 15px; border-radius:7px">
     *Debug*
     In case the output was not as expected, then the CLI executable file has not been correctly downloaded & extracted. Input the correct version of the CLI & Arch values, and rerun the commands.

     > For example, one can get an error message after running the following command
     >```
     > iamgroot@abcs-MacBook-Pro-2 ~ % shasum -a 256 -c dataos-ctl-darwin-amd64.tar.gz.sha256sum
     > ```
     > Error Message
     > ```
     > shasum: dataos-ctl-darwin-amd64.tar.gz.sha256sum: no properly formatted SHA checksum lines found
     > ```
     > Or an error message after running the following command
     > ```
     > iamgroot@abcs-MacBook-Pro-2 ~ % tar -xvf dataos-ctl-darwin-amd64.tar.gz
     > ```
     > Error message
     > ```
     > tar: Error opening archive: Unrecognized archive format
     > ```
     > These messages indicate that the correct executable file has not been downloaded by the ```curl``` command
     </div>
<br>


### Linux

1. Export the environment variable PRIME_APIKEY to pass it to the subsequent commands.

    ```bash
    export PRIME_APIKEY=<DataOS® prime apikey>
    ```

1. Determine processor architecture.

    ```bash
    uname -p
    ```

    You will get the following output based on your processor.

    ```bash
    amd64 
    #sample example
    #if the output here comes as x86_64, it also means you have amd64 processor
    ```

1. Update the <ARCH> value & <CLI_version> in the following command to download the checksum file. The available ARCH values are 386, amd64, arm, arm64.

    ```bash
    curl --silent --output dataos-ctl-linux-<ARCH>.tar.gz.sha256sum --location --request GET "https://prime.tmdata.io/plutus/api/v1/files/download?name=dataos-ctl-linux-<ARCH>.tar.gz.sha256sum&dir=cli-apps-<CLI_VERSION>&apikey=$PRIME_APIKEY"

    #2.5 is the CLI version getting installed
    #Contact the admin(operator in your organisation) to get the latest version
    #example: curl --silent --output dataos-ctl-linux-amd64.tar.gz.sha256sum --location --request GET "https://prime.tmdata.io/plutus/api/v1/files/download?name=dataos-ctl-linux-amd64.tar.gz.sha256sum&dir=cli-apps-2.5&apikey=$PRIME_APIKEY"
    ```

1. Download the CLI binary file using the following command

    ```bash
    curl --silent --output dataos-ctl-linux-<ARCH>.tar.gz --location --request GET "https://prime.tmdata.io/plutus/api/v1/files/download?name=dataos-ctl-linux-<ARCH>.tar.gz&dir=cli-apps-<CLI_version>&apikey=$PRIME_APIKEY"
    #replace the <ARCH> & <CLI_version> before executing the command
    ```

1. Validate that the zip has not been tampered (optional step).

    ```jsx
    #update the <ARCH> value in the command

    shasum -a 256 -c dataos-ctl-linux-<ARCH>.tar.gz.sha256sum
    ```

    Expected output after running the above command:

    ```bash
    dataos-ctl-linux-<ARCH>.tar.gz: OK
    ```

6. Extract the dataos-ctl binary.

    ```jsx
    #update the <ARCH> value in the command

    tar -xvf dataos-ctl-linux-<ARCH>.tar.gz
    ```

    Expected output:

    ```bash
    x linux-<ARCH>/
    x linux-<ARCH>/dataos-ctl
    ```

    > 🗣️ Place the extracted dataos-ctl in a directory that is in your PATH. In Linux, you can achieve this using the following command:

    ```jsx
    export PATH=$PATH:$HOME/.dataos/bin
    ```

    > 📌  To access DataOS, you have to run this command every time you restart your computer’s terminal or open a new tab in the terminal. If you are too lazy to do that, you should add the above path in your .bashrc file
    > 
    > - To add the path to you .bashrc file, you can follow the steps given in this toggle list. Click the toggle icon.
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

Yay! You have successfully installed the CLI, now let’s initialize. 

### Windows

1. Check whether your system has an Intel 64bit chip or an AMD chip.
2. Download the CLI binary by typing the given links in your web browser (according to the chip type AMD/Intel 64bit)
    - For intel 64bit chip, follow these steps:
    1. The below link will help you download the shasum file. In the link given below, 386 is the OS Architecture(processor) of your system and 2.4 is the CLI version.
        
        https://prime.tmdata.io/plutus/api/v1/files/download?name=dataos-ctl-windows-386.tar.gz.sha256sum&dir=cli-apps-2.4&apikey=$PRIME_APIKEY
    
    1. The below link will help you download .tar file.
        
        https://prime.tmdata.io/plutus/api/v1/files/download?name=dataos-ctl-windows-386.tar.gz&dir=cli-apps-2.4&apikey=$PRIME_APIKEY
    
    
    - For AMD chip, follow these steps:
    1. The below link will help you download shasum file. In the link given below, amd64 is the OS Architecture(processor) of your system and 2.4 is the CLI version
        
        https://prime.tmdata.io/plutus/api/v1/files/download?name=dataos-ctl-windows-amd64.tar.gz.sha256sum&dir=cli-apps-2.4&apikey=$PRIME_APIKEY
        
    1. The below link will help you download .tar file.
        
        https://prime.tmdata.io/plutus/api/v1/files/download?name=dataos-ctl-windows-amd64.tar.gz&dir=cli-apps-2.4&apikey=$PRIME_APIKEY
        
    
3. The next step is to unzip the downloaded .tar file, to extract it, you will need an archiver utility like Winrar. 
2. Open Winrar and highlight the zipped tar file (it should appear with other downloaded files in the lower part of the page), and click the “Extract to” button on the top. Place it in your chosen directory. 

> 🗣️ You will always use this directory to run DataOS. To open the DataOS from anywhere in the system, place the extracted file in a directory that is in your PATH. To add the directory in PATH, refer to [Setting the Path and Variables in Windows](./setting%20the%20path%20and%20variables%20in%20windows/setting%20the%20path%20and%20variables%20in%20windows.md).

Yay! You have successfully installed the CLI, now let’s initialize. 

## Initialize

If you have reached here, you are nearly there - at the promised landscape of DataOS. To initialize, run the init command.

```bash
dataos-ctl init
```

This command will start a short(really short) Q&A session. Don’t worry, I have got the cheat sheet below. Just follow the instructions.

```bash
dataos-ctl init

#to keep things interesting, the 'Y' is capital lettered, while 'n' is small lettered

INFO[0000] The DataOS® is already initialized, do you want to add a new context? (Y,n)  
->Y   #input the answer: Y or n
INFO[0255] 🚀 initialization...
                        
INFO[0255] The DataOS® is not initialized, do you want to proceed with initialization? (Y,n)  
->Y

INFO[0269] Please enter a name for the current DataOS® Context?  
-><name of the DataOS context> 
#for example 'kutumbakam'. You can write the name of your choice.
#your enterprise can have multiple contexts available for you to connect. Choose any one.
#you can always change the context through a CLI command, after login. 

INFO[0383] Please enter the fully qualified domain name of the DataOS® instance?  
-><domain name> 
#for example 'vasudhaiva-kutumbakam.dataos.app'
INFO[0408] entered DataOS®: kutumbakam : vasudhaiva-kutumbakam.dataos.app 

INFO[0408] Are you operating the DataOS®? (Y,n)         
->n  
#if you are the operator(admin) for your enterprise, type Y
#the installation steps, if you type Y, will change.
INFO[0452] 🚀 initialization...complete
```

If you are the operator/admin for your enterprise then the installation steps for you, after the last step, will change. These are covered in the Operator Document for DataOS.

## Log in

After the successful initialization of DataOS context, you can log into your account with the following command. Finally, the moment we have been waiting for is here.

```jsx
dataos-ctl login
```

If your enterprise has taken multiple DataOS contexts then you can use the same command terminal client, the one you just installed, to access & use any of those contexts.

## Test

Run the following commands to ensure the successful installation of DataOS CLI. These commands will show the version and health status of the installed DataOS CLI.

```jsx
dataos-ctl version
dataos-ctl health
```

Did it take you more than a couple of minutes? Well, when someone says ‘just a minute’ they don’t mean it literally!

## Linked Documents

- [Read on Curl utility](./read%20on%20curl%20utility.md)

- [Setting the Path and Variables in Windows](./setting%20the%20path%20and%20variables%20in%20windows/setting%20the%20path%20and%20variables%20in%20windows.md)