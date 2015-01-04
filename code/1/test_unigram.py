#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, math
from collections import defaultdict

#モデルを第一引数、評価データを第二引数として各単語のエントロピーを計算して、その合計を足して全ての単語の頻度で割る
#まずモデルファイルを辞書に格納する
#coverageはtypeなので別個で考える
#未知語の対応をしなければならない
def test_unigram():

	train_model_dic = {}
	all_token_frequency = 0
	all_entropy = 0
	known_word_freq = 0.95
	unknown_word_freq = 1 - known_word_freq
	tokens = 1000000
	unknown_freq = float(unknown_word_freq) / tokens
	unknown_word_count = 0

	#ここでモデルファイルを辞書に格納している
	for line in open(sys.argv[1]):
		word_list = line.strip().split()
		train_model_dic[word_list[0]] = float(word_list[1])

	#エントロピーとパープレキシー計算を行う
	for line in open(sys.argv[2]):
		word_list = line.strip().split()
		word_list.append("</s>")
		for word in word_list:
			all_token_frequency += 1
			if word in train_model_dic:
				each_entory = known_word_freq * train_model_dic[word] + unknown_freq
				all_entropy -= math.log(each_entory,2)
			else:
				each_entory = unknown_freq
				all_entropy -= math.log(each_entory,2)
				unknown_word_count += 1

	all_entropy = float(all_entropy) / all_token_frequency
	coverage = float(all_token_frequency - unknown_word_count) / all_token_frequency

	print all_entropy, coverage

if __name__ == "__main__":
	test_unigram()