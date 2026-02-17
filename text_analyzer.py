# AI Text Analyzer
# Analyzes text statistics and readability

import string

def analyze_text(text):
    words = text.split()
    sentences = text.split(".")
    
    num_words = len(words)
    num_sentences = len(sentences)
    num_chars = len(text)
    
    avg_word_length = sum(len(word.strip(string.punctuation)) for word in words) / num_words if num_words > 0 else 0
    
    return {
        "Words": num_words,
        "Sentences": num_sentences,
        "Characters": num_chars,
        "Average Word Length": round(avg_word_length, 2)
    }

if __name__ == "__main__":
    sample_text = input("Enter text to analyze: ")
    results = analyze_text(sample_text)
    
    print("\nAnalysis Results:")
    for key, value in results.items():
        print(f"{key}: {value}")
