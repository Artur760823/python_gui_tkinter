import tkinter as tk
from tkinter import END, filedialog
import tkinter.font as TkFont
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

root = tk.Tk()
helv12 = TkFont.Font(family="Helvetica",size=12,weight="normal")
helv16 = TkFont.Font(family="Helvetica",size=16,weight="normal")

#canvas
canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

#logo
logo = Image.open('./assets/logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)


#instructions
instructions = tk.Label(root, text="Select a PDF file on your computer to extract all it's text", font=helv16)
instructions.grid(columnspan=3, column=0, row=1)
text_content=[]

print(text_content)

def open_file():
    browse_text.set("Loading...")
    file = askopenfile(parent=root, mode='rb', title="Choose a file", filetypes=[("Pdf file", "*.pdf")])
    if file:
        read_pdf = PyPDF2.PdfReader(file)
        page = read_pdf.pages[0]
        page_content = page.extract_text()
        text_content.append(page_content)
        print(text_content)
        #text box
        text_box = tk.Text(root, height=10, width=50, padx=15, pady=15)
        text_box.insert(1.0, page_content)
        text_box.tag_configure("center", justify="center")
        text_box.tag_add("center", 1.0, "end")
        text_box.grid(column=1, row=3)
        browse_text.set("Browse")


def save_file():
    f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    f.write(text_content[0])
    f.close()

#browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda:open_file(), font=helv12, bg="#20bebe", fg="white", height=2, width=15)
browse_text.set("Browse")
browse_btn.grid(column=0, row=2)

canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)

#saveButton

save_text = tk.StringVar()
save_btn = tk.Button(root, textvariable=save_text, command=lambda:save_file(), font=helv12, bg="#20bebe", fg="white", height=2, width=15)
save_text.set("Save")
save_btn.grid(column=2, row=2)

canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)


root.mainloop()