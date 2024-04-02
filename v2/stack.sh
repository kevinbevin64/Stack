#! /bin/bash

source .venv/bin/activate
python3 writefile.py
./main
python3 createfile.py