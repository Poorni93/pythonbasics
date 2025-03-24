#hotel ordered

menu = {"vada":5,"pongal":50,"dosa":30,"idly":20}
money=money2=money4=money3=0
i = 1
while(i>0):
 a = input("if you need to order any food type yes or no: ")
 
 if(a == "yes"):
     print("order a food")
     b = input("what do you want vada pongal or idly dosa: ")
     d = int(input("quantity: "))
     if(b=="vada"):
        c = menu["vada"]
        money = d*c
     if(b=="pongal"):
      e = menu["pongal"]
      money2 = d*e
     if(b=="idly"):
       f = menu["idly"]
       money3=d*f
     if(b=="dosa"):
       g = menu["dosa"]
       money4=d*g     
 else:
    totalamount = money2+money+money3+money4
    print(totalamount)
    break
    
