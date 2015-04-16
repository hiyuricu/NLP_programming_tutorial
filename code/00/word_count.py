#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from collections import defaultdict

def word_count():
	count_of = defaultdict(int)
	for line in sys.stdin:
		for word in line.strip().split():
			count_of[word] += 1
	return count_of

if __name__ == "__main__":
	for k,v in sorted(word_count().items(), key=lambda x:x[1], reverse=True):
		print k,v