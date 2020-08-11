# picomemo
適当メモ  

## challengeファイルをローカルに落とす
```bash
scp <USERNAME>@2018shell4.picoctf.com:/problems/<PROBLEM DIRECTORY>/* ./
```

## ローカル環境のpwntoolsからリモートのChallengeを実行する方法 
ポートフォワードによって，リモートとローカルをつなぐ  
この方法を行うには，miscのssh-keyzを終わらしておく必要がある．  
(((この辺初心者なので用語怪しい)))  

1. ローカルのshellからポートフォワーディングを行う  
新しい端末を立ち上げ，以下のコマンドを実行．（リモートシェルが返ってくる）  
\<USERNAME\>を入力すること  
```local shell1
$ ssh -L 60000:localhost:60000 <USERNAME>@2018shell4.picoctf.com
```  
2. リモートshell上で，適当なポート番号に実行ファイルを設置する  
1で返ってきたリモートシェルで以下のコマンドを実行する．  
\<PROBLEM DIRECTORY\> は各問題のディレクトリ．  
```remote shell1
$ cd /problems/<PROBLEM DIRECTORY>/
$ socat TCP-LISTEN:60000,reuseaddr,fork EXEC:"./vuln"
```  
3. ローカルのshellで，`nc localhost 60000`とすればリモートの問題に接続できる
```local shell2
$ nc localhsot 60000
```
```exploit.py
from pwn import *
r = remote('localhost', 60000 )
r.interactive()
```

この方法を使えば，2で指定するファイルを変えるだけで問題の変更が可能である．  
