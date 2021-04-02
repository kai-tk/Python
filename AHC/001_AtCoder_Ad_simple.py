# coding: utf-8
# Your code here!

import bisect
import math
from copy import deepcopy

def area(a,b,c,d):
    return (c-a)*(d-b)

n=int(input())

office=[]

for i in range(n):
    x,y,r=map(int,input().split())
    office.append((x,y,r,i))

office.sort(key=lambda o:o[2])

Upper=[(10000,0,10000)]
Lower=[(0,0,10000)]
Left=[(10000,0,10000)]
Right=[(0,0,10000)]

for x,y,r,i in office:
    Upper.append((y,x,x+1))
    Lower.append((y+1,x,x+1))
    Left.append((x,y,y+1))
    Right.append((x+1,y,y+1))

ans=0

ANS=[]
p=0

upper=deepcopy(Upper)
lower=deepcopy(Lower)
left=deepcopy(Left)
right=deepcopy(Right)

for s,t,r,i in office:
    a,b,c,d=s,t,s+1,t+1
    aa,bb,cc,dd=a,b,c,d
    index=bisect.bisect(lower,(b+1,0,0))-1
    for y,x1,x2 in lower[index::-1]:
        if not (x2<=a or x1>=c):
            b=min(max(y,d-int(r//(c-a))),bb)
            break
    index=bisect.bisect(right,(a+1,0,0))-1
    for x,y1,y2 in right[index::-1]:
        if not (y2<=b or y1>=d):
            a=min(max(x,c-int(r//(d-b))),aa)
            break
    index=bisect.bisect(upper,(d,0,0))
    for y,x1,x2 in upper[index:]:
        if not (x2<=a or x1>=c):
            d=max(min(y,b+int(r//(c-a))),dd)
            break
    index=bisect.bisect(left,(c,0,0))
    for x,y1,y2 in left[index:]:
        if not (y2<=b or y1>=d):
            c=max(min(x,a+int(r//(d-b))),cc)
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
    p+=1-pow((1-min(r,area(a,b,c,d)/max(r,area(a,b,c,d)))),2)

    ANS.append((a,b,c,d,i,s,t,r))

if p>ans:
    ANS2=deepcopy(ANS)
    ans=p

ANS=[]
p=0

upper=deepcopy(Upper)
lower=deepcopy(Lower)
left=deepcopy(Left)
right=deepcopy(Right)

for s,t,r,i in office:
    a,b,c,d=s,t,s+1,t+1
    aa,bb,cc,dd=a,b,c,d
    index=bisect.bisect(right,(a+1,0,0))-1
    for x,y1,y2 in right[index::-1]:
        if not (y2<=b or y1>=d):
            a=min(max(x,c-int(r//(d-b))),aa)
            break
    index=bisect.bisect(upper,(d,0,0))
    for y,x1,x2 in upper[index:]:
        if not (x2<=a or x1>=c):
            d=max(min(y,b+int(r//(c-a))),dd)
            break
    index=bisect.bisect(left,(c,0,0))
    for x,y1,y2 in left[index:]:
        if not (y2<=b or y1>=d):
            c=max(min(x,a+int(r//(d-b))),cc)
            break
    index=bisect.bisect(lower,(b+1,0,0))-1
    for y,x1,x2 in lower[index::-1]:
        if not (x2<=a or x1>=c):
            b=min(max(y,d-int(r//(c-a))),bb)
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
    p+=1-pow((1-min(r,area(a,b,c,d)/max(r,area(a,b,c,d)))),2)

    ANS.append((a,b,c,d,i,s,t,r))

if p>ans:
    ANS2=deepcopy(ANS)
    ans=p

ANS=[]
p=0

upper=deepcopy(Upper)
lower=deepcopy(Lower)
left=deepcopy(Left)
right=deepcopy(Right)

for s,t,r,i in office:
    a,b,c,d=s,t,s+1,t+1
    aa,bb,cc,dd=a,b,c,d
    index=bisect.bisect(upper,(d,0,0))
    for y,x1,x2 in upper[index:]:
        if not (x2<=a or x1>=c):
            d=max(min(y,b+int(r//(c-a))),dd)
            break
    index=bisect.bisect(left,(c,0,0))
    for x,y1,y2 in left[index:]:
        if not (y2<=b or y1>=d):
            c=max(min(x,a+int(r//(d-b))),cc)
            break
    index=bisect.bisect(lower,(b+1,0,0))-1
    for y,x1,x2 in lower[index::-1]:
        if not (x2<=a or x1>=c):
            b=min(max(y,d-int(r//(c-a))),bb)
            break
    index=bisect.bisect(right,(a+1,0,0))-1
    for x,y1,y2 in right[index::-1]:
        if not (y2<=b or y1>=d):
            a=min(max(x,c-int(r//(d-b))),aa)
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
    p+=1-pow((1-min(r,area(a,b,c,d)/max(r,area(a,b,c,d)))),2)

    ANS.append((a,b,c,d,i,s,t,r))

if p>ans:
    ANS2=deepcopy(ANS)
    ans=p

ANS=[]
p=0

upper=deepcopy(Upper)
lower=deepcopy(Lower)
left=deepcopy(Left)
right=deepcopy(Right)

for s,t,r,i in office:
    a,b,c,d=s,t,s+1,t+1
    aa,bb,cc,dd=a,b,c,d
    index=bisect.bisect(left,(c,0,0))
    for x,y1,y2 in left[index:]:
        if not (y2<=b or y1>=d):
            c=max(min(x,a+int(r//(d-b))),cc)
            break
    index=bisect.bisect(lower,(b+1,0,0))-1
    for y,x1,x2 in lower[index::-1]:
        if not (x2<=a or x1>=c):
            b=min(max(y,d-int(r//(c-a))),bb)
            break
    index=bisect.bisect(right,(a+1,0,0))-1
    for x,y1,y2 in right[index::-1]:
        if not (y2<=b or y1>=d):
            a=min(max(x,c-int(r//(d-b))),aa)
            break
    index=bisect.bisect(upper,(d,0,0))
    for y,x1,x2 in upper[index:]:
        if not (x2<=a or x1>=c):
            d=max(min(y,b+int(r//(c-a))),dd)
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
    p+=1-pow((1-min(r,area(a,b,c,d)/max(r,area(a,b,c,d)))),2)

    ANS.append((a,b,c,d,i,s,t,r))

if p>ans:
    ANS2=deepcopy(ANS)


ANS2.sort(key=lambda o:o[4])

for a,b,c,d,i,x,y,r in ANS2:
    print(a,b,c,d)
