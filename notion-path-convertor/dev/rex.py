import re

def process_link(match):
    link = match.group(0)
    # Check if the link contains 'https://www.notion.so/'
    if 'https://www.notion.so/' in link:
        return link
    print(link)
    print("---")

    # Replace '%20' with '_' and lowercase the content in parentheses
    processed_link = re.sub(r'\((.*?)\)', lambda m: '(' + m.group(1).replace('%20', '_').lower() + ')', link)
    print(processed_link)
    print("---")

    # Split the content on '_' and '.'
    split_content = re.split(r'[_\.\/]', processed_link)
    print(split_content)
    print("---")
    # Remove strings greater than 30 characters
    filtered_content = [s if len(s) <= 30 else '' for s in split_content]
    print(filtered_content)
    print("---")

    # processed_link = re.sub(r'[^()\[\]]{31,}', '', processed_link)

    # Join the filtered content and replace the old string with the new one
    new_link_parts = [s for s in filtered_content if s]  # Skip empty strings
    new_link = '_'.join(new_link_parts)
    processed_link = processed_link.replace(''.join(split_content), new_link)
    print(processed_link)
    print("---")

    # Parse the link and replace '_/' with '_' and './' with '.'
    processed_link = processed_link.replace('_/', '_').replace('./', '.')
    print(processed_link)
    print("---")

    return processed_link

def transform_markdown_links(markdown):
    # Find all links in the Markdown text
    transformed_markdown = re.sub(r'\[.*?\]\(.*?\)', process_link, markdown)
    return transformed_markdown

# Example usage
markdown = """
# Title

This is a Markdown file containing links.

[****Depot Config Templates****](Depot%20bf0fbe4ed0e84b9098c391e7caee2f42/Depot%20Config%20Templates%20c26b0f2c441c4c55a1c3c23831667787.md)

[Storage](https://www.notion.so/Storage-fb33f69575ad46aca3c35a80aa233caa?pvs=21)

![Flow when Hive is chosen as the catalog type](Depot%20bf0fbe4ed0e84b9098c391e7caee2f42/depot_catalog.png)

Lorem ipsum dolor sit amet, consectetur adipiscing elit.

[Another Link](https://www.example.com)

Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
"""

transformed_markdown = transform_markdown_links(markdown)
print(transformed_markdown)
