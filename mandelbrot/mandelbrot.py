from numba import jit, prange
import numpy as np
from PIL import Image
import cv2
import os
import time
import colorsys


def hsv2rgb(h, s, v):
    return list(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))


def colour(n):
    if n:
        hue = n / 100
        sat = 1
        value = 1
        return hsv2rgb(hue, sat, value)
    return 0


@jit
def mandelbrot(c, steps):
    z = c
    for n in prange(steps):
        if z.real * z.real + z.imag * z.imag > 4:
            return n
        z = z * z + c
    return 0


@jit
def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, steps):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    z = np.empty((width, height))

    for i in prange(width):
        for k in prange(height):
            # Reverse row, since computer images start from (0, 0) on the top left
            z[i, k] = mandelbrot(x[i] + 1j * y[height - (k + 1)], steps)

    return z


def compute(res, scale, steps, video, max_frames, z_speed, center, x_length):
    axis_length = (x_length, x_length / scale)

    re_axis = (center[0] - axis_length[0] / 2, center[0] + axis_length[0] / 2)

    im_axis = (center[1] - axis_length[1] / 2, center[1] + axis_length[1] / 2)

    resolution = (int(scale * res), int(res))

    if video:
        out = cv2.VideoWriter(
            f"Mandel0_{time.time()}.avi",
            cv2.VideoWriter_fourcc(*"DIV4"),
            24,
            resolution,
        )

    frame = 1
    while True:
        if video:
            print(f"On frame {frame} out of {max_frames}")

        c = mandelbrot_set(
            re_axis[0],
            re_axis[1],
            im_axis[0],
            im_axis[1],
            resolution[0],
            resolution[1],
            steps,
        )

        data = np.zeros((resolution[1], resolution[0], 3), dtype=np.uint8)

        for row in range(resolution[1]):
            if not video:
                print(f"On row {row} out of {resolution[1]}")
            for col in range(resolution[0]):
                data[row, col] = colour(c[col, row])

        image = Image.fromarray(data)

        if not video:
            image.save(f"i_{center[0]}+{center[1]}i_{steps}_{axis_length[0]}.png")

        if video:
            image.save("screen.png")
            img = cv2.imread("screen.png")
            os.remove("screen.png")
            out.write(img)

            axis_length = (z_speed * axis_length[0], z_speed * axis_length[1])

            re_axis = (center[0] - axis_length[0] / 2, center[0] + axis_length[0] / 2)
            im_axis = (center[1] - axis_length[1] / 2, center[1] + axis_length[1] / 2)

            frame += 1

        if frame > max_frames or not video:
            break

    if video:
        out.release()
