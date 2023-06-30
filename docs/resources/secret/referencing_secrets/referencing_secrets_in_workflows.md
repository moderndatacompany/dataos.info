# Referencing Secrets in Workflows

Similarly, you could have called upon the secret in a Workflow. Here’s a sample YAML to do it:

## Create a Secret YAML

Create a YAML File to define a Secret.

```yaml
version: v1
name: kv-secrets-for-sanity
type: secret
description: KV Secrets For Sanity
secret:
  type: key-value
  acl: r
  data:
    MOUNTED_SECRETS_1: x
    MOUNTED_SECRETS_2: y
```

## Apply the Secret YAML

Apply the secret to the workspace where you plan to execute your workflow.

```bash
dataos-ctl apply -f <path-to-secret-yaml> -w <workspace>
```

## Referencing the Secret in the Workflow YAML

Create a YAML file for your workflow. In the application spec of your workflow, make a reference to the secret.

```yaml
version: v1
name: smoketest-alpha
type: workflow
workflow:
  dag:
    - name: smoketest-alpha
      spec:
        stack: alpha
        compute: runnable-default
        envs:
          DEPOT_SERVICE_URL: "https://hip-ray.dataos.app/ds/api/v2"
          HEIMDALL_SERVICE_URL: "https://hip-ray.dataos.app/heimdall/api/v1"
        dataosSecrets: #here, we are calling it by referring to it as dataosSecrets
          - name: kv-secrets-for-sanity
            workspace: public
            keys:
             - MOUNTED_SECRETS_1
             - MOUNTED_SECRETS_2
        configs:
          check-alpha-stack.py: /Users/iamgroot/work/dataos/dataos-smoke-test/test-usecases/alpha/check-alpha-stack.py
        alpha:
          image: rubiklabs/smoketest:0.0.1
          command:
            - python3
          arguments:
            - /etc/dataos/config/check-alpha-stack.py
```