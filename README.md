# dd_package

本パッケージは ZDD のライブラリである

* SAPPOROBDD（湊 真一先生）
* [SAPPOROBDD helper](https://github.com/junkawahara/sbdd_helper)（川原）
* [TdZdd](https://github.com/kunisura/TdZdd)（岩下 洋哲氏）

を、使いやすいようにまとめたものです。
SAPPOROBDD は BDD/ZDD の演算ライブラリ、
SAPPOROBDD helper は SAPPOROBDD を使いやすくするための補助ライブラリ、
TdZdd はトップダウン BDD/ZDD 構築ライブラリです。

SAPPOROBDD helper と TdZdd は web 上で公開されているライブラリですが、
SAPPOROBDD はまだ公開されていないライブラリですので、
取扱いに注意してください。

## パッケージの導入

git を使います。以下のコマンドを実行します。

```
git clone https://github.com/junkawahara/dd_package.git
cd dd_package
cp template.cpp program.cpp
make
./program
```

（template.cpp からコピーした）program.cpp
ファイルはサンプルプログラムです。
make でコンパイルして実行できる状態になっています。

本パッケージでは、program.cpp を編集して、
サンプルプログラムを上書き（消去）して自分のプログラムを書くという
使い方を想定しています。Makefile に詳しい人は、Makefile を
編集して、ソースファイルを自分の好きなファイル名にできます。


## マニュアル

* [SAPPOROBDD マニュアル](http://www.lab2.kuis.kyoto-u.ac.jp/jkawahara/dd/BDD+.pdf)
* [SAPPOROBDD helper マニュアル](https://github.com/junkawahara/sbdd_helper) (執筆中のため、まだほとんど情報がありません)
* [TdZdd の解説論文](http://doi.org/10.11309/jssst.34.3_97) / [ユーザガイド（英語）](http://kunisura.github.io/TdZdd/doc/index.html)
