# アプリ実行側
qemu-aarch64 -L /usr/aarch64-linux-gnu -g 1234 ./chall

# 対向側
gdb-multiarch ./chall

## gdb
target remote :1234
b main
continue