def count_words(sentence):
    print(sentence.split())
    return len(sentence.split())
text = input("Enter a sentence: ")
print(f"Word count: {count_words(text)}")
