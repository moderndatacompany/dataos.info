

You can visualize the query results by clicking the “`New Visualization`” button above the results table.

#### Edit Visualization

You can modify the settings of an existing visualization from the query editor screen. Clicking the 'Edit Visualization' will open the current settings for that visualization (type, X axis, Y axis, groupings etc.).

##### Data Labels

Various visualizations may need the nubers to be formatted in different manners in atlas. Here is a quick reference to how these formats can be achieved:

**NUMBERS**

Number | Format | Output
--- | --- | ---
10000 | '0,0.0000' | 10,000.0000
10000.23 | '0,0' | 10,000
10000.23 | '+0,0' | +10,000
-10000 | '0,0.0' | -10000.0
10000.1234 | ‘0.000’ | 10000.123
100.1234 | ‘00000’ | 00100
1000.1234 | ‘000000,0’ | 001,000
10 | ‘000.00’ | 010.00
10000.1234 | ‘0[.]00000’ | 10000.12340
-10000 | ‘(0,0.0000)’ |	(10,000.0000)
-0.23 |	‘.00’ |	-.23
-0.23 |	‘(.00)’ | (.23)
0.23 |	‘0.00000’ |	0.23000
0.23 |	‘0.0[0000]’ | 0.23
1230974 | ‘0.0a’ |	1.2m
1460 |	‘0 a’ |	1 k
-104000 | ‘0a’ | -104k
1 | ‘0o’| 1st
100 | ‘0o’ | 100th
_________________________________________________

**CURRENCY**

Number | Format | Output
--- | --- | ---
1000.234 | ’$0,0.00’ | $1,000.23
1000.2 | ‘0,0[.]00 $’ | 1,000.20 $
1001 | ’$ 0,0[.]00’ | $ 1,001
-1000.234 | ‘($0,0)’ | ($1,000)
-1000.234 | ’$0.00’ | -$1000.23
1230974 | ‘($ 0.00 a)’ | $ 1.23 m
_________________________________________________

**DATA SIZE**

Number | Format | Output
--- | --- | ---
100 | ‘0b’ | 100B
1024 | ‘0b’ | 1KB
2048 | ‘0 ib’ | 2 KiB
3072 | ‘0.0 b’ | 3.1 KB
7884486213 | ‘0.00b’ | 7.88GB
3467479682787 | ‘0.000 ib’ | 3.154 TiB
_________________________________________________

**PERCENTAGES**

Number | Format | Output
--- | --- | ---
100 | ‘0%’ | 100%
97.4878234 | ‘0.000%’ | 97.488%
-4.3 | ‘0 %’ | -4 %
65.43 | ‘(0.000 %)’ | 65.430 %
_________________________________________________

**EXPONENTIAL**

Number | Format | Output
--- | --- | ---
1123456789 | ‘0,0e+0’ |	1e+9
12398734.202 | ‘0.00e+0’ |	1.24e+7
0.000123987 | ‘0.000e+0’ |	1.240e-4