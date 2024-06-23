from pwn import *

io = remote('mercury.picoctf.net', 6989)
io.send('1')