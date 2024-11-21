# Routine checks and configuration

In this module, you’ll learn how to manage Kubernetes and Pulsar configurations to keep DataOS running smoothly. These tools are key to ensuring the stability and scalability of the platform. You’ll gain hands-on experience with essential commands, resource adjustments, and monitoring techniques for troubleshooting, optimizing, and maintaining your DataOS infrastructure.

## Scenario 

Imagine you're working on a DataOS platform with varying traffic loads. One day, the system experiences a sudden surge in traffic, and resources need to be scaled quickly to handle the load. Additionally, you're dealing with a persistent issue in the `poros` namespace affecting the platform’s performance. With the help of Kubernetes and Pulsar, you need to troubleshoot the issue, adjust resources, and ensure everything runs smoothly. Follow the steps given in this topic, to manage these tasks and maintain a robust, efficient platform.

## Mastering Kubernetes commands

Familiarize yourself with the most commonly used Kubernetes commands for monitoring and troubleshooting the platform.:

### **Listing Kubernetes resources**

To keep track of services, pods, namespaces, and nodes, use the following commands:

- **List services:**
    
    ```bash
    kubectl get svc --namespace <namespace>
    kubectl get svc --all-namespaces
    ```
    
- **List pods:**
    
    ```bash
    kubectl get pods --namespace <namespace>
    kubectl get pods --all-namespaces
    ```
    
- **List namespaces:**
    
    ```bash
    kubectl get namespaces
    ```
    
- **List nodes:**
    
    ```bash
    kubectl get nodes
    ```
    

### **Root cause analysis (RCA) on Pods**

If you encounter an issue with a pod in a namespace, you’ll need to dig deeper. Here’s how you can investigate further:

- **Get pod details:**
    
    ```bash
    kubectl describe pod <pod-name> --namespace <namespace>
    ```
    
- **Get events:**
    
    ```bash
    kubectl get events --namespace <namespace>
    ```
    
- **Check pod logs:**
    
    ```bash
    kubectl logs <pod-name> --namespace <namespace>
    kubectl logs <pod-name> -c <container-name> --namespace <namespace>
    ```
    

### **Adjusting resources**

Adjusting resources is crucial during periods of high load or when optimizing for cost. Here's how you can manage resources:

**Scenarios for adjustments:**

- **Increase resources:**
    - During high traffic or batch jobs that require more compute power.
- **Decrease resources:**
    - After peak events, to optimize costs.
    - When the platform is idle.

### **Increasing resources**

To handle a sudden increase in traffic, you can increase CPU and memory for a deployment:

```bash
kubectl set resources deployment <deployment-name> --cpu=2000m --memory=2Gi --namespace <namespace>
```

### **Decreasing resources**

Once traffic normalizes, you can reduce resource allocation to save on costs:

```bash
kubectl set resources deployment <deployment-name> --cpu=500m --memory=1Gi --namespace <namespace>
```

## **Monitoring dashboards**

Proactive monitoring is key to keeping your platform healthy. Set up these dashboards to keep an eye on crucial metrics:

- **Kubernetes dashboards:**
    - CPU/Memory usage across pods, nodes, and namespaces.
    - Cluster health (e.g., node status and pod restarts).
    - Resource usage per namespace.
- **DataOS monitoring dashboards:**
    - Monitor cluster health using `dataos-ctl` or the Operations app.

**Critical Namespaces to monitor:**

- `poros`, `core-apps`, `heimdall`, `network-gateway`: Issues here can lead to **P1 incidents**.
- Other namespaces: `caretaker`, `system`, `public`.

---

## **Configuring Pulsar**

Configuring Pulsar is crucial to managing message queues efficiently. Here’s how you can adjust key settings:

### **Key Pulsar adjustments**

- **Broker configuration:**
    
    You may need to tweak the broker stats interval for better performance:
    
    ```bash
    pulsar.brokerStatsIntervalSeconds=60
    ```
    
- **Restarting brokers:**
    
    After making changes, restart the broker deployment:
    
    ```bash
    kubectl rollout restart deployment <broker-deployment> --namespace <namespace>
    ```
    

### **Storage and retention policies**

Ensure that Pulsar has sufficient storage and that you’ve set proper message retention policies:

- **Message retention policy:** Configure how long messages are retained in topics.
- **Scaling Pulsar:** Use Kubernetes Horizontal Pod Autoscaler to adjust broker and bookie replicas when needed.

By following these steps, you’ll be able to manage Kubernetes and Pulsar effectively, ensuring the stability, scalability, and efficiency of your DataOS platform.