# コンパイル
aarch64-linux-gnu-as -g -o chall.o chall.S
aarch64-linux-gnu-gcc -g -o chall chall.o

# アプリ実行側
qemu-aarch64 -L /usr/aarch64-linux-gnu -g 1234 ./chall

# 対向側
gdb-multiarch ./chall

## gdb
target remote :1234
b main
continue

ps aux | grep qemu-aarch64
kill -9 <pid>