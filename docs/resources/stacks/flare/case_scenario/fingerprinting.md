# Fingerprinting in DataOS
Fingerprinting in DataOS analyzes data columns to detect distinctive patterns or signatures. 

This analysis serves several purposes:

**Understanding data**: It helps you better comprehend the data's characteristics.

**Enhancing discoverability**: By assigning relevant business labels or tags, it facilitates data discoverability and democratization.

**Automating sensitive data identification**: It automates the recognition of sensitive data, like Personally Identifiable Information (PII) or Protected Health Information (PHI). Once data is fingerprinted, you can create data policies to effectively manage and protect this sensitive information.

**Ensuring regulatory compliance**: It aids in ensuring compliance with government regulations such as GDPR."

## Fingerprinting process
The fingerprinting process is systematic and involves several key steps:

**Data column classification:** Data columns undergo comprehensive classification, categorizing them into different data types, differentiating between categorical and non-categorical data.

**Attribute tagging:** Attribute tagging involves a meticulous evaluation of both column names and their corresponding values. This evaluation helps in accurately assigning tags to the data columns.

Once the initial data classification is complete, categorical columns undergo further classification using a keyword match-based scoring algorithm, ensuring accurate and reliable classification. This algorithm assigns a score that reflects the extent to which a particular column belongs to a predefined category. 

DataOS provides both built-in and customizable classifications seamlessly integrated into data protection policies. You can utilize these classifications directly in your data policies to ensure that sensitive data remains secure and inaccessible to unauthorized users. Once data items are tagged as PHI or PII, associated data policies are automatically applied.

<aside class="callout"> On the Metis UI, you can access and manage classifications organized into tag groups.</aside>

## Classification of data
DataOS performs classification and attribute tagging with text patterns using pre-defined categories and regular expressions.

### **Pre-defined categories** 
Categories are defined based on related keywords and phrases, such as personally identifiable information, medical terminology, etc. Sensitive data is compared to the dictionary entries and evaluated based on a score. DataOS provides a range of built-in categorie  tailored to industries like healthcare, banking, finance, and more. It also takes care of country specific  columns such as SSN number for US and PAN and AADHAR for India. You also have the flexibility to create custom dictionaries to align with your organization's specific requirements.

### **Advanced patterns** 
Advanced patterns involve the use of regular expressions or phrases to detect specific patterns, such as social security numbers or credit card numbers.  DataOS includes built-in advanced patterns designed for the identification of PII and PHI information to comply with government regulations. Additionally, you have the option to create custom advanced patterns to suit your unique data classification needs.

## Classification ctegories and fields

DataOS supports the following classifications.

### **Data types**

- Integer 
- Fraction 
- Datetime 

### **Categorical/non categorical columns**
Based on the minimum number of non-null values, unique values and distribution of values, it determines and classifies a column as categorical.

### **Attributes**
Refer to the following table, which is used for classification and attribute tagging during the fingerprinting process in DataOS.

<div style="text-align: center;">

| Category | Attributes|
| --- | --- | 
| Personal Information | • ID, UUID, API Key<br> • Login ID, password<br> • Name - First and Last<br> • Gender<br> • Organization Name<br> • Bank Issued Card Number<br> • IP Address<br> • URL/Domain<br> • Salary<br> • Blood Group |
| Banking Information | • Bank Issued Card No.<br> • Indian Bank IFSC Code<br> • Bank Account number<br> • IBAN Code |
| Location Information | • country name<br>• country code<br>• state code<br>• Street | 
| Educational Information | • College Degree/Education |
| Contact Information | • email<br>• Contact Number | 
|Government-issued IDs | • US EIN Number<br>• US SSN Number<br>• Indian Aadhar Number<br>• Indian UPI Id<br>• Indian PAN Number |
| Driving License Information | • US Driving License<br>• Indian Driving License | 
| Demographic Information | • Religion<br>• Sex/Gender<br>• Race |

</div>
