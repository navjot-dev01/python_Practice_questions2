'''
Docstring for chapters._05_map_filter_reduce

MAP: Har element pr same function apply karta hai.
FILTER: Condition ke base pr elements ko select karta hai.
REDUCE: list ke hr element ko combine krke single value bnata hai. 'isko pehle import krna padta hai'.
'''
from functools import reduce

                           # MAP EXAMPLE>>>>>>>
my_list=[1,2,3,4,5]                 # don't use list as variable because it is built in function

square=lambda x:x*x

# sqlist=map(square,my_list)              # it shows output - map object at 0x0001B69d...., convert it into list
sqlist=list(map(square,my_list))
print(sqlist)


#                     FILTER EXAMPLE>>>>>>

def even(n):
    if(n%2==0):
        return True
    return False

onlyEven=filter(even,my_list)
print(list(onlyEven))

#          REDUCE EXAMPLE>>>>>>

def sum(a,b):
    return a+b

mul=lambda x,y: x*y

print(reduce(mul,my_list))
print(reduce(sum,my_list))