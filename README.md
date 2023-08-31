# dd_package

本パッケージは ZDD のライブラリである

* [SAPPOROBDD](https://github.com/Shin-ichi-Minato/SAPPOROBDD)（湊 真一先生）
* [SAPPOROBDD helper](https://github.com/junkawahara/sbdd_helper)（川原）
* [TdZdd](https://github.com/kunisura/TdZdd)（岩下 洋哲氏）

を一度にダウンロードするためのスクリプトです。
SAPPOROBDD は BDD/ZDD の演算ライブラリ、
SAPPOROBDD helper は SAPPOROBDD を使いやすくするための補助ライブラリ、
TdZdd はトップダウン BDD/ZDD 構築ライブラリです。

## パッケージの導入

コマンドラインから行います（現在のところ、Windows/Cygwin 環境のみで確認）。
git コマンドが必要です。
以下のコマンドを実行します。または [downloader.sh](https://raw.githubusercontent.com/junkawahara/dd_package/main/downloader.sh) を手動でダウンロードして実行してください。

```
# your_program は好きな名前
mkdir your_program
cd your_program
wget https://github.com/junkawahara/dd_package/raw/main/downloader.sh
sh downloader.sh
```

`downloader.sh` スクリプトを実行すると、your_program ディレクトリの中に、
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

* [ZDD の実装に関する情報](https://github.com/junkawahara/dd_documents)
* [SAPPOROBDD マニュアル](https://github.com/Shin-ichi-Minato/SAPPOROBDD/raw/main/man/BDD%2B.pdf) ダウンロードしたパッケージの SAPPOROBDD/man/BDD+.pdf に入っています。
* [SAPPOROBDD helper マニュアル](https://github.com/junkawahara/sbdd_helper)
* [TdZdd の解説論文](https://www.jstage.jst.go.jp/article/jssst/34/3/34_3_97/_article/-char/ja/) / [ユーザガイド（英語）](http://kunisura.github.io/TdZdd/doc/index.html)

## ライセンス

本パッケージは MIT ライセンスです。downloader.sh を用いてダウンロードされるソフトウェアはそれぞれのライセンスに従います。
