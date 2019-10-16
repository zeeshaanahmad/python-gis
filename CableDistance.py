# -*- coding: utf-8 -*-# ---------------------------------------------------------------------------# test.py# Created on: 2016-08-23 20:12:59.00000#   (generated by ArcGIS/ModelBuilder)# Usage: test <Input_Excel_file_of_the_points_on_cable> <Cables_shapefile> <Excel_file_sheet_name_that_containts_data> <Plots_shapefile> <Output_location_for_Excel_file> <Cable_unique_ID_column_name> <Output_directory_for_resulting_shapefile> # Description: # ---------------------------------------------------------------------------# Import arcpy moduleimport arcpyimport os, shutil# Script arguments# Param 1Input_Excel_file_of_the_points_on_cable = arcpy.GetParameterAsText(0)if Input_Excel_file_of_the_points_on_cable == '#' or not Input_Excel_file_of_the_points_on_cable:    Input_Excel_file_of_the_points_on_cable = "D:\\ArcmapWorkspace\\cables\\events.xlsx" # provide a default value if unspecified# Param 2Cables_shapefile = arcpy.GetParameterAsText(1)if Cables_shapefile == '#' or not Cables_shapefile:    Cables_shapefile = "D:\\ArcmapWorkspace\\cables\\XrefKLMSusteren_Kabelsleidingen_v001\\Xref-KLM-Susteren_Kabelsleidingen_v001_Elektriciteit_Laagspanning.shp" # provide a default value if unspecified# Param 3Excel_file_sheet_name_that_containts_data = arcpy.GetParameterAsText(2)if Excel_file_sheet_name_that_containts_data == '#' or not Excel_file_sheet_name_that_containts_data:    Excel_file_sheet_name_that_containts_data = "Sheet1" # provide a default value if unspecified# Param 4Plots_shapefile = arcpy.GetParameterAsText(3)if Plots_shapefile == '#' or not Plots_shapefile:    Plots_shapefile = "D:\\ArcmapWorkspace\\cables\\FrankvanNeer01_87AB4CFDC480682F40693F31A5773FFD\\kkadmin_2shp.shp\\Percelen_laag_poly.shp" # provide a default value if unspecified# Param 5Output_location_for_Excel_file = arcpy.GetParameterAsText(4)if Output_location_for_Excel_file == '#' or not Output_location_for_Excel_file:    Output_location_for_Excel_file = "D:\\ArcmapWorkspace\\cables\\out\\output.xls" # provide a default value if unspecifiedtry:    os.remove(Output_location_for_Excel_file)except OSError:    pass# Param 6Cable_unique_ID_column_name = arcpy.GetParameterAsText(5)if Cable_unique_ID_column_name == '#' or not Cable_unique_ID_column_name:    Cable_unique_ID_column_name = "[FID]" # provide a default value if unspecified# Param 7Output_directory_for_resulting_shapefile = arcpy.GetParameterAsText(6)if Output_directory_for_resulting_shapefile == '#' or not Output_directory_for_resulting_shapefile:    Output_directory_for_resulting_shapefile = "D:\\ArcmapWorkspace\\cables\\out" # provide a default value if unspecifiedfolder = Output_directory_for_resulting_shapefilearcpy.AddMessage("Emptying the output folder")print "Emptying the output folder"for the_file in os.listdir(folder):    file_path = os.path.join(folder, the_file)    try:                if os.path.isfile(file_path):                        os.unlink(file_path)        elif os.path.isdir(file_path): shutil.rmtree(file_path)    except Exception as e:        print(e)##Input_Excel_file_of_the_points_on_cable = 'D:\\ArcmapWorkspace\\cables\\events.xlsx'####Cables_shapefile = 'D:\\ArcmapWorkspace\\cables\\XrefKLMSusteren_Kabelsleidingen_v001\\Xref-KLM-Susteren_Kabelsleidingen_v001_Elektriciteit_Laagspanning.shp'####Excel_file_sheet_name_that_containts_data = arcpy.GetParameterAsText(2)####if Excel_file_sheet_name_that_containts_data == '#' or not Excel_file_sheet_name_that_containts_data:####    Excel_file_sheet_name_that_containts_data = "Sheet1" # provide a default value if unspecified####Plots_shapefile = 'D:\\ArcmapWorkspace\\cables\\FrankvanNeer01_87AB4CFDC480682F40693F31A5773FFD\\kkadmin_2shp.shp\\Percelen_laag_poly.shp' # enter the path to plots shwpefile. ########Output_location_for_Excel_file = 'D:\\ArcmapWorkspace\\cables\\out\\output.xls'##try:##    os.remove(Output_location_for_Excel_file)##except OSError:##    pass########Cable_unique_ID_column_name = arcpy.GetParameterAsText(5)####if Cable_unique_ID_column_name == '#' or not Cable_unique_ID_column_name:####    Cable_unique_ID_column_name = "[FID]" # provide a default value if unspecified########Output_directory_for_resulting_shapefile = 'D:\\ArcmapWorkspace\\cables\\out'# Local variables:Xref_KLM_Susteren_Kabelsleidingen_v001_Elektriciteit_Laagspanning_shp__2_ = Cables_shapefileXref_KLM_Susteren_Kabelsleidingen_v001_Elektriciteit_Laagspanning_shp__4_ = Xref_KLM_Susteren_Kabelsleidingen_v001_Elektriciteit_Laagspanning_shp__2_XrefKLMSusteren_Kabelsleidin1 = "in_memory\\XrefKLMSusteren_Kabelsleidin1"table = "in_memory\\event_table"events_lyr = "in_memory\\events_lyr"Percelen_laag_poly_Intersect = "in_memory\\events_lyr_Intersect"events_lyr_Intersect = Percelen_laag_poly_IntersectDerived_Folder = Output_directory_for_resulting_shapefile# Set Geoprocessing environments# arcpy.env.scratchWorkspace = "c:\\program files (x86)\\arcgis\\desktop10.4\\ArcToolbox\\Toolboxes\\Default.gdb"try:    # Process: Add Field    arcpy.AddField_management(Cables_shapefile, "cabid", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")    print "Field added"    arcpy.AddMessage("Field added")    # Process: Calculate Field    arcpy.CalculateField_management(Xref_KLM_Susteren_Kabelsleidingen_v001_Elektriciteit_Laagspanning_shp__2_, "cabid", Cable_unique_ID_column_name, "VB", "")    print "Unique keys for cables created"        arcpy.AddMessage("Unique keys for cables created")    # Process: Create Routes    arcpy.AddMessage("Making cables data network enabled. Generating m vlues for Linear Processing")    print "Making cables data network enabled. Generating m vlues for Linear Processing"    arcpy.CreateRoutes_lr(Xref_KLM_Susteren_Kabelsleidingen_v001_Elektriciteit_Laagspanning_shp__4_, "cabid", XrefKLMSusteren_Kabelsleidin1, "LENGTH", "", "", "UPPER_LEFT", "1", "0", "IGNORE", "INDEX")    # Process: Excel To Table    arcpy.AddMessage("Converting Excel file to ArcGIS table")    print "Converting Excel file to ArcGIS table"    arcpy.ExcelToTable_conversion(Input_Excel_file_of_the_points_on_cable, table, Excel_file_sheet_name_that_containts_data)    # Process: Make Route Event Layer    arcpy.AddMessage("Extracting line segment between from and to points")    print "Extracting line segment between from and to points"    arcpy.MakeRouteEventLayer_lr(XrefKLMSusteren_Kabelsleidin1, "cabid", table, "routeid LINE from_ to", events_lyr, "", "NO_ERROR_FIELD", "NO_ANGLE_FIELD", "NORMAL", "ANGLE", "LEFT", "POINT")    # Process: Intersect    arcpy.AddMessage("Extracting segments in each polygon to measure length")    print "Extracting segments in each polygon to measure length"    arcpy.Intersect_analysis([events_lyr,Plots_shapefile], Percelen_laag_poly_Intersect, "ALL", "", "INPUT")    # Process: Add Geometry Attributes    arcpy.AddMessage("Measuring Length for each segment")    print "Measuring Length for each segment"    arcpy.AddGeometryAttributes_management(Percelen_laag_poly_Intersect, "LENGTH", "METERS", "", "")    # Process: Table To Excel    arcpy.AddMessage("Generating output excel file")    print "Generating output excel file"    arcpy.TableToExcel_conversion(events_lyr_Intersect, Output_location_for_Excel_file, "ALIAS", "CODE")    # Process: Feature Class To Shapefile (multiple)    arcpy.AddMessage("Generating output shapefile")    print "Generating output shapefile"    arcpy.FeatureClassToShapefile_conversion("'in_memory\\events_lyr_Intersect'", Output_directory_for_resulting_shapefile)    print "Tool completed. Please find the resulting excel file at " + Output_location_for_Excel_file + " shapefile at " + Output_directory_for_resulting_shapefile + "\\" + events_lyr_Intersect + ".shp"    arcpy.AddMessage("Tool completed. Please find the resulting excel file at " + Output_location_for_Excel_file + " shapefile at " + Output_directory_for_resulting_shapefile + "\\" + events_lyr_Intersect + ".shp")except Exception as e:    print e.message        # If using this code within a script tool, AddError can be used to return messages     #   back to a script tool.  If not, AddError will have no effect.    arcpy.AddError(e.message)