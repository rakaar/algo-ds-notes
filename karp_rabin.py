# code from brilliant.org
# using base 26
# mapping each alpahbet to its position => a: 1, b: 2, .... z:26
# not using modulus to avoid headache


class RollingHash:
    def __init__(self, text, word_size):
        self.text = text
        self.word_size = word_size

        self.hash = 0
        for i in range(word_size):
            self.hash += (ord(self.text[i]) - 97 + 1)* (26**(self.word_size - 1 - i))
        print("self.hash ", self.hash)
        self.window_start = 0
        self.window_end = self.word_size

    def move_window(self):
        if self.window_end <= len(self.text)-1:
            self.hash -= (ord(self.text[self.window_start]) - 97 + 1)* (26**(self.word_size - 1))
            self.hash *= 26 # to make the numbers move left => increase base power by 1
            self.hash += ord(self.text[self.window_end]) - 97 + 1
            self.window_start += 1
            self.window_end += 1



def karp_rabin(word, text):
    word_hash = 0
    for i in range(len(word)):
        word_hash += (ord(word[i]) - 97 + 1)* (26**(len(word) - 1 - i))
    
    rolling_hash = RollingHash(text, len(word))
    for i in range(len(text) - len(word) + 1):
        if rolling_hash.hash == word_hash:
            window_word = text[rolling_hash.window_start:rolling_hash.window_end]
            if word == window_word:
                print("match found ", word)
        rolling_hash.move_window()


karp_rabin("ab", "abcdab")