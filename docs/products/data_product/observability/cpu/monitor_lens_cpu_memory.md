# Monitor the CPU and Memory Usage of a Lens
A Lens is a non-runnable Resource in DataOS; however, during the creation of a Lens model, a corresponding Service is automatically generated in the backend with the suffix ‘-api’. This Service handles the Lens’s API interface, and users can monitor its CPU and memory usage.

Additionally, when configuring a Lens Resource, users have the option to enable components such as a Worker, router, and metrics, depending on the specific use case. If these are defined in the Lens manifest, the system automatically provisions two additional Services, one for the router with suffix ‘-router’ and one for metrics with suffix ‘-metrics’, along with a Worker with suffix ‘-worker’. The below example shows a Lens ‘data-product-insights’ created three Services with suffix ‘-api’, ‘-metric’, and ‘router’, and a Worker with suffix ‘-worker’ added to the Lens identifier.

<div style="text-align: center;">
  <img src="/products/data_product/observability/status/lens/lens_lenses_dataproductinsights_explore_assets_meta.png" style="width: 70%; height: auto;">
  <figcaption><i>Lenses | data-product-insights 9 Explore Assets ¥ Meta Version: 0.5 Created: 1 month ago QA Owner: i A | Tier: - B | ...</i></figcaption>
</div>

<div style="text-align: center;">
  <img src="/products/data_product/observability/status/lens/lens_lenses_dataproductinsights_explore_assets_meta.png" style="width: 70%; height: auto;">
  <figcaption><i>Lenses | data-product-insights 9 Explore Assets ¥ Meta Version: 0.5 Created: 1 month ago QA Owner: i A | Tier: - B | ...</i></figcaption>
</div>

To monitor the CPU and memory usage for these components, users should refer to the documentation linked below.

- [Monitor the CPU and memory usage of a Service](https://www.notion.so/Monitor-the-CPU-and-memory-usage-of-a-Service-202c5c1d487680f1abd2e3ce672ad06b?pvs=21)
- [Monitor the CPU and memory usage of a Worker](https://www.notion.so/Monitor-the-CPU-and-memory-usage-of-a-Worker-202c5c1d487680b5ae7cd6638b796fa1?pvs=21)
