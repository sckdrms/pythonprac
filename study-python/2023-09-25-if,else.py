print(0)
if True:
    print(1)
else:
    print(2)
print(3)

print('---')

print(0)
if False:
    print(1)
else:
    print(2)
print(3)
'''
0
1
3
---
0
2
3
'''

print('---')
input_id = input('id: ')
id = 'rms'
if input_id == id:
    print('Welcome')
else: 
    print('Who?')

