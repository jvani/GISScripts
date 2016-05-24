import arcpy, time, os

#Variables#
folderName = "20160505"
week = "15/05/2016 - 19/05/2016"

#Constants#
MXDfolder = r"G:\Kearl\z2016\z16007\MXD"
MXDfolder=MXDfolder.replace("\\","\\\\")
PDFfolder =  r"G:\Kearl\z2016\z16007\PDF"
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
                    if textElement.name == "notes":
                         textElement.text = "<und>NOTES:</und>"+"\r\n"+"\r\n"+"Imagery Date: September 2015"+"\r\n"+"\r\n"+"Reporting Period: "+week
                tempMXD.save()
                arcpy.mapping.ExportToPDF(tempMXD, PDFfolder+"\\"+folderName+"\\"+str(pdf))
