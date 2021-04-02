import queue

INFTY=float('inf')

#プリム法
def prim(n,EdgeMatrix):

    EdgeList=queue.PriorityQueue() #探索対象の辺
    used=[False]*n #頂点の使用情報

    used[0]=True #0から探索を始める
    LastNode=0 #最新の頂点
    count=1 #つないだ頂点の数
    EdgeSum=0 #重みの合計

    while count<n:

        for i in range(len(EdgeMatrix[LastNode])):
            #探索していない頂点へ辺があればキューに追加
            Edge=EdgeMatrix[LastNode][i]
            if used[Edge[0]]==False:
                EdgeList.put([Edge[1],Edge[0]])

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


#入力
n=int(input())

#辺の隣接リスト
EdgeMatrix=[[] for i in range(n)]
for i in range(n):
    l=list(map(int,input().split()))
    for j in range(n):
        if l[j]!=-1:
            EdgeMatrix[i].append([j,l[j]])
            EdgeMatrix[j].append([i,l[j]])

#最小全域木の重みの総和
print(prim(n,EdgeMatrix))
