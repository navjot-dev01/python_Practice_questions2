# a=45                 # global variable

def fun():
    global a
    a=3               # Local variable if global is not written
    print(a)

a=89                  # global variable bec. outside the function
print(a)
fun()
print(a)