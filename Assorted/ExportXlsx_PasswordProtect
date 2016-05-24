import win32com.client, xlrd, PyPDF2, fnmatch, os, tkinter, glob
from PyPDF2 import PdfFileWriter, PdfFileReader
from tkinter import *
from tkinter import ttk

def printsheets(wb_path, pdf_location):
    o=win32com.client.Dispatch("Excel.Application")
    o.Visible=False
    wb=o.Workbooks.Open(wb_path)
    xls=xlrd.open_workbook(wb_path, on_demand=True)
    for x in xls.sheet_names():
        path_to_pdf=pdf_location+"\\_Delete_"+x+" Banked Time Summary.pdf"
        wb.WorkSheets(x).Select()
        wb.ActiveSheet.ExportAsFixedFormat(0, path_to_pdf)

def getpw(pdf_path):
    content=""
    pdf=PdfFileReader(pdf_path)
    pageObj=pdf.getPage(0)
    x=pageObj.extractText()
    array=x.split('\n')
    pwcell=fnmatch.filter(array, 'Password=*')
    string=pwcell[0]
    pw=string[9:]
    return(pw)

def encrypt(pdf_path, user_pass, owner_pass):
    
    path, filename = os.path.split(pdf_path)
    output_file = os.path.join(path, filename[8:])
    output = PyPDF2.PdfFileWriter()
    input_stream = PyPDF2.PdfFileReader(open(pdf_path, "rb"))
    
    for i in range(0, input_stream.getNumPages()):
        output.addPage(input_stream.getPage(i))
    outputStream = open(output_file, "wb")
    
    # Set user and owner password to pdf file
    output.encrypt(user_pass, owner_pass, use_128bit=True)
    output.write(outputStream)
    outputStream.close()

def runall():
    xslx=e1.get()
    print(xslx)
    pdf=e2.get()
    print(pdf)
    printsheets(xslx,pdf)
    for root, dirs, files in os.walk(pdf):
        for file in files:
            pdf_path=os.path.join(root,file)
            user_pass=getpw(pdf_path)
            owner_pass=getpw(pdf_path)
            encrypt(pdf_path, user_pass, owner_pass)
            print(file)

###App###
root=tkinter.Tk()
root.title("Create Banked Time Summary")
frame=Frame(root, width=600)
frame.pack()

e1=Entry(root)
e1.pack(fill=X)
e1.insert(0, "Path to .xlsx workbook.")

e2=Entry(root)
e2.pack(fill=X)
e2.insert(0, "Path to PDF output.")

button=ttk.Button(root, text="Run!", command=lambda:runall())
button.pack(fill=X)
