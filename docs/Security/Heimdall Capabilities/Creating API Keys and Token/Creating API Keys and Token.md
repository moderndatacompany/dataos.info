# Creating API Keys and Token

API keys/tokens are used to authenticate requests to  DataOS resources. For example, when calling a service endpoint, you need to supply a valid API token in the HTTP `Authorization` header, with a valid token specified as the header value. You can generate API keys/tokens from DataOS UI as well as using DataOS CLI commands.

# From DataOS CLI

## Create API Key

You need an API key to run this service and connect to Fastbase Pulsar 

- List existing key
- Create a new API key

### List Existing Key

```bash
tmdc@tmdc:~$ dataos-ctl user apikey get
INFO[0000] 🔑 user apikey get...                         
INFO[0000] 🔑 user apikey get...complete                 

                                                 TOKEN                                                 |  TYPE  |      EXPIRATION      |                  NAME                   
-------------------------------------------------------------------------------------------------------|--------|----------------------|-----------------------------------------
  aH9sAY5fcXVpY2tseV9ldmVubHlfY29ycmVjdF9raXQuM2ZiOTI4ZTYaH9sAY5fcXTUzLTgaH9sAY5fcXaH9sAY5fcX0| apikey | 2023-08-10T23:00:00Z | token_ad9baade458c5c6f3  
  bI9sAY5fcXVpY2tseV9ldmVubHlfY39ycmVjdF9raXQuM2ZiOTI4ZTYaH9sAY5fcXTUzLTgaH9sAY5fcXaH9sAY5fcX0| apikey | 2023-06-19T08:00:00Z | token_bc6hggaa435v8b5f3
```

### Create a new API key

```bash
tmdc@tmdc:~$ dataos-ctl user apikey create
INFO[0000] 🔑 user apikey...                             
INFO[0000] 🔑 user apikey...complete                     

                                                   TOKEN                                                   |  TYPE  |      EXPIRATION      |                  NAME                    
-----------------------------------------------------------------------------------------------------------|--------|----------------------|------------------------------------------
  aH9sAY5fcXVpY2tseV9ldmVubHlfY29ycmVjdF9raXQuM2ZiOTI4ZTYaH9sAY5fcXTUzLTgaH9sAY5fcXaH9sAY5fcX0 | apikey | 2022-06-22T12:00:00Z | token_bc6hggaa435v8b5f3
```

# DataOS UI

## Generate DataOS API token

1. Sign in to your DataOS instance with your username and password. On the DataOS home page, click on 'Profile'.

    <img src="../../Integration%20&%20Ingestion/Tableau/integration-dataos-homepage.png"
            alt="integration-dataos-homepage.png"
            style="display: block; margin: auto" />

2. On the 'Profile' page, click on Tokens.

    <img src="Creating%20API%20Keys%20and%20Token/integration-dataos-profile.png"
            alt="integration-dataos-profile.png"
            style="display: block; margin: auto" />

3. Click on the Add API Key link on the Tokens tab:

    <img src="Creating%20API%20Keys%20and%20Token/integration-dataos-token-apikey.png"
            alt="integration-dataos-token-apikey.png"
            style="display: block; margin: auto" />

4. Type in the name for this token and also set the validity period of your token based on the security requirements as per your business needs. Click Save to create one for you.

    <img src="Creating%20API%20Keys%20and%20Token/integration-add-key.png"
      alt="integration-add-key.png"
      style="display: block; margin: auto" />

5. The API key is listed below. Click on the “eye icon” on the right side to make the full API key visible.

    <img src="Creating%20API%20Keys%20and%20Token/integration-key-created.png"
        alt="integration-key-created.png"
        style="display: block; margin: auto" />

6. Click on the API key to copy it. You would need this API key to configure the Presto driver.