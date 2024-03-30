myfirstlist = [1, 2, 3, 4, 5]
mymixlist = [1, 2, 3, 'string', 4.5, [1, 2, 3], True]

print(mymixlist)
print(myfirstlist[0])  # 1
print(myfirstlist[1:])  # [2, 3, 4, 5]

myfirstlist.append("new item")
print(myfirstlist)  # [1, 2, 3, 4, 5, 'new item']
myfirstlist.extend([6, 7, 8])
print(myfirstlist)  # [1, 2, 3, 4, 5, 'new item', 6, 7, 8]

item = myfirstlist.pop()
print(myfirstlist)  # [1, 2, 3, 4, 5, 'new item', 6, 7]
print(item)  # 8

myfirstlist.reverse()
print(myfirstlist)  # [7, 6, 'new item', 5, 4, 3, 2, 1]