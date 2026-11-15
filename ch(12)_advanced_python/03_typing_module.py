from typing import List, Tuple,Dict,Union,Set

'''  Why we need this typing module?
ans:1. because of the 'subscript problem' before(3.9) version when we write list[int] it throw error.
  2. Catch bug early , if you write "hello" in List[int] your editor turns it into red before you
  even hit.
  3. good read-ability

'''

# List of integers:
numbers: List[int] = [1,2,3,4,5]

# Tuple of a string and integer:
person: Tuple[str,int] = ("Alice",40 , "Bob",23)

# Dictionary with string keys and integer values
scores: Dict[str,int]={"Alice":34 , "Harry":20 , "Lovely":35}

# set with string and integer
marks:Set[str,int]={"Alice",34,"gugu",56,37}

# Union types of variable that can hold multiple types:
identifier: Union[int,str]="1DB234","USR-99"
identifier = 12345    # also valid

print(numbers,type(numbers),end="   " )
print(person,type(person),end="     ")
print(scores,type(scores),end="    ")
print(marks,type(marks),end="    ")
print("   ")