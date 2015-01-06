#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from collections import defaultdict

#一文ずつ改行されたものを入力とし、単語とその単語のtestで線形補間で用いられるbigramの確率を返す
def train_bigram():
	count_of = defaultdict(int)
	context_count_of = defaultdict(int)
	bigram_model_dic = {}

	for line in open(sys.argv[1]):
		word_list = line.strip().split()
		word_list.insert(0, "<s>")
		word_list.append("</s>")
		for i in range(1,len(word_list) - 1):
			bigram = "%s\t%s" % (word_list[i - 1], word_list[i])
			unigram = word_list[i] #視認性のために代入した
			count_of[bigram] += 1
			context_count_of[word_list[i - 1]] += 1
			count_of[unigram] += 1
			context_count_of[""] += 1

	for k,v in count_of.iteritems():
		key_list = k.strip().split()
		if len(key_list) == 1:
			bigram_model_dic[k] = float(count_of[k]) / context_count_of[""]
		elif len(key_list) == 2:
			bigram_model_dic[k] = float(count_of[k]) / context_count_of[key_list[0]]

	return bigram_model_dic

if __name__ == "__main__":
	for k,v in sorted(train_bigram().iteritems(), key=lambda x:x[1], reverse=True):
		print k,v