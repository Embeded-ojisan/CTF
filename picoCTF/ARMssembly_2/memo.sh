#!/bin/sh
aarch64-linux-gnu-as -g -o chall_2.o chall_2.S
aarch64-linux-gnu-gcc -g -o chall_2 chall_2.o

qemu-aarch64 -L /usr/aarch64-linux-gnu ./chall_2 3736234946