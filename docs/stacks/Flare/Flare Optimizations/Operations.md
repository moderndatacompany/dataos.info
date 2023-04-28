# **Operations**

Operations Center gets all the data from CLI via Kubernetes clusters. It shows information about what is happening at the moment. Operations Center shows live action

**Collated:** It is a service that powers Hera. Collated behind the scenes is powered by POROS. It continuously captures the information related to deployments like jobs, workflows, and services*.* Collated stores all this information within Blob storage. There is a fine difference between Collated and the Operations Center on the UI. Collated shows all the information about events with a delay while the Operations Center shows live actions.

What is the difference between Collated and Operations Center?

**Answer:**

At present, Collated shows you the information after the event while the Operations Center shows the information about what is happening at the moment. This is the fundamental difference as of now between Collated and the Operations Center. Operations Center gets all the data from CLI via Kubernetes clusters.