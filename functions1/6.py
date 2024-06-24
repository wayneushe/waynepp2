def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence=' '.join(reversed(words))
    return reversed_sentence
#example 
sentence = "My name is Wayne"
print(reverse_words("My name is Wayne"))