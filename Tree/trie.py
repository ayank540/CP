class Trie:
	def __init__(self):
		self._end  = '*'
		self.trie = {}

	def __repr__(self):
		return repr(self.trie)

	def make_trie(self, *words):
		trie = {}
		for word in words:
			temp_dict = trie
			for letter in word:
				temp_dict = temp_dict.setdefault(letter, {})
			temp_dict[self._end] = self._end
		return trie

	def find_word(self, word):
		sub_trie = self.trie
		for letter in word:
			if letter in sub_trie:
				sub_trie =  sub_trie[letter]
			else:
				return False
		else:
			if self._end in sub_trie:
				return True
			else:
				return False

	def add_word(self, word):
		if self.find_word(word):
			print("Already there, no worries!")
			return self.trie
		temp_trie = self.trie
		for letter in word:
			if letter in temp_trie:
				temp_trie = temp_trie[letter]
			else:
				temp_trie = temp_trie.setdefault(letter, {})
		temp_trie[self._end] = self._end
		return temp_trie

if __name__ == '__main__':
	my_trie = Trie()
	trie = my_trie.make_trie('hi', 'hello', 'howdy')
	print(trie)
