# dd_package

本パッケージは ZDD のライブラリである

* [SAPPOROBDD](https://github.com/Shin-ichi-Minato/SAPPOROBDD)（湊 真一先生）
* [SAPPOROBDD helper](https://github.com/junkawahara/sbdd_helper)（川原）
* [TdZdd](https://github.com/kunisura/TdZdd)（岩下 洋哲氏）

を一度にダウンロード/アップデートするためのスクリプトです。
SAPPOROBDD は BDD/ZDD の演算ライブラリ、
SAPPOROBDD helper は SAPPOROBDD を使いやすくするための補助ライブラリ、
TdZdd はトップダウン BDD/ZDD 構築ライブラリです。

2021/9以前のユーザ向け: dd_package の旧バージョンについては old_version タグを参照してください。旧バージョンを使い続けるのはお勧めしません。

## パッケージの導入

コマンドラインから行います（現在のところ、Windows/Cygwin 環境のみで確認）。
wget, git コマンドが必要です。
以下のコマンドを実行します。

```
# your_program は好きな名前
mkdir your_program
cd your_program
wget https://github.com/junkawahara/dd_package/raw/main/downloader.sh
sh downloader.sh
```

このスクリプトを実行すると、your_program ディレクトリの中に、
SAPPOROBDD、sbdd_helper、TdZdd がダウンロードされます。
また、サンプル用の `Makefile` と `main.cpp` もダウンロードされます。

SAPPOROBDD は手動でビルドする必要があります。

```
cd SAPPOROBDD/src/
sh INSTALL
cd ../../
ls SAPPOROBDD/lib
# BDD64.a が表示されれば成功
```

ビルドに成功すると、SAPPOROBDD/lib ディレクトリの中に、BDD64.a が作成されます。

ダウンロードされた `Makefile` と `main.cpp` ファイルはサンプルプログラムです。
make でコンパイルして実行できる状態になっています。

```
make
./main
```

`./main` を実行して、"program works correctly" が出力されると、
正しくコンパイルできています。

本パッケージでは、main.cpp を編集して、
サンプルプログラムを上書き（消去）して自分のプログラムを書くという
使い方を想定しています。Makefile に詳しい人は、Makefile を
編集して、ソースファイルを自分の好きなファイル名にできます。


## マニュアル、リンク

* [SAPPOROBDD マニュアル](https://github.com/Shin-ichi-Minato/SAPPOROBDD/raw/main/man/BDD%2B.pdf) ダウンロードしたパッケージの SAPPOROBDD/man/BDD+.pdf に入っています。
* [SAPPOROBDD helper マニュアル](https://github.com/junkawahara/sbdd_helper)
* [TdZdd の解説論文](http://doi.org/10.11309/jssst.34.3_97) / [ユーザガイド（英語）](http://kunisura.github.io/TdZdd/doc/index.html)
