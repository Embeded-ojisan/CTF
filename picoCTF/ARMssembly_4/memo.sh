#!/bin/sh
aarch64-linux-gnu-as -g -o chall_4.o chall_4.S
aarch64-linux-gnu-gcc -g -o chall_4 chall_4.o

qemu-aarch64 -L /usr/aarch64-linux-gnu ./chall_4 3251372985