DataOS Interfaces empower your data journey by offering powerful tools for efficient data operations and seamless collaboration. It gives you the flexibility of the CLI or the intuitive experience of the GUI, enabling self-service data management. Let's explore these interfaces and their capabilities:

## CLI (Command-Line Interface)

The DataOS CLI provides a command-line environment for efficient and streamlined data operations. With the CLI, you can interact with DataOS through text-based commands, create and manage resources, and perform various data management tasks. It offers flexibility and control for administrators and data engineers who prefer working from the command line.

## GUI (Graphical User Interface)

The DataOS GUI offers an intuitive interface where you can access a suite of applications tailored to different data-related tasks and personas. Explore, analyze, and collaborate with ease, empowering your data journey.

The homepage of DataOS GUI will show you all the apps currently available for use:

![dataos_homepage.png](interfaces/dataos_homepage.png)

Each DataOS app within the GUI has unique capabilities:

### **Atlas**
An in-built BI solution to create visualizations, reports, and dashboards for powerful data storytelling and actionable insights. From the Atlas interface, you can manage queries, create snippets, set up alerts, and more.

### **Audience**
Understand your customers by leveraging semantic data models built via Lens for customer segmentation and data-driven decisions.

### **Bifrost**
Take control of access policies for applications, services, people, and datasets to ensure secure and compliant data access. Bifrost leverages the governance engine of DataOS, Heimdall, to ensure secure and compliant data access through ABAC policies,  giving users fine-grained control over the data and resources.

### **Lens**
Access and model data from diverse sources, create meaningful relationships between business concepts, define measures, and KPIs for data-informed decision-making.

### **Metis**
Discover, catalog, and observe enterprise data with comprehensive metadata management, providing technical and business context.
### **Notebook**
Leverage the power of Jupyter Notebook on DataOS for data science projects, coding, analysis, and communication of insights.

### **Operations**
Monitor and administer DataOS platform activity, gaining real-time visibility into resource utilization, cluster performance, and user activities. Keep your data ecosystem running smoothly and optimize resource allocation.

### **Workbench**
Explore and query your data assets using SQL with Workbench. Powered by the Minerva query engine (built on top of Trino), Workbench supports both simple and complex queries across a large variety of data sources, including traditional relational databases (Oracle, PostgreSQL, Redshift, etc.) as well as other data sources such as S3, Kafka, and Pulsar. You can query and explore data from these data sources without bringing it to DataOS.

From the DataOS homepage, you can also manage your profile, access tokens, and view all the depots that exist within the DataOS instance for accessing data.

## Manage Profile

![profile.png](interfaces/profileinfo.png)

## Create Tokens

API keys/tokens are used to authenticate requests to  DataOS resources. For example, when calling a service endpoint, you need to supply a valid API token in the HTTP `Authorization` header, with a valid token specified as the header value. You can generate API keys/tokens from DataOS UI as well as using DataOS CLI commands.

To learn more, refer to [Creating API Keys and Token](interfaces/create_token.md)

## View Depots

![Depot](interfaces/depots.png)

