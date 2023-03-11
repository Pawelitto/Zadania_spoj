b = int(input())

for i in range(b):
    a = list(input())
    p = 0
    rev = a[::-1]
    while True:

        b = int(''.join([x for x in a]))
        c = int(''.join([x for x in rev]))

        if [int(x) for x in str(b)] == [int(x) for x in str(c)]:
            break
        else:
            b = b + c
            rev = list(map(str, [int(x) for x in str(b)][::-1] ))
            a = list(map(str, [int(x) for x in str(b)] ))
            p += 1
    
    print('{} {}'.format(b, p))