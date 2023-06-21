# Notion Export Path Converter

The Notion Export Path Converter is a Python script that helps you process and convert the paths of Notion's exported files and folders. This script performs various operations, such as unzipping the export file, renaming folders, markdown files, images, and CSV files to a standardized format.

What it can do presently?

- File Path Formatting (Lowercasing, Removing Notion ID, Space Underscore replacement)
    - [x] Markdown Files
    - [x] Image Files (SVG, PNG, JPG, JPEG)
    - [x] CSV Files
    - [x] Folders
- Page Layout Formatting
    - [x] Notion Sidebar Removal
    - [x] Header Removal
- Link Formatting
    - [ ] Internal
    - [ ] External
- Text Formatting
    - [ ] Callout
    - [ ] Quote
    - [ ] Tables


## Getting Started

To get started with the Notion Export Path Converter, follow these steps:

1. Clone or download the repository to your local machine.
2. Open the `constants.py` file in a text editor.

## Configuration

In the `constants.py` file, you need to provide the following inputs:

- `notion_zip_file_path`: Specify the path of your Notion's exported zip file.
- `extract_to`: Specify the path of the directory where you want to extract the contents of the zip file.

Make sure to update the values of these variables with the appropriate paths.

## Execution

To execute the code and perform the path conversion, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the directory where the `main.py` file is located.
3. Run the following command:

```bash
python main.py
```

## Limitation

- Issues with naming the second word e.g. amazon%20s3.md --> amazon_s3.md but its becoming amazon.md
- Remove Table of Contents from End of Page
- Callout replacement
- Heading Order

Happy path conversion!
