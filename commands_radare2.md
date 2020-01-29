# radare2
思ったよりも複雑だったのでここに書く．  
静的解析中心．

# 基本
## 解析
aの数が多いほど深く解析する  
`> aa`  
`> aaa`  
`> aaaa`  
## 関数一覧表示
関数が多いと見にくい．  
`> afl`
## 関数の選択
`> s main`  
`> s sym.calc`
## ディスアセンブル
`> pdf`
## その他
### 履歴
`> !`
### ヘルプ
わからなければ基本これ  
`> ?`  
コマンドの途中でも使える  
```
> pdf?
Usage: pdf[bf]   disassemble function
| pdf   disassemble function
| pdfs  disassemble function summary
```
# ビジュアルモード
https://radare.gitbooks.io/radare2book/visual_mode/intro.html
```
Visual mode help:
 ?        show this help
 ??       show the user-friendly hud
 %        in cursor mode finds matching pair, or toggle autoblocksz
 @        redraw screen every 1s (multi-user view)
 ^        seek to the begining of the function
 !        enter into the visual panels mode
 _        enter the flag/comment/functions/.. hud (same as VF_)
 =        set cmd.vprompt (top row)
 |        set cmd.cprompt (right column)
 .        seek to program counter
 \        toggle visual split mode
 "        toggle the column mode (uses pC..)
 /        in cursor mode search in current block
 :cmd     run radare command
 ;[-]cmt  add/remove comment
 0        seek to beginning of current function
 [1-9]    follow jmp/call identified by shortcut (like ;[1])
 ,file    add a link to the text file
 /*+-[]   change block size, [] = resize hex.cols
 </>      seek aligned to block size (seek cursor in cursor mode)
 a/A      (a)ssemble code, visual (A)ssembler
 b        browse symbols, flags, configurations, classes, ...
 B        toggle breakpoint
 c/C      toggle (c)ursor and (C)olors
 d[f?]    define function, data, code, ..
 D        enter visual diff mode (set diff.from/to
 e        edit eval configuration variables
 f/F      set/unset or browse flags. f- to unset, F to browse, ..
 gG       go seek to begin and end of file (0-$s)
 hjkl     move around (or HJKL) (left-down-up-right)
 i        insert hex or string (in hexdump) use tab to toggle
 mK/'K    mark/go to Key (any key)
 M        walk the mounted filesystems
 n/N      seek next/prev function/flag/hit (scr.nkey)
 g        go/seek to given offset
 O        toggle asm.pseudo and asm.esil
 p/P      rotate print modes (hex, disasm, debug, words, buf)
 q        back to radare shell
 r        refresh screen / in cursor mode browse comments
 R        randomize color palette (ecr)
 sS       step / step over
 t        browse types
 T        enter textlog chat console (TT)
 uU       undo/redo seek
 v        visual function/vars code analysis menu
 V        (V)iew graph using cmd.graph (agv?)
 wW       seek cursor to next/prev word
 xX       show xrefs/refs of current function from/to data/code
 yY       copy and paste selection
 z        fold/unfold comments in disassembly
 Z        toggle zoom mode
 Enter    follow address of jump/call
Function Keys: (See 'e key.'), defaults to:
  F2      toggle breakpoint
  F4      run to cursor
  F7      single step
  F8      step over
  F9      continue
```
## ビジュアルモードに入る
`> VV`  
`> V!`
## gragh <-> disas 切り替え
`[space]`
## 表示切り替え
[graph] アドレス有りが良さげ  
`p/P`
## [gragh] disasを表示
グラフと紐付いているため，見やすい（し，かっこいい(≧∀≦) ）  
`D`
## [disas] 逆コンパイル表示
多分アセンブリ命令をそのままCっぽく表示させたもの．精度が低い．  
`*`
## 関数名検索
関数名で検索し，移動することができるため大変便利．  
`_`
## モード
### コマンドモード  
コマンドが打てるモード  
`:`
### カーソルモード  
命令の塊を移動することができるモード  
`c`


# 変数
https://radare.gitbooks.io/radare2book/analysis/variables.html
```
> afv?
Usage: afv  [rbs]
| afvr[?]                       manipulate register based arguments
| afvb[?]                       manipulate bp based arguments/locals
| afvs[?]                       manipulate sp based arguments/locals
| afv*                          output r2 command to add args/locals to flagspace
| afvR [varname]                list addresses where vars are accessed (READ)
| afvW [varname]                list addresses where vars are accessed (WRITE)
| afva                          analyze function arguments/locals
| afvd name                     output r2 command for displaying the value of args/locals in the debugger
| afvn [new_name] ([old_name])  rename argument/local
| afvt [name] [new_type]        change type for given argument/local
| afvf                          show BP relative stackframe variables
| afv-([name])                  remove all or given var
```
## 引数/ローカル変数を自動取得
```
> afva
```
## 引数/ローカル変数の表示
```
> afv
var int32_t var_dh @ ebp-0xd
var int32_t cnt @ ebp-0xc
arg int32_t buff @ ebp+0x8
arg signed int const_400 @ ebp+0xc
```
## 引数/ローカル変数の名称変更
```
> afvn cnt var_ch
```
## 引数/ローカル変数の削除
```
> afv- var_28h
```
