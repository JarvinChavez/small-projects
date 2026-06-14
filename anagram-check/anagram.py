word_one = "listen"
word_two = "silent"

def anagram(word_one, word_two):
    if len(word_one) != len(word_two):
        return False
    
    return sorted(word_one) == sorted(word_two)
    
print(anagram(word_one=word_one, word_two=word_two))