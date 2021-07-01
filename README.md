# OpenCV-img_hash-Sample
Python版OpenCVのimg_hashモジュールを用いた画像ハッシュのサンプルです。
<img src="https://user-images.githubusercontent.com/37477845/124159958-b174a400-dad6-11eb-960e-36a38f09c3de.png" loading="lazy" width="75%">

# Requirement 
* opencv-contrib-python 4.5.2.54 or later

# Algorithm
2021/07/02時点でOpenCVには以下6アルゴリズムが実装されています。
* Average Hash
* Block Mean Hash
* Color Moment Hash
* Marr Hildreth Hash
* Perceptual Hash
* Radial Variance Hashalgorithm

各アルゴリズムのパフォーマンスチャートは以下です。<br>
<img src="https://user-images.githubusercontent.com/37477845/124160871-aec67e80-dad7-11eb-88d6-8f1e914aed4c.png" loading="lazy" width="75%"><br>
※OpenCVドキュメント Performance under different attacksより引用

# Usage
「OpenCV_img_hash_Sample.ipynb」をColaboratoryかJupyter notebook上で開いて実行してください。<br>
また、画像をハッシュリスト化しpickle保存・読み込み、画像同士の類似度を比較するサンプルも用意しています。<br>
以下のコマンドで実行できます。
```
python 01_compute_sample.py
python 02_compare_sample.py
```

# Reference
[OpenCV:image hashing algorithms](https://docs.opencv.org/master/d4/d93/group__img__hash.html)

# Author
高橋かずひと(https://twitter.com/KzhtTkhs)
 
# License 
OpenCV-img_hash-Sample is under [Apache-2.0 License](LICENSE).

# License(Image)
使用している画像は[NHKクリエイティブ・ライブラリー](https://www.nhk.or.jp/archives/creative/)の[ストリートバスケット](https://www2.nhk.or.jp/archives/creative/material/view.cgi?m=D0002080169_00000)をフレーム毎に静止画を取り出したものです。
