# Import system modules
import arcpy

# Setting up the working directory. You should change the path to your working directory
arcpy.env.workspace = "C:/YOUR/WORKING/DIRECTORY"

# Performing the Cluster and Outlier Analysis
arcpy.ClustersOutliers_stats("SJ_output.shp", "Join_Count", "SJCopied.shp", "INVERSE_DISTANCE", "EUCLIDEAN_DISTANCE", "NONE")
