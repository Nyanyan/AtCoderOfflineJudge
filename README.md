# AtCoderOfflineJudge
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
$ python AtCoderOfflineJudge.py テストするファイル名.py
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

### 浮動小数点出力時

浮動小数点出力時は、AtCoderではACとなるものでもACOJではWAとなる場合があります。これはACOJ内部でのACの判定を文字列として行っているからです。この場合は出力が表示されるので目視で確認してください。

### スペースや改行について

AtCoderのジャッジはスペースや改行についてゆるいジャッジを行っていると思いますが、ACOJは(AOJのように？)スペースや改行に厳しい判定をしています。引っかかった場合はWAと出力されるので、目視で確認してください。