


Why adopt MML?
Challenges that MML can solve
Key considerations for MML
What all scenarios where you consider using MML
Best Use case
How MML works?
    Compnents
    How to set up MML





The story flow of this article is (THIS SECTION IS FOR INTERNAL CONSUMPTION ONLY) 

What is preventing the usage of existing data platforms by business and non-technical users ?  

What have we done in DataOS to make it usable by everyone? What did we introduce to abstract out the technical protocols and need for programming languages ?  

How can users with even limited SQL skills make the most of DataOS ? 


In a data-driven business world, for many organisations, a state-of-the-art data and analytics platform is no longer an option but a necessity. These platforms act as a central repository for enterprise-wide data and empowers businesses to translate data into business value. Over the last decade, these organisations have invested a lot in building best data platforms but have often failed in achieving true value from their data at rapid pace. One of the primary reasons for this is that the business users always depended on Technical teams for data because the data platforms demand programming and niche technical expertise. 

 

While building DataOS, we had one core agenda in mind - it should be used intuitively by a wide range of users. This means DataOS should make it possible for all users to easily discover and analyze data within the platform, understand the context associated with data, such as column descriptions, history and lineage and derive insights from data with minimal dependencies on the data or IT team. 

 

Data processing made easy with DataOS 

Executing data processing jobs has remained a nightmare for data engineers and with DataOS we wanted to simplify this. To achieve this we have built our own data processing engine called ‘Rio’. DataOS® Rio allows data engineers to ingest both batch and stream data processing. Rio Flare is a library that simplifies writing and executing ETL jobs and is built on top of Apache Spark.  

 

Typically when you use spark, in data processing, you need to write programs in a programming language like Python,Java or Scala. This requires users to have prior knowledge of one of these programming languages. In DataOS, we have abstracted out the programming interface and turned it into declarative. Flare allows you to declare your Transformation steps in simple YAML configuration files and then runs it on DataOS® managed Spark Cluster.  

 

Example : For a data ingestion job users can simply declare the source system from where the data needs to be read, transformation logic in simple SQL syntax and final destination where the data needs to be written. DataOS Flare abstracts out all the complexities related to different storage system protocols and performs the job for you. 

 

 

Screenshot showing details of input, output and steps in a sample data ingestion flare job 

 

So, essentially, we have tried to take out programming languages as a necessary skill and made things easy by introducing SQL as the only required skills for users. Contrary to earlier, users can now work on Spark if they are equipped with SQL, which many users are comfortable with. 

 

Data ingestion made easy with DataOS 

One of the core pain points for data engineers during data ingestion is to ingest data from varied data storage systems. They need to learn and understand the underlying protocols of these systems and deploy these ingestion jobs as per the pre-configured protocols. Organisations these days, store data in multiple sources in varied formats. Now, imagine the time these data engineers spend on understandingRemember, we said that we have abstracted out the need for programming languages while writing data processing jobs, similarly we have abstracted out the concept of varied storage protocols for different storages. Let me explain it with an example.  

 

Organisations store data in Redshift using it as DataWarehouse, BigQuery, S3 as blob storage or Snowflake. Now all of these storage systems have different storage protocols, as in how can we query data from these storage systems. What we have essentially done with DataOS is, we have thoroughly understood the underlying technologies and protocols behind these storage systems and created one standard SQL way for users, so that they can query and access data from multiple data source systems. In DataOS, we have made this possible by introducing DataOS ‘Depots’. 

 

More about DataOS Depots 

DataOS depots enable Data Engineers to write data ingestion jobs irrespective of the source data storage systems. Depots abstract out the challenge of accessing data stored across varied storage systems. Depots contain connection details about the data source and destination systems and the information about the type of data storage systems. Depots encapsulates the complexity and surfaces a simple dataset address and users can access their data using SQL. Backend protocols pertaining to data accessibility of that source system becomes immaterial now.  

 

From an end user point of view, accessing a kafka topic or data from a big query table is one and the same. The back end technical protocols of these two will be abstracted and taken care of by DataOS depots. In the next section, let us briefly understand about SQL workbench that brings in immense data capabilities into DataOS. 

 

DataOS workbench 

DataOS Workbench is a SQL based query engine and allows data analysts to write complex SQL queries for managing, manipulating and analysing data in the database. Data analysts can use DataOS workbench to connect to multiple data sources and process SQL queries at rapid pace and scale. DataOS Rio(our inhouse data processing engine) handles these SQL queries to create tables or views. It is simple and easy to use.  

 

Want to query your data but not proficient at writing long SQL queries? It is no longer a problem with DataOS. Business users can use SQL studio which is a visual query builder and build even complex queries visually via drag-and-drop even without writing queries. Users need to just select which data you want to get, apply necessary functions and aggregations to them, configure sorting and filtering, and that’s all.  All of these can be done using an intuitively built user interface (UI), and users won’t need to type even a single line of code. How cool ! 

 

 

 

Conclusion 

 

Nowadays, almost all data teams are overwhelmed with data requests. They spend sleepless nights trying to make disparate data sets talk to each other, building and maintaining data pipelines, solving data quality and accessibility issues all by themselves. DataOS is one platform that is designed to make the life of data teams easy. DataOS’s intuitive and extensive features encourage users, irrespective of their technical and programming abilities, to experiment with their data. This reduces dependency of business teams on Data teams and improves time to insight drastically. 

 

Along with many inbuilt features, DataOS also comes with a swift data processing engine and powerful workbench which require a minimal learning curve. Over the past 12 months, we’ve been working very closely with our beta customers to understand their data goals and showed them how DataOS can help them achieve data goals within 3-6 months. If you’d like to experience your data in a whole new way, manage it and extract value out of it at a rapid pace, email us at hi@tmdc.io or visit us at themoderndatacompany.com 

Discovery Calls with Potential Customers 

 

PRIMARY GOAL 

Gather information related to the customer’s data goals and data ecosystem so that we can come up with insights around their data needs and offer solutions. 

 

APPROACH 

Business Goals  ->  Data Goals  ->  Data Needs  ->   Solutions  ->  Capabilities enabled by DataOS  ->      Features in DataOS 

The Business Goals are the CEO-level goals. 

The Data Goals are the CIO-level goals which when accomplished contribute to their Business Goals. 

The Data Needs are the insights that we need to figure out which when solved will help the customer accomplish their Data Goals. 

For the customer to consider our solution to the data Needs as valuable, the solution to the needs to either 

Meet the Data Needs in a way that is both considered as valuable (faster, cheaper, comprehensive) by the customer and is better than the alternatives, OR 

Make new Data aspirations possible, OR  

BOTH 

  

 

Page Break
 

QUESTIONS 

High-level Goals of the Customer 

What are some of your Business’s goals that you are trying to contribute to? 

So that we can understand their Business Goals. 

Some goals we have seen in enterprises 

Be prepared for Volatility - New ways of doing business – to adapt to changing market conditions – user behavior, competition, new entrants. 

Enhanced User Experience - understand them better – to retain customers 

Automation – business processes automation - to reduce costs and improve accuracy 

Real Time or near-real time insights – to react to critical events on-time. 

Course Correction 

What are the technology/data goals that you are  trying to achieve? 

So that we understand their Data Goals. 

Some goals we have seen in enterprises 

Infrastructure agility  

Real-time insights 

Observability – data pipes and security & governance 

Multi-cloud security 

Governance 

Insights democratization (Shifting power of data/insights from IT to Business users) 

Enable experimentation / fail fast 

Data freedom - ability to move data across org freely 

Inefficiencies with Current Situation 

What is the status quo way of achieving the Data goals? 

So that we understand their current data ecosystem and how we can position ourselves to be perceived as a better solution. 

What are the known shortcomings in the status quo? With few follow up “5 Why” questions. 

So that we can understand what they consider valuable. 

From a data ecosystem readiness point of view, how much time/effort/cost did/would it take:  

to achieve GDPR compliance? 

to integrate an acquired company/brand? 

to get a 360 view of your customers? 

to move data to an external system without getting into data privacy issues? 

to handle peak season data traffic? 

to resolve data quality issues?   

to support near real time use cases?  

to implement governance on Data lake? 

to solve data discoverability issues for all the data assets stored in different systems? 

to monitor data pipelines? 

to define and manage SLAs (quality, availability, performance, security, and cost-effectiveness)? 

to manage incidents related to data movement and data management and alert stakeholders? 

to create compute clusters on demand for varied data processing/querying needs? 

to version control data artifacts? 

to deploy, track and monitor ML models in production? 

to build consensus on definition and calculation of key business metrics? 

To evolve data partitioning strategy on the fly to improve query performances of data consumers? 

 

For each of the above questions, how would the responses be viewed as in your organization - ? 

Unacceptable 

Should be improved 

Acceptable 

Importance of the problem to the customer 

What alternatives did you consider? 

So that we know this is an important goal for them relative to their other goals. 

Did you try some of the alternative solutions? 

So that we know they’ll put some money/time/effort in trying out our product. 

Why did the alternative solutions not satisfy your needs? 

So that we can understand what they consider valuable – faster, cheaper, comprehensive. 

How did you find out about these alternatives? 

So that we know how to reach our potential customers. 

Customer’s willingness and ability to pay 

How do you see budget getting allocated to solving these problems – new spend or able to retire existing spend? 

So that we understand there will be able to pay for the solution as per our expectations. 

Follow Up 

Who else in your organization should we talk to so we better understand how we can solve your needs? 

So that we get more calls and better understanding of their needs. 

How does the approval process work and who are involved in the process? 

So that we know who else need to be involved in the Sales process. 

Who else in your organization should we talk to for follow up questions that came out of this conversation? 

So that we get clarifications on unanswered questions. 

 

Page Break
 

PRODUCT – DataOS 

DataOS (Data Operating System) is a comprehensive data platform that abstracts out the entire complexities of data engineering by productizing it so that as a business, you can focus on driving value from data instead of managing data. 

Status quo at several companies is that they are spending lot of time and money on data wrangling than on how to use the data. 

DataOS provides entire data management in one product – everything from data ingestion, data governance, data quality, operationalizing data, data discoverability. 

Current alternatives to get the capabilities provided by DataOS are very suboptimal. The most common available alternative is: 

Custom build data ecosystem to power the data needs from ground-up by going to an SI (Accenture, Deloitte, etc.), taking a reference architecture, picking multiple vendors of point solutions for ingestion, catalog, quality, governance, processing. 

These tools are built on different and old stacks that limits their capabilities and integration with other tools. 

Sum of all these parts results in a very rigid architecture. 

Inefficiencies experienced 

Integrate Snowflake on top of existinf infrastructure would take a year. 

Moving away from Snowflake to Redshift would take 2 or 3 quarters. 

Data movement from Teradata on-prem to Teradata Cloud takes 2 years. 

Spend millions of dollars in license fees for Snowflake, PowerBI, Alteryx, etc. and not able to take advantage of the functionalities of those products. 

Creating each BI report/dashboard takes X weeks. 

 

 

The main gap in the market is that the customers of the companies are expecting experiences that can be provided only with an agile and modern data ecosystem but companies do not have a way to achieve it with the status quo and available alternatives. 

The rigidity of the data ecosystem and infrastructure that hinders the companies to adapt to dynamic business environment is the key problem that is solved by DataOS. 

DataOS gives enterprises an agile data infrastructure and future-proofs their infrastructure for next 5-10 years. 

 

 

DataOS 

CapabilitiesFeatures 

FeaturesCapabilities 

 

 

Data Management 

Data interface to access data that is residing in different systems in the organization – relational, non-relational, streaming, and object data stores. (Depots) 

Simplification of Data engineering effort by providing re-usable and version-controlled constructs. (Declarative Artifacts) 

Flexible data warehousing capability by providing ACID-compliant Data Lake based on Open Data formats. (Icebase) 

 

 

Data Processing 

Ability to process (transform, enrich) data with different volume, velocity needs – stream, batch, stateful & stateless computation. 

Orchestration engine to deploy, monitor, schedule, or trigger sophisticated data pipelines. (Workflows) 

 

 

Data Exploration 

Holistic view of all the data in the organization, their relationships and their usage. (Datanet) 

Ability to query data from across multiple databases using single SQL interface. (Workbench) 

Ability for users with no/minimal SQL expertise to access datasets through GUI. (Workbench - Studio) 

Ability to create on-demand compute clusters for recurring and critical queries for applications such as Dashboards. 

 

 

 

Data Activation 

Sending data to external systems (such as Salesforce) to achieve reverse-ETL. (Syndication) 

Sharing of datasets to enable secure access from external applications using UDLs (Universal Data Link). 

Ability to create data-powered applications end-to-end including GUI, processing, storage, dashboard. 

Ability to create REST APIs on demand (conceptually similar to GraphQL), and a runtime for fulfilling request on these APIs on the datasets stored in DataOS. 

Ability to define and track business KPIs in a consistent manner through MML paradigm; common vocabulary for entities and relationships (Model), map them to data sources (Map) and get data (Load). 

 

 

Data Governance 

Ability to govern and secure data at highly granular level through ABAC (Attribute-based access control); such as row-level redaction and column-level masking. 

Visibility for InfoSec team to sensitive data (such as PII) being accessed across the organization to enable data privacy compliance. 

 

 

APPENDIX 

Tips from the book: THE MOM TEST 

Tips: 

Talk about their life instead of your idea. 

Ask about specifics in the past instead of generics or opinions about the future. 

Talk less and listen more. 

Rules of Thumb when framing questions: 

Opinions are worthless. 

Anything involving the future is an over-optimistic lie. 

People will lie to you if they think it’s what you want to hear. 

You're shooting blind until you understand their goals. 

Watching someone do a task will show you where the problems and inefficiencies really are, not where the customer thinks they are. 

If they haven't looked for ways of solving it already, they're not going to look for (or buy) yours. 

People stop lying when you ask them for money. 

While it’s rare for someone to tell you precisely what they’ll pay you, they’ll often show you what it’s worth to them. 

In a B2B context, know where the money comes from 

Whose budget the purchase will come from 

Who else within their company holds the power to torpedo the deal. 

People want to help you. Give them an excuse to do so. 

"Who else should I talk to?" 

"Is there anything else I should have asked?" 

Hero Section 

The Modern DataOS Platform  

Option A:  The connective tissue for ALL your data infrastructure 

Option B:  A fully-integrated platform that allows you to programmatically manage and operationalize all your legacy and cloud data. 

Option C:  The connective tissue for your data, ML and analytics infrastructure 

Option D:  An operating system to power your entire data lifecycle. 

Option E : DataOS is the operating system for a new generation of data,ML and analytics infrastructure.  

DataOS is the operating system powering a new generation of data and analytics infrastructure. It is the connective tissue between your legacy and cloud data sources delivering quality, governed, secure and reliable data in real-time. Democratize and simplify access to data and insights for technical and business users in your team with DataOS. 




DataOS policies allow organizations to authorize users, employees and third parties to access company data in a manner that meets security, privacy and compliance requirements.

 
Access Policy  

Access policy is a security measure which is put in place to regulate the individuals that can view, use, or have access to a restricted DataOS environment/resource.A This is implemented by tags. For example a user with a tag 'operator' can access secrets or specific Depots to connect to data. 
 

Data Policies  

These policies are global policies available in the system which contains all the column level policy. Using these policies, you can:
Mask the data or 
Filter the data.  

Masking and filtering strategies can be defined in the YAML files. For example, PII data can be shown with appropriate mask, replacing with "####" string or with some hash function. You can filter the data based on tags such as some users can not see ' Florida' region data.  

The following examples show what the masked data might look like after the masking policy is applied.
Type     Original Value   Masked Value
Email ID abc.ef@gmail.com - bkfgohrnrtseqq85@bkgiplpsrhsll16.org
SSN 987654321 867-92-3415
Credit card number 8671 9211 3415 4546 #### #### #### ####

A data catalog is an organized inventory of data assets in the organization. It uses metadata to help organizations manage their data. This metadata helps in data discovery and governance. 

CTA: Schedule a Demo 

< Infographic here>  

 

Business Value from DataOS  

 

Benefit 1:   Secure Data Sharing  

Benefit 2:  Data fit for purpose  

Benefit 3:   Data Democratization 

Benefit 4:   Trusted and Reliable Data  

Benefit 5:   Built in governance and security 

Benefit 6:   Automation and Speed  

 

DataOS Capabilities  

One Platform for all your data activities  

Data Management 

The DataOS seamlessly connects to all your source and sink systems and transform and curate data with our model-based low-code declarative artifacts. ACID-compliant data lake enables teams to store structured, unstructured and streaming data. Out-of-the-box data quality and profiling functionality lets you get quality and trusted data without additional processing. Leverage our observability principles to create robust alerts across the data lifecycle.  

Data Exploration - 

DataOS’s Datanet creates a connective tissue between all your data systems continuously adding usage-based intelligence to your data. Easily Discover, search and find trusted and context-aware data. Understand the journey, relationships and impact of your datasets and make decisions with confidence. DataOS also has powerful workbench that lets you query datasets with simple SQL queries.   

Data Activation 

Activate your data and share it across your enterprise. DataOS lets you create customized reports on any datasets in minutes, share and collaborate on them securely. Build trigger alerts and notifications to 10+ destinations including ServiceNow, Jira, Pager Duty, Slack, MS teams, Pager Duty etc. Consume your shared data from SaaS systems like salesforce, zendesk, google ads etc 

Data Products 

Build and launch new data products faster.  DataOS handles all the infrastructure needed  - Run,host,store,process,sync,serve  to build your data application so teams can focus on innvoation. 

Governance & Security 

DataOS’s Tag-based governance enables flexible and granular policy creation that gives teams an automated and scalable way to ensure governance and compliance for data within your ecosystem. Attribute-based access control future-proofs your org and lets it adapts to changing and new compliance regulations. Easy-to-create access and Data policies let you control, track and audit access to data. Row-level filtering and column masking give you granular control of what data authenticated users can access. Advanced primitives like data masking, data abstraction and differential privacy ensure your teams are working with trusted data at all times.  

Data Sharing 

Share data easily across your business ecosystem without copying or moving data. DataOS’s best in class governance enables you to control access in a secured and auditable environment. Share data and collaborate with customers, internal and external partners to unlock newer and richer insights. 

Data Modeling 

DataOS’s foundational MML(Map-ModelModel-Map-Load) architecture brings a declarative model-first approach to pipeline creation. It abstracts away the complexity of pipeline building.  MML makes it easy to build and manage data pipelines helping data engineering teams to streamline and simplify their ETL processes.  

 

Principles of DataOS 

Model First Engg                                   

Abstract away the complexity of data engineering with our model-based approach to building pipelines. Give the control back to business decision makers to get to their insights – faster and easily.  

DataOps-friendly                      

Cloud native and agnostic and agile-friendly adopting the principles of DevOps and DataOps. 

Observability 

Data observability, with visibility into any anomalies encountered in permissions, roles, policies, or movement of data 

 

Use cases 

Data Engineering - Automate and simplify Data Engineering tasks thru MML (Map-Model-Load).  With our declarative model-first pipeline creation, engineering teams can streamline their ETL processes leaving them free to focus on value-add features.  

Data Governance - Deliver governance and security for all your data from a single, centralized platform. Future-proof your enterprise for governance and compliance requirements with Attribute-based access control. Easy setup of policies to control, observe and audit who and what data they are accessing.  Build confidence in your insights by delivering trusted data to your teams.  

Data Discovery  -   Discover data, understand the lineage, relationships and impact of your data. Remove barriers to data access for your business decision makers. Empower you technical and business teams with quality and contextual data  

Data sharing & collaboration – Collaborate and share data with your internal systems and stakeholders and your external partner ecosystem and customers in a secure, governed and auditable fashion.  Share datasets in real time without creating copies or moving it. Unearth richer insights and unlock powerful new use cases by sharing your data within your enterprise and your external partner ecosystem and customers.  

Data Observability  

Complete data observability into all your data activities from production to consumption of data, to access and sharing of data including events, metrics and logs  

 

 

 
 

   

 