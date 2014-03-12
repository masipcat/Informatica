def matriu():
    j = 0
    while j < 10:
        i = 1
        while i <=10:
            if len(str(j+i)) < 2:
                print "", j+i, "",
            else:
                print j+i, "",
            i+=1
        j+=1
        print # Escriure salt de linia

matriu()
