from turtle import color


cat = ['big', 'greeen', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]

print(size)

# Enumerate
supplies = ['pen', "stepler", "pencil", "papka"]
for index, item in enumerate(supplies):
    print("Index"+ str(index) + ' : ' + item)


import random
pets = ['Dog', "Cat", "los"]
a = random.choice(pets)
print(a)
