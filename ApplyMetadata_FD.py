import arcpy, time, os

##Variables##
fds = "FEATURE_DATASET"
source = "METADATA_SOURCE"

##Script##            
directory = os.path.dirname(fds)
arcpy.env.workspace = directory
fd = os.path.split(fds)[1]
for fc in arcpy.ListFeatureClasses('','',fd):
    target = os.path.join(directory,fd,fc)
    print target
    arcpy.MetadataImporter_conversion(source, target)
