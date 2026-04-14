#!/usr/bin/env python3
"""
Batch HEIC → JPG Converter
Double-click to run. Converts all HEIC files in the same folder as this script.
"""

import sys
import os
import subprocess
from pathlib import Path

# ── Auto-install dependencies if missing ────────────────────────────────────
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package, "-q"])

try:
    from pillow_heif import register_heif_opener
    from PIL import Image
    register_heif_opener()
except ImportError:
    print("📦 Installing required packages, please wait...\n")
    install("pillow")
    install("pillow-heif")
    from pillow_heif import register_heif_opener
    from PIL import Image
    register_heif_opener()

# ── Main conversion ─────────────────────────────────────────────────────────
def convert_heic_to_jpg(folder: Path, quality: int = 95):
    heic_files = [
        f for f in folder.iterdir()
        if f.suffix.lower() in (".heic", ".heif")
    ]

    if not heic_files:
        print("⚠️  No .HEIC or .HEIF files found in this folder.")
        return

    print(f"📂 Folder : {folder}")
    print(f"🔍 Found  : {len(heic_files)} file(s) to convert\n")

    success, failed = 0, 0

    for heic_file in sorted(heic_files):
        jpg_file = heic_file.with_suffix(".jpg")
        try:
            with Image.open(heic_file) as img:
                img = img.convert("RGB")
                img.save(jpg_file, "JPEG", quality=quality, optimize=True)
            print(f"  ✅ {heic_file.name}  →  {jpg_file.name}")
            success += 1
        except Exception as e:
            print(f"  ❌ {heic_file.name}  →  ERROR: {e}")
            failed += 1

    print(f"\n{'─'*50}")
    print(f"✔ Converted : {success}")
    if failed:
        print(f"✘ Failed    : {failed}")
    print(f"\n✅ Done! JPG files saved in the same folder.")


# ── Entry point ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # Always use the folder where THIS script lives
    script_folder = Path(__file__).resolve().parent

    print("=" * 50)
    print("   HEIC → JPG Batch Converter")
    print("=" * 50 + "\n")

    convert_heic_to_jpg(script_folder)

    print("\nPress Enter to close...")
    input()
