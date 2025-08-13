import logging
import subprocess
import os
from bs4 import BeautifulSoup

# Configure logging
logging.basicConfig(filename='validation_log.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

def validate_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    try:
        BeautifulSoup(content, "html.parser")
        logging.info(f"Valid HTML: {file_path}")
        return True, "Valid HTML"
    except Exception as e:
        logging.error(f"Invalid HTML in {file_path}: {e}")
        return False, str(e)

def run_validation_on_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if file.endswith('.md'):
                # Run mdl for Markdown files
                result = subprocess.run(['mdl', file_path], capture_output=True, text=True)
                if result.returncode != 0:  # mdl found issues
                    logging.warning(f"Markdown Lint issues in {file_path}:\n{result.stdout}")
                else:
                    logging.info(f"No Markdown Lint issues: {file_path}")
            elif file.endswith('.html'):
                # Validate HTML files
                is_valid, output = validate_html(file_path)
                if not is_valid:
                    logging.warning(f"HTML validation issues in {file_path}:\n{output}")

directory = '<path-to-dataos.info-repository>'  # Update this path to your files directory
run_validation_on_directory(directory)
