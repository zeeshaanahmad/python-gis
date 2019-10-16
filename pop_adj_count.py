import arcpy
import gc

# Update your workspace directory address
arcpy.env.workspace = "D:/UPDATE/THIS/PATH"

# Make feature layer from shapefile
arcpy.MakeFeatureLayer_management("HaysBG00.shp","BlockGroupLyr" )

# Create a search cursor
sc = arcpy.SearchCursor("BlockGroupLyr")

# Creates a file named result.txt in the workspace directory
with open('C:/UPDATE/THIS/PATH/result.txt','w') as f:

    # Writes header
    f.write('FID,COUNT,TOTALPOP\n')

    # Iterating over the rows and select each one
    for block in sc:

        # Getting the FID of the ith row
        id_bg = block.getValue("FID")

        # Selecting the row
        sel_block = arcpy.SelectLayerByAttribute_management("BlockGroupLyr", \
            "NEW_SELECTION", "FID = {}".format(id_bg))
        
        # Selecting the adjacent polygons, I have used INTERSECT relationship,
        # BOUNDARY_TOUCHES could also be used. You may try changing that to see
        # if there's any difference. 
        adj_blocks = arcpy.SelectLayerByLocation_management(sel_block, \
            "INTERSECT", "BlockGroupLyr", 0, "NEW_SELECTION")

        # Counting the adjacent blocks selected above
        count_adj_blocks = arcpy.GetCount_management(adj_blocks)

        adj_l = []

        # Iterating over the selected adjacent blocks to count population sum
        adj_blk_sc = arcpy.SearchCursor(adj_blocks)
        for adj_blk in adj_blk_sc:
            pop = int(adj_blk.getValue("POP2000"))
            adj_l.append(pop)
        
        # Above I just kept a running list of all the values found for 
        # selected adjacent blocks. Below using the Python's built-in sum method
        # it is getting the sum of population
        sum_pop = sum(adj_l)

        # Finally comma separated output of FID,COUNT,TOTALPOP
        output = '{0},{1},{2}\n'.format(id_bg, count_adj_blocks, sum_pop)
        
        print(output)  # Printing to console
        f.write(output)  # Writing to file

# Deletes the temporary layer
arcpy.Delete_management("BlockGroupLyr")

# Garbage collection
gc.collect()
