# input is some text
# output is a dictionary of words and the number of times they've been repeated
# e.g:
# input: "I I have ice-cream"
# output: "I: 2, have: 1, ice-cream, 1"

text = input("Please enter some text: ")
# print(text)

word_list = text.lower().split(' ')
# print(word_list)

res = {}
for word in word_list:
    if (word in res):
        res[word] = res[word]+1
    else:
        res.update({word:1})

print(res)

# extension: what if there is not always only one space?