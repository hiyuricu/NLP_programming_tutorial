#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from collections import defaultdict
from train_perceptron import * #train_perceptronは重みの辞書を返す

def predict_all(weights_dict, test_article):
	for sentence in test_article:
		# print sentence
		features_dict = defaultdict(int)
		features_dict = create_features(sentence)
		print predict_one(weights_dict, features_dict)

def test_perceptron(labelled_input):
	weights_dict = train_perceptron(labelled_input)
	predict_all(weights_dict, open(sys.argv[2]))

if __name__ == "__main__":
	test_perceptron(sys.argv[1])