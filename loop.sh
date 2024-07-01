#!/bin/bash

while true; do
    output=$(python main.py)

    if [ "$output" == "Bingo" ]; then
        echo "Bingo"
        break
    fi

    echo "Not Found - $(date)"
    sleep 300
done

