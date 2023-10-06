s=[6,3,9,2,1]
c=0
for i in range(len(s)-1):
    for j in range(i+1,len(s)):
        if s[i]>s[j]:
            c+=1
print(c)