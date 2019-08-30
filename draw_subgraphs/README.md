# フロンティア法や色付きフロンティア法のためのグラフ描画プログラム

与えられたグラフの部分グラフや部分色付きグラフを列挙した結果を描画。

## 使い方

svg 形式で描画

```
python draw_subgraphs.py example_grid2x2.txt subgraphs.txt > example.svg
```

拡張子が .svg のファイル（example.svg）が生成される。
svg 形式のファイルは web ブラウザ等で開くことができる。

'--reverse' オプションを付けると、部分グラフの辺の順を反転させることができる。

使用例
```
python draw_subgraphs.py example_grid2x2.txt subgraphs.txt --reverse > example.svg
```
