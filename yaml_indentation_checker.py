#!/usr/bin/env python3
"""
YAML Indentation Checker for Markdown Files

This script analyzes YAML code blocks in markdown files to identify indentation issues.
"""

import os
import re
import sys
from pathlib import Path
import yaml
from yaml import YAMLError

class YAMLIndentationChecker:
    def __init__(self):
        self.issues = []
        self.files_checked = 0
        self.yaml_blocks_found = 0
        
    def extract_yaml_blocks(self, content, filename):
        """Extract YAML code blocks from markdown content."""
        yaml_blocks = []
        lines = content.split('\n')
        i = 0
        
        while i < len(lines):
            line = lines[i]
            # Look for YAML code block start
            if re.match(r'^\s*```\s*(yaml|yml)\s*$', line, re.IGNORECASE):
                start_line = i + 1
                i += 1
                yaml_content = []
                
                # Collect YAML content until closing ```
                while i < len(lines) and not re.match(r'^\s*```\s*$', lines[i]):
                    yaml_content.append(lines[i])
                    i += 1
                
                if yaml_content:
                    yaml_blocks.append({
                        'content': '\n'.join(yaml_content),
                        'start_line': start_line,
                        'end_line': i,
                        'filename': filename
                    })
                    self.yaml_blocks_found += 1
            i += 1
            
        return yaml_blocks
    
    def check_yaml_syntax(self, yaml_block):
        """Check if YAML syntax is valid and identify indentation issues."""
        issues = []
        content = yaml_block['content']
        filename = yaml_block['filename']
        start_line = yaml_block['start_line']
        
        try:
            # Try to parse the YAML
            yaml.safe_load(content)
        except YAMLError as e:
            error_msg = str(e)
            if 'mapping values are not allowed here' in error_msg:
                issues.append(f"Indentation issue: Mapping values not properly aligned")
            elif 'could not find expected' in error_msg:
                issues.append(f"Indentation issue: {error_msg}")
            elif 'found character that cannot start any token' in error_msg:
                issues.append(f"Indentation issue: Invalid character or alignment")
            else:
                issues.append(f"YAML syntax error: {error_msg}")
        
        # Check for common indentation patterns
        lines = content.split('\n')
        for i, line in enumerate(lines):
            line_num = start_line + i
            
            # Skip empty lines and comments
            if not line.strip() or line.strip().startswith('#'):
                continue
                
            # Check for inconsistent indentation (mixing tabs and spaces)
            if '\t' in line and ' ' in line[:len(line) - len(line.lstrip())]:
                issues.append(f"Line {line_num}: Mixed tabs and spaces")
            
            # Check for incorrect indentation levels (not multiples of 2)
            indent = len(line) - len(line.lstrip())
            if indent > 0 and indent % 2 != 0:
                issues.append(f"Line {line_num}: Odd indentation level ({indent} spaces)")
            
            # Check for list items with incorrect indentation
            stripped = line.lstrip()
            if stripped.startswith('- '):
                # List items should have consistent indentation
                if i > 0:
                    prev_line = lines[i-1].strip()
                    if prev_line and not prev_line.startswith('-') and not ':' in prev_line:
                        # This might be an incorrectly indented list item
                        pass
        
        return issues
    
    def check_file(self, filepath):
        """Check a single markdown file for YAML indentation issues."""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            self.files_checked += 1
            yaml_blocks = self.extract_yaml_blocks(content, filepath)
            
            for yaml_block in yaml_blocks:
                issues = self.check_yaml_syntax(yaml_block)
                if issues:
                    self.issues.append({
                        'file': filepath,
                        'yaml_block': yaml_block,
                        'issues': issues
                    })
                    
        except Exception as e:
            print(f"Error reading file {filepath}: {e}")
    
    def generate_report(self):
        """Generate a report of all indentation issues found."""
        print(f"\n{'='*60}")
        print("YAML Indentation Issues Report")
        print(f"{'='*60}")
        print(f"Files checked: {self.files_checked}")
        print(f"YAML blocks found: {self.yaml_blocks_found}")
        print(f"Files with issues: {len(self.issues)}")
        print(f"{'='*60}\n")
        
        if not self.issues:
            print("🎉 No YAML indentation issues found!")
            return
        
        for issue_group in self.issues:
            filepath = issue_group['file']
            yaml_block = issue_group['yaml_block']
            issues = issue_group['issues']
            
            print(f"📄 File: {filepath}")
            print(f"   YAML Block: Lines {yaml_block['start_line']}-{yaml_block['end_line']}")
            
            for issue in issues:
                print(f"   ❌ {issue}")
            
            # Show the problematic YAML content (first 10 lines)
            yaml_lines = yaml_block['content'].split('\n')[:10]
            print("   YAML Content (first 10 lines):")
            for i, line in enumerate(yaml_lines):
                line_num = yaml_block['start_line'] + i
                print(f"   {line_num:3d}: {repr(line)}")
            
            if len(yaml_block['content'].split('\n')) > 10:
                print(f"   ... ({len(yaml_block['content'].split('\n')) - 10} more lines)")
            
            print()


def main():
    if len(sys.argv) > 1:
        # Use provided file list
        files_to_check = sys.argv[1:]
    else:
        # Read the file list from the previous command output
        file_list = """./docs/products/data_product/how_to_guides/build.md
./docs/products/data_product/how_to_guides/design.md
./docs/products/data_product/how_to_guides/deploy.md""".strip().split('\n')
        # Take first 20 files as sample
        files_to_check = file_list[:20]
    
    checker = YAMLIndentationChecker()
    
    print("Checking YAML indentation in markdown files...")
    
    for filepath in files_to_check:
        filepath = filepath.strip()
        if os.path.exists(filepath):
            checker.check_file(filepath)
        else:
            print(f"Warning: File not found: {filepath}")
    
    checker.generate_report()

if __name__ == "__main__":
    main()
