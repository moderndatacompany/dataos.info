
## RFM: Recency, Frequency, Monetary

RFM is a method where you identify customers based on the recency of their last purchase, the total number of purchases they have made (frequency) and the amount they have spent (monetary). The marketers can target specific customer groups with communications that are much pertinent to their specific shared behaviour


- **Recency:** The time elapsed since a customer’s last activity or transaction with the brand, forms the recency factor of RFM. An activity, though a transaction for most cases, can be a site/ store visit, adding products to cart etc. The guiding principle here is that the more recently a customer has interacted or transacted with a brand, the more likely that customer will be responsive to communications from the brand.

- **Frequency:** The number of times a customer transacted or interacted with the brand during a time window. The guiding principle here is that more frequent the activities by a customer the more engaged anf loyal they are; and vice versa.

- **Monetary:** Also referred to as “monetary value,” this factor reflects how much a customer has spent with the brand during a particular period of time. Big spenders should usually be treated differently than customers who spend little. Combining this with frequency, an estimate on average spending can be made


### Calculating Recency, Frequency and Monetary

Consider the following data exploration query:

``` sql
select                                             /* main query*/
  trans_frequency,
  count(accountname) as customer_count,
  round(avg(ltv)) as avg_ltv,
  round(avg(avg_rev)) as avg_rev
from
  (
    select                                         /* sub-query */
      accountname,
      count(distinct transaction_id) as trans_frequency,
      round(sum(product_revenue)) as ltv,
      round(avg(transaction_revenue)) as avg_rev
    from
      raw01.orders_05
    group by 1 
    order by 2 desc
  )
group by 1 
order by 1
```

The query has a nested sub-query inside, which creates an output table having the transaction frequency (trans_frequency), lifetime value (ltv) and average revenue per transaction (avg_rev) grouped by the name (accountname). Sample output is as follows:

 accountname | trans_frequency | ltv | avg_rev |
 --- | --- | --- | --- 
 Acc1 | 488 | 667890 | 1984
 Acc2 | 389 | 547900 | 2051
 Acc3 | 356 | 172072 | 662

The main query here tries to understand the distribution of customers in frequency bands.

 trans_frequency | customer_count | avg_ltv | avg_rev |
 --- | --- | --- | --- 
 205 | 1 | 185767 | 1746
 208 | 1 | 181988 | 1369
 203 | 1 | 178912 | 992


The following query delves into calculating the actual frequency (interactions) and on the basis of that, the recency.

``` sql
select
  days_since_last_purchase,
  count(accountname) as customer_count
from
  (
    select
      accountname,
      count(distinct date) as frequency,
      round(sum(product_revenue)) as ltv,
      date_diff('day', max(date(date_parse(date,'%Y%m%d'))), current_date) as days_since_last_purchase
    from
      raw01.orders_05
    group by 1 
    order by 2 desc
  )
group by
  1
order by
  1
```

The sub-query lists 'distinct' date as frequency, because every row (interaction) has a unique timestamp and hence its count is the effective frequency we need for our analysis. The date_diff here tries to mark the recency in days, of a customer's interactions; by calculating the day difference between interaction date and today.
Sample output is as follows:

 accountname | frequency | ltv | days_since_last_purchase
 --- | --- | --- | --- 
 AccA | 33 | 81897 | 75
 AccB | 33 | 133918 | 63
 AccC | 32 | 118922 | 66


The main query tries to group the customers into recency bands. The sample output is as follows:

days_since_last_purchase | customer_count
--- | ---
63 | 2951
64 | 3188
65 | 3372

For calculating the monetary value, we work on customer's ltv. Bucketizing it and dividing the customers in groups based on the buckets.

``` sql
select 
  (case 
    when ltv <= 250 then '$250'
    when ltv > 250 AND ltv <= 550 then '$250-$550'
    when ltv > 550 and ltv <= 1200 THEn '$550-$1200'
    WHEN ltv > 1200 AND ltv <= 3000 then '$1200 - $3000'
    when ltv > 3000 then '>$3000'
  end) as ltv_bucket, 
  count(accountname) as customer_count from 
(select
  account_id,
  accountname,
  count(distinct date) as frequency,
  round(sum(product_revenue)) as ltv,
  date_diff('day', max(date(date_parse(date,'%Y%m%d'))), current_date) as days_since_last_purchase
from
  raw01.orders_05
group by
  1,2) group by 1
```

The sample output is as follows:

ltv_bucket | customer_count
--- | ---
$250 | 7207
$250 - $550 | 5443
$550 - $1200 | 5999
$1200 - $3000 | 6768
| >$3000 | 11550

These queries try to get the recency, frequency and monetary value separately and accordingly group the customers. However, unless customers have a score attached to their RFM values, the exercise is not fruitful. 

Keeping that in mind, the following query tries to attach scores to each customer based on their RFM values.

``` sql
create view raw01.orders_rfm_analysis as
(select 
  account_id,
  accountname,
  frequency,
  recency,
  ltv,
  case 
    when frequency = 1 then 1
    when frequency = 2 then 2
    when frequency = 3 then 3
    when frequency = 4 then 4
    when frequency > 4 then 5
  end as f_score,
  case 
    when recency = 1 then 5
    when recency = 2 then 4
    when recency > 2 and recency <= 7 then 3
    when recency > 7 and recency <= 14 then 2
    when recency > 14 then 1
  end as r_score,
  case 
    when ltv <= 250 then 1
    when ltv > 250 AND ltv <= 550 then 2
    when ltv > 550 and ltv <= 1200 THEn 3
    WHEN ltv > 1200 AND ltv <= 3000 then 4
    when ltv > 3000 then 5
  end as m_score
FROM
(select
  account_id,
  accountname,
  count(distinct date) as frequency,
  round(sum(product_revenue)) as ltv,
  date_diff('day', max(date(date_parse(date,'%Y%m%d'))), current_date) as recency
from
  raw01.orders_05
group by
  1,2))
  ```

The actual RFM values are mapped to scores. The scores are marked from 1 to 5, 5 being the most preferred value and 1 being the least. This bucketization brings all customers to a level playing field, to further group them and in effect, identify the priority ones.

A sample of rows in the view is as follows:

account_id | accountname | frequency | recency | ltv | f_score | r_score | m_score
--- | --- | --- | --- | --- | --- | --- | ---
8509724 | AcctA | 14 |  3 | 22509 | 5 | 3 | 5
4609619 | AcctB | 3  |  6 | 25972 | 3 | 3 | 5
1002949 | AcctC | 2  | 68 |  1641 | 2 | 1 | 4
1602819 | AcctX | 3  | 81 |  1004 | 3 | 1 | 3

Customers with different combination of scores would mean different 'segments'. These segments are the actual deliverable of the exercise, pointing to the current state of the customer.

The following query tries to define some of the segments based on the scores identified above:

``` sql
create view raw01.segments as
select
  account_id,
  accountname,
  frequency as overall_frequency,
  recency as overall_recency,
  ltv as overall_ltv,
  f_score as overall_f_score,
  r_score as overall_r_score,
  m_score as overall_m_score,
  case when (r_score between 4 and 5) and (f_score between 4 and 5) and (m_score between 4 and 5) then 'Y' else 'N' end as overall_champions,
  case when (r_score between 2 and 5) and (f_score between 3 and 5) and (m_score between 3 and 5) then 'Y' else 'N' end as overall_loyal_customers,
  case when (r_score between 3 and 5) and (f_score between 1 and 3) and (m_score between 1 and 3) then 'Y' else 'N' end as overall_potential_loyalist,
  case when (r_score between 4 and 5) and (f_score between 0 and 1) and (m_score between 0 and 1) then 'Y' else 'N' end as overall_recent_customers,
  case when (r_score between 3 and 4) and (f_score between 0 and 1) and (m_score between 0 and 1) then 'Y' else 'N' end as overall_promising,
  case when (r_score between 2 and 3) and (f_score between 2 and 3) and (m_score between 2 and 3) then 'Y' else 'N' end as overall_customer_needs_attention,
  case when (r_score between 2 and 3) and (f_score between 0 and 2) and (m_score between 0 and 2) then 'Y' else 'N' end as overall_about_to_sleep,
  case when (r_score between 0 and 2) and (f_score between 2 and 5) and (m_score between 2 and 5) then 'Y' else 'N' end as overall_at_risk,
  case when (r_score between 0 and 1) and (f_score between 4 and 5) and (m_score between 4 and 5) then 'Y' else 'N' end as overall_cant_lose_them,
  case when (r_score between 1 and 2) and (f_score between 1 and 2) and (m_score between 1 and 2) then 'Y' else 'N' end as overall_hibernating,
  case when (r_score between 0 and 2) and (f_score between 0 and 2) and (m_score between 0 and 2) then 'Y' else 'N' end as overall_lost
from raw01.orders_rfm_analysis
```
Champions: Top tier (4 to 5) recency, frequency and monetary values. These are the priority target customers, deserving most attention and care.

Loyal Customers: A recency score ranging from 2 to 5, frequency and monetary scores ranging from 3 to 5 point to a group of customers who are frequent and have a decent average transaction value but may not be as recent.

Potential Loyalists: A recency score ranging from 3 to 5, frequency and monetary scores ranging from 1 to 3 point to a group of customers who are less frequent and have low average transaction value but are recent, and with appropriate targetting, can upscale to Loyal customers.

Recent Customers: A recency score ranging from 4 to 5, frequency and monetary scores ranging from 0 to 1 point to a group of customers who have recently shown interest in the product. This may be the right time to target such customers.

Promising Customers: A recency score ranging from 3 to 4, frequency and monetary scores ranging from 0 to 1 point to a group of customers who have fairly recently shown interest in the product. This may be the right time to target such customers.

Customers needing attention: A recency, frequency and monetary scores ranging from 2 to 3 point to a group of customers who need immediate attention to upscale to Loyal or champion customers.

Customers about to sleep: A recency score ranging from 2 to 3, frequency and monetary scores ranging from 0 to 2 point to a group of customers who close to being dormant/ go into hibernation.

Customers at risk: A recency score ranging from 0 to 2, frequency and monetary scores ranging from 2 to 5 point to a group of customers who might be lost and need attention.

Customers that shouldn't be lost ('Can't lose them'): A recency score ranging from 0 to 2, frequency and monetary scores ranging from 2 to 5 point to a group of customers who have a potential to be champions but have not shown any interest recently.

Hibernating customers: A recency, frequency and monetary scores ranging from 1 to 2 point to a group of customers who are dormant or hibernating. Any efforts to target these customers can be deprioritized.

Lost customers: A recency, frequency and monetary scores ranging from 0 to 2 point to a group of customers who are lost and all further efforts to target these customers should be stopped.


