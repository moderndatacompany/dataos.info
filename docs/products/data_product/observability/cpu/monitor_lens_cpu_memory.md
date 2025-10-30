# Monitor the CPU and Memory Usage of a Lens

A Lens is a non-runnable Resource in DataOS; however, during the creation of a Lens model, a corresponding Service is automatically generated in the backend with the suffix ‘-api’. This Service handles the Lens’s API interface, and users can monitor its CPU and memory usage.

Additionally, when configuring a Lens Resource, users have the option to enable components such as a Worker, router, and metrics, depending on the specific use case. If these are defined in the Lens manifest, the system automatically provisions two additional Services, one for the router with suffix ‘-router’ and one for metrics with suffix ‘-metrics’, along with a Worker with suffix ‘-worker’. The below example shows a Lens ‘data-product-insights’ created three Services with suffix ‘-api’, ‘-metric’, and ‘router’, and a Worker with suffix ‘-worker’ added to the Lens identifier.

<div style="text-align: center;">
  <img src="/products/data_product/observability/cpu/lens/lens_dataproductinsightq_services_dataproductinsightsapi_dataproductinsightsmetric_dataproductinsightsrouter.png" style="border:1px solid black; width: 70%; height: auto">
  <figcaption><i>Lens-generated Services</i></figcaption>
</div>

<div style="text-align: center;">
  <img src="/products/data_product/observability/cpu/lens/lens_worker_dataproduct_insights_workers_dataproductinsightsworker.png" style="border:1px solid black; width: 70%; height: auto">
  <figcaption><i>Lens-generated Worker</i></figcaption>
</div>

To monitor the CPU and memory usage for these components, users should refer to the documentation linked below.

- [Monitor the CPU and memory usage of a Service](/products/data_product/observability/cpu/monitor_service_cpu_memory)
- [Monitor the CPU and memory usage of a Worker](/products/data_product/observability/cpu/monitor_worker_cpu_memory)
