import queue

INFTY=float('inf')

#ダイクストラ法
def dijkstra(n,EdgeMatrix,start):

    NodeList=queue.PriorityQueue() #探索対象の頂点
    Distance=[INFTY]*n #頂点0からの最短経路
    used=[False]*n #頂点の使用情報

    Distance[start]=0 #0から0までの距離は0
    used[start]=True #0から探索を始める
    LastNode=start #最新の頂点
    count=1 #つないだ頂点の数
    NodeList.put([0,start])

    while not NodeList.empty():
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
                break

        LastNode=minNode[1] #最新の頂点を更新
        used[minNode[1]]=True #頂点の使用情報を更新
    return Distance

#入力
n=int(input())

#辺の隣接リスト
EdgeMatrix=[[] for i in range(n)]
for i in range(n):
    l=(list(map(int,input().split())))
    for j in range(l[1]):
        EdgeMatrix[l[0]].append([l[2*j+2],l[2*j+3]])

#頂点0からの最短経路
Distance=dijkstra(n,EdgeMatrix,0)

for node,distance in enumerate(Distance):
    print(node,distance)
