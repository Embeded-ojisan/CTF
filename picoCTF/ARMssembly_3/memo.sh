#!/bin/sh
aarch64-linux-gnu-as -g -o chall_3.o chall_3.S
aarch64-linux-gnu-gcc -g -o chall_3 chall_3.o

qemu-aarch64 -L /usr/aarch64-linux-gnu ./chall_3 1048110976