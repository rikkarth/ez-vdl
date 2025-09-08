"""
Core GUI rendering logic using Dear PyGui.
"""

from __future__ import annotations

import logging

import dearpygui.dearpygui as dpg  # type: ignore

import vdl_ops

log = logging.getLogger(__name__)

__all__ = ["render_gui"]


selected_path = ""


def render_gui() -> None:
    dpg.create_context()
    # Create window with autosize and fixed position (not draggable, not resizable)
    with dpg.window(label="Easy Video Downloader") as main_window_id:
        dpg.add_text("Enter the URL of the video:")
        video_url_input = dpg.add_input_text()

        ds_id = _directory_selector()

        dpg.add_button(
            label="Select Download Directory", callback=lambda: dpg.show_item(ds_id)
        )
        dpg.add_text(selected_path, tag="selected_path_text")
        dpg.add_button(
            label="Download",
            callback=lambda: vdl_ops.download_video(
                dpg.get_value(video_url_input),
                output_dir=dpg.get_value("selected_path_text"),
            ),
        )
        dpg.add_button(
            label="X",
            callback=lambda: dpg.stop_dearpygui(),
            tag="close_button",
            width=20,
            height=20,
        )

    _initialize_viewport(main_window_id)


def _directory_selector() -> int | str:
    win_id = dpg.add_file_dialog(
        directory_selector=True,
        show=True,
        callback=_directory_selector_callback,
        width=400,
        height=300,
        cancel_callback=_cancel_callback,
    )

    return win_id


def _directory_selector_callback(sender, app_data):
    log.debug("OK was clicked.")
    log.debug("Sender: %s", sender)
    log.debug("App Data: %s", app_data)
    selected_path = app_data["file_path_name"]
    dpg.set_value("selected_path_text", selected_path)


def _cancel_callback(sender, app_data):
    log.debug("Cancel was clicked.")
    log.debug("Sender: %s", sender)
    log.debug("App Data: %s", app_data)


def _initialize_viewport(main_window_id):
    dpg.create_viewport(title="EZ-VDL", resizable=False, width=475, height=375)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window(main_window_id, True)

    dpg.set_item_pos("close_button", [dpg.get_viewport_width() - 20, 0])

    dpg.start_dearpygui()
    dpg.destroy_context()
