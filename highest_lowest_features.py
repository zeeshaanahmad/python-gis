import arcpy
inPointFeatures = "ZeleznicniStanice"
inRaster = "dem"
output_path = "C:\\"

arcpy.CheckOutExtension("3D")

# Adds a column with Z value reading from dem raster
arcpy.AddSurfaceInformation_3d(inPointFeatures, inRaster, "Z")

# Find FID of the row with maximum Z value
fidMax = arcpy.SearchCursor(inPointFeatures, "", "", "", "Z" + " D").next().getValue("FID")

# Find FID of the row with maximum Z value
fidMin = arcpy.SearchCursor(inPointFeatures, "", "", "", "Z" + " A").next().getValue("FID")

# Selects the heighest and lowest stations
arcpy.SelectLayerByAttribute_management(inPointFeatures, "NEW_SELECTION", "FID IN ({}, {})".format(fidMin, fidMax))

# Exports the selected features to an output shapefile in C:\output.shp You may change this path at the top
arcpy.FeatureClassToFeatureClass_conversion(inPointFeatures, output_path, "output.shp")

# Prints the heighest and lowest train stations on console
cursor = arcpy.SearchCursor(inPointFeatures)
for row in cursor:
    if row.getValue("FID") == fidMax:
        print("Heighest train station is: {} at height {}".format(row.getValue("NAZEV_ASCI"), row.getValue("Z")))
    if row.getValue("FID") == fidMin:
        print("Lowest train station is: {} at height {}".format(row.getValue("NAZEV_ASCI"), row.getValue("Z")))

arcpy.CheckInExtension("3D")