def kok():
    a = int(input("a deyisenini daxil edin :"))
    b = int(input("b deyisenini daxil edin :"))
    c = int(input("c deyisenini daxil edin :"))
    d = (b**2)-4*a*c
    x1 = (-b+(d**0.5))/(2*a)
    x2 = (-b-(d**0.5))/(2*a)
    if d==0: 
        print("Tenliyin 2 eyni koku var")
        return x1,x2
    elif d>0 :
        print("Tenliyin 2 ferqli koku var")
        return x1,x2
    else:
        return "Tenliyin kokleri yoxdur"
print(kok())