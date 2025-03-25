#hotel ordered

menu = {"vada":5,"pongal":50,"dosa":30,"idly":20}
money=money2=money4=money3=0
i = 1
while(i>0):
 a = input("if you need to order any food type yes or no: ")
 
 if(a == "yes"):
     print("order a food")
     b = input("what do you want 1.vada 2.pongal or 3.idly 4.dosa: ")
     d = int(input("quantity: "))
     if(b=="1"):
        c = menu["vada"]
        money = d*c+money
     if(b=="2"):
      e = menu["pongal"]
      money2 = d*e+money2
     if(b=="3"):
       f = menu["idly"]
       money3=d*f+money3
     if(b=="4"):
       g = menu["dosa"]
       money4=d*g+money4    
 else:
    totalamount = money2+money+money3+money4
    print(totalamount)
    break
    
