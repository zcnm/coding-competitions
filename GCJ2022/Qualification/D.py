# chain reactions

def solve(funFactors, pointers):
    # treat structure like tree with void pointers as roots
    # assume there could be multiple pointers to void
    terminals = []
    paths = {}
    
    for i in range(len(pointers)):
        if pointers[i] == 0:
            terminals.append(i)
        else:
            if pointers[i] - 1 not in paths:
                paths[pointers[i] - 1] = []
            paths[pointers[i] - 1].append(i)
        
    def dfs(terminal):
        if terminal not in paths:
            return funFactors[terminal]
        
        current = funFactors[terminal]
        while len(paths[terminal]) == 1:
            terminal = paths[terminal][0]
            current = max(current, funFactors[terminal])
            if terminal not in paths:
                return current
        children = []
        for child in paths[terminal]: 
            children.append(dfs(child))
        children.sort()
        if len(children) > 1:
            for child in children[1:]:
                total[0] += child 
                
        current = max(current, children[0])
        return current 
    total = [0]
    
   
    for terminal in terminals:
        if terminal not in paths:
            total[0] += funFactors[terminal]
        else:
            children = []
            for child in paths[terminal]:
                children.append(dfs(child))
            children.sort()
            if len(children) > 1:
                for child in children[1:]:
                    total[0] += child 
            
            current = max(funFactors[terminal], children[0])
            total[0] += current       
            
    return total[0]
        
def main():
    T = int(input())
    for i in range(T):
        numMachines = int(input())
        funFactors = list(map(int, input().split()))
        pointers = list(map(int, input().split()))
        ans = solve(funFactors, pointers)
        output = "Case #{}: {}".format(i + 1, ans)
        print(output)

if __name__ == "__main__":
    main()