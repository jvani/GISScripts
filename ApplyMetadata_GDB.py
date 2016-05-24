import arcpy, time, os

##Variables##
directory = "GEODATABASE"
source = "METADATASOURCE"

##Script##
r = []
subdirs = [x[0] for x in os.walk(directory)]
for subdir in subdirs:
    if "Archive" in subdir:
        continue
    if subdir.endswith(".gdb"):
        arcpy.env.workspace = subdir
        for fds in arcpy.ListDatasets('', 'feature') + ['']:
            for fc in arcpy.ListFeatureClasses('','',fds):
                target = os.path.join(subdir,fds,fc)
                print target
                arcpy.MetadataImporter_conversion(source, target)
            
