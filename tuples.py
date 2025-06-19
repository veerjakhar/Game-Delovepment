stuDeatails = ('Veer', 90)

# Packing
address = ('777', 'Gasharpoon', "Forsaken", "Roblox", "Macbook")

for x in address:
    print(x, end = ' ')

# Unpacking
house_number, street_name, city, state, country = address

print()
print(house_number)
print(street_name)
print(city)
print(state)
print(country)

# A tuple can also be created without using parenthesis
life = 1, 3, 7, 9, 10, 11, 'Sigma'

print(life)

# Nested tuple
ntuple = ("Veer", [8, 11, 40, 44], (2020, 2023, 2025, 0000))

print(ntuple[1][2])
print(ntuple[0][3])

# Tuple slicing
stuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'n', 'g')

print(stuple[-3:])

#stuple[3] = 'a'