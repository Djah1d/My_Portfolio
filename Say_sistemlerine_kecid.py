def say():
    z = int(input("10-luga cevirmek istediyiniz say sistemini qeyd edin:"))
    a = input("Eded daxil edin :")
    s = 0
    i = 0
    x = int(len(str(a)))
    while i<=x:
        d = int(a[i])*(z**(x-1))
        s=s+d
        x-=1
        i+=1
    return s
print(say())