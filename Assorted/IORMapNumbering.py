###NOTES###
#You need to have the pdfminer python module installed on your computer to run this script#
#The "IOR Map No.: XXX-XXXX-XXX-XXX-XXX XX" that is in the legend box must be in the PDF#

###Variables###
infolder = r"G:\Paragon\MapNumbering\2016Figures\OriginalFigures\z16004"
outfolder = r"G:\Paragon\MapNumbering\2016Figures\RenamedPDFs"

###Modules###
import os
import glob
import fnmatch
from shutil import copyfile
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO

###Functions###
def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = file(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text

def getIORnum(filepath):
    x = convert_pdf_to_txt(filepath)
    array = x.split('\n')
    mapnum = fnmatch.filter(array, 'Imperial Map No.*')
    string = mapnum[0]
    IORnum = string[18:]
    return IORnum

###Script###
pdfs = glob.glob(infolder+"\\"+"*.pdf")
for x in pdfs:
    filename = getIORnum(x)
    dst = outfolder + "\\" + filename + ".pdf"
    copyfile(x, dst)
    print os.path.basename(x) + " HAS BEEN RENAMED: " + os.path.basename(dst)
    

    

