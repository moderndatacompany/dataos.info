# import os
# import csv

# base_folder = "docs/products/data_product/observability"  # update if needed
# log_file = os.path.join(base_folder, "image_rename_log.csv")

# # Create CSV log for tracking
# with open(log_file, "w", newline="", encoding="utf-8") as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(["Old Name", "New Name", "Folder Path"])

#     for root, _, files in os.walk(base_folder):
#         images = [f for f in files if f.lower().endswith((".png", ".jpg", ".jpeg"))]
#         if not images:
#             continue

#         # Determine prefix from folder name
#         folder_name = os.path.basename(root)
#         prefix = folder_name.replace(" ", "_").lower()

#         for i, img in enumerate(sorted(images), 1):
#             ext = os.path.splitext(img)[1]
#             new_name = f"{prefix}_image_{i}{ext}"
#             old_path = os.path.join(root, img)
#             new_path = os.path.join(root, new_name)

#             # Avoid overwriting
#             if os.path.exists(new_path):
#                 new_name = f"{prefix}_image_{i}_new{ext}"
#                 new_path = os.path.join(root, new_name)

#             os.rename(old_path, new_path)
#             writer.writerow([img, new_name, root])
#             print(f"✅ {img} → {new_name}")


import os
import pytesseract
from PIL import Image
import re

base_folder = "."

def sanitize_text(text):
    # Clean text and limit to 3–5 keywords for readability
    text = re.sub(r'[^A-Za-z0-9\s]', '', text)
    words = text.split()
    keywords = [w.lower() for w in words if len(w) > 3]
    return "_".join(keywords[:5]) or "context"

for root, _, files in os.walk(base_folder):
    images = [f for f in files if f.lower().endswith((".png", ".jpg", ".jpeg"))]
    if not images:
        continue

    folder_prefix = os.path.basename(root)
    for img in images:
        img_path = os.path.join(root, img)
        try:
            text = pytesseract.image_to_string(Image.open(img_path))
            context = sanitize_text(text)
            ext = os.path.splitext(img)[1]
            new_name = f"{folder_prefix}_{context}{ext}"
            new_path = os.path.join(root, new_name)

            # Avoid overwriting existing files
            if os.path.exists(new_path):
                base, ext = os.path.splitext(new_name)
                new_name = f"{base}_dup{ext}"
                new_path = os.path.join(root, new_name)

            os.rename(img_path, new_path)
            print(f"✅ {img} → {new_name}")
        except Exception as e:
            print(f"⚠️ Error processing {img}: {e}")
