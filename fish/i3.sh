#!/bin/bash

# Check if i3 is already running
if ! pgrep -x "i3" > /dev/null; then
    # Start i3 if it's not running
    startx
fi
