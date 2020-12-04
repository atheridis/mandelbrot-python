from numba import njit, prange
import numpy as np
from PIL import Image
import cv2
import os
import time
import colorsys


def hsv2rgb(h,s,v):
    return list(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))

def colour(n):
    if n:
        hue = n/100
        sat = 1
        value = 1
        return hsv2rgb(hue, sat, value)
    return 0

@njit(parallel=True, fastmath=True)
def mandelbrot(c, steps):
    z = c
    for n in prange(steps):
        if z.real * z.real + z.imag * z.imag > 4:
            return n
        z = z*z + c
    return 0

@njit(parallel=True, fastmath=True)
def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, steps):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    z = np.empty((width,height))

    for i in prange(width):
        for j in prange(height):
            z[i,j] = mandelbrot(x[i] + 1j*y[j], steps)

    return z

# settings
res = 1080  # height
scale = 16/9  # width / height
steps = 50  # search depth

# render video
video = False
max_frames = 480
z_speed = 0.9  # zoom speed


center = np.array([0, 0])  # center coordinates
x_length = 4  # length of x axis


##############################################
# NOTHING TO EDIT BELOW THIS line
##############################################
axis_length = (x_length, x_length/scale)

re_axis = (center[0] - axis_length[0] / 2,
                    center[0] + axis_length[0] / 2)

im_axis = (center[1] - axis_length[1] / 2,
                    center[1] + axis_length[1] / 2)

resolution = (int(scale*res), int(res))


if video:
    out = cv2.VideoWriter(f'Mandel0_{time.time()}.avi',
                        cv2.VideoWriter_fourcc(*'DIV4'),
                        24, resolution)

frame = 1
while True:
    if video:
        print(f"On frame {frame} out of {max_frames}")

    c = mandelbrot_set(re_axis[0], re_axis[1], im_axis[0], im_axis[1], resolution[0], resolution[1], steps)


    data = np.zeros((resolution[1], resolution[0], 3), dtype=np.uint8)


    for row in range(resolution[1]):
        if not video:
            print(f"On row {row} out of {resolution[1]}")
        for col in range(resolution[0]):
            data[row,col] = colour(c[col,row])

    image = Image.fromarray(data)

    if not video:
        image.save(f"i_{center[0]}+{center[1]}i_{steps}_{axis_length[0]}.png")

    if video:
        image.save("screen.png")
        img = cv2.imread("screen.png")
        os.remove("screen.png")
        out.write(img)

        axis_length = (z_speed * axis_length[0],
                        z_speed * axis_length[1])

        re_axis = (center[0] - axis_length[0] / 2,
                    center[0] + axis_length[0] / 2)
        im_axis = (center[1] - axis_length[1] / 2,
                    center[1] + axis_length[1] / 2)

        frame += 1

    if frame > max_frames or not video:
        break

if video:
    out.release()
