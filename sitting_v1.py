import os
import numpy as np
import bpy
import math
from random import randint

#from tqdm import tqdm

bpy.ops.object.armature_basic_human_metarig_add()
bpy.ops.object.posemode_toggle()
bpy.context.scene.tool_settings.use_keyframe_insert_auto = True
bpy.context.object.pose.use_auto_ik = False

#to bound the frames
bpy.data.scenes['Scene'].frame_start = 0
bpy.data.scenes['Scene'].frame_end = 500

#to define a preferred reset pose
bpy.context.object.pose.use_mirror_x = True
bpy.ops.pose.select_all(action='TOGGLE')
bpy.data.objects['metarig'].pose.bones['upper_arm.L'].bone.select = True
bpy.ops.transform.rotate(value = -1, orient_axis = 'Y')
bpy.data.objects['metarig'].pose.bones['upper_arm.L'].bone.select = False
bpy.context.object.pose.use_mirror_x = False
bpy.ops.pose.select_all(action='SELECT')
bpy.ops.pose.armature_apply(selected=True)
bpy.ops.pose.select_all(action='INVERT')

#bones
shin_R = bpy.data.objects['metarig'].pose.bones['shin.R']
shin_L = bpy.data.objects['metarig'].pose.bones['shin.L']
thigh_R = bpy.data.objects['metarig'].pose.bones['thigh.R']
thigh_L = bpy.data.objects['metarig'].pose.bones['thigh.L']
upper_arm_R = bpy.data.objects['metarig'].pose.bones['upper_arm.R']
upper_arm_L = bpy.data.objects['metarig'].pose.bones['upper_arm.L']
forearm_R = bpy.data.objects['metarig'].pose.bones['forearm.R']
forearm_L = bpy.data.objects['metarig'].pose.bones['forearm.L']
main_spine = bpy.data.objects['metarig'].pose.bones['spine']
up_side = bpy.data.objects['metarig'].pose.bones['spine.001']
head = bpy.data.objects['metarig'].pose.bones['spine.006']
neck = bpy.data.objects['metarig'].pose.bones['spine.004']
toe_L = bpy.data.objects['metarig'].pose.bones['toe.L']
toe_R = bpy.data.objects['metarig'].pose.bones['toe.R']
foot_L = bpy.data.objects['metarig'].pose.bones['foot.L']
foot_R = bpy.data.objects['metarig'].pose.bones['foot.R']
heel_L = bpy.data.objects['metarig'].pose.bones['heel.02.L']
heel_R = bpy.data.objects['metarig'].pose.bones['heel.02.R']
spine_chest = bpy.data.objects['metarig'].pose.bones['spine.003']
hand_L = bpy.data.objects['metarig'].pose.bones['hand.L']
hand_R = bpy.data.objects['metarig'].pose.bones['hand.R']

#set constraints for left thigh
thigh_L.bone.select = True
bpy.data.objects["metarig"].data.bones.active = thigh_L.bone
#bpy.ops.transform.rotate(value = math.radians(-2.5), orient_axis = 'X')
bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
bpy.context.object.pose.bones["thigh.L"].constraints["Limit Rotation"].owner_space = 'LOCAL_WITH_PARENT'
thigh_L.constraints["Limit Rotation"].use_limit_x = True
thigh_L.constraints["Limit Rotation"].min_x = math.radians(-130)
thigh_L.constraints["Limit Rotation"].max_x = math.radians(80)
thigh_L.constraints["Limit Rotation"].use_limit_y = True
thigh_L.constraints["Limit Rotation"].max_y = math.radians(30)
thigh_L.constraints["Limit Rotation"].use_limit_z = True
thigh_L.constraints["Limit Rotation"].max_z = 0
thigh_L.bone.select = False

#set constraints for right thigh
thigh_R.bone.select = True
bpy.data.objects["metarig"].data.bones.active = thigh_R.bone
bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
#bpy.ops.transform.rotate(value = math.radians(-2.5), orient_axis = 'X')
bpy.context.object.pose.bones["thigh.R"].constraints["Limit Rotation"].owner_space = 'LOCAL_WITH_PARENT'
thigh_R.constraints["Limit Rotation"].use_limit_x = True
thigh_R.constraints["Limit Rotation"].min_x = math.radians(-130)
thigh_R.constraints["Limit Rotation"].max_x = math.radians(80)
thigh_R.constraints["Limit Rotation"].use_limit_y = True
thigh_R.constraints["Limit Rotation"].max_y = math.radians(30)
thigh_R.constraints["Limit Rotation"].use_limit_z = True
thigh_R.constraints["Limit Rotation"].max_z = 0
thigh_R.bone.select = False

#set constraints for left shin
shin_L.bone.select = True
bpy.data.objects["metarig"].data.bones.active = shin_L.bone
#bpy.ops.transform.rotate(value = math.radians(3), orient_axis = 'X')
#bpy.ops.pose.constraint_add(type='IK')
#shin_L.constraints["IK"].target = bpy.data.objects["metarig"]
#shin_L.constraints["IK"].pole_target = bpy.data.objects["metarig"]
#shin_L.constraints["IK"].pole_subtarget = "thigh.L"
#shin_L.constraints["IK"].chain_count = 2
#shin_L.constraints["IK"].pole_angle = -1.5708

bpy.ops.pose.constraint_add(type = 'TRACK_TO')
bpy.context.object.pose.bones["shin.L"].constraints["Track To"].target = bpy.data.objects["metarig"]
bpy.context.object.pose.bones["shin.L"].constraints["Track To"].track_axis = 'TRACK_NEGATIVE_Y'
bpy.context.object.pose.bones["shin.L"].constraints["Track To"].up_axis = 'UP_Z'
bpy.context.object.pose.bones["shin.L"].constraints["Track To"].use_target_z = True

bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
bpy.context.object.pose.bones["shin.L"].constraints["Limit Rotation"].owner_space = 'LOCAL_WITH_PARENT'
shin_L.constraints["Limit Rotation"].use_limit_x = True
shin_L.constraints["Limit Rotation"].min_x = math.radians(-130)
shin_L.constraints["Limit Rotation"].max_x = math.radians(80)
shin_L.constraints["Limit Rotation"].use_limit_y = True
shin_L.constraints["Limit Rotation"].max_y = 0.174533
shin_L.constraints["Limit Rotation"].use_limit_z = True
shin_L.constraints["Limit Rotation"].max_z = 0
shin_L.bone.select = False

#set constraints for right shin
shin_R.bone.select = True
#bpy.ops.transform.rotate(value = math.radians(3), orient_axis = 'X')
bpy.data.objects["metarig"].data.bones.active = shin_R.bone
#bpy.ops.pose.constraint_add(type='IK')
#shin_R.constraints["IK"].target = bpy.data.objects["metarig"]
#shin_R.constraints["IK"].pole_target = bpy.data.objects["metarig"]
#shin_R.constraints["IK"].pole_subtarget = "thigh.R"
#shin_R.constraints["IK"].chain_count = 2
#shin_R.constraints["IK"].pole_angle = -1.5708
bpy.ops.pose.constraint_add(type = 'TRACK_TO')
bpy.context.object.pose.bones["shin.R"].constraints["Track To"].target = bpy.data.objects["metarig"]
bpy.context.object.pose.bones["shin.R"].constraints["Track To"].track_axis = 'TRACK_NEGATIVE_Y'
bpy.context.object.pose.bones["shin.R"].constraints["Track To"].up_axis = 'UP_Z'
bpy.context.object.pose.bones["shin.R"].constraints["Track To"].use_target_z = True

bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
bpy.context.object.pose.bones["shin.R"].constraints["Limit Rotation"].owner_space = 'LOCAL_WITH_PARENT'
shin_R.constraints["Limit Rotation"].use_limit_x = True
shin_R.constraints["Limit Rotation"].min_x = math.radians(-130)
shin_R.constraints["Limit Rotation"].max_x = math.radians(80)
shin_R.constraints["Limit Rotation"].use_limit_y = True
shin_R.constraints["Limit Rotation"].max_y = 0.174533
shin_R.constraints["Limit Rotation"].use_limit_z = True
shin_R.constraints["Limit Rotation"].max_z = 0
shin_R.bone.select = False

#set constraints for left foot
foot_L.bone.select = True
bpy.data.objects["metarig"].data.bones.active = foot_L.bone
bpy.ops.transform.rotate(value = math.radians(-5), orient_axis = 'X')
bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
bpy.context.object.pose.bones["foot.L"].constraints["Limit Rotation"].use_transform_limit = True
bpy.context.object.pose.bones["foot.L"].constraints["Limit Rotation"].owner_space = 'LOCAL_WITH_PARENT'
foot_L.constraints["Limit Rotation"].use_limit_x = True
foot_L.constraints["Limit Rotation"].min_x = math.radians(-30)
foot_L.constraints["Limit Rotation"].max_x = math.radians(60)
foot_L.constraints["Limit Rotation"].use_limit_y = True
foot_L.constraints["Limit Rotation"].max_y = 0
foot_L.constraints["Limit Rotation"].use_limit_z = True
foot_L.constraints["Limit Rotation"].max_z = 0
foot_L.bone.select = False

#set constraints for right foot
foot_R.bone.select = True
bpy.data.objects["metarig"].data.bones.active = foot_R.bone
bpy.ops.transform.rotate(value = math.radians(-5), orient_axis = 'X')
bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
bpy.context.object.pose.bones["foot.R"].constraints["Limit Rotation"].use_transform_limit = True
bpy.context.object.pose.bones["foot.R"].constraints["Limit Rotation"].owner_space = 'LOCAL_WITH_PARENT'
foot_R.constraints["Limit Rotation"].use_limit_x = True
foot_R.constraints["Limit Rotation"].min_x = math.radians(-30)
foot_R.constraints["Limit Rotation"].max_x = math.radians(60)
foot_R.constraints["Limit Rotation"].use_limit_y = True
foot_R.constraints["Limit Rotation"].max_y = 0
foot_R.constraints["Limit Rotation"].use_limit_z = True
foot_R.constraints["Limit Rotation"].max_z = 0
foot_R.bone.select = False



#set constraints for left heel
heel_L.bone.select = True
bpy.data.objects["metarig"].data.bones.active = heel_L.bone
bpy.ops.pose.constraint_add(type='LIMIT_LOCATION')
bpy.context.object.pose.bones["heel.02.L"].constraints["Limit Location"].owner_space = 'WORLD'
heel_L.constraints["Limit Location"].use_min_z = True
bpy.context.object.pose.bones["heel.02.L"].constraints["Limit Location"].use_transform_limit = True
#heel_L.constraints["Limit Location"].min_z = 0
heel_L.bone.select = False

#set constraints for right heel
heel_R.bone.select = True
bpy.data.objects["metarig"].data.bones.active = heel_R.bone
bpy.ops.pose.constraint_add(type='LIMIT_LOCATION')
bpy.context.object.pose.bones["heel.02.R"].constraints["Limit Location"].owner_space = 'WORLD'
heel_R.constraints["Limit Location"].use_min_z = True
bpy.context.object.pose.bones["heel.02.R"].constraints["Limit Location"].use_transform_limit = True
#heel_R.constraints["Limit Location"].min_z = 0
heel_R.bone.select = False

#main_spine.bone.select = True
#bpy.ops.transform.rotate(value = math.radians(-7), orient_axis = 'X')

coord_file_path = "D:\\Codes\\Blender\\final_files\\sitting_coordinates.txt"
#"D:\\Dropbox\\DFKI (Arbeit)\\Guided Students\\2021\\Masterarbeit\\Hesam (Blender)\\Code\\2021.11.08\\coordinates.txt"
if os.path.isfile(coord_file_path):
    os.remove(coord_file_path)

def record(frame_num):
    #frame_num = constsant + frame_num
    bpy.ops.pose.select_all(action='SELECT')
    bpy.context.scene.frame_set(frame_num)
    bpy.ops.anim.keyframe_insert_menu(type='BUILTIN_KSI_LocRot')
    bpy.ops.pose.select_all(action='INVERT')

def location(part):
    '''
    if part == 'neck' or part == 'main_spine':
        imu_sensor_location = part.bone.tail
    elif part == 'forearm_L' or part == 'forearm_R' or part == 'shin_L' or part == 'shin_R' :
        imu_sensor_location = (0.1*(part.bone.tail)) + (0.9*(part.bone.head))
    elif part == 'upper_arm_L' or part == 'upper_arm_R' or part == 'thigh_L' or part == 'thigh_R':
        imu_sensor_location = (0.1*(part.bone.head)) + (0.9*(part.bone.tail))
    '''
    sensor_location = ' '.join([str(elem) for elem in np.array(part.bone.head)]) + "\n"
    print("sensor_location =", sensor_location)
    w_on_file = open(coord_file_path, "a+")
    w_on_file.write(sensor_location)
    w_on_file.close()
    

def save_coords(imu_data, frame):
    resulting_list = []
    for bone in imu_data:
        # print("bone", bone.name)
        x = list(bone.matrix)
        y = list(x[0])
        use_head = False
        # initial_vector = np.array([bone.head[0], bone.head[1], bone.head[2], 1]).reshape(-1, 1)
        if use_head:
            initial_vector = np.array([bone.head[0], bone.head[1], bone.head[2], 1])
        else:
            initial_vector = np.array([bone.tail[0], bone.tail[1], bone.tail[2], 1])
        # print("initial_vector (***) =", initial_vector)
        # print(bone.name)
        # print("bone.matrix (***) =", bone.matrix)
        use_matrix_multiplication = False
        if use_matrix_multiplication:
            # print("np.numpy(bone.matrix) (***) =", np.array(bone.matrix))
            # result = np.matmul(bone.matrix, initial_vector).reshape(-1,)
            # print("bone.matrix =", bone.matrix)
            bone_matrix = np.array(bone.matrix).transpose()
            # print("bone.matrix.transpose() =", bone_matrix)
            result = np.matmul(initial_vector, bone_matrix)
        else:
            result = np.array(bone.matrix)[:,-1]
            # print("result (before neglect) =", result)
            # result = result[:-1]
            # print("result (after neglect) =", result)
        # print("result (***) =", result)
        sensor_location = [result[i] for i in range(len(result)-1)]
        resulting_list.extend(sensor_location)
    resulting_list = resulting_list + [frame]
    return resulting_list


imu_data = (head, neck, main_spine, upper_arm_L, forearm_L, upper_arm_R, forearm_R, thigh_L, shin_L, thigh_R, shin_R, foot_R, foot_L, hand_R, hand_L )
frame = 0




def random():
        return np.random.normal(scale=0.001)



limit = 50

#record(1)
final_result = []

thigh_L.bone.select = True
bpy.ops.transform.rotate(value = (math.radians(80)), orient_axis ='X')
thigh_L.bone.select = False

thigh_R.bone.select = True
bpy.ops.transform.rotate(value = (math.radians(80)), orient_axis = 'X')
thigh_R.bone.select = False

shin_L.bone.select = True
bpy.ops.transform.rotate(value = (math.radians(-80)), orient_axis ='X')
shin_L.bone.select = False

shin_R.bone.select = True
bpy.ops.transform.rotate(value = (math.radians(-80)), orient_axis = 'X')
shin_R.bone.select = False

bpy.ops.pose.select_all(action='TOGGLE')
bpy.ops.transform.translate(value = (0.0, 0.0, -0.48))
bpy.ops.pose.select_all(action='TOGGLE')

upper_arm_R.bone.select = True
bpy.ops.transform.rotate(value= (math.radians(25)), orient_axis='X')
upper_arm_R.bone.select = False

upper_arm_L.bone.select = True
bpy.ops.transform.rotate(value=(math.radians(25)), orient_axis='X')
upper_arm_L.bone.select = False

forearm_R.bone.select = True
bpy.ops.transform.rotate(value=(math.radians(35)), orient_axis='Y')
forearm_R.bone.select = False

forearm_L.bone.select = True
bpy.ops.transform.rotate(value=(math.radians(-35)), orient_axis='Y')
forearm_L.bone.select = False

record(1)

for rest in range(0, limit):
    axis = randint(1,3)

    thigh_L.bone.select = True
    bpy.ops.transform.rotate(value= random(), orient_axis='Z')
    thigh_L.bone.select = False

    thigh_R.bone.select = True
    bpy.ops.transform.rotate(value= random(), orient_axis='Z')
    thigh_R.bone.select = False

    upper_arm_R.bone.select = True
    bpy.ops.transform.rotate(value= random(), orient_axis='Z')
    upper_arm_R.bone.select = False

    upper_arm_L.bone.select = True
    bpy.ops.transform.rotate(value= random(), orient_axis='Z')
    upper_arm_L.bone.select = False

    forearm_R.bone.select = True
    bpy.ops.transform.rotate(value= random(), orient_axis='Z')
    forearm_R.bone.select = False

    forearm_L.bone.select = True
    bpy.ops.transform.rotate(value= random(), orient_axis='Z')
    forearm_L.bone.select = False

    up_side.bone.select = True
    bpy.ops.transform.rotate(value= random(), orient_axis='X')
    up_side.bone.select = False

    if axis == 1 :
        head.bone.select = True
        bpy.ops.transform.rotate(value= random(), orient_axis='X')
        head.bone.select = False
    elif axis == 2:
        head.bone.select = True
        bpy.ops.transform.rotate(value= random(), orient_axis='Y')
        head.bone.select = False
    elif axis == 3:
        head.bone.select = True
        bpy.ops.transform.rotate(value= random(), orient_axis='Z')
        head.bone.select = False

    frame = frame + 5
    record(frame)
    final_result.append(save_coords(imu_data, frame))




final_result = np.array(final_result)
print(final_result.shape)
np.savetxt(coord_file_path, final_result, "%.8g")

# w_on_file = open(coord_file_path, "a+")
# resulting_list = ' '.join(resulting_list + [str(frame)]) + "\n"
# w_on_file.write(resulting_list)
# w_on_file.close()
