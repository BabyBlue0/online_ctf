"""
ebp-0xc := loop_i( loop_i-=3, init=len )
ebp-0x8 := idx( init=0 )
ebp-0x4 := arg1[idx]
"""

import binascii

enc = binascii.a2b_hex( """
37 a1 2a a3 bd 33 22 ba 2f 3c 98 aa b9 2f 39 a4 
18 33 aa 9a 2f 39 18 b3 24 3a af 18 99 1c 1c b1 
19 b1 98 1b 3e 59 ae a6 00 
""".replace('\n', '' ).replace(' ', '') )

print( "enc : \n%s"%(enc) )

def rol( A, n ):
  n %= len(A)*8
  i = int.from_bytes( A, 'little' )
  r = ( ((i<<n)%(2**(len(A)*8))) | i>>(len(A)*8-n)).to_bytes( len(A), 'little' )
  #print("rol{}  {} ==> {}".format(n,A,r) )
  return r

def ror( A, n ):
  n %= len(A)*8
  i = int.from_bytes( A, 'little' )
  r = ( ((i<<(len(A)*8-n))%(2**(len(A)*8))) | i>>(n)).to_bytes( len(A), 'little' )
  #print("ror{}  {} ==> {}".format(n,A,r) )
  return r


for j in range( len(enc)-4 ):
  dec = bytearray(enc)

  input()

  for i in range( j, -1, -1 ):
    dec[i:i+4] = bytearray(ror( dec[i:i+4], 7 ))
    dec[i:i+2] = bytearray(rol( dec[i:i+2], 9 ))
    dec[i] = dec[i]^0x4c
  print( "j({}) : ".format( j ), end='' )
  print( dec.decode(errors='backslashreplace') )
  print()
