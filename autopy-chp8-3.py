import re

file1 = open('readfile.txt', 'r')
content = file1.read()
mad_lib_words = list(content.split())
file1.close()

adj_regex = re.compile(r'ADJECTIVE')
noun_regex = re.compile(r'NOUN')
adv_regex = re.compile(r'ADVERB')
verb_regex = re.compile(r'VERB')

result_file = open('resultfile.txt', 'w')
result_string = ""

for word in mad_lib_words:
    if adj_regex.match(word):
        input_adj  = input("Give an adjective: ")
        word = adj_regex.sub(input_adj, word)
    elif noun_regex.match(word):
        input_noun = input("Give an noun: ")
        word = noun_regex.sub(input_noun, word)
    elif verb_regex.match(word):
        input_adv  = input("Give an adverb: ")
        word = verb_regex.sub(input_adv, word)
    elif adv_regex.match(word):
        input_verb  = input("Give an verb: ")
        word = adv_regex.sub(input_verb, word)

    result_string += word + " "
    result_file.write(word + " ")

print(result_string)
result_file.close()