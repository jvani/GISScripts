print "Opening..."

import os, shutil, arcpy, time, Tkinter, ttk
from time import strftime
from Tkinter import *

##Notes##
"""
This application will:
    1) Search through a directory and all MXDs for contained feature classes that are sourced to C: or G:\Users.
    2) Create a list of the identified feature classes in a text file.
"""

##Modules##
import shutil, time, Tkinter, ttk
from Tkinter import *

##Function##
start =time.time()
def createdirectory():
        newpath = "G:\Paragon\Scripts\FileManagement\UserDrive_FC_Cleanup\Results" + "\\" + strftime("%Y%m%d")
        if not os.path.exists(newpath): os.makedirs(newpath)
        print "New Output Folder Created"
        
def list_files(dir):                                                                                                  
        r = []                                                                                                            
        subdirs = [x[0] for x in os.walk(dir)]                                                                            
        for subdir in subdirs:
            if "Archive" in subdir:
                continue        
            files = os.walk(subdir).next()[2]                                                                             
            if (len(files) > 0):                                                                                          
                for file in files:
                   try:
                    if file[-4:]==".mxd":
                        mxd = arcpy.mapping.MapDocument(subdir + "/" + file)
                        for layer in arcpy.mapping.ListLayers(mxd):
                          try:
                                row = ""
                                path = layer.dataSource
                                if  "G:\Users" in path or "C:" in path or "U:" in path:
                                        mxdPath=subdir + "/" + file
                                        row+= layer.name +","
                                        row+= layer.dataSource +","
                                        row+= subdir + "/" + file+","
                                        r.append(row)
                                        break
                                else:
                                        continue
                                break
                          except:
                                 pass
                   except:
                        path= subdir + "/" + file 
                        print path                                                                             
        return r

def runscript(dir, outputname):
        Layerlist=list_files(dir)
        file_name=time.strftime("G:\Paragon\Scripts\FileManagement\UserDrive_FC_Cleanup\Results\%Y%m%d")
        text_file = open(file_name+"\\"+outputname+".txt", "w")
        for x in Layerlist:
                text_file.write(x+"\n")
        text_file.close()
        print outputname+" has been prepared."

def runspecial():
        dir=str(d.get())
        outputname=str(o.get())
        Layerlist=list_files(dir)
        file_name=time.strftime("G:\Paragon\Scripts\FileManagement\UserDrive_FC_Cleanup\Results\%Y%m%d")
        text_file = open(file_name+"\\"+outputname+".txt", "w")
        for x in Layerlist:
                text_file.write(x+"\n")
        text_file.close()
        print outputname+" has been prepared."

def runall():
        createdirectory()
        runscript("G:\ATCO", "ATCO_2016")
        runscript("G:\FortHills\z2016", "FortHills_2016")
        runscript("G:\Kearl\z2016", "Kearl_2016")
        runscript("G:\MiscellaneousProjects\z2016", "Misc_2016")
        runscript("G:\ShellAlbianSands\JackpineMine\z2016", "ShellJPM_2016")
        runscript("G:\ShellAlbianSands\MuskegRiverMine\z2016", "ShellMRM_2016")
        runscript("G:\TCPL\z2016", "TCPL_2016")

##App##
root=Tkinter.Tk()
root.title("User Drive FC Check")
frame=Frame(root, width=400)
frame.pack()

testbutton=ttk.Button(root, text="Run All", command=lambda:runall())
testbutton.pack(fill=X)

testbutton=ttk.Button(root, text="Create Directory", command=lambda:createdirectory())
testbutton.pack(fill=X)

testbutton=ttk.Button(root, text="ATCO 2016", command=lambda:runscript("G:\ATCO", "ATCO_2016"))
testbutton.pack(fill=X)

testbutton=ttk.Button(root, text="Fort Hills 2016", command=lambda:runscript("G:\FortHills\z2016", "FortHills_2016"))
testbutton.pack(fill=X)

testbutton=ttk.Button(root, text="Kearl 2016", command=lambda:runscript("G:\Kearl\z2016", "Kearl_2016"))
testbutton.pack(fill=X)

testbutton=ttk.Button(root, text="Misc. Project 2016", command=lambda:runscript("G:\MiscellaneousProjects\z2016", "Misc_2016"))
testbutton.pack(fill=X)

testbutton=ttk.Button(root, text="Shell (JPM) 2016", command=lambda:runscript("G:\ShellAlbianSands\JackpineMine\z2016", "ShellJPM_2016"))
testbutton.pack(fill=X)

testbutton=ttk.Button(root, text="Shell (MRM) 2016", command=lambda:runscript("G:\ShellAlbianSands\MuskegRiverMine\z2016", "ShellMRM_2016"))
testbutton.pack(fill=X)

testbutton=ttk.Button(root, text="TCPL 2016", command=lambda:runscript("G:\TCPL\z2016", "TCPL_2016"))
testbutton.pack(fill=X)

d=Entry(root)
d.pack(fill=X)
d.insert(0,"Directory to search.")
o=Entry(root)
o.pack(fill=X)
o.insert(0,"Output .txt file")
testbutton=ttk.Button(root, text="Run", command=lambda:runspecial())
testbutton.pack(fill=X)

root.mainloop()

