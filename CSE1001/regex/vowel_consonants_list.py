import re

sentence = input()
vowel_words, consonant_words = [], []

for word in sentence.replace(r"[\./,]", " ").split(" "):
    if re.match("[AEIOUaeiou].*", word):
        vowel_words.append(word)
    elif re.match("^[A-Z].*", word):
        consonant_words.append(word)
print(vowel_words)
print(consonant_words)
