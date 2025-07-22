m = 10
def outer():
    m = 20
    print("this print function just under outer method : ", m)
    def inner():
        m = 30
        print("print function inside the inner method : ", m)

    inner()
    print("calling inner method and print the m value : ", m)
outer()
print("calling the outer method and print the m value : ", m)