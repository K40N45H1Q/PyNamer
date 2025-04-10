# PyNamer

**PyNamer** is a lightweight and easy-to-use Python command-line tool for batch renaming files in a specified directory.  
It supports two modes: random renaming and sequential numbering, while preserving file extensions.

## 📦 Features

- 🔀 Rename files to random names (letters + digits)
- 🔢 Rename files to a numbered sequence (e.g., 1.jpg, 2.png, ...)
- 🧼 Skips directories and the script file itself
- 💻 Cross-platform (Windows, macOS, Linux)

## 🛠️ Requirements

- Python 3.x  
*(No external dependencies required)*

## 🚀 Usage

```bash
python pynamer.py /path/to/directory [--random, -r] or [--numbers, -n]
