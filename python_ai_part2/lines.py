# f=open("file3.txt")

# lines=f.readlines()
# print(lines,type(lines))

# f.close()                        # it gives aas a list with \n 



f=open("file3.txt")

line1=f.readline()
print(line1,type(line1))

line2=f.readline()
print(line2,type(line2))

line3=f.readline()
print(line3,type(line3))

line4=f.readline()
print(line4,type(line4))

line5=f.readline()
print(line5,type(line5))

 # if i give space between lines then it consider space as line and give space a string type

line6=f.readline()
print(line6,type(line6)) 

# it does not print any line if there is no next line but if write to print type then it print string to en empty line as type 
line7=f.readline()
print(line7=="",type(line7))       

 # GIVES TRUE as output i.e. line7=="" means line 7 is empty so it gives true means really line 7 has no line

f.close()
