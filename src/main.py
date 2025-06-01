from yt_dlp import YDLOpts, YoutubeDL


def download_x_video(url: str, output_dir: str = "./downloads"):
    ydl_opts: YDLOpts = {
        "outtmpl": f"{output_dir}/%(title).50s.%(ext)s",
        "quiet": False,
        "no_warnings": True,
        "format": "bestvideo+bestaudio/best",
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


if __name__ == "__main__":
    video_url = input("Enter the URL of the X video: ")
    download_x_video(video_url)
