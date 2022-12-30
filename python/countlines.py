f=open("doc.txt",mode='a+')

f.seek(0)
n=len(f.readlines())
print("The no of lines are ",n)
f.close()


