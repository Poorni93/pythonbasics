#normal function
def buscar(end):
    for i in range(1,end+1):
        if i % 3 == 0 and i % 5 == 0:  
            print("buscar")
        elif i % 3 == 0:  
            print("bus")
        elif i % 5 == 0:  
            print("car")
        else:
            print(i)

# Call the function
buscar(5)

#direct value in argument
def dvfun(quality,name="ppoorni"):
    print(" "+ quality +","+ name +"")

dvfun("good girl")
#direct value also modified
dvfun("very good boy","gunal")

#*arg
def stararg(name,*arg):
    print("output is "+name+"")
    print(arg)

stararg("poorni","first","second")

#keyword arg
def keyarg(**kwargs):
    if 'name' in kwargs:
        print(""+kwargs['name']+"")
    if 'habit' in kwargs:
        print(""+kwargs['habit']+"")
    if 'colour' in kwargs:
        print(""+kwargs['colour']+"")

keyarg(name = "poorni",habit = "good habit")
