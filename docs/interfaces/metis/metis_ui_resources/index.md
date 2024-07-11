# Metadata of DataOS Resources

MetisDB serves as a comprehensive repository for detailed information about various DataOS Resources, including workflows, services, clusters, computes, secrets, and more, along with user interactions. 


## Resource Details
MetisDB stores comprehensive details about DataOS Resources such as workflows, Services, Clusters, Computes, Secrets, etc. and user interactions. Refer to the following to get all the details surfaced for each of the resources on Metis UI.

### **Quick Overview**
| Entity          | Filter    | Card View  | Side Pane View | Details Page   |
| --------------- | --------- | ---------- | -------------- | --------------- |
| Workflow        | 1. Workspace<br>2. Domain<br>3. Owner<br>4. Tag<br>5. Tier | 1. Name<br>2. Description<br>3. Tags<br>4. Owner<br>5. Tier<br>6. Domain<br>7. Workspace | 1. Name<br>2. Description<br>3. Workspace<br>4. Version<br>5. State<br>6. Followers Count<br>7. Last Updated<br>8. Jobs (Name and Description) | 1. Meta Version<br>2. Follow<br>3. Learn<br>4. Delete<br>5. Owner<br>6. Tier<br>7. Domain<br>8. Tags<br>9. Request description/Tags Update(?)<br>10. Edit description<br>12. Start Conversation<br>**Tabs**<br>1. Details<br>   a. Workspace<br>   b. Version<br>   c. State<br>   d. Aggregate Status<br>   e. Builder State<br>   f. Runtime State<br>   g. Lifecycle Event(s)<br>2. Jobs<br>3. Activity Feeds and Tasks<br>4. Run History<br>5. Manifest |
| Service          | 1. Workspace<br>2. Owner<br>3. Tag<br>4. Tier | 1. Name<br>2. Description<br>3. Tags<br>4. Owner<br>5. Tier<br>6. Domain<br>7. Workspace | 1. Name<br>2. Description<br>3. Workspace<br>4. Version<br>5. State<br>6. Followers Count<br>7. Last Updated | 1. Meta Version<br>2. Follow<br>3. Learn<br>4. Delete<br>5. Owner<br>6. Tier<br>7. Domain<br>8. Tags<br>9. Request description/Tags Update(?)<br>10. Edit description<br>12. Start Conversation<br>**Tabs**<br>1. Details<br>   a. Workspace<br>   b. Version<br>   c. State<br>   d. Aggregate Status<br>   e. Builder State<br>   f. Service Port<br>   g. Replicas<br>   h. Stack<br>   i. Compute<br>   j. Run As User<br>   k. Configurations<br>      - Ingress<br>      - Auto Scaling<br>      - Requests<br>      - Limits<br>   l. Stack Specifications<br>   m. Life Cycle Events<br>2. Topology<br>3. Activity Feeds and Tasks<br>4. Run Time<br>   a. Run name<br>   b. Status<br>   c. Started At<br>   d. Duration<br>   e. Date Filter<br>5. Manifest |
| Depot           | 1. Depot Source<br>2. Domain<br>3. Owner<br>4. Tag<br>5. Tier | 1. Name<br>2. Description<br>3. Tags<br>4. Owner<br>5. Tier<br>6. Domain | 1. Name<br>2. Description<br>3. Type<br>4. Layer<br>5. Version<br>6. State<br>7. Followers Count<br>8. Last Updated | 1. Meta Version<br>2. Follow<br>3. Learn<br>4. Delete<br>5. Owner<br>6. Tier<br>7. Domain<br>8. Tags<br>9. Request description/Tags Update(?)<br>10. Edit description<br>12. Start Conversation<br>**Tabs**<br>1. Details<br>   a. Type<br>   b. Layer<br>   c. Version<br>   d. State<br>   e. Aggregate Status<br>   f. Builder State<br>   f. Run As User<br>   g. Configurations<br>      - Requests<br>      - Limits<br>   h. Spec<br>   i. Life Cycle Events<br>2. Activity Feeds and Tasks<br>3. Manifest |
| Cluster         | 1. Workspace<br>2. Domain<br>3. Owner<br>4. Tag<br>5. Tier | 1. Name<br>2. Description<br>3. Tags<br>4. Owner<br>5. Tier<br>6. Domain<br>7. Workspace | 1. Name<br>2. Description<br>3. Engine<br>4. Workspace<br>5. Version<br>6. State<br>7. Followers Count<br>8. Last Updated | 1. Meta Version<br>2. Follow<br>3. Learn<br>4. Delete<br>5. Owner<br>6. Tier<br>7. Domain<br>8. Tags<br>9. Request description/Tags Update(?)<br>10. Edit description<br>12. Start Conversation<br>**Tabs**<br>1. Details<br>   a. Engine<br>   b. Workspace<br>   c. Version<br>   d. State<br>   e. Aggregate Status<br>   f. Builder State<br>   f. Compute<br>   g. Run As User<br>   h. Lifecycle Event(s)<br>2. Activity Feeds and Tasks<br>4. Runtime<br>5. Manifest |
| Bundle          | 1. Owner<br>2. Tag<br>3. Tier | 1. Name<br>2. Description<br>3. Tags<br>4. Owner<br>5. Tier<br>6. Domain | 1. Name<br>2. Description<br>3. Layer<br>4. Version<br>5. State<br>6. Followers Count<br>7. Last Updated | 1. Meta Version<br>2. Follow<br>3. Learn<br>4. Delete<br>5. Owner<br>6. Tier<br>7. Domain<br>8. Tags<br>9. Request description/Tags Update(?)<br>10. Edit description<br>12. Start Conversation<br>**Tabs**<br>1. Details<br>   a. Layer<br>   b. Version<br>   c. State<br>   d. Aggregate Status<br>   e. Builder State<br>   f. Workspace(s)<br>   g. Life Cycle Events<br>2. Resources<br>   a. Dag<br>   b. List<br>      - Name<br>      - Description<br>      - Type<br>3. Activity Feeds and Tasks<br>4. Run History<br>5. Manifest |
| Worker          | 1. Workspace<br>2. Owner<br>3. Tag | 1. Name<br>2. Description<br>3. Tags<br>4. Owner<br>5. Tier<br>6. Domain<br>7. Workspace | 1. Name<br>2. Description<br>3. Workspace<br>4. Version<br>5. State<br>6. Followers Count<br>7. Last Updated | 1. Meta Version<br>2. Follow<br>3. Learn<br>4. Delete<br>5. Owner<br>6. Tier<br>7. Domain<br>8. Tags<br>9. Request description/Tags Update(?)<br>10. Edit description<br>12. Start Conversation<br>**Tabs**<br>1. Details<br>
| Policy           | 1. Owner<br>2. Tag | 1. Name<br>2. Description<br>3. Tags<br>4. Owner<br>5. Tier<br>6. Domain | 1. Name<br>2. Description<br>3. Type<br>4. Layer<br>5. Version<br>6. State<br>7. Followers Count<br>8. Last Updated<br>9. Spec | 1. Meta Version<br>2. Follow<br>3. Learn<br>4. Delete<br>5. Owner<br>6. Tier<br>7. Domain<br>8. Tags<br>9. Request description/Tags Update(?)<br>10. Edit description<br>12. Start Conversation<br>**Tabs**<br>1. Details<br>   a. Type<br>   b. Layer<br>   c. Version<br>   d. State<br>   e. Aggregate Status<br>   f. Builder State<br>   g. Priority<br>   h. Policy Type<br>   i. Spec<br>   j. Lifecycle Event(s)<br>2. Activity Feeds and Tasks<br>3. Manifest |
| Stack            | 1. Owner<br>2. Tag | 1. Name<br>2. Description<br>3. Tags<br>4. Owner<br>5. Tier<br>6. Domain | 1. Name<br>2. Description<br>3. Layer<br>4. Version<br>5. Reconciler<br>6. State<br>7. Followers Count<br>8. Last Updated | 1. Meta Version<br>2. Follow<br>3. Learn<br>4. Delete<br>5. Owner<br>6. Tier<br>7. Domain<br>8. Tags<br>9. Request description/Tags Update(?)<br>10. Edit description<br>12. Start Conversation<br>**Tabs**<br>1. Details<br>   a. Layer<br>   b. Version<br>   c. Reconciler<br>   d. SecrtetProjection type<br>   e. DataOS Stack Version<br>   f. Flavour<br>   g. State<br>   h. Aggregate Status<br>   i. Builder State<br>   j. Lifecycle Event(s)<br>2. Activity Feeds and Tasks<br>3. Manifest |
| Database         | 1. Workspace<br>2. Owner<br>3. Tag<br>4. Tier | 1. Name<br>2. Description<br>3. Tags<br>4. Owner<br>5. Tier<br>6. Domain<br>7. Workspace | 1. Name<br>2. Description<br>3. Workspace<br>4. Version<br>5. State<br>6. Followers Count<br>7. Last Updated | 1. Meta Version<br>2. Follow<br>3. Learn<br>4. Delete<br>5. Owner<br>6. Tier<br>7. Domain<br>8. Tags<br>9. Request description/Tags Update(?)<br>10. Edit description<br>12. Start Conversation<br>**Tabs**<br>1. Details<br>   a. Workspace<br>   b. Version<br>   c. State<br>   d. Bundle(s)<br>2. Activity Feeds and Tasks<br>3. Manifest |
| Compute          | 1. Domain<br>2. Owner<br>3. Tier | 1. Name<br>2. Description<br>3. Tags<br>4. Owner<br>5. Tier<br>6. Domain | 1. Name<br>2. Description<br>3. Layer<br>4. Version<br>5. State<br>6. Followers Count<br>7. Last Updated | 1. Meta Version<br>2. Follow<br>3. Learn<br>4. Delete<br>5. Owner<br>6. Tier<br>7. Domain<br>8. Tags<br>9. Request description/Tags Update(?)<br>10. Edit description<br>12. Start Conversation<br>**Tabs**<br>1. Details<br>   a. Layer<br>   b. Version<br>   c. Data Plane<br>   d. State<br>   e. Aggregate Status<br>   f. Builder State<br>   g. Bundles<br>   h. Lifecycle Event(s)<br>2. Activity Feeds and Tasks<br>3. Manifest |
| Secret           | 1. Workspace<br>2. Owner<br>3. Tag<br>4. Tier | 1. Name<br>2. Description<br>3. Tags<br>4. Owner<br>5. Tier<br>6. Domain<br>7. Workspace | 1. Name<br>2. Description<br>3. Workspace<br>4. Version<br>5. State<br>6. Followers Count<br>7. Last Updated | 1. Meta Version<br>2. Follow<br>3. Learn<br>4. Delete<br>5. Owner<br>6. Tier<br>7. Domain<br>8. Tags<br>9. Request description/Tags Update(?)<br>10. Edit description<br>12. Start Conversation<br>**Tabs**<br>1. Details<br>   a. Workspace<br>   b. Version<br>   c. State<br>   d. Aggregate Status<br>   e. Builder State<br>   f. Bundles<br>   g. Lifecycle Event(s)<br>2. Activity Feeds and Tasks<br>3. Manifest |
| Monitors         | 1. Owner<br>2. Tags | 1. Name<br>2. Description<br>3. Tags<br>4. Owner<br>5. Tier<br>6. Domain<br>7. Workspace | 1. Name<br>2. Description<br>3. Workspace<br>4. Version<br>5. State<br>6. Followers Count<br>7. Last Updated | 1. Meta Version<br>2. Follow<br>3. Learn<br>4. Delete<br>5. Owner<br>6. Tier<br>7. Domain<br>8. Tags<br>9. Request description/Tags Update(?)<br>10. Edit description<br>12. Start Conversation<br>**Tabs**<br>1. Details<br>   a. Workspace<br>   b. Version<br>   c. State<br>   d. Aggregate Status<br>   e. Builder State<br>   f. Lifecycle Event(s)<br>2. Activity Feeds and Tasks<br>3. Manifest |
| Lakehouses       | 1. Owner<br>2. Tag | 1. Name<br>2. Description<br>3. Tags<br>4. Owner<br>5. Tier<br>6. Domain<br>7. Workspace | 1. Name<br>2. Description<br>3. Workspace<br>4. Version<br>5. State<br>6. Followers Count<br>7. Last Updated | 1. Meta Version<br>2. Follow<br>3. Learn<br>4. Delete<br>5. Owner<br>6. Tier<br>7. Domain<br>8. Tags<br>9. Request description/Tags Update(?)<br>10. Edit description<br>12. Start Conversation<br>**Tabs**<br>1. Details<br>   a. Workspace<br>   b. Version<br>   c. State<br>   d. Aggregate Status<br>   e. Builder State<br>   f. Compute<br>   g. Run As User<br>   h. Lifecycle Event(s)<br>2. Activity Feeds and Tasks<br>3. Manifest |
| Instance Secrets | 1. Owner<br>2. Tag | 1. Name<br>2. Description<br>3. Tags<br>4. Owner<br>5. Tier<br>6. Domain | 1. Name<br>2. Description<br>3. Version<br>4. State<br>5. Followers Count<br>6. Last Updated | 1. Meta Version<br>2. Follow<br>3. Learn<br>4. Delete<br>5. Owner<br>6. Tier<br>7. Domain<br>8. Tags<br>9. Request description/Tags Update(?)<br>10. Edit description<br>12. Start Conversation<br>**Tabs**<br>1. Details<br>   a. Version<br>   b. State<br>   c. Aggregate Status<br>   d. Builder State<br>   e. Lifecycle Event(s)<br>2. Activity Feeds and Tasks<br>3. Manifest |
| Operators        | 1. Domain<br>2. Owner<br>3. Tag | 1. Name<br>2. Description<br>3. Tags<br>4. Owner<br>5. Tier<br>6. Domain | 1. Name<br>2. Description<br>3. Version<br>4. State<br>5. Followers Count<br>6. Last Updated | 1. Meta Version<br>2. Follow<br>3. Learn<br>4. Delete<br>5. Owner<br>6. Tier<br>7. Domain<br>8. Tags<br>9. Request description/Tags Update(?)<br>10. Edit description<br>12. Start Conversation<br>**Tabs**<br>1. Details<br>   a. Version<br>   b State<br>   c. Aggregate Status<br>   d. Builder State<br>   e. Configurations<br>   f. Lifecycle Event(s)<br>2. Activity Feeds and Tasks<br>3. Manifest |
| Pagers           | 1. Owner<br>2. Tag<br>3. Tier | 1. Name<br>2. Description<br>3. Tags<br>4. Owner<br>5. Tier<br>6. Domain<br>7. Workspace | 1. Name<br>2. Description<br>3. Workspace<br>4. Version<br>5. State<br>6. Followers Count<br>7. Last Updated | 1. Meta Version<br>2. Follow<br>3. Learn<br>4. Delete<br>5. Owner<br>6. Tier<br>7. Domain<br>8. Tags<br>9. Request description/Tags Update(?)<br>10. Edit description<br>12. Start Conversation<br>**Tabs**<br>1. Details<br>   a. Workspace<br>   b. Version<br>   c. State<br>   d. Aggregate Status<br>   e. Builder State<br>   f. Lifecycle Event(s)<br>2. Activity Feeds and Tasks<br>3. Manifest |

### **Comprehensive View**
To deep dive into the wealth of details available, refer to the following sections on the Metis UI:

#### **Workflows**

To access metadata of Workflows on Metis UI, click [here](/interfaces/metis/metis_ui_resources/metis_resources_workflows/).

#### **Services**
To access metadata of Services on Metis UI, click [here](/interfaces/metis/metis_ui_resources/metis_resources_services/).

#### **Depots**
To access metadata of Depots on Metis UI, click [here](/interfaces/metis/metis_ui_resources/metis_resources_depots/).

#### **Clusters**
To access metadata of Clusters on Metis UI, click [here](/interfaces/metis/metis_ui_resources/metis_resources_clusters/).

#### **Bundles**
To access metadata of Bundles on Metis UI, click [here](/interfaces/metis/metis_ui_resources/metis_resources_bundles/).

#### **Workers**
To access metadata of Workers on Metis UI, click [here](/interfaces/metis/metis_ui_resources/metis_resources_workers/).

#### **Policies**
To access metadata of Policies on Metis UI, click [here](/interfaces/metis/metis_ui_resources/metis_resources_policies/).

#### **Stacks**
To access metadata of Stacks on Metis UI, click [here](/interfaces/metis/metis_ui_resources/metis_resources_stacks/).

#### **Databases**
To access metadata of Databases on Metis UI, click [here](/interfaces/metis/metis_ui_resources/metis_resources_databases/).

#### **Computes**
To access metadata of Computes on Metis UI, click [here](/interfaces/metis/metis_ui_resources/metis_resources_computes/).

#### **Secrets**
To access metadata of Secrets on Metis UI, click [here](/interfaces/metis/metis_ui_resources/metis_resources_secrets/).

#### **Monitors**
To access metadata of Monitors on Metis UI, click [here](/interfaces/metis/metis_ui_resources/metis_resources_monitors/).

#### **Lakehouses**
To access metadata of Lakehouses on Metis UI, click [here](/interfaces/metis/metis_ui_resources/metis_resources_lakehouses/).

#### **Instance Secrets**
To access metadata of Instance Secrets on Metis UI, click [here](/interfaces/metis/metis_ui_resources/metis_resources_instance_secrets/).

#### **Operators**
To access metadata of Operators on Metis UI, click [here](/interfaces/metis/metis_ui_resources/metis_resources_operators/).

#### **Pagers**
To access metadata of Pagers on Metis UI, click [here](/interfaces/metis/metis_ui_resources/metis_resources_pagers/).