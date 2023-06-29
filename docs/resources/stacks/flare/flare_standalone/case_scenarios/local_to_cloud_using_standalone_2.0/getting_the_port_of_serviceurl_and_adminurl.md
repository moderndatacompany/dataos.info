# Getting the Port of Service and AdminUrl

---

[Getting Started](https://www.notion.so/Getting-Started-DataOS-Documentation-1933e853addf4dc398814205d3948808?pvs=21)         [About DataOS](https://www.notion.so/About-DataOS-fc3287a179514b7ba846c12f18875f5c?pvs=21)         [Versions](https://www.notion.so/Versions-d70d557cf10c4c6fa55cd94089b0fd71?pvs=21)         [FAQs](https://www.notion.so/FAQs-a973bc1d466544589d865312cf7eea93?pvs=21)         [Contact](https://www.notion.so/Contact-c536fdcfbd8f4db78e0310fd46751b66?pvs=21)         [Glossary](https://www.notion.so/Glossary-8f34d8c84d4345cfb53194e9f0c8d9e8?pvs=21)

---

<aside>
📘 Content Structure

## [Overview](https://www.notion.so/Data-Management-Capabilities-14fe7dd7cef04cf3811ac8ca5211f03b?pvs=21)

### [CLI](https://www.notion.so/CLI-d5ae36a14d7a49d880f938e263c117ef?pvs=21)

[Installation](https://www.notion.so/CLI-d5ae36a14d7a49d880f938e263c117ef?pvs=21)

[Command Reference](https://www.notion.so/CLI-d5ae36a14d7a49d880f938e263c117ef?pvs=21)

### [GUI](https://www.notion.so/GUI-25f333328a0c4216a64ef540ee27487b?pvs=21)

[Apps](https://www.notion.so/GUI-Applications-57d6b4a3effa428d88a9780a23945482?pvs=21)

[Profile](https://www.notion.so/GUI-25f333328a0c4216a64ef540ee27487b?pvs=21)

## [Integration](https://www.notion.so/Integration-Ingestion-b0fd465bb2ed454ba764a55d514d518b?pvs=21)

### [Depot](https://www.notion.so/Depot-608f5f71991947e4bfa62772bba34e33?pvs=21)

- [Create Depot](https://www.notion.so/Create-Depot-d0b2b9f669eb457dafbff9094f2bada9?pvs=21)
- [Depot Config templates](https://www.notion.so/Depot-Config-Templates-10ea889c10534b4f978bdf4224a0319c?pvs=21)

### [Airbyte](https://www.notion.so/Airbyte-e61602710663453bb06af303c358fde6?pvs=21)

- [How Airbyte Works](https://www.notion.so/How-Airbyte-Works-7711dd530e64481dbd86a415ee1356bc?pvs=21)

### [Rclone](https://www.notion.so/Integration-Ingestion-b0fd465bb2ed454ba764a55d514d518b?pvs=21)

### Scanner

- [Creating Scanner Workflow](https://www.notion.so/Creating-Scanner-Workflow-7183dfe8dbf84f60910dbee7c873c6d5?pvs=21)
- [Creating Depot Scan Workflow](https://www.notion.so/Creating-Depot-Scan-Workflow-e322c77cdfa24958955e8c6aa7e89704?pvs=21)
- [Template for Depot Scan](https://www.notion.so/Templates-for-Depot-Scan-9bb651b4df2b4b6cbf4a6f142896491a?pvs=21)
- [Creating Non-Depot Scan Workflow](https://www.notion.so/Creating-Non-Depot-Scan-Workflow-cfed4a72c12148d98ad518e280d6b387?pvs=21)
- [Templates for Non-Depot Scan](https://www.notion.so/Templates-for-Non-Depot-Scan-16de0c454050468786e2d37a5e8d1d1f?pvs=21)
- [Data Profile Scan](https://www.notion.so/Data-Profile-Scan-f24606bc3bec49609616a559a7f93c01?pvs=21)
- [Data Quality Scan](https://www.notion.so/Data-Quality-Scan-440fc4cbc43b4ca8a15c97ec224cb043?pvs=21)
- [Query Usage Data Scan](https://www.notion.so/Query-Usage-Data-Scan-631fa20bd8ab446fb44bc374135aaa0e?pvs=21)
- [Workflows Data Scan](https://www.notion.so/Workflows-Data-Scan-df2fe420e04744f0bdc9e2aaf331a462?pvs=21)
- [Users Data Scan](https://www.notion.so/Users-Data-Scan-WIP-dbe9e26ab3604f919a6ce44a2b2d6a1f?pvs=21)
- [Scanner Workflow Related Errors](https://www.notion.so/Scanner-Workflow-Related-Errors-1b81c2a52c0d47ff9c00db83b1247045?pvs=21)

### [External Tools](https://www.notion.so/Integration-Ingestion-b0fd465bb2ed454ba764a55d514d518b?pvs=21)

[Power BI](https://www.notion.so/Power-BI-7ec27a7779004ea295c98c0303dce00e?pvs=21)

[Tableau](https://www.notion.so/Tableau-89980548c0d641e19c2ba584516a6f90?pvs=21)

[SPSS Statistics](https://www.notion.so/SPSS-Statistics-766499e3d73c4758a1f594f52cf9ccab?pvs=21)

[Hightouch](https://www.notion.so/Hightouch-c2cb3aa0ab6d4c02b95140ac50227fff?pvs=21)

## [Storage](https://www.notion.so/Storage-a44aedf79d904e96b8829f21fb4c5838?pvs=21)

### [Icebase](https://www.notion.so/Icebase-e17343411fd04cd69d261b1809238031?pvs=21)

- [Case Scenario: Creating and Getting Dataset](https://www.notion.so/Case-Scenario-Creating-and-Getting-Dataset-0cca0fe044b34b399d5479085f3d5a72?pvs=21)
- [Case Scenario: Table Properties](https://www.notion.so/Case-Scenario-Table-Properties-51b8c15d68784a27834ad12732916ae0?pvs=21)
- [Case Scenario:  Schema Evolution](https://www.notion.so/Case-Scenario-Schema-Evolution-9d155abf09ff4d03a4277ac8e225d7d6?pvs=21)
- [Case Scenario: Partitioning](https://www.notion.so/Case-Scenario-Partitioning-66989b931eed49f3952f0457783f529b?pvs=21)
- [Case Scenario: Maintenance](https://www.notion.so/Case-Scenario-Maintenance-Snapshots-and-Meta-Data-Listing-c259a31095284804b5200f67b756202c?pvs=21)

### [Fastbase](https://www.notion.so/Fastbase-cb9bc4f6dda94bd6b0d5bf3c1c510b26?pvs=21)

## [Transformation](https://www.notion.so/Transformation-92deba38f2884f5cb2384f9569899dd3?pvs=21)

### [Workflow](https://www.notion.so/3e4fc6c9379d4e078b6230a80785135e?pvs=21)

- [Executing Multiple Workflow YAMLs from a Single One](https://www.notion.so/4670aedf14ac4afeb106117559884e18?pvs=21)
- [Scheduled or Cron Workflow](https://www.notion.so/828466c24e144533b8d2209921fe2471?pvs=21)

### [Flare](https://www.notion.so/Flare-1da91bc8e6eb4d259cea243a497c14f5?pvs=21)

- [Basic concepts of Flare Workflow](https://www.notion.so/Basic-concepts-of-Flare-Workflow-e34353de80534694956c9cc48997a8b1?pvs=21)
- [Building Blocks of Flare Workflow](https://www.notion.so/Building-Blocks-of-Flare-Workflow-70968f528eda4483b4248700978c073d?pvs=21)
- [Flare Functions](https://www.notion.so/Flare-Functions-c0e4d8dcd03842c89b5207841eddca5a?pvs=21)
- [Create your first Flare Workflows](https://www.notion.so/Create-your-first-Flare-Workflow-b6c1125afccb4420a8cf88428a30be80?pvs=21)
- [Flare Standalone](https://www.notion.so/Flare-Standalone-07c0745a11b248d8949b9e4474d1c6cc?pvs=21)
- [Flare Optimizations](https://www.notion.so/Flare-Optimizations-2a0dd46789104bca9fcd0ded1773d7bb?pvs=21)
- [Flare Read/Write Config](https://www.notion.so/Flare-Read-Write-Config-f248739b7bdb484d87a3d171b7a71e08?pvs=21)
- [Case Scenario](https://www.notion.so/Case-Scenario-ed6a5030ff804fe8913af1f113b907e8?pvs=21)

### [Service](https://www.notion.so/Service-24c459b799724f29b33c76f00b8534fd?pvs=21)

### [Benthos](https://www.notion.so/Benthos-6c68336b26f644ea886026095fdbdfa2?pvs=21)

- [Twitter Data Processing](https://www.notion.so/Benthos-Twitter-Data-Processing-8e66699c834c4b13b2fb0aba53132dc4?pvs=21)
- [Stock Data API](https://www.notion.so/Benthos-Stock-Data-API-7784b99be6794c639c5a3caf2c204289?pvs=21)
- [Pulsar- DataOS](https://www.notion.so/Benthos-Pulsar-DataOS-019753f0f2204b54aaf075497b324d83?pvs=21)

### [Surge](https://www.notion.so/Transformation-92deba38f2884f5cb2384f9569899dd3?pvs=21)

## [Ontology](https://www.notion.so/Ontology-174a3d1ae7b346e5888a108a9e8ade73?pvs=21)

### [Metis](https://www.notion.so/Metis-835717e50489474b8440959fec63a4aa?pvs=21)

[Metis Features](https://www.notion.so/Metis-Features-51bbdeeec22b49798ef32bd1c1b1c24f?pvs=21)

[Architecture](https://www.notion.so/Architecture-cc8895ca95444076ac81f3b1a2d23eed?pvs=21)

[Metis UI](https://www.notion.so/Metis-UI-f3a402e2791d4db08d32a061bdbedc9f?pvs=21)

### [Lens](https://www.notion.so/Lens-fa08c2576c054c0e9b4b2d3b09eb8720?pvs=21)

- [Lens: Right-to-Left Data Engineering Approach](https://www.notion.so/Lens-Right-to-Left-Data-Engineering-Approach-5d572d5f0dd14be6b259de4c03206e36?pvs=21)
- [Getting Started with Lens](https://www.notion.so/Getting-Started-with-Lens-23a88cb1fe10416d971f99a78c4e6498?pvs=21)
- [Lens Query](https://www.notion.so/Lens-Query-9315a46912f041b08f082b8eccb7c01f?pvs=21)
- [Elements of Lens](https://www.notion.so/Data-Elements-674a81a94b7b4cd9b24899aa455c2806?pvs=21)
- [Lens Ecosystem](https://www.notion.so/Lens-Ecosystem-c2bf510553ef47f78c6dd38a1a893fff?pvs=21)
- [Recipes](https://www.notion.so/Recipes-fe3c302e43cc4df996692c2bd77b03ee?pvs=21)

### [Odin](https://www.notion.so/Knowledge-Graphs-04540d88bfae4bed8d518279e9c8d6ef?pvs=21)

### [Hera](https://www.notion.so/Hera-08459d9a06a6494c8c8342d82e6c6773?pvs=21)

### [Open Data Contracts](https://www.notion.so/Ontology-174a3d1ae7b346e5888a108a9e8ade73?pvs=21)

## [Analytics](https://www.notion.so/Analytics-209caee9018645008d44685e5c6d7e64?pvs=21)

### [Minerva](https://www.notion.so/Minerva-ac1e53d7680543cd942a914892bebd0e?pvs=21)

- [Architecture Overview](https://www.notion.so/Architecture-Overview-4911a2b8ddbd40b79f58bdf11bb72b16?pvs=21)
- [Cluster Tuning](https://www.notion.so/Cluster-Tuning-549fb7089f37488d968fea2db016c015?pvs=21)
- [Cluster Configuration Scenarios](https://www.notion.so/Cluster-Configuration-Scenarios-f33f39d797c640a8a522cce7cb3a482e?pvs=21)
- [Performance Tuning](https://www.notion.so/Performance-Tuning-f46833cfcf5c48a89be2ed06089b6626?pvs=21)
- [Connectors Configuration](https://www.notion.so/Connectors-Configuration-90d00deb7c614052899efebb159ffeb7?pvs=21)
- [Minerva Client](https://www.notion.so/Minerva-Client-5a057cb95d7c44779f1d2586c1e6660f?pvs=21)
- [Querying Heterogeneous Data Sources](https://www.notion.so/Querying-Heterogeneous-Data-Sources-da2558e26a2b486a93b7bb9b64f9b077?pvs=21)
- [Query Optimization](https://www.notion.so/Query-Optimization-8febb4d1b4ed43f3a374de503bb28c48?pvs=21)
- [On-Demand Computing](https://www.notion.so/On-Demand-Computing-2759a6b53b1f4229921df5b55a8ca514?pvs=21)
- [Configuration Properties](https://www.notion.so/Configuration-Properties-d84afdfb03214ba2b80b63e189c47743?pvs=21)
- [Create Minerva Clusters](https://www.notion.so/Create-Minerva-Clusters-3141e35c63c54d01b1830a0795e6e815?pvs=21)

### [Atlas](https://www.notion.so/Analytics-209caee9018645008d44685e5c6d7e64?pvs=21)

- [Dashboard](https://www.notion.so/Dashboard-39b5170dc2144240a4c90429c8f753ab?pvs=21)
- [Queries](https://www.notion.so/Queries-2882078185b1407786002caffa3f7970?pvs=21)
- [Snippets](https://www.notion.so/Snippets-1dafde685cf7480d99c992c9321571c0?pvs=21)
- [Alerts](https://www.notion.so/Alerts-5dab9a5d631c46b98a9858093ff01cae?pvs=21)
- [Destinations](https://www.notion.so/Destinations-3170bf522e334b9db5c9f1c37e1c3b04?pvs=21)
- [Adding Visualizations to Dashboards](https://www.notion.so/Atlas-3129c570469b4e37a5594d2976286219?pvs=21)
- [Sankey](https://www.notion.so/Sankey-b3f1a8c74b3b48349365043d8f756ea1?pvs=21)
- [Sunburst](https://www.notion.so/Sunburst-3a25c6c728ec4faaa80cab34d53278bf?pvs=21)
- [Treemap](https://www.notion.so/Treemap-e54188f7d6cf47179196c4345d5d5fae?pvs=21)
- [Cohort](https://www.notion.so/Cohort-9b5fa005902f4e5f8ce5e94b02e634fb?pvs=21)
- [Funnel](https://www.notion.so/Funnel-07f2121684b24645bb1ead06afbb0394?pvs=21)
- [Map (Choropleth)](https://www.notion.so/Map-Choropleth-9852956bfe774cf9958f24671d2e2e9e?pvs=21)

## [Data Apps](https://www.notion.so/Data-Apps-349e2281454e4a51a251079cefdca799?pvs=21)

### [Alpha](https://www.notion.so/Alpha-00977fdf48584c9e9bc19b60a5db932b?pvs=21)

### [Beacon](https://www.notion.so/Beacon-917e6ce5a47e49e3a900cc862c274ab2?pvs=21)

### [Query Book](https://www.notion.so/Data-Apps-349e2281454e4a51a251079cefdca799?pvs=21)

### [Audience App](https://www.notion.so/Audiences-6595f7451f9e4e7e8e09212e1738eaae?pvs=21)

## [Security](https://www.notion.so/Security-e42d269c14854046b6301d36df5c5dbd?pvs=21)

### [Authentication](https://www.notion.so/Authentication-53b1865e2daf4929b24d6f61a9854747?pvs=21)

- [OpenID Connect](https://www.notion.so/OpenID-Connect-447927e38049468fb40a1c88bca2258a?pvs=21)

### [Authorization](https://www.notion.so/Authorization-c106ddb85b1443cba1c0d7f4d48246c1?pvs=21)

- [Tag-based Authorization](https://www.notion.so/Tag-based-Authorization-0457c01731424962bdf4c13efdb33186?pvs=21)

### [Data Protection](https://www.notion.so/Data-Protection-3e7a734dc432454b8fbd13a5e08a9caf?pvs=21)

- [Policy](https://www.notion.so/Data-Protection-3e7a734dc432454b8fbd13a5e08a9caf?pvs=21)

### [Network Security](https://www.notion.so/Network-Security-7ba15309e6194dc19b43e945828f99cc?pvs=21)

### [Compliance](https://www.notion.so/Compliance-91dacebeabf04505958ed23f8c639a7d?pvs=21)

### [Heimdall Capabilities](https://www.notion.so/Heimdall-Capabilities-bf4b1f7f5ad0466cbba36f789a9c7972?pvs=21)

- [Gateway Service](https://www.notion.so/Gateway-Service-3e8f2ed0ef274976bb005c0616847e7d?pvs=21)
- [OpenID Connect](https://www.notion.so/Heimdall-Capabilities-bf4b1f7f5ad0466cbba36f789a9c7972?pvs=21)
- [User and Policy Tags Management](https://www.notion.so/User-and-Policy-Tags-Management-b5ddf5757d494d93b527f93be1655dc0?pvs=21)
- [Creating API Keys and Token](https://www.notion.so/Creating-API-Keys-and-Token-9aa3c2856a134636b77b9c4218d786d6?pvs=21)

## [Observability](https://www.notion.so/Observability-395dd5a0537b4cf0a7cf213ae983b91d?pvs=21)

### [Operations Center](https://www.notion.so/Operations-Center-c412de7cb2084ac7b5e817bdf8539399?pvs=21)

### [Grafana](https://www.notion.so/Grafana-Dashboard-9e31ec5d3bb84561af28b3c74102b3f4?pvs=21)

</aside>

1. Open the Operations App

![Untitled](../../Running%20Flare%20Standalone%206d1c2d888606476d91346ed3e4a7e1af/Getting%20the%20Port%20of%20Service%20and%20AdminUrl%201109047016724c15bb040e59dd9aa44c/Untitled.png)

1. Click on the Core Kernel

![Untitled](../../Running%20Flare%20Standalone%206d1c2d888606476d91346ed3e4a7e1af/Getting%20the%20Port%20of%20Service%20and%20AdminUrl%201109047016724c15bb040e59dd9aa44c/Untitled%201.png)

1. Click on the Services

![Untitled](../../Running%20Flare%20Standalone%206d1c2d888606476d91346ed3e4a7e1af/Getting%20the%20Port%20of%20Service%20and%20AdminUrl%201109047016724c15bb040e59dd9aa44c/Untitled%202.png)

1. In the services search for `pulsar-broker`

![Untitled](../../Running%20Flare%20Standalone%206d1c2d888606476d91346ed3e4a7e1af/Getting%20the%20Port%20of%20Service%20and%20AdminUrl%201109047016724c15bb040e59dd9aa44c/Untitled%203.png)

1. Click on the `pulsar-broker` service and navigate to the Service Details. Here you will find the Port section which gives the details of the name, protocol, and port

![Port.png](../../Running%20Flare%20Standalone%206d1c2d888606476d91346ed3e4a7e1af/Getting%20the%20Port%20of%20Service%20and%20AdminUrl%201109047016724c15bb040e59dd9aa44c/Port.png)