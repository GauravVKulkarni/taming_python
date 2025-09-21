text = "Python is an amazing programming language!"

vowels = 0
consonants = 0
vowel_set = {'a', 'e', 'i', 'o', 'u'}
consonants_set = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'}

text = text.lower()

for i in text:
    if i in vowel_set:
        vowels+= 1
    elif i in consonants_set:
        consonants += 1

print(f"Vowels: {vowels} Consonants: {consonants}")