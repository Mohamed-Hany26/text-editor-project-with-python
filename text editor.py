import tkinter as tk 
from tkinter.filedialog import askopenfilename , asksaveasfilename


def open_file():
    filepath = askopenfilename(
        filetypes=[("Text files","*.txt"), ("All files","*.*")]
        )
    if not filepath:
        return
    
    txt_edit.delete(1.0 , tk.END)
    with open(filepath , "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END , text)
    window.title(f'Almdrasa Text Editor - {filepath}')


def save_file():
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text files","*.txt"), ("All files","*.*")]
        )
    if not filepath:
        return

    with open(filepath , "w") as output_file:
        text = txt_edit.get(1.0 , tk.END)
        output_file.write(text)
    window.title(f'Almdrasa Text Editor - {filepath}')

window = tk.Tk()
window.title("Al Madrasa Text Editor")
window.rowconfigure(0,minsize=600)
window.columnconfigure(1,minsize=800)
# window.geometry("800x600")

txt_edit = tk.Text(window)

frame1 = tk.Frame(window , relief=tk.RAISED)


btn_open = tk.Button(frame1 , text="open file" , command=open_file)
btn_save = tk.Button(frame1 , text="save as", command=save_file)

btn_open.grid(column=0 , row=0, sticky="ew" , padx=5 , pady= 5)
btn_save.grid(column=0 , row=1 , sticky="ew" , padx= 5 , pady= 5)

frame1.grid(column= 0 , row=0 , sticky="ns")
txt_edit.grid(column=1 , row=0 , sticky="nsew")

window.mainloop()