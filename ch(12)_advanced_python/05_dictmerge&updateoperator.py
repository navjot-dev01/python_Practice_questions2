# dict1={'a': 2 , 'b': 4 }
# dict2={'b': 3 , 'd' : 6}   # output= {'a':2,'b':3,'d':6} dict. is mutable it gives value after updation

dict1={'a': 2 , 'b': 4 }
dict2={'c': 3 , 'd' : 6}

merged = dict1 | dict2
print(merged)