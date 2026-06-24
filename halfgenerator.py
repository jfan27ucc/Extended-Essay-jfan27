f = open('halfdecs.txt','w')
for i in range(1,65):
    dec = str(5**i)
    while len(dec) < i:
        dec = '0' + dec
    f.write(f'{dec}\n')
