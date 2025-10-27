import re
from pathlib import Path

# Root of your documentation
BASE_DIR = Path("docs/products/data_product/observability")

# Define a clean HTML block template to restore
CLEAN_TEMPLATE = '''<div style="text-align: center;">
  <img src="/products/data_product/observability/observability.png" style="width: 70%; height: auto;">
  <figcaption><i>Observability in DataOS</i></figcaption>
</div>'''

# Regex to detect any nested <div><img><figcaption> combinations with noisy captions
BAD_BLOCK_RE = re.compile(
    r'(<div style="text-align:\s*center;">\s*<div style="text-align:\s*center;">.*?<img[^>]+>.*?<figcaption><i>.*?</i></figcaption>\s*</div>\s*</div>)',
    re.DOTALL
)

changed_files = 0
for md_file in BASE_DIR.rglob("*.md"):
    content = md_file.read_text(encoding="utf-8")
    new_content, subs = BAD_BLOCK_RE.subn(CLEAN_TEMPLATE, content)
    if subs > 0:
        md_file.write_text(new_content, encoding="utf-8")
        changed_files += 1
        print(f"✅ Cleaned {subs} block(s) in {md_file.relative_to(BASE_DIR)}")

print(f"\n🎯 Cleanup complete. Modified {changed_files} file(s).")
