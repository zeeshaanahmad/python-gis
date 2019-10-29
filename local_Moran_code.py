# Import system modules
import arcpy

# Set property to overwrite outputs if they already exist
#arcpy.env.overwriteOutput = True

# Local variables...
arcpy.env.workspace = r"D:\UNMArcClasses2019\GEOG_527\Lab9_Python\Lab9_VectorOp"
#try:
    # Set the current workspace 
    #  (to avoid having to specify the full path to the feature classes each time)
 #   arcpy.env.workspace = workspace
  #  cf = arcpy.CopyFeatures_management("SJ_output.shp", "SJCopied.shp")
    
arcpy.ClustersOutliers_stats("SJ_output.shp", "Join_Count", "SJCopied.shp",
                             "GET_SPATIAL_WEIGHTS_FROM_FILE","EUCLIDEAN_DISTANCE", 
                             "NONE","#", "euclidean6Neighs.swm","NO_FDR")
