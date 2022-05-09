import numpy as np
from scipy.interpolate import interp1d
from scipy.misc import derivative
import os


file_path = "D:\\Codes\\Blender\\final_files\\acc.txt"
if os.path.isfile(file_path):
    os.remove(file_path)

data = np.loadtxt("D:\\Codes\\Blender\\final_files\\coordinates.txt")

head_location = data[ : , :3]
head_rot = data[ : , 3:12]

neck_location = data[ : , 12:15]
neck_rot = data[ : , 15:24]

main_spine_location = data[ : , 24:27]
main_spine_rot = data[ : , 27:36]

upper_arm_L_location = data[ : , 36:39]
upper_arm_L_rot = data[ : , 39:48]

forearm_L_location = data[ : , 48:51]
forearm_L_rot = data[ : , 51:60]

upper_arm_R_location = data[ : , 60:63]
upper_arm_R_rot = data[ : , 63:72]

forearm_R_location = data[ : , 72:75]
forearm_R_rot = data[ : , 75:84]

thigh_L_location = data[ : , 84:87]
thigh_L_rot = data[ : , 87:96]

shin_L_location = data[ : , 96:99]
shin_L_rot = data[ : , 99:108]

thigh_R_location = data[ : , 108:111]
thigh_R_rot = data[ : , 111:120]

shin_R_location = data[ : , 120:123]
shin_R_rot = data[ : , 123:132]

foot_R_location = data[ : , 132:135]
foot_R_rot = data[ : , 135:144]

foot_L_location = data[ : , 144:147]
foot_L_rot = data[ : , 147:156]

hand_R_location = data[ : , 156:159]
hand_R_rot = data[ : , 159:168]

hand_L_location = data[ : , 168:171]
hand_L_rot = data[ : , 171:180]

frame_numbers = data[:, -1]

loop = np.shape(frame_numbers)
col = np.reshape(frame_numbers, (loop[0],1))

def rot(ent):
    final_result = []
    iteration = np.shape(ent)
    for rows in range(0, iteration[0]):
        ele = ent[rows , :]
        each = np.reshape(ele, (3,3))
        final_result.append(each)
        del(ele,each)
    return final_result

head_rotation = rot(head_rot)
neck_rotation = rot(neck_rot)
main_spine_rotation = rot(main_spine_rot)
upper_arm_L_rotation = rot(upper_arm_L_rot)
forearm_L_rotation = rot(forearm_L_rot)
upper_arm_R_rotation = rot(upper_arm_R_rot)
forearm_R_rotation = rot(forearm_R_rot)
thigh_L_rotation = rot(thigh_L_rot)
shin_L_rotation = rot(shin_L_rot)
thigh_R_rotation = rot(thigh_R_rot)
shin_R_rotation = rot(shin_R_rot)
foot_R_rotation = rot(foot_R_rot)
foot_L_rotation = rot(foot_L_rot)
hand_R_rotation = rot(hand_R_rot)
hand_L_rotation = rot(hand_L_rot)

imu_data_location = (head_location, neck_location, main_spine_location, upper_arm_L_location, forearm_L_location, upper_arm_R_location, forearm_R_location, thigh_L_location, shin_L_location, thigh_R_location, shin_R_location, foot_R_location, foot_L_location, hand_R_location, hand_L_location )
imu_data_rotation = (head_rotation, neck_rotation, main_spine_rotation, upper_arm_L_rotation, forearm_L_rotation, upper_arm_R_rotation, forearm_R_rotation, thigh_L_rotation, shin_L_rotation, thigh_R_rotation, shin_R_rotation, foot_R_rotation, foot_L_rotation, hand_R_rotation, hand_L_rotation )


def derivative_x(part, relation):
    max_element = np.amax(relation.astype(int))
    #print("part =", part)
    #print("len(part) =", len(part))
    #print("type(part) =", type(part))
    if not isinstance(part, np.ndarray):
        part = np.array(part)
    # print("part.shape =", part.shape)
    """
    if isinstance(part, list):
        first_op = [elem[:,0] for elem in part]
    elif isinstance(part, np.ndarray):
        first_op = part[:,0]
    """
    first_op = part[:, 0]
    # first_op = [ary[:,0] for ary in part]
    # print("first_op =", first_op)
    second_op = relation
    interpolation = interp1d(second_op, first_op, 'cubic',fill_value='extrapolate')
    bandwith = 1.0
    result_x = []
    derivate_frame = 1.0
    # print(max_element)
    for i in range(0, max_element):

        #print()
        drv_x = derivative(func=interpolation, x0=derivate_frame, dx=bandwith, n=2)
        result_x.append(drv_x)
        derivate_frame = derivate_frame + 1
    result_x = np.reshape(result_x, (len(result_x), 1))
    return result_x

def derivative_y(part, relation):
    max_element = np.amax(relation.astype(int))
    first_op = part[:,1]
    second_op = relation
    interpolation = interp1d(second_op, first_op, 'cubic',fill_value='extrapolate')
    bandwith = 1.0
    result_y = []
    derivate_frame = 1.0
    # print(interpolation(1))
    for i in range(0, max_element):

        #print()
        drv_y = derivative(func=interpolation, x0=derivate_frame, dx=bandwith, n=2)
        result_y.append(drv_y)
        derivate_frame = derivate_frame + 1
    result_y = np.reshape(result_y, (len(result_y), 1))
    return result_y

def derivative_z(part, relation):
    max_element = np.amax(relation.astype(int))
    first_op = part[:,2]
    second_op = relation
    interpolation = interp1d(second_op, first_op, 'cubic',fill_value='extrapolate')
    bandwith = 1.0
    result_z = []
    derivate_frame = 1.0
    # print(interpolation(1))
    for i in range(0, max_element):

        #print()
        drv_z = derivative(func=interpolation, x0=derivate_frame, dx=bandwith, n=2)
        result_z.append(drv_z + 9.7)
        derivate_frame = derivate_frame + 1
    result_z = np.reshape(result_z, (len(result_z), 1))
    return result_z

bone = 0

for data in imu_data_location:

    if bone == 0 :
        X = derivative_x(data,frame_numbers)
        Y = derivative_y(data,frame_numbers)
        Z = derivative_z(data,frame_numbers)
        head_acc = np.concatenate((X, Y, Z), axis=1)
    elif bone == 1:
        X = derivative_x(data,frame_numbers)
        Y = derivative_y(data,frame_numbers)
        Z = derivative_z(data,frame_numbers)
        neck_acc = np.concatenate((X, Y, Z), axis=1)
    elif bone == 2:
        X = derivative_x(data,frame_numbers)
        Y = derivative_y(data,frame_numbers)
        Z = derivative_z(data,frame_numbers)
        main_spine_acc = np.concatenate((X, Y, Z), axis=1)
    elif bone == 3:
        X = derivative_x(data,frame_numbers)
        Y = derivative_y(data,frame_numbers)
        Z = derivative_z(data,frame_numbers)
        upper_arm_L_acc = np.concatenate((X, Y, Z), axis=1)
    elif bone == 4:
        X = derivative_x(data,frame_numbers)
        Y = derivative_y(data,frame_numbers)
        Z = derivative_z(data,frame_numbers)
        forearm_L_acc = np.concatenate((X, Y, Z), axis=1)
    elif bone == 5:
        X = derivative_x(data,frame_numbers)
        Y = derivative_y(data,frame_numbers)
        Z = derivative_z(data,frame_numbers)
        upper_arm_R_acc = np.concatenate((X, Y, Z), axis=1)
    elif bone == 6:
        X = derivative_x(data,frame_numbers)
        Y = derivative_y(data,frame_numbers)
        Z = derivative_z(data,frame_numbers)
        forearm_R_acc = np.concatenate((X, Y, Z), axis=1)
    elif bone == 7:
        X = derivative_x(data,frame_numbers)
        Y = derivative_y(data,frame_numbers)
        Z = derivative_z(data,frame_numbers)
        thigh_L_acc = np.concatenate((X, Y, Z), axis=1)
    elif bone == 8:
        X = derivative_x(data,frame_numbers)
        Y = derivative_y(data,frame_numbers)
        Z = derivative_z(data,frame_numbers)
        shin_L_acc = np.concatenate((X, Y, Z), axis=1)
    elif bone == 9:
        X = derivative_x(data,frame_numbers)
        Y = derivative_y(data,frame_numbers)
        Z = derivative_z(data,frame_numbers)
        thigh_R_acc = np.concatenate((X, Y, Z), axis=1)
    elif bone == 10:
        X = derivative_x(data, frame_numbers)
        Y = derivative_y(data, frame_numbers)
        Z = derivative_z(data, frame_numbers)
        shin_R_acc = np.concatenate((X, Y, Z), axis=1)
    elif bone == 11:
        X = derivative_x(data,frame_numbers)
        Y = derivative_y(data,frame_numbers)
        Z = derivative_z(data,frame_numbers)
        foot_R_acc = np.concatenate((X, Y, Z), axis=1)
    elif bone == 12:
        X = derivative_x(data,frame_numbers)
        Y = derivative_y(data,frame_numbers)
        Z = derivative_z(data,frame_numbers)
        foot_L_acc = np.concatenate((X, Y, Z), axis=1)
    elif bone == 13:
        X = derivative_x(data,frame_numbers)
        Y = derivative_y(data,frame_numbers)
        Z = derivative_z(data,frame_numbers)
        hand_R_acc = np.concatenate((X, Y, Z), axis=1)
    elif bone == 14:
        X = derivative_x(data,frame_numbers)
        Y = derivative_y(data,frame_numbers)
        Z = derivative_z(data,frame_numbers)
        hand_L_acc = np.concatenate((X, Y, Z), axis=1)
    elif bone > 14:
        break

    bone = bone + 1


final_list = []
imu_data_acc = (head_acc, neck_acc, main_spine_acc, upper_arm_L_acc, forearm_L_acc, upper_arm_R_acc, forearm_R_acc, thigh_L_acc, shin_L_acc, thigh_R_acc, shin_R_acc, foot_R_acc, foot_L_acc, hand_R_acc, hand_L_acc)

def execution(frame):
    time_exe = frame
    np.array(time_exe)
    pre_acc = []
    exe_list = []

    for each in range(0,len(imu_data_acc)):
        operand1 = imu_data_acc[each]   # 1860
        operand2 = imu_data_rotation[each]
        for j in range(0,loop[0]):
            # print("operand1 =", operand1)
            #print("operand1.shape =", operand1.shape)
            operand1_ = np.reshape(operand1[j,:],(3,1))
            # print("operand1_=", operand1_)
            # print("operand2[j] =", operand2[j])
            rotation = np.matmul(operand2[j],operand1_)
            rotation_ = np.reshape(rotation,(1,3))
            # print("rotation_", rotation_.shape)
            pre_acc.extend(rotation_)

            np.array(pre_acc)
            # print("pre_acc1", np.array(pre_acc).shape)
        if each == 0:
            np.reshape(pre_acc, (loop[0], 3))
            head_acc_final = pre_acc
            pre_acc = []
        if each == 1:
            np.reshape(pre_acc, (loop[0], 3))
            neck_acc_final = pre_acc
            pre_acc = []
        if each == 2:
            np.reshape(pre_acc, (loop[0], 3))
            main_spine_acc_final = pre_acc
            pre_acc = []
        if each == 3:
            np.reshape(pre_acc, (loop[0], 3))
            upper_arm_L_acc_final = pre_acc
            pre_acc = []
        if each == 4:
            np.reshape(pre_acc, (loop[0], 3))
            forearm_L_acc_final = pre_acc
            pre_acc = []
        if each == 5:
            np.reshape(pre_acc, (loop[0], 3))
            upper_arm_R_acc_final = pre_acc
            pre_acc = []
        if each == 6:
            np.reshape(pre_acc, (loop[0], 3))
            forearm_R_acc_final = pre_acc
            pre_acc = []
        if each == 7:
            np.reshape(pre_acc, (loop[0], 3))
            thigh_L_acc_final = pre_acc
            pre_acc = []
        if each == 8:
            np.reshape(pre_acc, (loop[0], 3))
            shin_L_acc_final = pre_acc
            pre_acc = []
        if each == 9:
            np.reshape(pre_acc, (loop[0], 3))
            thigh_R_acc_final = pre_acc
            pre_acc = []
        if each == 10:
            np.reshape(pre_acc, (loop[0], 3))
            shin_R_acc_final = pre_acc
            pre_acc = []
        if each == 11:
            np.reshape(pre_acc, (loop[0], 3))
            foot_R_acc_final = pre_acc
            pre_acc = []
        if each == 12:
            np.reshape(pre_acc, (loop[0], 3))
            foot_L_acc_final = pre_acc
            pre_acc = []
        if each == 13:
            np.reshape(pre_acc, (loop[0], 3))
            hand_R_acc_final = pre_acc
            pre_acc = []
        if each == 14:
            np.reshape(pre_acc, (loop[0], 3))
            hand_L_acc_final = pre_acc
            pre_acc = []

    np.array(exe_list)
    #np.reshape(pre_acc,(loop[0],3))
    #print("foot_L_shape", np.array(foot_L_acc_final).shape)
    #exe_list.append(pre_acc)
    exe_list = np.concatenate((head_acc_final, neck_acc_final, main_spine_acc_final, upper_arm_L_acc_final, forearm_L_acc_final, upper_arm_R_acc_final, forearm_R_acc_final, thigh_L_acc_final, shin_L_acc_final, thigh_R_acc_final, shin_R_acc_final, foot_R_acc_final, foot_L_acc_final, hand_R_acc_final, hand_L_acc_final), axis=1)
    #pre_acc = []

    # print('foot_L_acc ', foot_L_acc_final)
    # print("foot_R_acc", foot_R_acc_final)
    return exe_list

final_list = execution(frame_numbers)

print("final_list =", np.array(final_list).shape)
#final_list = np.array(final_list).reshape((-1,45))
np.savetxt(file_path, final_list, "%.10g")


"""
    * HAR (Human Activitys Recognition)
    * Simulation


"""




#new = derivative_x(head_location, frame_numbers)
#print(new)

#function_of_head_x =interp1d(frame_numbers, head_rot, 'cubic')

#bandwith = 1.0
#derivative_at_frame = 1.0
#derivative_of_head_x = derivative(func=function_of_head_x, x0=derivative_at_frame, dx=bandwith, n=2)
#print("derivative_of_head_x =", derivative_of_head_x)











#def rot(ele1, ele2, ele3):
#    final_result = []
#    i = 0
#    for rows in range(0,103):
#        new_row1 = ele1[rows , :3]
#        new_row2 = ele2[rows , :3]
#        new_row3 = ele3[rows , :3]
#        ele = np.append(new_row1,new_row2,new_row3)
#        each = ele.reshape((3,3))
#        #each = np.split(ele, (3,3), axis= 1)
#        final_result.append(each)
#        del(ele,each)
#    return final_result

#hand_L_rotation1 = data[ : , 171:180]
#hand_L_rotation2 = data[ : , 174:177]
#hand_L_rotation3 = data[ : , 177:180]

#hand_R_rotation1 = data[ : , 159:162]
#hand_R_rotation2 = data[ : , 162:165]
#hand_R_rotation3 = data[ : , 165:168]

#foot_L_rotation1 = data[ : , 147:150]
#foot_L_rotation2 = data[ : , 150:153]
#foot_L_rotation3 = data[ : , 153:156]

#foot_R_rotation1 = data[ : , 135:138]
#foot_R_rotation2 = data[ : , 138:141]
#foot_R_rotation3 = data[ : , 141:144]

#shin_R_rotation1 = data[ : , 123:126]
#shin_R_rotation2 = data[ : , 126:129]
#shin_R_rotation3 = data[ : , 129:132]

#thigh_R_rotation1 = data[ : , 111:114]
#thigh_R_rotation2 = data[ : , 114:117]
#thigh_R_rotation3 = data[ : , 117:120]

#shin_L_rotation1 = data[ : , 99:102]
#shin_L_rotation2 = data[ : , 102:105]
#shin_L_rotation3 = data[ : , 105:108]

#thigh_L_rotation1 = data[ : , 87:90]
#thigh_L_rotation2 = data[ : , 90:93]
#thigh_L_rotation3 = data[ : , 93:96]

#forearm_R_rotation1 = data[ : , 75:78]
#forearm_R_rotation2 = data[ : , 78:81]
#forearm_R_rotation3 = data[ : , 81:84]

#upper_arm_R_rotation1 = data[ : , 63:66]
#upper_arm_R_rotation2 = data[ : , 66:69]
#upper_arm_R_rotation3 = data[ : , 69:72]

#forearm_L_rotation1 = data[ : , 51:54]
#forearm_L_rotation2 = data[ : , 54:57]
#forearm_L_rotation3 = data[ : , 57:60]

#upper_arm_L_rotation1 = data[ : , 39:42]
#upper_arm_L_rotation2 = data[ : , 42:45]
#upper_arm_L_rotation3 = data[ : , 45:48]

#main_spine_rotation1 = data[ : , 27:30]
#main_spine_rotation2 = data[ : , 30:33]
#main_spine_rotation3 = data[ : , 33:36]

#neck_rotation1 = data[ : , 15:18]
#neck_rotation2 = data[ : , 18:21]
#neck_rotation3 = data[ : , 21:24]

#head_rotation1 = data[ : , 3:6]
#head_rotation2 = data[ : , 6:9]
#head_rotation3 = data[ : , 9:12]

#def diff(part):
#    i = 0
#    for element in range(0, 100):
#        x1 = part[i, :3]
#        x2 = part[i+1, :3]
#        result = np.subtract(x1, x2)
#        print(result)
#        i = i + 1







