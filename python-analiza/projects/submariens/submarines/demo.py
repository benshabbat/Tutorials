def my_fun(demo,*, demo2 ):
    print(demo)
    print(demo2)
    
    
def my_fun2(demo,/,demo2):
    print(demo)
    print(demo2)
    
    
def my_fun3(demo,/,demo2,*,demo3):
    print(demo)
    print(demo2)
    print(demo3)
   
   


# my_fun("demo","demo2")
# my_fun("demo",demo2="demo2")



# my_fun2("b","b")
# my_fun2("b",demo2="b")


# my_fun3("c","c",demo3="c")        
# my_fun3("c","c","c")        