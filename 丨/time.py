import time

def empty():
    return ""

n=100000

start=time.time()
l=[]
for i in range(n):
  l.append(empty())
print(*l,sep="",end="")
end=time.time()
print(end-start)


start=time.time()
for i in range(n):
    print(empty(),end="")
end=time.time()
print(end-start)

n=1000000

start=time.time()
l=[]
for i in range(n):
  l.append(empty())
print(*l,sep="",end="")
end=time.time()
print(end-start)


start=time.time()
for i in range(n):
    print(empty(),end="")
end=time.time()
print(end-start)
