def outer():
    m = 20
    print("this print statement inside the outer method  :  ", m)

    def inner():
        nonlocal m
        m += 1
        print("this print statement inside the inner method  :  ", m)

    inner()
    print(m)

outer()

