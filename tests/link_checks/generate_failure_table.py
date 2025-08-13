import pandas as pd  # Import pandas for data manipulation
import re  # Import re for regular expression operations
from tabulate import tabulate  # Import tabulate for generating tables in various formats

# Define the path to the log file that will be parsed
log_file = 'link_checker.log'

# Initialize a dictionary to store parsed log data
data = {
    'Status': [],
    'URL': [],
    'Link Text': [],
    'Near Heading': [],
    'Found On': []
}

# Compile a regular expression to match log entries that indicate failures or errors
# This pattern captures the status (FAIL or ERROR), URL, status code or exception, link text, nearest heading, and the page URL
log_pattern = re.compile(r'\[(FAIL|ERROR)\] (.+?) - Status Code: (\d+|Exception) - Link text: "(.*?)", Near heading: "(.*?)", Found on: (.+)')

# Open and read the log file line by line
with open(log_file, 'r') as file:
    for line in file:
        # Search for the compiled regex pattern in each line
        match = log_pattern.search(line)
        if match:
            # If a match is found, extract the details from the log entry
            status, url, status_code, link_text, heading, found_on = match.groups()

            # Append the extracted details to the corresponding lists in the data dictionary
            data['Status'].append(f"{status} ({status_code})")
            data['Found On'].append(found_on)
            data['Near Heading'].append(heading)
            data['Link Text'].append(link_text)
            data['URL'].append(url)

# Convert the data dictionary into a pandas DataFrame for easier data manipulation
df = pd.DataFrame(data)

# Generate a Markdown table from the DataFrame using tabulate
# Specify 'pipe' as the table format to match Markdown table syntax
markdown_table = tabulate(df, headers='keys', tablefmt='pipe', showindex=False)

# Optionally, write the Markdown table to a markdown file
with open('link_failures_markdown_table.md', 'w') as md_file:
    md_file.write(markdown_table)
