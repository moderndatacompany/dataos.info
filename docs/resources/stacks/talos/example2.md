



# Talos Use Case for Financial Services
Consider a financial services company that needs to provide up-to-date customer insights to its various internal applications, AI agents, and external partner systems. These insights are derived from multiple data sources, such as customer transactions, behavior patterns, and demographic details, stored in a data lakehouse. The challenge lies in combining data from disparate systems and delivering it via APIs for consumption by internal and external stakeholders in a secure, scalable, and efficient manner.

## Setup and Initialization with Talos

Using Talos, the company’s data team can rapidly build and expose APIs based on SQL templates that query and transform data stored in their data warehouse. To set up Talos within the DataOS environment, the team must first create the Talos project folder and initialize it using Bitbucket.

### **1. Set up the Talos project folder**
Download or set up the Talos project template and initialize it using Bitbucket. Follow these steps:

- Initialize the project using Git:

    ```shell
    git init
    git add --all
    git commit -m "Initial Commit"
    ```
- Push the repository to Bitbucket:

    ```shell
    git remote add origin https://username@your.bitbucket.domain/repo.git
    git push -u origin master
    ```

    
### **2. Connect to the data source**
The data team connects Talos to the company’s data warehouse by configuring the `config.yaml` manifest file, specifying the data sources and authentication details.

Example configuration:

``` yaml
name: customer-insights
description: A Talos app for customer data
version: 0.1.6
auth:
  heimdallUrl: https://liberal-donkey.dataos.app/heimdall
sources:
  - name: customer-data-lake
    type: depot
```

### **3. Exposing APIs for Internal and External Consumption**

With Talos, the data team can create APIs for multiple datasets. For example, to build an API that provides a unified view of a customer's lifetime value by combining data from customer accounts, transaction histories, and marketing engagement data, they need to define SQL templates:

SQL template configuration
Open the apis folder, create a customer_lifetime_value.sql file, and write the SQL query to pull data from multiple sources:

sql
Copy code
SELECT c.customer_id, SUM(t.amount) AS lifetime_value
FROM customers c
JOIN transactions t ON c.customer_id = t.customer_id
JOIN marketing_engagement m ON c.customer_id = m.customer_id
GROUP BY c.customer_id;
API configuration
Update the customer_lifetime_value.yaml to define the API endpoint and configure it:

yaml
Copy code
urlPath: /customer-lifetime-value
description: Customer Lifetime Value API
source: customer-data-lake
Caching Datasets for Improved Performance
To improve performance, Talos offers caching capabilities that allow frequently accessed datasets to be stored in cache. The data team can utilize this feature to ensure quick API responses without overloading the database:

Caching dataset configuration
Add a caching mechanism within the SQL query to cache the results:

sql
Copy code
{% cache 600 %}
SELECT c.customer_id, SUM(t.amount) AS lifetime_value
FROM customers c
JOIN transactions t ON c.customer_id = t.customer_id
GROUP BY c.customer_id;
This ensures that results are cached for 10 minutes, improving the API's response time.

Data Governance and Security with Talos
The company’s data governance policies are enforced using Talos' built-in security features. For instance, the data masking feature ensures that sensitive customer information, such as personally identifiable details, is protected:

Data masking
The team can apply data masking rules based on user roles in the SQL queries:

sql
Copy code
SELECT c.customer_id, 
  CASE 
    WHEN user_role = 'admin' THEN c.sensitive_data
    ELSE '***' 
  END AS masked_data
FROM customers c;
Authentication with Heimdall
Secure access to the API is ensured by integrating Heimdall authentication, which manages the access control for various users, ensuring only authorized personnel can view sensitive data.

Scaling and Monitoring APIs
With Talos, the company can easily scale its APIs and monitor their performance:

Monitoring API performance
Talos provides built-in monitoring of API metrics through the /metrics endpoint. The data team can configure this to track API performance and ensure system health.

Scaling API services
Talos allows for scaling the number of replicas for API services by configuring the service.yaml file:

yaml
Copy code
service:
  replicas: 3
This ensures that the API can handle increased traffic from internal applications, AI agents, and external partner systems.

Conclusion
With Talos, the financial services company can rapidly develop, secure, and scale APIs to deliver timely customer insights. The caching, governance, and API monitoring features further enhance the system's efficiency and reliability, allowing the company to meet its business needs while maintaining robust security and governance practices.









