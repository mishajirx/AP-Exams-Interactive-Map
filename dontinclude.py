s = input()
s = s.replace('!', '.').replace("?", '.')
sents = s.split('.')
text = [[] for i in range(len(sents))]
for i in range(len(sents)):
    word = ""
    for letter in sents[i]:
        if letter.isalnum():
            word += letter
        elif word:
            text[i].append(word)
            word = ""
    if word:
        text[i].append(word)
result = ""
for q in input().split():
    a, b, c = map(int, q.split('.'))
    try:
        symb = text[a - 1][b - 1][c - 1]
        result += symb
    except IndexError:
        print(a, b, c)
        if a-1 < len(text):
            print(text[a - 1], b-1)
        result += " "

print(result)
