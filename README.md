# 20020818-lfw

## 2020-08-18

データ
- data/lfw-deepfunneled/  https://www-tlab.math.ryukoku.ac.jp/tlab/?takataka/note/2016-10-06 
- data/lfw_attributes.pickle https://www-tlab.math.ryukoku.ac.jp/tlab/?takataka/note/2018-09-15

1. 5721人それぞれ最初の画像のみ取り出す
1. 250x250 から 96x128 を切り出す
```
lty = 70
height = 128
ltx = 76
width = 96
img2 = img[lty:lty+height, ltx:ltx+width, :]
```
1. ランダムに 4000 枚を学習用に，残り 1721 枚をテスト用に
1. PNG画像として保存

![元画像の平均（学習用）](./meanL_org.png)

![得られた画像の平均（学習用）](./meanL.png)

