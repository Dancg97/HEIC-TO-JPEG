# 🖼️ HEIC → JPG Batch Converter

A simple Python script that batch converts all `.HEIC` / `.HEIF` images in a folder to `.JPG`. Just drop it in the folder and double-click — no command line needed.

---

## ✨ Features

- 📁 Converts all `.HEIC` and `.HEIF` files in the same folder as the script
- 🖱️ Double-click to run — no terminal required
- 📦 Auto-installs dependencies (`pillow`, `pillow-heif`) if missing
- 🖼️ Preserves image quality (95% JPG quality by default)
- 🗂️ Original `.HEIC` files are kept — only `.JPG` copies are created
- ✅ Shows a clear summary of converted / failed files

---

## 🚀 Usage

1. Make sure **Python 3** is installed → [python.org](https://www.python.org/downloads/)
2. Drop `convert_heic_to_jpg.py` into the folder with your HEIC images
3. **Double-click** the script
4. Press **Enter** to close when done

Your `.JPG` files will appear in the same folder.

---

## 📋 Requirements

- Python 3.7+
- Dependencies are installed automatically on first run:
  - [`Pillow`](https://pypi.org/project/Pillow/)
  - [`pillow-heif`](https://pypi.org/project/pillow-heif/)

Or install them manually:

```bash
pip install pillow pillow-heif
```

---

## ⚠️ Windows note

For double-click to open a terminal window, `.py` files must be associated with Python.
If double-clicking opens Notepad instead:

> Right-click the file → **Open with** → **Python**

---

## 📄 License

MIT — free to use and modify.
