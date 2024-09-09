# Error Handling

Talos SQL Templates, like most programming languages, support error handling. To define an exception in your SQL templates, use the `{% error "ERROR_CODE" %}` syntax. When the template encounters an error during execution, Talos halts further execution and sends an error code to the client, rather than returning query results.

Consider the following example, where a check is performed before executing the main query:

```sql
{% req store %}
SELECT COUNT(*) AS count FROM sales.store AS s WHERE  s.businessentityid = {{ context.params.id }}
{% endreq %}

{% if store.value()[0].count == 0 %}
  {% error "STORE_NOT_FOUND" %}
{% endif %}

SELECT
    s.businessentityid as store_id,
    s.name as store_name
FROM
    sales.store s
WHERE 
    s.businessentityid = {{context.params.id}}
```

In this case, if clients send API requests with an invalid name, they will receive a `400` error along with the error code `STORE_NOT_FOUND`, instead of an empty array. This approach allows you to gracefully handle errors and provide meaningful feedback to the client.