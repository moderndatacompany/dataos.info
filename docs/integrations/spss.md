# DataOS Integration with IBM SPSS Statistics

This article will help you to set up the connection between DataOS and SPSS Statistics. It provides specific steps needed to fetch data from DataOS into SPSS Statistics for descriptive analysis and mining.

## Explore DataOS data with SPSS Statistics

SPSS Statistics is a comprehensive statistical analysis and data management solution.  SPSS can take data from almost any type of file and use them to generate tabulated reports, charts and plots of distributions and trends, descriptive statistics. It is  used by market researchers, survey companies, government, education researchers, marketing organizations and data miners.

DataOS and SPSS Statistics integration works to take advantage of powerful statistical analysis, on the data pulled from DataOS. 

## Requirements
 
- SPSS Statistics installed on your system - If SPSS Statistics is not installed on your system, you can download the latest version from the <a href="https://www.ibm.com/analytics/spss-statistics-software" target="_blank">IBM SPSS software website</a>

- Simba Presto ODBC Driver - In order to connect to DataOS Catalog, you would have to install the Presto driver. 

- DataOS API token - To authenticate to and access DataOS, you will need an API token.

## Download and install Presto driver

1.  Download it from <a href="https://www.magnitude.com/drivers/presto-odbc-jdbc" target="_blank">Presto ODBC & JDBC Drivers download page</a>.
      
   ![Image](./images/integration-presto-download.png)
2.  To run the installer, double-click on downloaded **Simba Presto XX-bit** installer file. Select the 32 or 64 bit version according to your system configurations. 

![Image](./images/integration-presto-setup.png)

Follow the steps for the successful installation.

a. Click **Next**.

b. Select the check box to accept the terms of the License Agreement if you agree, and then click **Next**.

c. To change the installation location, click Change, then browse to the desired folder, and then click **OK**.

To accept the installation location, click **Next**.

d. Click **Install**.

e. When the installation completes, click **Finish**.

![Image](./images/integration-presto-setup-finish.png)
3. After successful installation, copy the **license** file (that you have received in your email) into the **\lib** subfolder of the Simba installation folder.

![Image](./images/integration-presto-license-lib.png)

> :material-alert: **Note**: Contact your network administrator in case you encounter an error due to not having required admin privileges.


## Generate DataOS API token

1. Sign in to your DataOS instance with your username and password. On the DataOS home page, click on '**Profile**'.
![Image](./images/integration-dataos-homepage.png)
2. On the 'Profile' page, click on **Tokens**.
![Image](./images/integration-dataos-profile.png)
3. Click on the **Add API Key** link on the **Tokens** tab:
![Image](./images/integration-dataos-token-apikey.png)
4. Type in name for this token and also set the validity period of your token based on the security requirements as per your business needs. Click **Save** to create one for you. 
![Image](./images/integration-add-key.png)
5. The API key is listed below. Click on the “eye icon” on the right side to make the full API key visible.
![Image](./images/integration-key-created.png)
6. Click on the API key to copy it. You need this API key to configure Simba Presto driver. 

## Configure Presto ODBC DSN 

To use the Simba Presto ODBC Driver in SPSS Statistics application, you need to configure a Data Source Name (DSN) to connect to your data in DataOS.

>:material-alert: **Note**: Currently, SPSS does not provide an SPSS Data Access Pack for Mac so you need to use Windows system. For more information, refer to <a href="https://www.ibm.com/support/pages/can-i-setup-odbc-data-sources-mac-import-data-spss" target="_blank">IBM Support.</a>

1. Launch SPSS Statistics. Double-click on the ** New Database Query**.
![Image](./images/integration-spss-new-database-query.png)

2. Click on **Add ODBC DataSource**.
![Image](./images/integration-spss-add-datasource.png)
3. In **ODBC Data Source Administrator** (64-bit or 32-bit) dialog box, click  **System DSN** tab.

4. In the list of DSNs, select Simba Presto ODBC DSN, and then click **Configure**.
![Image](./images/integration-odbc-systemdsn.png)
5. In the DSN Setup dialog box, provide the following inputs:

    - Provide 'Description' for data source name.

    - In the 'Authentication' section

        - Select Authentication type as `No Authentication`
        - Enter generated API key as username

    - Now in the 'Data Source' section, provide required information.

        - `Host` (e.g. tcp.reasonably-welcome-grub.dataos.io)
        - `Port` (e.g. 7432)
        - `Catalog` (e.g. icebase)
        - `Schema` (optional)
![Image](./images/integration-simba-dsn-setup.png)

6. In the DSN Setup dialog box, click **SSL Options** and enable SSL.
![Image](./images/enable ssn.png)
7. Click **Test**. and if successful, press **OK** to close the Test Results dialog box.
![Image](./images/integration-prestodsn-testsuccess.png)
8. Click **OK** to save your DSN. 

> :material-alert: **Note**: If you encounter any error in setting up the connection, please check DataOS url, validity of API key and try again or contact your administrator.

## Access DataOS on SPSS Statistics
1. Launch SPSS Statistics. Click on the **New Database Query** option. 
![Image](./images/integration-spss-new-database-query.png)
2. Select the DSN you tested successfully during the DSN setup process, and double-click.
![Image](./images/integration-spss-select-dsn.png)
4. Enter IBM SPSS credentials in the dialogue box and click on **Connect**.
![Image](./images/integration-spss-dsn-login.png)
5. On successful connection, you can see the DataOS tables in the left panel. Select the table and click the Arrow button. 
![Image](./images/integration-spss-select-table.png)
7. You can see the fields of the selected table.
![Image](./images/integration-spss-table-fields.png)
6. Now you can explore and visualize this data in SPSS Statistics.
![Image](./images/integration-spss-table-data.png)


