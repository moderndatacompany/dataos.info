# Data Product Foundations · Course I 

In this course, you'll learn how to build a **source-aligned data product** from the ground up. By following each step and completing the checklists, you’ll learn how to connect, ingest, and shape source data into a product-ready asset on DataOS.

---

## 🌟 What You’ll Learn

By the end of this course, you’ll be able to:

- **Create Source-Aligned Data Products**  
  Understand the concepts and build a working data product using DataOS.

- **Connect, Explore, and Ingest Data**  
  Use depots to connect with source systems, explore external data using Scanner and Workbench, and build Flare workflows for ingestion and transformation.

- **Define Data Quality and Set Up Monitoring**  
  Define SLOs, run Soda quality checks, and configure monitors and pagers for reliable, observable data workflows.

- **Deploy and Register Data Products**  
  Package your work into a bundle, create the data product spec, deploy it, and make it searchable in the Data Product Hub.

---

## Scenario: Your Mission

You’re part of a retail company’s data team. You’ve been asked to build a **Retail Data Product** that makes customer, product, and sales data clean, trusted, and usable for dashboards, analytics, and future data products. Right now, this raw data is scattered across databases and blob storage—messy, inconsistent, and full of nulls and duplicates.

**Your goal?** Build a **source-aligned data product** that keeps the raw structure but makes the data usable. You’ll apply quality checks, transform formats, enforce governance, and organize it around real business entities and make them available for the downstream use.

---

## 📚 Learning Modules

### **Module 1: Understand Source-Aligned Data Products**

<div class="grid cards" markdown>

- [What Are Source-Aligned Data Products?](/learn_new/dp_foundations1_learn_track/source_aligned_dp/)

</div>

---

### **Module 2: Connect to Raw Data Sources**

<div class="grid cards" markdown>

- [Establishing Data Connections](/learn_new/dp_foundations1_learn_track/data_source_connectivity/)

</div>

---

### **Module 3: Explore Metadata and Raw Data**

<div class="grid cards" markdown>

- [#1 Create a Scanner Workflow](/learn_new/dp_foundations1_learn_track/create_scanner/) 

- [#2 View Scanned Metadata in Metis]()  

- [#3 Explore External Data via Workbench]()  

</div>

---

### **Module 4: Ingest and Transform Data**

<div class="grid cards" markdown>

- [#1 Build Ingestion Pipelines](/learn_new/dp_foundations1_learn_track/build_pipeline/)

- [#2 Verify Ingested Data]()  
</div>

---

### **Module 5: Add Quality Checks**

<div class="grid cards" markdown>

- [#1 Define SLOs]()  

- [#2 Implement Quality Checks](/learn_new/dp_foundations1_learn_track/quality_check/)

</div>

---

### **Module 6: Set Up Monitoring & Alerts**

<div class="grid cards" markdown>

- [#1 Workflow Failure Monitoring](/learn_new/dp_foundations1_learn_track/pipeline_observability/)

- [#2 Quality Check Monitoring](/learn_new/dp_foundations1_learn_track/quality_check_observability/)  

</div>

---

### **Module 7: Deploy Your First Source-aligned Data Product**

<div class="grid cards" markdown>

- [#1 Package Resources into a Bundle](/learn_new/dp_foundations1_learn_track/create_bundle/)  

- [#2 Create Data Product Spec](/learn_new/dp_foundations1_learn_track/create_dp_spec/)  

- [#3 Deploy Using CLI](/learn_new/dp_foundations1_learn_track/deploy_dp_cli/)  

- [#4 Register in Data Product Hub](/learn_new/dp_foundations1_learn_track/deploy_dp_cli/)  

</div>

---

## How to Use These Modules

Each module in this track is designed for self-paced, hands-on learning.

To follow along:

1. Copy the YAML snippets provided in each step.

2. Customize them for your use case (e.g., names, paths, credentials).

3. Login to your DataOS training instance via the CLI.

4. Use the dataos-ctl apply command to deploy and test your changes.

## Checklist for Success

Make sure you complete the following:

- ✅ CLI installed and initialized  
- ✅ Depot manifests created using Instance Secrets  
- ✅ Data explored via Workbench and metadata viewed in Metis  
- ✅ Ingestion pipelines built and verified  
- ✅ SLOs defined and implemented using SodaCL  
- ✅ Quality monitored in Metis with SLO trends and alerts  
- ✅ Data Product deployed and visible to intended users  

---

You’re all set to create your first source-aligned data product. Let’s get started!
