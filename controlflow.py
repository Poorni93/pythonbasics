#hotel ordered

menu = {"vada":5,"pongal":50,"dosa":30,"idly":20}

a,b,c,d = map(str,input("enter the menu items").split())
e,f,g,h = map(int,input("enter the item count").split())
totalamount:int
sum=sum3=sum1=sum2 = 0
if(a=="vada"):
    sum = menu["vada"]
    sum = e*sum
    
if(b=="pongal"):
    sum1 = menu["pongal"]
    sum1 = f*sum1
if(c=="dosa"):
    sum2 = menu["dosa"]
    sum2 = g*sum2
if(d=="idly"):
    sum3 = menu["idly"]
    sum3 = h*sum3
else:
    print("not in the menu")

totalamount = sum + sum1+sum2+sum3
print(totalamount)