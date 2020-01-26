# 解析で使う便利なコマンド集
一度調べたコマンドを二度も調べるのは面倒くさいのでここに書き殴ってく  

# OSのセキュリティ機構など
## ASLR（アドレスのランダム化）のオン/オフ
オフ `$ sysctl -w kernel.randomize_va_space=0  `  
オン `$ sysctl -w kernel.randomize_va_space=2  `  
または、  
`$ echo \(0 | 2\) > /proc/sys/kernel/randomize_va_space`  

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
|-fno-PIE|PIE(メモリ空間のランダム化)を無効|
|-z execstack|NXフラグ(コードの実行可能属性)を無効|
|-fno-stack-protector|canaryの無効|
|-o hoge|出力ファイル名を指定（デフォルトでa.out）|

# GDB
## shellを使いたくなったとき
(gdb) shell

# 静的解析
## ファイル内の文字列検索
grepも併用すると最強 
- $ strings -tx ./hoge
- $ readelf -p .rodata ./hoge
- $ objdump -s -j .rodata ./hoge

## GOTアドレス一覧
- $ readelf -r ./hoge

## セクションを指定してダンプ出力
- $ objdump -Mintel -d -j \(.plt|.text\|etc..) ./hoge

## リンクされたライブラリの表示
- $ ldd ./hoge

## シンボル表示
グローバル変数名や関数名からアドレスを求める    
- $ readelf -s ./hoge | grep buffer

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
## 仮想メモリのメモリマップ
libcや動的リンクされたバイナリの仮想アドレス値がわかる  
- (gdb) vmmap
- $ cat /proc/\<PID\>/maps
## 共有ライブラリの確認
- (gdb) info share
## スタックの確認
- (gdb) telescope <$ebp or $esp> \<num\>
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
- (gdb) stepuntil (cmp|xor|call|jmp)
