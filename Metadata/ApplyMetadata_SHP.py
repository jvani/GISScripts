import os, arcpy, time

###Variables###
# The directory is the folder that all shapefiles in.
# The source is your perfect metadata that will be applied to all .shp files in the directory.
directory = r"DIRECTORY"
source = r"METADATA_SOURCE"

###Script###
for file in os.listdir(directory):
    if file.endswith(".shp"):
        target =  directory + "/" + file
        print target
        arcpy.MetadataImporter_conversion(source, target)
