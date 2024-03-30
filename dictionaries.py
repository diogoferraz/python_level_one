my_stuff={"key1":123,"key2":"value2","key3":{"123":[1,2,"grabMe"]}}

print(my_stuff["key2"])  # value2
print(my_stuff["key3"]["123"][2])  # grabMe
print(my_stuff["key3"]["123"][2].upper())  # GRABME

my_stuff["key4"]=123
print(my_stuff)  # {'key1': 123, 'key2': 'value2', 'key3': {'123': [1, 2, 'grabMe']}, 'key4': 123}
