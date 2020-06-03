# Python3の型変換

## 1Byte
### str ⇔ binary
#### str ⇒ binary
```
>>> 'A'.encode()
b'A'
```
#### binary ⇒ str
```
>>> b'A'.decode()
'A'
```

### binary ⇔ int
#### binary ⇒ int
```
>>> b'A'[0]
65
```
#### int => binary
```
>>> chr(65).encode()
b'A'
```


## Bytes
### str ⇔ binary
#### str ⇒ binary
```
>>> 'ABCD'.encode()
b'ABCD'
```
#### binary ⇒ str
```
>>> b'ABCD'.decode(errors='backslashreplace')
'ABCD'
```

### binary ⇔ int
#### binary ⇒ int
```
>>> int.from_bytes(b'ABCD', 'big')
1094861636
>>> hex(int.from_bytes(b'ABCD', 'big'))
'0x41424344'
```
#### int ⇒ binary
```
>>> ( 1094861636 ).to_bytes( 4, 'big' )
b'ABCD'
```

## bytesについて
python3のbytesはimmutableな型であるため，bytes列中の文字列に対して代入処理ができない．  
```
>>> b = b'ABCDEF' 
>>> b[:3] = b'XYZ'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'bytes' object does not support item assignment
```

これを回避するのに，bytearrayを使う．  
```
>>> b = bytearray( b'ABCDEF' )
>>> b[:3] = bytearray(b'XYZ')
>>> b
bytearray(b'XYZDEF')
```

#### bytearray ⇒ str
```
>>> bytearray( b'ABCDEF' ).decode(errors='backslashreplace')
'ABCDEF'
```

## 参考サイト
16進,bytesの相互変換 [https://qiita.com/masakielastic/items/21ba9f68ef6c4fd7692d]  
エラーハンドラ, python3docs [https://docs.python.org/ja/3/library/codecs.html#error-handlers]  
バイナリシーケンス型, python3docs [https://docs.python.org/ja/3/library/stdtypes.html#binary-sequence-types-bytes-bytearray-memoryview]  
python3組み込み型, python3docs [https://docs.python.org/ja/3.6/library/stdtypes.html]
