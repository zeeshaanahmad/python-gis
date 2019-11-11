import arcpy
from arcpy import env
env.workspace = "D:/PATH/TO/WORKSPACE/DIRECTORY"

# Create a geodatabase to store rasters
out_folder_path = "D://YOUR/OUTPUT/DIR"
outgdb_name = "outgdb.gdb"
arcpy.CreateFileGDB_management(out_folder_path, outgdb_name)

# Lists all the rasters in your workspace directory
rasters_list = arcpy.ListRasters()

# Imports all the rasters to the geodatabase created above
arcpy.RasterToGeodatabase_conversion(";".join(rasters_list), out_folder_path + "/" + outgdb_name)