# AtCoderOfflineJudge 0.2
## 概要

AtCoderOfflineJudge(ACOJ)は、AtCoderにおいて該当するPythonのプログラム名と入出力例をターミナルに入力することで、自動的にジャッジを行ってくれるプログラムです。

## 要件

こちらのユーザスクリプトと併用することを前提としています。

atcoder_collect_all_examples

https://greasyfork.org/ja/scripts/387240-atcoder-collect-all-examples

このユーザスクリプトは、AtCoderの問題ページにおいて入出力例をまとめてコピーできるものです。

また、本スクリプトはPython3.7.0で動作確認をしています。

## 使い方

```
$ python AtCoderOfflineJudge0.2.py テストするファイル名.py
```

で本スクリプトを実行します。なお、本ファイルとテストするファイルが別のフォルダにある場合は適宜パスを入力してください。動作確認は本ファイルとテストするファイルが同じフォルダにあある場合のみ行っています。

```
input the eg input, then return 2 times
```

と表示された後、ユーザスクリプトで得られる入力例をペーストし、Enterを2回叩きます。そうすると

```
eg input finished
input the eg output, then return 2 times
```

と表示されるので、同じく出力例をペーストし、Enterを2回叩きます。

その後、

```
eg output finished
```

と出力され、ジャッジが行われます。

なお、本バージョンでは浮動小数点出力対応のため、ここで出力結果が文字列であるか小数または整数であるかを確認し、出力します。出力形式は、文字列の場合は

```python
output mode is str
```

であり、小数または整数の場合は

```python
output mode is float or int
```

です。

ジャッジの結果は

```
Testing...
```

から

```
Test Finished
```

までに出力され、形式はi番目のテストケースにおいて、

ACの場合:

```
eg i AC
```

WAの場合:

```
eg i WA
input: 
hoge
predicted: 
fuga
result:
piyo
```

このとき、hogeは入力、fugaは期待する出力、resultはテストするpyファイルによる出力です。

TLEの場合:

```
eg i TLE
```

なお、TLEは2秒で設定してあります。

REの場合:

WAと同様に表示されますが、piyoがエラー出力になります。

MLEの場合:

ACと判定されてしまうと思います。

## 留意事項

### 浮動小数出力時

本バージョンで浮動小数点出力へのジャッジの対応をしました。新機能につきバグを発見された方はご報告ください。なお、浮動小数点の誤差許容範囲はプログラム5行目の

```Python
floatthreshold = pow(10, -4)
```

に定義してあります。誤差は絶対誤差のみで判断します。

### スペースや改行について

AtCoderのジャッジはスペースや改行についてゆるいジャッジを行っていると思いますが、ACOJは(AOJのように？)スペースや改行に厳しい判定をしています。引っかかった場合はWAと出力されるので、目視で確認してください。