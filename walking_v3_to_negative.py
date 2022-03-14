import os
import numpy as np
import bpy
import math
from mathutils import Matrix
import random

#from tqdm import tqdm

bpy.ops.object.armature_basic_human_metarig_add()
#bpy.ops.transform.resize(value=(5, 5, 5))

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
bpy.ops.transform.rotate(value = -0.5, orient_axis = 'Y')
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
thigh_L.constraints["Limit Rotation"].max_y = 0
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
thigh_R.constraints["Limit Rotation"].max_y = 0
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
#bpy.ops.transform.rotate(value = math.radians(-5), orient_axis = 'X')
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
#bpy.ops.transform.rotate(value = math.radians(-5), orient_axis = 'X')
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

#set constraints for left toe
toe_L.bone.select = True
bpy.data.objects["metarig"].data.bones.active = toe_L.bone
bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
bpy.context.object.pose.bones["toe.L"].constraints["Limit Rotation"].owner_space = 'LOCAL_WITH_PARENT'
bpy.context.object.pose.bones["toe.L"].constraints["Limit Rotation"].use_transform_limit = True
toe_L.constraints["Limit Rotation"].use_limit_x = True
toe_L.constraints["Limit Rotation"].min_x = math.radians(0)
toe_L.constraints["Limit Rotation"].max_x = math.radians(30)
toe_L.constraints["Limit Rotation"].use_limit_y = True
toe_L.constraints["Limit Rotation"].max_y = 0
toe_L.constraints["Limit Rotation"].use_limit_z = True
toe_L.constraints["Limit Rotation"].max_z = 0

bpy.ops.pose.constraint_add(type='LIMIT_LOCATION')
bpy.context.object.pose.bones["toe.L"].constraints["Limit Location"].owner_space = 'WORLD'
toe_L.constraints["Limit Location"].use_min_z = True
bpy.context.object.pose.bones["toe.L"].constraints["Limit Location"].use_transform_limit = True
toe_L.constraints["Limit Location"].min_z = 0
toe_L.bone.select = False

#set constraints for right toe
toe_R.bone.select = True
bpy.data.objects["metarig"].data.bones.active = toe_R.bone
bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
bpy.context.object.pose.bones["toe.R"].constraints["Limit Rotation"].owner_space = 'LOCAL_WITH_PARENT'
bpy.context.object.pose.bones["toe.R"].constraints["Limit Rotation"].use_transform_limit = True
toe_R.constraints["Limit Rotation"].use_limit_x = True
toe_R.constraints["Limit Rotation"].min_x = math.radians(0)
toe_R.constraints["Limit Rotation"].max_x = math.radians(30)
toe_R.constraints["Limit Rotation"].use_limit_y = True
toe_R.constraints["Limit Rotation"].max_y = 0
toe_R.constraints["Limit Rotation"].use_limit_z = True
toe_R.constraints["Limit Rotation"].max_z = 0

bpy.ops.pose.constraint_add(type='LIMIT_LOCATION')
bpy.context.object.pose.bones["toe.R"].constraints["Limit Location"].owner_space = 'WORLD'
toe_R.constraints["Limit Location"].use_min_z = True
bpy.context.object.pose.bones["toe.R"].constraints["Limit Location"].use_transform_limit = True
toe_R.constraints["Limit Location"].min_z = 0

toe_R.bone.select = False

#set constraints for left heel
heel_L.bone.select = True
bpy.data.objects["metarig"].data.bones.active = heel_L.bone
bpy.ops.pose.constraint_add(type='LIMIT_LOCATION')
bpy.context.object.pose.bones["heel.02.L"].constraints["Limit Location"].owner_space = 'WORLD'
heel_L.constraints["Limit Location"].use_min_z = True
bpy.context.object.pose.bones["heel.02.L"].constraints["Limit Location"].use_transform_limit = True
heel_L.constraints["Limit Location"].min_z = 0
heel_L.bone.select = False

#set constraints for right heel
heel_R.bone.select = True
bpy.data.objects["metarig"].data.bones.active = heel_R.bone
bpy.ops.pose.constraint_add(type='LIMIT_LOCATION')
bpy.context.object.pose.bones["heel.02.R"].constraints["Limit Location"].owner_space = 'WORLD'
heel_R.constraints["Limit Location"].use_min_z = True
bpy.context.object.pose.bones["heel.02.R"].constraints["Limit Location"].use_transform_limit = True
heel_R.constraints["Limit Location"].min_z = 0
heel_R.bone.select = False

#main_spine.bone.select = True
#bpy.ops.transform.rotate(value = math.radians(-7), orient_axis = 'X')

#imu_data = (head, neck, main_spine, upper_arm_L, forearm_L, upper_arm_R, forearm_R, thigh_L, shin_L, thigh_R, shin_R, foot_R, foot_L, hand_R, hand_L)

coord_file_path = "D:\\Codes\\Blender\\final_files\\coordinates.txt"
if os.path.isfile(coord_file_path):
    os.remove(coord_file_path)







#factor = 0.66

    #elif person == 2:
      #  return np.random.normal(7.5*factor,0.1)

def waling_animation(person_dict):

    shin_m = person_dict["shin_m_radians"] * person_dict["factor"] # 50
    thigh_m = person_dict["thigh_m_radians"]*person_dict["factor"] # 10
    spine_m = 5.0*person_dict["factor"] # 1
    hand_m = 7
    msm = 20*person_dict["factor"]


person_dict_1 = {"factor" : 0.66,
                 "shin_m_radians" : 20,
                 "thigh_m_radians" : 10,
                 # ... define the other person specific data here.
                 "path" : ["S_15", "TR_7_27", "TL_22"]
                }
"""
GS_15 means go straight by 15 steps
TR_7_27 means turn right using a radius of 7 and go 27 steps
TL_7_27 means turn left using a radius of 7 and go 27 steps
TR_90 means turn right on its current position by 90 degrees and don't go any step after turning
-> Define some other path descriptions
"""

class Person:
    imu_data = (head, neck, main_spine, upper_arm_L, forearm_L, upper_arm_R, forearm_R, thigh_L, shin_L, thigh_R, shin_R, foot_R, foot_L, hand_R, hand_L)
    frame = 0
    rfap = 0  # right forearm position
    lfap = 0  # left forearm position
    rtp = 0  # right foot position
    ltp = 0  # left foot position
    stp = 0  # steps length
    rkp = 0  # right knee position
    lkp = 0  # left knee position
    lsp = 0  # left shin position
    rsp = 0  # right shin position
    msp = 0  # main spine position
    msz = 0  # deviation of main spine from Z axis
    ruap = 0  # right upper arm position
    luap = 0  # left upper arm position
    fc = 0
    final_result = []

    def __init__(self, factor, frame_constant):
        self.factor = factor
        self.shin_m = factor * 50
        self.thigh_m = factor * 10
        self.hand_m = 7
        self.spine_m = factor * 2
        self.fc = frame_constant  # frame constant respectively sampling rate 30 Hz means every 1/30 sec a new sample
        #record(1)

    def thigh_m_random(self):
            return np.random.normal(10 * self.factor, 0.1)

    def record(self, frame_num):
        # frame_num = constsant + frame_num
        bpy.ops.pose.select_all(action='SELECT')
        bpy.context.scene.frame_set(frame_num)
        bpy.ops.anim.keyframe_insert_menu(type='BUILTIN_KSI_LocRot')

        bpy.ops.pose.select_all(action='INVERT')

    def save_coords(self,imu_data, frame):
        resulting_list = []
        for bone in imu_data:
            result = np.array(bone.matrix)[:3, :4]
            location = result[:, -1]
            rotation = result[:3, :3]

        sensor_location = [location[i] for i in range(len(location))]
        sensor_rotation = []
        for j in range(0, 3):
            for k in range(0, 3):
                sensor_rotation.append(rotation[j][k])
                while k == 3:
                    k = 0

        resulting_list.extend(sensor_location + sensor_rotation)

        resulting_list = resulting_list + [frame]
        return resulting_list

    def start_walking(self):
        thigh_L.bone.select = True
        self.ltp = (math.radians(self.thigh_m_random())) + self.ltp
        bpy.ops.transform.rotate(value=(math.radians(self.thigh_m_random())), orient_axis='X')
        thigh_L.bone.select = False

        shin_L.bone.select = True
        self.lsp = (math.radians(-self.shin_m)) + self.lsp
        bpy.ops.transform.rotate(value=(math.radians(-self.shin_m)), orient_axis='X')
        shin_L.bone.select = False

        forearm_R.bone.select = True
        self.rfap = (math.radians(self.hand_m)) + self.rfap
        bpy.ops.transform.rotate(value=(math.radians(self.hand_m)), orient_axis='X')
        forearm_R.bone.select = False

        self.frame = self.frame + self.fc  # frame = 5
        self.record(self.frame)
        self.final_result.append(self.save_coords(self.imu_data, self.frame))

        thigh_L.bone.select = True
        self.ltp = (math.radians(self.thigh_m_random())) + self.ltp
        bpy.ops.transform.rotate(value=(math.radians(self.thigh_m_random())), orient_axis='X')
        thigh_L.bone.select = False

        shin_L.bone.select = True
        self.lsp = (math.radians(self.shin_m)) + self.lsp
        bpy.ops.transform.rotate(value=(math.radians(self.shin_m)), orient_axis='X')
        shin_L.bone.select = False

        main_spine.bone.select = True
        self.msp = (math.radians(-self.spine_m)) + self.msp
        bpy.ops.transform.rotate(value=(math.radians(-self.spine_m)), orient_axis='X')
        main_spine.bone.select = False

        upper_arm_R.bone.select = True
        self.ruap = (math.radians(self.hand_m)) + self.ruap
        bpy.ops.transform.rotate(value=(math.radians(self.hand_m)), orient_axis='X')
        upper_arm_R.bone.select = False

        self.frame = self.frame + self.fc  # frame = 10
        self.record(self.frame)
        self.final_result.append(self.save_coords(self.imu_data, self.frame))

        thigh_R.bone.select = True
        self.rtp = (math.radians(-self.thigh_m_random())) + self.rtp
        bpy.ops.transform.rotate(value=(math.radians(-self.thigh_m_random())), orient_axis='X')
        thigh_R.bone.select = False

        main_spine.bone.select = True
        self.msz = (math.radians(-self.spine_m)) + self.msz
        bpy.ops.transform.translate(value=(0.0, (math.radians(-self.thigh_m_random())), (math.radians(-self.spine_m))))
        main_spine.bone.select = False

        upper_arm_L.bone.select = True
        self.luap = (math.radians(-self.hand_m)) + self.luap
        bpy.ops.transform.rotate(value=(math.radians(-self.hand_m)), orient_axis='X')
        upper_arm_L.bone.select = False

        self.frame = self.frame + self.fc  # frame = 15
        self.record(self.frame)

        self.final_result = np.array(self.final_result)
        np.savetxt(coord_file_path, self.final_result, "%.10g")

        self.final_result = []



    def walk_straight(self, radius, steps=0):

        for iteration in range(0, steps):

            shin_R.bone.select = True
            self.rsp = (math.radians(-self.shin_m)) + self.rsp
            bpy.ops.transform.rotate(value=(math.radians(-self.shin_m)), orient_axis='X')
            shin_R.bone.select = False

            thigh_R.bone.select = True
            self.rtp = (math.radians(self.thigh_m_random())) + self.rtp
            bpy.ops.transform.rotate(value=(math.radians(self.thigh_m_random())), orient_axis='X')
            thigh_R.bone.select = False

            main_spine.bone.select = True
            self.msz = (math.radians(-self.spine_m)) + self.msz
            bpy.ops.transform.translate(value=(0.0, 0.0, (math.radians(-self.spine_m))))
            main_spine.bone.select = False

            upper_arm_L.bone.select = True
            self.luap = (math.radians(self.hand_m)) + self.luap
            bpy.ops.transform.rotate(value=(math.radians(self.hand_m)), orient_axis='X')
            upper_arm_L.bone.select = False

            self.frame = self.frame + random.randint(3,5) # self.fc  # frame = 30
            self.record(self.frame)
            self.final_result.append(self.save_coords(self.imu_data, self.frame))

            thigh_L.bone.select = True
            self.ltp = (math.radians(-self.thigh_m_random())) + self.ltp
            bpy.ops.transform.rotate(value=(math.radians(-self.thigh_m_random())), orient_axis='X')
            thigh_L.bone.select = False

            main_spine.bone.select = True
            self.msz = (math.radians(self.spine_m)) + self.msz
            bpy.ops.transform.translate(value=(0.0, (math.radians(-self.thigh_m_random())), (math.radians(self.spine_m))))
            main_spine.bone.select = False

            thigh_R.bone.select = True
            self.rtp = (math.radians(self.thigh_m_random())) + self.rtp
            bpy.ops.transform.rotate(value=(math.radians(self.thigh_m_random())), orient_axis='X')
            thigh_R.bone.select = False

            upper_arm_R.bone.select = True
            self.ruap = (math.radians(-self.hand_m)) + self.ruap
            bpy.ops.transform.rotate(value=(math.radians(-self.hand_m)), orient_axis='X')
            upper_arm_R.bone.select = False

            upper_arm_L.bone.select = True
            self.luap = (math.radians(self.hand_m)) + self.luap
            bpy.ops.transform.rotate(value=(math.radians(self.hand_m)), orient_axis='X')
            upper_arm_L.bone.select = False

            self.frame = self.frame + random.randint(3,5) # self.fc  # frame = 35
            self.record(self.frame)
            self.final_result.append(self.save_coords(self.imu_data, self.frame))

            thigh_L.bone.select = True
            self.ltp = (math.radians(-self.thigh_m_random())) + self.ltp
            bpy.ops.transform.rotate(value=(math.radians(-self.thigh_m_random())), orient_axis='X')
            thigh_L.bone.select = False

            main_spine.bone.select = True
            self.msz = (math.radians(self.spine_m)) + self.msz
            bpy.ops.transform.translate(value=(0.0, (math.radians(-self.thigh_m_random())), (math.radians(self.spine_m))))
            main_spine.bone.select = False

            upper_arm_R.bone.select = True
            self.ruap = (math.radians(-self.hand_m)) + self.ruap
            bpy.ops.transform.rotate(value=(math.radians(-self.hand_m)), orient_axis='X')
            upper_arm_R.bone.select = False

            forearm_R.bone.select = True
            self.rfap = (math.radians(-self.hand_m)) + self.rfap
            bpy.ops.transform.rotate(value=(math.radians(-self.hand_m)), orient_axis='X')
            forearm_R.bone.select = False

            self.frame = self.frame + random.randint(3,5) # self.fc  # frame = 40
            self.record(self.frame)
            ###final_result.append(save_coords(imu_data, frame))

            thigh_L.bone.select = True
            self.ltp = (math.radians(-self.thigh_m_random())) + self.ltp
            bpy.ops.transform.rotate(value=(math.radians(-self.thigh_m_random())), orient_axis='X')
            thigh_L.bone.select = False

            main_spine.bone.select = True
            self.msz = (math.radians(-self.spine_m)) + self.msz
            bpy.ops.transform.translate(value=(0.0, (math.radians(-self.thigh_m_random())), (math.radians(-self.spine_m))))
            main_spine.bone.select = False

            thigh_R.bone.select = True
            self.rtp = (math.radians(self.thigh_m_random())) + self.rtp
            bpy.ops.transform.rotate(value=(math.radians(self.thigh_m_random())), orient_axis='X')
            thigh_R.bone.select = False

            shin_R.bone.select = True
            self.rsp = (math.radians(self.shin_m)) + self.rsp
            bpy.ops.transform.rotate(value=(math.radians(self.shin_m)), orient_axis='X')
            shin_R.bone.select = False

            upper_arm_L.bone.select = True
            self.luap = (math.radians(self.hand_m)) + self.luap
            bpy.ops.transform.rotate(value=(math.radians(self.hand_m)), orient_axis='X')
            upper_arm_L.bone.select = False

            forearm_L.bone.select = True
            self.lfap = (math.radians(self.hand_m)) + self.lfap
            bpy.ops.transform.rotate(value=(math.radians(self.hand_m)), orient_axis='X')
            forearm_L.bone.select = False

            upper_arm_R.bone.select = True
            self.ruap = (math.radians(self.hand_m)) + self.ruap
            bpy.ops.transform.rotate(value=(math.radians(self.hand_m)), orient_axis='X')
            upper_arm_R.bone.select = False

            # relying on the right leg

            self.frame = self.frame + random.randint(3,5) # self.fc  # frame = 45
            self.record(self.frame)
            ###final_result.append(save_coords(imu_data, frame))

            thigh_L.bone.select = True
            self.ltp = (math.radians(self.thigh_m_random())) + self.ltp
            bpy.ops.transform.rotate(value=(math.radians(self.thigh_m_random())), orient_axis='X')
            thigh_L.bone.select = False

            shin_L.bone.select = True
            self.lsp = (math.radians(-self.shin_m)) + self.lsp
            bpy.ops.transform.rotate(value=(math.radians(-self.shin_m)), orient_axis='X')
            shin_L.bone.select = False

            main_spine.bone.select = True
            self.msz = (math.radians(-self.spine_m)) + self.msz
            bpy.ops.transform.translate(value=(0.0, 0.0, (math.radians(-self.spine_m))))
            main_spine.bone.select = False

            upper_arm_L.bone.select = True
            self.luap = (math.radians(-self.hand_m)) + self.luap
            bpy.ops.transform.rotate(value=(math.radians(-self.hand_m)), orient_axis='X')
            upper_arm_L.bone.select = False

            forearm_R.bone.select = True
            self.rfap = (math.radians(self.hand_m)) + self.rfap
            bpy.ops.transform.rotate(value=(math.radians(self.hand_m)), orient_axis='X')
            forearm_R.bone.select = False

            upper_arm_R.bone.select = True
            self.ruap = (math.radians(self.hand_m)) + self.ruap
            bpy.ops.transform.rotate(value=(math.radians(self.hand_m)), orient_axis='X')
            upper_arm_R.bone.select = False

            self.frame = self.frame + random.randint(3,5) # self.fc  # frame = 50
            self.record(self.frame)
            self.final_result.append(self.save_coords(self.imu_data, self.frame))

            thigh_R.bone.select = True
            self.rtp = (math.radians(-self.thigh_m_random())) + self.rtp
            bpy.ops.transform.rotate(value=(math.radians(-self.thigh_m_random())), orient_axis='X')
            thigh_R.bone.select = False

            main_spine.bone.select = True
            self.msz = (math.radians(self.spine_m)) + self.msz
            bpy.ops.transform.translate(value=(0.0, (math.radians(-self.thigh_m_random())), (math.radians(self.spine_m))))
            main_spine.bone.select = False

            upper_arm_L.bone.select = True
            self.luap = (math.radians(-self.hand_m)) + self.luap
            bpy.ops.transform.rotate(value=(math.radians(-self.hand_m)), orient_axis='X')
            upper_arm_L.bone.select = False

            forearm_L.bone.select = True
            self.lfap = (math.radians(-self.hand_m)) + self.lfap
            bpy.ops.transform.rotate(value=(math.radians(-self.hand_m)), orient_axis='X')
            forearm_L.bone.select = False

            forearm_R.bone.select = True
            self.rfap = (math.radians(-self.hand_m)) + self.rfap
            bpy.ops.transform.rotate(value=(math.radians(-self.hand_m)), orient_axis='X')
            forearm_R.bone.select = False

            upper_arm_R.bone.select = True
            self.ruap = (math.radians(self.hand_m)) + self.ruap
            bpy.ops.transform.rotate(value=(math.radians(self.hand_m)), orient_axis='X')
            upper_arm_R.bone.select = False

            self.frame = self.frame + random.randint(3,5) # self.fc  # frame = 55
            self.record(self.frame)
            self.final_result.append(self.save_coords(self.imu_data, self.frame))

            thigh_R.bone.select = True
            self.rtp = (math.radians(-self.thigh_m_random())) + self.rtp
            bpy.ops.transform.rotate(value=(math.radians(-self.thigh_m_random())), orient_axis='X')
            thigh_R.bone.select = False

            main_spine.bone.select = True
            self.msz = (math.radians(self.spine_m)) + self.msz
            bpy.ops.transform.translate(value=(0.0, (math.radians(-self.thigh_m_random())), (math.radians(self.spine_m))))
            main_spine.bone.select = False

            thigh_L.bone.select = True
            self.ltp = (math.radians(self.thigh_m_random())) + self.ltp
            bpy.ops.transform.rotate(value=(math.radians(self.thigh_m_random())), orient_axis='X')
            thigh_L.bone.select = False

            upper_arm_L.bone.select = True
            self.luap = (math.radians(-self.hand_m)) + self.luap
            bpy.ops.transform.rotate(value=(math.radians(-self.hand_m)), orient_axis='X')
            upper_arm_L.bone.select = False

            # upper_arm_R.bone.select = True
            # ruap = (math.radians(-hand_m)) + ruap
            # bpy.ops.transform.rotate(value=(math.radians(-hand_m)), orient_axis='X')
            # upper_arm_R.bone.select = False

            self.frame = self.frame + random.randint(3,5) # self.fc  # frame = 60
            self.record(self.frame)
            self.final_result.append(self.save_coords(self.imu_data, self.frame))

            thigh_R.bone.select = True
            self.rtp = (math.radians(-self.thigh_m_random())) + self.rtp
            bpy.ops.transform.rotate(value=(math.radians(-self.thigh_m_random())), orient_axis='X')
            thigh_R.bone.select = False

            main_spine.bone.select = True
            self.msz = (math.radians(-self.spine_m)) + self.msz
            bpy.ops.transform.translate(value=(0.0, (math.radians(-self.thigh_m_random())), (math.radians(-self.spine_m))))
            main_spine.bone.select = False

            thigh_L.bone.select = True
            self.ltp = (math.radians(self.thigh_m_random())) + self.ltp
            bpy.ops.transform.rotate(value=(math.radians(self.thigh_m_random())), orient_axis='X')
            thigh_L.bone.select = False

            shin_L.bone.select = True
            self.lsp = (math.radians(self.shin_m)) + self.lsp
            bpy.ops.transform.rotate(value=(math.radians(self.shin_m)), orient_axis='X')
            shin_L.bone.select = False

            upper_arm_R.bone.select = True
            self.ruap = (math.radians(-self.hand_m)) + self.ruap
            bpy.ops.transform.rotate(value=(math.radians(-self.hand_m)), orient_axis='X')
            upper_arm_R.bone.select = False

            forearm_R.bone.select = True
            self.rfap = (math.radians(self.hand_m)) + self.rfap
            bpy.ops.transform.rotate(value=(math.radians(self.hand_m)), orient_axis='X')
            forearm_R.bone.select = False

            self.frame = self.frame + random.randint(3,5) # self.fc  # frame = 65
            self.record(self.frame)






        self.final_result = np.array(self.final_result)
        np.savetxt(coord_file_path, self.final_result, "%.10g")

        self.final_result = []

    def stop_walking(self):
        thigh_L.bone.select = True
        if self.ltp > 0:
            bpy.ops.transform.rotate(value=(-self.ltp), orient_axis='X')
        elif self.ltp < 0:
            bpy.ops.transform.rotate(value=(self.ltp), orient_axis='X')
        thigh_L.bone.select = False

        shin_L.bone.select = True
        if self.lsp > 0:
            bpy.ops.transform.rotate(value=(-self.lsp), orient_axis='X')
        elif self.lsp < 0:
            bpy.ops.transform.rotate(value=(self.lsp), orient_axis='X')
        shin_L.bone.select = False

        thigh_R.bone.select = True
        if self.rtp > 0:
            bpy.ops.transform.rotate(value=(-self.rtp), orient_axis='X')
        elif self.rtp < 0:
            bpy.ops.transform.rotate(value=(self.rtp), orient_axis='X')
        thigh_R.bone.select = False

        main_spine.bone.select = True
        bpy.ops.transform.rotate(value=(math.radians(self.spine_m)), orient_axis='X')
        bpy.ops.transform.translate(value=(0.0, (math.radians(-self.thigh_m_random() - self.thigh_m_random())), (math.radians(self.spine_m))))
        main_spine.bone.select = False

        upper_arm_R.bone.select = True
        # ruap = (math.radians(-hand_m)) + ruap
        if self.ruap > 0:
            bpy.ops.transform.rotate(value=(-self.ruap), orient_axis='X')
        elif self.ruap < 0:
            bpy.ops.transform.rotate(value=(self.ruap), orient_axis='X')
        upper_arm_R.bone.select = False

        forearm_R.bone.select = True
        # rfap = (math.radians(hand_m)) + rfap
        if self.rfap > 0:
            bpy.ops.transform.rotate(value=(-self.rfap), orient_axis='X')
        elif self.rfap < 0:
            bpy.ops.transform.rotate(value=(self.rfap), orient_axis='X')
        forearm_R.bone.select = False

        upper_arm_L.bone.select = True
        # luap = (math.radians(-hand_m)) + luap
        if self.luap > 0:
            bpy.ops.transform.rotate(value=(-self.luap), orient_axis='X')
        elif self.luap < 0:
            bpy.ops.transform.rotate(value=(self.luap), orient_axis='X')
        upper_arm_L.bone.select = False

        forearm_L.bone.select = True
        # lfap = (math.radians(-hand_m)) + lfap
        if self.lfap > 0:
            bpy.ops.transform.rotate(value=(-self.lfap), orient_axis='X')
        elif self.lfap < 0:
            bpy.ops.transform.rotate(value=(self.lfap), orient_axis='X')
        forearm_L.bone.select = False

        self.frame = self.frame + self.fc
        record(self.frame)

        self.final_result = np.array(self.final_result)
        np.savetxt(coord_file_path, self.final_result, "%.10g")


    def turn_right(self, radius, steps=0):
        self.turn = radius
        bpy.ops.pose.select_all(action='TOGGLE')
        bpy.ops.transform.rotate(value=(math.radians(turn)), orient_axis='Z')
        bpy.ops.pose.select_all(action='INVERT')

    def turn_left(self, radius, steps=0):
        pass

    def animate(self, action_list):
        for action in action_list:
            if action[:2] == "GS":
                self.walk_straight(int(action[3:]))


person_dict_2 = {"factor" : 0.66,
                 "shin_m_radians" : 20,
                 "thigh_m_radians" : 10,
                 # ... define the other person specific data here.
                }

def turn_right(radius, steps=0):
    pass

def make_animation(person_dict):
    pass

make_animation(person_dict_1)

waling_animation(person_dict_1)

new = Person(0.66, 5)

new.start_walking()

new.walk_straight(0, 15)