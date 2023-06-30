## Building Blocks of Toolbox Job

Here, you need to specify the configuration settings required to perform a data processing job such as driver, executor, inputs, outputs, steps, etc. You can define multiple jobs that will be executed in sequential order.

The below table summarizes the various attributes within the dag structure:

| --- | --- | --- | --- | --- | --- | --- |
| name | Name of the job | name: dataos-toolbox-city-01 | NA | NA | Rules for name: 37 alphanumeric characters and a special character '-' allowed. [a-z0-9]\([-a-z0-9]*[a-z0-9]). The maximum permissible length for the name is 47, as showcased on CLI. Still, it's advised to keep the name length less than 30 characters because Kubernetes appends a Unique ID in the name which is usually 17 characters. Hence reduce the name length to 30, or your workflow will fail. | Mandatory |
| title | Title of the job | title: Toolbox Job | NA | NA | There is no limit on the length of the title. | Optional |
| description | This is the text describing the job. | description: The job sets the metadata version to the latest using Toolbox stack | NA | NA | There is no limit on the length of the description. | Optional |
| spec | Specs of job | spec:
    {} | NA | NA | NA | Mandatory |
| tags | Tags for the job | tags:
   - Toolbox
   - City | NA | NA | The tags are case-sensitive, so Connect and CONNECT will be different tags. There is no limit on the length of the tag.  | Optional |
| stack | The Toolbox stack to run the workflow is defined here.  | stack: toolbox | NA | toolbox | NA | Mandatory |
| toolbox | Stack specific section | toolbox: 
     {} | NA | NA | NA | Mandatory |
| dataset | Dataset addressThe dataset UDL address is defined here.  | dataset: dataos://icebase:sample/city?acl=rw | NA | NA | The dataset UDL should be defined in the form of dataos://[depot]:[collection]/[dataset] | Mandatory |
| action | The Toolbox action section | action: 
    {} | NA | NA | NA | Mandatory |
| name | Name of the Toolbox Action | name: set_version | NA | set_version | The set_verison action sets the metadata version to any specific version you want it to. | Mandatory |
| value | The version of the metadata which you want to set to. | value: latest | NA | latest/v2 or any specific version of the metadata. | You can use the dataos-ctl list-metadata to check the available metadata version for iceberg datasets. | Mandatory |
