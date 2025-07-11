# Knowing About the Quality of Data Products

!!! info "Overview"
    Let’s dive into how DataOS ensures your Product Affinity Data Product meets the mark for accuracy, freshness, and trustworthiness—so you can confidently use it for analysis.


## Scenario

You’re preparing to analyze customer and sales data to uncover product affinities. But before diving into insights, how do you know the data is actually trustworthy?
Answer: You validate it with quality checks!

## Quick concepts

### **Overview of data quality checks**

Data quality checks verify that data meet predefined standards of accuracy, completeness, uniqueness, and validity. These checks are essential for:

- Identifying and resolving data inconsistencies.

- Ensuring data readiness for reliable analysis.

- Maintaining compliance with defined Service Level Objectives (SLOs).

### **Common SLOs for data quality**

| **SLO**              | **What It Means**                      | **Example**                            |
| ---------------- | ---------------------------------- | ---------------------------------- |
| **Accuracy**     | Data reflects real-world events    | 99% of country names must be valid |
| **Completeness** | All required fields are filled     | Customer ID cannot be missing      |
| **Freshness**    | Data is updated on time            | No data older than 24 hours        |
| **Schema**       | Structure follows defined format   | Birth year must be an integer      |
| **Uniqueness**   | No duplicate records               | Max 0.5% duplicates allowed        |
| **Validity**     | Values meet expected rules/formats | Phone numbers follow valid format  |


## Steps to access Data Product quality

Follow the below steps to understand the quality of the Data Product on the Data Product Hub.

### **Access the quality tab on the Data Product details page**
    
Navigate to the Data Product details page and click on the 'Quality' tab. The Accuracy section displays quality checks applied to the dataset. 
Example: country column has an average length over 6 characters = ✅ 100% accuracy
    
![qua_accuracy.png](/learn_new/dp_consumer_learn_track/dp_quality/qua_accuracy.png)
    
### **Understand the completeness of the data**
    
Switch to the Completeness tab → No missing customer IDs = 100% score
    
![qua_completeness.png](/learn_new/dp_consumer_learn_track/dp_quality/qua_completeness.png)
    
### **Know about the freshness of the data**
    
In the 'Freshness' tab, you will see a 100% freshness rating, Data updated within 2 days = ✅ 100% freshness
    
![qua_freshness.png](/learn_new/dp_consumer_learn_track/dp_quality/qua_freshness.png)
    
### **Understand the schema of the data**
    
On the 'Schema' tab, you may find a trend line at zero, indicating that the data has not passed certain quality checks. This could mean that the data types of columns like 'birth_year' and 'recency' do not align with the established quality conditions.
    
![qua_schema.png](/learn_new/dp_consumer_learn_track/dp_quality/qua_schema.png)
    
### **Assess uniqueness of the data**
    
In the 'Uniqueness' tab, a trend line at 100% indicates that all customer IDs are unique = 100% data integrity.
    
![qua_unique.png](/learn_new/dp_consumer_learn_track/dp_quality/qua_unique.png)
    
### **Check validity**
    
The 'Validity' tab shows a 0% trend line, indicating that some quality checks have failed. For instance, there may be invalid customer IDs in the dataset.
    
![qua_validity.png](/learn_new/dp_consumer_learn_track/dp_quality/qua_validity.png)

## Best practices

1. Regularly review tabs like Accuracy, Completeness, and Freshness on Data Product Hub.
2. Ensure the structure of datasets aligns with predefined schema rules.
3. Run periodic checks for duplicate records, especially in critical fields like customer IDs.
4. Schedule workflows to update data regularly, preventing outdated information from affecting analysis.
5. Investigate and resolve issues flagged in tabs like Validity or Schema as soon as possible.

## Quick knowledge check

**1. What does a 0% validity score indicate?**<br>
A. All data is valid<br>
B. Schema is perfect<br>
C. Several fields fail format checks <br>
D. There are no customer IDs<br>

**2. Which tab would show duplicate issues?**<br>
A. Accuracy<br>
B. Schema<br>
C. Uniqueness <br>
D. Freshness<br>

## Next step

Connect your Data Products with BI tools:

👉 [Integrating Data Products with BI Tools and Applications](/learn_new/dp_consumer_learn_track/integrate_bi_tools/)