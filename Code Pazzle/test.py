from functools import reduce

def lets_take_tea_break(m,e,n,c):
    if pow(m,e)%n==c: return str(m)
    return ""
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
morse={
        "iI":"A",
        "Iiii":"B",
        "IiIi":"C",
        "Iii":"D",
        "i":"E",
        "iiIi":"F",
        "IIi":"G",
        "iiii":"H",
        "ii":"I",
        "iIII":"J",
        "IiI":"K",
        "iIii":"L",
        "II":"M",
        "Ii":"N",
        "III":"O",
        "iIIi":"P",
        "IIiI":"Q",
        "iIi":"R",
        "iii":"S",
        "I":"T",
        "iiI":"U",
        "iiiI":"V",
        "iII":"W",
        "IiiI":"X",
        "IiII":"Y",
        "IIii":"Z",
        "iIIII":"1",
        "iiIII":"2",
        "iiiII":"3",
        "iiiiI":"4",
        "iiiii":"5",
        "Iiiii":"6",
        "IIiii":"7",
        "IIIii":"8",
        "IIIIi":"9",
        "IIIII":"0",
        "iIiiIi":"\"",
        "iIIIIi":"\'",
        "iIiIiI":".",
        "IIiiII":",",
        "IIIiii":":",
        "iiIIii":"?",
        "iiIIiI":"_",
        "iIiIi":"+",
        "IiiiiI":"-",
        "iiiiii":"^",
        "IiiIi":"/",
        "iIIiIi":"@",
        "IiIIi":"(",
        "IiIIiI":")"
    }
def decode_morse(code):
    s=""
    text=""
    for i in range(len(code)):
        if code[i]==" ":
            if s!="":
                text+=morse[s]
            s=""
        else:
            s+=code[i]
    return text
def encode_morse(text):
    code=""
    for i in range(len(text)):
        code = [k for k, v in morse.items() if v == text[i]][0]
    return code
def encode_hash(value,n):
    v=pow(4,n-1)
    bars=Bars(" "*n)
    for i in range(n):
        bars[i]=chars[value//v]
        value-=(value//v)*v
        v//=4
    if value==0:
        return bars

chars = " iTI"
Bars.xor = lambda self, i, x: self.__setitem__(i, chars[chars.index(self[i]) ^ chars.index(x)])
Bars.num = lambda self: reduce(lambda a,b: a*4+chars.index(b), self, 0)
verify_RSA_signature = lets_take_tea_break

correctHash=1758412232636122750
e = 65537
n = 47775743999999999999
signature=26984024434151540355

def solve(data):
    bars = Bars(" "*32)
    bars_pos = 0

    for c in data:
        c = c.upper()
        code = encode_morse(c)
        for i in code:
            bars.xor(bars_pos, i)
            bars_pos += 1
            bars_pos %= len(bars)
        bars_pos += 1
        bars_pos %= len(bars)
        print(bars)
        bars.next()
        print(bars)

    hash_value = bars.num()
    if verify_RSA_signature(hash_value, e, n, signature):
        print("verification succeeded!")
    #else:
        #print("verification failed")

solve("exit()")

"""
bars=Bars(" iT iTiI T TTiTIITITIITTi iTiIIT")
print(bars.prev())
#         "T iT iTI i IITIIIiIiIIiI   iTiII"
bars=Bars("T iT iTI i IITIIIi         iTiII")
print(bars.prev())
#         "IT iT IiTTTiIiIIi           iTiI"
bars=Bars("IT iT IiTTTi                iTiI")
print(bars.prev())
#         "IIT i ITIiI                  iTi"
bars=Bars("IIT i ITIi                   iTi")
print(bars.prev())
#         "iIITTTiii                     iT"
bars=Bars("iIITTTi                       iT")
print(bars.prev())
#         "TiIiiI                         i"
bars=Bars("Ti                             i")
print(bars.prev())

#i          E
#IiiI       X
#ii         I
#I          T
#IiIIi      (
#IiIIiI     )
"""
