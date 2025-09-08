from __future__ import annotations

import logging

import arg_parser
import vdl_ops
import view


def main():
    """
    Main entry point for the video downloader.
    """

    # Parse command line arguments
    args = arg_parser.get()

    _set_logging_level(args)

    # Baseline validation, will be improved later
    # This program will either run in GUI mode or CLI mode
    if args.url:
        logging.info("Downloading video from URL: %s", args.url)
        vdl_ops.download_video(args.url, args.output_dir)
        return

    if args.gui:
        logging.info("Launching GUI...")
        view.render_gui()


def _set_logging_level(args):
    if args.quiet:
        logging.basicConfig(level=logging.ERROR)

    if args.debug_log:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)


if __name__ == "__main__":
    main()
