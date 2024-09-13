# Monitor Talos APIs

Talos provides a comprehensive metrics monitoring system that can be accessed via the `/metric` endpoint. This system offers two types of metrics: Summary and Histogram. Below is a detailed explanation of how to configure and use these metrics.

## Enabling the metrics

### **Summary**

Summary metrics provide a statistical summary of the data, including configurable percentiles. In your `config.yaml` file, you can define summary metrics as follows:

```yaml

metrics:
  type: summary
  percentiles: [ 0.5, 0.75, 0.95, 0.98, 0.99, 0.999 ]

```
**Explanation**

- **type**: Specifies that the metric type is a summary.
- **percentiles**: A list of percentiles to calculate for the summary metrics. These percentiles help you understand the distribution of your data.


### **Histogram**

Histogram metrics provide a distribution of data across predefined buckets. In your `config.yaml` file, you can define histogram metrics as follows:

```yaml

metrics:
  type: histogram
  buckets: [ 0.003, 0.03, 0.1, 0.3, 1.5, 10, 20, 50 ]

```

**Explanation**

- **type**: Specifies that the metric type is a histogram.
- **buckets**: A list of bucket boundaries for the histogram. These buckets define the range of values for the histogram bins.

## Viewing metrics

After configuring your metrics in `config.yaml`, you can view the metrics by accessing the `/metric` endpoint in your browser or via a tool like `curl`:

```bash

curl http://your-talos-endpoint/metric

```

This endpoint will display the metrics in a readable format, showing the statistical summaries or histograms based on your configuration.