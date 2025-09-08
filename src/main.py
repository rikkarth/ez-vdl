from __future__ import annotations

import arg_parser
import vdl_ops
import view


def main():
    """
    Main entry point for the video downloader.
    """

    # Parse command line arguments
    args = arg_parser.get()

    # Baseline validation, will be improved later
    # This program will either run in GUI mode or CLI mode
    if args.url:
        print("Downloading video from URL:", args.url)
        vdl_ops.download_video(args.url, args.output_dir)
        return

    if args.gui:
        print("Launching GUI...")
        view.render_gui()


if __name__ == "__main__":
    main()
