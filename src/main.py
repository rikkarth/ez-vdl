from __future__ import annotations

import arg_parser
import vdl_ops
import view


def main():
    args = arg_parser.get()

    if args.url:
        print("Downloading video from URL:", args.url)
        vdl_ops.download_video(args.url, args.output_dir)
        return

    if args.gui:
        print("Launching GUI...")
        view.render_gui()


if __name__ == "__main__":
    main()
