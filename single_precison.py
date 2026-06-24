from storage import *

def floattoIEEE754(i):
    true_value = [0]*10#getting the true value of this trial
    a = i
    for j in range(10):
        true_value[9-j] = a%10
        a //= 10
    #print(true_value)

    #converting to IEEE754
    sign = str(int(i<0))#getting sign digit (should always be 0)
    
    base = 0#repeatidly multiply by 2 until 1s digit is nonzero
    product = true_value[:]
    while product[0] == 0:
        product = multiplyby2(product)
        base += 1
        #print(product)

    exponent10 = 127 - base#getting the exponent
    exponent = bin(exponent10)[2:]
    while len(exponent) < 8:
        exponent = '0' + exponent
    #print(exponent)

    fraction = ''#getting the fraction
    for i in range(23):
        product[0] = 0
        product = multiplyby2(product)
        fraction += str(product[0])
        #print(product)
    product[0] = 0
    product = multiplyby2(product)
    if product[0] == 1:#round up
        fraction = increment(fraction)
    #print(fraction)

    word = sign + exponent + fraction#oh yeah, its coming together
    return word

def IEEE754tofloat(word):
    sign = word[0]#spliting into components
    exponent = word[1:9]
    fraction = word[9:]
    #print(sign,exponent,fraction)

    base = int(exponent,2) - 127#getting the base
    #print(base)

    halfdecs = open('halfdecs.txt','r').read().split()
    decimal = '0'
    for i in range(23):#looping through entire fraction
        if bool(int(fraction[i])):
            decimal = add(decimal,halfdecs[i])
    decimal = float('1.'+''.join(decimal))
    expobias = 2**base
    output = decimal * expobias
    if bool(int(sign)):
        output *= -1
    return output

totalupls = 0
for i in range(0,1000000000,10):#from 0 to 1 with 9 decimal digits
    if i != 0:
        original = printdec(i)
        word = floattoIEEE754(i)
        floating = IEEE754tofloat(word)
        totalupls += abs(original-floating)
        if i%100000==0:
            print(original,floating,totalupls)
            w = open('spr_data.txt','a')
            w.write(f'org:{original} flo:{floating} total:{totalupls}\n')
print(totalupls)