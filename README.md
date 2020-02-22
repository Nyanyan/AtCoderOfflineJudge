# AtCoderOfflineJudge
## 概要

AtCoderOfflineJudge(ACOJ)は、AtCoderにおいて該当するプログラム名と入出力例をターミナルに入力することで、自動的にジャッジを行ってくれるプログラムです。

## 要件

こちらのユーザスクリプトと併用することを前提としています。

atcoder_collect_all_examples

https://greasyfork.org/ja/scripts/387240-atcoder-collect-all-examples

このユーザスクリプトは、AtCoderの問題ページにおいて入出力例をまとめてコピーできるものです。

また、本スクリプトはPython3.7.0で動作確認をしています。

## 使い方

```
python AtCoderOfflineJudge.py テストするファイル名.py
```

で本スクリプトを実行し、

```
>input the eg input, then return 2 times
```

と表示された後、ユーザスクリプトで得られる入力例をペーストし、Enterを2回叩きます。