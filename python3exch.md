# Python3の型変換

## 1Byte
### str ↔ binary
#### str → binary
```
>>> 'A'.encode()
b'A'
```
#### binary → str
```
>>> b'A'.decode()
'A'
```

### binary ↔ int
#### binary → int
```
>>> b'A'[0]
65
```
#### int → binary
```
>>> chr(65).encode()
b'A'
```


## Bytes
### str ↔ binary
#### str → binary
```
>>> 'ABCD'.encode()
b'ABCD'
```
#### binary → str
```
>>> b'ABCD'.decode()
'ABCD'
```

### binary ↔ int
#### binary → int
```
>>> int.from_bytes(b'ABCD', 'big')
1094861636
>>> hex(int.from_bytes(b'ABCD', 'big'))
'0x41424344'
```
#### int → binary
```
>>> ( 1094861636 ).to_bytes( 4, 'big' )
b'ABCD'
```


## 参考サイト
[https://qiita.com/masakielastic/items/21ba9f68ef6c4fd7692d]
