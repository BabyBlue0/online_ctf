# picomemo
適当メモ  

## ローカル環境のpwntoolsからリモートのChallengeを実行する方法 
ポートフォワードによって，リモートとローカルをつなぐ  
この方法を行うには，miscのssh-keyzを終わらしておく必要がある．  
(((この辺初心者なので用語怪しい)))  

1. リモートshell上で，適当なポート番号に実行ファイルを設置する  
\<PROBLEM DIRECTORY\> は各問題のディレクトリ．  
```remote shell1
$ socat TCP-LISTEN:60000,reuseaddr,fork EXEC:"/problems/<PROBLEM DIRECTORY>/vuln"
```  
2. ローカルのshellからポートフォワーディングを行う  
新しい端末を立ち上げ，以下のコマンドを実行．（リモートシェルのプロンプトが返るが，そのままにしておく）  
```local shell1
$ ssh -L 60000:localhost:60000 <USERNAME>@2018shell4.picoctf.com
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

この方法を使えば，1で指定するファイルを変えるだけで問題の変更が可能となる．  
