#!/usr/bin/env python3
"""
Find YAML indentation issues in all markdown files
"""

import os
import re
import yaml
from yaml import YAMLError
import subprocess

def find_yaml_files():
    """Find all markdown files with YAML code blocks."""
    result = subprocess.run(['find', '.', '-name', '*.md', '-exec', 'grep', '-l', '```.*yaml\\|```.*yml', '{}', ';'], 
                           capture_output=True, text=True)
    return result.stdout.strip().split('\n') if result.stdout.strip() else []

def extract_yaml_blocks(content, filename):
    """Extract YAML code blocks from markdown content."""
    yaml_blocks = []
    lines = content.split('\n')
    i = 0
    
    while i < len(lines):
        line = lines[i]
        if re.match(r'^\s*```\s*(yaml|yml)\s*$', line, re.IGNORECASE):
            start_line = i + 1
            i += 1
            yaml_content = []
            
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
        i += 1
        
    return yaml_blocks

def check_yaml_issues(yaml_block):
    """Check for YAML syntax and indentation issues."""
    issues = []
    content = yaml_block['content']
    start_line = yaml_block['start_line']
    
    # Try to parse YAML
    try:
        yaml.safe_load(content)
    except YAMLError as e:
        error_msg = str(e)
        if 'mapping values are not allowed' in error_msg:
            issues.append("Mapping values alignment issue")
        elif 'could not find expected' in error_msg:
            issues.append("Structure/indentation issue")  
        elif 'found unhashable key' in error_msg:
            issues.append("Invalid key format (possibly template syntax)")
        elif 'expected alphabetic or numeric character' in error_msg:
            issues.append("Invalid character in alias/reference")
        else:
            issues.append(f"YAML parsing error: {error_msg.split(chr(10))[0]}")
    
    # Check indentation patterns
    lines = content.split('\n')
    for i, line in enumerate(lines):
        line_num = start_line + i
        
        if not line.strip() or line.strip().startswith('#'):
            continue
            
        # Mixed tabs and spaces
        if '\t' in line and ' ' in line[:len(line) - len(line.lstrip())]:
            issues.append(f"Mixed tabs/spaces at line {line_num}")
        
        # Odd indentation levels
        indent = len(line) - len(line.lstrip())
        if indent > 0 and indent % 2 != 0:
            issues.append(f"Odd indentation ({indent} spaces) at line {line_num}")
    
    return issues

def main():
    yaml_files = find_yaml_files()
    print(f"Scanning {len(yaml_files)} markdown files with YAML blocks...\n")
    
    total_files = 0
    total_yaml_blocks = 0
    files_with_issues = []
    
    for filepath in yaml_files:
        if not os.path.exists(filepath):
            continue
            
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            total_files += 1
            yaml_blocks = extract_yaml_blocks(content, filepath)
            total_yaml_blocks += len(yaml_blocks)
            
            file_issues = []
            for yaml_block in yaml_blocks:
                issues = check_yaml_issues(yaml_block)
                if issues:
                    file_issues.append({
                        'block': yaml_block,
                        'issues': issues
                    })
            
            if file_issues:
                files_with_issues.append({
                    'file': filepath,
                    'issues': file_issues
                })
                
        except Exception as e:
            print(f"Error reading {filepath}: {e}")
    
    # Generate summary report
    print("="*80)
    print("YAML INDENTATION ISSUES SUMMARY")
    print("="*80)
    print(f"Total files scanned: {total_files}")
    print(f"Total YAML blocks found: {total_yaml_blocks}")
    print(f"Files with issues: {len(files_with_issues)}")
    print("="*80)
    print()
    
    if not files_with_issues:
        print("✅ No YAML indentation issues found!")
        return
    
    # Group issues by type for summary
    issue_types = {}
    
    for file_data in files_with_issues:
        print(f"📁 {file_data['file']}")
        for issue_data in file_data['issues']:
            yaml_block = issue_data['block']
            issues = issue_data['issues']
            
            print(f"   └── YAML block (lines {yaml_block['start_line']}-{yaml_block['end_line']})")
            for issue in issues:
                print(f"       ❌ {issue}")
                # Count issue types
                issue_type = issue.split(':')[0] if ':' in issue else issue.split(' at ')[0]
                issue_types[issue_type] = issue_types.get(issue_type, 0) + 1
        print()
    
    print("="*80)
    print("ISSUE TYPES SUMMARY:")
    print("="*80)
    for issue_type, count in sorted(issue_types.items(), key=lambda x: x[1], reverse=True):
        print(f"{issue_type}: {count} occurrences")
    
    print(f"\n📝 Total issues found: {sum(issue_types.values())}")

if __name__ == "__main__":
    main()
