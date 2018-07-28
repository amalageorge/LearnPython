def break_words(stuff):
   	words = stuff.split(' ')
	return words

def sort_words(words):
	return sorted(words)

def print_first_word(words):
	words = words.pop(0)
	print words

def print_last_words(words):
	words = words.pop(-1)
	print words

def sort_sentence(sentence):
	words = break_words(sentence)
	return sort_words(words)

def print_first_last_sentence(sentence):
	words = break_words(sentence)
	print_first_word(words)
	print_last_words(words)

def print_first_last_sorted(sentence):
	print_first_word(words)
	print_last_words(words)
