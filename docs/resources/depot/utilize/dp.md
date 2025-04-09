# Building Data Products

A Depot plays a fundamental role in [Data Product](/resources/depot/) development, a Data Product can be created directly from the source Depot or from the lakehouse ([Lakehouse](/resources/lakehouse/)) Depot.

**For example:**

A large enterprise’s procurement team uses the Vendor Data Insights Data Product to streamline compliance audits and vendor management. By leveraging insights on incorporation details, DBE status, and engagement metrics, they can quickly identify high-risk vendors with missing or outdated registration documents. The Data Product enables automated compliance reports, reducing manual effort, and helps procurement teams filter DBE-certified vendors to meet regulatory requirements. Additionally, vendor insights are exposed via APIs, allowing integration with risk assessment dashboards for real-time monitoring. This ensures better decision-making, improved vendor tracking, and seamless regulatory compliance.

The below  manifest file defines the deployment of the `vendor-data-insights` Data Product, categorized under `Vendor Management` with a `Bronze` tier. The Data Product ingests information from various sources within `operationaldb`, including organizations, categories, vendors, certifications, and user data. The processed insights are stored in `operationlake:analytics:vendor_data_insights`. Additionally, it exposes service endpoints through `Lens` and `Talos` for querying vendor insights and API access.

```yaml
name: vendor-data-insights
version: v1beta
entity: product
type: data

# High-level description and purpose
purpose: To provide detailed insights into vendor data, including incorporation details, DBE status, and contact information. This enables reporting, tracking, and analysis of vendor engagement.

# Product categorization tags
tags:   
    - DPDomain.VendorManagement
    - DPTier.Bronze
    - DPUsecase.Vendor Insights

description: Provides vendor details, including state of incorporation, DBE status, and contact attributes like email, phone, and organization information. This data product supports reporting, tracking, and vendor management workflows.

# External references and documentation
refs:
    - title: 'Vendor Data Management Info'
    href: https://proud-cobra.dataos.app/metis/assets/table/lakehouse.lakehouse.promo_effectiveness.vendor_subscription_insights

# Main product configuration
v1beta:
    data:
    # Metadata and tracking information
    meta:
        sourceCodeUrl: https://bitbucket.org/tmdc/vendor-data-insights/src/main/
        title: Vendor Subscription Insights
        trackerUrl: https://rubikai.atlassian.net/browse/DPRB-245?atlOrigin=eyJpIjoiOWMyMDg1ZGE4ZjQ2NDUwNTkzYjYyYTMxM2IwMDY5YWQiLCJwIjoiaiJ9

    # Team members and roles
    collaborators:
        - name: iamgroot
        description: data product owner
        - name: thisisthor
        description: data product developer
        - name: itsloki
        description: consumer of vendor insights

    # Resource bundle configuration
    resource:
        description: 'Resources associated with Vendor Data Insights Data Product'
        purpose: 'Vendor Data Management'
        refType: dataos  
        ref:  bundle:v1beta:vendor-data-bundle

    # Input data sources
    inputs:
        # Vendor database sources
    #  - refType: dataos
    #    ref: dataset:lakehouse:promo_effectiveness:vendor_subscription_insights

        - refType: dataos
        ref: dataset:operationaldb:public:organization

        - refType: depot
        ref: dataos://operationaldb:public/categories

        - refType: depot
        ref: dataos://operationaldb:public/vendor

        - refType: depot
        ref: dataos://operationaldb:public/certification

        - refType: depot
        ref: dataos://operationaldb:public/pending_user

        - refType: depot
        ref: dataos://operationaldb:public/user

        - refType: depot
        ref: dataos://operationaldb:public/vendor_categories

        - refType: depot
        ref: dataos://operationaldb:public/vendor_lists

        - refType: depot
        ref: dataos://operationaldb:public/government_subscriptions

        - refType: depot
        ref: dataos://operationaldb:public/vendor_list_users

    # Output destinations
    outputs:
        - refType: dataos
        ref: dataset:operationlake:analytics:vendor_data_insights

    # Service endpoints
    ports:
        lens:
        ref: lens:v1alpha:vendor-insights360:public
        refType: dataos

        talos:
        - ref: service:v1:vendor-dataapi:public
        refType: dataos


```
