x = ['apple','grape','banana','kiwi','orange']

print("length of list:",len(x))
print("first element:",x[0])
print("last element:",x[-1])


x.append('papaya')
print("updated list:",x)

x.remove('grape')
print('updated list;',x)

x.sort()
print('sorted list:',x)

x.pop(1)
print("updated list:",x)

x.reverse()
print("reversed list:",x)

print("multiplication on list:",x*2)

x = x[:4]
print ("sliced list:",x)

x.clear()
print("updated list:",x)