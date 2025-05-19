from collections import defaultdict

def minTime(n, edges, hasApple):
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u) 
    
    def dfs(node, parent):
        time = 0
        for neighbor in tree[node]:
            if neighbor == parent:
                continue 
        
            cost = dfs(neighbor, node) 
            
            if cost > 0 or hasApple[neighbor]:  
                time += cost + 2  
            
        return time

    return dfs(0, -1)

print(minTime(7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [False,False,True,False,True,True,False]))  # Output: 8
print(minTime(7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [False,False,True,False,False,True,False])) # Output: 6
print(minTime(7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [False,False,False,False,False,False,False])) # Output: 0
