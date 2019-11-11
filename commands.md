# 解析で使う便利なコマンド集
一度調べたコマンドを二度も調べるのは面倒くさいのでここに書き殴ってく  

## gcc コンパイルオプション
|option|description|
|:--|:--|
|-m32|32bitでコンパイル(要インストール)|
||*sudo apt install libc6-dev-i386*|
|-fno-PIE|PIE(メモリ空間のランダム化)を無効|
|-z execstack|NXフラグ(コードの実行可能属性)を無効|
|-fno-stack-protector|カナリアノムコウ|
|-o hoge|出力ファイル名を指定（デフォルトでa.out）|

## ASLR（アドレスのランダム化）のオン/オフ
オフ sysctl -w kernel.randomize_va_space=0  
オン sysctl -w kernel.randomize_va_space=2  
または、  
echo \[0/2\] | /proc/sys/kernel/randomize_va_space

## ファイル内の文字列検索
grepも併用すると最強 
- strings -tx ./hoge
- readelf -p .rodata ./hoge
- objdump -s -j .rodata ./hoge

## GOTアドレス一覧
- readelf -r ./hoge

## セクションを指定して表示
- objdump -Mintel -d -j \[.plt|.text\] ./hoge

## リンクされたライブラリの表示
- ldd ./hoge

## シンボル表示
グローバル変数名や関数名からアドレスを求める    
- readelf -s ./hoge | grep buffer

## elfファイルヘッダ情報
### ヘッダ情報をすべて表示
- objdump -x ./hoge
### ファイルヘッダ
- readelf -h ./hoge
- objdump -f ./hoge
### プログラムヘッダ（メモリマップ？）
- readelf -l --wide ./hoge
### ベースアドレス？の表示
- readelf -l --wide ./hoge | grep LOAD
### セクションヘッダ
- objdump -h ./hoge
