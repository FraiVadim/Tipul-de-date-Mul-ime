A=set(input('dati elementele multimii A:'))
B=set(input('dati elementele multimii B:'))
A.remove(',')
B.remove(',')
a=b=0
for i in A:
    if ord(i)>64 and ord(i)<91:
        a+=1
for i in B:
    if ord(i)>64 and ord(i)<91:
        b+=1
if len(A)==a and len(B)==b:
    print('intersectia multimilor:',A.intersection(B))
    print('reuniunea multimilor:',A.union(B))
    print('A/B:',A.difference(B))
    print('B/A:',B.difference(A))
else:
    print('dati litere MAJUSCULE!')