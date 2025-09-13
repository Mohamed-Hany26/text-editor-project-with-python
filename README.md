# 📝Text Editor (Python GUI Project)

This is my **first GUI project using Python**, built with the `tkinter` library.  
It was developed as part of the course:  
**[Practical Projects using Python + ChatGPT](https://almdrasa.com/tracks/programming-foundations/courses/python-projects/)** on [Almdrasa](https://almdrasa.com).

---

## 🧠 Project Overview

The project simulates a basic text editor, similar to Notepad or a mini VS Code.  
It started with a visual plan using [Miro](https://miro.com), then was built step-by-step and improved with ChatGPT's support.

---

## 📂 Files in the Repository

| File                     | Description                                 |
|--------------------------|---------------------------------------------|
| `text editor.py`         | Basic version with open/save functionality |
| `text editor_chatgpt.py` | Enhanced version with explorer and themes   |
| `text editor Planning.jpg` | Visual planning of the project (Miro)     |

---

## 🚀 Features Comparison

### 🔹 Basic Version – `text editor.py`

- Simple text area
- Open `.txt` or any file
- Save current text to a new file
- Set window title based on opened file

---

### ⚡ Enhanced Version – `text editor_chatgpt.py`

Includes everything in the basic version, plus:

- ✅ **File Explorer** (like VS Code sidebar) that shows all files & folders
- ✅ **Dark/Light Theme Toggle**
- ✅ **Edit menu with Cut, Copy, Paste**
- ✅ **Open Folder support**
- ✅ **Unsaved changes warning on exit**
- ✅ **About Window with app info**
- ✅ **Dynamic UI using PanedWindow**
- ✅ Keeps track of the opened file and folder

---

## 🎯 Why This Project?

- It’s my **first GUI project using Python** 🐍
- Helped me understand real-world GUI layout concepts (Frames, PanedWindow, MenuBar, FileDialogs, etc.)
- Showed how to break down features from idea → design → implementation
- Boosted my confidence with `tkinter` and Python applications

---

## 🧰 Tech Used

- `Python 3.13`
- `tkinter` for GUI
- `os` for folder/file operations
- `filedialog`, `messagebox` for file & alert handling

---

## 📸 Preview

Planning board (Miro):  
`text editor Planning.jpg`

---

## ✅ Run the Project

Just make sure you have Python installed. Then run:

```bash
python "text editor.py"
# or
python "text editor_chatgpt.py"