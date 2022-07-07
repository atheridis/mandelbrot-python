from setuptools import setup, find_packages

setup(
    name="mandelbrot",
    version="0.0.1",
    author="Georgios Atheridis",
    author_email="atheridis@tutamail.com",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "mandelbrot=mandelbrot.main:main",
        ],
    },
    install_requires=[
        "numba",
        "Pillow",
        "numpy",
        "opencv-python",
    ],
)
