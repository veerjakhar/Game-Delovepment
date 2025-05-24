num = input("Enter a number: ")

numCount = {
    "1":0,
    "2":0,
    "3":0,
    "4":0,
    "5":0,
    "6":0,
    "7":0,
    "8":0,
    "9":0,
    "0":0
}

for i in num:
    if i in numCount:
        numCount[i] =  numCount[i] + 1

panagram = True

for count in numCount.values():
    if count == 0:
        panagram = False

if panagram:
    print("This is a pananagram")
else:
    print("This is not a panagram")