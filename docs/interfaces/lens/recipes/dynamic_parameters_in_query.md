# Dynamic Parameters in Query

At times you might want to vary the results of your query based on the inputs. Let’s suppose you want to view the running total of items sold for a specific category or monthly active users for a particular month. But you want to define the specific category or month during runtime. You can use ‘params’. 

Whenever you want to use dynamic parameters, i.e. passing input during query time, ‘params’ should be used. Defining the parameters in the fields, dimension or measure, where you want to pass them will be the first step.

Consider this example, where we want to find the monthly active user, and let the month be defined during the query time, for which we need the count of users.  We have defined a measure month active users, and to define param to get month input during the query time, we use the following format {{key:value}}.

> 🗣 Note: Do not use ‘key’ while defining the param, it’s a reserved keyword

```yaml
measures:
	- name: monthly_active_user
    type: count
    sql_snippet: case when month(${visitedcampaign.ts_}) = {{month:2}}  then entity_id else null end
```

And while querying you can input the params as follows:

```sql
LENS (
    SELECT      
     visitedcampaign.monthly_active_users
    FROM
test_extend  
# give params input as follows
PARAMS (month=3)
)
```