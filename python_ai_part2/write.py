st="hey how are you"
f=open("file4.txt","w")
f.write(st)

f.close()

# if i write it in preexisting file then it erase the previous data and write new data
# so write new file name in f=open("NEW_FILE_NAME")