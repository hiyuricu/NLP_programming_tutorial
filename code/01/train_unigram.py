#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from collections import defaultdict

#一文ずつ改行されたものを入力とし、単語とそのunigramの値を返す
def train_unigram():
	all_token_frequency = 0
	count_of = defaultdict(int)
	unigram_model_dic = {}

	for line in open(sys.argv[1]):
		word_list = line.strip().split()
		word_list.append("</s>")
		for word in word_list:
			count_of[word] += 1
			all_token_frequency += 1

	for k,v in count_of.items():
		unigram_model_dic[k] = float(v) / all_token_frequency

	return unigram_model_dic

if __name__ == "__main__":
	for k,v in sorted(train_unigram().items(), key=lambda x:x[1], reverse=True):
		print k,v