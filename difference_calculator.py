import numpy as np
from scipy.interpolate import interp1d
from scipy.misc import derivative

data = np.loadtxt("D:\\Codes\\Blender\\final_files\\coordinates.txt")
#print(data.shape()
head = data[0: , :3]
neck = data[0: , 3:6]
main_spine = data[0: , 6:9]
upper_arm_L = data[0: , 9:12]
forearm_L = data[0: , 12:15]
upper_arm_R = data[0: , 15:18]
forearm_R = data[0: , 18:21]
thigh_L = data[0: , 21:24]
shin_L = data[0: , 24:27]
thigh_R = data[0: , 27:30]
shin_R = data[0: , 30:33]
foot_R = data[0: , 33:36]
foot_L = data[0: , 36:39]
hand_R = data[0: , 39:42]
hand_L = data[0: , 42:45]

def diff(part):
    i = 0
    for element in range(0, 100):
        x1 = part[i, :3]
        x2 = part[i+1, :3]
        result = np.subtract(x1, x2)
        print(result)
        i = i + 1

print("head =", head)
print("head[:, 1] =", head[:, 1])

head_y = data[:, 1]
frame_numbers = data[:, -1]
function_of_head_x =interp1d(frame_numbers, head_y, 'cubic')
print("f(0) =", function_of_head_x(0))
print("f(1) =", function_of_head_x(1))
print("f(2) =", function_of_head_x(2))
print("f(5) =", function_of_head_x(5))
print("f(6) =", function_of_head_x(6))
print("f(25) =", function_of_head_x(25))
bandwith = 1.0
derivative_at_frame = 15.0
derivative_of_head_x = derivative(func=function_of_head_x, x0=derivative_at_frame, dx=bandwith, n=2)
print("derivative_of_head_x =", derivative_of_head_x)
#diff(head)