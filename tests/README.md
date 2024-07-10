# Tests for dataos.info

## Overview

This project consists of a Python-based tests to validate the links and content on dataos.info. 

## Features

- [x] Scans a given website for broken links.
- [x] Generates a detailed log of all links checked, including the status of each link.
- [x] Parses the generated log to identify and report broken links.
- [x] Outputs a Markdown table for easy visualization of broken links and their context.

## Installation

### **Prerequisites**
Before you install and run this project, make sure you have Python 3.11.7 or higher installed on your system. You can download Python from [python.org](https://www.python.org/).

### Setup
1. Clone this repository to your local machine using:
   ```shell
   git clone https://github.com/moderndatacompany/dataos.info.git
   ```
2. Navigate into the project directory:
   ```shell
   cd tests
   ```
3. Install the required Python packages:
   ```shell
   pip install -r requirements.txt
   ```

## Usage

### **Running the Link Checker**

To start the link checker, run:
```bash
python tests/link_checks/link_checker.py
```
Make sure to modify `tests/link_checks/link_checker.py` with the localhost URL of the website to be checked.

### **Parsing the Log File**

After running the link checker, you can parse the generated log file to identify broken links:

```bash
python tests/link_checks/generate_failure_table.py
```

This will generate a report in Markdown format, listing all broken links, their status codes, and the context in which they were found.