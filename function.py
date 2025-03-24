def buscar(start,end):
    for i in range(start,end):
    
        if(i%3==0):
         print("bus")
        elif(i%5==0):
          print("car")

        else:
           print(i)

    
     
result = buscar(1,17)
print(result)