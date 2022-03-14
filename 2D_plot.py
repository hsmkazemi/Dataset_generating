import os
import numpy as np
import matplotlib.pyplot as plt
import cv2
import time
data = np.loadtxt("D:\\Codes\\Blender\\final_files\\acc.txt")
frame = np.loadtxt("D:\\Codes\\Blender\\final_files\\coordinates.txt")


head_acc = data[ : , :3]
neck_acc = data[ : , 3:6]
main_spine_acc = data[ : , 6:9]
upper_arm_L_acc = data[ : , 9:12]
forearm_L_acc = data[ : , 12:15]
upper_arm_R_acc = data[ : , 15:18]
forearm_R_acc = data[ : , 18:21]
thigh_L_acc = data[ : , 21:24]
shin_L_acc = data[ : , 24:27]
thigh_R_acc = data[ : , 27:30]
shin_R_acc = data[ : , 30:33]
foot_R_acc = data[ : , 33:36]
foot_L_acc = data[ : , 36:39]
hand_R_acc = data[ : , 39:42]
hand_L_acc = data[ : , 42:45]

head_location = frame[ : , :3]
neck_location = frame[ : , 12:15]
main_spine_location = frame[ : , 24:27]
upper_arm_L_location = frame[ : , 36:39]
forearm_L_location = frame[ : , 48:51]
upper_arm_R_location = frame[ : , 60:63]
forearm_R_location = frame[ : , 72:75]
thigh_L_location = frame[ : , 84:87]
shin_L_location = frame[ : , 96:99]
thigh_R_location = frame[ : , 108:111]
shin_R_location = frame[ : , 120:123]
foot_R_location = frame[ : , 132:135]
foot_L_location = frame[ : , 144:147]
hand_R_location = frame[ : , 156:159]
hand_L_location = frame[ : , 168:171]



frame_number = frame[: , -1]
print(data)





# ax_3D.view_init(90, 90)

colors = ["black", "blue", "red", "green", "yellow", "purple", "orange", "brown", "pink", "gray", "cyan"]

fig, (x_acc, y_acc, z_acc) = plt.subplots(3, 1)
fig.suptitle("Acceleration")

x_acc.set_xlim([0, np.amax(frame_number)])
x_acc.set_ylim([-10, 10])
y_acc.set_xlim([0, np.amax(frame_number)])
y_acc.set_ylim([8.7, 9.8])
z_acc.set_xlim([0, np.amax(frame_number)])
z_acc.set_ylim([-2.5, 4])

z_acc.set_xlabel("Time")
x_acc.set_ylabel("X acceleration")
y_acc.set_ylabel("Y acceleration")
z_acc.set_ylabel("Z acceleration")

plt.tight_layout(pad=1.5)

x_acc.plot(frame_number, shin_R_acc[:, 0])
# x_acc.view_init(0, 0)
y_acc.plot(frame_number, shin_R_acc[:, 1])
# y_acc.view_init(0, 0)
z_acc.plot(frame_number, shin_R_acc[:, 2])

# Assume there is a function my_walking(person_dict):
def my_walking(person_dict):
    pass

# Dictionary Idea from Matthias:
person_dict = {"P_ID": 1,
               # "path": {"straight" : [0, 15], "curve_right" : [(5, 27), (15, 64)]},
               "path": ["S_15", "TR_5_27", "TL_1_5"],
                }

imu_data = my_walking(person_dict)