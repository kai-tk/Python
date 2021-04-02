"""
E - Two Currencies
https://atcoder.jp/contests/abc164/tasks/abc164_e
"""

import queue
def dijkstra(n,EdgeMatrix,start):

    NodeList=queue.PriorityQueue() #探索対象の頂点
    Distance=[float('inf')]*n #頂点0からの最短経路
    used=[False]*n #頂点の使用情報

    Distance[start]=0 #0から0までの距離は0
    used[start]=True #0から探索を始める
    LastNode=start #最新の頂点
    Flag=True #探索対象が残っている時はTrue

    while Flag:
        Flag=False
        for i in range(len(EdgeMatrix[LastNode])):
            #探索していない頂点へ距離の短い辺があればキューに追加
            Edge=EdgeMatrix[LastNode][i]
            if used[Edge[0]]==False and Distance[Edge[0]]>Distance[LastNode]+Edge[1]:
                    Distance[Edge[0]]=Distance[LastNode]+Edge[1]
                    NodeList.put([Distance[Edge[0]],Edge[0]])

        #最も近い探索していない頂点
        while not NodeList.empty():
            minNode=NodeList.get()
            if used[minNode[1]]==False:
                Flag=True
                break

        LastNode=minNode[1] #最新の頂点を更新
        used[minNode[1]]=True #頂点の使用情報を更新
    return Distance

#入力
n,m,s=map(int,input().split())

#辺の隣接リスト
EdgeMatrix=[[] for i in range(125000)]

for i in range(m):
    u,v,a,b=map(int,input().split())
    for j in range(a,2500):
        EdgeMatrix[(u-1)*2500+j].append([(v-1)*2500+j-a,b])
        EdgeMatrix[(v-1)*2500+j].append([(u-1)*2500+j-a,b])

for i in range(n):
    c,d=map(int,input().split())
    for j in range(2450):
        EdgeMatrix[i*2500+j].append([min(i*2500+j+c,(i+1)*2500-1),d])

#for i in range(2502):
#    print(EdgeMatrix[i])

#頂点0からの最短経路
Distance=dijkstra(125000,EdgeMatrix,min(s,2499))

for i in range(1,n):
    print(min(Distance[i*2500:(i+1)*2500-1]))
