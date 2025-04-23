---
search:
  exclude: true
---

# DataOS Integration with Power BI Using ODBC Driver

This article will help you to set up the connection between DataOS and Power BI. It provides specific steps needed to fetch data from DataOS into Power BI using Simba Presto ODBC driver.

## Requirements

- Power BI Desktop installed on your system - If Power BI is not installed on your system, you can download the latest version from the [Power BI website](https://powerbi.microsoft.com/en-us/downloads/).
- Simba Presto ODBC Driver - In order to connect to DataOS Catalog, you would have to install this Presto driver.
- DataOS API token - To authenticate and access DataOS, you will need API token.

## Download and Install Presto Driver

1.  Download it from [Presto ODBC & JDBC Drivers download page](https://www.magnitude.com/drivers/presto-odbc-jdbc).

    <center>
      <div style="text-align: center;">
        <img src="/resources/cluster/bi_tools/powerbi/using_odbc_driver/integration-presto-download.png" alt="Presto download" style="width: 40rem; border: 1px solid black;">
        <figcaption>Presto download</figcaption>
      </div>
    </center>

2. To run the installer, double-click on downloaded Simba Presto XX-bit installer file. Select the 32 or 64 bit version according to your system configurations.

    <center>
      <div style="text-align: center;">
        <img src="/resources/cluster/bi_tools/powerbi/using_odbc_driver/integration-presto-setup.png" alt="Presto setup" style="width: 40rem; border: 1px solid black;">
        <figcaption>Presto setup</figcaption>
      </div>
    </center>

    Follow the steps for the successful installation.

    a. Click Next.

    b. Select the check box to accept the terms of the License Agreement if you agree, and then click Next.

    c. To change the installation location, click Change, then browse to the desired folder, and then click OK.

    To accept the installation location, click Next.

    d. Click Install.

    e. When the installation completes, click Finish.

    <center>
      <div style="text-align: center;">
        <img src="/resources/cluster/bi_tools/powerbi/using_odbc_driver/integration-presto-setup-finish.png" style="width: 40rem; border: 1px solid black;">
        <figcaption>Presto setup done</figcaption>
      </div>
    </center>


3. After successful installation, copy the license file (that you have received in your email) into the \lib subfolder of the Simba installation folder.

<center>
  <div style="text-align: center;">
    <img src="/resources/cluster/bi_tools/powerbi/using_odbc_driver/integration-presto-license-lib.png" alt="Presto license" style="width: 40rem; border: 1px solid black;">
    <figcaption>Presto license</figcaption>
  </div>
</center>

    

> 📌 Note: Contact your network administrator in case you encounter an error due to not having required admin privileges.

## Generate DataOS API Token

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


6. Click on the API key to copy it. You need this API key to configure Simba Presto driver.

## Configure Presto ODBC DSN

To use the Simba Presto ODBC Driver in Power BI application, you need to configure a Data Source Name (DSN) to connect to your data in DataOS.

1. Open ODBC Data Source Administrator (64-bit or 32-bit).

2. Click  System DSN tab.

3. In the list of DSNs, select Simba Presto ODBC DSN, and then click Configure.

    <center>
      <div style="text-align: center;">
        <img src="/resources/cluster/bi_tools/powerbi/using_odbc_driver/integration-odbc-systemdsn.png" alt="ODBC system DSN" style="width: 40rem; border: 1px solid black;">
        <figcaption>ODBC system DSN</figcaption>
      </div>
    </center>


4. In the DSN Setup dialog box, provide the following inputs:

    - Provide 'Description' for the data source name.
    - In the 'Authentication' section:
        - Select Authentication type as LDAP Authentication.
        - Enter username for the User and generated API key as the password.
    - Now in the 'Data Source' section, provide the required information.
        - Host (e.g. tcp.reasonably-welcome-grub.dataos.io)
        - Port (e.g. 7432)
        - Catalog (e.g. icebase)
        - Schema (optional)

    <center>
      <div style="text-align: center;">
        <img src="/resources/cluster/bi_tools/powerbi/using_odbc_driver/new_image.png" alt="Inputs for DSN setup" style="width: 30rem; border: 1px solid black;">
        <figcaption>Inputs for DSN setup</figcaption>
      </div>
    </center>


5. In the DSN Setup dialog box, click SSL Options and enable SSL.

    <center>
      <div style="text-align: center;">
        <img src="/resources/cluster/bi_tools/powerbi/using_odbc_driver/enable_ssn.png" alt="Enable SSN" style="width: 30rem; border: 1px solid black;">
        <figcaption>Enable SSN</figcaption>
      </div>
    </center>

6. Click Test. and if successful, press OK to close the Test Results dialog box.

    <center>
      <div style="text-align: center;">
        <img src="/resources/cluster/bi_tools/powerbi/using_odbc_driver/integration-prestodsn-testsuccess.png" alt="Test success" style="width: 30rem; border: 1px solid black;">
        <figcaption>Test success</figcaption>
      </div>
    </center>

7.Click OK to save your DSN.

> 📌 Note: If you encounter any error in setting up the connection, please check DataOS url, validity of API key and try again or contact your administrator.

## Access DataOS on Power BI

1. Launch Power BI. Click on the Get Data option in the top menu bar and click More.

    <center>
      <div style="text-align: center;">
        <img src="/resources/cluster/bi_tools/powerbi/using_odbc_driver/integration-powerbi-getdata-more.png" alt="Get data" style="width: 40rem; border: 1px solid black;">
        <figcaption>Get data</figcaption>
      </div>
    </center>

2. Search for the ODBC from the data source list, then select ODBC and click on Connect.

    <center>
      <div style="text-align: center;">
        <img src="/resources/cluster/bi_tools/powerbi/using_odbc_driver/integration-powerbi-search-odbc.png" alt="Search ODBC" style="width: 40rem; border: 1px solid black;">
        <figcaption>Search ODBC</figcaption>
      </div>
    </center>


3. Select the DSN you tested successfully during the DSN setup process, and click OK

    <center>
      <div style="text-align: center;">
        <img src="/resources/cluster/bi_tools/powerbi/using_odbc_driver/integration-powerbi-dsn-selectname.png" alt="Select DSN name" style="width: 40rem; border: 1px solid black;">
        <figcaption>Select DSN name</figcaption>
      </div>
    </center>

4. Enter API key for username and password both in the dialogue box and click on Connect.

    <center>
      <div style="text-align: center;">
        <img src="/resources/cluster/bi_tools/powerbi/using_odbc_driver/integration-powerbi-dsn-unpass.png" alt="Credentials to access the data source" style="width: 40rem; border: 1px solid black;">
        <figcaption>Credentials to access the data source</figcaption>
      </div>
    </center>
    
5. On successful connection, you can see the DataOS catalog in the left panel. Select the schema and table and click Load.

    <center>
      <div style="text-align: center;">
        <img src="/resources/cluster/bi_tools/powerbi/using_odbc_driver/integration-powerbi-data-loaded.png" alt="Data loaded" style="width: 40rem; border: 1px solid black;">
        <figcaption>Data loaded</figcaption>
      </div>
    </center>

    

6. Now you can explore and visualize this data in Power BI.

<center>
  <div style="text-align: center;">
    <img src="/resources/cluster/bi_tools/powerbi/using_odbc_driver/integration-powerbi-data-chart.png" alt="PowerBI data chart" style="width: 40rem; border: 1px solid black;">
    <figcaption>PowerBI data chart</figcaption>
  </div>
</center>