sen = input("Type in the sentence: ")
vowels = 0
sent = {
    "a":0,
    "e":0,
    "i":0,
    "o":0,
    "u":0
}

for k in  sen:
    if k in sent:
        sent[k] = sent[k] + 1

for count in sent.values():
    vowels = vowels + count

print(count)
