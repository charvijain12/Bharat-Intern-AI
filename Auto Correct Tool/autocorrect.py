#!/usr/bin/env python
# coding: utf-8

# # Bharat Intern - AI Intern 

# In[1]:


import re
from collections import Counter

def words(text):
    return re.findall(r'\w+', text.lower())

def train(features):
    model = Counter(features)
    return model

def autocorrect(word, word_model):
    candidates = known([word], word_model) or known(edits1(word), word_model) or known(edits2(word), word_model) or [word]
    return max(candidates, key=word_model.get)

def known(words, word_model):
    return set(w for w in words if w in word_model)

def edits1(word):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
    inserts = [L + c + R for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def edits2(word):
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))

# Example usage
word_list = words(open('big.txt').read())
word_model = train(word_list)

misspelled_word = 'alibity'
corrected_word = autocorrect(misspelled_word, word_model)

print(f"Original word: {misspelled_word}")
print(f"Corrected word: {corrected_word}")

