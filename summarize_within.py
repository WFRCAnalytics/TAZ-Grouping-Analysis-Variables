import os

gdb = 'E:\\Tasks\\MB-Neighborhood-Analysis\\Outputs\\results.gdb'
arterial = ''' CARTOCODE IN ('8 - 8 Major Local Roads, Paved', '2', '3', '4', '5') '''
local = ''' CARTOCODE IN ('8 - 8 Major Local Roads, Paved', '11', '10', '9', '8') '''
collector =  ''' CARTOCODE IN ('8 - 8 Major Local Roads, Paved', '7') '''
roads_layer = arcpy.MakeFeatureLayer_management("Roads", 'roads_lyr')

#=========================
# inside (100% of length)
#=========================

# arterial
arcpy.SelectLayerByAttribute_management(roads_layer, 'NEW_SELECTION', arterial)
inside_sw_arterial = arcpy.analysis.SummarizeWithin('_03_nbhd_erase', roads_layer, os.path.join(gdb, '_04_inside_sw_arterial'), "KEEP_ALL", "Miles Sum", "ADD_SHAPE_SUM", 'MILES')

# local
arcpy.SelectLayerByAttribute_management(roads_layer, 'NEW_SELECTION', local)
inside_sw_local = arcpy.analysis.SummarizeWithin('_03_nbhd_erase', roads_layer, os.path.join(gdb, '_04_inside_sw_local'), "KEEP_ALL", "Miles Sum", "ADD_SHAPE_SUM", 'MILES')

# collector
arcpy.SelectLayerByAttribute_management(roads_layer, 'NEW_SELECTION', collector)
inside_sw_collector = arcpy.analysis.SummarizeWithin('_03_nbhd_erase', roads_layer, os.path.join(gdb, '_04_inside_sw_collector'), "KEEP_ALL", "Miles Sum", "ADD_SHAPE_SUM", 'MILES')

# all
arcpy.SelectLayerByAttribute_management(roads_layer, 'CLEAR_SELECTION')
inside_sw_all = arcpy.analysis.SummarizeWithin('_03_nbhd_erase', roads_layer, os.path.join(gdb, '_04_inside_sw_all'), "KEEP_ALL", "Miles Sum", "ADD_SHAPE_SUM", 'MILES')

#===========================
# boundary (50% of length)
#===========================

# arterial
arcpy.SelectLayerByAttribute_management(roads_layer, 'NEW_SELECTION', arterial)
boundary_sw_arterial = arcpy.analysis.SummarizeWithin('_02_nbhd_bnd_buff', roads_layer, os.path.join(gdb, '_05_boundary_sw_arterial'), "KEEP_ALL", "Miles Sum", "ADD_SHAPE_SUM", 'MILES')
# local
arcpy.SelectLayerByAttribute_management(roads_layer, 'NEW_SELECTION', local)
boundary_sw_local = arcpy.analysis.SummarizeWithin('_02_nbhd_bnd_buff', roads_layer, os.path.join(gdb, '_05_boundary_sw_local'), "KEEP_ALL", "Miles Sum", "ADD_SHAPE_SUM", 'MILES')
# collector
arcpy.SelectLayerByAttribute_management(roads_layer, 'NEW_SELECTION', collector)
boundary_sw_collector = arcpy.analysis.SummarizeWithin('_02_nbhd_bnd_buff', roads_layer, os.path.join(gdb, '_05_boundary_sw_collector'), "KEEP_ALL", "Miles Sum", "ADD_SHAPE_SUM", 'MILES')

# all
arcpy.SelectLayerByAttribute_management(roads_layer, 'CLEAR_SELECTION')
boundary_sw_all = arcpy.analysis.SummarizeWithin('_02_nbhd_bnd_buff', roads_layer, os.path.join(gdb, '_05_boundary_sw_all'), "KEEP_ALL", "Miles Sum", "ADD_SHAPE_SUM", 'MILES')