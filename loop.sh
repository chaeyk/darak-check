#!/bin/bash

min=$1

if [ "$min" = "" ]; then
    echo "usage: $0 {min}"
    exit 1
fi

while true; do
    output=$(python main.py)

    if [[ "$output" =~ "Bingo" ]]; then
        echo "Bingo"
        break
    fi

    echo "Not Found - $(date)"
    sleep $((60 * $min))
done

