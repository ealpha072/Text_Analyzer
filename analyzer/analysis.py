#This file contains general analysis functions
#analyser.py

import argparse
import sys
import os

def analyze_document(text):
    """
    Perform a general analysis of given text.

    Parameters:
    -text (str): THe text to be analysed

    Returns: 
    -dict: A dictionary conating values of the analysis
    """
    word_count = count_words(text)
    sentence_count = count_sentenses(text)
    paragraph_count = count_paragraphs(text)

    analysis_results = {
            'word_count': word_count,
            'sentence_count': sentence_count,
            'paragraph_count': paragraph_count
    }

    return analysis_results

def count_words(text):
    """Count number of words in the given text.

    Parameters:
    -text (str): Text to be analyzed

    Returns:
    -int:the number of words
    """
    split_text = text.split(" ")
    return (len(split_text))

def count_sentenses(text):
    """Count number of sentenses.
    Parameters:
    -text (str): Text to be analyzed
    Returns:
    -int: Number of sentences
    """
    count = 0
    separators = ['.', '!', '?']

    for char in text:
        if char in separators:
            count+=1
    return count

def count_paragraphs(text):
    """Count number of paragraphs.
    Parameters:
    -text (str): Text to be analyzed
    Returns:
    -int: Number of paragraphs
    """
    split_text = text.split('\n\n')
    return (len(split_text))

def read_file(file_path):
    """Read path to file.

    Parameters:
    -file_path (path): Path to file 

    Returns:
    content: content of the read file
    """
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")

def main():
    parser = argparse.ArgumentParser(description='Count number of words in text or file')
    parser.add_argument("input", help="Text or file path to analyse")
    parser.add_argument("-a", "--all", action="store_true", help="All analysis")
    parser.add_argument("-wc", "--word-count", action="store_true", help="Count words")
    parser.add_argument("-sc", "--sentense-count", action="store_true", help="Count sentense")
    parser.add_argument("-pc", "--paragraph-count", action="store_true", help="Count number of paragraphs")

    args = parser.parse_args()

    #check if input argument is a file path

    if os.path.isfile(args.input):
        file_name, file_extension = os.path.splitext(args.input)
        if file_extension != '.txt':
            print("Allowed document type is txt")
            sys.exit(1)

        document_text = read_file(args.input)
    else:
        document_text = args.input

    if args.word_count:
        words = count_words(document_text)
        print(f"Words: {words}")

    if args.sentense_count:
        results = count_sentenses(document_text)
        print(f"Sentence: {results}")

    if args.paragraph_count:
        results = count_paragraphs(document_text)
        print(f"Paragraphs: {results}")

    if args.all:
        results = analyze_document(document_text)
        print(results)

if __name__ == "__main__":
    main()


