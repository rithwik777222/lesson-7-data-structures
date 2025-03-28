x = {}

x = {1:'apple',2:'ball'}

x = {'name':'jack','age':26}
x = {'name':'john',1:[2,3,4]}

print(x['name'])
print(x.get('age'))

x['age'] = 27
print(x)

x['address'] = 'downtown'
print(x)

x.pop('age')
print(x)