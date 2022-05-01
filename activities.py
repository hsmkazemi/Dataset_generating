import os
import numpy as np
import bpy
import math
from mathutils import Matrix
import random

#from tqdm import tqdm


bpy.ops.object.armature_basic_human_metarig_add()

bpy.ops.object.editmode_toggle()

bpy.ops.armature.bone_primitive_add(name='guide')
bpy.ops.object.posemode_toggle()

rotation = math.radians(90)
bpy.data.objects['metarig'].pose.bones['guide'].bone.select = True
bpy.ops.transform.create_orientation(name='Track', use_view=False, use=False, overwrite=False)
bpy.ops.transform.resize(value=(0.001, 0.001, 0.001))
bpy.ops.transform.rotate(value=rotation, orient_axis='X', orient_type='LOCAL')
bpy.ops.transform.create_orientation(name='Track', use_view=False, use=False, overwrite=True)
bpy.data.objects['metarig'].pose.bones['guide'].bone.select = False

bpy.context.scene.tool_settings.use_keyframe_insert_auto = True
bpy.context.object.pose.use_auto_ik = False

#to bound the frames
bpy.data.scenes['Scene'].frame_start = 0
bpy.data.scenes['Scene'].frame_end = 500

#to define a preferred reset pose
bpy.context.object.pose.use_mirror_x = True
#bpy.ops.pose.select_all(action='TOGGLE')

bpy.data.objects['metarig'].pose.bones['upper_arm.L'].bone.select = True
bpy.ops.transform.rotate(value = -0.5, orient_axis = 'Y')
bpy.data.objects['metarig'].pose.bones['upper_arm.L'].bone.select = False
bpy.context.object.pose.use_mirror_x = False
bpy.ops.pose.select_all(action='SELECT')
bpy.ops.pose.armature_apply(selected=True)
bpy.ops.pose.select_all(action='INVERT')

#bones
guide = bpy.data.objects['metarig'].pose.bones['guide']
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
mid_spine = bpy.data.objects['metarig'].pose.bones['spine.002']
hand_L = bpy.data.objects['metarig'].pose.bones['hand.L']
hand_R = bpy.data.objects['metarig'].pose.bones['hand.R']
shoulder_L = bpy.data.objects['metarig'].pose.bones['shoulder.L']
shoulder_R = bpy.data.objects['metarig'].pose.bones['shoulder.R']


#set constraints for left thigh
thigh_L.bone.select = True
bpy.data.objects["metarig"].data.bones.active = thigh_L.bone
#bpy.ops.transform.rotate(value = math.radians(-2.5), orient_axis = 'X')
bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
bpy.context.object.pose.bones["thigh.L"].constraints["Limit Rotation"].owner_space = 'LOCAL_WITH_PARENT'
thigh_L.constraints["Limit Rotation"].use_limit_x = True
thigh_L.constraints["Limit Rotation"].min_x = math.radians(-130)
thigh_L.constraints["Limit Rotation"].max_x = math.radians(80)
thigh_L.constraints["Limit Rotation"].use_limit_y = False
thigh_L.constraints["Limit Rotation"].max_y = 0
thigh_L.constraints["Limit Rotation"].use_limit_z = False
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
thigh_R.constraints["Limit Rotation"].use_limit_y = False
thigh_R.constraints["Limit Rotation"].max_y = 0
thigh_R.constraints["Limit Rotation"].use_limit_z = False
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
shin_L.constraints["Limit Rotation"].use_limit_y = False
shin_L.constraints["Limit Rotation"].max_y = 0.174533
shin_L.constraints["Limit Rotation"].use_limit_z = False
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
shin_R.constraints["Limit Rotation"].use_limit_y = False
shin_R.constraints["Limit Rotation"].max_y = 0.174533
shin_R.constraints["Limit Rotation"].use_limit_z = False
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
foot_L.constraints["Limit Rotation"].use_limit_y = False
foot_L.constraints["Limit Rotation"].max_y = 0
foot_L.constraints["Limit Rotation"].use_limit_z = False
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
foot_R.constraints["Limit Rotation"].use_limit_y = False
foot_R.constraints["Limit Rotation"].max_y = 0
foot_R.constraints["Limit Rotation"].use_limit_z = False
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
toe_L.constraints["Limit Rotation"].use_limit_y = False
toe_L.constraints["Limit Rotation"].max_y = 0
toe_L.constraints["Limit Rotation"].use_limit_z = False
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
toe_R.constraints["Limit Rotation"].use_limit_y = False
toe_R.constraints["Limit Rotation"].max_y = 0
toe_R.constraints["Limit Rotation"].use_limit_z = False
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



class Person:
    parts = (shin_R, shin_L, thigh_R, thigh_L, upper_arm_R, upper_arm_L, forearm_R, forearm_L, up_side, head, neck, toe_L, toe_R, foot_L, foot_R, heel_L, heel_R, spine_chest, mid_spine, hand_L, hand_R, shoulder_L, shoulder_R)
    imu_data = (head, neck, main_spine, upper_arm_L, forearm_L, upper_arm_R, forearm_R, thigh_L, shin_L, thigh_R, shin_R, foot_R, foot_L, hand_R, hand_L)
    lower_side =(shin_R, shin_L, thigh_R, thigh_L, toe_L, toe_R, foot_L, foot_R, heel_L, heel_R)
    upper_side = (upper_arm_R, upper_arm_L, forearm_R, forearm_L, up_side, head, neck, spine_chest, mid_spine, hand_L, hand_R, shoulder_L, shoulder_R)
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
    position = 0 #1 start walking #2 walkning straight #3 stop walking #4 sitting #5 lying down #0 standing


    def __init__(self, factor, frame_constant):
        self.factor = factor
        self.shin_m = factor * 50
        self.thigh_m = factor * 10
        self.hand_m = 7
        self.spine_m = factor * 2
        self.fc = frame_constant  # frame constant respectively sampling rate 30 Hz means every 1/30 sec a new sample
        self.position = "Standing"
        self.turn(0)
        #record(1)

    def thigh_m_random(self):
            return np.random.normal(10 * self.factor, 0.1)

    def turn(self, degree):
        guide.bone.select = True
        bpy.ops.transform.rotate(value=(math.radians(degree)), orient_axis='Z', orient_type='LOCAL')
        bpy.ops.transform.create_orientation(name='Track', use_view=False, use=False, overwrite=True )
        guide.bone.select = False

        main_spine.bone.select = True
        bpy.ops.transform.rotate(value=(math.radians(degree)), orient_axis='Z', orient_type='Track')
        main_spine.bone.select = False


    def record(self, frame_num):
        # frame_num = constsant + frame_num
        bpy.ops.pose.select_all(action='SELECT')
        bpy.context.scene.frame_set(int(frame_num))
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

    def wait(self,time):
        for line in range(0,time):
            if self.position == "Sitting_in_front_of_a_table" and time >= 3:
                self._looking_around()
                self.frame = self.frame + random.uniform(6,5)  # frame = 10
                self.record(self.frame)
            elif self.position == "Standing" and time >= 3:
                #self._crossing_arms()
                self.frame = self.frame + random.uniform(2,3)  # frame = 10
                self.record(self.frame)
            elif self.position == "Lying_down" and time >= 3:
                self._crossing_legs()
                self.frame = self.frame + random.uniform(2,3)  # frame = 10
                self.record(self.frame)
            else:
                self.frame = self.frame + random.uniform(2,3)  # frame = 10
                self.record(self.frame)


    def start_walking(self): # position 0->1
        if self.position == "Standing":

            thigh_L.bone.select = True
            self.ltp = (math.radians(self.thigh_m_random())) + self.ltp
            bpy.ops.transform.rotate(value=(math.radians(self.thigh_m_random())), orient_axis='X', orient_type='Track')
            thigh_L.bone.select = False

            shin_L.bone.select = True
            self.lsp = (math.radians(-self.shin_m)) + self.lsp
            bpy.ops.transform.rotate(value=(math.radians(-self.shin_m)), orient_axis='X', orient_type='Track')
            shin_L.bone.select = False

            forearm_R.bone.select = True
            self.rfap = (math.radians(self.hand_m)) + self.rfap
            bpy.ops.transform.rotate(value=(math.radians(self.hand_m)), orient_axis='X', orient_type='Track')
            forearm_R.bone.select = False

            self.frame = self.frame + self.fc  # frame = 5
            self.record(self.frame)
            self.final_result.append(self.save_coords(self.imu_data, self.frame))

            thigh_L.bone.select = True
            self.ltp = (math.radians(self.thigh_m_random())) + self.ltp
            bpy.ops.transform.rotate(value=(math.radians(self.thigh_m_random())), orient_axis='X', orient_type='Track')
            thigh_L.bone.select = False

            shin_L.bone.select = True
            self.lsp = (math.radians(self.shin_m)) + self.lsp
            bpy.ops.transform.rotate(value=(math.radians(self.shin_m)), orient_axis='X', orient_type='Track')
            shin_L.bone.select = False

            main_spine.bone.select = True
            self.msp = (math.radians(-self.spine_m)) + self.msp
            bpy.ops.transform.rotate(value=(math.radians(-self.spine_m)), orient_axis='X', orient_type='Track')
            main_spine.bone.select = False

            upper_arm_R.bone.select = True
            self.ruap = (math.radians(self.hand_m)) + self.ruap
            bpy.ops.transform.rotate(value=(math.radians(self.hand_m)), orient_axis='X', orient_type='Track')
            upper_arm_R.bone.select = False

            self.frame = self.frame + self.fc  # frame = 10
            self.record(self.frame)
            self.final_result.append(self.save_coords(self.imu_data, self.frame))

            thigh_R.bone.select = True
            self.rtp = (math.radians(-self.thigh_m_random())) + self.rtp
            bpy.ops.transform.rotate(value=(math.radians(-self.thigh_m_random())), orient_axis='X', orient_type='Track')
            thigh_R.bone.select = False

            main_spine.bone.select = True
            self.msz = (math.radians(-self.spine_m)) + self.msz
            bpy.ops.transform.translate(value=(0.0, (math.radians(-self.thigh_m_random())), (math.radians(-self.spine_m))), orient_type='Track') # , orient_axis_ortho='Y'
            main_spine.bone.select = False

            upper_arm_L.bone.select = True
            self.luap = (math.radians(-self.hand_m)) + self.luap
            bpy.ops.transform.rotate(value=(math.radians(-self.hand_m)), orient_axis='X', orient_type='Track')
            upper_arm_L.bone.select = False

            self.frame = self.frame + self.fc  # frame = 15
            self.record(self.frame)
            self.final_result.append(self.save_coords(self.imu_data, self.frame))

            self.final_result = np.array(self.final_result)
            np.savetxt(coord_file_path, self.final_result, "%.10g")

            self.final_result = []

            self.position = "Start_walking"
        else:
            print(self.position)

    def walk_straight(self, radius, steps=0): # position 1->2
        if self.position == "Start_walking" :
            angle = radius
            self.turn(angle)

            for iteration in range(0, steps):

                shin_R.bone.select = True
                self.rsp = (math.radians(-self.shin_m)) + self.rsp
                bpy.ops.transform.rotate(value=(math.radians(-self.shin_m)), orient_axis='X', orient_type='Track')
                shin_R.bone.select = False

                thigh_R.bone.select = True
                self.rtp = (math.radians(self.thigh_m_random())) + self.rtp
                bpy.ops.transform.rotate(value=(math.radians(self.thigh_m_random())), orient_axis='X', orient_type='Track')
                thigh_R.bone.select = False

                main_spine.bone.select = True
                self.msz = (math.radians(-self.spine_m)) + self.msz
                bpy.ops.transform.translate(value=(0.0, 0.0, (math.radians(-self.spine_m))), orient_type='Track') # , orient_axis_ortho='Y'
                main_spine.bone.select = False

                upper_arm_L.bone.select = True
                self.luap = (math.radians(self.hand_m)) + self.luap
                bpy.ops.transform.rotate(value=(math.radians(self.hand_m)), orient_axis='X', orient_type='Track')
                upper_arm_L.bone.select = False

                self.frame = self.frame + random.uniform(3,5) # self.fc  # frame = 30
                self.record(self.frame)
                self.final_result.append(self.save_coords(self.imu_data, self.frame))

                thigh_L.bone.select = True
                self.ltp = (math.radians(-self.thigh_m_random())) + self.ltp
                bpy.ops.transform.rotate(value=(math.radians(-self.thigh_m_random())), orient_axis='X', orient_type='Track')
                thigh_L.bone.select = False

                main_spine.bone.select = True
                self.msz = (math.radians(self.spine_m)) + self.msz
                bpy.ops.transform.translate(value=(0.0, (math.radians(-self.thigh_m_random())), (math.radians(self.spine_m))), orient_type='Track') # , orient_axis_ortho='Y'
                main_spine.bone.select = False

                thigh_R.bone.select = True
                self.rtp = (math.radians(self.thigh_m_random())) + self.rtp
                bpy.ops.transform.rotate(value=(math.radians(self.thigh_m_random())), orient_axis='X', orient_type='Track')
                thigh_R.bone.select = False

                upper_arm_R.bone.select = True
                self.ruap = (math.radians(-self.hand_m)) + self.ruap
                bpy.ops.transform.rotate(value=(math.radians(-self.hand_m)), orient_axis='X', orient_type='Track')
                upper_arm_R.bone.select = False

                upper_arm_L.bone.select = True
                self.luap = (math.radians(self.hand_m)) + self.luap
                bpy.ops.transform.rotate(value=(math.radians(self.hand_m)), orient_axis='X', orient_type='Track')
                upper_arm_L.bone.select = False

                self.frame = self.frame + random.uniform(3,5) # self.fc  # frame = 35
                self.record(self.frame)
                self.final_result.append(self.save_coords(self.imu_data, self.frame))

                thigh_L.bone.select = True
                self.ltp = (math.radians(-self.thigh_m_random())) + self.ltp
                bpy.ops.transform.rotate(value=(math.radians(-self.thigh_m_random())), orient_axis='X', orient_type='Track')
                thigh_L.bone.select = False

                main_spine.bone.select = True
                self.msz = (math.radians(self.spine_m)) + self.msz
                bpy.ops.transform.translate(value=(0.0, (math.radians(-self.thigh_m_random())), (math.radians(self.spine_m))), orient_type='Track') # , orient_axis_ortho='Y'
                main_spine.bone.select = False

                upper_arm_R.bone.select = True
                self.ruap = (math.radians(-self.hand_m)) + self.ruap
                bpy.ops.transform.rotate(value=(math.radians(-self.hand_m)), orient_axis='X', orient_type='Track')
                upper_arm_R.bone.select = False

                forearm_R.bone.select = True
                self.rfap = (math.radians(-self.hand_m)) + self.rfap
                bpy.ops.transform.rotate(value=(math.radians(-self.hand_m)), orient_axis='X', orient_type='Track')
                forearm_R.bone.select = False

                self.frame = self.frame + random.uniform(3,5) # self.fc  # frame = 40
                self.record(self.frame)
                ###final_result.append(save_coords(imu_data, frame))

                thigh_L.bone.select = True
                self.ltp = (math.radians(-self.thigh_m_random())) + self.ltp
                bpy.ops.transform.rotate(value=(math.radians(-self.thigh_m_random())), orient_axis='X', orient_type='Track')
                thigh_L.bone.select = False

                main_spine.bone.select = True
                self.msz = (math.radians(-self.spine_m)) + self.msz
                bpy.ops.transform.translate(value=(0.0, (math.radians(-self.thigh_m_random())), (math.radians(-self.spine_m))), orient_type='Track') # , orient_axis_ortho='Y'
                main_spine.bone.select = False

                thigh_R.bone.select = True
                self.rtp = (math.radians(self.thigh_m_random())) + self.rtp
                bpy.ops.transform.rotate(value=(math.radians(self.thigh_m_random())), orient_axis='X', orient_type='Track')
                thigh_R.bone.select = False

                shin_R.bone.select = True
                self.rsp = (math.radians(self.shin_m)) + self.rsp
                bpy.ops.transform.rotate(value=(math.radians(self.shin_m)), orient_axis='X', orient_type='Track')
                shin_R.bone.select = False

                upper_arm_L.bone.select = True
                self.luap = (math.radians(self.hand_m)) + self.luap
                bpy.ops.transform.rotate(value=(math.radians(self.hand_m)), orient_axis='X', orient_type='Track')
                upper_arm_L.bone.select = False

                forearm_L.bone.select = True
                self.lfap = (math.radians(self.hand_m)) + self.lfap
                bpy.ops.transform.rotate(value=(math.radians(self.hand_m)), orient_axis='X', orient_type='Track')
                forearm_L.bone.select = False

                upper_arm_R.bone.select = True
                self.ruap = (math.radians(self.hand_m)) + self.ruap
                bpy.ops.transform.rotate(value=(math.radians(self.hand_m)), orient_axis='X', orient_type='Track')
                upper_arm_R.bone.select = False

                # relying on the right leg

                self.frame = self.frame + random.uniform(3,5) # self.fc  # frame = 45
                self.record(self.frame)
                ###final_result.append(save_coords(imu_data, frame))

                thigh_L.bone.select = True
                self.ltp = (math.radians(self.thigh_m_random())) + self.ltp
                bpy.ops.transform.rotate(value=(math.radians(self.thigh_m_random())), orient_axis='X', orient_type='Track')
                thigh_L.bone.select = False

                shin_L.bone.select = True
                self.lsp = (math.radians(-self.shin_m)) + self.lsp
                bpy.ops.transform.rotate(value=(math.radians(-self.shin_m)), orient_axis='X', orient_type='Track')
                shin_L.bone.select = False

                main_spine.bone.select = True
                self.msz = (math.radians(-self.spine_m)) + self.msz
                bpy.ops.transform.translate(value=(0.0, 0.0, (math.radians(-self.spine_m))), orient_type='Track') # , orient_axis_ortho='Y'
                main_spine.bone.select = False

                upper_arm_L.bone.select = True
                self.luap = (math.radians(-self.hand_m)) + self.luap
                bpy.ops.transform.rotate(value=(math.radians(-self.hand_m)), orient_axis='X', orient_type='Track')
                upper_arm_L.bone.select = False

                forearm_R.bone.select = True
                self.rfap = (math.radians(self.hand_m)) + self.rfap
                bpy.ops.transform.rotate(value=(math.radians(self.hand_m)), orient_axis='X', orient_type='Track')
                forearm_R.bone.select = False

                upper_arm_R.bone.select = True
                self.ruap = (math.radians(self.hand_m)) + self.ruap
                bpy.ops.transform.rotate(value=(math.radians(self.hand_m)), orient_axis='X', orient_type='Track')
                upper_arm_R.bone.select = False

                self.frame = self.frame + random.uniform(3,5) # self.fc  # frame = 50
                self.record(self.frame)
                self.final_result.append(self.save_coords(self.imu_data, self.frame))

                thigh_R.bone.select = True
                self.rtp = (math.radians(-self.thigh_m_random())) + self.rtp
                bpy.ops.transform.rotate(value=(math.radians(-self.thigh_m_random())), orient_axis='X', orient_type='Track')
                thigh_R.bone.select = False

                main_spine.bone.select = True
                self.msz = (math.radians(self.spine_m)) + self.msz
                bpy.ops.transform.translate(value=(0.0, (math.radians(-self.thigh_m_random())), (math.radians(self.spine_m))), orient_type='Track') # , orient_axis_ortho='Y'
                main_spine.bone.select = False

                upper_arm_L.bone.select = True
                self.luap = (math.radians(-self.hand_m)) + self.luap
                bpy.ops.transform.rotate(value=(math.radians(-self.hand_m)), orient_axis='X', orient_type='Track')
                upper_arm_L.bone.select = False

                forearm_L.bone.select = True
                self.lfap = (math.radians(-self.hand_m)) + self.lfap
                bpy.ops.transform.rotate(value=(math.radians(-self.hand_m)), orient_axis='X', orient_type='Track')
                forearm_L.bone.select = False

                forearm_R.bone.select = True
                self.rfap = (math.radians(-self.hand_m)) + self.rfap
                bpy.ops.transform.rotate(value=(math.radians(-self.hand_m)), orient_axis='X', orient_type='Track')
                forearm_R.bone.select = False

                upper_arm_R.bone.select = True
                self.ruap = (math.radians(self.hand_m)) + self.ruap
                bpy.ops.transform.rotate(value=(math.radians(self.hand_m)), orient_axis='X', orient_type='Track')
                upper_arm_R.bone.select = False

                self.frame = self.frame + random.uniform(3,5) # self.fc  # frame = 55
                self.record(self.frame)
                self.final_result.append(self.save_coords(self.imu_data, self.frame))

                thigh_R.bone.select = True
                self.rtp = (math.radians(-self.thigh_m_random())) + self.rtp
                bpy.ops.transform.rotate(value=(math.radians(-self.thigh_m_random())), orient_axis='X', orient_type='Track')
                thigh_R.bone.select = False

                main_spine.bone.select = True
                self.msz = (math.radians(self.spine_m)) + self.msz
                bpy.ops.transform.translate(value=(0.0, (math.radians(-self.thigh_m_random())), (math.radians(self.spine_m))), orient_type='Track') # , orient_axis_ortho='Y'
                main_spine.bone.select = False

                thigh_L.bone.select = True
                self.ltp = (math.radians(self.thigh_m_random())) + self.ltp
                bpy.ops.transform.rotate(value=(math.radians(self.thigh_m_random())), orient_axis='X', orient_type='Track')
                thigh_L.bone.select = False

                upper_arm_L.bone.select = True
                self.luap = (math.radians(-self.hand_m)) + self.luap
                bpy.ops.transform.rotate(value=(math.radians(-self.hand_m)), orient_axis='X', orient_type='Track')
                upper_arm_L.bone.select = False

                # upper_arm_R.bone.select = True
                # ruap = (math.radians(-hand_m)) + ruap
                # bpy.ops.transform.rotate(value=(math.radians(-hand_m)), orient_axis='X')
                # upper_arm_R.bone.select = False

                self.frame = self.frame + random.uniform(3,5) # self.fc  # frame = 60
                self.record(self.frame)
                self.final_result.append(self.save_coords(self.imu_data, self.frame))

                thigh_R.bone.select = True
                self.rtp = (math.radians(-self.thigh_m_random())) + self.rtp
                bpy.ops.transform.rotate(value=(math.radians(-self.thigh_m_random())), orient_axis='X', orient_type='Track')
                thigh_R.bone.select = False

                main_spine.bone.select = True
                self.msz = (math.radians(-self.spine_m)) + self.msz
                bpy.ops.transform.translate(value=(0.0, (math.radians(-self.thigh_m_random())), (math.radians(-self.spine_m))), orient_type='Track') # , orient_axis_ortho='Y'
                main_spine.bone.select = False

                thigh_L.bone.select = True
                self.ltp = (math.radians(self.thigh_m_random())) + self.ltp
                bpy.ops.transform.rotate(value=(math.radians(self.thigh_m_random())), orient_axis='X', orient_type='Track')
                thigh_L.bone.select = False

                shin_L.bone.select = True
                self.lsp = (math.radians(self.shin_m)) + self.lsp
                bpy.ops.transform.rotate(value=(math.radians(self.shin_m)), orient_axis='X', orient_type='Track')
                shin_L.bone.select = False

                upper_arm_R.bone.select = True
                self.ruap = (math.radians(-self.hand_m)) + self.ruap
                bpy.ops.transform.rotate(value=(math.radians(-self.hand_m)), orient_axis='X', orient_type='Track')
                upper_arm_R.bone.select = False

                forearm_R.bone.select = True
                self.rfap = (math.radians(self.hand_m)) + self.rfap
                bpy.ops.transform.rotate(value=(math.radians(self.hand_m)), orient_axis='X', orient_type='Track')
                forearm_R.bone.select = False

                self.frame = self.frame + random.uniform(3,5) # self.fc  # frame = 65
                self.record(self.frame)






            self.final_result = np.array(self.final_result)
            np.savetxt(coord_file_path, self.final_result, "%.10g")

            self.final_result = []
            self.position = "Walking_straight"
        else:
            print(self.position)

    def stop_walking(self): # position 2->0

        if self.position == "Walking_straight":

            bpy.ops.pose.select_all(action='SELECT')
            bpy.ops.pose.rot_clear()
            bpy.ops.pose.select_all(action='TOGGLE')

            bpy.context.object.pose.use_mirror_x = True
            bpy.data.objects['metarig'].pose.bones['upper_arm.L'].bone.select = True
            bpy.ops.transform.rotate(value=-0.5, orient_axis='Y', orient_type='Track')
            bpy.context.object.pose.use_mirror_x = False

            main_spine.bone.select = True
            bpy.ops.transform.translate(value=(0.0, (math.radians(-self.thigh_m_random())), 0.0), orient_type='Track')
            main_spine.bone.select = False



            self.frame = self.frame + self.fc +2
            self.record(self.frame)
            self.final_result.append(self.save_coords(self.imu_data, self.frame))

            self.final_result = np.array(self.final_result)
            np.savetxt(coord_file_path, self.final_result, "%.10g")

            self.rfap = 0  # right forearm position
            self.lfap = 0  # left forearm position
            self.rtp = 0  # right foot position
            self.ltp = 0  # left foot position
            self.stp = 0  # steps length
            self.rkp = 0  # right knee position
            self.lkp = 0  # left knee position
            self.lsp = 0  # left shin position
            self.rsp = 0  # right shin position
            self.msp = 0  # main spine position
            self.msz = 0  # deviation of main spine from Z axis
            self.ruap = 0  # right upper arm position
            self.luap = 0  # left upper arm position
            self.frame = self.frame + 3

            self.final_result = []

            self.position = "Standing"

        else:
            print(self.position)

    def sitting_half_raised(self): # position 0->3
        if self.position == "Standing":
            for l in range(0,3):
                thigh_L.bone.select = True
                bpy.ops.transform.rotate(value=(math.radians(26)), orient_axis = 'X')
                thigh_L.bone.select = False

                thigh_R.bone.select = True
                bpy.ops.transform.rotate(value=(math.radians(26)), orient_axis = 'X')
                thigh_R.bone.select = False


                shin_L.bone.select = True
                bpy.ops.transform.rotate(value=(math.radians(-50)), orient_axis='X')
                shin_L.bone.select = False

                shin_R.bone.select = True
                bpy.ops.transform.rotate(value=(math.radians(-50)), orient_axis='X')
                shin_R.bone.select = False

                foot_L.bone.select = True
                bpy.ops.transform.rotate(value=(math.radians(15)), orient_axis='X')
                foot_L.bone.select = False

                foot_R.bone.select = True
                bpy.ops.transform.rotate(value=(math.radians(15)), orient_axis='X')
                foot_R.bone.select = False


                if l == 0:
                    main_spine.bone.select = True
                    bpy.ops.transform.translate(value = (0.0, 0.0, (math.radians(-6))))
                    main_spine.bone.select = False
                elif l == 1:
                    main_spine.bone.select = True
                    bpy.ops.transform.translate(value=(0.0, 0.0, (math.radians(-18))))
                    main_spine.bone.select = False
                elif l == 2:
                    main_spine.bone.select = True
                    bpy.ops.transform.translate(value=(0.0, 0.0, (math.radians(-20.5))))
                    main_spine.bone.select = False

                self.frame = self.frame + random.uniform(3,5)
                self.record(self.frame)
                self.final_result.append(self.save_coords(self.imu_data, self.frame))


            self.final_result = np.array(self.final_result)
            np.savetxt(coord_file_path, self.final_result, "%.10g")
            self.final_result = []
            self.position = "Sitting_half_raised"
        else:
            print(self.position)

    def lying_down(self): # position 3->4
        if self.position == "Sitting_half_raised":

            for s in range(0,3):
                mid_spine.bone.select = True
                bpy.ops.transform.rotate(value= (math.radians(-10)), orient_axis='Z')
                mid_spine.bone.select = False

                upper_arm_L.bone.select = True
                bpy.ops.transform.rotate(value= (math.radians(10)), orient_axis='Z')
                bpy.ops.transform.rotate(value= (math.radians(-5)), orient_axis='X')
                upper_arm_L.bone.select = False


                forearm_L.bone.select = True
                bpy.ops.transform.rotate(value= (math.radians(-4)), orient_axis='X')
                forearm_L.bone.select = False


                self.record(self.frame)
                self.frame = self.frame + random.uniform(3, 5)
                self.final_result.append(self.save_coords(self.imu_data, self.frame))

            for n in range(0,3):
                main_spine.bone.select = True
                bpy.ops.transform.rotate(value= (math.radians(9)), orient_axis = 'X')
                bpy.ops.transform.translate(value= (0.0, math.radians(3.5), math.radians(-2.5)))
                main_spine.bone.select = False

                hand_L.bone.select = True
                bpy.ops.transform.rotate(value = (math.radians(-30)), orient_axis='X')
                hand_L.bone.select = False

                thigh_R.bone.select = True
                bpy.ops.transform.rotate(value= (math.radians(15)), orient_axis='X')
                thigh_R.bone.select = False

                thigh_L.bone.select = True
                bpy.ops.transform.rotate(value= (math.radians(15)), orient_axis='X')
                thigh_L.bone.select = False

                shin_L.bone.select = True
                bpy.ops.transform.rotate(value= (math.radians(6)), orient_axis= 'X')
                shin_L.bone.select = False

                shin_R.bone.select = True
                bpy.ops.transform.rotate(value= (math.radians(6)), orient_axis= 'X')
                shin_R.bone.select = False

                foot_R.bone.select = True
                bpy.ops.transform.rotate(value= (math.radians(-14)), orient_axis='X')
                foot_R.bone.select = False

                foot_L.bone.select = True
                bpy.ops.transform.rotate(value= (math.radians(-14)), orient_axis='X')
                foot_L.bone.select = False

                upper_arm_R.bone.select = True
                bpy.ops.transform.rotate(value= (math.radians(20)), orient_axis='X')
                bpy.ops.transform.rotate(value=(math.radians(10)), orient_axis='Y')
                upper_arm_R.bone.select = False





                self.record(self.frame)
                self.frame = self.frame + random.uniform(3, 5)
                self.final_result.append(self.save_coords(self.imu_data, self.frame))

            for m in range(0,3):
                upper_arm_L.bone.select = True
                bpy.ops.transform.rotate(value= (math.radians(np.random.uniform(2.75,2.77))), orient_axis='X')
                upper_arm_L.bone.select = False

                #forearm_L.bone.select = True
                #bpy.ops.transform.rotate(value = (math.radians(6)), orient_axis = 'X')
                #forearm_L.bone.select = False

                main_spine.bone.select = True
                bpy.ops.transform.rotate(value=(math.radians(np.random.uniform(1.5,1.6))), orient_axis='X')
                bpy.ops.transform.translate(value= (0.0, math.radians(np.random.uniform(0,0.25)), math.radians(np.random.uniform(0,0.25))))
                main_spine.bone.select = False

                shoulder_R.bone.select = True
                bpy.ops.transform.rotate(value=np.random.normal(-0.02, 0.01), orient_axis='Z')
                shoulder_R.bone.select = False

                shoulder_L.bone.select = True
                bpy.ops.transform.rotate(value=np.random.normal(-0.05, 0.01), orient_axis='X')
                shoulder_L.bone.select = False

                upper_arm_R.bone.select = True
                bpy.ops.transform.rotate(value= (np.random.normal(-0.1, 0.1)) , orient_axis='X')
                bpy.ops.transform.rotate(value= (np.random.normal(-0.1, 0.1)) , orient_axis='Z')
                upper_arm_R.bone.select = False


                #thigh_R.bone.select = True
                #bpy.ops.transform.rotate(value= (math.radians(2)), orient_axis='X')
                #thigh_R.bone.select = False

                #thigh_L.bone.select = True
                #bpy.ops.transform.rotate(value= (math.radians(2)), orient_axis='X')
                #thigh_L.bone.select = False

                self.record(self.frame)
                self.frame = self.frame + random.uniform(3, 5)
                self.final_result.append(self.save_coords(self.imu_data, self.frame))

            for k in range(0,3):
                shin_L.bone.select = True
                bpy.ops.transform.rotate(value= (math.radians(41)), orient_axis='X')
                shin_L.bone.select = False

                thigh_L.bone.select = True
                bpy.ops.transform.rotate(value= (math.radians(-23)), orient_axis='X')
                thigh_L.bone.select = False

                shin_R.bone.select = True
                bpy.ops.transform.rotate(value= (math.radians(np.random.uniform(5,7))), orient_axis='X')
                shin_R.bone.select = False

                thigh_R.bone.select = True
                bpy.ops.transform.rotate(value= (math.radians(np.random.uniform(-5,0))), orient_axis='X')
                thigh_R.bone.select = False

                main_spine.bone.select = True
                bpy.ops.transform.rotate(value=(math.radians(np.random.uniform(2,2.1))), orient_axis='X')
                bpy.ops.transform.translate(value= (0.0, math.radians(np.random.uniform(0,0.25)), math.radians(np.random.uniform(-0.5,-0.25))))
                main_spine.bone.select = False

                upper_arm_L.bone.select = True
                bpy.ops.transform.rotate(value= (math.radians(np.random.uniform(0,0.5))), orient_axis='X')
                upper_arm_L.bone.select = False

                forearm_L.bone.select = True
                bpy.ops.transform.rotate(value = (math.radians(np.random.uniform(1,1.5))), orient_axis = 'X')
                forearm_L.bone.select = False

                up_side.bone.select = True
                bpy.ops.transform.rotate(value = (math.radians(np.random.uniform(-2,-1.5))), orient_axis = 'X')
                up_side.bone.select = False

                mid_spine.bone.select = True
                bpy.ops.transform.rotate(value = (math.radians(np.random.uniform(-2,-1.5))), orient_axis = 'X')
                mid_spine.bone.select = False

                upper_arm_R.bone.select = True
                bpy.ops.transform.rotate(value= (math.radians(5)), orient_axis='X')
                bpy.ops.transform.rotate(value=(math.radians(15)), orient_axis='Z')
                upper_arm_R.bone.select = False

                self.record(self.frame)
                self.frame = self.frame + random.uniform(3, 5)
                self.final_result.append(self.save_coords(self.imu_data, self.frame))

            for o in range(0,3):

                shin_R.bone.select = True
                bpy.ops.transform.rotate(value= (math.radians(40)), orient_axis='X')
                shin_R.bone.select = False

                thigh_R.bone.select = True
                bpy.ops.transform.rotate(value= (math.radians(-19)), orient_axis='X')
                thigh_R.bone.select = False

                shin_L.bone.select = True
                bpy.ops.transform.rotate(value= (math.radians(5)), orient_axis='X')
                shin_L.bone.select = False

                thigh_L.bone.select = True
                bpy.ops.transform.rotate(value= (math.radians(1.8)), orient_axis='X')
                thigh_L.bone.select = False

                main_spine.bone.select = True
                bpy.ops.transform.rotate(value=(math.radians(np.random.uniform(-4.1,-4.0))), orient_axis='X')
                bpy.ops.transform.translate(value= (0.0, math.radians(np.random.uniform(0,0.25)), math.radians(np.random.uniform(-0.75,-0.5))))
                main_spine.bone.select = False

                upper_arm_R.bone.select = True
                bpy.ops.transform.rotate(value= (math.radians(-25)), orient_axis='X')
                #bpy.ops.transform.rotate(value=(math.radians(15)), orient_axis='Z')
                upper_arm_R.bone.select = False

                mid_spine.bone.select = True
                bpy.ops.transform.rotate(value= (math.radians(10)), orient_axis='Z')
                bpy.ops.transform.rotate(value= (math.radians(3)), orient_axis='Y')
                mid_spine.bone.select = False

                hand_L.bone.select = True
                bpy.ops.transform.rotate(value = (math.radians(30)), orient_axis='X')
                hand_L.bone.select = False


                self.record(self.frame)
                self.frame = self.frame + random.uniform(3, 5)
                self.final_result.append(self.save_coords(self.imu_data, self.frame))

            for last in range(0,3):
                main_spine.bone.select = True
                bpy.ops.transform.rotate(value=(math.radians(21.5)), orient_axis='X')
                main_spine.bone.select = False

                upper_arm_R.bone.select = True
                bpy.ops.transform.rotate(value= (math.radians(12)), orient_axis='X')
                upper_arm_R.bone.select = False

                upper_arm_L.bone.select = True
                bpy.ops.transform.rotate(value= (math.radians(10)), orient_axis='X')
                upper_arm_L.bone.select = False

                forearm_L.bone.select = True
                bpy.ops.transform.rotate(value = (math.radians(np.random.uniform(5,6))), orient_axis = 'X')
                forearm_L.bone.select = False

                forearm_R.bone.select = True
                bpy.ops.transform.rotate(value = (math.radians(np.random.uniform(5,6))), orient_axis = 'X')
                forearm_R.bone.select = False

                thigh_R.bone.select = True
                bpy.ops.transform.rotate(value= (math.radians(-22)), orient_axis='X')
                thigh_R.bone.select = False

                thigh_L.bone.select = True
                bpy.ops.transform.rotate(value= (math.radians(-22)), orient_axis='X')
                thigh_L.bone.select = False

                self.record(self.frame)
                self.frame = self.frame + random.uniform(3, 5)
                self.final_result.append(self.save_coords(self.imu_data, self.frame))

            for stable in self.parts:
                stable.bone.select = True
                bpy.ops.pose.rot_clear()
                stable.bone.select = False

            self.record(self.frame)
            self.frame = self.frame + random.uniform(1,2)
            self.final_result.append(self.save_coords(self.imu_data, self.frame))

            self.final_result = np.array(self.final_result)
            np.savetxt(coord_file_path, self.final_result, "%.10g")
            self.final_result =[]
            self.position = "Lying_down"

        else:
            print(self.position)

    def standing_from_lying(self): # position 4->0
        if self.position == "Lying_down":

            bpy.context.object.pose.use_mirror_x = True
            upper_arm_L.bone.select = True
            bpy.ops.transform.rotate(value=0.5, orient_axis='Z')
            bpy.context.object.pose.use_mirror_x = False

            for first in range(0,3):
                main_spine.bone.select = True
                bpy.ops.transform.rotate(value=(math.radians(-21.5)), orient_axis='X')
                main_spine.bone.select = False

                upper_arm_R.bone.select = True
                bpy.ops.transform.rotate(value= (math.radians(np.random.uniform(10,12))), orient_axis='X')
                upper_arm_R.bone.select = False

                upper_arm_L.bone.select = True
                bpy.ops.transform.rotate(value= (math.radians(np.random.uniform(10,12))), orient_axis='X')
                upper_arm_L.bone.select = False

                forearm_L.bone.select = True
                bpy.ops.transform.rotate(value = (math.radians(np.random.uniform(-6,-5))), orient_axis = 'X')
                forearm_L.bone.select = False

                forearm_R.bone.select = True
                bpy.ops.transform.rotate(value = (math.radians(np.random.uniform(-6,-5))), orient_axis = 'X')
                forearm_R.bone.select = False

                thigh_R.bone.select = True
                bpy.ops.transform.rotate(value= (math.radians(22)), orient_axis='X')
                thigh_R.bone.select = False

                thigh_L.bone.select = True
                bpy.ops.transform.rotate(value= (math.radians(22)), orient_axis='X')
                thigh_L.bone.select = False

                self.record(self.frame)
                self.frame = self.frame + random.uniform(3, 5)
                self.final_result.append(self.save_coords(self.imu_data, self.frame))

            for mid in range(0,6):

                upper_arm_R.bone.select = True
                bpy.ops.transform.rotate(value= (math.radians(np.random.uniform(-12,-10))), orient_axis='X')
                upper_arm_R.bone.select = False

                upper_arm_L.bone.select = True
                bpy.ops.transform.rotate(value= (math.radians(np.random.uniform(-12,-10))), orient_axis='X')
                upper_arm_L.bone.select = False

                forearm_L.bone.select = True
                bpy.ops.transform.rotate(value = (math.radians(np.random.uniform(1,2))), orient_axis = 'X')
                forearm_L.bone.select = False

                forearm_R.bone.select = True
                bpy.ops.transform.rotate(value = (math.radians(np.random.uniform(1,2))), orient_axis = 'X')
                forearm_R.bone.select = False

                self.record(self.frame)
                self.frame = self.frame + random.uniform(1, 2)



            for second in range(0, 3):

                shoulder_L.bone.select = True
                bpy.ops.transform.rotate(value=np.random.normal(-0.05, 0.01), orient_axis='X')
                shoulder_L.bone.select = False

                shin_R.bone.select = True
                bpy.ops.transform.rotate(value=(math.radians(-40)), orient_axis='X')
                shin_R.bone.select = False

                thigh_R.bone.select = True
                bpy.ops.transform.rotate(value=(math.radians(19)), orient_axis='X')
                thigh_R.bone.select = False

                shin_L.bone.select = True
                bpy.ops.transform.rotate(value=(math.radians(-5)), orient_axis='X')
                shin_L.bone.select = False

                thigh_L.bone.select = True
                bpy.ops.transform.rotate(value=(math.radians(-1.8)), orient_axis='X')
                thigh_L.bone.select = False

                main_spine.bone.select = True
                bpy.ops.transform.rotate(value=(math.radians(np.random.uniform(4.0, 4.1))), orient_axis='X')
                bpy.ops.transform.translate(value=(0.0, math.radians(np.random.uniform(-0.25,0.0)), math.radians(np.random.uniform(0.5, 0.75))))
                main_spine.bone.select = False

                upper_arm_R.bone.select = True
                bpy.ops.transform.rotate(value=(math.radians(25)), orient_axis='X')
                # bpy.ops.transform.rotate(value=(math.radians(15)), orient_axis='Z')
                upper_arm_R.bone.select = False

                mid_spine.bone.select = True
                bpy.ops.transform.rotate(value=(math.radians(-11)), orient_axis='Z')
                bpy.ops.transform.rotate(value=(math.radians(-4)), orient_axis='Y')
                mid_spine.bone.select = False

                hand_L.bone.select = True
                bpy.ops.transform.rotate(value=(math.radians(-30)), orient_axis='X')
                hand_L.bone.select = False

                self.record(self.frame)
                self.frame = self.frame + random.uniform(3, 5)
                self.final_result.append(self.save_coords(self.imu_data, self.frame))

            for third in range(0,3):
                shin_L.bone.select = True
                bpy.ops.transform.rotate(value= (math.radians(-41)), orient_axis='X')
                shin_L.bone.select = False

                thigh_L.bone.select = True
                bpy.ops.transform.rotate(value= (math.radians(23)), orient_axis='X')
                thigh_L.bone.select = False

                shin_R.bone.select = True
                bpy.ops.transform.rotate(value= (math.radians(np.random.uniform(-7,-5))), orient_axis='X')
                shin_R.bone.select = False

                thigh_R.bone.select = True
                bpy.ops.transform.rotate(value= (math.radians(np.random.uniform(0,5))), orient_axis='X')
                thigh_R.bone.select = False

                main_spine.bone.select = True
                bpy.ops.transform.rotate(value=(math.radians(np.random.uniform(-2.1,-2.0))), orient_axis='X')
                bpy.ops.transform.translate(value= (0.0, math.radians(np.random.uniform(-0.25,0.0)), math.radians(np.random.uniform(0.25,0.5))))
                main_spine.bone.select = False

                upper_arm_L.bone.select = True
                bpy.ops.transform.rotate(value= (math.radians(np.random.uniform(-0.5,0.0))), orient_axis='X')
                upper_arm_L.bone.select = False

                forearm_L.bone.select = True
                bpy.ops.transform.rotate(value = (math.radians(np.random.uniform(-1.5,-1))), orient_axis = 'X')
                forearm_L.bone.select = False

                up_side.bone.select = True
                bpy.ops.transform.rotate(value = (math.radians(np.random.uniform(1.5,2))), orient_axis = 'X')
                up_side.bone.select = False

                mid_spine.bone.select = True
                bpy.ops.transform.rotate(value = (math.radians(np.random.uniform(1.5,2))), orient_axis = 'X')
                mid_spine.bone.select = False

                upper_arm_R.bone.select = True
                bpy.ops.transform.rotate(value= (math.radians(5)), orient_axis='X')
                bpy.ops.transform.rotate(value=(math.radians(15)), orient_axis='Z')
                upper_arm_R.bone.select = False

                self.record(self.frame)
                self.frame = self.frame + random.uniform(3, 5)
                self.final_result.append(self.save_coords(self.imu_data, self.frame))

            for fourth in range(0,3):
                upper_arm_L.bone.select = True
                bpy.ops.transform.rotate(value= (math.radians(np.random.uniform(-2.5,-2.6))), orient_axis='X')
                upper_arm_L.bone.select = False

                forearm_L.bone.select = True
                bpy.ops.transform.rotate(value = (math.radians(6)), orient_axis = 'X')
                forearm_L.bone.select = False

                main_spine.bone.select = True
                bpy.ops.transform.rotate(value=(math.radians(np.random.uniform(-1.6,-1.5))), orient_axis='X')
                bpy.ops.transform.translate(value= (0.0, math.radians(np.random.uniform(-0.25,0.0)), math.radians(np.random.uniform(-0.25,0.0))))
                main_spine.bone.select = False

                shoulder_R.bone.select = True
                bpy.ops.transform.rotate(value=np.random.normal(-0.02, 0.01), orient_axis='Z')
                shoulder_R.bone.select = False

                #shoulder_L.bone.select = True
                #bpy.ops.transform.rotate(value=np.random.normal(-0.05, 0.01), orient_axis='X')
                #shoulder_L.bone.select = False

                upper_arm_R.bone.select = True
                bpy.ops.transform.rotate(value= (np.random.normal(-0.1, 0.1)) , orient_axis='X')
                bpy.ops.transform.rotate(value= (np.random.normal(-0.1, 0.1)) , orient_axis='Z')
                upper_arm_R.bone.select = False


                self.record(self.frame)
                self.frame = self.frame + random.uniform(3, 5)
                self.final_result.append(self.save_coords(self.imu_data, self.frame))

            for fifth in range(0,3):
                main_spine.bone.select = True
                bpy.ops.transform.rotate(value= (math.radians(-9)), orient_axis = 'X')
                bpy.ops.transform.translate(value= (0.0, math.radians(-3.5), math.radians(1.8)))
                main_spine.bone.select = False

                hand_L.bone.select = True
                bpy.ops.transform.rotate(value = (math.radians(30)), orient_axis='X')
                hand_L.bone.select = False

                thigh_R.bone.select = True
                bpy.ops.transform.rotate(value= (math.radians(-15)), orient_axis='X')
                thigh_R.bone.select = False

                thigh_L.bone.select = True
                bpy.ops.transform.rotate(value= (math.radians(-15)), orient_axis='X')
                thigh_L.bone.select = False

                shin_L.bone.select = True
                bpy.ops.transform.rotate(value= (math.radians(-6)), orient_axis= 'X')
                shin_L.bone.select = False

                shin_R.bone.select = True
                bpy.ops.transform.rotate(value= (math.radians(-6)), orient_axis= 'X')
                shin_R.bone.select = False

                foot_R.bone.select = True
                bpy.ops.transform.rotate(value= (math.radians(14)), orient_axis='X')
                foot_R.bone.select = False

                foot_L.bone.select = True
                bpy.ops.transform.rotate(value= (math.radians(14)), orient_axis='X')
                foot_L.bone.select = False

                upper_arm_R.bone.select = True
                bpy.ops.transform.rotate(value= (math.radians(-20)), orient_axis='X')
                bpy.ops.transform.rotate(value=(math.radians(-10)), orient_axis='Y')
                upper_arm_R.bone.select = False

                upper_arm_L.bone.select = True
                bpy.ops.transform.rotate(value= (math.radians(np.random.uniform(2.5,2.6))), orient_axis='X')
                upper_arm_L.bone.select = False

                forearm_L.bone.select = True
                bpy.ops.transform.rotate(value = (math.radians(-6)), orient_axis = 'X')
                forearm_L.bone.select = False


                self.record(self.frame)
                self.frame = self.frame + random.uniform(3, 5)
                self.final_result.append(self.save_coords(self.imu_data, self.frame))

            for before_standing in range(0,3):
                mid_spine.bone.select = True
                bpy.ops.transform.rotate(value= (math.radians(10)), orient_axis='Z')
                mid_spine.bone.select = False

                upper_arm_L.bone.select = True
                bpy.ops.transform.rotate(value= (math.radians(-10)), orient_axis='Z')
                bpy.ops.transform.rotate(value= (math.radians(5)), orient_axis='X')
                upper_arm_L.bone.select = False


                forearm_L.bone.select = True
                bpy.ops.transform.rotate(value= (math.radians(4)), orient_axis='X')
                forearm_L.bone.select = False


                self.record(self.frame)
                self.frame = self.frame + random.uniform(3, 5)
                self.final_result.append(self.save_coords(self.imu_data, self.frame))

            for upper in self.upper_side:
                upper.bone.select = True
                bpy.ops.pose.rot_clear()
                upper.bone.select = False

            bpy.context.object.pose.use_mirror_x = True
            upper_arm_L.bone.select = True
            bpy.ops.transform.rotate(value=-0.5, orient_axis='Y')
            bpy.context.object.pose.use_mirror_x = False

            self.record(self.frame)
            self.frame = self.frame + random.uniform(3, 5)
            self.final_result.append(self.save_coords(self.imu_data, self.frame))

            for sixth in range(0,3):
                thigh_L.bone.select = True
                bpy.ops.transform.rotate(value=(math.radians(-26)), orient_axis = 'X')
                thigh_L.bone.select = False

                thigh_R.bone.select = True
                bpy.ops.transform.rotate(value=(math.radians(-26)), orient_axis = 'X')
                thigh_R.bone.select = False


                shin_L.bone.select = True
                bpy.ops.transform.rotate(value=(math.radians(50)), orient_axis='X')
                shin_L.bone.select = False

                shin_R.bone.select = True
                bpy.ops.transform.rotate(value=(math.radians(50)), orient_axis='X')
                shin_R.bone.select = False

                foot_L.bone.select = True
                bpy.ops.transform.rotate(value=(math.radians(-15)), orient_axis='X')
                foot_L.bone.select = False

                foot_R.bone.select = True
                bpy.ops.transform.rotate(value=(math.radians(-15)), orient_axis='X')
                foot_R.bone.select = False


                if sixth == 0:
                    main_spine.bone.select = True
                    bpy.ops.transform.translate(value=(0.0,(math.radians(3.25)), (math.radians(20.5))))
                    main_spine.bone.select = False
                elif sixth == 1:
                    main_spine.bone.select = True
                    bpy.ops.transform.translate(value=(0.0,(math.radians(-4.25)), (math.radians(18))))
                    main_spine.bone.select = False
                elif sixth == 2:
                    main_spine.bone.select = True
                    bpy.ops.transform.translate(value = (0.0,(math.radians(-2.75)), (math.radians(9))))
                    main_spine.bone.select = False



                self.frame = self.frame + random.uniform(3,5)
                self.record(self.frame)
                self.final_result.append(self.save_coords(self.imu_data, self.frame))

            for each in self.parts:
                each.bone.select = True
                bpy.ops.pose.rot_clear()
                each.bone.select = False

            bpy.context.object.pose.use_mirror_x = True
            upper_arm_L.bone.select = True
            bpy.ops.transform.rotate(value=-0.5, orient_axis='Y')
            bpy.context.object.pose.use_mirror_x = False

            self.record(self.frame)
            self.frame = self.frame + random.uniform(3, 5)
            self.final_result.append(self.save_coords(self.imu_data, self.frame))


            self.final_result = np.array(self.final_result)
            np.savetxt(coord_file_path, self.final_result, "%.10g")
            self.final_result = []
            self.position = "Standing"
        else:
            print(self.position)

    def standing_from_half_raised(self):
        if self.position == "Sitting_half_raised":

            for stand in range(0,3):
                thigh_L.bone.select = True
                bpy.ops.transform.rotate(value=(math.radians(-26)), orient_axis = 'X')
                thigh_L.bone.select = False

                thigh_R.bone.select = True
                bpy.ops.transform.rotate(value=(math.radians(-26)), orient_axis = 'X')
                thigh_R.bone.select = False


                shin_L.bone.select = True
                bpy.ops.transform.rotate(value=(math.radians(50)), orient_axis='X')
                shin_L.bone.select = False

                shin_R.bone.select = True
                bpy.ops.transform.rotate(value=(math.radians(50)), orient_axis='X')
                shin_R.bone.select = False

                foot_L.bone.select = True
                bpy.ops.transform.rotate(value=(math.radians(-15)), orient_axis='X')
                foot_L.bone.select = False

                foot_R.bone.select = True
                bpy.ops.transform.rotate(value=(math.radians(-15)), orient_axis='X')
                foot_R.bone.select = False

                if stand == 0:
                    main_spine.bone.select = True
                    bpy.ops.transform.translate(value=(0.0,(math.radians(3.25)), (math.radians(18.5))))
                    main_spine.bone.select = False
                elif stand == 1:
                    main_spine.bone.select = True
                    bpy.ops.transform.translate(value=(0.0,(math.radians(-4.25)), (math.radians(18))))
                    main_spine.bone.select = False
                elif stand == 2:
                    main_spine.bone.select = True
                    bpy.ops.transform.translate(value = (0.0,(math.radians(-2.75)), (math.radians(9))))
                    main_spine.bone.select = False

                self.frame = self.frame + random.uniform(3, 5)
                self.record(self.frame)
                self.final_result.append(self.save_coords(self.imu_data, self.frame))

            for each in self.parts:
                each.bone.select = True
                bpy.ops.pose.rot_clear()
                each.bone.select = False

            bpy.context.object.pose.use_mirror_x = True
            upper_arm_L.bone.select = True
            bpy.ops.transform.rotate(value=-0.5, orient_axis='Y')
            bpy.context.object.pose.use_mirror_x = False

            self.record(self.frame)
            self.frame = self.frame + random.uniform(3, 5)
            self.final_result.append(self.save_coords(self.imu_data, self.frame))

            self.final_result = np.array(self.final_result)
            np.savetxt(coord_file_path, self.final_result, "%.10g")
            self.final_result = []

            self.position = "Standing"

        else:
            print(self.position)



    def sitting_in_fron_of_a_table(self):
        if self.position == "Standing":
            for l in range(0,3):
                thigh_L.bone.select = True
                bpy.ops.transform.rotate(value=(math.radians(26)), orient_axis = 'X')
                thigh_L.bone.select = False

                thigh_R.bone.select = True
                bpy.ops.transform.rotate(value=(math.radians(26)), orient_axis = 'X')
                thigh_R.bone.select = False


                shin_L.bone.select = True
                bpy.ops.transform.rotate(value=(math.radians(-26)), orient_axis='X')
                shin_L.bone.select = False

                shin_R.bone.select = True
                bpy.ops.transform.rotate(value=(math.radians(-26)), orient_axis='X')
                shin_R.bone.select = False

                foot_L.bone.select = True
                bpy.ops.transform.rotate(value=(math.radians(1)), orient_axis='X')
                foot_L.bone.select = False

                foot_R.bone.select = True
                bpy.ops.transform.rotate(value=(math.radians(1)), orient_axis='X')
                foot_R.bone.select = False

                mid_spine.bone.select = True
                bpy.ops.transform.rotate(value=(math.radians(np.random.uniform(-3.5, -4.1))), orient_axis='X')
                mid_spine.bone.select = False

                up_side.bone.select = True
                bpy.ops.transform.rotate(value=(math.radians(np.random.uniform(-3.5, -4.1))), orient_axis='X')
                up_side.bone.select = False

                upper_arm_L.bone.select = True
                bpy.ops.transform.rotate(value=(math.radians(np.random.uniform(10, 12))), orient_axis='X')
                upper_arm_L.bone.select = False

                upper_arm_R.bone.select = True
                bpy.ops.transform.rotate(value=(math.radians(np.random.uniform(10, 12))), orient_axis='X')
                upper_arm_R.bone.select = False




                if l == 0:
                    main_spine.bone.select = True
                    bpy.ops.transform.translate(value = (0.0, (math.radians(12)), (math.radians(-6))))
                    main_spine.bone.select = False
                elif l == 1:
                    main_spine.bone.select = True
                    bpy.ops.transform.translate(value=(0.0, (math.radians(10)), (math.radians(-8))))
                    main_spine.bone.select = False
                elif l == 2:
                    main_spine.bone.select = True
                    bpy.ops.transform.translate(value=(0.0, (math.radians(5)), (math.radians(-13))))
                    main_spine.bone.select = False

                self.frame = self.frame + random.uniform(3,5)
                self.record(self.frame)
                self.final_result.append(self.save_coords(self.imu_data, self.frame))

            mid_spine.bone.select = True
            bpy.ops.pose.rot_clear()
            mid_spine.bone.select = False

            up_side.bone.select = True
            bpy.ops.pose.rot_clear()
            up_side.bone.select = False

            upper_arm_L.bone.select = True
            bpy.ops.pose.rot_clear()
            upper_arm_L.bone.select = False

            upper_arm_R.bone.select = True
            bpy.ops.pose.rot_clear()
            upper_arm_R.bone.select = False

            bpy.context.object.pose.use_mirror_x = True
            upper_arm_L.bone.select = True
            bpy.ops.transform.rotate(value=-0.5, orient_axis='Y')
            bpy.context.object.pose.use_mirror_x = False

            self.frame = self.frame + random.uniform(5, 7)
            self.record(self.frame)
            self.final_result.append(self.save_coords(self.imu_data, self.frame))

            self.position = "Sitting_in_front_of_a_table"

        else:
            print(self.position)




    def standing_in_fron_of_a_table(self):
        if self.position == "Sitting_in_front_of_a_table":
            for l in range(0, 3):
                thigh_L.bone.select = True
                bpy.ops.transform.rotate(value=(math.radians(-26)), orient_axis='X')
                thigh_L.bone.select = False

                thigh_R.bone.select = True
                bpy.ops.transform.rotate(value=(math.radians(-26)), orient_axis='X')
                thigh_R.bone.select = False

                shin_L.bone.select = True
                bpy.ops.transform.rotate(value=(math.radians(26)), orient_axis='X')
                shin_L.bone.select = False

                shin_R.bone.select = True
                bpy.ops.transform.rotate(value=(math.radians(26)), orient_axis='X')
                shin_R.bone.select = False

                foot_L.bone.select = True
                bpy.ops.transform.rotate(value=(math.radians(1)), orient_axis='X')
                foot_L.bone.select = False

                foot_R.bone.select = True
                bpy.ops.transform.rotate(value=(math.radians(1)), orient_axis='X')
                foot_R.bone.select = False

                mid_spine.bone.select = True
                bpy.ops.transform.rotate(value=(math.radians(np.random.uniform(-3.5, -4.1))), orient_axis='X')
                mid_spine.bone.select = False

                up_side.bone.select = True
                bpy.ops.transform.rotate(value=(math.radians(np.random.uniform(-3.5, -4.1))), orient_axis='X')
                up_side.bone.select = False

                upper_arm_L.bone.select = True
                bpy.ops.transform.rotate(value=(math.radians(np.random.uniform(10, 12))), orient_axis='X')
                upper_arm_L.bone.select = False

                upper_arm_R.bone.select = True
                bpy.ops.transform.rotate(value=(math.radians(np.random.uniform(10, 12))), orient_axis='X')
                upper_arm_R.bone.select = False

                if l == 2:
                    main_spine.bone.select = True
                    bpy.ops.transform.translate(value=(0.0, (math.radians(-12)), (math.radians(6))))
                    main_spine.bone.select = False
                elif l == 1:
                    main_spine.bone.select = True
                    bpy.ops.transform.translate(value=(0.0, (math.radians(-10)), (math.radians(8))))
                    main_spine.bone.select = False
                elif l == 0:
                    main_spine.bone.select = True
                    bpy.ops.transform.translate(value=(0.0, (math.radians(-5)), (math.radians(13))))
                    main_spine.bone.select = False

                self.frame = self.frame + random.uniform(3, 5)
                self.record(self.frame)
                self.final_result.append(self.save_coords(self.imu_data, self.frame))

            mid_spine.bone.select = True
            bpy.ops.pose.rot_clear()
            mid_spine.bone.select = False

            up_side.bone.select = True
            bpy.ops.pose.rot_clear()
            up_side.bone.select = False

            upper_arm_L.bone.select = True
            bpy.ops.pose.rot_clear()
            upper_arm_L.bone.select = False

            upper_arm_R.bone.select = True
            bpy.ops.pose.rot_clear()
            upper_arm_R.bone.select = False

            bpy.context.object.pose.use_mirror_x = True
            upper_arm_L.bone.select = True
            bpy.ops.transform.rotate(value=-0.5, orient_axis='Y')
            bpy.context.object.pose.use_mirror_x = False
            self.position = "Standing"
        else:
            print(self.position)

    def _crossing_legs(self):
        pass

    def _crossing_arms(self):
        pass

    def _looking_around(self):

        neck.bone.select = True
        bpy.ops.transform.rotate(value=(math.radians(np.random.uniform(40, 45))), orient_axis='Z')
        neck.bone.select = False

        self.frame = self.frame + random.uniform(7, 10)
        self.record(self.frame)
        self.final_result.append(self.save_coords(self.imu_data, self.frame))

        neck.bone.select = True
        bpy.ops.transform.rotate(value=(math.radians(np.random.uniform(-80, -75))), orient_axis='Z')
        neck.bone.select = False

        self.frame = self.frame + random.uniform(15, 20)
        self.record(self.frame)
        self.final_result.append(self.save_coords(self.imu_data, self.frame))

        neck.bone.select = True
        bpy.ops.pose.rot_clear()
        neck.bone.select = False

        self.frame = self.frame + random.uniform(7, 10)
        self.record(self.frame)
        self.final_result.append(self.save_coords(self.imu_data, self.frame))





new = Person(0.66, 5)
new.start_walking()
new.walk_straight(15, 5)
new.stop_walking()

new.wait(6)

new.start_walking()
new.walk_straight(0, 5)
new.stop_walking()




## we need some idle state activites in lying down or standing or sitting in front of the table. therefore we can use the wait method and include or add a random movements like look around (moving the head) then cross the arms in front of the torso, crossing the legs if it is in the lying position
## the condition of wait method should be consider the time to run the idle mode