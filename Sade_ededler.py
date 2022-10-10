x = int(input("Eded daxil edin:"))
def funk(x):
    d = x
    z = 0
    while x>0:
        if d%x==0:
            z=z+1
        x=x-1
    def funk2(z):
        if z==1 or z==0:
            return False
        elif z == 2:
            return True 
        else:
            return False
    return funk2(z)

print(funk(x))
