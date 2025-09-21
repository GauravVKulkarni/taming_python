sentence = "Data science is fun"

words_list = list(sentence.split(" "))

reversed_sentence = ""

reversed_sentence += words_list[len(words_list) - 1]

for i in range (len(words_list) - 2 , -1, -1):
    reversed_sentence += " "
    reversed_sentence += words_list[i]

print(reversed_sentence)