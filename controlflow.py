#hotel ordered

menu = {"vada":5,"pongal":50,"dosa":30,"idly":20}
stack = {"vada":10,"pongal":20,"dosa":10,"idly":15}
money=0
stackofvada=0
i = 1
while(i>0):
 a = input("if you need to order any food type y/Y or n/N: ")
 
 if(a == "y" or a=="Y"):
     print("order a food menu is 1.vada 2.pongal 3.dosa 4.idly")
     ordered = int(input("what do you want: "))
     if(ordered < 5):
         quantity = int(input("quantity: "))
         if(ordered==1):
             if(stack["vada"]>=quantity):
              stack["vada"] = stack["vada"]-quantity
              c = menu["vada"]
              money = quantity*c+money
             else:
              print(" vada no stack")
      
         if(ordered==2):
            if(stack["pongal"]>=quantity):
             stack["pongal"]=stack["pongal"]-quantity
             e = menu["pongal"]
             money = quantity*e+money
            else:
               print("pongal no stack")
         if(ordered==3):
              if(stack["dosa"]>=quantity):
                stack["dosa"]=stack["dosa"]-quantity
                f = menu["dosa"]
                money=quantity*f+money
              else:
                 print("no stack in dosa")
         if(ordered==4):
             if(stack["idly"]>=quantity):
                stack["idly"]=stack["idly"]-quantity
                g = menu["idly"]
                money=quantity*g+money 
             else:
                print("no stack in idly")

     else:
       print("number not in menu") 
 else:
    totalamount = money
    print(totalamount)
    break
    
