def count_sheeps(sheep):
    try:
        for x in sheep:
            if x == True:
                c1 = sheep.count(x)
        return c1
    except UnboundLocalError:
        return 0