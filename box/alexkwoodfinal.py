# {"name": "Alexkwoods script", "author": "Poseidon", "version": (1, 0), "blender": (2, 92, 0)}

import bpy


#Remove all objects
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()
for col in bpy.data.collections:
    bpy.data.collections.remove(col)

for block in bpy.data.materials:
    bpy.data.materials.remove(block)
for block in bpy.data.images:
    bpy.data.images.remove(block)

col = bpy.data.collections.new('Collection')
bpy.context.scene.collection.children.link(col)
layer_collection = bpy.context.view_layer.layer_collection.children[col.name]
bpy.context.view_layer.active_layer_collection = layer_collection

bpy.context.scene.frame_start = 0
bpy.context.scene.frame_end = 250


#######LOGO PART####################
def addMaterialImg(name):       
    material = bpy.data.materials.new(name= name)
    material.use_nodes = True
    #create a reference to the material output
    material_output = material.node_tree.nodes.get('Material Output')
    Principled_BSDF = material.node_tree.nodes.get('Principled BSDF')

    bpy.ops.image.open(filepath='C:\\Users\\yassine\\Pictures\\bonnet.png') #edit this
    myImg = bpy.data.images['bonnet.png']                                   #and this

    texImage_node = material.node_tree.nodes.new('ShaderNodeTexImage')
    texImage_node.image = myImg
    #set location of node
    material_output.location = (400, 20)
    Principled_BSDF.location = (0, 0)
    texImage_node.location = (-400, -500)


    material.node_tree.links.new(texImage_node.outputs[0], Principled_BSDF.inputs[0])
    material.node_tree.links.new(texImage_node.outputs[1], Principled_BSDF.inputs[19])

    mat = bpy.data.materials.get(name)
    mat.blend_method = 'CLIP'
    return mat

def joinPlaneCube(Plane_obj, box_obj, axis, sign):
    Plane_obj.location = box_obj.location
    if (sign == '+'):
        Plane_obj.location[axis] += (box_obj.dimensions[axis]/2)+0.0003
        Plane_obj.location[1] -= 0.044 #
    elif (sign == '-'):
        Plane_obj.location[axis] -= (box_obj.dimensions[axis]/2 )+0.0003 
        Plane_obj.location[1] += 0.044 #
        
    Plane_obj.rotation_euler = box_obj.rotation_euler
    if(axis == 0):
        Plane_obj.rotation_euler[0]=1.5708
        if (sign == '+'):
            Plane_obj.rotation_euler[2]=1.5708
        elif (sign == '-'):
            Plane_obj.rotation_euler[2]=-1.5708
            
    elif(axis == 1):
        Plane_obj.rotation_euler[0]=1.5708
        if (sign == '+'):
            Plane_obj.rotation_euler[2]=3.14159
    
    elif(axis == 2) and (sign == '-'):
        Plane_obj.rotation_euler[1]=3.14159

def addPlaneWithMaterial(name, material, obj):
    bpy.ops.mesh.primitive_plane_add(size=0.0175, location= obj.location, rotation= obj.rotation_euler) #
    bpy.context.active_object.active_material = material
    bpy.context.active_object.name= name
    plane = bpy.context.scene.collection.children['Collection'].objects[name]
    return plane


mat_A = addMaterialImg('Logo')

##############################

def makeTextObj(text, box_obj):
    bpy.ops.object.select_all(action='DESELECT')

    
    font_curve = bpy.data.curves.new(type="FONT", name="FC_alpha")
    font_curve.body = text
    font_obj = bpy.data.objects.new(name=text, object_data=font_curve)
    bpy.context.scene.collection.objects.link(font_obj)

    bpy.data.objects[text].select_set(True)
    bpy.context.view_layer.objects.active = bpy.data.objects[text]
    bpy.context.object.data.extrude = 0.0002
    bpy.ops.object.origin_set(type='GEOMETRY_ORIGIN', center='MEDIAN')
    
    
    bpy.ops.object.convert(target='MESH', keep_original=False, angle=1.22173, thickness=5, seams=False, faces=True, offset=0.01)
    bpy.data.objects[text].scale[0] = box_obj.dimensions[0]/4
    bpy.data.objects[text].scale[1] = box_obj.dimensions[1]/4
    val = bpy.data.objects[text]
    return val

def makeTextObjBig(text, box_obj):
    bpy.ops.object.select_all(action='DESELECT')

    
    font_curve = bpy.data.curves.new(type="FONT", name="FC_alpha")
    font_curve.body = text
    font_obj = bpy.data.objects.new(name=text, object_data=font_curve)
    bpy.context.scene.collection.objects.link(font_obj)

    bpy.data.objects[text].select_set(True)
    bpy.context.view_layer.objects.active = bpy.data.objects[text]
    bpy.context.object.data.extrude = 0.0002
    bpy.ops.object.origin_set(type='GEOMETRY_ORIGIN', center='MEDIAN')
    
    
    bpy.ops.object.convert(target='MESH', keep_original=False, angle=1.22173, thickness=5, seams=False, faces=True, offset=0.01)
    bpy.data.objects[text].scale[0] = box_obj.dimensions[0]/6
    bpy.data.objects[text].scale[1] = box_obj.dimensions[1]/9
    val = bpy.data.objects[text]
    return val

def makeTextObjBiggest(text, box_obj):
    bpy.ops.object.select_all(action='DESELECT')

    
    font_curve = bpy.data.curves.new(type="FONT", name="FC_alpha")
    font_curve.body = text
    font_obj = bpy.data.objects.new(name=text, object_data=font_curve)
    bpy.context.scene.collection.objects.link(font_obj)

    bpy.data.objects[text].select_set(True)
    bpy.context.view_layer.objects.active = bpy.data.objects[text]
    bpy.context.object.data.extrude = 0.0002
    bpy.ops.object.origin_set(type='GEOMETRY_ORIGIN', center='MEDIAN')
    
    
    bpy.ops.object.convert(target='MESH', keep_original=False, angle=1.22173, thickness=5, seams=False, faces=True, offset=0.01)
    bpy.data.objects[text].scale[0] = box_obj.dimensions[0]/16
    bpy.data.objects[text].scale[1] = box_obj.dimensions[1]/9
    val = bpy.data.objects[text]
    return val

def joinTextCube(text_obj, box_obj, axis, sign):

    text_obj.location = box_obj.location
    if (sign == '+'):
        text_obj.location[axis] += box_obj.dimensions[axis]/2
    elif (sign == '-'):
        text_obj.location[axis] -= box_obj.dimensions[axis]/2    
        
    text_obj.rotation_euler = box_obj.rotation_euler
    if(axis == 0):
        text_obj.rotation_euler[0]=1.5708
        if (sign == '+'):
            text_obj.rotation_euler[2]=1.5708
        elif (sign == '-'):
            text_obj.rotation_euler[2]=-1.5708
            
    elif(axis == 1):
        text_obj.rotation_euler[0]=1.5708
        if (sign == '+'):
            text_obj.rotation_euler[2]=3.14159
    
    elif(axis == 2) and (sign == '-'):
        text_obj.rotation_euler[1]=3.14159

def merge(box_obj, text_obj):
    bpy.ops.object.select_all(action='DESELECT')
    bpy.context.view_layer.objects.active = box_obj
    box_obj.select_set(True)
    text_obj.select_set(True)
    bpy.ops.object.join()

def addMaterial(name, color, val1, val2):
	material = bpy.data.materials.new(name= name)
	material.use_nodes = True
	#create a reference to the material output
	material_output = material.node_tree.nodes.get('Material Output')
	Principled_BSDF = material.node_tree.nodes.get('Principled BSDF')

	normalMap_node = material.node_tree.nodes.new('ShaderNodeNormalMap')
	#set location of node
	material_output.location = (400, 20)
	Principled_BSDF.location = (0, 0)
	normalMap_node.location = (-400, -500)
	material.node_tree.links.new(normalMap_node.outputs[0], Principled_BSDF.inputs[20])

	material.node_tree.nodes["Principled BSDF"].inputs[0].default_value = color
	material.node_tree.nodes["Principled BSDF"].inputs[5].default_value = val1
	material.node_tree.nodes["Principled BSDF"].inputs[7].default_value = val2
	mat = bpy.data.materials.get(name)
	return mat

def addBoxWithMaterial(name, material, location, rotation, scale):
    if (2,93,0) < bpy.app.version:
        bpy.ops.mesh.primitive_cube_add(size=1, location= location, rotation= rotation, scale= scale)
    else:
        bpy.ops.mesh.primitive_cube_add(size=2, location= location, rotation= rotation, scale= scale)
    bpy.context.active_object.active_material = material
    bpy.context.active_object.name= name
    box = bpy.context.scene.collection.children['Collection'].objects[name]
    return box

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

material_white = addMaterial("White", (1, 1, 1, 1), 1.000, 0.859)
material_top = addMaterial("Top", (0.592, 0.831, 0.776, 1), 1.000, 0.859)
material_L6 = addMaterial("L6", (0.329, 0.435, 0.576, 1), 1.000, 0.859)
material_L5 = addMaterial("L5", (0.189, 0.789, 1, 1), 1.000, 0.859)
material_bottom = addMaterial("Bottom", (0.579, 0.919, 1, 1), 1.000, 0.859)

####################################
####################################
####################################
####################################
####################################

#####bottom#####
bot1 = addBoxWithMaterial('bot1', material_bottom, (-0.041742, -0.006646, 0.229326), (-0.000003, 0, 0), (0.035, 0.11, 0.02))
#start Test
val = makeTextObjBig('Records', bot1)
val.active_material = material_white
joinTextCube(val, bot1, 1, '-')
merge(bot1, val)
#end Test
#start Test
val = makeTextObjBig('Records', bot1)
val.active_material = material_white
joinTextCube(val, bot1, 1, '+')
merge(bot1, val)
#end Test
#start Test
val = makeTextObjBig('Aliasing', bot1)
val.active_material = material_white
joinTextCube(val, bot1, 0, '-')
merge(bot1, val)
#end Test
#this get's it done                                                                 xxxxx
plane_A = addPlaneWithMaterial('logo_A', mat_A, bot1)
joinPlaneCube(plane_A, bot1, 0, '-')
merge(bot1, plane_A)


bot1.keyframe_insert(data_path="location", frame=1)
bot1.location = (-0.041742, -0.006646, 0)
bot1.keyframe_insert(data_path="location", frame=47)
#**********#

#**********#
bot2 = addBoxWithMaterial('bot2', material_bottom, (-0.002744, -0.006646, 0.249497), (-0.000003, 0, 0), (0.035, 0.11, 0.02))
#start Test
val = makeTextObjBig('Operations', bot2)
val.active_material = material_white
joinTextCube(val, bot2, 1, '-')
merge(bot2, val)
#end Test
#start Test
val = makeTextObjBig('Operations', bot2)
val.active_material = material_white
joinTextCube(val, bot2, 1, '+')
merge(bot2, val)
#end Test
bot2.keyframe_insert(data_path="location", frame=3)
bot2.location = (-0.002744, -0.006646, 0)
bot2.keyframe_insert(data_path="location", frame=53)
#**********#

#**********#
bot3 = addBoxWithMaterial('bot3', material_bottom, (0.036255, -0.006646, 0.249497), (-0.000003, 0, 0), (0.035, 0.11, 0.02))
#start Test
val = makeTextObjBig('API', bot3)
val.active_material = material_white
joinTextCube(val, bot3, 1, '-')
merge(bot3, val)
#end Test
#start Test
val = makeTextObjBig('API', bot3)
val.active_material = material_white
joinTextCube(val, bot3, 1, '+')
merge(bot3, val)
#end Test
#start Test
val = makeTextObjBig('Aliasing', bot3)
val.active_material = material_white
joinTextCube(val, bot3, 0, '+')
merge(bot3, val)
#end Test
#this get's it done                                                                 xxxxx
plane_A = addPlaneWithMaterial('logo_A', mat_A, bot3)
joinPlaneCube(plane_A, bot3, 0, '+')
merge(bot3, plane_A)
bot3.keyframe_insert(data_path="location", frame=18)
bot3.location = (0.036255, -0.006646, 0)
bot3.keyframe_insert(data_path="location", frame=60)
#**********#


#####low mid#####
lowMid = addBoxWithMaterial('lowMid', material_L5, (-0.002744, -0.006646, 0.277979), (-0.000003, 0, 0), (0.113, 0.11, 0.02))
#start Test
val = makeTextObjBiggest('Routing Layer', lowMid)
val.active_material = material_white
joinTextCube(val, lowMid, 1, '-')
merge(lowMid, val)
#end Test
#start Test
val = makeTextObjBiggest('Routing Layer', lowMid)
val.active_material = material_white
joinTextCube(val, lowMid, 1, '+')
merge(lowMid, val)
#end Test
#start Test
val = makeTextObjBiggest('VGS Platform', lowMid)
val.active_material = material_white
joinTextCube(val, lowMid, 0, '+')
merge(lowMid, val)
#end Test
#start Test
val = makeTextObjBiggest('VGS Platform', lowMid)
val.active_material = material_white
joinTextCube(val, lowMid, 0, '-')
merge(lowMid, val)
#end Test
#this get's it done                                                                 xxxxx
plane_A = addPlaneWithMaterial('logo_A', mat_A, lowMid)
joinPlaneCube(plane_A, lowMid, 0, '+')
merge(lowMid, plane_A)

plane_A = addPlaneWithMaterial('logo_A', mat_A, lowMid)
joinPlaneCube(plane_A, lowMid, 0, '-')
merge(lowMid, plane_A)

lowMid.keyframe_insert(data_path="location", frame=26)
lowMid.location = (-0.002744, -0.006646, 0.028483)
lowMid.keyframe_insert(data_path="location", frame=72)
#**********#

#####high mid#####
#**********#
highMid1 = addBoxWithMaterial('highMid1', material_L6, (-0.041742, -0.006646, 0.305599), (-0.000003, 0, 0), (0.035, 0.11, 0.02))
#start Test
val = makeTextObjBig('PCI', highMid1)
val.active_material = material_white
joinTextCube(val, highMid1, 1, '-')
merge(highMid1, val)
#end Test
#start Test
val = makeTextObjBig('PCI', highMid1)
val.active_material = material_white
joinTextCube(val, highMid1, 1, '+')
merge(highMid1, val)
#end Test
#start Test
val = makeTextObjBig('Compliances', highMid1)
val.active_material = material_white
joinTextCube(val, highMid1, 0, '-')
merge(highMid1, val)
#end Test
#this get's it done                                                                 xxxxx
plane_A = addPlaneWithMaterial('logo_A', mat_A, highMid1)
joinPlaneCube(plane_A, highMid1, 0, '-')
merge(highMid1, plane_A)
highMid1.keyframe_insert(data_path="location", frame=45)
highMid1.location = (-0.041742, -0.006646, 0.056102)
highMid1.keyframe_insert(data_path="location", frame=82)
#**********#

#**********#
highMid2 = addBoxWithMaterial('highMid2', material_L6, (-0.002744, -0.006646, 0.305599), (-0.000003, 0, 0), (0.035, 0.11, 0.02))
#start Test
val = makeTextObjBig('GDPR', highMid2)
val.active_material = material_white
joinTextCube(val, highMid2, 1, '-')
merge(highMid2, val)
#end Test
#start Test
val = makeTextObjBig('GDPR', highMid2)
val.active_material = material_white
joinTextCube(val, highMid2, 1, '+')
merge(highMid2, val)
#end Test
highMid2.keyframe_insert(data_path="location", frame=54)
highMid2.location = (-0.002744, -0.006646, 0.056102)
highMid2.keyframe_insert(data_path="location", frame=89)
#**********#

#**********#
highMid3 = addBoxWithMaterial('highMid3', material_L6, (0.036255, -0.006646, 0.305599), (-0.000003, 0, 0), (0.035, 0.11, 0.02))
#start Test
val = makeTextObjBig('SOC2', highMid3)
val.active_material = material_white
joinTextCube(val, highMid3, 1, '-')
merge(highMid3, val)
#end Test
#start Test
val = makeTextObjBig('SOC2', highMid3)
val.active_material = material_white
joinTextCube(val, highMid3, 1, '+')
merge(highMid3, val)
#end Test
#start Test
val = makeTextObjBig('Compliances', highMid3)
val.active_material = material_white
joinTextCube(val, highMid3, 0, '+')
merge(highMid3, val)
#end Test
#this get's it done                                                                 xxxxx
plane_A = addPlaneWithMaterial('logo_A', mat_A, highMid3)
joinPlaneCube(plane_A, highMid3, 0, '+')
merge(highMid3, plane_A)
highMid3.keyframe_insert(data_path="location", frame=63)
highMid3.location = (0.036255, -0.006646, 0.056102)
highMid3.keyframe_insert(data_path="location", frame=95)
#**********#








#####top

#####left#####

#**********#
topRight3 = addBoxWithMaterial('topRight3', material_top, (-0.041742, -0.045646, 0.333565), (-0.000003, 0, 0), (0.035, 0.032, 0.02))
#start Test
val = makeTextObj('APP', topRight3)
val.active_material = material_white
joinTextCube(val, topRight3, 1, '-')
merge(topRight3, val)
#end Test
#start Test
val = makeTextObj('APP', topRight3)
val.active_material = material_white
joinTextCube(val, topRight3, 0, '-')
merge(topRight3, val)
#end Test
#start Test
val = makeTextObj('M', topRight3)
val.active_material = material_white
joinTextCube(val, topRight3, 2, '+')
merge(topRight3, val)
#end Test

topRight3.keyframe_insert(data_path="location", frame=139)
topRight3.location = (-0.041742, -0.045646, 0.084068)
topRight3.keyframe_insert(data_path="location", frame=180)
#**********#

#**********#
topRight2 = addBoxWithMaterial('topRight2', material_top, (-0.041742, -0.006646, 0.333565), (-0.000003, 0, 0), (0.035, 0.032, 0.02))
#start Test
val = makeTextObj('App', topRight2)
val.active_material = material_white
joinTextCube(val, topRight2, 0, '-')
merge(topRight2, val)
#end Test
#start Test
val = makeTextObj('S', topRight2)
val.active_material = material_white
joinTextCube(val, topRight2, 2, '+')
merge(topRight2, val)
#end Test
topRight2.keyframe_insert(data_path="location", frame=108)
topRight2.location = (-0.041742, -0.006646, 0.084068)
topRight2.keyframe_insert(data_path="location", frame=155)
#**********#

#**********#
topRight1 = addBoxWithMaterial('topRight1', material_top, (-0.041742, 0.032354, 0.333565), (-0.000003, 0, 0), (0.035, 0.032, 0.02))
#start Test
val = makeTextObj('App', topRight1)
val.active_material = material_white
joinTextCube(val, topRight1, 1, '+')
merge(topRight1, val)
#end Test
#start Test
val = makeTextObj('App', topRight1)
val.active_material = material_white
joinTextCube(val, topRight1, 0, '-')
merge(topRight1, val)
#end Test
#start Test
val = makeTextObj('IVR', topRight1)
val.active_material = material_white
joinTextCube(val, topRight1, 2, '+')
merge(topRight1, val)
#end Test
topRight1.keyframe_insert(data_path="location", frame=89)
topRight1.location = (-0.041742, 0.032354, 0.084068)
topRight1.keyframe_insert(data_path="location", frame=118)
#**********#


#####middle#####

#**********#
topMiddle3 = addBoxWithMaterial('topMiddle3', material_top, (-0.002744, -0.045646, 0.333565), (-0.000003, 0, 0), (0.035, 0.032, 0.02))
#start Test
val = makeTextObj('App', topMiddle3)
val.active_material = material_white
joinTextCube(val, topMiddle3, 1, '-')
merge(topMiddle3, val)
#end Test
#start Test
val = makeTextObj('C', topMiddle3)
val.active_material = material_white
joinTextCube(val, topMiddle3, 2, '+')
merge(topMiddle3, val)
#end Test
topMiddle3.keyframe_insert(data_path="location", frame=134)
topMiddle3.location = (-0.002744, -0.045646, 0.084068)
topMiddle3.keyframe_insert(data_path="location", frame=171)
#**********#

#**********#
topMiddle2 = addBoxWithMaterial('topMiddle2', material_top, (-0.002744, -0.006646, 0.333565), (-0.000003, 0, 0), (0.035, 0.032, 0.02))
#start Test
val = makeTextObj('API', topMiddle2)
val.active_material = material_white
joinTextCube(val, topMiddle2, 2, '+')
merge(topMiddle2, val)
#end Test
topMiddle2.keyframe_insert(data_path="location", frame=99)
topMiddle2.location = (-0.002744, -0.006646, 0.084068)
topMiddle2.keyframe_insert(data_path="location", frame=145)
#**********#

#**********#
topMiddle1 = addBoxWithMaterial('topMiddle1', material_top, (-0.002744, 0.032354, 0.333565), (-0.000003, 0, 0), (0.035, 0.032, 0.02))
#start Test
val = makeTextObj('App', topMiddle1)
val.active_material = material_white
joinTextCube(val, topMiddle1, 1, '+')
merge(topMiddle1, val)
#end Test
#start Test
val = makeTextObj('PDF', topMiddle1)
val.active_material = material_white
joinTextCube(val, topMiddle1, 2, '+')
merge(topMiddle1, val)
#end Test
topMiddle1.keyframe_insert(data_path="location", frame=82)
topMiddle1.location = (-0.002744, 0.032354, 0.084068)
topMiddle1.keyframe_insert(data_path="location", frame=109)
#**********#






#####right#####

#**********#
topLeft3 = addBoxWithMaterial('topLeft3', material_top, (0.036255, -0.045646, 0.333565), (-0.000003, 0, 0), (0.035, 0.032, 0.02))
#start Test
val = makeTextObj('App', topLeft3)
val.active_material = material_white
joinTextCube(val, topLeft3, 1, '-')
merge(topLeft3, val)
#end Test
#start Test
val = makeTextObj('App', topLeft3)
val.active_material = material_white
joinTextCube(val, topLeft3, 0, '+')
merge(topLeft3, val)
#end Test
#start Test
val = makeTextObj('ID', topLeft3)
val.active_material = material_white
joinTextCube(val, topLeft3, 2, '+')
merge(topLeft3, val)
#end Test
topLeft3.keyframe_insert(data_path="location", frame=120)
topLeft3.location = (0.036255, -0.045646, 0.084068)
topLeft3.keyframe_insert(data_path="location", frame=159)
#**********#

#**********#
topLeft2 = addBoxWithMaterial('topLeft2', material_top, (0.036255, -0.006646, 0.333565), (-0.000003, 0, 0), (0.035, 0.032, 0.02))
#start Test
val = makeTextObj('App', topLeft2)
val.active_material = material_white
joinTextCube(val, topLeft2, 0, '+')
merge(topLeft2, val)
#end Test
#start Test
val = makeTextObj('PII', topLeft2)
val.active_material = material_white
joinTextCube(val, topLeft2, 2, '+')
merge(topLeft2, val)
#end Test
topLeft2.keyframe_insert(data_path="location", frame=92)
topLeft2.location = (0.036255, -0.006646, 0.084068)
topLeft2.keyframe_insert(data_path="location", frame=131)
#**********#

#**********#
topLeft1 = addBoxWithMaterial('topLeft1', material_top, (0.036255, 0.032354, 0.333565), (-0.000003, 0, 0), (0.035, 0.032, 0.02))
#start Test
val = makeTextObj('App', topLeft1)
val.active_material = material_white
joinTextCube(val, topLeft1, 1, '+')
merge(topLeft1, val)
#end Test
#start Test
val = makeTextObj('App', topLeft1)
val.active_material = material_white
joinTextCube(val, topLeft1, 0, '+')
merge(topLeft1, val)
#end Test
#start Test
val = makeTextObj('R', topLeft1)
val.active_material = material_white
joinTextCube(val, topLeft1, 2, '+')
merge(topLeft1, val)
#end Test
topLeft1.keyframe_insert(data_path="location", frame=71)
topLeft1.location = (0.036255, 0.032354, 0.084068)
topLeft1.keyframe_insert(data_path="location", frame=104)
#**********#


filePath = "D:\\cube.fbx"   #edit this
bpy.ops.export_scene.fbx(filepath=filePath, use_selection=False, path_mode = 'COPY', bake_anim_use_all_bones=False, bake_anim_use_nla_strips=False, bake_anim_use_all_actions=False, bake_anim_force_startend_keying=False    )