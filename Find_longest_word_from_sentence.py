"""
Problem Statement
Find Longest words from given sentence.
Example 1
Input string: "I like Python"
Output: ["Python"]
Example 2:
Input string: "He likess Python"
Output: ["Likess", "Python"]
Example 3:
Input string: "He likess Python 00a:=bcd"
Output: ["Likess", "Python", "00abcd"]
"""

import re

def longest_words(sentence, remove_special_char=True):
	"""Finds the longest words in a given sentence, optionally removing special_char.
	

	Args:
		sentence: The input sentence.
		remove_special_char: If True, removes special_char before finding longest words.

	Returns:
		A list of the longest words in the sentence.
	"""

	if remove_special_char:
		# enter regex pattern which you want to remove from sentence
		sentence = re.sub(r'[^\w\s]', '', sentence)

	words = sentence.split(" ")
	if len(words) > 0:
		max_length = len(max(words, key=len))
		longest_words_list = [word for word in words if len(word) == max_length]
		return longest_words_list 
	else:
		return "Empty string."

sentence = "He likess Python 00a:=bcd"
output = longest_words(sentence)
print(output)