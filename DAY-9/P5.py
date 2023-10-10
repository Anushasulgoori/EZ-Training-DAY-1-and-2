#input: A string of comma separated numbers are given such that the numbers are given such that the numbers 4 and 7 are already available in the list
#Assumption: 7 always comes after 4 in the given string
#Number 1: add all numbers which do not lie b/w 4 and 7(excluding 4 and 7) in the given input
#Number 2:numbers formed by cancatinating all numbers from 4 to 7(including 4 and 7)
#OUTPUT:sum of num 1 and num2,Example:2,5,1,4,3,2,7,8,Number 1: 2+5+1+8,Number 2: '4'+'3'+'2'+'7'='4327',OUTPUT: 16+4327=434
def demo(s):
    los=s.split(',')
    idxpof=los.index('4')
    idxpos=los.index('7')
    n1,n2=0,''
    for i in los[:idxpof]+los[idxpos+1:]:
        n1+=int(i)
    for i in los[idxpof:idxpos+1]:
        n2+=i
    return (n1+int(n2))
s=input()
if __name__=='__main__':
    print(demo(s))