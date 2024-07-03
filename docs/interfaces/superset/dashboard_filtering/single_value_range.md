# Single Value Range

We will now introduce the **Single value** configuration option, which is exclusive to the Numerical Range filter. This option is utilized to set up a single value type for minimum, maximum, and exact values.

## **Filter Configuration Options**

The following configuration options are available for these filter types:

|  | Value | Numerical Range | Time Range | Time Column | Time Grain |
| --- | --- | --- | --- | --- | --- |
| Parent-child | ✔ |  |  |  |  |
| Pre-filter available values| ✔ | ✔ |  |  |  |
| Sort-filter value | ✔ |  | ✔ | ✔ | ✔ |
| Single value |  | ✔ |  |  |  |

---

## **Single Value Range**

**Option available for this Filter Type: Numerical Range**

The Single value option is exclusive to numerical ranges, serving to restrict the number or range that can be specified in a numerical range filter. To employ this feature, ensure that you are operating with a Numerical Range filter.

Within the *Filter Configuration* panel, opt for **Single Value**.

Then, select a single value type:

<p align="center">
  <img src="/interfaces/superset/dashboard_filtering/single_value_range/Untitled%20(10).png" alt="Your Image Description" />
</p>

**Minimum**: In the numerical range filter, there exists only one anchor point, which is employed to designate a minimum (i.e., starting point) for a range. For instance, if "26" is chosen, then all values greater than or equal to 26 will be encompassed by the filter. It's worth noting the presence of a blue highlight, indicating the filtered range.

<p align="center">
  <img src="/interfaces/superset/dashboard_filtering/single_value_range/Untitled%20(11).png" alt="Your Image Description" />
</p>

**Exact**: The numerical range filter consists of a single anchor point, employed to specify an exact value. Only chart data corresponding to the selected value will be incorporated.

<p align="center">
  <img src="/interfaces/superset/dashboard_filtering/single_value_range/Untitled%20(12).png" alt="Your Image Description" />
</p>

**Maximum**: In the numerical range filter, there exists only one anchor point, utilized to designate a maximum (i.e., ending point) for a range. For instance, if "63" is selected, then all values less than or equal to 63 will be encompassed by the filter. It's worth noting the presence of a blue highlight, indicating the filtered range.

<p align="center">
  <img src="/interfaces/superset/dashboard_filtering/single_value_range/Untitled%20(13).png" alt="Your Image Description" />
</p>