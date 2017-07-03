x = '3141592653589793238462643383279502884197169399375105820974944592'
y = '2718281828459045235360287471352662497757247093699959574966967627'

n = int(len(x))

a = int(x[:n/2])
b = int(x[n/2:])
c = int(y[:n/2])
d = int(y[n/2:])

ac = a*c
ad = a*d
bc = b*c
bd = b*d

karatsuba = ((10**n)*ac) + ((10**(n/2))*(ad + bc)) + bd
multiple = int(x)*int(y)

print karatsuba
print multiple