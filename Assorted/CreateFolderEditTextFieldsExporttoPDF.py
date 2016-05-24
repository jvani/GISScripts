import arcpy, time, os

#Variables#
folderName = "FOLDER_NAME"
textelement_namme = "TEXTELEMENT_NAME"
text_content = "TEXT_CONTENT"

#Constants#
MXDfolder = r"MXD_PATH"
MXDfolder=MXDfolder.replace("\\","\\\\")
PDFfolder =  r"PDF_PATH"
PDFfolder =PDFfolder.replace("\\","\\\\")

###Script###
#Create PDF Folder#
newpath = PDFfolder + "\\" + folderName
if not os.path.exists(newpath): os.makedirs(newpath)
print "New Folder Created"

#Export PDFs#
for fn in os.listdir(MXDfolder ):
     if fn[-3:]=="mxd":
                tempMXD = arcpy.mapping.MapDocument(MXDfolder +"\\"+fn)
                title =  tempMXD.filePath.split("\\")
                title = title[-1]
                pdf =title[0:-4]
                print pdf
                for textElement in arcpy.mapping.ListLayoutElements(tempMXD, "TEXT_ELEMENT"):
                    if textElement.name == textelement_name:
                         textElement.text = text_content
                tempMXD.save()
                arcpy.mapping.ExportToPDF(tempMXD, PDFfolder+"\\"+folderName+"\\"+str(pdf))
