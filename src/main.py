"""
    ez-vdl (Easy Video Downloader)

    This module provides a simple command-line tool for downloading videos
    from X (formerly Twitter) using yt-dlp as the backend.

    Features:
        - Interactive prompt for video URL if not provided via CLI.
        _ Configurable output directory using the -o/--output option.
        - Automatically creates the output directory if it doesn't exist.
        - Downloads the best available video and audio combination.

    Typical Usage Example:
        uv run src/main.py -u "https://x.com/username/status/123456789" -o ./my_videos
"""
from __future__ import annotations
import argparse
import os
from pathlib import Path
import yt_dlp
from yt_dlp import YoutubeDL


def parse_args():
    """
    Parse command-line arguements for ez-vdl.

    Returns:
        argparse.Namespace: Parsed arguments containing:
            - url (str | None): URL of the X post containing the video.
            - output (str): Directory path where the video will be saved.
    """
    parser = argparse.ArgumentParser(
        description="ez-vdl: Easy Video Downloader")
    parser.add_argument(
        "-u", "--url",
        type=str,
        help="URL of the X post containing the video"
    )
    parser.add_argument(
        "-o", "--output",
        type=str,
        default="./downloads",
        help="Directory path where the video will be saved"
    )
    return parser.parse_args()


def download_x_video(url: str, output_dir: str = "./downloads"):
    """
    Download a video from an X post using yt-dlp.

    Args:
        url (str): URL of the X post containing the video.
        output_dir (str, optional): Directory path where the video will be saved.
                                    Defaults to "./downloads".
    """

    output_path = Path(output_dir).expanduser().resolve()
    os.makedirs(output_path, exist_ok=True)

    ydl_opts: yt_dlp._Params = {
        "outtmpl": str(output_path / "%(title).50s.%(ext)s"),
        "quiet": False,
        "no_warnings": True,
        "format": "bestvideo+bestaudio/best",
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def main():
    """
        Entry point for the ez-vdl.

        - Parses arguments from the command line.
        - Prompts for URL if not provided via -u/--url flag.
        - Downloads the video to the specified output directory.
    """

    args = parse_args()
    url = args.url or input("Enter the URL of the X video: ")
    download_x_video(url, args.output)


if __name__ == "__main__":
    main()
