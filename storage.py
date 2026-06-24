def increment(word):
    word = list(word)
    for i in range(len(word)-1,-1,-1):
        if word[i] == '1':
            word[i] = '0'
        elif word[i] == '0':
            word[i] = '1'
            break
    return ''.join(word)

def multiplyby2(product):
    carry = False#carried digit
    for j in range(9,-1,-1):#multiply by 2 (adding by itself)
        product[j] *= 2
        if carry:
            product[j] += 1
            carry = False
        if product[j] > 9:
            product[j] -= 10
            carry = True
    return product

def add(addend1,addend2):
    addend1 = list(addend1)
    addend2 = list(addend2)
    length = max(len(addend1),len(addend2))
    while len(addend1) < length:
        addend1.append('0')
    while len(addend2) < length:
        addend2.append('0')
    sum = []
    carry = False
    for i in range(length-1,-1,-1):
        digit = int(addend1[i])+int(addend2[i])+int(carry)
        carry = False
        if digit > 9:
            carry = True
            digit -= 10
        sum.insert(0,str(digit))
    return sum

def printdec(i):
    true_value = [0]*10#getting the true value of this trial
    a = i
    for j in range(10):
        true_value[9-j] = a%10
        a //= 10
    true_value = list(map(str,true_value))
    return float(f'{true_value[0]}.{''.join(true_value[1:])}')