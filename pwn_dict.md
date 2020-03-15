# pwn辞書

abcdefghijklmnopqrstuvwxyz

### double free
to be editing...  

### stack pivot
espまたはrspを任意の値に変更することで，pop,retなどのスタックを使う命令において，任意の値で操作することができる．  

### t-cache poisoning
詳細 => [t-cache poisoning: FireShell CTF 2019 babyheap](https://furutsuki.hatenablog.com/entry/2019/02/26/112207)  
heapにおいてt-cacheの指すアドレスを任意のアドレス値にすることで，次に同じ大きさのチャンクを要求したとき，t-cacheが優先されることで攻撃者が指定したアドレスが返り値として帰ってしまい，任意アドレスの内容を編集することができる攻撃手法．  
GOT overwriteと組み合わせて使用することが多い（と思ふ）．（t-cacheに変更したいGOTのアドレス，malloc後のデータ書き込み時にsystemやone_gadgetなどのshellを呼ぶ事のできるアドレスを指定．）

### type confusion
本来の変数の型と違う型で，その変数を操作することができる脆弱性．  
配列（char *）型と整数（int）型の間でtype confusionが存在すると，任意アドレスの値を出力，書き換えなどの攻撃が可能となってしまう．

  
