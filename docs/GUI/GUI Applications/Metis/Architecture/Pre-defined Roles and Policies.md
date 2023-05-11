# Pre-defined Roles and Policies

Metis supports defining roles and policies for metadata operations. A User can be assigned Roles. The policies define the set of permissions in the form of rules about what users can do with metadata, for example, whether users can only view metadata or update tags, add descriptions to data assets, change owners or create a glossary.

Once the Metis admin creates these roles and policies, roles can be assigned to users on Metis UI.

> 🗣 You can contact the DataOS system administrator to assign you the ‘admin’ role from Metis UI. The system administrator can also give an admin role for Metis by adding `roles:direct:metis` tag to your DataOS user profile.

## Personas for Metis GUI

There is a direct 1-to-1 mapping between roles and policies, within further bifurcation in rules.

## Roles

| Persona | Description |
| --- | --- |
| Admin | They oversee onboarding users, assign roles, and manage members and their permissions. By default, they have all the permissions. |
| Data Governor | Compliance within the organization will be ensured by DevOps members in this role. In addition to creating tags, they will also define policies. Within the organization, everything related to governance. |
| Data Steward | Data Stewards are the know-how around the business or organizational data. They associate the right semantics with the data assets. |
| Data Owner | Data Owners are individuals who create a dataset or onboard a dataset. This role is intended for developers who want to manage workflows, pipelines, and data sources. They will also be responsible for managing metadata and ensuring the permissions and quality of their dataset.  |
| Data Consumer | These are data Consumers accessing data through a variety of tools to complete their day-to-day tasks. For instance, they can be a data analyst responsible for managing and supporting the data and analytical needs of their team.  |

## Policies

| Policy | Rules | Permission |
| --- | --- | --- |
| Admin Policy | Access Management | Ops: ALL <br> Resources: User, Team, Role, Policy |
|  | Taxonomy  Management | Ops: ALL <br> Resources: Tags, Tag Category, Glossary, Glossary Term, Type |
|  | Asset Management | Ops: ALL <br> Resources: Table, Storage Source, Database, Database Schema, Database Source, Dashboard, Dashboard Source, Charts, Metrics, MLmodel, MLmodel Source, Workflow, Workflow Source, Messaging Source, Topics, Test Suites, Webhook |
| Governance Policy | Policy Management | Ops: Create, EditAll, ViewAll <br> Resources: Policy, Role |
|  | Taxonomy Management | Ops: EditAll, ViewAll <br> Resources: Tags, Tag Category, Glossary, Glossary Term, Type, Table |
| Data Owner | Metadata Management | Ops: Edit Lineage, ViewAll, EditAll, EditDescription, EditDisplayName, EditCustomFields <br> Resources: Workflow, Topics, Table, MLModel, Dashboard, Charts, Test Suites, Webhook, Storage Source, Database Schema, Database Source, Messaging Source, Dashboard Source, Workflow Source, MLmodel Source |
| Data Steward | Metadata Management | Ops: EditTags, EditDescription, EditDisplayName, ViewAll <br> Resources: Workflow, Table, Metrics, Dashboard, Charts, Dashboard Source, MLModel |

> 🗣  Initially, all users are assigned a Data Consumer role which enables them to have view access to all assets in Metis.

## Data Policies

| Policy | Description |
| --- | --- |
| `PII.age` | An age bucket is formed by grouping the ages together. Based on defined age buckets, the age of individuals is redacted and anonymized. If an individual’s age falls under a defined bucket, it is replaced with the lowest value of the bucket.  |
| `PII.income` | Incomes are grouped into buckets to represent different income ranges. An individual's income is redacted and anonymized with the lowest value in the bucket. |
| `PHI.date_of_birth` <br> `PII.date_of_birth` | Groups the date of births into buckets and redacts it to either(hour/day/week/month). By replacing the Date of Birth with the bucket's lower value, an individual's Date of Birth is hidden. |
| `PII.name` | Masks an individual’s name by replacing it with a generated hash against the value. |
| `PII.social_security_number` | By replacing an individual's Personal ID number with a random string of the same length, it masks their identity. The column data type is preserved. |
| `PII.email` | Masks an individual’s email address by replacing it with a generated hash against the value. |
| `PII.location` | The location of all individuals is redacted and replaced with a constant value ‘REDACTED’. Location can be classified as an individual’s address, zip code, state, or country. |
| `PII.gender` | The gender of all individuals is redacted and replaced with a constant value ‘REDACTED’ |
| `PII.license_number` | By replacing an individual's license number with a random string of the same length, it masks their identity. The column data type is preserved. |
| `PII.phone_number` | Replaces the last five digits of an individual’s phone number with ‘XXXX’ to mask the contact information |