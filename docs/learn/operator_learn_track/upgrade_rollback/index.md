# Upgrade and rollback strategies

In this module, you’ll walk through the key steps for both upgrading and rolling back processes, ensuring your platform remains robust and scalable.

## Scenario

Imagine you’re the DataOS Operator, preparing for a scheduled upgrade to improve performance and add new features. Shortly after the upgrade, unforeseen issues disrupt system functionality. With limited time, you assess the situation, determine a rollback is needed, and follow a structured rollback plan to restore service.

Your goal is to ensure system stability, communicate with stakeholders, and effectively manage both the upgrade and rollback processes. You'll apply a combination of preparation, execution, and validation techniques to maintain smooth operations.

<aside class="callout">
🗣  This documentation covers only the rollback and upgrade scenarios for DataOS. For comprehensive details regarding the installation of DataOS, please contact the DataOS Platform Administrative from Modern Team.  
</aside>

## Upgrade strategy

Upgrading DataOS is a structured process that involves updating the **dataos-manager** tag and executing helm commands. In this module, you'll follow a clear set of steps to ensure a smooth upgrade process for DataOS.

## Steps for an upgrade

### **1. Release notes**

- First, review the detailed release notes outlining new features, fixes, and potential impacts.
- Then, communicate the planned upgrade date and expected downtime to all relevant stakeholders.

### **2. Downtime planning**

Identify a low-traffic window for the upgrade and seek approval for the schedule.

### **3. DataOS Manager tag update**

Update the `dataos-manager` image tag to the latest version, ensuring compatibility with the new release.

```yaml
instanceName:  <DATAOS_INSTANCE_DOMAIN_NAME> # Replace with DataOS Instance Domain Name
primeAccountId: <PRIME_ACCOUNT> # DataOS Prime Account ID
primeApiKey: <PRIME_API_KEY> # DataOS Prime API key
enablePrimeSyncUp: true
enablePrimeSyncExecute: true
primeSyncIntervalUp: 5m
primeSyncIntervalExecute: 30s
image:
    tag: **<DATAOS_MANAGER_TAG_VERSION> # Update the DataOS Manager tag version to the latest one**
redisUrl: redis-cache-master.caretaker.svc.cluster.local:6379
redisDbId: 8
redisUseTls: false
logLevel: info
cloudKernelJson: <CLOUD_KERNEL_JSON_IN_BASE64_ENCRYPTED_FORMAT>
```

### **4. Execution**

Use `helm install` to apply the upgrade.

```bash
helm install -n dataos-manager dataos-manager dataos/dataos-manager -f <path to dataos-manager values file>
```

Ensure all pre-installation checks are completed and dependencies are met.

### **5. Post-upgrade validation**

Validate the upgraded system’s functionality and monitor performance using Grafana.

## Rollback strategy

When a new release causes unforeseen issues, rolling back to a stable version becomes essential to restore platform stability. This section guides you through the **Rollback plan for DataOS**, helping you manage rollbacks efficiently and ensuring minimal disruption to operations.

## Pre-rollback preparation

Before initiating a rollback, ensure the following steps are completed:

### **1. Identify rollback target**

Determine the version to rollback to and verify compatibility with dependencies across the **User Space**, **Core Kernel**, and **Cloud Kernel** layers.

### **2. Backup and safeguard**

Create backups of critical data, configurations, and stateful components to ensure nothing is lost during the rollback.

### **3. Notify stakeholders**

Communicate with the following teams:

- Data Product Consumer teams
- Data Product Development teams
- DataOS Operators or Platform Administrators
- Any other affected teams (e.g., Operations staff)

### **4. Risk assessment**

Evaluate the potential impacts of the rollback, including downtime and service interruptions, and prepare mitigation strategies.


## Rollback execution

Follow a **top-down rollback strategy** to address each layer systematically and minimize dependencies and conflicts.

### **Step 1: User Space**

1. **New Stacks:** Remove recently introduced stacks and their dependencies.
2. **Stack upgrades:** For upgraded stacks, modify environment install files to use the previous stable versions and reinstall them.
3. **Clusters:** Revert cluster images to the last known stable version.

### **Step 2: Core Kernel**

1. **Component interdependencies:** Analyze semantic version changes and roll back interdependent components (e.g., *Poros*, *Metis*).
2. **Docker artifacts:** For minor version changes, roll back individual components. For major updates, consult with component owners for compatibility checks.

### **Step 3: Cloud Kernel**

1. **Infrastructure as Code:** Use cloud provider tools to rollback supported components.
2. **Kubernetes:** If a direct rollback isn’t possible, create a new cluster with the desired version.
3. **Postgres:** Restore data from a snapshot matching the target version.

## Post-rollback Verification

After executing the rollback, ensure the platform’s stability through comprehensive testing:

### **Step 1: Component testing**

1. Verify the functionality of rolled-back components across all layers.
2. Conduct regression testing to identify any residual issues.

### **Step 2: Data integrity checks**

Validate the consistency and accuracy of critical data.

### **Step 3: Inter-layer communication**

Confirm seamless interaction between the **User Space**, **Core Kernel**, and **Cloud Kernel**.


## Root cause analysis and continuous improvement

After the rollback, focus on long-term improvements:

### **1. Issue investigation**

Conduct a detailed analysis to pinpoint the cause of the rollback.

### **2. Documentation**

Record lessons learned, including challenges faced and areas for improvement.

### **3. Process enhancements**

Update release and rollback procedures, incorporating preventive measures.

### **4. Stakeholder debrief**

Share findings with relevant teams to ensure better preparation for future releases.

## Key Takeaways

- **Layered rollback strategy:** A top-down approach minimizes dependencies and ensures systematic execution.
- **Stakeholder collaboration:** Clear communication and coordination are essential for successful rollbacks.
- **Continuous improvement:** Post-rollback analysis helps enhance future release processes.