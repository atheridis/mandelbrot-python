<h1 align="center">Mandelbrot Image Renderer</h1>

<p align="center">
    <img width="600"
        alt="Mandelbrot Image Renderer"
        src="https://imgur.com/M4IIXNp.png">
</p>

## Installation

To install the latest version just type `$ pip install git+https://github.com/atheridis/mandelbrot-python.git`
in your terminal. The program has a bunch of different options, type `$ mandelbrot --help`
to see all of the options.

You may also clone this repository and install it from there.
```
$ git clone https://github.com/atheridis/mandelbrot-python.git
$ cd mandelbrot-python
$ pip install .
```

## How to use

Just by typing `$ mandelbrot` will create an 1080p image of the mandelbrot set inside
the directory you are currently in. You also have a number of options to choose from.

* `$ mandelbrot -r 1440` will make the image have a width of 1440 pixels.
* `$ mandelbrot --scale 1` will make the image a square. The default is 16/9
* `$ mandelbrot -s 100` The depth which each point will check wether it is in the set or not.
* `$ mandelbrot -c -0.745428 0.113009 -l 0.0001` Will center at x=-0.745428 y=0.113009, with the x axis having a total length of 0.0001
* `$ mandelbrot -r 480 -v -f 350 -z 0.9` Will produce a video of resolution 480p, containing 350 frames (at 24fps) and each frame will reduce the x axis length to 0.9 times the previous. Since this code is running on Python, it is quite slow. A lower quality video is advised.


## OLD PROJECT

This is one of many of my older projects which I have decided to turn it into a package and upload it to github.

