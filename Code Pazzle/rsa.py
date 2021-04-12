def lets_take_tea_break(m,e,n,c):
    if pow(m,e)%n==c: return str(m)
    return ""

def solveD(e,EulerN):
    i=0
    #e*d=Φ(n)*i+1
    while True:
        if (EulerN*i+1)%e==0:
            return (EulerN*i+1)//e
        i+=1

m=1758412232636122750
e = 65537
n = 47775743999999999999 # TODO: this bit length is too short for RSA!
c=26984024434151540355

#n=p*q
p=6912000001
q=6911999999
EulerN=(p-1)*(q-1)

d=solveD(e,EulerN)
print(d)

print(pow(c,d,n))
print(lets_take_tea_break(m,e,n,c))
