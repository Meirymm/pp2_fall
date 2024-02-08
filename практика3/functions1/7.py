def has_33(number):
    t = False
    for i in range(len(number)- 1):
        if number[i]== 3:
            if number[i+1] == 3:
                t = True
                break
            else:
                continue
    print(t)
has_33([1,3,3])
has_33([1,3,2,3])
has_33([3,1,3])