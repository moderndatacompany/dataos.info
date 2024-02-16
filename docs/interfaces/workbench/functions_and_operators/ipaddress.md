# IP Address Functions

### **`contains()`**

| Function                   | Description                                               | Return Type |
| -------------------------- | --------------------------------------------------------- | ----------- |
| `contains(network, address)`| Returns true if the address exists in the CIDR network.    | `boolean`   |


```sql
SELECT contains('10.0.0.0/8', IPADDRESS '10.255.255.255'); -- true
SELECT contains('10.0.0.0/8', IPADDRESS '11.255.255.255'); -- false

SELECT contains('2001:0db8:0:0:0:ff00:0042:8329/128', IPADDRESS '2001:0db8:0:0:0:ff00:0042:8329'); -- true
SELECT contains('2001:0db8:0:0:0:ff00:0042:8329/128', IPADDRESS '2001:0db8:0:0:0:ff00:0042:8328'); -- false
```