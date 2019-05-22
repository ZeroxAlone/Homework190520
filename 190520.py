#p1,1
'''
s=str(input(""))
a="a"
e="e"
i="i"
o="o"
u="u"
x=s.count(a)
y=s.count(e)
z=s.count(i)
w=s.count(o)
v=s.count(u)
print("number of vowels is:",x+y+z+w+v)
'''
#p1,2
'''
s=str(input(""))
l=list(s)
nl=[]
b=[]
c=0
f=0
a=""
k="bob"
for y in l:
    c+=1
for i in range(3,c+1):
    for p in range(i-3,i):
        nl.append(s[p])
for w in nl:
    a+=str(w)
for v in range(3,(c-4)*3+7):
    j=a[v-3:v]
    b.append(j)
print("Number of bob:",b.count(k))
print(b)
print(a)
'''
a=0
for i in range(5):
    a+=2
    print(a)
    if a>10:
        break
print("Goodbye!")









