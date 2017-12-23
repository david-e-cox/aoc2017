#!/bin/sh

if [ ! -f "./pipe" ]; then
   mkfifo pipe
fi

./d18b.py 0 < pipe | ./d18b.py 1 > pipe



