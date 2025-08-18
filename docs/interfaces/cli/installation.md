
# CLI Installation

Follow the steps enumerated below to install the Command Line Interface. Check the prerequisites before moving forward.

## Requirements

 1. Get the following items from the DataOS administrator or the Modern Data team:
    - DataOS prime apikey
    - Domain name of the DataOS context/instance
    - Version of the CLI to be installed
 <!-- 2. Please ensure that the curl utility is installed on your system. To check, use this command:
    ```sh
    curl --version
    ```
    If curl is not installed, follow the steps to [download curl](/interfaces/cli/read_on_curl_utility/). -->

 2. Find out the operating system you are using, and the processor's architecture. The following is a list of supported Arch values:
     

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

 3. Ensure that the curl utility is installed on your system. This step applies to Mac and Linux users.
    To check, use this command:
    ```sh
    curl --version
    ```
    If curl is not installed, follow the steps to [download curl](/interfaces/cli/read_on_curl_utility/).
  

<aside class="callout">🗣️ Replace <b>{{placeholder}}</b> text in various commands with appropriate values before running the command.</aside>

## Installation on MacOS

1. Export the environment variable PRIME_APIKEY to pass it to the subsequent commands(replace **`{{prime_apikey}}`**  with the DataOS® API key to connect with the prime context).

    ```sh
    export PRIME_APIKEY="{{prime_apikey}}" #replace whole placeholder
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

    <aside class="callout">🗣️ Reach out to the DataOS administrator to obtain the latest version of the CLI.</aside>

3. Download the DataOS CLI binary using the below command (replace the **`ARCH`** </span> value of the processor and the **`CLI_VERSION`** </span>to be installed):

    ```bash
    curl --silent --output dataos-ctl-{{ARCH}}.tar.gz --location --request GET "https://prime.tmdata.io/plutus/api/v1/files/download?name=dataos-ctl-{{ARCH}}.tar.gz&dir=cli-apps-{{CLI_VERSION}}&apikey=$PRIME_APIKEY"
    ```
    
    Example:

    A Mac user with intel-chip, installing the 2.8 version of the CLI would input the below command.
    
    ```bash
    curl --silent --output dataos-ctl-darwin-amd64.tar.gz --location --request GET "https://prime.tmdata.io/plutus/api/v1/files/download?name=dataos-ctl-darwin-amd64.tar.gz&dir=cli-apps-2.8&apikey=$PRIME_APIKEY"
    ```

4. *Optional step*: Download the checksum file using the following command (replace the **`ARCH`** value of the processor and the **`CLI_VERSION`** to be installed):

    ```bash
    curl --silent --output dataos-ctl-{{ARCH}}.tar.gz.sha256sum --location --request GET "https://prime.tmdata.io/plutus/api/v1/files/download?name=dataos-ctl-{{ARCH}}.tar.gz.sha256sum&dir=cli-apps-{{CLI_VERSION}}&apikey=$PRIME_APIKEY"
    ```

    Example:

    A Mac user with an intel-chip (identified as  **darwin-amd64** for the processor), installing the **2.8 version of the CLI** would input the below command.

    ```bash
    
    curl --silent --output dataos-ctl-darwin-amd64.tar.gz.sha256sum --location --request GET "https://prime.tmdata.io/plutus/api/v1/files/download?name=dataos-ctl-darwin-amd64.tar.gz.sha256sum&dir=cli-apps-2.8&apikey=$PRIME_APIKEY"
    ```
    

5. *Optional step*: Validate that the zip has not been tampered with.

    ```bash
    shasum -a 256 -c dataos-ctl-{{Arch}}.tar.gz.sha256sum
    ```
    Example:

    ```bash
    shasum -a 256 -c dataos-ctl-darwin-amd64.tar.gz.sha256sum
    ```

    If the zip file has been downloaded as expected, you should get the following output:

    ```bash
    dataos-ctl-darwin-amd64.tar.gz: OK
    ```

6. Extract the dataos-ctl binary.

    ```bash
    tar -xvf dataos-ctl-{{ARCH}}.tar.gz
    ```
    Example:

    ```bash
    tar -xvf dataos-ctl-darwin-amd64.tar.gz
    ```
    Here is the expected output:

    ```bash
    x darwin-amd64/
    x darwin-amd64/dataos-ctl
    ```

7. Run the following command to place the extracted dataos-ctl in a directory that is in your PATH. 

    ```bash
    export PATH=$PATH:$HOME/{{dir-name}}
    ```
    You will get the directory name from the output of the previous command. 
    Example:

    In this case, it is **`darwin-amd64/`**.
    ```
    export PATH=$PATH:$HOME/darwin-amd64/
    ```
    <br>

    > 🗣️  To ensure persistent access to the dataos-ctl command, add the export statement to your shell's initialization file (e.g., `.zshrc` for Zsh or `.bash_profile` for Bash). This prevents the need to re-run the command each time you open a new terminal session.
    >
    > Here's a more detailed explanation:
    >
    > 1. Identify Your Shell and Initialization File:
    >        - Check your shell: Open Terminal and type echo `$SHELL`. If it outputs `/bin/zsh`, you're using Zsh (the default shell in newer macOS versions). 
    >    If the output is `/bin/bash`, you're using Bash.
    >        - Determine the correct  and Open the file using the command below:
    >            - `Zsh`: Edit the `~/.zshrc` file.
    >            - `Bash`: Edit the `~/.bash_profile` file. 
    >
    > 2. Open the Initialization File: 
    >       - Open Terminal.
    >       - Use a text editor to open the appropriate file. For example:
    >            - `Zsh`: nano ~/.zshrc 
    >            - `Bash`: nano ~/.bash_profile 
    >
    >
    > 3. Add the Export Path to Your Shell Configuration File.
    >   ```bash
    >   export PATH=$PATH:$HOME/.dataos/bin
    >   ```
    >
    >
    > 4. Save the changes to the file (e.g., press Ctrl+X, then Y, then Enter in nano). 
    >  
    >
    > 5. Load the file in Shell using:      
    >   ```bash
    >   source ~/.zshrc
    >   ```


You have successfully installed the CLI, now the next step is to [initialize](/interfaces/cli/initialization/) the DataOS context. 


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


## Installation on Linux

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

    <aside class="callout">🗣️ Reach out to the DataOS administrator to obtain the latest version of the CLI.</aside>
    

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


    ```bash
    
    shasum -a 256 -c dataos-ctl-linux-{{ARCH}}.tar.gz.sha256sum
    ```

    Expected output after running the above command:

    ```bash
    dataos-ctl-linux-{{ARCH}}.tar.gz: OK
    ```

6. Extract the dataos-ctl binary. Update the **`ARCH`** value in the command


    ```bash
    
    tar -xvf dataos-ctl-linux-{{ARCH}}.tar.gz
    ```

    Expected output:

    ```bash
    x linux-{{ARCH}}/
    x linux-{{ARCH}}/dataos-ctl
    ```

7. Run the following command to place the extracted dataos-ctl in a directory that is in your PATH.

    ```bash
    export PATH=$PATH:$HOME/linux-{{ARCH}}
    ```
    
    Example:
    
    ```
    export PATH=$PATH:$HOME/linux-amd64
    ```

    > 🗣️  To ensure persistent access to the dataos-ctl command, add the export statement to your shell's initialization file (e.g., `.zshrc` for Zsh or `.bash_profile` for Bash). This prevents the need to re-run the command each time you open a new terminal session.
    >
    > Here's a more detailed explanation:
    >
    > 1. Identify Your Shell and Initialization File:
    >        - Check your shell: Open Terminal and type echo `$SHELL`. If it outputs `/bin/zsh`, you're using Zsh (the default shell in newer macOS versions). 
    >    If the output is `/bin/bash`, you're using Bash.
    >        - Determine the correct  and Open the file using the command below:
    >            - `Zsh`: Edit the `~/.zshrc` file.
    >            - `Bash`: Edit the `~/.bash_profile` file. 
    >
    > 2. Open the Initialization File: 
    >       - Open Terminal.
    >       - Use a text editor to open the appropriate file. For example:
    >            - `Zsh`: nano ~/.zshrc 
    >            - `Bash`: nano ~/.bash_profile 
    >
    >
    > 3. Add the Export Path to Your Shell Configuration File.
    >   ```bash
    >   export PATH=$PATH:$HOME/.dataos/bin
    >   ```
    >
    >
    > 4. Save the changes to the file (e.g., press Ctrl+X, then Y, then Enter in nano). 
    >  
    >
    > 5. Load the file in Shell using:      
    >   ```bash
    >   source ~/.zshrc
    >   ```

You have successfully installed the CLI, now the next step is to [initialize](/interfaces/cli/initialization/) the DataOS context. 

## Installation on Windows

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
   
    <aside class="callout">🗣️ Reach out to the DataOS administrator to obtain the latest version of the CLI.</aside>

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
    <aside class="callout">🗣️ Reach out to the DataOS administrator to obtain the latest version of the CLI.</aside>


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

   You will always use this directory to run DataOS. 
   
   To open the DataOS from anywhere in the system, place the extracted file in a directory that is in your PATH. To add the directory in PATH, refer to [Setting the Path and Variables in Windows](/interfaces/cli/windows_path_setting/).

   > Important: If you have not added the directory containing the dataos-ctl executable to your PATH variables, you must use `.\dataos-ctl `to run the command. Once you add the directory to the PATH variable, you can simply use `dataos-ctl` from any location.

You have successfully installed the CLI, now the next step is to initialize the DataOS context.

Click here to proceed to [CLI Initialization](/interfaces/cli/initialization/).



## Linked Documents

- [Read on Curl utility](/interfaces/cli/read_on_curl_utility/).

- [Setting the Path and Variables in Windows](/interfaces/cli/windows_path_setting/).
