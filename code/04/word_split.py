#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from collections import defaultdict

lambda_1 = 0.95
lambda_unk = 1 - lambda_1
N = 1000000

def load_unigram_model(model_file): #keyに単語、valueに1-gramモデル確率が入った辞書を返す
	probabilities_model_dict = defaultdict(int)
	for line in open(model_file):
		(word, prob) = line.strip().split()
		word = word.decode("utf-8") #日本語に対応するためにutf-8でdecodeを行う
		probabilities_model_dict[word] = float(prob)
	return probabilities_model_dict

#一文ずつ改行されたものを入力とし、単語とそのunigramの値を返す
def word_split(unigram_probabilities_model,test_article):
	import math
	probabilities_model_dict = load_unigram_model(unigram_probabilities_model)
	probabilities_dict = defaultdict(int)
	word_split_list = []

	for line in open(test_article):
		line = line.strip().decode('utf-8')
		best_score_dic = defaultdict(int)
		best_edge_dic = defaultdict(int)
		best_edge_dic[0] = "NULL"
		temp_word_split_list = []

		for end_number in range(1, len(line) + 1): #forward_step
			for start_number in range(0, len(line)):
				if start_number >= end_number:
					continue
				key_string = line[start_number:end_number]
				probabilities_dict[key_string] = lambda_1 * probabilities_model_dict[key_string] + lambda_unk / N
				temp_score = - math.log(probabilities_dict[key_string]) + best_score_dic[start_number]
				if temp_score < best_score_dic[end_number] or best_score_dic[end_number] == 0:
					best_score_dic[end_number] = temp_score
					best_edge_dic[end_number] = (start_number, end_number)

		# for k,v in best_score_dic.items():
		# 	print k,v

		# やりかた違うけどbackward_step
		next_pass_tuple = best_edge_dic[len(line)]
		temp_word_split_list.append(line[next_pass_tuple[0]:next_pass_tuple[1]])
		while next_pass_tuple[0] != 0:
			next_pass_tuple = best_edge_dic[next_pass_tuple[0]]
			temp_word_split_list.append(line[next_pass_tuple[0]:next_pass_tuple[1]])

		temp_word_split_list.reverse()
		word_split_list.append(' '.join(temp_word_split_list))
	return word_split_list

if __name__ == "__main__":
	for splited_sentence in word_split(sys.argv[1], sys.argv[2]):
		print splited_sentence
