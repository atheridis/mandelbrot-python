from .args import parse_arguments
from .mandelbrot import compute


def main():
    argsv = parse_arguments()
    compute(
        argsv.resolution,
        argsv.scale,
        argsv.steps,
        argsv.video,
        argsv.frames,
        argsv.zoom_speed,
        argsv.center,
        argsv.length,
    )


if __name__ == "__main__":
    main()
