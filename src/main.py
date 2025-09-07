from __future__ import annotations
from yt_dlp import YoutubeDL
import yt_dlp
import dearpygui.dearpygui as dpg

def download_video(url: str, output_dir: str = "./downloads"):
    ydl_opts: yt_dlp._Params = {
        "outtmpl": f"{output_dir}/%(title).50s.%(ext)s",
        "quiet": False,
        "no_warnings": True,
        "format": "bestvideo+bestaudio/best",
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def render_gui():
    dpg.create_context()
    dpg.create_viewport(title="EZ-VDL", width=600, height=400)
    with dpg.window(label="Easy Video Downloader"):
        dpg.add_text("Enter the URL of the video:")
        video_url_input = dpg.add_input_text()
        dpg.add_button(label="Download", callback=lambda: download_video(dpg.get_value(video_url_input)))

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()

def main():
    video_url = input("Enter the URL of the video: ")
    download_video(video_url)

if __name__ == "__main__":
    main()
