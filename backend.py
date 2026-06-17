import heapq, csv, time
import pandas as pd
import matplotlib.pyplot as plt
from collections import deque

ROWS=25
DIRS=[(0,1),(0,-1),(1,0),(-1,0)]

# ---------- ALGORITHMS ----------
def heuristic(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

def bfs(start,goal,snake):
    q=deque([(start,[])])
    vis=set()
    while q:
        cur,path=q.popleft()
        if cur==goal: return path
        for d in DIRS:
            nxt=(cur[0]+d[0],cur[1]+d[1])
            if 0<=nxt[0]<ROWS and 0<=nxt[1]<ROWS and nxt not in snake and nxt not in vis:
                vis.add(nxt); q.append((nxt,path+[d]))
    return []

def dfs(start,goal,snake):
    st=[(start,[])]
    vis=set()
    while st:
        cur,path=st.pop()
        if cur==goal: return path
        for d in DIRS:
            nxt=(cur[0]+d[0],cur[1]+d[1])
            if 0<=nxt[0]<ROWS and 0<=nxt[1]<ROWS and nxt not in snake and nxt not in vis:
                vis.add(nxt); st.append((nxt,path+[d]))
    return []

def astar(start,goal,snake):
    heap=[(0,start,[])]
    vis=set()
    while heap:
        _,cur,path=heapq.heappop(heap)
        if cur==goal: return path
        if cur in vis: continue
        vis.add(cur)
        for d in DIRS:
            nxt=(cur[0]+d[0],cur[1]+d[1])
            if 0<=nxt[0]<ROWS and 0<=nxt[1]<ROWS and nxt not in snake:
                g=len(path)+1; h=heuristic(nxt,goal)
                heapq.heappush(heap,(g+h,nxt,path+[d]))
    return []

def hamiltonian_cycle():
    path=[]
    for y in range(ROWS):
        row=list(range(ROWS))
        if y%2: row.reverse()
        for x in row: path.append((x,y))
    return path

# ---------- DATA ----------
def save_result(mode,score,steps,start):
    with open("results.csv","a",newline="") as f:
        csv.writer(f).writerow([mode,score,steps,round(time.time()-start,2)])

def show_graph():
    data=pd.read_csv("results.csv",header=None)
    data.columns=["Algorithm","Score","Steps","Time"]

    data["Score"]=pd.to_numeric(data["Score"],errors="coerce")
    data=data.dropna()

    grouped=data.groupby("Algorithm")["Score"].mean()

    print("\nCOMPARISON TABLE:\n",grouped)

    plt.bar(grouped.index,grouped.values)
    plt.title("Algorithm Comparison")
    plt.show()