from pwn import *
from z3 import *

def change( num ):
    num = str(num)
    num = int(num)
    return num


#r = remote("159.89.166.12", 9800)
r = process("./challenge1")

text = r.recvuntil(";\n")

# Split text with v6(one), v7(two) , v8(three)
one, two, three, four = text.split(";")

one = int(one[58:])

two = int(two)

three = int(three)

v9 = Real("v9")
v10 = Real("v10")
v11 = Real("v11")

s = Solver()

s.add(v9 + v10 == one)
s.add(v10 + v11 == two)
s.add(v11 + v9 == three)

s.check()
v9 = s.model()[v9]
v10 = s.model()[v10]
v11 = s.model()[v11]

v10 = change(v10)
v11 = change(v11)
v9 = change(v9)

# Make payload
v9_num = len(str(v9))
v10_num = len(str(v10))
v11_num = len(str(v11))

payload = str(v9)
payload += "-"+"0"*(8-v9_num-1)
payload += "0"*2
payload += str(v10)
payload += "-"+"0"*(8-v10_num-1)
payload += "0"*2
payload += str(v11)
payload += "-"+"0"*(8-v11_num-1)

print(payload)

# Send payload
r.sendline(payload)

print(r.recv(100))
