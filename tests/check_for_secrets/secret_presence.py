import os
import re

# Configuration
documentation_dir = '/home/piyushjoshi/modern_office/docX/reference_doc/development/dataos.info'  # Update with your directory path
log_file_path = 'secrets_detection_log.txt'

# Secret patterns
secret_patterns = [
    r'\b(?:API_KEY|APIKEY|TOKEN):\s*"?[A-Za-z0-9]{32,}"?',
    r'\b[A-Za-z0-9]{40}\b',
]

def is_excluded(file_path, excluded_dirs, excluded_extensions):
    """Check if the file should be excluded based on its path or extension."""
    if any(excluded_dir in file_path for excluded_dir in excluded_dirs):
        return True
    return file_path.endswith(tuple(excluded_extensions))

def search_for_secrets(file_path, patterns):
    findings = []
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        for i, line in enumerate(file, start=1):
            for pattern in patterns:
                if re.search(pattern, line):
                    findings.append((i, line.strip()))
    return findings

def scan_documentation(directory, patterns, log_file_path):
    excluded_dirs = ['.git','docs/api_docs']
    excluded_extensions = ['.git', '.svg', '.png']
    with open(log_file_path, 'w') as log_file:
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                # Check if the file is in an excluded directory or has an excluded extension
                if is_excluded(file_path, excluded_dirs, excluded_extensions):
                    continue
                findings = search_for_secrets(file_path, patterns)
                if findings:
                    log_file.write(f'Potential secrets found in {file_path}:\n')
                    for line_no, line in findings:
                        log_file.write(f'  Line {line_no}: {line}\n')
                    log_file.write('\n')

if __name__ == '__main__':
    scan_documentation(documentation_dir, secret_patterns, log_file_path)
    print(f"Scan complete. Findings have been logged to {log_file_path}.")
