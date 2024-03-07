def upper_lower_case(s):
    count = 0
    cout1 = 0
    for x in s:
        if x.isupper():
            count += 1
        else:
            cout1 += 1

    return count, cout1
s = input()
print(upper_lower_case(s))