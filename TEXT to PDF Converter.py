from tkinter import *
from tkinter import ttk, filedialog
from fpdf import FPDF
import os

# Window
root = Tk()
root.title("PDF Conveter")
root.geometry("600x240")

# Frame
frame = LabelFrame(root, text="PDF Converter", font=('Times', 15, "bold"),
            bd=0, fg='black', labelanchor='n', relief=GROOVE)
frame.place(x=50,y=35)

# Labels
open_file = Label(frame, text="Open File", font=('Times', 15, 'bold'))
open_file.grid(row=0, column=0, padx=15, pady=15, sticky='e')

format_label = Label(frame, text="Format", font=('Times', 15, 'bold'))
format_label.grid(row=1, column=0, padx=15, pady=15, sticky='e')

info_label = Label(frame, font=('Times', 15, 'bold'))
info_label.grid(row=2, column=1, pady=15)

# File Entry
file= StringVar()
file_entry = Entry(frame, textvariable=file,font=("Times", 11, 'bold'), bd=2, relief=RIDGE)
file_entry.grid(row=0,column=1, padx=15, pady=15)
file_path = " "

def browse():
    file_path = filedialog.askopenfilename(initialdir = os.getcwd(),
                    title= "select file",filetypes = (("Text file","*.txt"),("All files","*.*")))
    file.set(file_path)

def convert():
    global file_path, file

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Times", size = 24)
    text_file = open(file.get(), "r")
    for text in text_file:
            pdf.cell(200, 10, txt = text, ln=1,align="E")
    name=file.get().split('/')[-1]
    pdf.output(f"{name.split('.')[0]}.{format1.get()}")


# Button
browser_file = Button(frame, text="Browse File", font=('Times', 15, 'bold'),
                    bd=2, relief=RIDGE,bg='white', command = browse)
browser_file.grid(row=0,column=2,padx=15,pady=15)

convert_file = Button(frame, text="Convert File", font=('Times', 15, 'bold'),
                    bd=2, relief=RIDGE,bg='white', command = convert)
convert_file.grid(row=1,column=2,padx=15,pady=15)

# ComboBox
format1 = StringVar()
file_formats = ['PDF']

format_combo = ttk.Combobox(frame, textvariable=format1, font=('Times', 15, 'bold'),
                    width=12,state=DISABLED)
format_combo['value']=file_formats

format_combo.current(0)
format_combo.grid(row=1,column=1,padx=15,pady=15)


root.mainloop()