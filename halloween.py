import random

adjective_list = []
file = open('adjectives.txt','r')
while (file.readline() != ""):

    split = file.readline().split('\n')
    adjective_list.append(split[0])

file.close()


costume_file = open('costumes.txt','r')
costume_list = []

while(costume_file.readline() != ''):

    split = costume_file.readline().split('\n')
    costume_list.append(split[0])
costume_file.close()

# print(costume_list)
print(f"Your halloween costume is {random.choice(adjective_list)} {random.choice(costume_list)}")

