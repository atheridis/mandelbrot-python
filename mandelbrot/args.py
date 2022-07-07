import argparse


def parse_arguments():
    arg_parser = argparse.ArgumentParser(
        prog="yorugo-mandelbrot",
        description="Generates the mandelbrot set",
    )

    arg_parser.add_argument(
        "-r",
        "--resolution",
        type=int,
        default=1080,
        help="Set the height of the image or video in pixels. Default: 1080",
    )
    arg_parser.add_argument(
        "--scale",
        type=float,
        default=16 / 9,
        help="The scale of the image. Width / Height. Default: 16 / 9",
    )
    arg_parser.add_argument(
        "-s",
        "--steps",
        type=int,
        default=50,
        help="The search depth for the mandelbrot set. Default: 50",
    )

    arg_parser.add_argument(
        "-v",
        "--video",
        type=bool,
        action=argparse.BooleanOptionalAction,
        default=False,
        help="Render a video instead of an image.",
    )
    arg_parser.add_argument(
        "-f",
        "--frames",
        type=int,
        default=500,
        help="The number of frames to be rendered into the video. Default: 500",
    )
    arg_parser.add_argument(
        "-z",
        "--zoom-speed",
        type=float,
        default=0.9,
        help="Zoom speed. Default: 0.9",
    )

    arg_parser.add_argument(
        "-c",
        "--center",
        type=float,
        nargs=2,
        default=(0, 0),
        help="Center coordinates. Default 0 0",
    )
    arg_parser.add_argument(
        "-l",
        "--length",
        type=float,
        default=4,
        help="Length of X axis. Default 4",
    )

    return arg_parser.parse_args()
