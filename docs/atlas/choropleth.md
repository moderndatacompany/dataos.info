
Choropleth Maps display coloured, shaded or patterned geographical areas or regions that conform to a data variable. This provides a way to visualise trends over a geographical area.

Colour variance and progression (dark to light and vice versa) show the data value measure. Typically, this can be a blending from one colour to another, a single hue progression, transparent to opaque, light to dark or an entire colour spectrum.

![Image](./images/atlas-mapchoropleth.png)

## Example Query
```sql
SELECT
  region,
  sum(round(cast(productprice AS double) * cast(orderquantity AS int), 2)) AS revenue
FROM
  icebase.sportsproducts.sports_transactions_data_with_ts a
  LEFT JOIN icebase.sportsproducts.sports_products_data_with_ts b ON b.productkey = a.productkey
  LEFT JOIN icebase.sportsproducts.sports_productsubcategories_data_with_ts c ON c.productsubcategorykey = b.productsubcategorykey
  LEFT JOIN icebase.sportsproducts.sports_productcategories_data_with_ts d ON d.productcategorykey = c.productcategorykey
  LEFT JOIN icebase.sportsproducts.sports_salesterritories_data_with_ts e ON e.salesterritorykey = a.territorykey
WHERE
  year (date_parse (concat(regexp_extract (orderdate, '[^\/]*'), '/', regexp_extract (orderdate, '/([a-zA-Z0-9]+)/', 1), '/', CASE regexp_extract (orderdate, '/.*/(.*)', 1)
        WHEN '16' THEN
          '2016'
        WHEN '17' THEN
          '2017'
        WHEN '15' THEN
          '2015'
        ELSE
          regexp_extract (orderdate, '/.*/(.*)', 1)
        END), '%m/%d/%Y')) = 2017
GROUP BY
  1


```
![Image](./images/atlas-mapchoropleth-wb.png)

The results of the above query have been exported to Atlas and plotted into a Choropleth Map as follows.


![Image](./images/atlas-mapchoropleth-editing1.png)

This is how the Choropleth Map will look like:

![Image](./images/atlas-mapchoropleth-chart.png)
