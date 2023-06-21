#!/usr/bin/env python
# coding: utf-8

# # Bharat Intern - AI Intern
# 
# ## Task 3 - Translator Tool

# In[2]:


from googletrans import Translator
from IPython.display import display, HTML

translator = Translator(service_urls=['translate.google.com'])

def translate_text(text, target_language):
    translation = translator.translate(text, dest=target_language)
    translated_text = translation.text
    source_language = translation.src
    
    display(HTML(f'<b>Source Language:</b> {source_language}'))
    display(HTML(f'<b>Translated Text:</b> {translated_text}'))

while True:
    choice = input("Enter 'q' to quit or 't' to translate: ")
    
    if choice.lower() == 'q':
        print("Quitting the translator tool...")
        break
    
    if choice.lower() == 't':
        text = input("Enter the text to translate: ")
        target_language = input("Enter the target language: ")
        translate_text(text, target_language)
    else:
        print("Invalid choice. Please try again.")


# In[ ]:




