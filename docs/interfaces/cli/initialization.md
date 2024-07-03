# CLI Initialization

## Initialize the DataOS Context

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

<details><summary>Potential Errors and Solutions</summary>

<b>Error</b>
<br>
When attempting to log in using the <code>dataos-ctl</code> command-line tool, if the following sequence of log messages are observed:

```shell
iamgroot@abcs-MacBook-Pro-2 ~ % ./darwin-arm64/dataos-ctl login
INFO[0000] 🔑 login...                                   
ERRO[0000] no cred file, need to login                  
WARN[0000] no cred file, logging in now, Config File ".dataos.cred.config" Not Found in "[/Users/fsnooruddin/.dataos/hawk]"
ERRO[0000] 🔑 login...error                              
ERRO[0000] Post "https://https//emerging-hawk.dataos.app/home//heimdall/api/v1/oidc/tickets": dial tcp: lookup https: no such host
```
<b>Solution</b>
<br>

The final error message indicates an issue with the URL used during the login process. Specifically, the URL contains an incorrect and duplicated protocol prefix (<code>https://https//</code>).
<br>
Ensure that the URL specified during initialization or within your configuration files is correctly formatted. The correct URL should not include the <code>https://</code> protocol as part of the hostname. Instead, use only the domain name.
<br>
<b>Correct URL Format</b>

```shell
INFO[0383] Please enter the fully qualified domain name of the DataOS® instance?  
->vasudhaiva-kutumbakam.dataos.app
```
</details>

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

Proceed to the [CLI Command Reference](/interfaces/cli/command_reference/) to get details of the available commands.