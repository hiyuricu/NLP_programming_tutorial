#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, math
from collections import defaultdict

#モデルを第一引数、評価データを第二引数として各単語のエントロピーを計算して、その合計を足して全ての単語の頻度で割る
#まずモデルファイルを辞書に格納する
#coverageはtypeなので別個で考える
def test_unigram():

	train_model_dic = defaultdict(float)
	all_bigram_token_frequency = 0
	all_entropy = 0
	unigram_known_word_freq = 0.1 #グリッド探索でfor文でループさせる必要がある
	bigram_known_word_freq = 0.9
	tokens = 1000000
	unknown_bigram_count = 0

	#ここでモデルファイルを辞書に格納している
	for line in open(sys.argv[1]):
		train_word_list = line.strip().split(" ")
		train_model_dic[train_word_list[0]] = float(train_word_list[1])

	#2gramと1gramのそれぞれのエントロピーを計算している
	for line in open(sys.argv[2]):
		test_word_list = line.strip().split()
		test_word_list.insert(0, "<s>")
		test_word_list.append("</s>")

		for i in range(1, len(test_word_list) - 1):
			all_bigram_token_frequency += 1
			# unigramのエントロピーの計算
			unigram_each_entory = unigram_known_word_freq * train_model_dic[test_word_list[i]] + float(1 - unigram_known_word_freq) / tokens

			# bigramのエントロピーの計算
			bigram = "%s\t%s" % (test_word_list[i - 1], test_word_list[i])
			if bigram not in train_model_dic:
				unknown_bigram_count += 1
			bigram_each_entory = bigram_known_word_freq * train_model_dic[bigram] + float(1 - bigram_known_word_freq) * unigram_each_entory
			
			all_entropy -= math.log(bigram_each_entory,2)

	#エントロピーとパープレキシー計算を行う
	all_entropy = float(all_entropy) / all_bigram_token_frequency
	coverage = float(all_bigram_token_frequency - unknown_bigram_count) / all_bigram_token_frequency

	print all_entropy, coverage

if __name__ == "__main__":
	test_unigram()