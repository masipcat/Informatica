def nprimersparells(x):
    if x <= 0:
        print "Valor no valid"
    else:
        i = 1
        p = 0
        while i <= x:
            print i, ": ",p
            i+=1
            p+=2

nprimersparells(80)
