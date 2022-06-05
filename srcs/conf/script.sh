#!/bin/bash

python3 add_db.py

uwsgi --ini conf/uwsgi.ini
