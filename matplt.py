import os
import numpy as np
import matplotlib.pyplot as plt
import cv2
import time
data = np.loadtxt("D:\\Codes\\Blender\\final_files\\coordinates.txt")
#data = np.loadtxt("D:\\Codes\\Blender\\final_files\\coordinates_first_results.txt")






# ax_3D.view_init(90, 90)

colors = ["black", "blue", "red", "green", "yellow", "purple", "orange", "brown", "pink", "gray", "cyan"]


action_dict = {1.0: "Stand",
               2.0: "Walk",
               3.0: "Sit",
               4.0: "Lie",
               }


use_opencv = True
if use_opencv:
    output_width = 1200
    output_height = 900
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video_writer = cv2.VideoWriter(os.getcwd() + os.sep + "Output.mkv", fourcc, 10, (output_width, output_height))

    for frame in range(len(data)):

        plt.figure().clear()
        plt.close()
        plt.cla()
        plt.clf()

        fig_3D = plt.figure("Ergebnisse", (16 * 0.75, 12 * 0.75))
        # fig_3D.suptitle(t="Frame " + str(frame_num), x=0.5, y=0.88, fontsize=18)
        ax_3D = fig_3D.add_subplot(111, projection='3d')

        # ax_3D.set_xlim([-20, 20])
        # ax_3D.set_ylim([-20, 20])
        ax_3D.set_zlim([0, 2.5])
        '''ax_3D.set_xlim([-1, 1])
        ax_3D.set_ylim([-50, 0])
        ax_3D.set_zlim([0, 1.8])'''

        ax_3D.set_xlabel("x-Axis")
        ax_3D.set_ylabel("y-Axis")
        ax_3D.set_zlabel("z-Axis")
        plt.tight_layout()
        # ax_3D.view_init(0, 0)
        ax_3D.view_init(10, -15)

        label = data[frame, -1]
        keyframe = data[frame, -2]
        plt.title(action_dict[label], fontsize=15)

        for i in np.arange(0, len(data[0])-2, 12):
            x_col = data[frame,i]
            y_col = data[frame,i+1]
            z_col = data[frame,i+2]
            #print("x_col =", x_col)
            #print("y_col =", y_col)
            x = len(data[0])-2
            #print("z_col =", z_col)
            ax_3D.scatter(x_col, y_col, z_col, c=colors[i % len(colors)])
            # fig_3D.canvas.draw()
        #plt.show()
        head = data[frame, :3]
        neck = data[frame, 12:15]
        main_spine = data[frame, 24:27]
        upper_arm_L = data[frame, 36:39]
        forearm_L = data[frame, 48:51]
        upper_arm_R = data[frame, 60:63]
        forearm_R = data[frame, 72:75]
        thigh_L = data[frame, 84:87]
        shin_L = data[frame, 96:99]
        thigh_R = data[frame, 108:111]
        shin_R = data[frame, 120:123]
        foot_R = data[frame, 132:135]
        foot_L = data[frame, 144:147]
        hand_R = data[frame, 156:159]
        hand_L = data[frame, 168:171]
        #print("neck =", neck)
        #print("head =", head)
        ax_3D.plot([neck[0], head[0]],
                   [neck[1], head[1]],
                   [neck[2], head[2]], c="black")
        ax_3D.plot([upper_arm_R[0], neck[0], upper_arm_L[0]],
                   [upper_arm_R[1], neck[1], upper_arm_L[1]],
                   [upper_arm_R[2], neck[2], upper_arm_L[2]], c="black")
        ax_3D.plot([upper_arm_R[0], forearm_R[0], hand_R[0]],
                   [upper_arm_R[1], forearm_R[1], hand_R[1]],
                   [upper_arm_R[2], forearm_R[2], hand_R[2]], c="black")
        ax_3D.plot([upper_arm_L[0], forearm_L[0], hand_L[0]],
                   [upper_arm_L[1], forearm_L[1], hand_L[1]],
                   [upper_arm_L[2], forearm_L[2], hand_L[2]], c="black")
        ax_3D.plot([neck[0], main_spine[0]],
                   [neck[1], main_spine[1]],
                   [neck[2], main_spine[2]], c="black")
        ax_3D.plot([thigh_R[0], main_spine[0], thigh_L[0]],
                   [thigh_R[1], main_spine[1], thigh_L[1]],
                   [thigh_R[2], main_spine[2], thigh_L[2]], c="black")
        ax_3D.plot([thigh_R[0], shin_R[0], foot_R[0]],
                   [thigh_R[1], shin_R[1], foot_R[1]],
                   [thigh_R[2], shin_R[2], foot_R[2]], c="black")
        ax_3D.plot([thigh_L[0], shin_L[0], foot_L[0]],
                   [thigh_L[1], shin_L[1], foot_L[1]],
                   [thigh_L[2], shin_L[2], foot_L[2]], c="black")

        # ax_3D.plot([-55,55,55,-55,-55], [50,50,252,252,50], [30,30,30,30,30], c="black")
            # fig_3D.canvas.draw()

        fig_3D.canvas.draw()


        # Now we can save it to a numpy array.
        # data = np.fromstring(fig_3D.canvas.tostring_rgb(), dtype=np.uint8, sep='')
        img = np.frombuffer(fig_3D.canvas.tostring_rgb(), dtype=np.uint8)
        img = img.reshape(fig_3D.canvas.get_width_height()[::-1] + (3,))
        img = cv2.resize(img, (output_width, output_height))
        img_BRG = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        #cv2.imshow("Test", img_BRG)
        #cv2.waitKey()
        video_writer.write(img_BRG)
    video_writer.release()
    cv2.destroyAllWindows()

else:
    for frame in range(len(data)):
        for i in np.arange(0, len(data[0])-4, 3):
            x_col = data[frame,i]
            y_col = data[frame,i+1]
            z_col = data[frame,i+2]
            #print("x_col =", x_col)
            #print("y_col =", y_col)
            #print("z_col =", z_col)
            ax_3D.scatter(x_col, y_col, z_col, c=colors[i % len(colors)])
            # fig_3D.canvas.draw()
            plt.pause(0.001)
            time.sleep(1)

    """
    data = np.frombuffer(fig_3D.canvas.tostring_rgb(), dtype=np.uint8)
    data = data.reshape(fig_3D.canvas.get_width_height()[::-1] + (3,))
    data = cv2.resize(data, (output_width, output_height))
    data_BRG = cv2.cvtColor(data, cv2.COLOR_RGB2BGR)
    """