# Monitor the Logs of a Lens

A Lens is a non-runnable Resource in DataOS; however, during the creation of a Lens model, a corresponding Service is automatically generated in the backend with the suffix ‘-api’. This Service handles the Lens’s API interface, and users can monitor its logs to observe the behavior and health of the Lens.

Additionally, when configuring a Lens Resource, users have the option to enable components such as a Worker, router, and metrics, depending on the specific use case. If these are defined in the Lens manifest, the system automatically provisions two additional Services, one for the router with suffix ‘-router’ and one for metrics with suffix ‘-metrics’, along with a Worker with suffix ‘-worker’. The below example shows a Lens ‘data-product-insights’ created three Services with suffix ‘-api’, ‘-metric’, and ‘router’, and a Worker with suffix ‘-worker’ added to the Lens identifier.

<div style="text-align: center;">
  <img src="/products/data_product/observability/observability.png" style="width: 70%; height: auto;">
  <figcaption><i>Observability in DataOS</i></figcaption>
</div>

<div style="text-align: center;">
  <img src="/products/data_product/observability/observability.png" style="width: 70%; height: auto;">
  <figcaption><i>Observability in DataOS</i></figcaption>
</div>

To monitor logs for these components, users should refer to the documentation linked below.

- [Monitor the logs of a Service](https://www.notion.so/Monitor-the-logs-of-a-Service-207c5c1d487680b5a048f6e09e8a70a5?pvs=21)
- [Monitor the logs of a Worker](https://www.notion.so/Monitor-the-logs-of-a-Worker-207c5c1d4876806b81f9fd13bcefeebe?pvs=21)
