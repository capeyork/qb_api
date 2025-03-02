#!/bin/sh
if [ "$0" = "$BASH_SOURCE" ]; then
    echo "Run this script using 'source venv.sh' or '. ./venv.sh'"
else
    source venv/bin/activate
fi
