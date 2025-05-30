---
search:
  exclude: true
---

# DataOS Integration with Tableau

This article will help you to set up the connection between DataOS and Tableau. It provides specific steps needed to fetch data from DataOS into Tableau.

## Explore your DataOS data with Tableau

Tableau is one of the most powerful business intelligence tools which allows you to pull vast amounts of information from disparate sources, and helps you turn it into advanced visualizations. The dashboard created from these visualizations empowers you with business insights and helps in data-driven decisions.

DataOS and Tableau integration work to take advantage of that powerful visualization technology on the data pulled from DataOS.

## Requirements

- Tableau Desktop installed on your system - If Tableau is not installed on your system, you can download the latest version from the [Tableau website](https://www.tableau.com/products/desktop/download).
- Java installed on your system- you can download the latest version from the [Latest Oracle Java](https://www.oracle.com/java/technologies/downloads/#jdk17-mac).
- Driver - In order to connect to DataOS Catalog, you would have to install the driver.
- DataOS Wrapped Token- To authenticate and access DataOS, you need a wrapped token. This token contains the API key along with the cluster name. 

## Download and install the driver

Check your Tableau version and follow the steps given below:

- Tableau: 2021.3, 2021.2.2, 2021.1.5, 2020.4.8, 2020.3.12, and above
    
    a. Download the driver (for example, trino-jdbc-373.jar) from the [Trino](https://trino.io/docs/current/client/jdbc.html) [](https://trino.io/docs/current/installation/jdbc.html)page. Please note that Presto is Trino now.
    
    b. Copy the downloaded JAR file to the appropriate location.
    
    - ~/Library/Tableau/Drivers for MAC
    - C:\Program Files\Tableau\Drivers for WINDOWS

- Tableau: 10.0-2020.2 and below.
    
    a. Download the driver from [Tableau driver download page](https://www.tableau.com/support/drivers?__full-version=20204.21.0114.0916#presto).
    
    <b>Select the operating system and bit version according to your system configurations.</b>

    <center>
      <div style="text-align: center;">
        <img src="/resources/cluster/bi_tools/tableau/integration-tableau-driver-download_.png" alt="Driver download" style="width: 40rem; border: 1px solid black;">
        <figcaption>Driver download</figcaption>
      </div>
    </center>

<b>Click on the Download button (mac or Windows).</b>

  <center>
    <div style="text-align: center;">
      <img src="/resources/cluster/bi_tools/tableau/integration-tableau-driver-downloadmac.png" alt="Driver download for Mac" style="width: 40rem; border: 1px solid black;">
      <figcaption>Driver download for Mac</figcaption>
    </div>
  </center>

<b>Double-click on downloaded 'Simba Presto 1.1.pkg' for mac or Windows 64-bit driver to run the installer.</b>

<b>Click Continue and follow the steps for a successful installation.</b>

## Generate DataOS API token


1. Sign in to your DataOS instance with your username and password. On the DataOS home page, click on Profile.

    <center>
      <div style="text-align: center;">
        <img src="/resources/cluster/home.png" alt="DataOS Homepage" style="width: 40rem; border: 1px solid black;">
        <figcaption>DataOS Homepage</figcaption>
      </div>
    </center>

2. On the 'Profile' page, click on Tokens.

    <center>
      <div style="text-align: center;">
        <img src="/resources/cluster/bi_tools/powerbi/using_odbc_driver/integration-dataos-profile.png" alt="Profile" style="width: 40rem; border: 1px solid black;">
        <figcaption>Profile</figcaption>
      </div>
    </center>


3. Click on the Add API Key link on the Tokens tab.
    
    <center>
      <div style="text-align: center;">
        <img src="/resources/cluster/bi_tools/powerbi/using_odbc_driver/integration-dataos-token-apikey.png" alt="DataOS Token" style="width: 40rem; border: 1px solid black;">
        <figcaption>DataOS Token</figcaption>
      </div>
    </center>

4. Type in a name for this token and also set the validity period of your token based on the security requirements as per your business needs. Click Save to create one for you.

    <center>
      <div style="text-align: center;">
        <img src="/resources/cluster/bi_tools/powerbi/using_odbc_driver/integration-add-key.png" alt="Add key" style="width: 40rem; border: 1px solid black;">
        <figcaption>Add key</figcaption>
      </div>
    </center>

5. The API key is listed below. Click on the “eye icon” on the right side to make the full API key visible.

    <center>
      <div style="text-align: center;">
        <img src="/resources/cluster/bi_tools/powerbi/using_odbc_driver/integration-key-created.png" alt="Key created" style="width: 40rem; border: 1px solid black;">
        <figcaption>Key created</figcaption>
      </div>
    </center>


6. Click on the API key to copy it. You would need this API key to create wrapped token.


## Create Wrapped Token Using Terminal

1. On CLI, use the command below to create a wrapped token. Provide the apikey token and name of the Cluster.

```bash
echo '{"token":"<apikey-token>","cluster":"<cluster-name>"}' | base64
```
2. For the following values of api-key and cluster-name, the command will appear as shown below:<br>
   apikey-token = abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz <br>
   cluster-name = miniature
<br>Ensure that JSON string should not contain any spaces.
```bash

echo '{"token":"abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz","cluster":"miniature"}' | base64

```
3. Upon successful execution, the output will resemble the following, creating a token.

```bash
eyJ0b2tlbiI6ImFiY2RlZmdoaWprbG1ub3BxcnN0dXZ3eHl6YWJjZGVmZ2hpamtsbW5vcHFyc3R1
dnd4eXoiLCAiY2x1c3RlciI6ImphcnZpc2NsdXN0ZXIifQ
```
4. Once the token is created then align it in a single line. You would need this token to configure the Presto driver.

```bash
eyJ0b2tlbiI6ImFiY2RlZmdoaWprbG1ub3BxcnN0dXZ3eHl6YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXoiLCAiY2x1c3RlciI6ImphcnZpc2NsdXN0ZXIifQ
```


## Configure driver on Tableau

You need to configure the Presto driver in the Tableau application to connect to your data in DataOS.

1. Open the Tableau desktop application. Click on More to access the list of all the servers connectors. Search for Presto and click on it.

    <center>
      <div style="text-align: center;">
        <img src="/resources/cluster/bi_tools/tableau/integration-tableau-more.png" style="width: 40rem; border: 1px solid black;">
        <figcaption>Server connectors</figcaption>
      </div>
    </center>

2. A dialogue box appears where the user can provide the following values:

    | Property | Value |
    | --- | --- |
    | Server | e.g. tcp.reasonably-welcome-grub.dataos.io |
    | Port | 7432 |
    | Catalog | e.g. icebase |
    | Schema | an optional field |
    | Authentication | LDAP |
    | Username | Username |
    | Password | Access API Key from DataOS |
    | Require SSL | Check the box |

    <center>
      <div style="text-align: center;">
        <img src="/resources/cluster/bi_tools/tableau/integration-tableau-inputs.png" alt="Inputs" style="width: 40rem; border: 1px solid black;">
        <figcaption>Inputs</figcaption>
      </div>
    </center>


3. Click Sign In.

> 📌 Note: If you encounter any error in setting up the connection, please check DataOS URL, and validity of the API key and try again or contact your administrator.


## Access DataOS on Tableau

1. Once you've completed the driver configuration steps successfully, you can see the DataOS catalog in the left panel in Tableau dialog.

    <center>
      <div style="text-align: center;">
        <img src="/resources/cluster/bi_tools/tableau/integration-tableau-connected.png" alt="Tableau connected" style="width: 40rem; border: 1px solid black;">
        <figcaption>Tableau connected</figcaption>
      </div>
    </center>

2. To get the list of available schemas, click on Search icon. To select the relevant schema, double-click on it.

    <center>
      <div style="text-align: center;">
        <img src="/resources/cluster/bi_tools/tableau/integration-tableau-schema.png" alt="Schema" style="width: 40rem; border: 1px solid black;">
        <figcaption>Schema</figcaption>
      </div>
    </center>

3. To bring the data from the table, click on Search icon and you can see all the tables available in your DataOS schema cluster. Double-click to select a table that you want to retrieve data from.

    <center>
      <div style="text-align: center;">
        <img src="/resources/cluster/bi_tools/tableau/integration-tableau-tables.png" alt="Tables" style="width: 40rem; border: 1px solid black;">
        <figcaption>Tables</figcaption>
      </div>
    </center>

4. Click Upload Now to load the data for preview. Tableau retrieves data from the selected DataOS table and loads it into a worksheet.

    <center>
      <div style="text-align: center;">
        <img src="/resources/cluster/bi_tools/tableau/integration-tableau-data.png" alt="Data loaded" style="width: 40rem; border: 1px solid black;">
        <figcaption>Data loaded</figcaption>
      </div>
    </center>

5. Now you can explore and visualize this data in Tableau.

<center>
  <div style="text-align: center;">
    <img src="/resources/cluster/bi_tools/tableau/integration-tableau-visualization.png" alt="Tableau visualization" style="width: 40rem; border: 1px solid black;">
    <figcaption>Tableau visualization</figcaption>
  </div>
</center>
