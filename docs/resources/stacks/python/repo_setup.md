# Application set up

This section provides the steps to provision and structure a Python repository in GitHub. The objective here is not to deploy anything yet, but rather to set up a scaffolded project layout and code that adheres to DataOS Python Stack conventions.

## Steps to provision a repository

The repository must be provisioned in a proper structure. Follow the steps below to provision a repository.

### **Step 1. Create/Select a Repository**

Create or select a repository in GitHub or Bitbucket where you will add the Python code.

### **Step 2. Create  base directory**

Inside that repository, add a folder named app, which will include the Python script with a `.py` extension and a requirements file with a `.txt` extension.

```
python-stack/
└── app/                        # baseDir (referenced in service/stack manifest)
    ├── main.py                 # Application entry point (required)
    ├── requirements.txt        # Dependencies (required)
    └── .streamlit/             # Streamlit-specific configuration folder
        └── config.toml         # Custom Streamlit configuration
```

**Required Files**: At a minimum, the repo must include:

- `main.py`: Entry point script executed by the Stack.
- `requirements.txt`: Python dependencies in pip format.

### **Step 3. Add the Python code and dependencies**

In the file with the .py extension, add your Python script. In requirements.txt, add the requirements to run that Python script. 

**Example:**


<details>
    <summary>main.py</summary>

```python
import os
import sys
import streamlit as st

def run_app():
    st.set_page_config(page_title="Simple Calculator", layout="centered")

    st.title("Simple Calculator")
    st.caption("Minimal Streamlit app to demonstrate Python UI + requirements.txt")

    # Inputs
    a = st.number_input("First number", value=10.0)
    b = st.number_input("Second number", value=5.0)
    op = st.selectbox("Operation", ["add", "subtract", "multiply", "divide"])

    # Action
    if st.button("Compute"):
        if op == "add":
            result = a + b
        elif op == "subtract":
            result = a - b
        elif op == "multiply":
            result = a * b
        else:  # divide
            result = "Error: division by zero" if b == 0 else a / b

        st.success(f"Result: {result}")

def main():
    # Detect if running inside Streamlit; if not, relaunch with `streamlit run`
    if not os.environ.get("IS_RUNNING_STREAMLIT"):
        os.environ["IS_RUNNING_STREAMLIT"] = "1"
        script = os.path.abspath(__file__)
        os.execvpe(sys.executable, [sys.executable, "-m", "streamlit", "run", script], os.environ)
    else:
        run_app()

if __name__ == "__main__":
    main()

```
</details>


<details>
    <summary>requirements.txt</summary>
    
```bash
streamlit==1.37.1
```
</details>

<details>
    <summary>config.toml</summary>
    
```toml
# .streamlit/config.toml
[server]
port = 8050
address = "0.0.0.0"
baseUrlPath = "myapp"
```

</details>
    

### **Step 4. Push the changes**

Once the repository and the code are ready to be deployed, push the changes by executing the commands below.

```bash
git add .
git commit -m "chore: provision repo with baseDir, starter script, and requirements file"
git push -u origin main
```

### **Next Step**

After provisioning the repository, the next step is to [configure the Python Service](/resources/stacks/python/python_service/) manifest file to execute the Python script.