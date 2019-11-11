import arcpy
from arcpy import env
from arcpy.sa import *

# Setting up workspace
env.workspace = "D://YOUR/PATH"

# Calculating aspect for DEM
dem_aspect = Aspect("dem")

# Calculating hillshade with given parameters for DEM
dem_hillshade = Hillshade("dem", 260, 60, "SHADOWS", 0.3048)

# Using raster algebra to add aspect and hillshade
raster_add = dem_aspect + dem_hillshade

# Saving in the local directory
# Just to demonstrate that ESRI GRID cannot have a name longer than certain number of characters
# So to handle that, this output is being stored in tif format
raster_add.save("final_aspect_hillshade.tif")

# It could be saved as ESRI GRID if the name was shorter like below - without an extention
raster_add.save("fin_out")

# In order to save to a file geodatabase
# Create a geodatabase to store output
out_folder_path = "D://YOUR/OUTPUT/DIR"
outgdb_name = "outgdb.gdb"
arcpy.CreateFileGDB_management(out_folder_path, outgdb_name)

raster_add.save(out_folder_path + "/" + outgdb_name + "/" + "fin_out")