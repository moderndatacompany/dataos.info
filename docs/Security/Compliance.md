# Compliance

DataOS incorporates secure data processing practices and privacy standards to protect your data and applications. It ensures regulatory compliance such as GDPR, CCPA, and PCI DSS to keep individuals’ personal data safe and private.

DataOS’s Tag-based governance enables flexible and granular level access policy creation that adapts to changing or new compliance regulations. You can define clear authorized access and data usage policies and meet regulatory compliance requirements. For example, if data contains a column for a name, social security number, credit card number, or phone number, you can tag this data as personal identification information(PII). DataOS’s data policies allow you to safely anonymize, mask, hash, redact and share this sensitive PII data with regulatory data privacy compliance. 

To learn more about DataOS policies, refer to
[Policy](../About%20DataOS/Primitives%20Resources/Policy.md). 

DataOS implements an additional metadata layer for identifying personal information and then masking and hashing the corresponding data. 

Fingerprinting analyzes the data to know that a column of data has a signature or a fingerprint. By examining the data values in a column, we can identify what type of data is there and determine what business terms or labels can be attached to this data.

Examining and categorizing the data values is important as it allows you to automate identifying sensitive data that needs to be secured. 