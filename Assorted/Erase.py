##Erase function for users without Spatial Analyst License
##The extent of EraseFC is deleted from the TargetFC. The output is saved to a FC (outputname) in the workspace.
#Modules
import arcpy
from arcpy import env

#Environment
env.workspace = "WORKSPACE_PATH"

###Function###
def erase(TargetFC, EraseFC, outputname):
    arcpy.Union_analysis([TargetFC, EraseFC], outputname)
    arcpy.MakeFeatureLayer_management(outputname, "outputnamelayer")
    arcpy.SelectLayerByLocation_management("outputnamelayer", "WITHIN", EraseFC)
    arcpy.DeleteFeatures_management("outputnamelayer")

#Variables
TargetFC = "TARGET_FC"
EraseFC = "ERASE_FC"
outputname = "OUTPUT_NAME"

#Script
erase(TargetFC, EraseFC, outputname)
