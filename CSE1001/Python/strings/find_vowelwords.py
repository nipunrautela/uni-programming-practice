import re

sentence = input("Enter the sentence: ")
vowel_count = 0
for word in sentence.split(' '):
    if re.match("[aeiouAEIOU].*", word):
        vowel_count += 1;

print("Number of words starting with vowel:", vowel_count) 