#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Context-aware image placement for DataOS docs (observability).
- Re-runs OCR on all images under observability/
- Computes semantic similarity between section text and OCR text
- Replaces dummy placeholders with best-match images (HTML format only, cautious)
- Generates CSV log of changes

Author: Shraddha + Assistant
"""

import os
import re
import csv
import json
import hashlib
from pathlib import Path
from typing import Dict, List, Tuple

# ---------- CONFIG ----------
BASE_DIR = Path(".").resolve()  # run script from observability/ root
IMG_EXTS = (".png", ".jpg", ".jpeg")
MD_EXT = ".md"

# Cautious mode threshold
SIMILARITY_THRESHOLD = 0.60

# How many lines above a placeholder to consider for context
CONTEXT_LINES_ABOVE = 10

# Standard HTML snippet to enforce for every replacement
HTML_TEMPLATE = '<div style="text-align: center;">\n  <img src="{src}" style="width: 70%; height: auto;">\n  <figcaption><i>{caption}</i></figcaption>\n</div>'

# Whether to prevent reusing the same image more than once
UNIQUE_USE = False  # set True if you want strict 1:1 mapping

# Output log file
LOG_PATH = BASE_DIR / "image_reference_log.csv"

# Cache files (speed-ups for re-runs; still re-OCRs each run but persists embeddings)
OCR_CACHE_JSON = BASE_DIR / ".ocr_text_cache.json"
EMB_CACHE_JSON = BASE_DIR / ".embeddings_cache.json"
# ----------------------------

# ML imports (lazy, so import errors are clearer)
from PIL import Image
import pytesseract
from sentence_transformers import SentenceTransformer, util

# ---------- UTILITIES ----------
def list_all_images(base: Path) -> List[Path]:
    return [p for p in base.rglob("*") if p.suffix.lower() in IMG_EXTS]

def list_all_markdown(base: Path) -> List[Path]:
    return [p for p in base.rglob(f"*{MD_EXT}")]

def file_hash(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def rel_from_observability(p: Path) -> str:
    # Produce URL-style relative path for <img src="...">
    return "/" + str(p.relative_to(BASE_DIR.parent.parent.parent)).replace(os.sep, "/")

def sanitize_caption(text: str) -> str:
    # Small, readable caption from OCR text
    t = re.sub(r"\s+", " ", text).strip()
    if len(t) > 120:
        t = t[:117] + "..."
    return t if t else "Observability in DataOS"

# ---------- OCR PIPELINE ----------
def build_ocr_cache(images: List[Path]) -> Dict[str, Dict]:
    """
    Returns a dict: { image_abs_path: { "hash": ..., "text": ... } }
    Re-runs OCR each time (as requested) but still uses file hash cache to avoid accidental reuse across runs.
    """
    cache = {}
    for img in images:
        try:
            text = pytesseract.image_to_string(Image.open(img))
        except Exception as e:
            text = ""
            print(f"[WARN] OCR failed for {img}: {e}")
        cache[str(img)] = {"hash": file_hash(img), "text": text}
    # persist for transparency
    with OCR_CACHE_JSON.open("w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)
    return cache

# ---------- EMBEDDINGS ----------
def load_model():
    # small, fast, good quality
    return SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def embed_texts(model, items: Dict[str, str]) -> Dict[str, List[float]]:
    """
    items: {key -> text}
    returns: {key -> embedding}
    """
    keys = list(items.keys())
    vals = [items[k] for k in keys]
    embs = model.encode(vals, normalize_embeddings=True)
    return {k: e for k, e in zip(keys, embs)}

# ---------- MARKDOWN PARSING ----------
MD_IMAGE_RE = re.compile(r'!\[[^\]]*?\]\((.*?)\)')
HTML_IMG_RE = re.compile(r'<img[^>]*src=["\'](.*?)["\'][^>]*>', re.IGNORECASE)

def find_placeholders(lines: List[str]) -> List[Tuple[int, str, str]]:
    """
    Returns a list of (line_index, type, current_src)
    type = "md" or "html"
    """
    out = []
    for i, line in enumerate(lines):
        # markdown
        for m in MD_IMAGE_RE.finditer(line):
            out.append((i, "md", m.group(1)))
        # html
        for m in HTML_IMG_RE.finditer(line):
            out.append((i, "html", m.group(1)))
    return out

def extract_context(lines: List[str], idx: int, window: int) -> str:
    start = max(0, idx - window)
    chunk = " ".join([l.strip() for l in lines[start:idx]])
    # Light cleanup
    chunk = re.sub(r"<[^>]+>", " ", chunk)
    chunk = re.sub(r"\s+", " ", chunk).strip()
    return chunk

def replace_line_with_html(line: str, new_src: str, caption: str) -> str:
    # Always standardize to our HTML block
    # Preserve indentation of current line
    indent = re.match(r"^\s*", line).group(0)
    html = HTML_TEMPLATE.format(src=new_src, caption=caption)
    html = "\n".join(indent + ln if ln.strip() else ln for ln in html.splitlines())
    return html

# ---------- MAIN ----------
def main():
    print("▶ Running context-aware image mapper (cautious mode)")
    print(f"Working dir: {BASE_DIR}")

    # 1) Gather assets
    images = list_all_images(BASE_DIR)
    md_files = list_all_markdown(BASE_DIR)

    if not images:
        print("[INFO] No images found under observability/. Exiting.")
        return
    if not md_files:
        print("[INFO] No markdown files found under observability/. Exiting.")
        return

    print(f"[INFO] Images: {len(images)} | Markdown files: {len(md_files)}")

    # 2) OCR (re-run) and caption prep
    ocr_cache = build_ocr_cache(images)
    image_text_map = {str(p): ocr_cache[str(p)]["text"] for p in images}

    # 3) Build embeddings (images)
    model = load_model()
    img_embeddings = embed_texts(model, image_text_map)

    # For optional uniqueness guarantees
    used_images = set()

    # 4) Open CSV log
    with LOG_PATH.open("w", newline="", encoding="utf-8") as fcsv:
        w = csv.writer(fcsv)
        w.writerow(["markdown_file", "line_number", "section_context_snippet", "chosen_image_rel_url", "similarity_score"])

        # 5) Process each Markdown
        for md in md_files:
            lines = md.read_text(encoding="utf-8").splitlines()
            placeholders = find_placeholders(lines)
            if not placeholders:
                continue

            updated = False

            for (i, ptype, current_src) in placeholders:
                section_ctx = extract_context(lines, i, CONTEXT_LINES_ABOVE)
                if not section_ctx:
                    continue

                ctx_emb = model.encode([section_ctx], normalize_embeddings=True)[0]

                # Similarity search
                best_image = None
                best_score = -1.0

                for img_path_str, emb in img_embeddings.items():
                    if UNIQUE_USE and img_path_str in used_images:
                        continue
                    score = float(util.cos_sim(ctx_emb, emb))
                    if score > best_score:
                        best_score = score
                        best_image = Path(img_path_str)

                # Decision (cautious)
                if best_image is not None and best_score >= SIMILARITY_THRESHOLD:
                    # Build relative URL from repo docs root (per your pattern)
                    new_src = rel_from_observability(best_image)
                    caption = sanitize_caption(ocr_cache[str(best_image)]["text"])

                    # Replace the line with standardized HTML block
                    new_line = replace_line_with_html(lines[i], new_src, caption)
                    lines[i] = new_line
                    updated = True
                    if UNIQUE_USE:
                        used_images.add(str(best_image))

                    # Log
                    snippet = section_ctx[:120] + ("..." if len(section_ctx) > 120 else "")
                    w.writerow([str(md.relative_to(BASE_DIR)), i + 1, snippet, new_src, f"{best_score:.4f}"])

                    print(f"[OK] {md.name}: line {i+1} → {best_image.name} (score={best_score:.2f})")
                else:
                    # No confident match — leave unchanged, but log decision
                    snippet = section_ctx[:120] + ("..." if len(section_ctx) > 120 else "")
                    w.writerow([str(md.relative_to(BASE_DIR)), i + 1, snippet, "", f"{best_score:.4f}"])
                    print(f"[SKIP] {md.name}: line {i+1} no confident match (best={best_score:.2f})")

            if updated:
                md.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"\n✅ Completed. Audit log written to: {LOG_PATH}")

if __name__ == "__main__":
    main()
