#!/bin/bash

pyinstaller \
--onefile src/main.py \
--name ez-vdl \
--workpath target \
--distpath target/dist
