p = 23
# what is inefficient?
# everytime i am calculating the ord of the strings unnecesaarily
# can use numbers to speed it up
def calculate_hash(sentence):
    nums = [str(ord(c)) for c in sentence]
    number = int("".join(nums))
    hash_num = number % p
    return hash_num

# print("hash is ",calculate_hash("abc"))

sentence = "the quick fox jumps the dog"
word = "the"

hash_of_word = calculate_hash(word)

def match():
    first_substr = sentence[:len(word)]
    if calculate_hash(first_substr) == hash_of_word:
        if word == first_substr:
            print(first_substr)
            print("found match")
    prev_substr = first_substr
    for c in sentence[len(word):]:
        new_substr = prev_substr[1:] + c
        if calculate_hash(new_substr) == hash_of_word:
            if word == new_substr:
                print(new_substr)
                print("found match")
        prev_substr = new_substr

match()