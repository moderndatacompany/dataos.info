# Data Integration - Supported Connectors in DataOS

The following section provides an overview of the data sources accessible by one or more components within DataOS.

<aside class="callout">
🗣️ In relation to Minerva (DataOS's query engine), the supported source systems for query pushdown are also indicated.*
</aside>

## Supported Connectors

| Data Source                                          | Type                             | Depot | Minerva | Pushdown Support (Minerva) | Flare | Scanner |
|------------------------------------------------------|----------------------------------|-------|---------|----------------------------|-------|---------|
| ElasticSearch                                        | Database                         | :white_check_mark:           | :white_check_mark:         | :white_large_square:       | :white_check_mark:       | :white_large_square:     |
| Icebase (Iceberg Format)                             | Database                         | :white_check_mark:           | :white_check_mark:         | :white_large_square:       | :white_check_mark:       | :white_check_mark:     |
| MySQL                                                | Database                         | :white_check_mark:           | :white_check_mark:         | :white_check_mark:         | :white_check_mark:       | :white_check_mark:     |
| MS SQL                                               | Database                         | :white_check_mark:           | :white_check_mark:         | :white_check_mark:         | :white_check_mark:       | :white_check_mark:     |
| MongoDB                                              | Database                         | :white_check_mark:           | :white_check_mark:         | :white_large_square:       | :white_check_mark:       | :white_large_square:     |
| Oracle                                               | Database                         | :white_check_mark:           | :white_check_mark:         | :white_check_mark:         | :white_check_mark:       | :white_check_mark:     |
| PostgreSQL                                          | Database                         | :white_check_mark:           | :white_check_mark:         | :white_large_square:       | :white_check_mark:       | :white_check_mark:     
| Eventhub                                             | Messaging & Streaming Datastore | :white_check_mark:           | :white_large_square:       | :white_large_square:       | :white_check_mark:       | :white_large_square:   |
| Fastbase (Pulsar)                                    | Messaging & Streaming Datastore | :white_check_mark:           | :white_large_square:       | :white_large_square:       | :white_check_mark:       | :white_check_mark:     |
| Kafka                                                | Messaging & Streaming Datastore | :white_check_mark:           | :white_check_mark:         | :white_large_square:       | :white_check_mark:       | :white_check_mark:     
| AWS Redshift                                         | Warehouses & Data Lake           | :white_check_mark:           | :white_check_mark:         | :white_large_square:       | :white_check_mark:       | :white_check_mark:     |
| AWS S3 Blob Storage                                  | Warehouses & Data Lake           | :white_check_mark:           | :white_large_square:       | :white_large_square:       | :white_check_mark:       | :white_large_square:   |
| ABFSS (Azure Data Lake Gen2)                         | Warehouses & Data Lake           | :white_check_mark:           | :white_large_square:       | :white_large_square:       | :white_check_mark:       | :white_large_square:   |
| WASBS (Azure Blob Storage)                           | Warehouses & Data Lake           | :white_check_mark:           | :white_large_square:       | :white_large_square:       | :white_check_mark:       | :white_large_square:   |
| BigQuery                                             | Warehouses & Data Lake           | :white_check_mark:           | :white_check_mark:         | :white_large_square:       | :white_check_mark:       | :white_check_mark:     |
| GCS (Google Cloud Storage)                           | Warehouses & Data Lake           | :white_check_mark:           | :white_large_square:       | :white_large_square:       | :white_check_mark:       | :white_large_square:   |
| Snowflake                                            | Warehouses & Data Lake           | :white_check_mark:           | :white_large_square:       | :white_large_square:       | :white_check_mark:       | :white_check_mark:     
| "JDBC (any source exposed via JDBC driver is supported, e.g. MSSQL Server, SAP Hana)" | Miscellaneous                    | :white_check_mark:           | :white_check_mark:         | :white_large_square:       | :white_check_mark:       | :white_check_mark:     |
| OpenSearch                                           | Miscellaneous                    | :white_check_mark:           | :white_large_square:       | :white_large_square:       | :white_check_mark:       | :white_large_square:   
| Accumulo                                             | Databases                        | :white_large_square:         | :white_check_mark:         | :white_large_square:       | :white_large_square:     | :white_large_square:   |
| Cassandra                                            | Databases                        | :white_large_square:         | :white_check_mark:         | :white_large_square:       | :white_large_square:     | :white_large_square:   |
| ClickHouse                                           | Databases                        | :white_large_square:         | :white_check_mark:         | :white_check_mark:         | :white_large_square:     | :white_check_mark:     |
| DB2 (IBM)                                            | Databases                        | :white_large_square:         | :white_large_square:       | :white_large_square:       | :white_large_square:     | :white_check_mark:     |
| DOMO Database                                        | Databases                        | :white_large_square:         | :white_large_square:       | :white_large_square:       | :white_large_square:     | :white_check_mark:     |
| Ignite                                               | Databases (for in-memory computing) | :white_large_square:         | :white_check_mark:         | :white_check_mark:         | :white_large_square:     | :white_large_square:   |
| Kudu                                                 | Databases                        | :white_large_square:         | :white_check_mark:         | :white_large_square:       | :white_large_square:     | :white_large_square:   |
| Phoenix                                              | Databases                        | :white_large_square:         | :white_check_mark:         | :white_large_square:       | :white_large_square:     | :white_large_square:   |
| Pinot                                                | Databases                        | :white_large_square:         | :white_check_mark:         | :white_check_mark:         | :white_large_square:     | :white_large_square:   |
| Prometheus                                           | Databases (Metrics Collection & Time-series DB)| :white_large_square:         | :white_check_mark:         | :white_large_square:       | :white_large_square:     | :white_large_square:   |
| SingleStore                                          | Databases                        | :white_large_square:         | :white_check_mark:         | :white_check_mark:         | :white_large_square:     | :white_check_mark:     
| Azure Databricks                                     | Warehouses & Data lakes          | :white_large_square:         | :white_large_square:       | :white_large_square:       | :white_large_square:     | :white_check_mark:     |
| Hive                                                 | Warehouses & Data Lake           | :white_large_square:         | :white_check_mark:         | :white_large_square:       | :white_large_square:     | :white_check_mark:     |
| Hudi                                                 | Warehouses & Data Lake           | :white_large_square:         | :white_check_mark:         | :white_large_square:       | :white_large_square:     | :white_large_square:   |
| MariaDB                                              | Warehouses & Data lakes          | :white_large_square:         | :white_check_mark:         | :white_check_mark:         | :white_large_square:     | :white_check_mark:     |
| Delta Lake                                           | Lakehouse                        | :white_large_square:         | :white_check_mark:         | :white_large_square:       | :white_large_square:     | :white_large_square:   
| Atop                                                 | Miscellaneous (Linux Server Performance Analysis Tool) | :white_large_square:         | :white_check_mark:         | :white_large_square:       | :white_large_square:     | :white_large_square:   |
| AWS Glue                                             | Miscellaneous (Data Integration Service) | :white_large_square:         | :white_large_square:       | :white_large_square:       | :white_large_square:     | :white_check_mark:     |
| AWS Athena                                           | Miscellaneous (Interactive Analytics Service) | :white_large_square:         | :white_large_square:       | :white_large_square:       | :white_large_square:     | :white_check_mark:     |
| Druid                                                | Miscellaneous (for Real-time Analytics) | :white_large_square:         | :white_check_mark:         | :white_large_square:       | :white_large_square:     | :white_check_mark:     |
| Google Sheets                                        | File System                      | :white_large_square:         | :white_check_mark:         | :white_large_square:       | :white_large_square:     | :white_large_square:   |
| JMX                                                  | Miscellaneous                    | :white_large_square:         | :white_check_mark:         | :white_large_square:       | :white_large_square:     | :white_large_square:   |
| Kinesis                                              | Messaging & Streaming Platform   | :white_large_square:         | :white_check_mark:         | :white_large_square:       | :white_large_square:     | :white_large_square:   |
| Redis                                                | Miscellaneous                    | :white_large_square:         | :white_check_mark:         | :white_check_mark:         | :white_large_square:     | :white_large_square:   |


## Airbyte - Connectors

In addition to the above mentioned sources, Airbyte has been seamlessly integrated into DataOS's Technology Stack. This integration empowers us to facilitate connectivity with approximately **300 data sources**, encompassing a wide array of WebAPIs and Analytics Tools. Refer to the comprehensive list below:

<details>
<summary>List of connectors supported by Airbyte</summary>

<table>
  <thead>
    <tr>
      <th>Sno.</th>
      <th>Connector Name</th>
      <th>Type</th>
      <th>Sources</th>
      <th>Destinations</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>AlloyDB for Postgre SQL</td>
      <td>Databases</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>2</td>
      <td>Apache Doris</td>
      <td>Databases</td>
      <td></td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Apache Iceberg</td>
      <td>Databases</td>
      <td></td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Apache Kafka</td>
      <td>Databases</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>5</td>
      <td>Click House</td>
      <td>Databases</td>
      <td>Yes</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>6</td>
      <td>CockroachDB</td>
      <td>Databases</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>7</td>
      <td>Convex.dev</td>
      <td>Databases</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>8</td>
      <td>DuckDB</td>
      <td>Databases</td>
      <td></td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>9</td>
      <td>DynamoDB</td>
      <td>Databases</td>
      <td>Yes</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>10</td>
      <td>Elasticsearch</td>
      <td>Databases</td>
      <td>Yes</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>11</td>
      <td>Fauna</td>
      <td>Databases</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>12</td>
      <td>Firebase</td>
      <td>Databases</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>13</td>
      <td>Google Pubsub</td>
      <td>Databases</td>
      <td></td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>14</td>
      <td>IBM Db2</td>
      <td>Databases</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>15</td>
      <td>Kafka</td>
      <td>Databases</td>
      <td></td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>16</td>
      <td>MSSQL SQL Server</td>
      <td>Databases</td>
      <td>Yes</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>17</td>
      <td>MySQL</td>
      <td>Databases</td>
      <td>Yes</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>18</td>
      <td>MongoDB</td>
      <td>Databases</td>
      <td>Yes</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>19</td>
      <td>Microsoft Dataverse</td>
      <td>Databases</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>20</td>
      <td>Oracle DB</td>
      <td>Databases</td>
      <td>Yes</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>21</td>
      <td>Postgre SQL</td>
      <td>Databases</td>
      <td>Yes</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>22</td>
      <td>Pulsar</td>
      <td>Databases</td>
      <td>Yes</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>23</td>
      <td>TiDB</td>
      <td>Databases</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>24</td>
      <td>Yugabytedb</td>
      <td>Databases</td>
      <td></td>
      <td>Yes</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>25</td>
      <td>S3</td>
      <td>Warehouses and Lakes</td>
      <td>Yes</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>26</td>
      <td>BigQuery</td>
      <td>Warehouses and Lakes</td>
      <td>Yes</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>27</td>
      <td>MariaDB Columnstore</td>
      <td>Warehouses and Lakes</td>
      <td></td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>28</td>
      <td>Firebolt</td>
      <td>Warehouses and Lakes</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>29</td>
      <td>Azure Blob Storage</td>
      <td>Warehouses and Lakes</td>
      <td></td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>30</td>
      <td>Azure Table Storage</td>
      <td>Warehouses and Lakes</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>31</td>
      <td>S3 Glue</td>
      <td>Warehouses and Lakes</td>
      <td></td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>32</td>
      <td>Redshift</td>
      <td>Warehouses and Lakes</td>
      <td>Yes</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>33</td>
      <td>Google Cloud Storage</td>
      <td>Warehouses and Lakes</td>
      <td></td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>34</td>
      <td>Snowflake Data Cloud</td>
      <td>Warehouses and Lakes</td>
      <td>Yes</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>35</td>
      <td>Teradata</td>
      <td>Warehouses and Lakes</td>
      <td></td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>36</td>
      <td>Databricks Lakehouse</td>
      <td>Warehouses and Lakes</td>
      <td></td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>37</td>
      <td>AWS</td>
      <td>Warehouses and Lakes</td>
      <td></td>
      <td>Yes</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>38</td>
      <td>AWS Cloud Trail</td>
      <td>Engineering Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>39</td>
      <td>Amazon SQS</td>
      <td>Engineering Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>40</td>
      <td>Auth0</td>
      <td>Engineering Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>41</td>
      <td>Ashby</td>
      <td>Engineering Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>42</td>
      <td>Convex</td>
      <td>Engineering Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>43</td>
      <td>Courier</td>
      <td>Engineering Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>44</td>
      <td>Datadog</td>
      <td>Engineering Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>45</td>
      <td>Dockerhub</td>
      <td>Engineering Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>46</td>
      <td>E2E Testing</td>
      <td>Engineering Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>47</td>
      <td>GitLab</td>
      <td>Engineering Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>48</td>
      <td>Harness</td>
      <td>Engineering Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>49</td>
      <td>Intruder</td>
      <td>Engineering Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>50</td>
      <td>K6 Cloud</td>
      <td>Engineering Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>51</td>
      <td>PagerDuty</td>
      <td>Engineering Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>52</td>
      <td>Jira</td>
      <td>Engineering Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>53</td>
      <td>Jenkins</td>
      <td>Engineering Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>54</td>
      <td>MeiliSearch</td>
      <td>Engineering Analytics</td>
      <td></td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>55</td>
      <td>PyPI</td>
      <td>Engineering Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>56</td>
      <td>Rest Api</td>
      <td>Engineering Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>57</td>
      <td>Sentry</td>
      <td>Engineering Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>58</td>
      <td>SonarCloud</td>
      <td>Engineering Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>59</td>
      <td>Statuspage</td>
      <td>Engineering Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>60</td>
      <td>Statuspage.io</td>
      <td>Engineering Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>61</td>
      <td>Streamr</td>
      <td>Engineering Analytics</td>
      <td></td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>62</td>
      <td>Typesense</td>
      <td>Engineering Analytics</td>
      <td></td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>63</td>
      <td>Vantage</td>
      <td>Engineering Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>64</td>
      <td>VictorOps</td>
      <td>Engineering Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>65</td>
      <td>App follow</td>
      <td>Product Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>66</td>
      <td>Adjust</td>
      <td>Product Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>67</td>
      <td>Aha</td>
      <td>Product Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>68</td>
      <td>Amplitude</td>
      <td>Product Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>69</td>
      <td>Chartmogul</td>
      <td>Product Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>70</td>
      <td>Config Cat</td>
      <td>Product Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>71</td>
      <td>Keen</td>
      <td>Product Analytics</td>
      <td></td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>72</td>
      <td>Launch Darkly</td>
      <td>Product Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>73</td>
      <td>Looker</td>
      <td>Product Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>74</td>
      <td>Mixpanel</td>
      <td>Product Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>75</td>
      <td>Metabase</td>
      <td>Product Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>76</td>
      <td>Plausible</td>
      <td>Product Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>77</td>
      <td>Posthog</td>
      <td>Product Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>78</td>
      <td>Microsoft Dynamics NAV</td>
      <td>Product Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>79</td>
      <td>Facebook Marketing</td>
      <td>Marketing Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>80</td>
      <td>Facebook Pages</td>
      <td>Marketing Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>81</td>
      <td>Google Ads</td>
      <td>Marketing Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>82</td>
      <td>Google Analytics</td>
      <td>Marketing Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>83</td>
      <td>Google Search Console</td>
      <td>Marketing Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>84</td>
      <td>Instagram</td>
      <td>Marketing Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>85</td>
      <td>Webflow</td>
      <td>Marketing Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>86</td>
      <td>Active Campaign</td>
      <td>Marketing Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>87</td>
      <td>Amazon Ads</td>
      <td>Marketing Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>88</td>
      <td>Bing Ads</td>
      <td>Marketing Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>89</td>
      <td>Braze</td>
      <td>Marketing Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>90</td>
      <td>Cart</td>
      <td>Marketing Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>91</td>
      <td>Emarsys</td>
      <td>Marketing Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>92</td>
      <td>Formidable Forms</td>
      <td>Marketing Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>93</td>
      <td>Heap</td>
      <td>Marketing Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>94</td>
      <td>HubSpot</td>
      <td>Marketing Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>95</td>
      <td>HubSpot CRM</td>
      <td>Marketing Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>96</td>
      <td>HubSpot Marketing</td>
      <td>Marketing Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>97</td>
      <td>Iterable</td>
      <td>Marketing Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>98</td>
      <td>Klaviyo</td>
      <td>Marketing Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>99</td>
      <td>LinkedIn Pages</td>
      <td>Marketing Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>100</td>
      <td>LinkedIn</td>
      <td>Marketing Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>101</td>
      <td>Mailchimp</td>
      <td>Marketing Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>102</td>
      <td>Marketo</td>
      <td>Marketing Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>103</td>
      <td>Microsoft Advertising</td>
      <td>Marketing Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>104</td>
      <td>Microsoft Dynamics 365</td>
      <td>Marketing Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>105</td>
      <td>Twitter Ads</td>
      <td>Marketing Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>106</td>
      <td>LinkedIn Ads</td>
      <td>Marketing Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>107</td>
      <td>Lokalise</td>
      <td>Marketing Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>108</td>
      <td>Mailchimp</td>
      <td>Marketing Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>109</td>
      <td>Mailgun</td>
      <td>Marketing Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>110</td>
      <td>Mailjet Email</td>
      <td>Marketing Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>111</td>
      <td>Mailjet SMS</td>
      <td>Marketing Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>112</td>
      <td>Marketo</td>
      <td>Marketing Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>113</td>
      <td>N8n</td>
      <td>Marketing Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>114</td>
      <td>Omnisend</td>
      <td>Marketing Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>115</td>
      <td>OneSignal</td>
      <td>Marketing Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>116</td>
      <td>Orbit.love</td>
      <td>Marketing Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>117</td>
      <td>PartnerStack</td>
      <td>Marketing Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>118</td>
      <td>Pinterest Ads</td>
      <td>Marketing Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>119</td>
      <td>Postmark App</td>
      <td>Marketing Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>120</td>
      <td>Qualaroo</td>
      <td>Marketing Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>121</td>
      <td>RD Station Marketing</td>
      <td>Marketing Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>122</td>
      <td>SendGrid</td>
      <td>Marketing Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>123</td>
      <td>Sendinblue</td>
      <td>Marketing Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>124</td>
      <td>Short.io</td>
      <td>Marketing Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>125</td>
      <td>Smaily</td>
      <td>Marketing Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>126</td>
      <td>SmartEngage</td>
      <td>Marketing Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>127</td>
      <td>Snapchat Marketing</td>
      <td>Marketing Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>128</td>
      <td>SurveyMonkey</td>
      <td>Marketing Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>129</td>
      <td>SurveySparrow</td>
      <td>Marketing Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>130</td>
      <td>TikTok for Business Marketing</td>
      <td>Marketing Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>131</td>
      <td>Twilio</td>
      <td>Marketing Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>132</td>
      <td>Twitter</td>
      <td>Marketing Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>133</td>
      <td>Tyntec SMS</td>
      <td>Marketing Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>134</td>
      <td>Typeform</td>
      <td>Marketing Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>135</td>
      <td>Whisky Hunter</td>
      <td>Marketing Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>136</td>
      <td>Wordpress</td>
      <td>Marketing Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>137</td>
      <td>Yandex Metrica</td>
      <td>Marketing Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>138</td>
      <td>YouTube Analytics</td>
      <td>Marketing Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>139</td>
      <td>Zapier Supported Storage</td>
      <td>Marketing Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>140</td>
      <td>App Store</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>141</td>
      <td>Asana</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>142</td>
      <td>Alpha Vantage</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>143</td>
      <td>Airtable</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>144</td>
      <td>Amazon Seller Partner</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>145</td>
      <td>BambooHR</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>146</td>
      <td>Big Commerce</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>147</td>
      <td>Braintree</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>148</td>
      <td>Chargebee</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>149</td>
      <td>Chargify</td>
      <td>Finance & Ops Analytics</td>
      <td></td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>150</td>
      <td>ClickUp</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>151</td>
      <td>Clockify</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>152</td>
      <td>Coin API</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>153</td>
      <td>Coin Gecko Coins</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>154</td>
      <td>CoinMarketCap</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>155</td>
      <td>Exchange Rates API</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>156</td>
      <td>Fastbill</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>157</td>
      <td>Confluence</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>158</td>
      <td>Commerce tools</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>159</td>
      <td>Flexport</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>160</td>
      <td>GetLago</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>161</td>
      <td>Glassfrog</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>162</td>
      <td>GoCardless</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>163</td>
      <td>Greenhouse</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>164</td>
      <td>Gutendex</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>165</td>
      <td>Google Directory</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>166</td>
      <td>Harvest</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>167</td>
      <td>Hubplanner</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>168</td>
      <td>Klarna</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>169</td>
      <td>Lever Hiring</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>170</td>
      <td>Kyriba</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>171</td>
      <td>Linnworks</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>172</td>
      <td>Notion</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>173</td>
      <td>Okta</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>174</td>
      <td>Google Workspace Admin Reports</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>175</td>
      <td>Microsoft Dynamics AX</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>176</td>
      <td>Microsoft Teams</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>177</td>
      <td>Microsoft Dynamics GP</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>178</td>
      <td>My Hours</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>179</td>
      <td>Netsuite</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>180</td>
      <td>Oracle PeopleSoft</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>181</td>
      <td>Orb</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>182</td>
      <td>Pagar.me</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>183</td>
      <td>PayPal Transaction</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>184</td>
      <td>Plaid</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>185</td>
      <td>PrestaShop</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>186</td>
      <td>Primetric</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>187</td>
      <td>QuickBooks</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>188</td>
      <td>Railz</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>189</td>
      <td>Recharge</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>190</td>
      <td>Recruitee</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>191</td>
      <td>Recurly</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>192</td>
      <td>Rocket.chat</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <th>Sno.</th>
      <th>Connector Name</th>
      <th>Type</th>
      <th>Sources</th>
      <th>Destinations</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>193</td>
      <td>SAP Business One</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>194</td>
      <td>SAP Fieldglass</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>195</td>
      <td>Shopify</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>196</td>
      <td>Slack</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>197</td>
      <td>Spree Commerce</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>198</td>
      <td>Square</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>199</td>
      <td>Stripe</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>200</td>
      <td>Tempo</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>201</td>
      <td>Timely</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>202</td>
      <td>Toggl</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>203</td>
      <td>Trello</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>204</td>
      <td>Visma E-conomic</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>205</td>
      <td>WooCommerce</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>206</td>
      <td>Workramp</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>207</td>
      <td>Wrike</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>208</td>
      <td>Younium</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>209</td>
      <td>Zenefits</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>210</td>
      <td>Zencart</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>211</td>
      <td>Zoom</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>212</td>
      <td>Zuora</td>
      <td>Finance & Ops Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>213</td>
      <td>Salesforce</td>
      <td>Sales & Support Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>214</td>
      <td>Close.com</td>
      <td>Sales & Support Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>215</td>
      <td>Coda</td>
      <td>Sales & Support Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>216</td>
      <td>Delighted</td>
      <td>Sales & Support Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>217</td>
      <td>Dixa</td>
      <td>Sales & Support Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>218</td>
      <td>Drift</td>
      <td>Sales & Support Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>219</td>
      <td>Freshcaller</td>
      <td>Sales & Support Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>220</td>
      <td>Freshdesk</td>
      <td>Sales & Support Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>221</td>
      <td>Freshsales</td>
      <td>Sales & Support Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>222</td>
      <td>Intercom</td>
      <td>Sales & Support Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>223</td>
      <td>Kustomer</td>
      <td>Sales & Support Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>224</td>
      <td>Oracle Siebel CRM</td>
      <td>Sales & Support Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>225</td>
      <td>Outreach</td>
      <td>Sales & Support Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>226</td>
      <td>PersistIq</td>
      <td>Sales & Support Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>227</td>
      <td>Pipedrive</td>
      <td>Sales & Support Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>228</td>
      <td>Reply.io</td>
      <td>Sales & Support Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>229</td>
      <td>Retently</td>
      <td>Sales & Support Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>230</td>
      <td>SalesLoft</td>
      <td>Sales & Support Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>231</td>
      <td>Sugar CRM</td>
      <td>Sales & Support Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>232</td>
      <td>TalkDesk Explore</td>
      <td>Sales & Support Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>233</td>
      <td>Vitally</td>
      <td>Sales & Support Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>234</td>
      <td>Zendesk Chat</td>
      <td>Sales & Support Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>235</td>
      <td>Zendesk Sell</td>
      <td>Sales & Support Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>236</td>
      <td>Zendesk Sunshine</td>
      <td>Sales & Support Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>237</td>
      <td>Zendesk Support</td>
      <td>Sales & Support Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>238</td>
      <td>Zendesk Talk</td>
      <td>Sales & Support Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>239</td>
      <td>Zenloop</td>
      <td>Sales & Support Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
    <tr>
      <td>240</td>
      <td>Zoho CRM</td>
      <td>Sales & Support Analytics</td>
      <td>Yes</td>
      <td></td>
    </tr>
  <tr>
    <td>241</td>
    <td>Microsoft Dynamics Customer Engagement</td>
    <td>Sales & Support Analytics</td>
    <td>Yes</td>
    <td></td>
  </tr>
  <tr>
    <td>242</td>
    <td>Google Sheets</td>
    <td>Files</td>
    <td>Yes</td>
    <td>Yes</td>
  </tr>
  <tr>
    <td>243</td>
    <td>CSV</td>
    <td>Files</td>
    <td>Yes</td>
    <td>Yes</td>
  </tr>
  <tr>
    <td>244</td>
    <td>Excel</td>
    <td>Files</td>
    <td>Yes</td>
    <td></td>
  </tr>
  <tr>
    <td>245</td>
    <td>Feather</td>
    <td>Files</td>
    <td>Yes</td>
    <td></td>
  </tr>
  <tr>
    <td>246</td>
    <td>JSON File</td>
    <td>Files</td>
    <td>Yes</td>
    <td>Yes</td>
  </tr>
  <tr>
    <td>247</td>
    <td>SFTP</td>
    <td>Files</td>
    <td>Yes</td>
    <td></td>
  </tr>
  <tr>
    <td>248</td>
    <td>Parquet File</td>
    <td>Files</td>
    <td>Yes</td>
    <td></td>
  </tr>
  <tr>
    <td>249</td>
    <td>Smartsheets</td>
    <td>Files</td>
    <td>Yes</td>
    <td></td>
  </tr>
  <tr>
    <td>250</td>
    <td>Apify</td>
    <td>Others</td>
    <td>Yes</td>
    <td></td>
  </tr>
  <tr>
    <td>251</td>
    <td>Breezometer</td>
    <td>Others</td>
    <td>Yes</td>
    <td></td>
  </tr>
  <tr>
    <td>252</td>
    <td>Faker</td>
    <td>Others</td>
    <td>Yes</td>
    <td></td>
  </tr>
  <tr>
    <td>253</td>
    <td>NASA</td>
    <td>Others</td>
    <td>Yes</td>
    <td></td>
  </tr>
  <tr>
    <td>254</td>
    <td>New York Times</td>
    <td>Others</td>
    <td>Yes</td>
    <td></td>
  </tr>
  <tr>
    <td>255</td>
    <td>News API</td>
    <td>Others</td>
    <td>Yes</td>
    <td></td>
  </tr>
  <tr>
    <td>256</td>
    <td>IP2Whois</td>
    <td>Others</td>
    <td>Yes</td>
    <td></td>
  </tr>
  <tr>
    <td>257</td>
    <td>Google Webfonts</td>
    <td>Others</td>
    <td>Yes</td>
    <td></td>
  </tr>
  <tr>
    <td>258</td>
    <td>Newsdata</td>
    <td>Others</td>
    <td>Yes</td>
    <td></td>
  </tr>
  <tr>
    <td>259</td>
    <td>OpenWeather</td>
    <td>Others</td>
    <td>Yes</td>
    <td></td>
  </tr>
  <tr>
    <td>260</td>
    <td>Oura</td>
    <td>Others</td>
    <td>Yes</td>
    <td></td>
  </tr>
  <tr>
    <td>261</td>
    <td>Pexels API</td>
    <td>Others</td>
    <td>Yes</td>
    <td></td>
  </tr>
  <tr>
    <td>262</td>
    <td>Pocket</td>
    <td>Others</td>
    <td>Yes</td>
    <td></td>
  </tr>
  <tr>
    <td>263</td>
    <td>PokéAPI</td>
    <td>Others</td>
    <td>Yes</td>
    <td></td>
  </tr>
  <tr>
    <td>264</td>
    <td>Polygon</td>
    <td>Others</td>
    <td>Yes</td>
    <td></td>
  </tr>
  <tr>
    <td>265</td>
    <td>Public API</td>
    <td>Others</td>
    <td>Yes</td>
    <td></td>
  </tr>
  <tr>
    <td>266</td>
    <td>Punk API</td>
    <td>Others</td>
    <td>Yes</td>
    <td></td>
  </tr>
  <tr>
    <td>267</td>
    <td>REST Countries</td>
    <td>Others</td>
    <td>Yes</td>
    <td></td>
  </tr>
  <tr>
    <td>268</td>
    <td>RKI Covid</td>
    <td>Others</td>
    <td>Yes</td>
    <td></td>
  </tr>
  <tr>
    <td>269</td>
    <td>RSS</td>
    <td>Others</td>
    <td>Yes</td>
    <td></td>
  </tr>
  <tr>
    <td>270</td>
    <td>Recreation.gov</td>
    <td>Others</td>
    <td>Yes</td>
    <td></td>
  </tr>
  <tr>
    <td>271</td>
    <td>SFTP Bulk</td>
    <td>Others</td>
    <td>Yes</td>
    <td></td>
  </tr>
  <tr>
    <td>272</td>
    <td>SearchMetrics</td>
    <td>Others</td>
    <td>Yes</td>
    <td></td>
  </tr>
  <tr>
    <td>273</td>
    <td>Secoda</td>
    <td>Others</td>
    <td>Yes</td>
    <td></td>
  </tr>
  <tr>
    <td>274</td>
    <td>Senseforce</td>
    <td>Others</td>
    <td>Yes</td>
    <td></td>
  </tr>
  <tr>
    <td>275</td>
    <td>SpaceX API</td>
    <td>Others</td>
    <td>Yes</td>
    <td></td>
  </tr>
  <tr>
    <td>276</td>
    <td>Strava</td>
    <td>Others</td>
    <td>Yes</td>
    <td></td>
  </tr>
  <tr>
    <td>277</td>
    <td>TMDb</td>
    <td>Others</td>
    <td>Yes</td>
    <td></td>
  </tr>
  <tr>
    <td>278</td>
    <td>TVMaze Schedule</td>
    <td>Others</td>
    <td>Yes</td>
    <td></td>
  </tr>
  <tr>
    <td>279</td>
    <td>The Guardian API</td>
    <td>Others</td>
    <td>Yes</td>
    <td></td>
  </tr>
  <tr>
    <td>280</td>
    <td>US Census</td>
    <td>Others</td>
    <td>Yes</td>
    <td></td>
  </tr>
  <tr>
    <td>281</td>
    <td>Waiteraid</td>
    <td>Others</td>
    <td>Yes</td>
    <td></td>
  </tr>
  <tr>
    <td>282</td>
    <td>Weatherstack</td>
    <td>Others</td>
    <td>Yes</td>
    <td></td>
  </tr>
  <tr>
    <td>283</td>
    <td>Wikipedia Pageviews</td>
    <td>Others</td>
    <td>Yes</td>
    <td></td>
  </tr>
  <tr>
    <td>284</td>
    <td>xkcd</td>
    <td>Others</td>
    <td>Yes</td>
    <td></td>
  </tr>
</tbody>
</table>

</details>


## BI Tools Connectors

DataOS seamlessly integrates with multiple Business Intelligence (BI) Tools, including Tableau, PowerBI, and IBM SPSS Statistics. Refer to the link to know [more](/interfaces/atlas/bi_tools/)

## High Touch Connectors

DataOS also provides integration with HighTouch, enabling the syndication of data from diverse Data Warehouses, Spreadsheets, and Data Lakes to over 125 Software-as-a-Service (SaaS) tools and Business Applications. This functionality empowers various Reverse-ETL use cases.

Refer to the following list of supported Destinations and Sources within HighTouch:

<details><summary>List of Sources supported by Hightouch</summary>
<center>
<table>
  <thead>
    <tr>
      <th>Sno.</th>
      <th>Connector Name</th>
      <th>Type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>AlloyDB</td>
      <td>Data System</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Amazon Athena</td>
      <td>Data System</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Amazon Redshift</td>
      <td>Data System</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Azure Synapse</td>
      <td>Data System</td>
    </tr>
    <tr>
      <td>5</td>
      <td>ClickHouse</td>
      <td>Data System</td>
    </tr>
    <tr>
      <td>6</td>
      <td>Databricks</td>
      <td>Data System</td>
    </tr>
    <tr>
      <td>7</td>
      <td>Elasticsearch</td>
      <td>Data System</td>
    </tr>
    <tr>
      <td>8</td>
      <td>Firebolt</td>
      <td>Data System</td>
    </tr>
    <tr>
      <td>9</td>
      <td>Google BigQuery</td>
      <td>Data System</td>
    </tr>
    <tr>
      <td>10</td>
      <td>Greenplum Database</td>
      <td>Data System</td>
    </tr>
    <tr>
      <td>11</td>
      <td>Microsoft SQL Server</td>
      <td>Data System</td>
    </tr>
    <tr>
      <td>12</td>
      <td>MongoDB</td>
      <td>Data System</td>
    </tr>
    <tr>
      <td>13</td>
      <td>MySQL</td>
      <td>Data System</td>
    </tr>
    <tr>
      <td>14</td>
      <td>Oracle</td>
      <td>Data System</td>
    </tr>
    <tr>
      <td>15</td>
      <td>Palantir Foundary</td>
      <td>Data System</td>
    </tr>
    <tr>
      <td>16</td>
      <td>PlanetScale</td>
      <td>Data System</td>
    </tr>
    <tr>
      <td>17</td>
      <td>PostgreSQL</td>
      <td>Data System</td>
    </tr>
    <tr>
      <td>18</td>
      <td>Rockset</td>
      <td>Data System</td>
    </tr>
    <tr>
      <td>19</td>
      <td>Snowflake</td>
      <td>Data System</td>
    </tr>
    <tr>
      <td>20</td>
      <td>Trino</td>
      <td>Data System</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>21</td>
      <td>Amazon S3</td>
      <td>Other</td>
    </tr>
    <tr>
      <td>22</td>
      <td>Azure Blob Storage</td>
      <td>Other</td>
    </tr>
    <tr>
      <td>23</td>
      <td>Google Cloud Storage</td>
      <td>Other</td>
    </tr>
    <tr>
      <td>24</td>
      <td>Metabase</td>
      <td>Other</td>
    </tr>
    <tr>
      <td>25</td>
      <td>Mixpanel Cohort</td>
      <td>Other</td>
    </tr>
    <tr>
      <td>26</td>
      <td>SFTP</td>
      <td>Other</td>
    </tr>
    <tr>
      <td>27</td>
      <td>Tableau</td>
      <td>Other</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>28</td>
      <td>Airtable</td>
      <td>Spreadsheets</td>
    </tr>
    <tr>
      <td>29</td>
      <td>Google Sheets</td>
      <td>Spreadsheets</td>
    </tr>
    <tr>
      <td>30</td>
      <td>Microsoft Excel</td>
      <td>Spreadsheets</td>
    </tr>
  </tbody>
</table>
</center>

</details>


<details><summary>List of Destinations supported by Hightouch</summary>

<table>
  <thead>
    <tr>
      <th>Sno.</th>
      <th>Connector Name</th>
      <th>Type</th>
      <th>Additional Capability</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>AlloyDB</td>
      <td>Databases</td>
      <td></td>
    </tr>
    <tr>
      <td>2</td>
      <td>CockroachDB</td>
      <td>Databases</td>
      <td>Developer tool and Advertising</td>
    </tr>
    <tr>
      <td>3</td>
      <td>DynamoDB</td>
      <td>Databases</td>
      <td></td>
    </tr>
    <tr>
      <td>4</td>
      <td>HubDB</td>
      <td>Databases</td>
      <td>Email, Sales, Live chat and help desk</td>
    </tr>
    <tr>
      <td>5</td>
      <td>IBMDB2</td>
      <td>Databases</td>
      <td></td>
    </tr>
    <tr>
      <td>6</td>
      <td>MariaDB</td>
      <td>Databases</td>
      <td>Developer Tool</td>
    </tr>
    <tr>
      <td>7</td>
      <td>MongoDB</td>
      <td>Databases</td>
      <td>Developer Tool</td>
    </tr>
    <tr>
      <td>8</td>
      <td>OracleDB</td>
      <td>Databases</td>
      <td></td>
    </tr>
    <tr>
      <td>9</td>
      <td>Firestore</td>
      <td>Databases</td>
      <td>Developer Tool</td>
    </tr>
    <tr>
      <td>10</td>
      <td>Hightouch Personalization API</td>
      <td>Databases</td>
      <td>Developer Tool and Product Experience</td>
    </tr>
    <tr>
      <td>11</td>
      <td>MySQL</td>
      <td>Databases</td>
      <td>Developer Tool</td>
    </tr>
    <tr>
      <td>12</td>
      <td>PostgreSQL</td>
      <td>Databases</td>
      <td>Developer Tool</td>
    </tr>
    <tr>
      <td>13</td>
      <td>Redis</td>
      <td>Databases</td>
      <td></td>
    </tr>
    <tr>
      <td>14</td>
      <td>Rockset</td>
      <td>Databases</td>
      <td>Developer Tool</td>
    </tr>
    <tr>
      <td>15</td>
      <td>SQLServer</td>
      <td>Databases</td>
      <td></td>
    </tr>
    <tr>
      <td>16</td>
      <td>Adobe Target</td>
      <td>Analytics</td>
      <td>Product Experience</td>
    </tr>
    <tr>
      <td>17</td>
      <td>Algolia</td>
      <td>Analytics</td>
      <td>Product Experience</td>
    </tr>
    <tr>
      <td>18</td>
      <td>Amplitude</td>
      <td>Analytics</td>
      <td></td>
    </tr>
    <tr>
      <td>19</td>
      <td>Calixa</td>
      <td>Analytics</td>
      <td>CRM and Customer Success</td>
    </tr>
    <tr>
      <td>20</td>
      <td>ChartMogul</td>
      <td>Analytics</td>
      <td></td>
    </tr>
    <tr>
      <td>21</td>
      <td>FullStory</td>
      <td>Analytics</td>
      <td>Product Experience and Surveys</td>
    </tr>
    <tr>
      <td>22</td>
      <td>Gainsight</td>
      <td>Analytics</td>
      <td>Customer Success, Product Experience and Surveys</td>
    </tr>
    <tr>
      <td>23</td>
      <td>GainsightPX</td>
      <td>Analytics</td>
      <td>Customer Success, Product Experience and Surveys</td>
    </tr>
    <tr>
      <td>24</td>
      <td>Google Analytics</td>
      <td>Analytics</td>
      <td></td>
    </tr>
    <tr>
      <td>25</td>
      <td>Heap</td>
      <td>Analytics</td>
      <td></td>
    </tr>
    <tr>
      <td>26</td>
      <td>Mixpanel</td>
      <td>Analytics</td>
      <td></td>
    </tr>
    <tr>
      <td>27</td>
      <td>MoEngage</td>
      <td>Analytics</td>
      <td>Email, SMS and Push</td>
    </tr>
    <tr>
      <td>28</td>
      <td>mParticle</td>
      <td>Analytics</td>
      <td></td>
    </tr>
    <tr>
      <td>29</td>
      <td>Optimizely</td>
      <td>Analytics</td>
      <td>Product Experience</td>
    </tr>
    <tr>
      <td>30</td>
      <td>Orbit</td>
      <td>Analytics</td>
      <td>CRM and Customer Success</td>
    </tr>
    <tr>
      <td>31</td>
      <td>Pendo</td>
      <td>Analytics</td>
      <td>Product Experience and Surveys</td>
    </tr>
    <tr>
      <td>32</td>
      <td>Planhat</td>
      <td>Analytics</td>
      <td>Customer Success</td>
    </tr>
    <tr>
      <td>33</td>
      <td>PostHog</td>
      <td>Analytics</td>
      <td>Product Experience</td>
    </tr>
    <tr>
      <td>34</td>
      <td>Rudderstack</td>
      <td>Analytics</td>
      <td></td>
    </tr>
    <tr>
      <td>35</td>
      <td>Segment</td>
      <td>Analytics</td>
      <td></td>
    </tr>
    <tr>
      <td>36</td>
      <td>Singular</td>
      <td>Analytics</td>
      <td></td>
    </tr>
    <tr>
      <td>37</td>
      <td>Statsig</td>
      <td>Analytics</td>
      <td>Product Experience</td>
    </tr>
    <tr>
      <td>38</td>
      <td>Vitally</td>
      <td>Analytics</td>
      <td>Customer Success and Surveys</td>
    </tr>
    <tr>
      <td>39</td>
      <td>Anaplan</td>
      <td>Finance and ERP</td>
      <td></td>
    </tr>
    <tr>
      <td>40</td>
      <td>Microsoft Dynamics 365</td>
      <td>Finance and ERP</td>
      <td></td>
    </tr>
    <tr>
      <td>41</td>
      <td>NetSuite (REST)</td>
      <td>Finance and ERP</td>
      <td></td>
    </tr>
    <tr>
      <td>42</td>
      <td>NetSuite (SOAP)</td>
      <td>Finance and ERP</td>
      <td></td>
    </tr>
    <tr>
      <td>43</td>
      <td>QuickBooks</td>
      <td>Finance and ERP</td>
      <td></td>
    </tr>
    <tr>
      <td>44</td>
      <td>Sage Intacct</td>
      <td>Finance and ERP</td>
      <td></td>
    </tr>
    <tr>
      <td>45</td>
      <td>SAPS/4HANA</td>
      <td>Finance and ERP</td>
      <td></td>
    </tr>
    <tr>
      <td>46</td>
      <td>Workday</td>
      <td>Finance and ERP</td>
      <td></td>
    </tr>
    <tr>
      <td>47</td>
      <td>Xero</td>
      <td>Finance and ERP</td>
      <td></td>
    </tr>
    <tr>
      <td>48</td>
      <td>Zuora</td>
      <td>Finance and ERP</td>
      <td>Payments</td>
    </tr>
    <tr>
      <td>49</td>
      <td>Azure Blob Storage</td>
      <td>File Storage</td>
      <td></td>
    </tr>
    <tr>
      <td>50</td>
      <td>Box</td>
      <td>File Storage</td>
      <td></td>
    </tr>
    <tr>
      <td>51</td>
      <td>Dropbox</td>
      <td>File Storage</td>
      <td></td>
    </tr>
    <tr>
      <td>52</td>
      <td>Google Cloud Storage</td>
      <td>File Storage</td>
      <td>Developer Tools</td>
    </tr>
    <tr>
      <td>53</td>
      <td>Google Drive</td>
      <td>File Storage</td>
      <td></td>
    </tr>
    <tr>
      <td>54</td>
      <td>Microsoft OneDrive</td>
      <td>File Storage</td>
      <td></td>
    </tr>
    <tr>
      <td>55</td>
      <td>S3</td>
      <td>File Storage</td>
      <td>Developer Tools</td>
    </tr>
    <tr>
      <td>56</td>
      <td>SFTP</td>
      <td>File Storage</td>
      <td>Developer Tools</td>
    </tr>
    <tr>
      <td>57</td>
      <td>ActiveCampaign</td>
      <td>CRM</td>
      <td>Email and Sales</td>
    </tr>
    <tr>
      <td>58</td>
      <td>Attio</td>
      <td>CRM</td>
      <td></td>
    </tr>
    <tr>
      <td>59</td>
      <td>Close</td>
      <td>CRM</td>
      <td>Email and Sales</td>
    </tr>
    <tr>
      <td>60</td>
      <td>Correlated</td>
      <td>CRM</td>
      <td></td>
    </tr>
    <tr>
      <td>61</td>
      <td>Freshsales</td>
      <td>CRM</td>
      <td>Email, Sales, Live chat and help desk</td>
    </tr>
    <tr>
      <td>62</td>
      <td>HubSpot</td>
      <td>CRM</td>
      <td>Email, Sales and Live chat and help desk</td>
    </tr>
    <tr>
      <td>63</td>
      <td>Kustomer</td>
      <td>CRM</td>
      <td>Customer Success, Email, Live chat and help desk, SMS and Push.</td>
    </tr>
    <tr>
      <td>64</td>
      <td>Microsoft Dynamics 365</td>
      <td>CRM</td>
      <td>Finance and ERP</td>
    </tr>
    <tr>
      <td>65</td>
      <td>NCR Advanced Marketing Solution</td>
      <td>CRM</td>
      <td>Advertising</td>
    </tr>
    <tr>
      <td>66</td>
      <td>Pipedrive</td>
      <td>CRM</td>
      <td>Email and Sales</td>
    </tr>
    <tr>
      <td>67</td>
      <td>Salesforce</td>
      <td>CRM</td>
      <td>Customer Success, and Sales</td>
    </tr>
    <tr>
      <td>68</td>
      <td>Salesforce (Sandbox)</td>
      <td>CRM</td>
      <td>Customer Success, and Sales</td>
    </tr>
    <tr>
      <td>69</td>
      <td>Salesloft</td>
      <td>CRM</td>
      <td>Email and Sales</td>
    </tr>
    <tr>
      <td>70</td>
      <td>Zoho CRM</td>
      <td>CRM</td>
      <td>Email and Sales</td>
    </tr>
    <tr>
      <td>71</td>
      <td>ChurnZero</td>
      <td>Customer Success</td>
      <td>Product Experience and Surveys</td>
    </tr>
    <tr>
      <td>72</td>
      <td>ClientSuccess</td>
      <td>Customer Success</td>
      <td></td>
    </tr>
    <tr>
      <td>73</td>
      <td>Freshdesk</td>
      <td>Customer Success</td>
      <td>Live Chat & help desk</td>
    </tr>
    <tr>
      <td>74</td>
      <td>Intercom</td>
      <td>Customer Success</td>
      <td>Email. Live chat & help desk, product experience, Sales and Surveys</td>
    </tr>
    <tr>
      <td>75</td>
      <td>Planhat</td>
      <td>Customer Success</td>
      <td></td>
    </tr>
    <tr>
      <td>76</td>
      <td>SMTP Email</td>
      <td>Customer Success</td>
      <td>Email</td>
    </tr>
    <tr>
      <td>77</td>
      <td>Totango</td>
      <td>Customer Success</td>
      <td></td>
    </tr>
    <tr>
      <td>78</td>
      <td>Amazon EventBridge</td>
      <td>Developer Tools</td>
      <td></td>
    </tr>
    <tr>
      <td>79</td>
      <td>Amazon Kinesis</td>
      <td>Developer Tools</td>
      <td></td>
    </tr>
    <tr>
      <td>80</td>
      <td>Amazon SNS</td>
      <td>Developer Tools</td>
      <td></td>
    </tr>
    <tr>
      <td>81</td>
      <td>Amazon SQS</td>
      <td>Developer Tools</td>
      <td></td>
    </tr>
    <tr>
      <td>82</td>
      <td>Apache Kafka</td>
      <td>Developer Tools</td>
      <td></td>
    </tr>
    <tr>
      <td>83</td>
      <td>Auth0</td>
      <td>Developer Tools</td>
      <td></td>
    </tr>
    <tr>
      <td>84</td>
      <td>AWS Lambda</td>
      <td>Developer Tools</td>
      <td></td>
    </tr>
    <tr>
      <td>85</td>
      <td>Azure Functions</td>
      <td>Developer Tools</td>
      <td></td>
    </tr>
    <tr>
      <td>86</td>
      <td>Embedded Destination</td>
      <td>Developer Tools</td>
      <td></td>
    </tr>
    <tr>
      <td>87</td>
      <td>Google Cloud Functions</td>
      <td>Developer Tools</td>
      <td></td>
    </tr>
    <tr>
      <td>88</td>
      <td>Google Cloud Pub/Sub</td>
      <td>Developer Tools</td>
      <td></td>
    </tr>
    <tr>
      <td>89</td>
      <td>HTTP Request</td>
      <td>Developer Tools</td>
      <td></td>
    </tr>
    <tr>
      <td>90</td>
      <td>RabbitMQ</td>
      <td>Developer Tools</td>
      <td></td>
    </tr>
    <tr>
      <td>91</td>
      <td>Webflow</td>
      <td>Developer Tools</td>
      <td></td>
    </tr>
    <tr>
      <td>92</td>
      <td>Zapier</td>
      <td>Developer Tools</td>
      <td></td>
    </tr>
    <tr>
      <td>93</td>
      <td>Attentive</td>
      <td>E-commerce</td>
      <td>SMS &amp; Push and Advertising</td>
    </tr>
    <tr>
      <td>94</td>
      <td>BigCommerce</td>
      <td>E-commerce</td>
      <td></td>
    </tr>
    <tr>
      <td>95</td>
      <td>Bloomreach</td>
      <td>E-commerce</td>
      <td>Email, SMS &amp; Push</td>
    </tr>
    <tr>
      <td>96</td>
      <td>Facebook Product Catalog</td>
      <td>E-commerce</td>
      <td>Advertising</td>
    </tr>
    <tr>
      <td>97</td>
      <td>Rokt</td>
      <td>E-commerce</td>
      <td>Advertising</td>
    </tr>
    <tr>
      <td>98</td>
      <td>Shopify</td>
      <td>E-commerce</td>
      <td></td>
    </tr>
    <tr>
      <td>99</td>
      <td>Acoustic</td>
      <td>Email</td>
      <td>SMS &amp; Push</td>
    </tr>
    <tr>
      <td>100</td>
      <td>Braze</td>
      <td>Email</td>
      <td>SMS &amp; Push</td>
    </tr>
    <tr>
      <td>101</td>
      <td>Braze Cohorts</td>
      <td>Email</td>
      <td>SMS &amp; Push</td>
    </tr>
    <tr>
      <td>102</td>
      <td>Campaign Monitor</td>
      <td>Email</td>
      <td></td>
    </tr>
    <tr>
      <td>103</td>
      <td>Campaigner</td>
      <td>Email</td>
      <td></td>
    </tr>
    <tr>
      <td>104</td>
      <td>Clever Tap</td>
      <td>Email</td>
      <td>SMS &amp; Push</td>
    </tr>
    <tr>
      <td>105</td>
      <td>Cordial</td>
      <td>Email</td>
      <td>SMS &amp; Push</td>
    </tr>
    <tr>
      <td>106</td>
      <td>Courier</td>
      <td>Email</td>
      <td>Internal Notification, SMS &amp; Push</td>
    </tr>
    <tr>
      <td>107</td>
      <td>Customer.io</td>
      <td>Email</td>
      <td>SMS &amp; Push</td>
    </tr>
    <tr>
      <td>108</td>
      <td>Drift</td>
      <td>Email</td>
      <td>Live chat &amp; help desk, Sales</td>
    </tr>
    <tr>
      <td>109</td>
      <td>Eloqua</td>
      <td>Email</td>
      <td></td>
    </tr>
    <tr>
      <td>110</td>
      <td>Emarsys</td>
      <td>Email</td>
      <td>SMS and Push</td>
    </tr>
    <tr>
      <td>111</td>
      <td>Help Scout</td>
      <td>Email</td>
      <td>Live chat &amp; help desk</td>
    </tr>
    <tr>
      <td>112</td>
      <td>Iterable</td>
      <td>Email</td>
      <td>SMS &amp; Push</td>
    </tr>
    <tr>
      <td>113</td>
      <td>Klaviyo</td>
      <td>Email</td>
      <td>SMS &amp; Push</td>
    </tr>
    <tr>
      <td>114</td>
      <td>Mailchimp</td>
      <td>Email</td>
      <td></td>
    </tr>
    <tr>
      <td>115</td>
      <td>Marketo</td>
      <td>Email</td>
      <td></td>
    </tr>
    <tr>
      <td>116</td>
      <td>OneSignal</td>
      <td>Email</td>
      <td>SMS &amp; Push</td>
    </tr>
    <tr>
      <td>117</td>
      <td>Ortto</td>
      <td>Email</td>
      <td>SMS &amp; Push</td>
    </tr>
    <tr>
      <td>118</td>
      <td>Outreach</td>
      <td>Email</td>
      <td>Sales</td>
    </tr>
    <tr>
      <td>119</td>
      <td>Reply.io</td>
      <td>Email</td>
      <td>Sales</td>
    </tr>
    <tr>
      <td>120</td>
      <td>Responsys</td>
      <td>Email</td>
      <td></td>
    </tr>
    <tr>
      <td>121</td>
      <td>Retention Science</td>
      <td>Email</td>
      <td></td>
    </tr>
    <tr>
      <td>122</td>
      <td>Sailthru</td>
      <td>Email</td>
      <td>SMS &amp; Push</td>
    </tr>
    <tr>
      <td>123</td>
      <td>Salesforce Marketing Cloud</td>
      <td>Email</td>
      <td></td>
    </tr>
    <tr>
      <td>124</td>
      <td>Salesforce Pardot</td>
      <td>Email</td>
      <td></td>
    </tr>
    <tr>
      <td>125</td>
      <td>Salesforce Pardot (Sandbox)</td>
      <td>Email</td>
      <td></td>
    </tr>
    <tr>
      <td>126</td>
      <td>SendGrid</td>
      <td>Email</td>
      <td></td>
    </tr>
    <tr>
      <td>127</td>
      <td>Vero</td>
      <td>Email</td>
      <td></td>
    </tr>
    <tr>
      <td>128</td>
      <td>Mattermost</td>
      <td>Internal Notifications</td>
      <td></td>
    </tr>
    <tr>
      <td>129</td>
      <td>Microsoft Teams</td>
      <td>Internal Notifications</td>
      <td></td>
    </tr>
    <tr>
      <td>130</td>
      <td>Slack</td>
      <td>Internal Notifications</td>
      <td></td>
    </tr>
    <tr>
      <td>131</td>
      <td>Front</td>
      <td>Live chat &amp; help desk</td>
      <td></td>
    </tr>
    <tr>
      <td>132</td>
      <td>Gladly</td>
      <td>Live chat &amp; help desk</td>
      <td></td>
    </tr>
    <tr>
      <td>133</td>
      <td>Zendesk</td>
      <td>Live chat &amp; help desk</td>
      <td></td>
    </tr>
    <tr>
      <td>134</td>
      <td>Chargebee</td>
      <td>Payments</td>
      <td></td>
    </tr>
    <tr>
      <td>135</td>
      <td>Stripe</td>
      <td>Payments</td>
      <td></td>
    </tr>
    <tr>
      <td>136</td>
      <td>Zuora</td>
      <td>Payments</td>
      <td></td>
    </tr>
    <tr>
      <td>137</td>
      <td>Appcues</td>
      <td>Product Experience</td>
      <td>Surveys</td>
    </tr>
    <tr>
      <td>138</td>
      <td>Chameleon</td>
      <td>Product Experience</td>
      <td></td>
    </tr>
    <tr>
      <td>139</td>
      <td>LaunchDarkly</td>
      <td>Product Experience</td>
      <td></td>
    </tr>
    <tr>
      <td>140</td>
      <td>Userflow</td>
      <td>Product Experience</td>
      <td></td>
    </tr>
    <tr>
      <td>141</td>
      <td>Airtable</td>
      <td>Productivity Tools</td>
      <td></td>
    </tr>
    <tr>
      <td>142</td>
      <td>Asana</td>
      <td>Productivity Tools</td>
      <td></td>
    </tr>
    <tr>
      <td>143</td>
      <td>ClickUp</td>
      <td>Productivity Tools</td>
      <td></td>
    </tr>
    <tr>
      <td>144</td>
      <td>Google Sheets</td>
      <td>Productivity Tools</td>
      <td></td>
    </tr>
    <tr>
      <td>145</td>
      <td>Google Sheets (Service Account)</td>
      <td>Productivity Tools</td>
      <td></td>
    </tr>
    <tr>
      <td>146</td>
      <td>Jira</td>
      <td>Productivity Tools</td>
      <td></td>
    </tr>
    <tr>
      <td>147</td>
      <td>Microsoft Excel</td>
      <td>Productivity Tools</td>
      <td></td>
    </tr>
    <tr>
      <td>148</td>
      <td>Notion</td>
      <td>Productivity Tools</td>
      <td></td>
    </tr>
    <tr>
      <td>149</td>
      <td>ServiceNow</td>
      <td>Productivity Tools</td>
      <td></td>
    </tr>
    <tr>
      <td>150</td>
      <td>KakaoTalk</td>
      <td>SMS &amp; Push</td>
      <td></td>
    </tr>
    <tr>
      <td>151</td>
      <td>Line</td>
      <td>SMS &amp; Push</td>
      <td></td>
    </tr>
    <tr>
      <td>152</td>
      <td>WhatsApp</td>
      <td>SMS &amp; Push</td>
      <td></td>
    </tr>
    <tr>
      <td>153</td>
      <td>Gong</td>
      <td>Sales</td>
      <td></td>
    </tr>
    <tr>
      <td>154</td>
      <td>Partnerstack</td>
      <td>Sales</td>
      <td></td>
    </tr>
    <tr>
      <td>156</td>
      <td>Delighted</td>
      <td>Surveys</td>
      <td></td>
    </tr>
    <tr>
      <td>157</td>
      <td>Qualtrics</td>
      <td>Surveys</td>
      <td></td>
    </tr>
    <tr>
      <td>158</td>
      <td>User Interviews</td>
      <td>Surveys</td>
      <td></td>
    </tr>
    <tr>
      <td>159</td>
      <td>Amazon Ads</td>
      <td>Advertising</td>
      <td></td>
    </tr>
    <tr>
      <td>160</td>
      <td>Amobee</td>
      <td>Advertising</td>
      <td></td>
    </tr>
    <tr>
      <td>161</td>
      <td>Beeswax</td>
      <td>Advertising</td>
      <td></td>
    </tr>
    <tr>
      <td>162</td>
      <td>Bing Ads</td>
      <td>Advertising</td>
      <td></td>
    </tr>
    <tr>
      <td>163</td>
      <td>CitrusAd</td>
      <td>Advertising</td>
      <td></td>
    </tr>
    <tr>
      <td>164</td>
      <td>Criteo</td>
      <td>Advertising</td>
      <td></td>
    </tr>
    <tr>
      <td>165</td>
      <td>eBay</td>
      <td>Advertising</td>
      <td></td>
    </tr>
    <tr>
      <td>166</td>
      <td>Facebook Conversions</td>
      <td>Advertising</td>
      <td></td>
    </tr>
    <tr>
      <td>167</td>
      <td>Facebook Custom Audiences</td>
      <td>Advertising</td>
      <td></td>
    </tr>
    <tr>
      <td>168</td>
      <td>Facebook Offline Conversions</td>
      <td>Advertising</td>
      <td></td>
    </tr>
    <tr>
      <td>169</td>
      <td>Google Ad Manager 360</td>
      <td>Advertising</td>
      <td></td>
    </tr>
    <tr>
      <td>170</td>
      <td>Google Ads</td>
      <td>Advertising</td>
      <td></td>
    </tr>
    <tr>
      <td>171</td>
      <td>Google Campaign Manager 360</td>
      <td>Advertising</td>
      <td></td>
    </tr>
    <tr>
      <td>172</td>
      <td>Google Display &amp; Video 360</td>
      <td>Advertising</td>
      <td></td>
    </tr>
    <tr>
      <td>173</td>
      <td>Google Search Ads 360</td>
      <td>Advertising</td>
      <td></td>
    </tr>
    <tr>
      <td>174</td>
      <td>LinkedIn Ads</td>
      <td>Advertising</td>
      <td></td>
    </tr>
    <tr>
      <td>175</td>
      <td>NCR Advanced Marketing Solution</td>
      <td>Advertising</td>
      <td></td>
    </tr>
    <tr>
      <td>176</td>
      <td>Pinterest Ads</td>
      <td>Advertising</td>
      <td></td>
    </tr>
    <tr>
      <td>177</td>
      <td>Reddit Ads</td>
      <td>Advertising</td>
      <td></td>
    </tr>
    <tr>
      <td>178</td>
      <td>Rokt</td>
      <td>Advertising</td>
      <td></td>
    </tr>
    <tr>
      <td>179</td>
      <td>Snapchat</td>
      <td>Advertising</td>
      <td></td>
    </tr>
    <tr>
      <td>180</td>
      <td>Spotify</td>
      <td>Advertising</td>
      <td></td>
    </tr>
    <tr>
      <td>181</td>
      <td>StackAdapt</td>
      <td>Advertising</td>
      <td></td>
    </tr>
    <tr>
      <td>182</td>
      <td>The Trade Desk</td>
      <td>Advertising</td>
      <td></td>
    </tr>
    <tr>
      <td>183</td>
      <td>TikTok</td>
      <td>Advertising</td>
      <td></td>
    </tr>
    <tr>
      <td>184</td>
      <td>Twitter Ads</td>
      <td>Advertising</td>
      <td></td>
    </tr>
    <tr>
      <td>185</td>
      <td>Yahoo</td>
      <td>Advertising</td>
      <td></td>
    </tr>
  </tbody>
</table>

</details>

