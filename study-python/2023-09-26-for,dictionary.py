#순서에 따라서 데이터 저장 할 때: list #
#데이터에 이름을 주고 싶을 때 dictionary #

person = {'name':'rms','adress':'Gumi','interest':'Web'}
for key in person:
    print(key, person[key])
    #print(key, person['adress'])

print('---')

persons = [
    {'name':'r','adress':'Gumi','interest':'Web'},
    {'name':'m','adress':'Ulsan','interest':'Iot'},
    {'name':'s','adress':'Seoul','interest':'ML'}
]
for peo in persons:
    for key in peo:
        print(key,':', peo[key])
    print('---------------------')