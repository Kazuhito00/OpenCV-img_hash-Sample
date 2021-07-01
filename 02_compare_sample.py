#!/usr/bin/env python
# -*- coding: utf-8 -*-
import glob
import pickle

import cv2 as cv
import numpy as np


def main():
    # テスト用ファイル一覧取得
    test_files = glob.glob('03_test/*')

    # img_hashインスタンス生成
    # hash_func = cv.img_hash.AverageHash_create()
    # hash_func = cv.img_hash.BlockMeanHash_create(mode=0)
    # hash_func = cv.img_hash.BlockMeanHash_create(mode=1)
    hash_func = cv.img_hash.ColorMomentHash_create()
    # hash_func = cv.img_hash.MarrHildrethHash_create()
    # hash_func = cv.img_hash.PHash_create()
    # hash_func = cv.img_hash.RadialVarianceHash_create()

    # 事前計算済みハッシュリスト読み込み
    hash_list = []
    with open('hash_list.pickle', 'rb') as f:
        hash_list = pickle.load(f)

    # テスト画像のハッシュ値を計算し、事前計算済みのハッシュリストと比較
    for test_file in test_files:
        # テスト画像のハッシュ値計算
        test_image = cv.imread(test_file)
        test_hash_value = hash_func.compute(test_image)

        # 事前計算済みハッシュリストと比較
        result_list = []
        for temp_hash in hash_list:
            target_hash_value = temp_hash[1]
            result = hash_func.compare(target_hash_value, test_hash_value)
            result_list.append(result)

        # 計算結果から最小距離(類似画像)のインデックスを取得
        result_index = np.argmin(np.array(result_list))

        # 結果表示
        target_file = hash_list[result_index][0]
        compare_value = result_list[result_index]
        print(target_file, test_file, compare_value)


if __name__ == '__main__':
    main()
