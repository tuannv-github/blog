#!/bin/bash

SCRIPT_DIR=$(dirname "$0")
# echo $SCRIPT_DIR

mkdir -p ~/.ewm

kill  `cat ~/.ewm/ewm_server.pid`
nohup python3 -m http.server 8000 --directory $SCRIPT_DIR/../build/html &
echo $! > ~/.ewm/ewm_server.pid
