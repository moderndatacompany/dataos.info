# Lens model folder setup

!!! abstract "Quick Guide"
    To quickly get started with creating a Lens model in DataOS, follow the [quick guide on creating a Lens model](/quick_guides/create_data_model/). This guide provides step-by-step instructions to help you transform your conceptual design into a functional semantic model, ensuring effective data structuring and organization to meet your analytical and business needs.

### **Prerequisites**

Before setting up Lens, make sure all required dependencies are installed. Follow the [Prerequisites for Lens](/resources/lens/installing_prerequisites/) guide for detailed instructions and resources to ensure a seamless installation and configuration process.

### **Lens Project Folder Structure**

In the Model folder, the Lens semantic model will be defined, encompassing SQL mappings, logical tables, logical views, and user groups. Each folder contains specific files related to the Lens model or you can download the following template to quickly get started.

[lens template](/resources/lens/lens_model_folder_setup/lens-project-template.zip)

- Open the Model folder in the preferred editor. It's recommended to place each table or view in a separate file, in model/tables and model/views folders, respectively. for example, the Model folder will have the following hierarchy:

``` bash
model
├── sqls 
│   └── sample.sql
├── tables 
│   └── sample_table.yml //A logical table definition includes joins, dimensions, measures, and segments.
├── views 
│   └── sample_view.yml //View reference dimensions, measures, and segments from tables.
└── user_groups.yml //User groups organize users for easier policy application.
```

- **Create `sqls` Folder**
    - This directory will contain SQL scripts corresponding to the dimensions of tables.  A dedicated SQL file needs to be maintained for each table. The SQL dialect used will be source-specific.

- **Create `tables` Folder**
    - This directory will store logical tables, with each table defined in a separate YAML file.
    
- **Create `views` Folder**
    - This directory will store all logical views.

-  **Add user_groups.yml Folder**
    - User groups organize users for easier policy applications to control access.
    - Presently, we have a 'default' user group defined in the YAML that includes all users.

## Next Steps

[Optimizing Lens testing in local development](/resources/lens/optimizing_lens_testing_in_local_development/)

[Deploying Lens model on DataOS](/resources/lens/lens_deployment/)



