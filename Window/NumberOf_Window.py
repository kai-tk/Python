"""
合計値がs以下になる区間の個数
"""

n,q=[int(x) for x in input().split()]
a=[int(x) for x in input().split()]
ss=[int(x) for x in input().split()]

def two_pointers(s):
    left=0
    S=0
    ans=0
    for right in range(n):
        S+=a[right]
        while S>s:
            S-=a[left]
            left+=1
        ans+=right-left+1
    return ans

for s in ss:
    print(two_pointers(s))
