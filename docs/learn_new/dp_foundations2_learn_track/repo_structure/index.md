# Organizing and Versioning Your Data Product

A well-structured data product isn’t just about clean code—it’s about enabling collaboration, versioning, and long-term maintainability. In this module, you’ll set up your code repository, define a clean folder structure, and securely connect DataOS to your version control system.

---

## Step 1: Create and Set Up Your Code Repository

###  ** Initialize a Git Repository**

Start by creating a version-controlled repository using your team’s preferred platform:

- [Bitbucket](https://support.atlassian.com/bitbucket-cloud/docs/push-code-to-bitbucket/)

- [GitHub](https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github)

- [AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/getting-started.html)

Once created, clone the repository to your local machine and begin developing your DataOS resources.

---

### **Organize with a Clear Folder Structure**

Structure your data product directory to keep things organized:

![image](/learn_new/dp_foundations2_learn_track/deploy_dp_cli/dp_folder.png)


Each folder should hold only the relevant YAML specs for that DataOS component.

> 💡 **Tip:** A clear folder structure helps new contributors onboard faster and ensures smooth CI/CD workflows.

![dp_folder.png](attachment:b0841bad-fd9b-4713-9661-5aff6fcf8601:dp_folder.png)

---

## Step 2: Configure a Repo Secret for DataOS

To enable DataOS to sync from your private repository, you must define an **Instance Secret** containing Git credentials.

### **Define the Secret**

```yaml
name: bitbucket-cred
version: v1
type: instance-secret
tags:
  - dataos:type:resource
  - dataos:type:cluster-resource
  - dataos:resource:instance-secret
  - dataos:layer:user
description: bitbucket read secrets for repos.
owner: ""
layer: user
instance-secret:
  type: key-value
  acl: r
  data:
    GITSYNC_USERNAME: ""   # Your Git username
    GITSYNC_PASSWORD: ""   # Your Git token/password
```
### **Apply the Secret**
Run the following command in the CLI:

```bash
dataos-ctl apply -f bitbucket-secret.yaml

```

<aside class="callout">

🗣️ If your repo is public, you can skip the secret—but we recommend private repos for better security.

</aside>

## Step 3: Push the Data Product Directory to a Code Repository 

After developing all your code, you will push your local data product directory to a preferred hosted code repository.

## What’s Next?

Now that your data product has a structured, version-controlled foundation, it’s time to connect it to the real world—your source systems.

👉 [Next: Configure Source Connectivity](/learn_new/dp_foundations2_learn_track/data_source_connectivity/)

