"""
合計値がs以上になる最小の区間
"""

n,s=map(int,input().split())
a=list(map(int,input().split()))
left=0
right=0
S=0
INF=(1<<31)-1
ans=INF

for left in range(n):
    while right<n and S<s:
        S+=a[right]
        right+=1
    if(S<s):
        break
    ans=min(ans,right-left)
    S-=a[left]
    if(left==right):
        right+=1

if ans==INF:
    ans=0
print(ans)
