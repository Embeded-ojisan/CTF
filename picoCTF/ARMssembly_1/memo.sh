#!/bin/sh

# コンパイル
aarch64-linux-gnu-as -g -o chall.o chall.S
aarch64-linux-gnu-gcc -g -o chall chall.o

qemu-aarch64 -L /usr/aarch64-linux-gnu ./chall_1 232