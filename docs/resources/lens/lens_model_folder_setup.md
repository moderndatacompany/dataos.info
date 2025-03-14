# Lens model folder setup

!!! abstract "Quick Guide"
    To quickly get started with creating a Lens model in DataOS, follow the [quick guide on creating a Lens model](/quick_guides/create_data_model/). This guide provides step-by-step instructions to help you transform your conceptual design into a functional semantic model, ensuring effective data structuring and organization to meet your analytical and business needs.

<!-- ### **Prerequisites**

Before setting up Lens, make sure all required dependencies are installed. Follow the [Prerequisites for Lens](/resources/lens/installing_prerequisites/) guide for detailed instructions and resources to ensure a seamless installation and configuration process. -->

### **Lens project folder structure**

In the Model folder, the Lens semantic model will be defined, encompassing SQL mappings, logical tables, logical views, and user groups. Each folder contains specific files related to the Lens model or you can download the following template to quickly get started.

[lens template](/resources/lens/lens_model_folder_setup/lens-project-template.zip)

- Open the Model folder in your preferred editor. It is recommended to organize each Table or View into a separate file within the `model/tables` and `model/views` folders, respectively. The Model folder should follow this structure:

``` bash
model
├── sqls
│   └── sample.sql  # SQL script for the dimensions of the tables
├── tables
│   └── sample_table.yml  # Logical table definition, including joins, dimensions, measures, and segments.
├── views
│   └── sample_view.yml  # View referencing dimensions, measures, and segments from tables.
└── user_groups.yml  # User groups for easier policy enforcement and access control.
```

- **Create `sqls` folder**
    - This directory will contain SQL scripts corresponding to the dimensions of tables.  A dedicated SQL file needs to be maintained for each table. The SQL dialect used will be source-specific.

- **Create `tables` folder**
    - This directory will store logical tables, with each Table defined in a separate YAML file. It defines all the dimensions, measures, segments of the Table.
    
- **Create `views` folder**
    - This directory will store all logical views. Each view should be defined in a separate YAML file, like `sample_view.yml`, which references dimensions, measures, and segments from the tables.

-  **Add `user_groups.yml` manifest file**
    - This YAML manifest file is used to manage access levels for the Lens semantic model. It defines user groups that organize users based on their access privileges. In this file, you can create multiple groups and assign different users to each group, allowing you to control access to the model.By default, there is a 'default' user group in the YAML file that includes all users.

## Next steps

<!-- [Optimizing Lens testing in local development](/resources/lens/optimizing_lens_testing_in_local_development/) -->

[Deploying Lens model on DataOS](/resources/lens/lens_deployment/)



