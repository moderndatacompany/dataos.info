# Advanced Analytical Use Cases in Lens

This document outlines advanced analytical patterns in **Lens**, accompanied by manifest configurations and explanatory notes. Each example leverages rolling window functions and windowed aggregations to support complex business intelligence scenarios.

!!! info 

        Each configuration defines a *measure*. Successful execution requires selecting appropriate *dimensions* within the Lens UI. Failure to do so may result in “group by” errors.

---

## Use Case 1: Sequential Campaign Indexing

**Objective**: Generate sequential numbering for campaigns within each traffic source.

```yaml
- name: rolling_window_testing1
  sql: |
    row_number() OVER (
      PARTITION BY {TABLE.source}
      ORDER BY {TABLE.total_campaigns}
    )
  type: number
  rolling_window:
    offset: start
  description: "Sequential index of campaigns within each source."

- name: lead_campaigns
  sql: |
    lead({TABLE.total_campaigns}) OVER (
      PARTITION BY {TABLE.source}
      ORDER BY {TABLE.total_campaigns}
    )
  type: number
  rolling_window:
    offset: start
  description: "Next campaign's total_campaigns value per source."
```

**Explanation**:

* `ROW_NUMBER()` provides a unique index per `source`, ordered by `total_campaigns`.
* `LEAD()` returns the next campaign’s value in the defined order.
* `offset: start` ensures full-partition coverage for both metrics.

---

## Use Case 2: Month-over-Month Revenue Calculation

!!! tip "Recommendation"

        For period-over-period metrics such as Month-over-Month (MoM), Week-over-Week (WoW), or Year-over-Year (YoY), the following method is preferred over `LEAD` or `LAG`.

**Objective**: Calculate revenue for the current and previous month, along with their ratio.

```yaml
- name: current_month_revenue
  sql: ext_net
  type: sum
  rolling_window:
    trailing: 1 month
    offset: end
  description: "Sum of external net revenue in the current month."

- name: previous_month_revenue
  sql: ext_net
  type: sum
  rolling_window:
    trailing: 1 month
    offset: start
  description: "Sum of external net revenue in the previous month."

- name: month_over_month_ratio
  sql: "{TABLE.current_month_revenue} / cast({TABLE.previous_month_revenue} AS double)"
  type: number
  description: "Ratio of current-month to previous-month revenue."
```

**Explanation**:

* `trailing: 1 month` defines the window size.
* `offset: end` captures current-month data; `offset: start` targets the preceding month.
* The `month_over_month_ratio` metric calculates directional change between periods.

---

## Use Case 3: Supplier Revenue Ranking

**Objective**: Assign dense revenue-based ranks to suppliers by month.

```yaml
- name: supplier_rank
  sql: |
    DENSE_RANK() OVER (
      PARTITION BY {TABLE.year}, {TABLE.month_name}
      ORDER BY {TABLE.total_revenue} DESC
    )
  type: number
  rolling_window:
    offset: start
  description: "Monthly rank of each supplier by revenue (dense, no gaps)."
```

**Explanation**:

* `DENSE_RANK()` applies consecutive ranks without gaps for ties.
* Partitioning by `year` and `month_name` resets rankings each month.
* `offset: start` defines the complete partition scope.

---

## Use Case 4: Customer Revenue Ranking

**Objective**: Identify top-revenue customers on a monthly basis.

```yaml
- name: customer_revenue_rank
  sql: |
    RANK() OVER (
      PARTITION BY {TABLE.year}, {TABLE.month_name}
      ORDER BY {TABLE.total_revenue} DESC
    )
  type: number
  rolling_window:
    offset: start
  description: "Monthly rank of customers by total revenue."
```

**Explanation**:

* `RANK()` assigns ranks with gaps when ties occur.
* Rankings are recalculated monthly based on `year` and `month_name`.
* `offset: start` includes all entries in the partition window.

---

!!info "Note"

        Partitioning dimensions and window definitions can be modified based on data model requirements and reporting needs.


