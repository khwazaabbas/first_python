
def fun1():
        name = "shahrukh"
        
        def fun2():
            nonlocal name  
            name = "salmaan"  # Modify before using
            print(name)  
        
        fun1()
        print(name)  # Modified value in fun2()
    
fun1()
print(name)  # Unchanged value in fun1()

fun1()