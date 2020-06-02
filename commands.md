# 解析で使う便利なコマンド集
一度調べたコマンドを二度も調べるのは面倒くさいのでここに書き殴ってく  

# OSのセキュリティ機構など
## ASLR（アドレスのランダム化）のオン/オフ
オフ `$ sysctl -w kernel.randomize_va_space=0  `  
オン `$ sysctl -w kernel.randomize_va_space=2  `  
または、  
`$ echo <0|2> > /proc/sys/kernel/randomize_va_space`  

# Linuxシステムコール定義ファイル位置
## 32bit
`/usr/include/asm/unistd_32.h`
## 64bit
`/usr/include/asm/unistd_64.h`
## その他情報
### マニュアル
https://syscalls.kernelgrok.com/  
man syscall
``` man syscall
       The second table shows the registers used to pass the system call arguments.

       arch/ABI      arg1  arg2  arg3  arg4  arg5  arg6  arg7  Notes
       ──────────────────────────────────────────────────────────────
       ---
       i386          ebx   ecx   edx   esi   edi   ebp   -
       ---
       x86-64        rdi   rsi   rdx   r10   r8    r9    -
       x32           rdi   rsi   rdx   r10   r8    r9    -
       ---
```

# GCC( Cコンパイラ )
## gcc コンパイルオプション
|option|description|
|:--|:--|
|-m32|32bitでコンパイル(要インストール)|
||*sudo apt install libc6-dev-i386*|
|-no-pie|PIE(メモリ空間のランダム化)を無効|
|-z execstack|NXフラグ(コードの実行可能属性)を無効|
|-fno-stack-protector|canaryの無効|
|-o hoge|出力ファイル名を指定（デフォルトでa.out）|

# Python3
## 16進 → ASCII
```python3
>>> from binascii import unhexlify as u
>>> u(b'4142434445464748494a4b4c4d4e4f')
b'ABCDEFGHIJKLMNO'
```
もしくは，，，  
```python3
>>> b'\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f'
b'ABCDEFGHIJKLMNO'
```
# バイナリファイルからnByte分抜き出すコマンド  
フォーマットは適宜，変更すること．  
hexdumpの書式設定でバクスラをエスケープすると2つに増殖するので('\\\\xbe\\\\xba'みたいになる)，sedで文字列を置換している．
```
$ hexdump -s <行数(10進数)> -n <byte> -e '/1 "xx%02x"' main | sed 's/xx/\\x/g'
\x29\x06\x16\x4f\x2b\x35\x30\x1e\x51\x1b\x5b\x14\x4b\x08\x5d\x2b\x50\x14\x5d\x00\x19\x17\x59\x52\x5d
```
# libcの検索
libcの下位2Byteは固定．なのでデータベースからlibcを推測することができる  
https://libc.blukat.me/  

# bvi(バイナリエディタ)
/* 後で調べる */

# GDB
## shellを使いたくなったとき
- (gdb) shell
## 親プロセスのままデバッグしたいとき
GDBは子プロセスが生成されると自動的に子プロセスの方をアタッチする．それを無効化する（つまり親プロセスのままデバッグする）コマンド．  
参考：[https://access.redhat.com/documentation/ja-jp/red_hat_enterprise_linux/6/html/developer_guide/gdbforkedexec]  
- (gdb) set follow-fork-mode parent  

# 静的解析
## ファイル内の文字列検索
grepも併用すると最強 
- $ strings -tx ./hoge
- $ readelf -p .rodata ./hoge  

メモリダンプだが，仮想アドレス表示なのでわかりやすい（かも？）
- $ objdump -s -j .rodata ./hoge

## GOTアドレス一覧
- $ readelf -r ./hoge

## セクションを指定してダンプ出力
- $ objdump -Mintel -d -j \(.plt|.text\|etc..) ./hoge

## リンクされたライブラリの表示
- $ ldd ./hoge

## シンボル表示
グローバル変数名や関数名からアドレスを求める    
- $ readelf -s ./hoge | grep \<symbol name\>

## elfファイルヘッダ情報
### ヘッダ情報をすべて表示
- $ objdump -x ./hoge
### ファイルヘッダ
- readelf -h ./hoge
- $ objdump -f ./hoge
### プログラムヘッダ（メモリマップ？）
- $ readelf -l --wide ./hoge
### ベースアドレス？の表示
- $ readelf -l --wide ./hoge | grep LOAD
### セクションヘッダ
- $ objdump -h ./hoge


# 動的解析
参考:[http://ropshell.com/peda/Linux_Interactive_Exploit_Development_with_GDB_and_PEDA_Slides.pdf]
## ファイル情報
- (gdb) info files
## alarmの解除
- (gdb) handle SIGALRM ignore
## 仮想メモリのメモリマップ
libcや動的リンクされたバイナリの仮想アドレス値がわかる  
- (gdb) vmmap
- $ cat /proc/\<PID\>/maps  

pidofを使えば，プロセス名から調べられる．  
- $ cat /proc/\`pidof \<process name\>\`/maps

## GOTの確認
got overwriteができてるかの確認で使う  
```
(gdb) p 'atol@got.plt'
$7 = (<text from jump slot in .got.plt, no debug info>) 0x400590 <printf@plt>
```
## pythonコマンド実行
- (gef) pi print('A'*0x20+'B'*0x08)
## 共有ライブラリの確認
- (gdb) info share
## 参照先
- (gef) dereference \<$sp|$pc\> \<length\>
## スタックの確認
- (gdb) telescope \<$ebp|$esp\> \<length\>
## shellcode
### create
- (peda) shellcode generate x86/linux exec
### search
- (peda) shellcode search \<keyword\>
## find
- (peda) find "/bin/sh" libc
## dumprop
- (peda) dumprop binary "pop"
## ropgadget
- (peda) ropgadget
## 指定した命令まで実行
- (gdb) stepuntil \<cmp|xor|call|jmp\>
## PLT領域の表示
breakあり  
- (peda) plt  

breakなし  
- (peda) elfsymbol
- (peda) elfsymbol printf
