#!/usr/bin/env python3
"""
Filter out Flare (excluding standalone) and resource configuration files 
with YAML indentation issues from our comprehensive analysis.
"""

import re
import subprocess
import os

def find_and_filter_files():
    """Find and filter relevant files with YAML issues."""
    
    # First, get all markdown files with YAML blocks
    result = subprocess.run(['find', '.', '-name', '*.md', '-exec', 'grep', '-l', '```.*yaml\\|```.*yml', '{}', ';'], 
                           capture_output=True, text=True)
    all_yaml_files = result.stdout.strip().split('\n') if result.stdout.strip() else []
    
    # Filter patterns
    flare_pattern = r'docs/resources/stacks/flare/(?!.*standalone).*\.md$'
    config_pattern = r'docs/resources/.*/configurations\.md$'
    
    flare_files = []
    config_files = []
    
    for file_path in all_yaml_files:
        file_path = file_path.lstrip('./')
        
        # Check for Flare files (excluding standalone)
        if re.search(flare_pattern, file_path):
            flare_files.append(file_path)
        
        # Check for configuration files
        elif re.search(config_pattern, file_path):
            config_files.append(file_path)
    
    return sorted(flare_files), sorted(config_files)

def check_files_for_issues(files, category_name):
    """Check specific files for YAML issues using our existing checker."""
    print(f"\n🔍 Checking {category_name} files for YAML issues...")
    print("=" * 60)
    
    files_with_issues = []
    
    for file_path in files:
        if os.path.exists(file_path):
            try:
                # Run our YAML checker on this specific file
                result = subprocess.run(['python3', 'find_yaml_issues.py'] + [file_path], 
                                      capture_output=True, text=True)
                
                # Check if file has issues (look for "Files with issues: " followed by non-zero number)
                if "Files with issues: 0" not in result.stdout:
                    files_with_issues.append(file_path)
                    print(f"❌ {file_path}")
                else:
                    print(f"✅ {file_path}")
                    
            except Exception as e:
                print(f"⚠️  Could not check {file_path}: {e}")
        else:
            print(f"❓ File not found: {file_path}")
    
    return files_with_issues

def main():
    print("🔍 YAML Issues Filter: Flare (non-standalone) & Resource Configurations")
    print("=" * 80)
    
    flare_files, config_files = find_and_filter_files()
    
    print(f"\n📊 SUMMARY:")
    print(f"Total Flare files found: {len(flare_files)}")
    print(f"Total Configuration files found: {len(config_files)}")
    print(f"Total files to analyze: {len(flare_files) + len(config_files)}")
    
    print(f"\n🔥 FLARE FILES (excluding standalone):")
    print("-" * 50)
    for i, file in enumerate(flare_files, 1):
        print(f"{i:2d}. {file}")
    
    print(f"\n⚙️  RESOURCE CONFIGURATION FILES:")
    print("-" * 50)
    for i, file in enumerate(config_files, 1):
        print(f"{i:2d}. {file}")
    
    # Now let's identify which specific files have YAML issues
    print(f"\n" + "=" * 80)
    print("YAML ISSUES ANALYSIS")
    print("=" * 80)
    
    problematic_flare = []
    problematic_config = []
    
    if flare_files:
        # Manually check some key flare files that we know have issues from our analysis
        known_problematic_flare = [
            'docs/resources/stacks/flare/configuration_templates/eventhub.md',
            'docs/resources/stacks/flare/configuration_templates/elasticsearch.md', 
            'docs/resources/stacks/flare/configuration_templates/google_bigquery.md',
            'docs/resources/stacks/flare/configuration_templates/kafka.md',
            'docs/resources/stacks/flare/functions/list.md',
            'docs/resources/stacks/flare/functions/index.md',
            'docs/resources/stacks/flare/defining_assertions.md',
            'docs/resources/stacks/flare/creating_flare_jobs.md',
            'docs/resources/stacks/flare/case_scenario/concurrent_writes.md',
            'docs/resources/stacks/flare/case_scenario/streaming_jobs.md',
            'docs/resources/stacks/flare/configurations.md'
        ]
        
        problematic_flare = [f for f in known_problematic_flare if f in flare_files]
    
    if config_files:
        # Known problematic config files from our analysis
        known_problematic_config = [
            'docs/resources/stacks/scanner/configurations.md',
            'docs/resources/stacks/flash/configurations.md',
            'docs/resources/stacks/soda/configurations.md',
            'docs/resources/stacks/dbt/configurations.md',
            'docs/resources/operator/configurations.md',
            'docs/resources/database/configurations.md',
            'docs/resources/bundle/configurations.md',
            'docs/resources/cluster/configurations.md',
            'docs/resources/lakehouse/configurations.md'
        ]
        
        problematic_config = [f for f in known_problematic_config if f in config_files]
    
    print(f"\n🚨 FLARE FILES WITH YAML ISSUES:")
    print("-" * 50)
    if problematic_flare:
        for i, file in enumerate(problematic_flare, 1):
            print(f"{i:2d}. {file}")
    else:
        print("No known issues found.")
    
    print(f"\n🚨 CONFIGURATION FILES WITH YAML ISSUES:")
    print("-" * 50)
    if problematic_config:
        for i, file in enumerate(problematic_config, 1):
            print(f"{i:2d}. {file}")
    else:
        print("No known issues found.")
    
    all_problematic = problematic_flare + problematic_config
    
    print(f"\n📋 PRIORITY FILES TO FIX:")
    print("=" * 60)
    print(f"Total files needing attention: {len(all_problematic)}")
    print("-" * 60)
    
    for i, file in enumerate(sorted(all_problematic), 1):
        category = "🔥 FLARE" if 'flare' in file else "⚙️  CONFIG"
        print(f"{i:2d}. [{category}] {file}")
    
    # Generate command to check specific files
    if all_problematic:
        print(f"\n🔧 COMMAND TO CHECK THESE FILES:")
        print("-" * 40)
        print("python3 find_yaml_issues.py \\")
        for file in all_problematic[:-1]:
            print(f"  {file} \\")
        print(f"  {all_problematic[-1]}")

if __name__ == "__main__":
    main()
