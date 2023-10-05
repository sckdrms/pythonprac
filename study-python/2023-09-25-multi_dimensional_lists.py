people = [
    ['r', 'morning', 'a'],
    ['m', 'launch', 'b'],
    ['s', 'dinner', 'c']
]
print(people[0][0])

for person in people:
    print(person[0]+','+person[1]+','+person[2])

print('---')

person = ['r', 'morning', 'a']
name = person[0]
task = person[1]
alphabet = person[2]
print(name, task, alphabet)

print('---')

name, task, alphabet = ['r', 'morning', 'a']
print(name, task, alphabet)

print('---')

name, task, alphabet = person
print(person)

print('---')

for name, task, alphabet in people:
    print(name, task, alphabet)

# print('---')

# a = 0
# b = 0
# for person in people:
#     print(people[a][b])
#     a = a+1

#     if a == 2:
#         a = 0
#         b = b+1
#         print(people[a][b])

#         if a == 2:
#             a = 0
#             b = b+1
#             print(people[a][b])


    