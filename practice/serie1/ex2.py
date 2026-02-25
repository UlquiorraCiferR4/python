def suite(n,i=0):
    if (n==1):
        return 1
    elif (n==2):
        return 2
    else:
        return 2 *(suite(n)+ suite(n-1))
