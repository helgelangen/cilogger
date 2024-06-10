#!/bin/bash

python3 -m venv .venv
source .venv/bin/activate

python3 setup.py install

python3 test/test_init.py
python3 test/test.py
python3 test/test_final.py