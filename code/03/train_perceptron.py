#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from collections import defaultdict

def create_features(sentence):
	features_dict = defaultdict(int) #ここで初期化しないと一行前のunigram素性の値が残るため初期化する必要がある
	word_list = sentence.strip().split()
	for word in word_list:
		features_dict[word] += 1

	return features_dict

def predict_one(weights_dict, features_dict):
	measure_score = 0
	for word, features_value in features_dict.iteritems():
		measure_score += weights_dict[word]

	if measure_score >= 0:
		return 1
	else:
		return -1

def update_weights(weights_dict, features_dict, label):
	for word, features_value in features_dict.iteritems():
		weights_dict[word] += label * features_value

#
def train_perceptron(labelled_input):
	weights_dict = defaultdict(int)

	for line in open(labelled_input):
		(label, sentence) = line.strip().split("\t")
		label = float(label)
		features_dict = create_features(sentence)
		predict_label = predict_one(weights_dict, features_dict)
		if predict_label != label:
			update_weights(weights_dict, features_dict, label)

	return weights_dict

if __name__ == "__main__":
	for k,v in sorted(train_perceptron(sys.argv[1]).iteritems(), key=lambda x:x[0], reverse=False):
		print "UNI:%s\t%s" % (k,v)
