#Modules
import arcpy
from arcpy import env

#Environment
env.workspace = "G:\Users\Jordan\Projects\FH_2015Submission\Submission.gdb\Submission"

###Function###
def erase(TargetFC, EraseFC, outputname):
    arcpy.Union_analysis([TargetFC, EraseFC], outputname)
    arcpy.MakeFeatureLayer_management(outputname, "outputnamelayer")
    arcpy.SelectLayerByLocation_management("outputnamelayer", "WITHIN", EraseFC)
    arcpy.DeleteFeatures_management("outputnamelayer")

#Variables
TargetFC = "G:\Users\Jordan\Projects\FH_2015Submission\Submission.gdb\Submission\SurfaceSoilErase_v01_20151216_JV"
EraseFC = "G:\Users\Jordan\Projects\FH_2015Submission\Submission.gdb\Submission\OilSandsLandCover_RevG_Reclaimed_v01_20151216_JV"
outputname = "SurfaceSoil_DisturbancePlacement_Erase_v01_20151216_JV"

#Script
erase(TargetFC, EraseFC, outputname)
