# Pre-defined Roles and Policies

Metis supports defining roles and policies for metadata operations. A user can be assigned roles. The policies define the set of permissions in the form of rules about what users can do with metadata, for example, whether users can only view metadata or update tags, add descriptions to data assets, change owners, or create a glossary.

In metis, a user must have `Admin` role to configure roles and policies for performing metadata operation. Once the Metis admin creates these roles and policies, roles can be assigned to users on Metis UI.

## Getting Admin Role

A DataOS user  with the `roles:id:operator` tag are designated as dataOS operators. These operators possess full access privileges within the Metis component and are automatically assigned the 'Admin' role. 

Within the Metis user interface (UI), users holding the 'Admin' role enjoy additional privileges, including the ability to assign the `Admin` role to other users. It's important to note that these users being assigned the `Admin` role may not necessarily possess the `roles:id:operator` tag. By granting the 'Admin' role to other users, they are empowered with the capability to create roles and policies within Metis.

<aside class="callout">
🗣 To obtain the required use case and Metis admin role, please contact the DataOS system administrator.

</aside>

## Personas for Metis GUI

There is a direct 1-to-1 mapping between roles and policies, within further bifurcation in rules.

### **Roles**

| Persona | Description |
| --- | --- |
| Admin | They oversee onboarding users, assign roles, and manage members and their permissions. By default, they have all the permissions. |
| Data Governor | Compliance within the organization will be ensured by DevOps members in this role. In addition to creating tags, they will also define policies. Within the organization, everything related to governance. |
| Data Steward | Data Stewards are the know-how around the business or organizational data. They associate the right semantics with the data assets. |
| Data Owner | Data Owners are individuals who create a dataset or onboard a dataset. This role is intended for developers who want to manage workflows, pipelines, and data sources. They will also be responsible for managing metadata and ensuring the permissions and quality of their dataset.  |
| Data Consumer | These are data Consumers accessing data through a variety of tools to complete their day-to-day tasks. For instance, they can be a data analyst responsible for managing and supporting the data and analytical needs of their team.  |

### **Policies**

| Policy | Rules | Permission |
| --- | --- | --- |
| Admin Policy | Access Management | Ops: ALL
Resources: User, Team, Role, Policy |
|  | Taxonomy  Management | Ops: ALL
Resources: Tags, Tag Category, Glossary, Glossary Term, Type |
|  | Asset Management | Ops: ALL
Resources: Table, Storage Source, Database, Database Schema, Database Source, Dashboard, Dashboard Source, Charts, Metrics, MLmodel, MLmodel Source, Workflow, Workflow Source, Messaging Source, Topics, Test Suites, Webhook |
| Governance Policy | Policy Management | Ops: Create, EditAll, ViewAll
Resources: Policy, Role |
|  | Taxonomy Management | Ops: EditAll, ViewAll
Resources: Tags, Tag Category, Glossary, Glossary Term, Type, Table |
| Data Owner | Metadata Management | Ops: Edit Lineage, ViewAll, EditAll, EditDescription, EditDisplayName, EditCustomFields
Resources: Workflow, Topics, Table, MLModel, Dashboard, Charts, Test Suites, Webhook, Storage Source, Database Schema, Database Source, Messaging Source, Dashboard Source, Workflow Source, MLmodel Source |
| Data Steward | Metadata Management | Ops: EditTags, EditDescription, EditDisplayName, ViewAll
Resources: Workflow, Table, Metrics, Dashboard, Charts, Dashboard Source, MLModel |

<aside class="callout">
🗣 Initially, all users are assigned a Data Consumer role, which enables them to have view access to all assets in Metis.

</aside>