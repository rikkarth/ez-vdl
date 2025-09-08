from __future__ import annotations

import yt_dlp
from yt_dlp import YoutubeDL


def download_video(url: str, output_dir: str = ".") -> None:
    ydl_opts: yt_dlp._Params = {
        "outtmpl": f"{output_dir}/%(title).50s.%(ext)s",
        "quiet": False,
        "no_warnings": True,
        "format": "bestvideo+bestaudio/best",
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
