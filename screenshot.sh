#!/bin/bash

dir="$(dirname "$(readlink -f "$0")")"
flameshot gui -r | python "$dir/main.py"

