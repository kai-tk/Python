import math
import bisect
from collections import deque

EPS=1e-10
INF=(1<<31)-1

#点クラス
#多角形は点オブジェクトのリスト
class Point:
    def __init__(self,x,y):
        self.vec=Vector(x,y) #位置ベクトル
        self.x=x
        self.y=y

    def __str__(self):
        return '{0:.10f} {1:.10f}'.format(self.x,self.y)

#(ベクトルを持つ)線分クラス
#始点,終点を持つベクトルクラス
class Segment:
    def __init__(self,p,q):
        self.vec=Vector(p,q) #方向ベクトル
        self.start=p
        self.end=q

    def __str__(self):
        return '{0:.10f} {1:.10f}'.format(self.x,self.y)

#円クラス
class Circle:
    def __init__(self,c,r):
        self.c=c #中心
        self.r=r #半径

    def __str__(self):
        return f'{self.c.x} {self.c.y} {self.r}'

#ベクトルクラス
class Vector:
    def __init__(self,A,B):
        #座標から作成
        if type(A) is int or type(A) is float:
            self.x=A
            self.y=B
        #点オブジェクトから作成
        elif type(A) is Point:
            self.x=B.x-A.x
            self.y=B.y-A.y

    def __add__(self,other):
        return Vector(self.x+other.x,self.y+other.y)

    def __sub__(self,other):
        return Vector(self.x-other.x,self.y-other.y)

    def __mul__(self,t):
        return Vector(self.x*t,self.y*t)

    def __str__(self):
        return '{0:.10f} {1:.10f}'.format(self.x,self.y)

    #絶対値
    def norm(self):
        return math.sqrt(dot(self,self))

#ベクトルの内積
def dot(U,V):
    return U.x*V.x+U.y*V.y

#ベクトルの外積
def cross(U,V):
    return U.x*V.y-U.y*V.x

#Pから線分ABへ下ろした垂線の足の位置ベクトル
def project(a,AB,p):
    if type(AB) is Segment:
        AB=AB.vec
    AP=Vector(a,p)
    t=dot(AP,AB)/dot(AB,AB)
    AH=AB*t
    return a.vec+AH

#Pと線分ABで対称な点の位置ベクトル
def reflect(a,AB,p):
    if type(AB) is Segment:
        AB=AB.vec
    OH=project(a,AB,p)
    PH=OH-p.vec
    return p.vec+PH*2

#3点の位置関係
def ccw(a,b,c):
    U=Segment(a,b).vec
    V=Segment(a,c).vec
    #bacが反時計回り
    if cross(U,V)>EPS:
        return 1
    #bacが時計回り
    elif cross(U,V)<-EPS:
        return -1
    #bacの順で直線
    elif dot(U,V)<-EPS:
        return 2
    #abcの順で直線
    elif U.norm()<V.norm():
        return -2
    #acbの順で直線
    else:
        return 0

#平行判定
def isParallel(S,T):
    return abs(cross(S.vec,T.vec))<EPS

#垂直判定
def isOrthogonal(S,T):
    return abs(dot(S.vec,T.vec))<EPS

#線分の交差判定
def isIntersectSS(S,T):
    return ccw(S.start,S.end,T.start)*ccw(S.start,S.end,T.end)<=0 and ccw(T.start,T.end,S.start)*ccw(T.start,T.end,S.end)<=0

#円の交差判定(共通接線の数)
def isIntersectCC(C,D):
    d=distancePP(C.c,D.c)
    sumr=C.r+D.r
    difr=abs(C.r-D.r)
    if d>sumr:
        return 4 #交わらない
    elif d==sumr:
        return 3 #外接
    elif d>difr:
        return 2 #交わる
    elif d==difr:
        return 1 #内接
    else:
        return 0 #内包

#点と点の距離
def distancePP(p,q):
    return Vector(p,q).norm()

#点と直線の距離
def distanceLP(L,p):
    return abs(cross(L.vec,Vector(L.start,p.vec)))/L.vec.norm()

#点と線分の距離
def distanceSP(S,p):
    if dot(Vector(S.start,p),S.vec)<0:
        return (p.vec-S.start.vec).norm()
    elif dot(Vector(S.end,p),S.vec*-1)<0:
        return (p.vec-S.end.vec).norm()
    else:
        return distanceLP(S,p)

#線分と線分の距離
def distanceST(S,T):
    if isIntersect(S,T):
        return 0
    else:
        return min(distanceSP(S,T.start),distanceSP(S,T.end),distanceSP(T,S.start),distanceSP(T,S.end))

#直線の交点
def crossPointLL(S,T):
    d1=distanceLP(S,T.start)
    d2=distanceLP(S,T.end)
    c1=ccw(S.start,S.end,T.start)
    c2=ccw(S.start,S.end,T.end)
    #線分の端点がもう片方の直線上にある
    if c1==0 or c1==2 or c1==-2:
        return T.start
    if c2==0 or c2==2 or c2==-2:
        return T.end
    #線分T(とS)を延長すると交差する
    if c1*c2==1:
        if d1>d2:
            d1,d2=d2,d1
            T=Segment(T.end,T.start)
        t=d1/abs(d1-d2)
        cp=T.start.vec-T.vec*t
    #線分Sを延長すると交差する
    else:
        t=d1/(d1+d2)
        cp=T.start.vec+T.vec*t
    return Point(cp.x,cp.y)

#多角形の面積
def polygonArea(P):
    n=len(P)
    if n<3:
        return 0
    ans=0
    for i in range(n):
        ans+=cross(P[i].vec,P[(i+1)%n].vec)
    return ans/2

#多角形の凸性判定
def isConvex(P):
    n=len(P)
    for i in range(n-1):
        if ccw(P[i],P[i+1],P[(i+2)%n])==-1:
            return False
    return True

#多角形が点を内包するか
def contains(P,p):
    n=len(P)
    c=False
    for i in range(n):
        A=Vector(p,P[i])
        B=Vector(p,P[(i+1)%n])
        if A.y>B.y:
            A,B=B,A
        #点が辺上にある
        if abs(cross(A,B))<EPS and dot(A,B)<EPS:
            return 1
        elif A.y<EPS and B.y>EPS and cross(A,B)>EPS:
            c=not c
    return 2 if c else 0

#凸包(最も下の点から時計回り)
def andrewScan(P):
    n=len(P)
    R=[]
    L=[]
    #逆にすると最も左のものから
    P.sort(key=lambda P:(P.y,P.x))
    if n<3:
        return P
    R.append(P[0])
    R.append(P[1])
    L.append(P[n-1])
    L.append(P[n-2])
    for i in range(2,n):
        r=len(R)
        while r>=2 and ccw(R[r-2],R[r-1],P[i])>=0:
            R.pop()
            r-=1
        R.append(P[i])
    for i in range(n-3,-1,-1):
        l=len(L)
        while l>=2 and ccw(L[l-2],L[l-1],P[i])>=0:
            L.pop()
            l-=1
        L.append(P[i])
    L.reverse()
    for i in range(len(R)-2,0,-1):
        L.append(R[i])
    return L

#凸多角形の直径
def calipers(P):
    P=andrewScan(P)
    n=len(P)
    if n==2:
        return distancePP(P[0],P[1])
    d=0
    i=0
    j=1
    while j<n:
        while j<n-1 and distancePP(P[i],P[j])<distancePP(P[i],P[j+1]):
            j+=1
        d=max(d,distancePP(P[i],P[j]))
        i+=1
        if i==j:
            j+=1
    return d

#凸多角形を直線で切断したときに左側にできる凸多角形
def cutPolygon(P,S):
    n=len(P)
    Q=[]
    for i in range(n):
        c1=ccw(S.start,S.end,P[i])
        c2=ccw(S.start,S.end,P[(i+1)%n])
        PS=Segment(P[i],P[(i+1)%n])
        #直線がある辺と重なる時
        if isParallel(PS,S) and abs(c1)!=1:
            if ccw(S.start,S.end,P[(i+2)%n])==1:
                return P
            else:
                return []
        if c1==1:
            Q.append(P[i])
        if c1*c2<=0:
            Q.append(crossPointLL(PS,S))
    return Q

def closestPair(P):
    P.sort(key=lambda P:(P.x))
    return closest_Pair(P)

def closest_Pair(P):
    n=len(P)
    if n<=1:
        return INF
    m=n//2
    x=P[m].x
    d=min(closest_Pair(P[:m]),closest_Pair(P[m:]))
    P.sort(key=lambda P:P.y)
    L=[]
    for i in range(n):
        if abs(P[i].x-x)<d:
            for j in range(len(L)):
                if P[i].y-L[-j-1].y>=d:
                    break
                d=min(d,distancePP(P[i],L[-j-1]))
            L.append(P[i])
    return d

#マンハッタン幾何
def manhattanIntersection(S):
    M=[]
    for s in S:
        dx=s.vec.x
        t=Segment(s.end,s.start)
        if dx==0:
            M.append(s)
            M.append(t)
        elif dx>0:
            M.append(s)
        else:
            M.append(t)

    M.sort(key=lambda S:(S.start.y,-S.vec.y))
    L=deque()
    ans=0
    for s in M:
        dy=s.vec.y
        if dy==0:
            ans+=bisect.bisect(L,s.end.x)-bisect.bisect_left(L,s.start.x)
        elif dy>0:
            bisect.insort_left(L,s.start.x)
        else:
            del L[bisect.bisect_left(L,s.start.x)]
    return ans

#三角形の3辺から面積
def heron(a,b,c):
    s=(a+b+c)/2
    return math.sqrt(s*(s-a)*(s-b)*(s-c))

#三角形の内接円
def inscribedCircle(P):
    c=Vector(P[0],P[1]).norm()
    a=Vector(P[1],P[2]).norm()
    b=Vector(P[2],P[0]).norm()
    d=a+b+c
    C=P[0].vec*(a/d)+P[1].vec*(b/d)+P[2].vec*(c/d)
    R=2*heron(a,b,c)/d
    return Circle(C,R)

def circumscribedCircle(P):
    a=P[0].x
    b=P[0].y
    c=P[1].x
    d=P[1].y
    e=P[2].x
    f=P[2].y
    y=((e-a)*(a*a+b*b-c*c-d*d)-(c-a)*(a*a+b*b-e*e-f*f))/(2*(e-a)*(b-d)-2*(c-a)*(b-f))
    if c==a:
        x=(2*(b-f)*y-a*a-b*b+e*e+f*f)/(2*(e-a))
    else:
        x=(2*(b-d)*y-a*a-b*b+c*c+d*d)/(2*(c-a))
    C=Point(x,y)
    R=distancePP(C,P[0])
    return Circle(C,R)

P=[]
for i in range(3):
    x,y=map(float,input().split())
    P.append(Point(x,y))
print(circumscribedCircle(P))
