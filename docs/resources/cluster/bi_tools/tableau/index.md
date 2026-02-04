---
search:
  exclude: true
---

# DataOS Integration with Tableau

This article will help you to set up the connection between DataOS and Tableau. It provides specific steps needed to fetch data from DataOS into Tableau.

## Explore your DataOS data with Tableau

Tableau is one of the most powerful business intelligence tools which allows you to pull vast amounts of information from disparate sources, and helps you turn it into advanced visualizations. The dashboard created from these visualizations empowers you with business insights and helps in data-driven decisions.

DataOS and Tableau integration work to take advantage of that powerful visualization technology on the data pulled from DataOS.

## DataOS Connection Ports Reference

Before setting up your connection, it's important to understand which port to use based on your connection method and tool:

| Port | Protocol | Use Case | Tools/Connections |
|------|----------|----------|-------------------|
| **7432** | Trino/Presto (JDBC/ODBC) | Direct connection to DataOS Minerva/Trino engine for SQL queries | • Tableau (Presto/Trino connector)<br>• Power BI (ODBC via Simba Presto driver)<br>• SPSS Statistics (ODBC via Simba Presto driver)<br>• Any JDBC/ODBC client using Trino/Presto protocol |
| **6432** | PostgreSQL | Connection to DataOS Lens via PostgreSQL protocol | • Power BI Service (via on-premises data gateway)<br>• PostgreSQL clients connecting to Lens<br>• Tools that support PostgreSQL protocol for Lens access |
| **5432** | PostgreSQL | Standard PostgreSQL database connections | • Minerva data source connections<br>• Data Product Postgres ports<br>• Direct PostgreSQL database access |
| **443** | HTTPS | Secure web-based connections | • Databricks JDBC connections<br>• REST API endpoints (HTTPS) |
| **3306** | MySQL | MySQL database connections | • MySQL depot connections<br>• External MySQL data sources |
| **1433** | SQL Server | Microsoft SQL Server connections | • SQL Server depot connections<br>• External SQL Server data sources |

### When to Use Which Port

- **Use Port 7432** when:
  - Connecting via Tableau Desktop using Presto/Trino connector
  - Using Power BI Desktop with ODBC driver (Simba Presto)
  - Using SPSS Statistics with ODBC driver
  - Any application using Trino/Presto JDBC or ODBC drivers
  - You need direct SQL query access to DataOS catalogs

- **Use Port 6432** when:
  - Connecting to DataOS Lens via PostgreSQL protocol
  - Using Power BI Service with on-premises data gateway
  - Accessing Lens data models through PostgreSQL clients
  - Tools that support PostgreSQL protocol for Lens

- **Use Port 5432** when:
  - Connecting to standard PostgreSQL databases
  - Accessing Minerva as a PostgreSQL data source
  - Configuring Data Product Postgres ports

> 📌 **Note:** For Tableau connections to DataOS, always use **Port 7432** with the Presto/Trino connector.

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
    | Server | **Important:** Enter your DataOS server URL (e.g. tcp.reasonably-welcome-grub.dataos.io or tcp.dataos-training.mydataos.com). Do NOT use a Tableau Online URL or any other server address. The server URL should end with `.dataos.io`, `.dataos.app`, or `.mydataos.com`. |
    | Port | 7432 |
    | Catalog | e.g. lakehouse |
    | Schema | an optional field |
    | Authentication | LDAP |
    | Username | Your DataOS username |
    | Password | Your DataOS wrapped token (created in the previous section) |
    | Require SSL | Check the box |

    <center>
      <div style="text-align: center;">
        <img src="/resources/cluster/bi_tools/tableau/integration-tableau-inputs.png" alt="Inputs" style="width: 40rem; border: 1px solid black;">
        <figcaption>Inputs</figcaption>
      </div>
    </center>


3. Click Sign In.

> 📌 **Important:** 
> - The **Server** field must contain your DataOS server URL (format: `tcp.<cluster-name>.dataos.io`, `tcp.<cluster-name>.dataos.app`, or `tcp.<cluster-name>.mydataos.com`). 
> - Do NOT enter a Tableau Online URL or any other server address in the Server field.
> - The **Password** field should contain your wrapped token (not the raw API key).
> - If you encounter SSL certificate errors, see the [SSL Certificate Authentication Error](#error-peer-certificate-cannot-be-authenticated-with-given-ca-certificates) section in Troubleshooting.
> - If you encounter any other error, see the [Troubleshooting](#troubleshooting) section below.


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

## Troubleshooting

This section addresses common connection errors and their solutions.

### Error: SSL connect error - Unable to connect to Presto server

**Error Message:**
```
[Simba][Presto] (1020) Error with HTTP API at https://prod-apnortheast-a.online.tableau.com:8080/v1/statement : SSL connect error Unable to connect to the Presto server "https://prod-apnortheast-a.online.tableau.com"
```

**Cause:** This error occurs when Tableau is trying to connect to an incorrect server URL. The error message shows a Tableau Online URL (`prod-apnortheast-a.online.tableau.com`) instead of your DataOS server URL.

**Solution:**
1. Verify that you are entering the correct DataOS server URL in the **Server** field. The server URL should:
   - End with `.dataos.io`, `.dataos.app`, or `.mydataos.com`
   - Follow the format: `tcp.<cluster-name>.dataos.io`, `tcp.<cluster-name>.dataos.app`, or `tcp.<cluster-name>.mydataos.com`
   - **NOT** be a Tableau Online URL or any other server address

2. To find your correct DataOS server URL:
   - Contact your DataOS administrator
   - Check your DataOS cluster configuration
   - The server URL is typically provided during cluster setup

3. Double-check all connection parameters:
   - **Server:** Your DataOS server URL (e.g., `tcp.reasonably-welcome-grub.dataos.io`)
   - **Port:** `7432`
   - **Authentication:** `LDAP`
   - **Username:** Your DataOS username
   - **Password:** Your wrapped token (not the raw API key)
   - **Require SSL:** Checked

### Error: Invalid credentials or authentication failure

**Cause:** Incorrect username, password, or wrapped token.

**Solution:**
1. Verify that you are using your DataOS username (not email address) in the **Username** field
2. Ensure you are using the **wrapped token** (created using the base64 command) in the **Password** field, not the raw API key
3. Verify that your API key is still valid and has not expired
4. Recreate the wrapped token if necessary using the steps in the [Create Wrapped Token Using Terminal](#create-wrapped-token-using-terminal) section

### Error: Cannot find the Presto driver

**Cause:** The Presto/Trino driver is not installed or not in the correct location.

**Solution:**
1. Verify that the driver JAR file is in the correct directory:
   - **Mac:** `~/Library/Tableau/Drivers`
   - **Windows:** `C:\Program Files\Tableau\Drivers`
2. Ensure you have downloaded the correct driver version for your Tableau version
3. Restart Tableau Desktop after installing the driver
4. For Tableau 2021.3 and above, use the Trino JDBC driver (trino-jdbc-373.jar or later)

### Error: Peer certificate cannot be authenticated with given CA certificates

**Error Message:**
```
[Simba][Presto] (1020) Error with HTTP API at https://tcp.dataos-training.mydataos.com:7432/v1/statement : Peer certificate cannot be authenticated with given CA certificates Unable to connect to the Presto server "https://tcp.dataos-training.mydataos.com"
```

**Cause:** This error occurs when the Presto/Trino driver cannot verify the SSL certificate presented by the DataOS server. This typically happens when:
- The server uses a self-signed certificate
- The CA certificate is not in the Java trust store
- SSL certificate validation is too strict for the environment

**Solution:**

#### Option 1: Configure SSL Options in Tableau (Recommended for Simba Presto Driver)

If you're using the Simba Presto driver (Tableau 10.0-2020.2 and below):

1. In the Presto connection dialog, look for an **Advanced** or **SSL Options** button/link
2. Click on it to open SSL configuration options
3. Look for options such as:
   - **Verify SSL Certificate** - Uncheck this option to disable certificate validation
   - **SSL Mode** - Set to a less strict mode if available
4. Save the settings and try connecting again

#### Option 2: Configure Custom Properties (For Trino JDBC Driver)

If you're using the Trino JDBC driver (Tableau 2021.3 and above), you may need to configure custom connection properties:

1. In the Presto connection dialog, look for an **Advanced** or **Custom Properties** section
2. Add the following custom properties to disable SSL certificate validation:
   ```
   SSLVerificationMode=NONE
   ```
   Or:
   ```
   SSL=true
   SSLVerificationMode=NONE
   ```

#### Option 3: Add CA Certificate to Java Trust Store

If your organization requires certificate validation, you can add the DataOS CA certificate to the Java trust store:

1. Obtain the CA certificate from your DataOS administrator
2. Import the certificate into the Java trust store used by Tableau:
   
   **For Mac:**
   ```bash
   keytool -import -alias dataos-ca -file /path/to/dataos-ca.crt -keystore "$JAVA_HOME/lib/security/cacerts" -storepass changeit
   ```
   
   **For Windows:**
   ```cmd
   keytool -import -alias dataos-ca -file C:\path\to\dataos-ca.crt -keystore "%JAVA_HOME%\lib\security\cacerts" -storepass changeit
   ```
3. Restart Tableau Desktop after importing the certificate

#### Option 4: Use Connection String with SSL Parameters

If Tableau allows custom connection strings, you can try:

1. In the connection dialog, look for an option to enter a custom connection string
2. Use a connection string format like:
   ```
   jdbc:trino://tcp.dataos-training.mydataos.com:7432/lakehouse?SSL=true&SSLVerificationMode=NONE
   ```

> ⚠️ **Security Note:** Disabling SSL certificate validation reduces security. Only use this option if:
> - You're in a trusted internal network
> - Your organization's security policy allows it
> - You've verified the server identity through other means
> 
> For production environments, prefer adding the CA certificate to the trust store (Option 3).

### Error: Connection timeout

**Cause:** Network connectivity issues or firewall blocking the connection.

**Solution:**
1. Verify that your network connection is active
2. Check if your firewall or network security settings are blocking connections to the DataOS server
3. Verify that port 7432 is not blocked by your network firewall
4. Try connecting from a different network to rule out network-specific issues
5. Contact your network administrator if you suspect firewall restrictions

### General troubleshooting steps

If you continue to experience connection issues:

1. **Verify your connection parameters:**
   - Double-check the Server URL format and ensure it's your DataOS server, not a Tableau Online URL
   - Confirm the Port is set to `7432`
   - Verify Authentication is set to `LDAP`
   - Ensure Require SSL is checked

2. **Test your wrapped token:**
   - Verify the token was created correctly using the base64 command
   - Ensure the token is on a single line (no line breaks)
   - Recreate the token if you're unsure

3. **Check driver installation:**
   - Verify the driver file is in the correct location
   - Ensure you're using the correct driver version for your Tableau version
   - Restart Tableau after driver installation

4. **Contact support:**
   - If the issue persists, contact your DataOS administrator with:
     - The exact error message
     - Your Tableau version
     - Your DataOS cluster name
     - Screenshots of the connection dialog (with sensitive information redacted)
