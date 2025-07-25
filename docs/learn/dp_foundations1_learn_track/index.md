# Data Product Foundations Track: Course I 

!!! info "Overview"
    In this course, you'll learn how to build a **source-aligned Data Product** from the ground up. By following each step and completing the checklists, you’ll learn how to connect, ingest, and shape source data into a product-ready asset on DataOS.

---

## 🌟 What you’ll learn

By the end of this course, you’ll be able to:

- **Create source-aligned Data Products**  
  Understand the concepts and build a working Data Product using DataOS.

- **Connect, explore, and ingest Data**  
  Use depots to connect with source systems, explore external data using Scanner and Workbench, and build Flare workflows for ingestion and transformation.

- **Define data quality and set up monitoring**  
  Define SLOs, run Soda quality checks, and configure monitors and pagers for reliable, observable data workflows.

- **Deploy and register Data Products**  
  Package your work into a bundle, create the Data Product spec, deploy it, and make it searchable in the Data Product Hub.

---

## 📘 Scenario

You’re part of a retail company’s data team. You’ve been asked to build a **Retail Data Product** that makes customer, product, and sales data clean, trusted, and usable for dashboards, analytics, and future Data Products. Right now, this raw data is scattered across databases and blob storage—messy, inconsistent, and full of nulls and duplicates.

**Your goal?** Build a **source-aligned Data Product** that keeps the raw structure but makes the data usable. You’ll apply quality checks, transform formats, enforce governance, and organize it around real business entities and make them available for the downstream use.

---

## 📚 Learning modules

### **Module 1: Understand Source-Aligned Data Products**

<div class="grid cards" markdown>

- [What Are Source-Aligned Data Products?](/learn/dp_foundations1_learn_track/source_aligned_dp/)

</div>

---

### **Module 2: Connect to Raw Data Sources**

<div class="grid cards" markdown>

- [Establishing Data Connections](/learn/dp_foundations1_learn_track/data_source_connectivity/)

</div>

---

### **Module 3: Explore Metadata and Raw Data**

<div class="grid cards" markdown>

- [Create a Scanner Workflow](/learn/dp_foundations1_learn_track/create_scanner/) 

<!-- - [#2 View Scanned Metadata in Metis]()  

- [#3 Explore External Data via Workbench]()   -->

</div>

---

### **Module 4: Ingest and Transform Data**

<div class="grid cards" markdown>

- [Build Ingestion Pipelines](/learn/dp_foundations1_learn_track/build_pipeline/)

<!-- - [#2 Verify Ingested Data]()   -->
</div>

---

### **Module 5: Add Quality Checks**

<div class="grid cards" markdown>

<!-- - [#1 Define SLOs]()   -->

- [Implement Quality Checks](/learn/dp_foundations1_learn_track/quality_check/)

</div>

---

### **Module 6: Set Up Monitoring & Alerts**

<div class="grid cards" markdown>

- [#1 Workflow Failure Monitoring](/learn/dp_foundations1_learn_track/pipeline_observability/)

- [#2 Quality Check Monitoring](/learn/dp_foundations1_learn_track/quality_check_observability/)  

</div>

---

### **Module 7: Deploy Your First Source-aligned Data Product**

<div class="grid cards" markdown>

- [#1 Package Resources into a Bundle](/learn/dp_foundations1_learn_track/create_bundle/)  

- [#2 Create Data Product Spec](/learn/dp_foundations1_learn_track/create_dp_spec/)  

- [#3 Deploy Using CLI](/learn/dp_foundations1_learn_track/deploy_dp_cli/)  

<!-- - [#4 Register in Data Product Hub](/learn/dp_foundations1_learn_track/deploy_dp_cli/)   -->

</div>

---

## How to use these modules

Each module in this track is designed for self-paced, hands-on learning.

To follow along:

1. Open your preferred code editor and create a new file with a `.yaml` extension.

2. Based on your objective (e.g., creating a data pipeline, configuring access policies), copy the relevant YAML snippets provided in the training materials.

3. Modify the snippets as needed to suit your use case—update names, paths, and credentials as appropriate.

4. Login to your DataOS training instance via the CLI.

5. Use the `dataos-ctl apply` command to deploy and test your changes.

> Each section includes specific instructions and configuration details to guide you through the process.

## Checklist for success

Make sure you complete the following:

- ✅ CLI installed and initialized  
- ✅ Depot manifests created using Instance Secrets  
- ✅ Data explored via Workbench and metadata viewed in Metis  
- ✅ Ingestion pipelines built and verified  
- ✅ SLOs defined and implemented using SodaCL  
- ✅ Quality monitored in Metis with SLO trends and alerts  
- ✅ Data Product deployed and visible to intended users  

---

You’re all set to create your first source-aligned Data Product. Let’s get started!
