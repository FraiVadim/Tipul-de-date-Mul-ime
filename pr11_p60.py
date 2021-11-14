A={'A','B','C','D'}
for i in A:
    print(i)
    if i=='A':
        print(i,chr(ord(i)+1))
        print(i,chr(ord(i)+2))
        print(i,chr(ord(i)+3))
        print(i,chr(ord(i)+1),chr(ord(i)+2))
        print(i,chr(ord(i)+1),chr(ord(i)+3))
        print(i,chr(ord(i)+2),chr(ord(i)+3))
        print(i,chr(ord(i)+1),chr(ord(i)+2),chr(ord(i)+3))
    if i=='B':
        print(i,chr(ord(i)+1))
        print(i,chr(ord(i)+2))
        print(i,chr(ord(i)+1),chr(ord(i)+2))
    if i=='C':
        print(i,chr(ord(i)+1))
