A=set(input('dati elementele multimii A:'))
B=set(input('dati elementele multimii B:'))
A.remove(',')
B.remove(',')
a=b=0
for i in A:
    if i.isdigit() :
        a+=i.isdigit()
for i in B:
    if i.isdigit() :
        b+=i.isdigit()
if len(A)==a and len(B)==b:
    print('intersectia multimilor:',A.intersection(B))
    print('reuniunea multimilor:',A.union(B))
    print('A/B:',A.difference(B))
    print('B/A:',B.difference(A))
else:
    print('dati cifre!')
   