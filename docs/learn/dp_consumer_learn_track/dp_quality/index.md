# Knowing About the Quality of Data Products

In this topic, you will learn about the quality of the 'Product360' Data Product after exploring it for your use case. The focus is on ensuring the Data Product meets necessary quality standards for reliable analysis.

## Scenario

To effectively analyze customer and sales data for uncovering product affinities, the Data Product must pass various quality checks. This ensures that the insights drawn from it are both valid and actionable.

## Quick concepts

### **Overview of data quality checks**

Data quality checks verify that data meet predefined standards of accuracy, completeness, uniqueness, and validity. These checks are essential for:

- Identifying and resolving data inconsistencies.

- Ensuring data readiness for reliable analysis.

- Maintaining compliance with defined Service Level Objectives (SLOs).

### **Common SLOs for data quality**

- **Accuracy:** The degree to which data correctly represents the real-world entity or event. For example, at least 99% of data points must be correct.
- **Completeness:** The extent to which all required data is available and no essential information is missing. Like, No more than 1% of records can have missing values.
- **Freshness:** The timeliness of the data, ensuring it is up-to-date and reflects the most recent information. You may require that data should be updated within the last 24 hours.
- **Schema:** The structure or organization of the data, defining how data elements are arranged and related. In critical applications, you might want that 100% of records must adhere to the expected schema.
- **Uniqueness:** Ensuring that each record or data point is distinct and not duplicated within the dataset. You may define that a maximum of 0.5% of records can be duplicates.
- **Validity:** The adherence of data to defined formats, rules, and constraints to ensure correctness.

## Steps to access Data Product quality

Follow the below steps to understand the quality of the Data Product on the Data Product Hub.

### **Access the quality tab on the Data Product details page**
    
Navigate to the Data Product details page and click on the 'Quality' tab. The Accuracy section opens by default, displaying quality checks applied to the dataset. For example, it indicates that the average length of the “country” column is over six characters, confirming 100% accuracy.
    
![qua_accuracy.png](/learn/dp_consumer_learn_track/dp_quality/qua_accuracy.png)
    
### **Understand the completeness of the data**
    
Switch to the 'Completeness' tab, which shows a 100% score, indicating there are no missing customer IDs.
    
![qua_completeness.png](/learn/dp_consumer_learn_track/dp_quality/qua_completeness.png)
    
### **Know about the freshness of the data**
    
In the 'Freshness' tab, you will see a 100% freshness rating, meaning no data is older than two days as per the defined quality check conditions.
    
![qua_freshness.png](/learn/dp_consumer_learn_track/dp_quality/qua_freshness.png)
    
### **Understand the schema of the data**
    
On the 'Schema' tab, you may find a trend line at zero, indicating that the data has not passed certain quality checks. This could mean that the data types of columns like “birth_year” and “recency” do not align with the established quality conditions.
    
![qua_schema.png](/learn/dp_consumer_learn_track/dp_quality/qua_schema.png)
    
### **Assess uniqueness of the data**
    
In the 'Uniqueness' tab, a trend line at 100% indicates no duplicate customer IDs, confirming data integrity.
    
![qua_unique.png](/learn/dp_consumer_learn_track/dp_quality/qua_unique.png)
    
### **Check validity**
    
The 'Validity' tab shows a 0% trend line, indicating that some quality checks have failed. For instance, there may be invalid customer IDs in the dataset.
    
![qua_validity.png](/learn/dp_consumer_learn_track/dp_quality/qua_validity.png)

## Best practices

1. Regularly review tabs like Accuracy, Completeness, and Freshness on Data Product Hub.
2. Ensure the structure of datasets aligns with predefined schema rules.
3. Run periodic checks for duplicate records, especially in critical fields like customer IDs.
4. Schedule workflows to update data regularly, preventing outdated information from affecting analysis.
5. Investigate and resolve issues flagged in tabs like Validity or Schema as soon as possible.

## Next step

Connect your Data Products with BI tools:

[Integrating Data Products with BI Tools and Applications](/learn/dp_consumer_learn_track/integrate_bi_tools/)