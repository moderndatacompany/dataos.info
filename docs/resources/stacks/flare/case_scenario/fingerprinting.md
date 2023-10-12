# Fingerprinting in DataOS
Fingerprinting in DataOS analyzes data columns to detect distinctive patterns or signatures. This analysis helps identify the nature of the data and enables the assignment of relevant business labels or tags for discoverability. Moreover, fingerprinting plays a vital role in automating the identification of sensitive data, such as Personally Identifiable Information (PII) or Protected Health Information (PHI). It suggests the appropriate business terms and tags based on the type of data. Once the data is fingerprinted, you can create data policies to effectively manage and protect the sensitive data. By leveraging fingerprinting, you can ensure that sensitive data is adequately protected and compliant with government regulations like GDPR.

The fingerprinting process is systematic and involves several key steps:

**Data Column Classification:** Data columns undergo comprehensive classification, categorizing them into different data types, differentiating between categorical and non-categorical data.

**Attribute Tagging:** Attribute tagging involves a meticulous evaluation of both column names and their corresponding values. This evaluation helps in accurately assigning tags to the data columns.

Once the initial data classification is complete, categorical columns undergo further classification using a keyword match-based scoring algorithm, ensuring accurate and reliable classification. This algorithm assigns a score that reflects the extent to which a particular column belongs to a predefined category. 

DataOS provides both built-in and customizable classifications seamlessly integrated into data protection policies. You can utilize these classifications directly in your data policies to ensure that sensitive data remains secure and inaccessible to unauthorized users. Once data items are tagged as PHI or PII, associated data policies are automatically applied.

<aside class="callout">On the Metis UI, you can access and manage classifications organized into tag groups.</aside>

## Classification of Data

Sensitive data is identified with text patterns using dictionaries and regular expressions.

### **Dictionary** 
Dictionaries consist of related keywords and phrases, such as personally identifiable information, medical terminology, etc. Sensitive data is compared to the dictionary entries and evaluated based on a score. DataOS provides a range of built-in dictionaries tailored to industries like healthcare, banking, finance, and more. You also have the flexibility to create custom dictionaries to align with your organization's specific requirements.

## **Advanced Patterns** 
Advanced patterns involve the use of regular expressions or phrases to detect specific patterns, such as social security numbers or credit card numbers.  DataOS includes built-in advanced patterns designed for the identification of PII and PHI information to comply with government regulations. Additionally, you have the option to create custom advanced patterns to suit your unique data classification needs.

## Classification Categories and Fields

### **Data Types**

- Integer 
- Fraction 
- Datetime 


### **Attributes**
| Category | Attributes|
| --- | --- | 
| Personal Information | • ID, UUID, API Key<br> • Login ID, password<br> • Name - First and Last<br> • Gender<br> • Organization Name<br> • Bank Issued Card Number<br> • IP Address<br> • URL/Domain<br> • Salary<br> • Blood Group |
| Banking Information | • Bank Issued Card No.<br> • Indian Bank IFSC Code<br> • Bank Account number<br> • IBAN Code |
| Location Information | • country name<br>• country code<br>• state code<br>• Street | 
| Educational Information | • College Degree/Education |
| Contact Information | • email<br>• Contact Number | 
|Government-issued IDs | • US EIN Number<br>• US SSN Number<br>• Indian Aadhar Number<br>• Indian UPI Id<br>• Indian PAN Number |
| Driving License Information | • US Driving License<br>• Indian Driving License | 
| Demographic Information | • Religion<br>• Sexuality<br>• Race |