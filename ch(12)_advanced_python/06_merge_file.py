                           # Exam - friendly
# with open('file1.txt','r') as f1 , open('file2.txt','r') as f2 , open('merged.txt' , 'w') as fout:
#     fout.write(f1.read())

#     fout.write("\n\n")

#     fout.write(f2.read())
    
                            # merge file line by line:
# with open('file2.txt','r') as f2 , open('file3.txt','r') as f3 , open('merged_01.txt' , 'w') as fout:
#     for line in f2:
#         fout.write(line)

#     fout.write("\n\n")
#     for line in f3:
#         fout.write(line)

                          # merge multiple line using list   
files=["file1.txt","file2.txt","file3.txt"]

with open("merged_02.txt",'w') as fout:
    for file in files:
        with open(file,'r') as fin:
            fout.write(fin.read())
            fout.write("\n\n")
    
    