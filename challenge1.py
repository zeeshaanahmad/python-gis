import arcpy
from arcpy import env
from arcpy.sa import *

# Setting up workspace
env.workspace = "D://YOUR/PATH"

# Create a geodatabase to store output
out_folder_path = "D://YOUR/OUTPUT/DIR"
outgdb_name = "outgdb.gdb"
arcpy.CreateFileGDB_management(out_folder_path, outgdb_name)

# Calculating slope of Elevation raster
elev_slope = Slope("Elevation")

# Save the slope to geodatabase
elev_slope.save(out_folder_path + "/" +  outgdb_name + "/" + "elevation_slope")

# Calculating slope greater than 5
elev_slope_gt_5 = elev_slope > 5

# Calculating slope lesser than 20
elev_slope_lt_20 = elev_slope < 20

# Calculating slope between 5 and 20 using Raster Algenbra
mod_slope = elev_slope_gt_5 & elev_slope_lt_20

# Save the moderate slope to geodatabase
mod_slop.save(out_folder_path + "/" +  outgdb_name + "/" + "moderate_slope")

# Calculating aspect of Elevation raster
elev_aspect = Aspect("Elevation")

# Save the elevation aspect to geodatabase
elev_aspect.save(out_folder_path + "/" +  outgdb_name + "/" + "elevation_aspect")

# Calculating elevation aspect between 150 and 270 degree using Raster Algebra
# Just to show it can be done in one line as well
s_elev = (elev_aspect > 150) & (elev_aspect < 270)

# Save the southerly aspect to geodatabase
s_elev.save(out_folder_path + "/" +  outgdb_name + "/" + "southerly_aspect")

# Setting up classification filter for 41, 42 and 43 values
myremap = RemapValue([[41,1], [42,1], [43,1]])

# Reclassifying the landcover using myremap classification filter
outreclass = Reclassify("landcover.tif", "VALUE", myremap, "NODATA")

# Save the reclassified landcover to geodatabase
outreclass.save(out_folder_path + "/" +  outgdb_name + "/" + "reclassified_landcover")

# Save the southerly aspect to geodatabase
outreclass.save(out_folder_path + "/" +  outgdb_name + "/" + "reclassified_landcover")

# Creating the final output for areas matching the given criteria
# • Moderate slope—between 5 and 20 degrees
# • Southerly aspect—between 150 and 270 degrees 
# • Forested—land cover types of 41, 42, or 43
final_output = mod_slope & s_elev & outreclass

# Saving final output to a Geodatabase
final_output.save(out_folder_path + "/" +  outgdb_name + "/" + "final_areas")
