"""
隣接行列                   隣接リスト
    　  0  1  2  3
        _  _  _  _
    0| -1  1  2 -1         0 -> [1,1],[2,2]
    1|  1 -1  3  2         1 -> [0,1],[2,3],[3,2]
    2|  2  3 -1  1         2 -> [0,2],[1,3],[3,1]
    3| -1  2  1 -1         3 -> [1,2],[2,1]
"""

import queue

"""
プリム法
    入力:prim(頂点数,重み付きグラフ隣接リスト)
    出力:最小全域木の重みの総和　int:EdgeSum
"""

def prim(n,EdgeMatrix):

    EdgeList=queue.PriorityQueue() #探索対象の辺
    used=[False]*n #頂点の使用情報

    used[0]=True #0から探索を始める
    LastNode=0 #最新の頂点
    EdgeSum=0 #重みの合計
    Flag=True #探索対象が残っている時はTrue

    while Flag:
        Flag=False
        for i in range(len(EdgeMatrix[LastNode])):
            #探索していない頂点へ辺があればキューに追加
            Edge=EdgeMatrix[LastNode][i]
            if used[Edge[0]]==False:
                EdgeList.put([Edge[1],Edge[0]])

        #探索していない頂点への最も重みの小さい辺を取り出す
        while not EdgeList.empty():
            minEdge=EdgeList.get()
            if used[minEdge[1]]==False:
                Flag=True
                break

        EdgeSum+=minEdge[0] #辺の合計を増やす
        LastNode=minEdge[1] #最新の頂点を更新
        used[minEdge[1]]=True #頂点の使用情報を更新

    return EdgeSum



"""
ダイクストラ法
    入力:dijkstra(頂点数,重み付きグラフ隣接リスト,始点)
    出力:startを始点とする単一始点最短経路(各点までの最短経路) list:Distance
"""
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



"""
ワーシャルフロイド法
    入力:warshallFloyd(頂点数,重み付きグラフ隣接行列)
    出力:全点対間最短経路 list:l
"""
def warshallFloyd(n,l):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                l[i][j]=min(l[i][j],l[i][k]+l[k][j])
    return l

n,e=map(int,input().split())
l=[[float('inf') for i in range(n)] for i in range(n)]
for i in range(n):
    l[i][i]=0

for i in range(e):
    a,b,c=map(int,input().split())
    l[a][b]=c

distance=warshallFloyd(n,l)

negative=False

for i in range(n):
    if l[i][i]<0:
        negative=True
        break

if negative:
    print("NEGATIVE CYCLE")
else:
    for i in range(n):
        for j in range(n):
            if j:
                print(" ",end='')
            if l[i][j]==float('inf'):
                print("INF",end='')
            else:
                print(l[i][j],end='')
        print()






















"""
プリム法
    入力:prim(頂点数,重み付きグラフ隣接行列)
    出力:最小全域木の重みの総和　int:EdgeSum
"""
def prim(n,EdgeMatrix,start):

    EdgeList=queue.PriorityQueue() #探索対象の辺
    used=[False]*n #頂点の使用情報

    used[0]=True #0から探索を始める
    LastNode=0 #最新の頂点
    count=1 #つないだ頂点の数
    EdgeSum=0 #重みの合計

    while count<n:

        for i in range(n):
            #探索していない頂点へ辺があればキューに追加
            if EdgeMatrix[LastNode][i]!=float('inf') and used[i]==False:
                EdgeList.put([EdgeMatrix[LastNode][i],i])

        #探索していない頂点への最も重みの小さい辺を取り出す
        while True:
            minEdge=EdgeList.get()
            if used[minEdge[1]]==False:
                break

        EdgeSum+=minEdge[0] #辺の合計を増やす
        LastNode=minEdge[1] #最新の頂点を更新
        used[minEdge[1]]=True #頂点の使用情報を更新
        count+=1 #つないだ頂点の数を更新

    return EdgeSum



"""
ダイクストラ法
    入力:dijkstra(頂点数,重み付きグラフ隣接行列,始点)
    出力:startを始点とする単一始点最短経路 list:Distance
"""
def dijkstra(n,EdgeMatrix,start):

    NodeList=queue.PriorityQueue() #探索対象の頂点
    Distance=[float('inf')]*n #startからの最短経路
    used=[False]*n #頂点の使用情報

    Distance[start]=0 #startからstartまでの距離は0
    used[start]=True #startから探索を始める
    LastNode=start #最新の頂点
    count=1 #つないだ頂点の数

    while count<n:
        for i in range(n):
            #探索していない頂点へ距離の短い辺があればキューに追加
            if EdgeMatrix[LastNode][i]!=float('inf') and used[i]==False:
                if Distance[i]>Distance[LastNode]+EdgeMatrix[LastNode][i]:
                    Distance[i]=Distance[LastNode]+EdgeMatrix[LastNode][i]
                    NodeList.put([Distance[i],i])

        #最も近い探索していない頂点
        while True:
            minNode=NodeList.get()
            if used[minNode[1]]==False:
                break

        LastNode=minNode[1] #最新の頂点を更新
        used[minNode[1]]=True #頂点の使用情報を更新
        count+=1 #つないだ頂点の数を更新

    return Distance
