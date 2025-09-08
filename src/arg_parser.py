import argparse
import importlib.metadata
import sys


def get():
    """
    Parse command line arguments. Prints help message and exits if no arguments are provided.

    Returns:
        argparse.Namespace: Parsed command line arguments.
    """
    parser = argparse.ArgumentParser(description="Easy Video Downloader")
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=importlib.metadata.version("ez-vdl"),
    )
    parser.add_argument("-u", "--url", help="URL of the video to download")
    parser.add_argument(
        "-g",
        "--gui",
        default=False,
        help="Launch GUI",
        action="store_true",
    )
    parser.add_argument(
        "-q",
        "--quiet",
        default=False,
        help="Only show errors",
        action="store_true",
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        default=".",
        help="Directory to save downloaded video",
    )
    parser.add_argument(
        "--debug-log",
        default=False,
        help="Enable debug logging",
        action="store_true",
    )

    # If no arguments are provided, print help and exit
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    return parser.parse_args()
