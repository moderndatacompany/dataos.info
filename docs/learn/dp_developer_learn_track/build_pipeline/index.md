# Building and maintaining data pipelines

In this topic, you’ll learn how to build and maintain data pipelines to deliver high-quality, reliable data for your data products. Your goal is to ensure seamless data flow through various processes, focusing on accuracy and consistency.

This topic is divided into two key sections:

- **Building data pipelines**: Learn the fundamentals and explore the various resources DataOS offers for constructing robust data pipelines.

- **Pipeline maintainability**: Focus on keeping your pipelines running smoothly through scheduling, monitoring, and alerting to maintain reliability and efficiency.

## Scenario

You are a Data Engineer tasked with transforming raw data into a clean, reliable dataset that powers your company’s data products. After connecting to your data sources, you face the challenge of building pipelines that can handle data efficiently while ensuring accuracy at every step. By mastering this module, you will gain the skills needed to construct and maintain data pipelines that provide trustworthy data, enabling better decision-making across the organization.

## Permissions and access

Before diving into building data pipelines, you need to ensure:

| **Access Permission (if granted using use-cases)** | **Access Permissions (if granted using tags)** |
| --- | --- |
| Read Workspace | `roles:id:data-dev` |
| Manage All Depot | `roles:id:system-dev` |
| Read All Dataset | `roles:id:user` |
| Read all secrets from Heimdall |  |

Some steps in this module require permissions typically granted to DataOS Operators. Max confirms he has access to either of the following:

Verify the assigned tags using the following command:

```bash
dataos-ctl user get
```

You can navigate to the **Bifrost** application to check if any permissions are missing, if they are missing, contacts DataOS Operator for assistance.


## Topic 1: Building data pipelines

Begin by learning the basics of creating data pipelines in DataOS. This involves understanding the fundamental Resources required to construct a pipeline.

Follow the step-by-step instructions provided in the [Creating Your First Data Pipeline guide](/learn/dp_developer_learn_track/build_pipeline/first_pipeline/).

## Topic 2: Pipeline maintainability

Now you understand that building a pipeline is only the beginning. Maintaining its performance and reliability over time is equally important. This section focuses on strategies for keeping pipelines efficient and up-to-date.

### **1. Scheduling Workflows**

<aside class="callout">
🗣 Scheduling can only be applied on the Workflow Resource, and not on the **Worker** and **Service Resource** as they don’t have a defined end.

</aside>

You can ensure data is refreshed at regular intervals by scheduling workflows. This keeps data current with source systems and relevant for decision-making. The **DataOS Workflow Resource** support scheduling capabilities that can be configured directly in your pipeline to meet your specific needs. For a detailed guide on setting up and managing pipeline schedules, refer to the link below.

[Topic: Scheduling pipelines](/learn/dp_developer_learn_track/build_pipeline/scheduling_workflows/)


### **2. Data expectations**

To maintain data quality, you can configure data expectations or "data quality checks." These checks validate data against predefined criteria, such as:

- Data type constraints
- Value ranges
- Uniqueness and many more.

To learn more refer to the link below:

[Topic: Data expectation](/learn/dp_developer_learn_track/build_pipeline/dq_check/)


### **3. Pipeline observability**

You can ensure pipeline performance is monitored in real-time using DataOS observability tools. DataOS Resources such as **Monitor** and **Pager Resource** help detect issues early and optimize workflows.

[Topic: Pipeline observability](/learn/dp_developer_learn_track/build_pipeline/pipeline_observability/)


By completing the above topics, you would gain the skills to:

- Build robust data pipelines using DataOS resources.
- Maintain pipeline reliability and performance through scheduling, data quality checks, and observability.


