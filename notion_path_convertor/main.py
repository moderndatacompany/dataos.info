import zipfile
import os
import re
import constants


# Step 1: Unzips the Notion Export File
def unzip_file(zip_file_path, extract_to):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print("Step 1. Extraction Complete.")

# Step 2: Rename folders to lowercase with underscores instead of spaces
def rename_folders(directory):
    for root, dirs, files in os.walk(directory, topdown=False):
        for dir_name in dirs:
            old_path = os.path.join(root, dir_name)
            new_dir = re.sub(r"\s+", "_", dir_name.lower())
            new_dir = re.sub(r"_[^_]+$", "", new_dir)
            new_path = os.path.join(root, new_dir)
            os.rename(old_path, new_path)
    print("Step 2. Folder Renaming Complete.")

# Step 3: Rename markdown files to lowercase with underscores instead of spaces
def rename_markdown_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                old_path = os.path.join(root, file)
                new_file = re.sub(r"\s+", "_", file.lower())
                # new_file = re.sub(r"_\w{21,}\.md", ".md", new_file)
                new_path = os.path.join(root, new_file)
                os.rename(old_path, new_path)
                                # Read the content of the file
                with open(new_path, "r") as fileopen:
                    content = fileopen.read()
                
                # Remove the --- and </aside> block section
                # new_content = re.sub(r"\n---\n.*?\n</aside>", "", content, flags=re.DOTALL)
                
                # Write the modified content back to the file
                with open(new_path, "w") as fileopen:
                    fileopen.write(content)
    print("Step 3. Markdown Files Renaming Complete.")



# Step 4: Rename images to lowercase with underscores instead of spaces
def rename_images(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith((".png", ".jpg", ".jpeg", ".svg")):
                old_path = os.path.join(root, file)
                new_file = re.sub(r"\s+", "_", file.lower())
                # new_file = re.sub(r"_\w{21,}\.", ".", new_file)
                new_path = os.path.join(root, new_file)
                os.rename(old_path, new_path)
    print("Step 4. Image Files Renaming Complete.")

# Step 5: Rename csv to lowercase with underscores instead of spaces
def rename_csv_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".csv"):
                old_path = os.path.join(root, file)
                new_file = re.sub(r"\s+", "_", file.lower())
                # new_file = re.sub(r"_\w{21,}\.csv", ".csv", new_file)
                new_path = os.path.join(root, new_file)
                os.rename(old_path, new_path)
    print("Step 5. CSV Files Renaming Complete.")
            


def main():
    unzip_file(constants.notion_zip_file_path, constants.extract_to)
    rename_folders(constants.extract_to)
    rename_markdown_files(constants.extract_to)
    rename_images(constants.extract_to)
    rename_csv_files(constants.extract_to)


if __name__ == "__main__":
    main()
