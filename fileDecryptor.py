import os
directory=input("enter the path to encrypt files:")
filename=os.listdir(directory)
alpha="abcdefghijklmnopqrstuvwxyz"
alpha=list(alpha)
alpha.append('\n')
ft=""
p=0
diff=0
key=input("Enter a Key:")
d=dict()
for i in range(len(alpha)):
     d[alpha[i]]=i
for t in range(len(filename)):
        st=filename[t]
        ft=""
	with open(directory+st) as f:
	    file_str = f.read()
	#Encryption part
	ckey=""
	for i in range((len(file_str)//len(key))):
	    if i%2==0:
		ckey=ckey+key
	    else:
		ckey=ckey+key[::-1]
        if len(ckey)<len(file_str):
            diff=abs(len(file_str)-len(ckey))
            ckey=ckey+('k'*diff)
	for i in range(len(file_str)):
	    p=d[file_str[i]]-d[ckey[i]]
	    if p<0:
               p=27+p
	    ft=ft+alpha[p]
	with open(directory+st, "w") as f:
	    f.write(ft)
        f.close()
