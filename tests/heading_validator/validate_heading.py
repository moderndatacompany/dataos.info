import os
import re
from markdown2 import markdown
from titlecase import titlecase
import logging

# Configure logging
logging.basicConfig(filename='headings_validation.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

def is_title_case(text):
    return text == titlecase(text)

def is_sentence_case(text, exceptions=[]):
    words = text.split()
    if not words:
        return True
    if words[0][0] != words[0][0].upper():
        return False
    for word in words[1:]:
        if word in exceptions:
            continue
        if word[0] == word[0].upper() and not word.isupper():
            return False
    return True

def validate_headings(file_path, exceptions=[]):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    html = markdown(text)
    headings = re.findall(r'<h([1-6])>(.*?)<\/h\1>', html)

    for level, heading in headings:
        if level == '1' and not is_title_case(heading):
            logging.warning(f"{file_path}: H1 heading not in title case - {heading}")
        elif level != '1' and not is_sentence_case(heading, exceptions):
            logging.warning(f"{file_path}: H{level} heading not in sentence case - {heading}")

# Example usage
exceptions = ["Cluster", "Lakehouse", "Monitor", "Pager", "Monitor", "Secret", "Service", "Worker", "Workflow", "Bundle", "Compute", "Depot", "Instance Secret", "Operator", "Policy", "Stack"]  # Add your exceptions here
directory = '/home/iamgroot/modern_office/docX/reference_doc/development/dataos.info/docs'  # Update this path

for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith('.md'):
            file_path = os.path.join(root, file)
            validate_headings(file_path, exceptions)
