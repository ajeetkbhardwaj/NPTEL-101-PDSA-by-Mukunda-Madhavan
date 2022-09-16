def h(x):
    #Initialization of (d,n)
    (d,n) = (1,0)
    # While loop will run until the condition is true
    while d <= x:
        (d,n) = (d*3,n+1)
        print((d,n))
    return(n)