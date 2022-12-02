d = input("Setir daxil edin :") 
z = int(input("Araliq mesafeni qeyd edin :"))


def funk(d,z):
    setir_=[]
    e = 0
    x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    say = len(d)
    if z>26:
        return False 
    for i in range(0,say):
        if d[i].isalpha()==True and d[i]!=" ":
            if d[i]==d[i].upper():
                index = x.index(d[i].lower())
            else:
                index = x.index(d[i])
            if (index+z)>=26:
                e = (index+z)-26
            else:
                e = index+z
            if d[i] == d[i].upper():
                    setir_.append(x[e].upper())
            else:
                setir_.append(x[e])
        elif d[i]==" ":
            setir_.append(" ")
        else:
            pass
        
        setir="".join(setir_)
    return setir 
    
print(funk(d,z))