import bisect
import math

def area(a,b,c,d):
    return (d-b)*(c-a)

def search1(s,t):
    l=[]
    a=-1
    m=-1
    lower.sort()
    right.sort()
    index=bisect.bisect(lower,(t+1,0,0))-1
    if index<n and lower[index+1][0]==t:
        index+=1
    for y,x1,x2 in lower[index::-1]:
        index2=bisect.bisect(right,(s+1,0,0))-1
        for x,y1,y2 in right[index2::-1]:
            if y2>y:
                a=x
                break
        if a>=m:
            l.append((a,y))
            m=a
        if x2>s:
            return l

def search2(s,t):
    l=[]
    a=10001
    m=10001
    upper.sort()
    left.sort()
    index=bisect.bisect(upper,(t+1,0,0))
    if index>0 and upper[index-1][0]==t:
        index-=1
    for y,x1,x2 in upper[index:]:
        index2=bisect.bisect(left,(s,0,0))
        for x,y1,y2 in left[index2:]:
            if y1<y:
                a=x
                break
        if a<=m:
            l.append((a,y))
            m=a
        if x1<s:
            return l

def dead(e,f,g,h):
    lower.remove((h,e,g))
    upper.remove((f,e,g))
    left.remove((e,f,h))
    right.remove((g,f,h))
    for i in range(10000):
        for x,y1,y2 in right:
            if y1<=i<y2:
                flag=True
                for a,b,c,d,ii,s,t,r in ANS:
                    if a<=x<c and b<=x<d:
                        flag=False
                for a,b,c,d,ii,s,t,r in ANS2:
                    if a<=x<c and b<=x<d:
                        flag=False
                for a,b,c,d in deadAll:
                    if a<=x<c and b<=i<d:
                        flag=False
                if flag:
                    lower.append((i+1,x,x+1))
                    upper.append((i,x,x+1))
                    left.append((x,i,i+1))
                    right.append((x+1,i,i+1))
                    lower.sort()
                    right.sort()
                    upper.sort()
                    left.sort()
                    return (x,i,x+1,i+1)


n=int(input())

office=[]

for i in range(n):
    x,y,r=map(int,input().split())
    office.append((x,y,r,i))

office.sort(key=lambda o:-o[2])

upper=[(10000,0,10000)]
lower=[(0,0,10000)]
left=[(10000,0,10000)]
right=[(0,0,10000)]

for x,y,r,i in office:
    upper.append((y,x,x+1))
    lower.append((y+1,x,x+1))
    left.append((x,y,y+1))
    right.append((x+1,y,y+1))

ANS=[]
p=0

for x,y,r,i in office:
    U=search1(x,y)
    V=search2(x+1,y+1)
    s=0
    ans=(0,0,10000,10000)
    for a,b in U:
        for c,d in V:
            if a>=c or b>=d:
                continue
            if area(a,b,c,d)>s:
                s=area(a,b,c,d)
                ans=(a,b,c,d)
            if s>=r and c-a<d-b:
                break

    if s>r:
        a,b,c,d=ans
        w=c-a
        h=d-b
        while True:
            if w>h:
                nw=math.ceil(r/h)
                nh=h
            else:
                nw=w
                nh=math.ceil(r/w)
            if nw==w and nh==h:
                break
            w,h=nw,nh
        ans=(a,b,a+nw,b+nh)

    a,b,c,d=ans

    if not (a<=x<c and b<=y<d):
        dx=max(0,x+1-c)
        dy=max(0,y+1-d)
        ans=(a+dx,b+dy,c+dx,d+dy)

    upper.remove((y,x,x+1))
    lower.remove((y+1,x,x+1))
    left.remove((x,y,y+1))
    right.remove((x+1,y,y+1))

    a,b,c,d=ans
    upper.append((b,a,c))
    lower.append((d,a,c))
    left.append((a,b,d))
    right.append((c,b,d))

    #print((x,y),r,U,V)
    #print(a,b,c,d)

    ANS.append((a,b,c,d,i,x,y,r))

    s=area(a,b,c,d)
    p+=1-pow((1-min(r,s)/max(r,s)),2)

ANS.sort(key=lambda o:area(o[0],o[1],o[2],o[3]))

S=[]
ANS2=[]
R=1

deadAll=[]

for a,b,c,d,i,s,t,r in ANS:
    aa,bb,cc,dd=a,b,c,d
    index=bisect.bisect(lower,(b+1,0,0))-1
    for y,x1,x2 in lower[index::-1]:
        if not (x2<=a or x1>=c):
            b=min(max(y,d-int(r*R//(c-a))),bb)
            break
    index=bisect.bisect(right,(a+1,0,0))-1
    for x,y1,y2 in right[index::-1]:
        if not (y2<=b or y1>=d):
            a=min(max(x,c-int(r*R//(d-b))),aa)
            break
    index=bisect.bisect(upper,(d,0,0))
    for y,x1,x2 in upper[index:]:
        if not (x2<=a or x1>=c):
            d=max(min(y,b+int(r*R//(c-a))),dd)
            break
    index=bisect.bisect(left,(c,0,0))
    for x,y1,y2 in left[index:]:
        if not (y2<=b or y1>=d):
            c=max(min(x,a+int(r*R//(d-b))),cc)
            break
    lower.remove((dd,aa,cc))
    upper.remove((bb,aa,cc))
    left.remove((aa,bb,dd))
    right.remove((cc,bb,dd))
    lower.append((d,a,c))
    upper.append((b,a,c))
    left.append((a,b,d))
    right.append((c,b,d))
    lower.sort()
    right.sort()
    upper.sort()
    left.sort()

    deadRemove=[]
    deadAppend=[]
    deadFlag=False

    for e,f,g,h,ii,ss,tt,rr in S:
        if (e<=a<g and f<=b<h) or (e<c<=g and f<=b<h) or (e<=a<g and f<d<=h) or (e<c<=g and f<d<=h):
            ANS2.remove((e,f,g,h,ii,ss,tt,rr))
            deadRemove.append((e,f,g,h,ii,ss,tt,rr))
            e,f,g,h=dead(e,f,g,h)
            ANS2.append((e,f,g,h,ii,ss,tt,rr))
            deadAppend.append((e,f,g,h,ii,ss,tt,rr))
            deadAll.append((e,f,g,h))

    for e,f,g,h,ii,ss,tt,rr in deadRemove:
        S.remove((e,f,g,h,ii,ss,tt,rr))
    for e,f,g,h,ii,ss,tt,rr in deadAppend:
        S.append((e,f,g,h,ii,ss,tt,rr))

    S.append((a,b,c,d,i,s,t,r))
    ANS2.append((a,b,c,d,i,s,t,r))

ANS2.sort(key=lambda o:o[4])

for a,b,c,d,i,x,y,r in ANS2:
    print(a,b,c,d)
