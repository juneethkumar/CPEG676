# coding: utf-8
from pwn import *
def exploit():
    proc= process("./chall_09")
    elf= ELF("./chall_09")
    p= ((xor(elf.string(elf.sym.key), b'\x69'))+ b'\x00\n')
    proc.send(p)
    proc.interactive()
    proc.close()
    
exploit()
