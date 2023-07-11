# Curl

Curl is a command-line utility that transfers data from or to a server that is designed to work without user interaction. Before installing a Curl utility, check if it is already installed. If Curl is already installed on your system, then you can skip the rest of the steps.

Below are the steps mentioned to check if Curl is already installed and useful resources to download and install in case Curl is not installed on your system. 

## Curl on Ubuntu or Linux

```bash
# To check if you have curl installed already:
curl --version

# To update your ubuntu or linux box:
sudo apt update

# To install curl utility:
sudo apt install curl
```

## Curl on Mac

```bash
# To check if you have curl installed already:
curl --version

# To see if you have brew installed already:
brew -v

# In case brew is not installed, make sure to install it:
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" < /dev/null 2> /dev/null

# After installing brew, let's install curl:
brew install curl
```

## Installing Curl on Windows

To download and install curl on your Windows OS, visit [curl Download Wizard](https://curl.se/dlwiz/?type=bin). Look for the version of your Windows OS and download the curl executable file. After downloading, extract the zip file and go to the SRC folder to locate the executable file.

Copy your executable file and place it inside the following directory `C:\Users{your_user}\programs>`. Next, open the command prompt and change the directory to `C:\Users{your_user}\programs>`.

Finally, run the following command ensuring a successful installation.

```bash
curl --version
```