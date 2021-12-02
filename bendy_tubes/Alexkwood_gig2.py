# {"name": "Alexkwoods 2nd script", "author": "Poseidon", "version": (1, 0), "blender": (2, 92, 5)}
import bpy

win      = bpy.context.window
scr      = win.screen
areas3d  = [area for area in scr.areas if area.type == 'VIEW_3D']
region   = [region for region in areas3d[0].regions if region.type == 'WINDOW']

override = {'window':win,
            'screen':scr,
            'area'  :areas3d[0],
            'region':region[0],
            'scene' :bpy.context.scene,
            }

##########################################################################
#Remove all objects
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()
for col in bpy.data.collections:
    bpy.data.collections.remove(col)

col = bpy.data.collections.new('Collection')
bpy.context.scene.collection.children.link(col)
layer_collection = bpy.context.view_layer.layer_collection.children[col.name]
bpy.context.view_layer.active_layer_collection = layer_collection

bpy.context.scene.frame_start = 60
bpy.context.scene.frame_end = 170
##########################################################################

font1 = 'C:\\Users\\yassine\\Desktop\\Alexkwood\\APOLLO.otf'
font2 = 'C:\\Users\\yassine\\Desktop\\Alexkwood\\Baxoe.ttf'
font3 = 'C:\\Users\\yassine\\Desktop\\Alexkwood\\Rockstar.otf'
filePath = "C:\\Users\\yassine\\Desktop\\Alexkwood\\cube.fbx"

#function that creates a Tube, and an origin, for the bendth
def funcDZB(name_tube, name_origin,  location, material):
    bpy.ops.object.empty_add(type='PLAIN_AXES', align='WORLD', location=location, scale=(1, 1, 1))
    bpy.context.active_object.name = name_origin
    if (2,93,0) < bpy.app.version:
        bpy.ops.mesh.primitive_cube_add(size= 0.5, enter_editmode=False, align='WORLD', location=(location[0]+0, location[1]+0.25, location[2]+0.25), scale=(1, 1, 5))
    else:
        bpy.ops.mesh.primitive_cube_add(size= 1, enter_editmode=False, align='WORLD', location=(location[0]+0, location[1]+0.25, location[2]+0.25), scale=(1, 1, 5))
    bpy.context.active_object.active_material = material
    bpy.context.active_object.name= name_tube
    tube = bpy.context.scene.collection.children['Collection'].objects[name_tube]
    origin = bpy.context.scene.collection.children['Collection'].objects[name_origin]    
    return tube, origin
#cut tube in edit mode
def cutTube(obj):
    bpy.ops.object.select_all(action='DESELECT')
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj

    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.loopcut_slide(override, MESH_OT_loopcut={"number_cuts":40, "smoothness":0, "falloff":'INVERSE_SQUARE', "object_index":0, "edge_index":3, "mesh_select_mode_init":(True, False, False)}, TRANSFORM_OT_edge_slide={"value":0, "single_side":False, "use_even":False, "flipped":False, "use_clamp":True, "mirror":True, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "correct_uv":True, "release_confirm":True, "use_accurate":False})
    bpy.ops.object.editmode_toggle()
#bend tube
def bendTube(obj, origin, angle, axis):
    bpy.ops.object.select_all(action='DESELECT')
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj

    bpy.ops.object.modifier_add(type='SIMPLE_DEFORM')
    bpy.context.object.modifiers["SimpleDeform"].deform_method = 'BEND'
    bpy.context.object.modifiers["SimpleDeform"].origin = origin
    bpy.context.object.modifiers["SimpleDeform"].deform_axis = axis
    bpy.context.object.modifiers["SimpleDeform"].angle = angle
#add a material, you give it the name & rgb color as input
def addMaterial(name, color):
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
    mat = bpy.data.materials.get(name)
    return mat
#this will create a text object, in the font 1
def makeTextObj_1(text, box_obj, size):
    bpy.ops.object.select_all(action='DESELECT')

    
    font_curve = bpy.data.curves.new(type="FONT", name="FC_alpha")
    font_curve.body = text
    font_obj = bpy.data.objects.new(name=text, object_data=font_curve)
    font_obj.data.size = size
    font_obj.data.align_x = 'CENTER'
    #######
    my_name = text
    
    for ob in bpy.data.objects:
        if ob.name == my_name:
            ob.data.font = bpy.data.fonts.load(font1)

    #######
    bpy.context.scene.collection.objects.link(font_obj)

    bpy.data.objects[text].select_set(True)
    bpy.context.view_layer.objects.active = bpy.data.objects[text]
    bpy.context.object.data.extrude = 0.02
    bpy.ops.object.origin_set(type='GEOMETRY_ORIGIN', center='MEDIAN')
    
    
    bpy.ops.object.convert(target='MESH', keep_original=False, angle=1.22173, thickness=5, seams=False, faces=True, offset=0.01)
    bpy.data.objects[text].scale[0] = box_obj.dimensions[0]/2
    bpy.data.objects[text].scale[1] = box_obj.dimensions[1]/2
    val = bpy.data.objects[text]
    val.name+= "_text"
    return val
#this will create a text object, in the font 2
def makeTextObj_2(text, box_obj, size):
    bpy.ops.object.select_all(action='DESELECT')

    
    font_curve = bpy.data.curves.new(type="FONT", name="FC_alpha")
    font_curve.body = text
    font_obj = bpy.data.objects.new(name=text, object_data=font_curve)
    font_obj.data.size = size
    #######
    my_name = text
    
    for ob in bpy.data.objects:
        if ob.name == my_name:
            ob.data.font = bpy.data.fonts.load(font2)

    #######
    bpy.context.scene.collection.objects.link(font_obj)

    bpy.data.objects[text].select_set(True)
    bpy.context.view_layer.objects.active = bpy.data.objects[text]
    bpy.context.object.data.extrude = 0.02
    bpy.ops.object.origin_set(type='GEOMETRY_ORIGIN', center='MEDIAN')
    
    
    bpy.ops.object.convert(target='MESH', keep_original=False, angle=1.22173, thickness=5, seams=False, faces=True, offset=0.01)
    bpy.data.objects[text].scale[0] = box_obj.dimensions[0]/2
    bpy.data.objects[text].scale[1] = box_obj.dimensions[1]/2
    val = bpy.data.objects[text]
    val.name+= "_te2xt2"
    return val
#this will create a text object, in the font 3
def makeTextObj_nbr(text, box_obj):
    bpy.ops.object.select_all(action='DESELECT')

    
    font_curve = bpy.data.curves.new(type="FONT", name="FC_alpha")
    font_curve.body = text
    font_obj = bpy.data.objects.new(name=text, object_data=font_curve)
    #######
    my_name = text
    for ob in bpy.data.objects:
        if ob.name == my_name:
            ob.data.font = bpy.data.fonts.load(font3)

    #######
    bpy.context.scene.collection.objects.link(font_obj)

    bpy.data.objects[text].select_set(True)
    bpy.context.view_layer.objects.active = bpy.data.objects[text]
    bpy.context.object.data.extrude = 0.0002
    bpy.ops.object.origin_set(type='GEOMETRY_ORIGIN', center='MEDIAN')
    
    
    bpy.ops.object.convert(target='MESH', keep_original=False, angle=1.22173, thickness=5, seams=False, faces=True, offset=0.01)
    bpy.data.objects[text].scale[0] = box_obj.dimensions[0]/2
    bpy.data.objects[text].scale[1] = box_obj.dimensions[1]/2
    val = bpy.data.objects[text]

    return val
#this function joins the text objext to the face of a cube
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
#this one merges the text and the cube into one object
def merge(box_obj, text_obj):
    bpy.ops.object.select_all(action='DESELECT')
    bpy.context.view_layer.objects.active = box_obj
    box_obj.select_set(True)
    text_obj.select_set(True)
    bpy.ops.object.join()
#zemla dzb
def zemla(tube):
    for obj in bpy.data.objects:
        if "origin" in obj.name:
            obj.location[2] -= tube.scale[2]
    bpy.context.scene.tool_settings.transform_pivot_point = 'INDIVIDUAL_ORIGINS'
    for obj in bpy.data.objects:
        if "tube" in obj.name:
            bpy.ops.object.select_all(action='DESELECT')
            obj.scale[0] -= 0.25
            obj.scale[1] -= 0.25
            obj.select_set(True)
            bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
            obj.keyframe_insert(data_path="scale", frame=170)
            obj.scale[2] = 0
            obj.keyframe_insert(data_path="scale", frame=0)

    for obj in bpy.data.objects:
        if "_te2xt2" in obj.name:
            obj.keyframe_insert(data_path="scale", frame=100)
            obj.scale[0] = 0
            obj.scale[1] = 0
            obj.keyframe_insert(data_path="scale", frame=60)
def update_viewport():
    bpy.context.scene.frame_current = 0
    bpy.context.scene.frame_current = 170

##########################################################################
blue = addMaterial('BLUE', (0.18,0.45, 0.51, 1))
yellow = addMaterial('YELLOW', (0.96, 0.76, 0.16, 1))
light_brown = addMaterial('LIGHT_BROWN', (0.95, 0.6, 0.47, 1))
light_green = addMaterial('LIGHT_GREEN', (0.42, 0.81, 0.525, 1))
light_blue = addMaterial('LIGHT_BLUE', (0.69 , 0.87, 0.9 , 1))
orange = addMaterial('ORANGE', (0.95, 0.43, 0.066, 1))
white = addMaterial('WHITE', (1, 1, 1, 1))
not_so_white = addMaterial('NOT_SO_WHITE', (0.98, 0.93, 0.78, 1))
green = addMaterial('GREEN', (0.52, 0.7, 0.63, 1))
black = addMaterial('BLACK', (0.02, 0.02, 0.02, 1))
red = addMaterial('RED', (1, 0, 0, 1))
purple = addMaterial('PURPLE', (0.5, 0, 0.5, 1))
##########################################################################



#the base plane with the base text
bpy.ops.mesh.primitive_plane_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, -1), scale=(1, 1, 1))
plane = bpy.context.active_object
bpy.context.scene.cursor.location = plane.location
ob = bpy.data.objects['Plane']
ob.active_material = white
#######
ab = makeTextObj_2('Excel \n Template \n Groups', ob, 0.5)
ab.active_material = purple
joinTextCube(ab, ob, 2, '+')

##########################################################################
#the texts
#1
txt1 = makeTextObj_1('Requirements\nGathering', ob, 0.25)
txt1.active_material = red
txt1.location = (-0.7, 1.3, 1.6)
#2
txt2 = makeTextObj_1('Database Design &\nImplementation', ob, 0.25)
txt2.active_material = red
txt2.location = (0.9, 1.3, 1.6)
#3
txt3 = makeTextObj_1('Reporting\n&\nDistribution', ob, 0.25)
txt3.active_material = red
txt3.location = (1.5, 0.5, 1.6)
#4
txt4 = makeTextObj_1('Analytics\n&\nDashboards', ob, 0.25)
txt4.active_material = red
txt4.location = (1.5, -0.5, 1.6)
#5
txt5 = makeTextObj_1('Entreprise\nTools\nMigrations', ob, 0.25)
txt5.active_material = red
txt5.location = (0.5, -1.4, 1.6)
#6
txt6 = makeTextObj_1('Web\n& Mobile\nApps', ob, 0.25)
txt6.active_material = red
txt6.location = (-0.5, -1.4, 1.6)
#7
txt7 = makeTextObj_1('Deployment\n&\nMonitoring', ob, 0.25)
txt7.active_material = red
txt7.location = (-1.7, -0.5, 1.6)
#8
txt8 = makeTextObj_1('API\nSupport using\nLua & Python', ob, 0.25)
txt8.active_material = red
txt8.location = (-1.7, 0.5, 1.6)
##########################################################################

#all the tubes
##NORTH##
leTube, leOrigin = funcDZB('tubeNorthRight', 'originNorthRight', (0.5, 1, 0), not_so_white)
#######
N0=makeTextObj_nbr('02', leTube)
N0.active_material = black
joinTextCube(N0, leTube, 2, '+')
merge(leTube,N0)
#######
cutTube(leTube)
bendTube(leTube, leOrigin, -0.279253, 'X')

leTube, leOrigin = funcDZB('tubeNorthLeft', 'originNorthLeft', (-0.5, 1, 0), orange)
#######
N0=makeTextObj_nbr('01', leTube)
N0.active_material = black
joinTextCube(N0, leTube, 2, '+')
merge(leTube,N0)
#######
cutTube(leTube)
bendTube(leTube, leOrigin, -0.279253, 'X')

##SOUTH##
leTube, leOrigin = funcDZB('tubeSouthRight', 'originSouthRiht', (0.5, -1.5, 0), yellow)
#######
N0=makeTextObj_nbr('05', leTube)
N0.active_material = black
joinTextCube(N0, leTube, 2, '+')
merge(leTube,N0)
#######
cutTube(leTube)
bendTube(leTube, leOrigin, 0.279253, 'X')

leTube, leOrigin = funcDZB('tubeSouthLeft', 'originSouthLeft', (-0.5, -1.5, 0), light_brown)
#######
N0=makeTextObj_nbr('06', leTube)
N0.active_material = black
joinTextCube(N0, leTube, 2, '+')
merge(leTube,N0)
#######
cutTube(leTube)
bendTube(leTube, leOrigin, 0.279253, 'X')


##EAST##
leTube, leOrigin = funcDZB('tubeEastTop', 'originEastTop', (1.25, 0.25, 0), green)
#######
N0=makeTextObj_nbr('03', leTube)
N0.active_material = black
joinTextCube(N0, leTube, 2, '+')
merge(leTube,N0)
#######
cutTube(leTube)
bendTube(leTube, leOrigin, -0.279253, 'Y')

leTube, leOrigin = funcDZB('tubeEastBot', 'originEastBot', (1.25, -0.75, 0), blue)
#######
N0=makeTextObj_nbr('04', leTube)
N0.active_material = black
joinTextCube(N0, leTube, 2, '+')
merge(leTube,N0)
#######
cutTube(leTube)
bendTube(leTube, leOrigin, -0.279253, 'Y')


##WEST##
leTube, leOrigin = funcDZB('tubeWestTop', 'originWestTop', (-1.25, 0.25, 0), light_blue)
#######
N0=makeTextObj_nbr('08', leTube)
N0.active_material = black
joinTextCube(N0, leTube, 2, '+')
merge(leTube,N0)
#######
cutTube(leTube)
bendTube(leTube, leOrigin, 0.279253, 'Y')

leTube, leOrigin = funcDZB('tubeWestBot', 'originWestBot', (-1.25, -0.75, 0), light_green)
#######
N0=makeTextObj_nbr('07', leTube)
N0.active_material = black
joinTextCube(N0, leTube, 2, '+')
merge(leTube,N0)
#######
cutTube(leTube)
bendTube(leTube, leOrigin, 0.279253, 'Y')

#######

zemla(leTube)
update_viewport()

bpy.ops.export_scene.fbx(filepath=filePath, use_selection=False, path_mode = 'COPY', bake_anim_use_all_bones=False, bake_anim_use_nla_strips=False, bake_anim_use_all_actions=False, bake_anim_force_startend_keying=False, use_mesh_modifiers=True)
bpy.ops.wm.quit_blender()
update_viewport()