import os
import re

# Problem 1: Rename folders to lowercase with underscores instead of spaces
def rename_folders(directory):
    for root, dirs, files in os.walk(directory, topdown=False):
        for dir_name in dirs:
            old_path = os.path.join(root, dir_name)
            new_dir = re.sub(r"\s+", "_", dir_name.lower())
            new_path = os.path.join(root, new_dir)
            os.rename(old_path, new_path)

# Problem 2: Rename Markdown files to lowercase with underscores instead of spaces
def rename_markdown_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                old_path = os.path.join(root, file)
                new_file = re.sub(r"\s+", "_", file.lower())
                new_path = os.path.join(root, new_file)
                os.rename(old_path, new_path)

# Problem 3: Rename images to lowercase with underscores instead of spaces
def rename_images(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith((".png", ".jpg", ".jpeg", ".svg")):
                old_path = os.path.join(root, file)
                new_file = re.sub(r"\s+", "_", file.lower())
                new_path = os.path.join(root, new_file)
                os.rename(old_path, new_path)

# Problem 4: Update links in Markdown files to reflect the changes
def update_links(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r+') as f:
                    content = f.read()
                    # Update links to other Markdown files
                    content = re.sub(r"\]\((\.{1,2}/)(.*?\.md)\)", lambda m: "](%s%s)" % (m.group(1), m.group(2).lower().replace(" ", "_")), content)
                    # Update links to images
                    content = re.sub(r"\]\((\.{1,2}/)(.*?\.(?:png|jpg|jpeg|svg))\)", lambda m: "](%s%s)" % (m.group(1), m.group(2).lower().replace(" ", "_")), content)
                    # Rewind and overwrite the file
                    f.seek(0)
                    f.write(content)
                    f.truncate()

# Run the code
directory = "D:\All\dataos.info\docs\T sql syntaxes"  # Replace with the actual directory path
rename_folders(directory)
rename_markdown_files(directory)
rename_images(directory)
update_links(directory)

