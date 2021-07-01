#!/usr/bin/env python
# -*- coding: utf-8 -*-
import glob
import pickle

import cv2 as cv


def main():
    # ハッシュリスト用ファイル一覧取得
    input_files = glob.glob('02_input/*')

    # img_hashインスタンス生成
    # hash_func = cv.img_hash.AverageHash_create()
    # hash_func = cv.img_hash.BlockMeanHash_create(mode=0)
    # hash_func = cv.img_hash.BlockMeanHash_create(mode=1)
    hash_func = cv.img_hash.ColorMomentHash_create()
    # hash_func = cv.img_hash.MarrHildrethHash_create()
    # hash_func = cv.img_hash.PHash_create()
    # hash_func = cv.img_hash.RadialVarianceHash_create()

    # ハッシュ計算
    hash_list = []
    for input_file in input_files:
        temp_image = cv.imread(input_file)
        hash_value = hash_func.compute(temp_image)

        hash_list.append([input_file, hash_value])

    # ハッシュリストpickle保存
    with open('hash_list.pickle', 'wb') as f:
        pickle.dump(hash_list, f)


if __name__ == '__main__':
    main()
