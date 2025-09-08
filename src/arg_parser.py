import argparse
import importlib.metadata
import sys


def get():
    parser = argparse.ArgumentParser(description="Easy Video Downloader")
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=importlib.metadata.version("ez-vdl"),
    )
    parser.add_argument("-u", "--url", help="URL of the video to download")
    parser.add_argument(
        "-g", "--gui", default=False, help="Launch GUI", action="store_true"
    )
    parser.add_argument(
        "-q", "--quiet", default=False, help="Only show errors", action="store_true"
    )
    parser.add_argument(
        "-o", "--output-dir", default=".", help="Directory to save downloaded video"
    )
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    return parser.parse_args()
