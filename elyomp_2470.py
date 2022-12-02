n = int(input())
x = []
for i in range(n): 
    lst = list(map(int, input().split()))
    x.append(lst)

def funk(x):
    d = 0
    say=len(x)
    for z in range(say):
        for j in range( say):
            if x[z][j]==x[j][z]:
                d+=1
                if z == j and x[z][j]==1:             
                    return "NO"
            else:
                continue
            
    if d ==n**2 :
        return "YES"
    else:
        return "NO"

print(funk(x))