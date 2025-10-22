#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)

import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True

#Function to get the sentence
def get_sentence():
    while True:
        print("Enter a sentence: ")
        sentence = input()
        if is_sentence(sentence):
            return sentence
        else:
            print("Error: Please enter a valid sentence.")

#Function to calculate the word frequencies 
def calculate_frequencies(sentence):
    words = []
    frequencies = []

    #remove punctuation 
    sentence_remove = sentence[:-1].lower()

    #split the list
    word_list = sentence_remove.split()

    #count word frquencies
    for word in word_list:
        if word in words:
            index = words.index(word)
            frequencies[index] += 1
        else:
            words.append(word)
            frequencies.append(1)
    return words, frequencies


#Function to print word frequencies 
def print_frequincies(words, frequincies):
    print("\nWord Frequencies: ")
    for i in range(len(words)):
        print(f"{words[i]}: {frequincies[i]}")

# main function
def main():
    sentence = get_sentence()
    words, freqs = calculate_frequencies(sentence)
    print_frequincies(words, freqs)

if __name__ == "__main__":
    main() 
