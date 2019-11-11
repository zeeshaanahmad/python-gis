import arcpy
import gc

# Setting up the working directory. You should change the path to your working directory
arcpy.env.workspace = "C:/YOUR/WORKING/DIRECTORY"

# Creating feature layers from the shapefiles
arcpy.MakeFeatureLayer_management("CensusTracts2000.shp", "CensusTracts2000")
arcpy.MakeFeatureLayer_management("SAPDCrimes_Jan05.shp", "SAPDCrimes_Jan05")
arcpy.MakeFeatureLayer_management("MajorHighways.shp", "MajorHighways")

# Selecting the census tracts with population over 5000
lyr_over5k_pop = arcpy.SelectLayerByAttribute_management("CensusTracts2000", "NEW_SELECTION", "POPULATION > 5000")

# Clipping the crime incidents using the selected census tracts with population over 5000
clipped_feats = arcpy.Clip_analysis("SAPDCrimes_Jan05", lyr_over5k_pop)

# Creating a buffer of 1 mile around the major highways
lyr_1_mile_hwy_buff = arcpy.Buffer_analysis("MajorHighways", "buffer_lyr", "1 Miles")

# Erasing the crime incidents occured with 1 mile of the major highways and storing the results in 
# final_output.shp in the same working directory
final_output = arcpy.Erase_analysis(clipped_feats, lyr_1_mile_hwy_buff, "final_output.shp")

# Below lines are for deleting the intermediate layers created. 
# You may uncomment them to delete them if you want.

# arcpy.Delete_management("CensusTracts2000")
# arcpy.Delete_management("SAPDCrimes_Jan05")
# arcpy.Delete_management("MajorHighways")

# Just being responsible by explicit garbage collection
gc.collect()