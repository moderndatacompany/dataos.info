# Implementing Filter Data Policy

### Understanding the Filter Policy structure

In a filter policy, the following elements are defined:

- **Selector:** Specifies the user(s) to whom this policy applies. Here, the user with the tag `users:id:iamgroot` is selected.
- **Dataset ID:** Indicates the dataset to which the filter is applied, in this case, `icebase.retail.city`.
- **Filters:** Defines the conditions to filter data rows. Here, the policy filters out rows where the `city_name` column value is not equal to `Verbena`.

## Example

Suppose a user, part of a marketing team, needs access to city-specific data from a shared dataset on Workbench. However, users should only view the data relevant to their assigned city, ensuring that the marketing strategies remain localized. In such scanerio, we will create a policy that automatically filters the data based on the user's city, making it efficient for controlling data views across multiple users.


**Before filtering:**

<div style="text-align: center;">
  <img src="/resources/policy/how_to_guide/filterbefore.png" alt="Sample inaccessible dataset" style="border:1px solid black; width: 80%; height: auto;">
  <figcaption>Access to all cities</ficaption>
</div>


### **Case 1**

If the user is assigned to a city other than Verbena, a filter policy can be implemented to ensure they do not see any data rows where the city is Verbena.

The goal is to filter out all data rows where the city equals "Verbena." This filter data policy ensures that users can only access rows where the city is not "Verbena," maintaining the necessary data restrictions.

To implement the filter policy that restricts access based on city data, use the following YAML structure:


???tip "Filter Policy for city not equals to Verbena"

    ```yaml
    --8<-- "/examples/resources/policy/sample_filter_data_policy01.yml"
    ```

**After applying filter on city not equals to Verbena**

<div style="text-align: center;">
  <img src="/resources/policy/how_to_guide/afterfilter01.png" alt="Sample inaccessible dataset" style="border:1px solid black; width: 80%; height: auto;">
  <figcaption>Access to all cities except Verbena</ficaption>
</div>

In this scenario, the policy applies a filter on the city_name column, restricting access to rows where city_name is Verbena. If the operator assigns this filter to the user tagged as `users:id:iamgroot`, the user will not be able to view any data rows where the city is Verbena.


### **Case 2**

Conversely, another user `ironman` is specifically responsible for Verbena, a filter can be set to allow access only to data where the city is Verbena, ensuring they have the necessary information to develop targeted marketing strategies.


???tip "Filter Policy for city not equals to Verbena"

    ```yaml
    --8<-- "/examples/resources/policy/sample_filter_data_policy02.yml"
    ```

**After applying filter on city equals to Verbena**

<div style="text-align: center;">
  <img src="/resources/policy/how_to_guide/afterfilter01.png" alt="Sample inaccessible dataset" style="border:1px solid black; width: 80%; height: auto;">
  <figcaption>Access to all cities except Verbena</ficaption>
</div>

In this scenario, the policy applies a filter on the city_name column, restricting access to all citites except when city_name is Verbena. If the operator assigns this filter to the user tagged as `users:id:ironman`, the user will not be able to view any data rows of city other than Verbena.


