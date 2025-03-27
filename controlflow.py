#hotel ordered

menu = {"vada":5,"pongal":50,"dosa":30,"idly":20}
stack = {"vada":10,"pongal":20,"dosa":10,"idly":15}

money=0
stackofvada=0
i = 1
while(i>0):
 a = input("if you need to order any food type y/Y or n/N: ")
 
 if(a == "y" or a=="Y"):
     print("order a food menu is 1.vada 2.pongal 3.idly 4.dosa ")
     ordered = int(input("what do you want: "))
     if(ordered < 5):
         quantity = int(input("quantity: "))
         if(ordered=="1"):
             sv=stack["vada"]
             stackofvada =  sv - quantity
             print(stackofvada)
             if(stackofvada>=0):
              c = menu["vada"]
              money = quantity*c+money
             else:
              print("no stack")
      
         if(ordered=="2"):
             e = menu["pongal"]
             money = quantity*e+money
         if(ordered=="3"):
              f = menu["idly"]
              money=quantity*f+money
         if(ordered=="4"):
          g = menu["dosa"]
          money=quantity*g+money 
     else:
       print("number not in menu") 
 else:
    totalamount = money
    print(totalamount)
    break
    
