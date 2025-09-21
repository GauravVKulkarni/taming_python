text = """
    In the world of programming, Python is popular. 
    The world of coding has many languages, 
    but Python stands out in the world of simplicity.
"""
text = text.lower()
clean_text = text.replace("\n", ' ').replace(".", '').replace(",", '')
words_list = clean_text.split()


words_dict = dict()

for i in words_list:
    words_dict[i] = words_dict.get(i, 0)+1

print(words_dict)