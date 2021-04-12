import re
class SimpleBars(list):
    def __init__(self,s):
        self.extend(s)

    def __str__(self):
        return "".join(self)

    def next(self):
        n=len(self)
        t=list(' '*n)
        table=[{ " ":" ", "i":"T", "T":"i"},{ " ":"i", "T":" "}]
        for i in range(n):
            a,b,c=self[(i-1)%n],self[i],self[(i+1)%n]
            count=0
            if a=='i':
                count+=1
            if c=='i':
                count+=1
            t[i]=table[count%2][b]
        self.clear()
        self.extend(t)
        return "".join(self)

class Bars(SimpleBars):
    def next(self):
        n=len(self)
        t=list(' '*n)
        table=[{" ":" ","i":"T","T":"i","I":"I"},{" ":"i","i":"I","T":" ","I":"T"}]
        for i in range(n):
            a,b,c=self[(i-1)%n],self[i],self[(i+1)%n]
            count=0
            if a=='i' or a=='I':
                count+=1
            if c=='i' or c=='I':
                count+=1
            t[i]=table[count%2][b]
        self.clear()
        self.extend(t)
        return "".join(self)

    def prev(self):
        n=len(self)
        bw=[0]*n
        t=list(' '*n)
        table=[{" ":" ","T":"i","i":"T","I":"I"},{"i":" ","I":"i"," ":"T","T":"I"}]
        for i in range(n):
            if self[i]==' ' or self[i]=='i':
                bw[i]=0
            else:
                bw[i]=1
        for i in range(n):
            t[i]=table[(bw[(i-1)%n]+bw[(i+1)%n])%2][self[i]]
        self.clear()
        self.extend(t)
        return "".join(self)

"""
#2nd
bs=SimpleBars(' '*24)
bs[8]='T'
for i in range(30):
    print(bs.next())
"""
"""
bs = SimpleBars(' '*78)
pos = 0; acc = 1; accx = 1; output = ""

commands = "1(///(1iTiTiTi|||[(1 ])1( [L|[L|[L|[(] |1//)/)1i||1)///)1i||||1(///)1i\
(/////)1iTiTi[L!])|])[L!])])l|])1/( [(1/ ]L!l|[(1 ])1( //(1 ]L[L!|"

for c in commands:
    if   c == "1": acc = 1
    elif c == "/": acc = acc * 2
    elif c == ")": pos += acc; pos %= len(bs)
    elif c == "(": pos -= acc; pos %= len(bs)
    elif c == "i" or c == "T" or c == " ":
        for i in range(acc): bs[pos] = c; pos += 1; pos %= len(bs)
    elif c == "]":
        s = str(bs)[pos:]+str(bs)[:pos+1];         m = re.search("^ *[iT]* ", s)
        acc = (m and m.end() - 1) or 0
    elif c == "[":
        t = str(bs); s = t[pos-1]+t[pos:]+t[:pos]; m = re.search(" [iT]* *$", s)
        acc = (m and len(s) - m.start() - 1) or 0
    elif c == "l": acc, accx = accx, acc
    elif c == "L": acc, accx = accx - acc, accx + acc
    elif c == "|": print(bs); bs.next()
    elif c == "!": output += chr((ord('0') + acc) % 128)

print("answer: " + output)

#3rd
from third_code import decode_morse

bs = Bars("I    IT ii  i I   I i   i   I  T")
for i in range(26):
    #print(bs)
    bs.next()

print(bs)

print("answer: " + decode_morse(str(bs)))

#4th
s="ITT TI I T TIii"
bs = Bars(s)
bsub = Bars(s)
bs.next()
while s!="".join(bs):
    bs.next()
    bsub.next()

print(bsub)
# bsub+="I I I  Iii i  I Iii"
print("answer: " + decode_morse(bsub))
"""
