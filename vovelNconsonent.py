def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    vowels_count = sum(1  for char in s if char in vowels)
    consonants_count = sum(1  for char in s if char.isalpha() and char not in vowels)
    return vowels_count, consonants_count

sentence = input("Enter a string: ")
vowels, consonants = count_vowels_consonants(sentence)
print(f"Vowels: {vowels}, Consonants: {consonants}")
