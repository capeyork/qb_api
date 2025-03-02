#!/bin/sh
if [ "$0" = "$BASH_SOURCE" ]; then
    echo "Run this script using 'source leave.sh' or '. leave.sh'"
else
    deactivate
fi
