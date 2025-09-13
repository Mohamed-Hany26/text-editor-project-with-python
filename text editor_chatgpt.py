import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename, askdirectory
from tkinter import messagebox
import os

# 🔁 متغيرات عامة
current_file_path = None
current_folder_path = "."
is_modified = False
theme = "dark"

# ✅ دوال الوظائف الأساسية
def open_file():
    global current_file_path, is_modified
    filepath = askopenfilename(
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if not filepath:
        return
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.delete("1.0", tk.END)
        txt_edit.insert(tk.END, text)

    current_file_path = filepath
    is_modified = False
    window.title(f"AL Madrasa Text Editor - {filepath}")

def save_file():
    global current_file_path, is_modified
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)

    current_file_path = filepath
    is_modified = False
    window.title(f"AL Madrasa Text Editor - {filepath}")

def on_text_modified(event=None):
    global is_modified
    is_modified = True

def on_close():
    if is_modified:
        result = messagebox.askyesnocancel("Unsaved Changes", "You have unsaved changes. Save before exiting?")
        if result:  # Yes
            save_file()
            window.destroy()
        elif result is None:  # Cancel
            return
        else:  # No
            window.destroy()
    else:
        window.destroy()

# ✅ نافذة About
def show_about():
    about_window = tk.Toplevel(window)
    about_window.title("About")
    about_window.geometry("300x150")
    about_window.resizable(False, False)
    tk.Label(about_window, text="AL Madrasa CodePad", font=("Arial", 14, "bold")).pack(pady=10)
    tk.Label(about_window, text="تم تطويره بواسطة نبيل\nبمساعدة ChatGPT", font=("Arial", 10)).pack(pady=5)

# ✅ تغيير الثيم
def toggle_theme():
    global theme
    if theme == "dark":
        txt_edit.config(bg="white", fg="black", insertbackground="black")
        explorer_frame.config(bg="lightgray")
        explorer_label.config(bg="lightgray", fg="black")
        theme = "light"
    else:
        txt_edit.config(bg="#1e1e1e", fg="white", insertbackground="white")
        explorer_frame.config(bg="#2c2c2c")
        explorer_label.config(bg="#2c2c2c", fg="white")
        theme = "dark"
    load_folder(current_folder_path)

# ✅ أوامر التعديل
def cut_text():
    txt_edit.event_generate("<<Cut>>")

def copy_text():
    txt_edit.event_generate("<<Copy>>")

def paste_text():
    txt_edit.event_generate("<<Paste>>")

# ✅ فتح ملف من الإكسبلورر
def open_file_from_explorer(filepath):
    global current_file_path, is_modified
    try:
        with open(filepath, "r") as f:
            content = f.read()
            txt_edit.delete("1.0", tk.END)
            txt_edit.insert(tk.END, content)
        current_file_path = filepath
        is_modified = False
        window.title(f"AL Madrasa Text Editor - {filepath}")
    except Exception as e:
        messagebox.showerror("Error", f"Couldn't open file:\n{e}")

# ✅ تحميل محتويات الفولدر (ملفات + مجلدات)
def load_folder(path="."):
    global current_folder_path
    current_folder_path = path
    for widget in explorer_frame.winfo_children():
        if isinstance(widget, tk.Button):
            widget.destroy()

    files = os.listdir(path)
    files.sort()

    for file in files:
        full_path = os.path.join(path, file)

        if os.path.isdir(full_path):
            icon = "📁"
            cmd = lambda f=full_path: load_folder(f)
        else:
            icon = "📄"
            cmd = lambda f=full_path: open_file_from_explorer(f)

        btn = tk.Button(
            explorer_frame,
            text=f"{icon} {file}",
            anchor="w",
            relief="flat",
            bg="#2c2c2c" if theme == "dark" else "lightgray",
            fg="white" if theme == "dark" else "black",
            activebackground="#444" if theme == "dark" else "#ccc",
            activeforeground="white" if theme == "dark" else "black",
            command=cmd
        )
        btn.pack(fill="x", padx=5, pady=2)

# ✅ اختيار فولدر من المستخدم
def open_folder():
    folderpath = askdirectory()
    if folderpath:
        load_folder(folderpath)

# ✅ الواجهة الرئيسية
window = tk.Tk()
window.title("AL Madrasa Text Editor")
window.geometry("1000x600")
window.protocol("WM_DELETE_WINDOW", on_close)

window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

# ✅ PanedWindow
paned = tk.PanedWindow(window, orient=tk.HORIZONTAL, sashrelief=tk.RAISED)
paned.grid(row=0, column=0, sticky="nsew")

# ✅ Explorer Frame
explorer_frame = tk.Frame(paned, width=200, bg="#2c2c2c")
explorer_label = tk.Label(explorer_frame, text="📁 Explorer", fg="white", bg="#2c2c2c", anchor="w", font=("Arial", 11, "bold"))
explorer_label.pack(fill="x", padx=5, pady=(5, 10))
paned.add(explorer_frame)

# ✅ Text Editor
txt_edit = tk.Text(paned, wrap="word", font=("Consolas", 12), bg="#1e1e1e", fg="white", insertbackground="white")
txt_edit.bind("<<Modified>>", on_text_modified)
paned.add(txt_edit)

# ✅ Menu Bar
menu_bar = tk.Menu(window)

# 🔹 File Menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open File", command=open_file)
file_menu.add_command(label="Save As", command=save_file)
file_menu.add_command(label="Open Folder", command=open_folder)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=on_close)
menu_bar.add_cascade(label="File", menu=file_menu)

# 🔹 Edit Menu
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut", command=cut_text)
edit_menu.add_command(label="Copy", command=copy_text)
edit_menu.add_command(label="Paste", command=paste_text)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# 🔹 View Menu
view_menu = tk.Menu(menu_bar, tearoff=0)
view_menu.add_command(label="Toggle Theme", command=toggle_theme)
menu_bar.add_cascade(label="View", menu=view_menu)

# 🔹 Help Menu
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=show_about)
menu_bar.add_cascade(label="Help", menu=help_menu)

# ✅ ربط المينيو بالنافذة
window.config(menu=menu_bar)

# ✅ تحميل محتويات الفولدر الحالي
load_folder()

# ✅ Start App
window.mainloop()
