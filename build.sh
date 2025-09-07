#!/bin/bash

pyinstaller \
--onefile src/main.py \
--name rmvdl \
--workpath target \
--distpath target/dist
