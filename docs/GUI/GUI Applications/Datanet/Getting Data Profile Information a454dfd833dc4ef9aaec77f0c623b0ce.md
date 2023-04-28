# Getting Data Profile Information

1. Sign in to your DataOS instance with your username and password.

2. On the **DataOS Datanet** page, search for the dataset for which you want to view the profile data. To display the dataset information, click on its name.

![dataprofile-datanet-search1.png](Getting%20Data%20Profile%20Information/dataprofile-datanet-search1.png)

3. On the **Dataset information** page, click on **Profile**.

![dataprofile-dataset1.png](Getting%20Data%20Profile%20Information/dataprofile-dataset1.png)

1. You will get the following profile data and chart:
    - Summary
    - Correlation matrix
    - Tabular profile data

![dataprofile-dataset-profile1.png](Getting%20Data%20Profile%20Information/dataprofile-dataset-profile1.png)

# **Summary**

DataOS enables you to have an overview of the data in the profile report.

The following information is generated as a summary:

1. **Job run details** such as job name, who run the job, date & time

2. **Sample selection filter**- click on the link to see the applied filter (if any) to get the sample data for profiling

3. **Query**- click on the link to see the generated query

4. **Number of rows analyzed**

5. **Number of columns analyzed**

6. **Number of columns with type mismatches**

7. **Number of columns with complete data and names of those columns**

8. **Number of columns with incomplete data and names of those columns**

# **Correlation matrix**

Data profiling generates a correlation matrix, a table showing a correlation between data elements (essentially having numerical values)using color gradients. It helps in quick visual analysis.
You can explore the association between two variables and makes inferences about the strength of the relationship. You can discover uncommon associations using this matrix that can help you going ahead with further exploration of data.

# **Tabular profile data**

DataOS also allows you to have more detailed view and to drill down the data in the profile report. You will get the following information in the tabular form.

- **General**

| Property | Value |
| --- | --- |
| Column | Data type of the column, length of the data in the column//check |
| Unique(% / value) | Uniqueness Percentage/ Unique count |
| Distinct | Number of distinct patterns observed |
| Completeness | Number and percentage of records with a null value |
- **Statistics**

| Statistical Measures | Description |
| --- | --- |
| Min | The smallest mathematical value in the data set |
| Max | The largest mathematical value in the data set |
| Mean | Average value of a distribution |
| Mode | The most frequent value |
| Median | Middle value in a sorted set |
| Standard Deviation | How much the members of a group differ from the mean value for the group. This is very useful in finding an outliers histogram. Outliers are the abnormal distance from the group, the occurrence of these numbers are uncommon |
| Skewness | Measure of symmetry, or more precisely, the lack of symmetry. A data set is symmetric if it looks same to the left and right of the center point (mean) |
| Coefficient of variation | The coefficient of variation shows the extent of variability of data in a sample in relation to the mean of the population |
| First quartile | The lower quartile, or first quartile, is denoted as Q1 and is the middle number that falls between the smallest value of the dataset and the median |
| Second quartile | The second quartile (Q2) is the median of a data set; thus 50% of the data lies below this point |

![dataprofile-dataset-profile-tabulardata.png](Getting%20Data%20Profile%20Information/dataprofile-dataset-profile-tabulardata.png)

# **Interpretation of profile data**

The output from any data profiling job needs to be interpreted before it is useful.