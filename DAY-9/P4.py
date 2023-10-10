#Reverse the given string and keeping its special char at same place
#example:input:srin#ivas,output:savi#nirs,input:we@lcome,output:em@oclem,input:pyth#on,output:noht#yp
def demo(s):
    l=[]
    for i in s:
        if i.isalpha():
            l.append(i)
        else:
            spc=i
            idxspc=s.index(i)
    l.reverse()
    l.insert(idxspc,spc)
    return ''.join(l)
s=input()
print(demo(s))
        