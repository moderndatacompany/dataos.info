# Best Practices

This section outlines recommended best practices for developing, deploying, and managing Python Services on DataOS. Following these guidelines will help ensure your applications are secure, reliable, and maintainable.

### **Avoid embedding secrets directly in the manifest file**

Hardcoding secrets such as tokens, keys, or passwords into the manifest file directly creates major security risks. Instead, always secure the repository credentials using [Instance Secret](/resources/instance_secret/) (instance level) or [Secret](/resources/secret/) (Workspace level) and then refer to those secrets in the Service manifest file as shown in the example below.

```yaml
  dataosSecrets:
    - name: gitcred
      allKeys: true
      consumptionType: envVars
```

### **Start with modest requests/limits and right-size based on observation.**

When defining CPU and memory requests/limits for long-running Services, begin conservatively. Over-provisioning wastes resources, while under-provisioning can cause crashes. Monitor usage patterns in the Metis UI, then adjust allocations iteratively to achieve the right balance between stability and efficiency.


<div style="text-align: center;">
    <figure>
    <img src="/resources/stacks/python/cpumemory.png" 
        alt="Operations App" 
        style="border: 1px solid black; width: 80%; height: auto; display: block; margin: auto;">
    <figcaption style="margin-top: 8px; font-style: italic;">Operations App</figcaption>
    </figure>
</div>

### **For heavy workloads, set generous limits**

For heavy workloads, provision higher memory limits to prevent out-of-memory errors, and adopt chunked/batch processing strategies in Pandas or NumPy to break large datasets into manageable pieces, improving stability and throughput.

### **Persist large outputs to persistent volumes rather than memory**

Do not store large intermediate results or datasets entirely in memory, as this can lead to instability. Instead, write them to a persistent storage volume. This approach improves scalability, enables reproducibility, and avoids memory exhaustion.

### **Document dashboards and applications clearly in `README.md`**

Every project should include a `README.md` that explains the Pyrthon script. Additionally, document dashboards (Vizro) so that teams can quickly interpret metrics, troubleshoot issues, and improve collaboration.

### **Always name the dependency file `requirements.txt`**

A common mistake is misspelling the dependencies file as `requirement.txt` (singular). The Python ecosystem expects the file to be named `requirements.txt` (plural). Using the wrong name will break builds and deployments. Double-check the spelling before committing your code to avoid unnecessary errors.

```sql
your-repo/
└── app/                  # baseDir (configurable)
    ├── main.py           # REQUIRED – entry point
    └── requirements.txt  # REQUIRED – dependencies 
```